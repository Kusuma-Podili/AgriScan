from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.models.alert import AgroAlert
from app.iot.sensor_simulator import VirtualIoTSensorNode, SensorTelemetryPayload
from app.api.deps import get_current_user

router = APIRouter()

# In-memory virtual sensor nodes
VIRTUAL_NODES = {
    "node_sensor_01": VirtualIoTSensorNode("node_sensor_01", "farm_demo_1", "parcel_01"),
    "node_sensor_02": VirtualIoTSensorNode("node_sensor_02", "farm_demo_1", "parcel_02"),
}


@router.get("/poll/{sensor_id}", response_model=SensorTelemetryPayload)
def poll_sensor_telemetry(sensor_id: str):
    """Poll latest telemetric measurement from virtual or physical IoT sensor probe."""
    node = VIRTUAL_NODES.get(sensor_id)
    if not node:
        node = VirtualIoTSensorNode(sensor_id, "default_farm", "default_parcel")
        VIRTUAL_NODES[sensor_id] = node

    reading = node.generate_reading()
    return reading


@router.post("/ingest", response_model=SensorTelemetryPayload)
def ingest_sensor_telemetry(
    payload: SensorTelemetryPayload,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Ingest sensor data from field gateway and evaluate anomaly triggers."""
    if payload.filtered_moisture_vol_pct < 18.0:
        alert = AgroAlert(
            user_id=current_user.id,
            farm_id=payload.farm_id,
            alert_type="moisture_deficit",
            severity="critical",
            title=f"Critical Soil Moisture Deficit on Sensor {payload.sensor_id}",
            message=f"Volumetric water content has dropped to {payload.filtered_moisture_vol_pct}%, nearing permanent wilting point.",
            action_required="Initiate scheduled drip irrigation cycle immediately.",
        )
        db.add(alert)
        db.commit()

    return payload
