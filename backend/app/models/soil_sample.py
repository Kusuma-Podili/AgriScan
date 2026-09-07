import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base


class SoilSample(Base):
    """Laboratory or IoT probe soil chemical and physical test measurement record."""

    __tablename__ = "soil_samples"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    farm_id = Column(String(36), ForeignKey("farms.id"), nullable=False, index=True)
    field_parcel_id = Column(String(36), ForeignKey("field_parcels.id"), nullable=True, index=True)
    sample_code = Column(String(100), unique=True, index=True, nullable=False)
    sampling_date = Column(DateTime, default=datetime.utcnow)
    depth_cm = Column(Float, default=15.0)

    # Primary Macronutrients
    nitrogen_kg_ha = Column(Float, nullable=False)
    phosphorus_kg_ha = Column(Float, nullable=False)
    potassium_kg_ha = Column(Float, nullable=False)

    # Reaction & Physical Properties
    ph = Column(Float, nullable=False)
    electrical_conductivity_ds_m = Column(Float, default=0.6)
    organic_carbon_pct = Column(Float, default=0.55)
    texture_class = Column(String(50), default="Loam")
    sand_pct = Column(Float, default=40.0)
    silt_pct = Column(Float, default=40.0)
    clay_pct = Column(Float, default=20.0)

    # Secondary & Micronutrients (ppm)
    sulphur_ppm = Column(Float, nullable=True)
    zinc_ppm = Column(Float, nullable=True)
    boron_ppm = Column(Float, nullable=True)
    iron_ppm = Column(Float, nullable=True)
    manganese_ppm = Column(Float, nullable=True)
    copper_ppm = Column(Float, nullable=True)

    laboratory_name = Column(String(255), nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    farm = relationship("Farm", back_populates="soil_samples")
    field_parcel = relationship("FieldParcel", back_populates="soil_samples")
    recommendations = relationship("RecommendationLog", back_populates="soil_sample")
