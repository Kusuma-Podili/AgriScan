from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, Field


class DailyForecast(BaseModel):
    forecast_date: date
    temp_max_c: float
    temp_min_c: float
    humidity_pct: float
    rainfall_prob_pct: float
    expected_rainfall_mm: float
    wind_speed_m_s: float
    et0_mm_day: float
    condition_summary: str  # Sunny, Scattered Showers, Heavy Rain, etc.
    heat_stress_alert: bool = False
    frost_alert: bool = False


class WeatherCurrentResponse(BaseModel):
    latitude: float
    longitude: float
    temperature_c: float
    temp_max_c: float
    temp_min_c: float
    humidity_pct: float
    wind_speed_m_s: float
    rainfall_mm: float
    et0_reference_mm_day: float
    condition: str
    observed_at: datetime
    forecast_7day: List[DailyForecast]


class IrrigationAdvisoryResponse(BaseModel):
    crop_id: str
    growth_stage: str
    current_et0_mm_day: float
    crop_coefficient_kc: float
    crop_evapotranspiration_etc_mm_day: float
    effective_rainfall_mm: float
    net_irrigation_depth_mm: float
    recommended_drip_runtime_hours: float
    irrigation_urgency: str  # Critical, Recommended, Adequate, None (Saturated)
    soil_moisture_depletion_pct: float
