import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base


class Farm(Base):
    """Farm holding with geographical parcels, boundaries, and soil characteristics."""

    __tablename__ = "farms"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    owner_id = Column(String(36), ForeignKey("users.id"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    state = Column(String(100), nullable=False)
    district = Column(String(100), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    elevation_m = Column(Float, default=150.0)
    total_area_hectares = Column(Float, nullable=False)
    irrigation_source = Column(String(100), default="Canal / Tube Well")  # Rainfed, Borewell, Canal, Drip, Sprinkler
    soil_type_primary = Column(String(100), default="Loam")
    polygon_geojson = Column(Text, nullable=True)  # GeoJSON representation of boundary polygon
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    owner = relationship("User", back_populates="farms")
    fields = relationship("FieldParcel", back_populates="farm", cascade="all, delete-orphan")
    soil_samples = relationship("SoilSample", back_populates="farm", cascade="all, delete-orphan")


class FieldParcel(Base):
    """Specific subdivided plot or parcel within a farm holding."""

    __tablename__ = "field_parcels"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    farm_id = Column(String(36), ForeignKey("farms.id"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    area_hectares = Column(Float, nullable=False)
    current_crop = Column(String(100), nullable=True)
    sowing_date = Column(DateTime, nullable=True)
    irrigation_system = Column(String(100), default="Drip Irrigation")
    polygon_geojson = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    farm = relationship("Farm", back_populates="fields")
    soil_samples = relationship("SoilSample", back_populates="field_parcel")
