from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class FieldParcelBase(BaseModel):
    name: str
    area_hectares: float = Field(..., gt=0)
    current_crop: Optional[str] = None
    sowing_date: Optional[datetime] = None
    irrigation_system: str = "Drip Irrigation"
    polygon_geojson: Optional[str] = None


class FieldParcelCreate(FieldParcelBase):
    farm_id: Optional[str] = None


class FieldParcelResponse(FieldParcelBase):
    id: str
    farm_id: str
    created_at: datetime

    class Config:
        from_attributes = True


class FarmBase(BaseModel):
    name: str
    state: str
    district: str
    latitude: float = Field(..., ge=-90.0, le=90.0)
    longitude: float = Field(..., ge=-180.0, le=180.0)
    elevation_m: float = 150.0
    total_area_hectares: float = Field(..., gt=0)
    irrigation_source: str = "Canal / Tube Well"
    soil_type_primary: str = "Loam"
    polygon_geojson: Optional[str] = None


class FarmCreate(FarmBase):
    pass


class FarmUpdate(BaseModel):
    name: Optional[str] = None
    total_area_hectares: Optional[float] = None
    irrigation_source: Optional[str] = None
    soil_type_primary: Optional[str] = None
    polygon_geojson: Optional[str] = None


class FarmResponse(FarmBase):
    id: str
    owner_id: str
    created_at: datetime
    fields: List[FieldParcelResponse] = []

    class Config:
        from_attributes = True
