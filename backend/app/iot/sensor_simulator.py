"""
AgroPulse Virtual IoT Field Sensor Telemetry Simulator.
Simulates multi-depth FDR/TDR capacitance soil probes, EC sensors, and canopy temperature.
"""

import time
import random
from typing import Dict, Any
from pydantic import BaseModel, Field
from app.iot.kalman_filter import SoilTelemetryKalmanFilter


class SensorTelemetryPayload(BaseModel):
    sensor_id: str
    farm_id: str
    field_parcel_id: str
    timestamp_epoch: int
    raw_moisture_vol_pct: float
    filtered_moisture_vol_pct: float
    raw_ec_ds_m: float
    filtered_ec_ds_m: float
    soil_temperature_c: float
    battery_level_pct: float
    is_anomaly: bool = False


class VirtualIoTSensorNode:
    """
    Virtual IoT node generating realistic telemetry with white noise.
    """

    def __init__(self, sensor_id: str, farm_id: str, field_parcel_id: str):
        self.sensor_id = sensor_id
        self.farm_id = farm_id
        self.field_parcel_id = field_parcel_id
        self.moisture_filter = SoilTelemetryKalmanFilter(process_variance_q=1e-3, measurement_variance_r=0.08, initial_value=28.0)
        self.ec_filter = SoilTelemetryKalmanFilter(process_variance_q=1e-4, measurement_variance_r=0.02, initial_value=0.75)
        self.battery = 98.5

    def generate_reading(self, baseline_moisture: float = 28.0, baseline_ec: float = 0.75) -> SensorTelemetryPayload:
        # Add random zero-mean Gaussian measurement noise
        noise_m = random.gauss(0.0, 1.2)
        noise_ec = random.gauss(0.0, 0.08)

        raw_m = max(0.0, min(100.0, baseline_moisture + noise_m))
        raw_ec = max(0.0, baseline_ec + noise_ec)

        filtered_m = self.moisture_filter.update(raw_m)
        filtered_ec = self.ec_filter.update(raw_ec)

        self.battery = max(5.0, self.battery - 0.001)

        is_anom = (filtered_m < 15.0 or filtered_m > 55.0 or filtered_ec > 4.0)

        return SensorTelemetryPayload(
            sensor_id=self.sensor_id,
            farm_id=self.farm_id,
            field_parcel_id=self.field_parcel_id,
            timestamp_epoch=int(time.time()),
            raw_moisture_vol_pct=round(raw_m, 2),
            filtered_moisture_vol_pct=filtered_m,
            raw_ec_ds_m=round(raw_ec, 2),
            filtered_ec_ds_m=filtered_ec,
            soil_temperature_c=round(24.0 + random.uniform(-0.5, 0.5), 1),
            battery_level_pct=round(self.battery, 1),
            is_anomaly=is_anom,
        )
