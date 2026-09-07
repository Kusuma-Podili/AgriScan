from typing import List, Optional
from fastapi import APIRouter, Query, HTTPException
from app.schemas.recommendation import RecommendationRequest
from app.ml.agronomy.ssnm_fertilizer import (
    SSNMEngine,
    SoilTestValues,
    FertilizerRecommendationSchedule,
)
from app.ml.data.fertilizer_db import FERTILIZER_DATABASE, FertilizerProduct, list_fertilizers_by_category

router = APIRouter()


@router.get("/catalog", response_model=List[FertilizerProduct])
def list_fertilizer_catalog(category: Optional[str] = None):
    """Retrieve full catalog of commercial and straight fertilizers."""
    if category:
        return list_fertilizers_by_category(category)
    return list(FERTILIZER_DATABASE.values())


@router.post("/calculate-ssnm", response_model=FertilizerRecommendationSchedule)
def calculate_ssnm_schedule(
    crop_id: str = Query(...),
    target_yield_ton_ha: Optional[float] = Query(None),
    strategy: str = Query("dap_urea_mop", description="Formulation: dap_urea_mop or straight_ssp_mop"),
    soil_n: float = Query(280.0),
    soil_p: float = Query(25.0),
    soil_k: float = Query(160.0),
    ph: float = Query(6.8),
    soil_oc: float = Query(0.55),
    soil_ec: float = Query(0.6),
    soil_texture: str = Query("loam"),
    zinc_ppm: Optional[float] = Query(None),
    boron_ppm: Optional[float] = Query(None),
):
    """
    Calculates precision Site-Specific Nutrient Management (SSNM) schedule
    balancing target yield nutrient removal against indigenous soil supply.
    """
    soil = SoilTestValues(
        available_n_kg_ha=soil_n,
        available_p2o5_kg_ha=soil_p,
        available_k2o_kg_ha=soil_k,
        organic_carbon_pct=soil_oc,
        ph=ph,
        electrical_conductivity_ds_m=soil_ec,
        soil_texture=soil_texture,
        zinc_ppm=zinc_ppm,
        boron_ppm=boron_ppm,
    )

    try:
        schedule = SSNMEngine.generate_fertilizer_schedule(
            crop_id=crop_id,
            soil=soil,
            target_yield_ton_ha=target_yield_ton_ha,
            strategy=strategy,
        )
        return schedule
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
