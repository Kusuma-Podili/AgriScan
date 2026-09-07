from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from app.ml.pipeline.ensemble import CompositeRecommendation
from app.ml.agronomy.ssnm_fertilizer import FertilizerRecommendationSchedule
from app.ml.agronomy.yield_estimator import YieldEstimationReport
from app.ml.agronomy.pest_risk_index import CropPestRiskReport


class RecommendationRequest(BaseModel):
    farm_id: Optional[str] = None
    field_parcel_id: Optional[str] = None
    soil_sample_id: Optional[str] = None

    # Soil Parameters (either supplied or inferred from soil_sample_id)
    n_kg_ha: float = Field(280.0, ge=0)
    p_kg_ha: float = Field(30.0, ge=0)
    k_kg_ha: float = Field(180.0, ge=0)
    ph: float = Field(6.8, ge=3.0, le=12.0)
    organic_carbon_pct: float = Field(0.55, ge=0.0)
    ec_ds_m: float = Field(0.7, ge=0.0)
    soil_texture: str = "loam"

    # Meteorological / Climate Parameters (either supplied or fetched via coordinates)
    temperature_c: float = Field(26.0, ge=-10.0, le=55.0)
    temp_max_c: Optional[float] = None
    temp_min_c: Optional[float] = None
    humidity_pct: float = Field(65.0, ge=5.0, le=100.0)
    rainfall_mm: float = Field(750.0, ge=0.0)
    elevation_m: float = 150.0

    # Operational Preferences
    category_filter: Optional[str] = None  # Cereals, Pulses, Oilseeds, Commercial, Vegetables, Fruits, etc.
    top_k: int = Field(10, ge=1, le=50)
    target_budget_usd_ha: Optional[float] = None


class RecommendationDetailResponse(BaseModel):
    crop_rankings: List[CompositeRecommendation]
    top_crop_fertilizer_schedule: FertilizerRecommendationSchedule
    top_crop_yield_risk_analysis: YieldEstimationReport
    top_crop_pest_alerts: CropPestRiskReport
    ensemble_metadata: Dict[str, Any]
    query_timestamp: datetime


class WhatIfScenarioRequest(BaseModel):
    base_request: RecommendationRequest
    simulated_rainfall_delta_pct: float = Field(0.0, description="% change in rainfall (-50 to +100%)")
    simulated_temperature_delta_c: float = Field(0.0, description="Temperature shift (-5 to +5°C)")
    supplemental_irrigation_mm: float = Field(0.0, ge=0.0)
    additional_fertilizer_budget_pct: float = Field(0.0)


class WhatIfScenarioResponse(BaseModel):
    baseline_top_crop: str
    baseline_suitability: float
    simulated_top_crop: str
    simulated_suitability: float
    rank_changes: List[Dict[str, Any]]
    water_stress_shift_pct: float
    summary_insight: str
