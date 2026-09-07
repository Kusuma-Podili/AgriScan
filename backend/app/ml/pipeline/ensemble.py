"""
AgroPulse Hybrid Recommendation Ensemble Engine.
Blends multi-model machine learning probabilities (Random Forest, Gradient Boosting, Deep MLP)
with deterministic FAO EcoCrop agronomic boundary checks, yield estimation, and gross margin optimization.
"""

from typing import Dict, List, Optional, Tuple, Any
from pydantic import BaseModel, Field
from app.ml.pipeline.feature_engineering import RawAgroFeatures
from app.ml.classifiers.random_forest import rf_classifier
from app.ml.classifiers.gradient_boosted import gbdt_classifier
from app.ml.classifiers.neural_mlp import neural_mlp_classifier
from app.ml.agronomy.ecocrop_matcher import FAOEcoCropMatcher, EnvironmentalConditions, CropSuitabilityEvaluation
from app.ml.data.crop_database import CROP_DATABASE, CropAgronomicProfile, get_crop_by_id, list_all_crops


class CompositeRecommendation(BaseModel):
    rank: int
    crop_id: str
    crop_name: str
    category: str
    composite_suitability_score: float = Field(..., ge=0.0, le=100.0, description="Blended overall score 0-100%")
    ml_confidence_pct: float
    ecocrop_score: float
    fao_suitability_class: str
    estimated_yield_ton_ha: float
    estimated_gross_revenue_usd_ha: float
    estimated_cultivation_cost_usd_ha: float
    estimated_net_profit_usd_ha: float
    economic_roi_pct: float
    risk_level: str  # Low, Moderate, High, Speculative
    primary_limiting_factor: str
    agronomic_advisory: str


class EnsembleRecommendationResult(BaseModel):
    query_summary: Dict[str, Any]
    recommendations: List[CompositeRecommendation]
    model_weights: Dict[str, float]
    total_evaluated_crops: int


