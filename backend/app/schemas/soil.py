from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field


class SoilSampleCreate(BaseModel):
    farm_id: str
    field_parcel_id: Optional[str] = None
    sample_code: str
    depth_cm: float = 15.0

    nitrogen_kg_ha: float = Field(..., ge=0, description="Available Nitrogen (kg/ha)")
    phosphorus_kg_ha: float = Field(..., ge=0, description="Available Phosphorus (kg P2O5/ha)")
    potassium_kg_ha: float = Field(..., ge=0, description="Available Potassium (kg K2O/ha)")

    ph: float = Field(..., ge=3.0, le=12.0)
    electrical_conductivity_ds_m: float = Field(0.6, ge=0.0)
    organic_carbon_pct: float = Field(0.55, ge=0.0, le=10.0)
    texture_class: str = "Loam"
    sand_pct: float = 40.0
    silt_pct: float = 40.0
    clay_pct: float = 20.0

    sulphur_ppm: Optional[float] = None
    zinc_ppm: Optional[float] = None
    boron_ppm: Optional[float] = None
    iron_ppm: Optional[float] = None
    laboratory_name: Optional[str] = "Govt District Soil Testing Lab"
    notes: Optional[str] = None


class SoilSampleResponse(SoilSampleCreate):
    id: str
    sampling_date: datetime
    created_at: datetime

    class Config:
        from_attributes = True


class SoilHealthCardSummary(BaseModel):
    sample_id: str
    sample_code: str
    ph_rating: str
    ph_diagnosis: str
    ec_rating: str
    ec_diagnosis: str
    oc_rating: str
    nitrogen_rating: str
    phosphorus_rating: str
    potassium_rating: str
    texture_class: str
    overall_health_score_pct: float
    amendment_prescription: Optional[str] = None
