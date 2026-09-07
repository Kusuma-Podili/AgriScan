import json
from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.models.recommendation_log import RecommendationLog
from app.models.soil_sample import SoilSample
from app.schemas.recommendation import (
    RecommendationRequest,
    RecommendationDetailResponse,
    WhatIfScenarioRequest,
    WhatIfScenarioResponse,
)
from app.ml.pipeline.feature_engineering import RawAgroFeatures
from app.ml.pipeline.ensemble import crop_ensemble_engine
from app.ml.agronomy.ssnm_fertilizer import SSNMEngine, SoilTestValues
from app.ml.agronomy.yield_estimator import YieldResponseSimulator
from app.ml.agronomy.pest_risk_index import PestRiskForecaster, CurrentMicroclimate
from app.api.deps import get_current_user

router = APIRouter()


@router.post("/run", response_model=RecommendationDetailResponse)
def run_crop_recommendation(
    req: RecommendationRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Executes precision crop recommendation combining multi-model ML and FAO EcoCrop suitability.
    Computes SSNM fertilizer schedules, Bayesian yield projections, and pest alerts for top crops.
    """
    # If soil_sample_id was provided, override soil parameters with verified lab measurements
    n_val = req.n_kg_ha
    p_val = req.p_kg_ha
    k_val = req.k_kg_ha
    ph_val = req.ph
    oc_val = req.organic_carbon_pct
    ec_val = req.ec_ds_m
    text_val = req.soil_texture

    if req.soil_sample_id:
        sample = db.query(SoilSample).filter(SoilSample.id == req.soil_sample_id).first()
        if sample:
            n_val = sample.nitrogen_kg_ha
            p_val = sample.phosphorus_kg_ha
            k_val = sample.potassium_kg_ha
            ph_val = sample.ph
            oc_val = sample.organic_carbon_pct
            ec_val = sample.electrical_conductivity_ds_m
            text_val = sample.texture_class

    raw_features = RawAgroFeatures(
        n_kg_ha=n_val,
        p_kg_ha=p_val,
        k_kg_ha=k_val,
        ph=ph_val,
        organic_carbon_pct=oc_val,
        ec_ds_m=ec_val,
        sand_pct=40.0,
        clay_pct=25.0,
        temperature_c=req.temperature_c,
        temp_max_c=req.temp_max_c,
        temp_min_c=req.temp_min_c,
        humidity_pct=req.humidity_pct,
        rainfall_mm=req.rainfall_mm,
        elevation_m=req.elevation_m,
    )

    # 1. Run Ensemble Crop Recommendation
    ensemble_res = crop_ensemble_engine.recommend(
        raw_features=raw_features,
        category_filter=req.category_filter,
        top_k=req.top_k,
    )

    if not ensemble_res.recommendations:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="No crops met the viability criteria for the supplied soil and climate parameters.",
        )

    top_rec = ensemble_res.recommendations[0]

    # 2. Compute SSNM Fertilizer Schedule for top recommended crop
    soil_tests = SoilTestValues(
        available_n_kg_ha=n_val,
        available_p2o5_kg_ha=p_val,
        available_k2o_kg_ha=k_val,
        organic_carbon_pct=oc_val,
        ph=ph_val,
        electrical_conductivity_ds_m=ec_val,
        soil_texture=text_val,
    )
    fert_schedule = SSNMEngine.generate_fertilizer_schedule(
        crop_id=top_rec.crop_id,
        soil=soil_tests,
        target_yield_ton_ha=top_rec.estimated_yield_ton_ha,
    )

    # 3. Run Monte Carlo Yield Sensitivity Analysis
    yield_report = YieldResponseSimulator.run_monte_carlo_simulation(
        crop_id=top_rec.crop_id,
        soil_n=n_val,
        soil_p=p_val,
        soil_k=k_val,
        rainfall_mm=req.rainfall_mm,
        mean_temp_c=req.temperature_c,
    )

    # 4. Generate Pest and Disease Microclimatic Alerts
    pest_report = PestRiskForecaster.evaluate_crop_risks(
        crop_id=top_rec.crop_id,
        weather=CurrentMicroclimate(
            temperature_c=req.temperature_c,
            humidity_pct=req.humidity_pct,
            rainfall_mm=req.rainfall_mm / 120.0,  # daily average
        ),
    )

    # 5. Log Recommendation in Database
    rec_log = RecommendationLog(
        user_id=current_user.id,
        soil_sample_id=req.soil_sample_id,
        temperature_c=req.temperature_c,
        rainfall_mm=req.rainfall_mm,
        soil_n=n_val,
        soil_p=p_val,
        soil_k=k_val,
        soil_ph=ph_val,
        top_recommended_crop_id=top_rec.crop_id,
        top_recommended_crop_name=top_rec.crop_name,
        suitability_score=top_rec.composite_suitability_score,
        fao_class=top_rec.fao_suitability_class,
        projected_yield_ton_ha=top_rec.estimated_yield_ton_ha,
        estimated_profit_usd_ha=top_rec.estimated_net_profit_usd_ha,
        full_ranking_json=json.dumps([r.model_dump() for r in ensemble_res.recommendations]),
        fertilizer_advisory_json=json.dumps(fert_schedule.model_dump()),
    )
    db.add(rec_log)
    db.commit()

    return RecommendationDetailResponse(
        crop_rankings=ensemble_res.recommendations,
        top_crop_fertilizer_schedule=fert_schedule,
        top_crop_yield_risk_analysis=yield_report,
        top_crop_pest_alerts=pest_report,
        ensemble_metadata=ensemble_res.model_weights,
        query_timestamp=datetime.utcnow(),
    )


@router.post("/quick", response_model=RecommendationDetailResponse)
def quick_crop_recommendation(req: RecommendationRequest):
    """
    Public precision crop recommendation endpoint for interactive web dashboard.
    Combines multi-model ML ensemble (Random Forest, GBDT, Neural MLP) and FAO EcoCrop suitability.
    Computes SSNM fertilizer schedules, Bayesian yield projections, and pest alerts for top crops.
    """
    raw_features = RawAgroFeatures(
        n_kg_ha=req.n_kg_ha,
        p_kg_ha=req.p_kg_ha,
        k_kg_ha=req.k_kg_ha,
        ph=req.ph,
        organic_carbon_pct=req.organic_carbon_pct,
        ec_ds_m=req.ec_ds_m,
        sand_pct=40.0,
        clay_pct=25.0,
        temperature_c=req.temperature_c,
        temp_max_c=req.temp_max_c,
        temp_min_c=req.temp_min_c,
        humidity_pct=req.humidity_pct,
        rainfall_mm=req.rainfall_mm,
        elevation_m=req.elevation_m,
    )

    ensemble_res = crop_ensemble_engine.recommend(
        raw_features=raw_features,
        category_filter=req.category_filter,
        top_k=req.top_k,
    )

    if not ensemble_res.recommendations:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="No crops met the viability criteria for the supplied soil and climate parameters.",
        )

    top_rec = ensemble_res.recommendations[0]

    soil_tests = SoilTestValues(
        available_n_kg_ha=req.n_kg_ha,
        available_p2o5_kg_ha=req.p_kg_ha,
        available_k2o_kg_ha=req.k_kg_ha,
        organic_carbon_pct=req.organic_carbon_pct,
        ph=req.ph,
        electrical_conductivity_ds_m=req.ec_ds_m,
        soil_texture=req.soil_texture,
    )
    fert_schedule = SSNMEngine.generate_fertilizer_schedule(
        crop_id=top_rec.crop_id,
        soil=soil_tests,
        target_yield_ton_ha=top_rec.estimated_yield_ton_ha,
    )

    yield_report = YieldResponseSimulator.run_monte_carlo_simulation(
        crop_id=top_rec.crop_id,
        soil_n=req.n_kg_ha,
        soil_p=req.p_kg_ha,
        soil_k=req.k_kg_ha,
        rainfall_mm=req.rainfall_mm,
        mean_temp_c=req.temperature_c,
    )

    pest_report = PestRiskForecaster.evaluate_crop_risks(
        crop_id=top_rec.crop_id,
        weather=CurrentMicroclimate(
            temperature_c=req.temperature_c,
            humidity_pct=req.humidity_pct,
            rainfall_mm=req.rainfall_mm / 120.0,
        ),
    )

    return RecommendationDetailResponse(
        crop_rankings=ensemble_res.recommendations,
        top_crop_fertilizer_schedule=fert_schedule,
        top_crop_yield_risk_analysis=yield_report,
        top_crop_pest_alerts=pest_report,
        ensemble_metadata=ensemble_res.model_weights,
        query_timestamp=datetime.utcnow(),
    )


@router.post("/what-if", response_model=WhatIfScenarioResponse)
def simulate_what_if_scenario(
    scenario: WhatIfScenarioRequest,
    current_user: User = Depends(get_current_user),
):
    """
    Real-time interactive What-If scenario simulator.
    Modulates rainfall, temperature shifts, or irrigation depth to observe crop ranking shifts.
    """
    base = scenario.base_request

    # Baseline run
    base_raw = RawAgroFeatures(
        n_kg_ha=base.n_kg_ha,
        p_kg_ha=base.p_kg_ha,
        k_kg_ha=base.k_kg_ha,
        ph=base.ph,
        temperature_c=base.temperature_c,
        humidity_pct=base.humidity_pct,
        rainfall_mm=base.rainfall_mm,
    )
    base_res = crop_ensemble_engine.recommend(base_raw, top_k=5)
    base_top = base_res.recommendations[0]

    # Adjusted climate trajectory
    sim_rain = max(0.0, (base.rainfall_mm * (1.0 + scenario.simulated_rainfall_delta_pct / 100.0)) + scenario.supplemental_irrigation_mm)
    sim_temp = base.temperature_c + scenario.simulated_temperature_delta_c

    sim_raw = RawAgroFeatures(
        n_kg_ha=base.n_kg_ha * (1.0 + scenario.additional_fertilizer_budget_pct / 100.0),
        p_kg_ha=base.p_kg_ha * (1.0 + scenario.additional_fertilizer_budget_pct / 100.0),
        k_kg_ha=base.k_kg_ha * (1.0 + scenario.additional_fertilizer_budget_pct / 100.0),
        ph=base.ph,
        temperature_c=sim_temp,
        humidity_pct=min(95.0, base.humidity_pct + (scenario.simulated_rainfall_delta_pct * 0.15)),
        rainfall_mm=sim_rain,
    )
    sim_res = crop_ensemble_engine.recommend(sim_raw, top_k=5)
    sim_top = sim_res.recommendations[0]

    rank_changes = []
    for rank, rec in enumerate(sim_res.recommendations, start=1):
        rank_changes.append({
            "crop_id": rec.crop_id,
            "crop_name": rec.crop_name,
            "new_rank": rank,
            "new_suitability_score": rec.composite_suitability_score,
        })

    # Summary insight
    rain_diff = sim_rain - base.rainfall_mm
    temp_diff = scenario.simulated_temperature_delta_c
    insight = (
        f"Under {rain_diff:+.1f} mm water shift and {temp_diff:+.1f}°C temperature delta, "
        f"top recommendation transitioned from {base_top.crop_name} ({base_top.composite_suitability_score}%) "
        f"to {sim_top.crop_name} ({sim_top.composite_suitability_score}%)."
    )

    return WhatIfScenarioResponse(
        baseline_top_crop=base_top.crop_name,
        baseline_suitability=base_top.composite_suitability_score,
        simulated_top_crop=sim_top.crop_name,
        simulated_suitability=sim_top.composite_suitability_score,
        rank_changes=rank_changes,
        water_stress_shift_pct=round(((sim_rain - base.rainfall_mm) / max(1.0, base.rainfall_mm)) * 100.0, 1),
        summary_insight=insight,
    )


@router.post("/what-if/quick", response_model=WhatIfScenarioResponse)
def quick_what_if_scenario(scenario: WhatIfScenarioRequest):
    """
    Public interactive What-If scenario simulation for the web dashboard.
    """
    base = scenario.base_request

    # Baseline run
    base_raw = RawAgroFeatures(
        n_kg_ha=base.n_kg_ha,
        p_kg_ha=base.p_kg_ha,
        k_kg_ha=base.k_kg_ha,
        ph=base.ph,
        temperature_c=base.temperature_c,
        humidity_pct=base.humidity_pct,
        rainfall_mm=base.rainfall_mm,
    )
    base_res = crop_ensemble_engine.recommend(base_raw, top_k=5)
    base_top = base_res.recommendations[0]

    # Adjusted climate trajectory
    sim_rain = max(0.0, (base.rainfall_mm * (1.0 + scenario.simulated_rainfall_delta_pct / 100.0)) + scenario.supplemental_irrigation_mm)
    sim_temp = base.temperature_c + scenario.simulated_temperature_delta_c

    sim_raw = RawAgroFeatures(
        n_kg_ha=base.n_kg_ha * (1.0 + scenario.additional_fertilizer_budget_pct / 100.0),
        p_kg_ha=base.p_kg_ha * (1.0 + scenario.additional_fertilizer_budget_pct / 100.0),
        k_kg_ha=base.k_kg_ha * (1.0 + scenario.additional_fertilizer_budget_pct / 100.0),
        ph=base.ph,
        temperature_c=sim_temp,
        humidity_pct=min(95.0, base.humidity_pct + (scenario.simulated_rainfall_delta_pct * 0.15)),
        rainfall_mm=sim_rain,
    )
    sim_res = crop_ensemble_engine.recommend(sim_raw, top_k=5)
    sim_top = sim_res.recommendations[0]

    rank_changes = []
    for rank, rec in enumerate(sim_res.recommendations, start=1):
        rank_changes.append({
            "crop_id": rec.crop_id,
            "crop_name": rec.crop_name,
            "new_rank": rank,
            "new_suitability_score": rec.composite_suitability_score,
        })

    # Summary insight
    rain_diff = sim_rain - base.rainfall_mm
    temp_diff = scenario.simulated_temperature_delta_c
    insight = (
        f"Under {rain_diff:+.1f} mm water shift and {temp_diff:+.1f}°C temperature delta, "
        f"top recommendation transitioned from {base_top.crop_name} ({base_top.composite_suitability_score}%) "
        f"to {sim_top.crop_name} ({sim_top.composite_suitability_score}%)."
    )

    return WhatIfScenarioResponse(
        baseline_top_crop=base_top.crop_name,
        baseline_suitability=base_top.composite_suitability_score,
        simulated_top_crop=sim_top.crop_name,
        simulated_suitability=sim_top.composite_suitability_score,
        rank_changes=rank_changes,
        water_stress_shift_pct=round(((sim_rain - base.rainfall_mm) / max(1.0, base.rainfall_mm)) * 100.0, 1),
        summary_insight=insight,
    )

