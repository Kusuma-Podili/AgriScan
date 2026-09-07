import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base


class RecommendationLog(Base):
    """Archival log of crop recommendation queries, ML inferences, and farmer decisions."""

    __tablename__ = "recommendation_logs"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False, index=True)
    soil_sample_id = Column(String(36), ForeignKey("soil_samples.id"), nullable=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Input snapshot
    temperature_c = Column(Float, nullable=False)
    rainfall_mm = Column(Float, nullable=False)
    soil_n = Column(Float, nullable=False)
    soil_p = Column(Float, nullable=False)
    soil_k = Column(Float, nullable=False)
    soil_ph = Column(Float, nullable=False)

    # Results snapshot
    top_recommended_crop_id = Column(String(100), nullable=False)
    top_recommended_crop_name = Column(String(100), nullable=False)
    suitability_score = Column(Float, nullable=False)
    fao_class = Column(String(50), nullable=False)
    projected_yield_ton_ha = Column(Float, nullable=False)
    estimated_profit_usd_ha = Column(Float, nullable=False)

    # Full JSON serializations
    full_ranking_json = Column(Text, nullable=False)
    fertilizer_advisory_json = Column(Text, nullable=False)

    status = Column(String(50), default="completed")
    user_selected_crop = Column(String(100), nullable=True)

    # Relationships
    user = relationship("User", back_populates="recommendations")
    soil_sample = relationship("SoilSample", back_populates="recommendations")
