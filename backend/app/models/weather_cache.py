import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, Text, Integer
from app.core.database import Base


class WeatherCache(Base):
    """Cached agro-meteorological observations and 7-day numerical forecasts."""

    __tablename__ = "weather_cache"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    location_key = Column(String(100), unique=True, index=True, nullable=False)  # "lat_lon" rounded to 2 decimals
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    # Current conditions
    temperature_c = Column(Float, nullable=False)
    temp_max_c = Column(Float, nullable=False)
    temp_min_c = Column(Float, nullable=False)
    humidity_pct = Column(Float, nullable=False)
    wind_speed_m_s = Column(Float, default=2.0)
    rainfall_mm = Column(Float, default=0.0)
    solar_radiation_mj_m2_day = Column(Float, nullable=True)
    et0_mm_day = Column(Float, nullable=False)

    forecast_7day_json = Column(Text, nullable=False)
    cached_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)
