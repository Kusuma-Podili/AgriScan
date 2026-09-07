import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, ForeignKey, Boolean, Text
from app.core.database import Base


class AgroAlert(Base):
    """Agronomic alerts for pest outbreaks, frost, heat stress, and irrigation thresholds."""

    __tablename__ = "agro_alerts"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False, index=True)
    farm_id = Column(String(36), ForeignKey("farms.id"), nullable=True, index=True)
    alert_type = Column(String(50), nullable=False)  # pest_disease, frost, heat_stress, moisture_deficit, market_spike
    severity = Column(String(20), default="warning")  # info, watch, warning, critical
    title = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    action_required = Column(Text, nullable=True)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