class HybridCropEnsembleEngine:
    """
    Weighted Soft Voting & Stacking Ensemble orchestrator.
    """

    # Weights for ML sub-models
    WEIGHT_RANDOM_FOREST = 0.40
    WEIGHT_GRADIENT_BOOST = 0.35
    WEIGHT_NEURAL_MLP = 0.25

    # Hybrid blending weights between empirical ML and deterministic agronomic EcoCrop laws
    WEIGHT_EMPIRICAL_ML = 0.45
    WEIGHT_DETERMINISTIC_ECOCROP = 0.55

    @classmethod
    def recommend(
        cls,
        raw_features: RawAgroFeatures,
        category_filter: Optional[str] = None,
        top_k: int = 10,
    ) -> EnsembleRecommendationResult:
        """
        Executes hybrid ensemble prediction and agronomic ranking across all crops.
        """
        # 1. Gather Machine Learning Probabilities
        rf_probs = rf_classifier.predict_probabilities(raw_features)
        gbdt_probs = gbdt_classifier.predict_probabilities(raw_features)
        mlp_probs = neural_mlp_classifier.predict_probabilities(raw_features)

        # 2. Convert raw features to EcoCrop Environmental Conditions
        env = EnvironmentalConditions(
            mean_temperature_c=raw_features.temperature_c,
            min_temperature_c=raw_features.temp_min_c,
            max_temperature_c=raw_features.temp_max_c,
            total_rainfall_mm=raw_features.rainfall_mm,
            soil_ph=raw_features.ph,
            soil_salinity_ec_ds_m=raw_features.ec_ds_m,
            soil_texture="loam",
        )

        all_crops = list_all_crops()
        if category_filter:
            all_crops = [c for c in all_crops if c.category.lower() == category_filter.lower().strip()]

        candidates: List[CompositeRecommendation] = []

        for crop in all_crops:
            cid = crop.id

            # Blended ML Probability
            p_rf = rf_probs.get(cid, 0.0)
            p_gbdt = gbdt_probs.get(cid, 0.0)
            p_mlp = mlp_probs.get(cid, 0.0)

            blended_ml_prob = (
                (p_rf * cls.WEIGHT_RANDOM_FOREST)
                + (p_gbdt * cls.WEIGHT_GRADIENT_BOOST)
                + (p_mlp * cls.WEIGHT_NEURAL_MLP)
            )
            ml_score = min(100.0, blended_ml_prob * 100.0 * 2.5)  # Scale up probability into 0-100 space

            # Deterministic EcoCrop Evaluation
            ecocrop_eval = FAOEcoCropMatcher.evaluate_crop(crop, env)
            ecocrop_score = ecocrop_eval.overall_suitability_score

            # If EcoCrop deems the climate lethal (<20%), suppress score completely
            if ecocrop_score < 20.0:
                composite_score = ecocrop_score * 0.5
            else:
                composite_score = (
                    (ml_score * cls.WEIGHT_EMPIRICAL_ML)
                    + (ecocrop_score * cls.WEIGHT_DETERMINISTIC_ECOCROP)
                )

            composite_score = round(max(0.0, min(100.0, composite_score)), 1)

            # Economic & Yield Projections
            yield_factor = composite_score / 100.0
            est_yield = round(crop.benchmark_yield_ton_ha * yield_factor, 2)
            gross_rev = round(est_yield * crop.market_price_usd_per_ton, 1)
            cult_cost = crop.cost_of_cultivation_usd_ha
            net_profit = round(gross_rev - cult_cost, 1)
            roi_pct = round(((net_profit / cult_cost) * 100.0) if cult_cost > 0 else 0.0, 1)

            # Determine Risk Profile
            if crop.risk_volatility_index > 0.35:
                risk_level = "High Volatility (Speculative)"
            elif crop.risk_volatility_index > 0.25:
                risk_level = "Moderate"
            else:
                risk_level = "Low Risk (Stable)"

            candidates.append(
                CompositeRecommendation(
                    rank=0,  # Will assign after sorting
                    crop_id=cid,
                    crop_name=crop.name,
                    category=crop.category,
                    composite_suitability_score=composite_score,
                    ml_confidence_pct=round(min(100.0, ml_score), 1),
                    ecocrop_score=round(ecocrop_score, 1),
                    fao_suitability_class=ecocrop_eval.fao_suitability_class,
                    estimated_yield_ton_ha=est_yield,
                    estimated_gross_revenue_usd_ha=gross_rev,
                    estimated_cultivation_cost_usd_ha=cult_cost,
                    estimated_net_profit_usd_ha=net_profit,
                    economic_roi_pct=roi_pct,
                    risk_level=risk_level,
                    primary_limiting_factor=ecocrop_eval.primary_limiting_factor,
                    agronomic_advisory=crop.agronomic_advisory,
                )
            )

        # Sort descending by composite suitability score
        candidates.sort(key=lambda x: x.composite_suitability_score, reverse=True)

        # Assign ranks
        for idx, item in enumerate(candidates, start=1):
            item.rank = idx

        top_candidates = candidates[:top_k]

        return EnsembleRecommendationResult(
            query_summary={
                "temperature_c": raw_features.temperature_c,
                "rainfall_mm": raw_features.rainfall_mm,
                "soil_ph": raw_features.ph,
                "soil_n": raw_features.n_kg_ha,
                "soil_p": raw_features.p_kg_ha,
                "soil_k": raw_features.k_kg_ha,
            },
            recommendations=top_candidates,
            model_weights={
                "random_forest": cls.WEIGHT_RANDOM_FOREST,
                "gradient_boosting": cls.WEIGHT_GRADIENT_BOOST,
                "deep_neural_mlp": cls.WEIGHT_NEURAL_MLP,
                "ecocrop_deterministic_weight": cls.WEIGHT_DETERMINISTIC_ECOCROP,
            },
            total_evaluated_crops=len(candidates),
        )


crop_ensemble_engine = HybridCropEnsembleEngine()
