"""
AgriScan ISOBUS ISO 11783-10 Task Controller & Path Planning Engine.
Implements Variable Rate Application (VRA), Dubins vehicle path kinematics,
and CAN bus J1939 telemetry parsing for connected tractors and implements.
"""

from typing import Dict, List, Tuple, Optional
from pydantic import BaseModel, Field
import numpy as np


class CanBusJ1939Frame(BaseModel):
    timestamp_ms: int
    pgn: int  # Parameter Group Number (e.g., 61444 for EEC1)
    source_address: int
    data_payload_hex: str
    engine_speed_rpm: Optional[float] = None
    engine_torque_pct: Optional[float] = None
    fuel_rate_l_hr: Optional[float] = None
    wheel_speed_km_h: Optional[float] = None
    wheel_slip_pct: Optional[float] = None


class VraGridCellPrescription(BaseModel):
    cell_id: str
    latitude: float
    longitude: float
    target_seed_rate_per_ha: int
    target_n_rate_kg_ha: float
    target_p2o5_rate_kg_ha: float
    target_k2o_rate_kg_ha: float
    calculated_pwm_duty_cycle_pct: float


class VehicleGuidancePoint(BaseModel):
    waypoint_index: int
    x_east_m: float
    y_north_m: float
    heading_deg: float
    curvature_m_inv: float
    swath_pass_number: int


class IsobusTaskController:
    """
    Decodes telemetry and generates variable rate prescription grids.
    """

    @staticmethod
    def decode_j1939_eec1(raw_bytes: List[int]) -> Tuple[float, float]:
        """
        Decodes PGN 61444: Electronic Engine Controller 1 (EEC1)
        Bytes 4-5: Engine Speed (0.125 rpm/bit)
        Byte 3: Actual Engine Percent Torque (1% per bit, -125% offset)
        """
        if len(raw_bytes) < 6:
            return 0.0, 0.0
        torque_pct = float(raw_bytes[2] - 125)
        raw_speed = (raw_bytes[4] << 8) | raw_bytes[3]
        speed_rpm = float(raw_speed * 0.125)
        return speed_rpm, torque_pct

    @staticmethod
    def calculate_pwm_duty_cycle(target_l_ha: float, ground_speed_kmh: float, nozzle_spacing_m: float = 0.5, nozzle_flow_l_min: float = 1.2) -> float:
        """
        Calculates pulse-width modulation duty cycle for target application rate.
        """
        if ground_speed_kmh <= 0.0 or nozzle_flow_l_min <= 0.0:
            return 0.0
        # Required flow per nozzle in L/min = (Target L/ha * Speed km/h * Spacing m) / 60000
        req_flow = (target_l_ha * ground_speed_kmh * nozzle_spacing_m) / 600.0
        duty = (req_flow / nozzle_flow_l_min) * 100.0
        return float(np.clip(duty, 10.0, 100.0))

    @staticmethod
    def generate_dubins_headland_turn(
        start_pt: Tuple[float, float], start_heading: float,
        end_pt: Tuple[float, float], end_heading: float,
        turn_radius_m: float = 6.5
    ) -> List[VehicleGuidancePoint]:
        """
        Generates smooth vehicle turn trajectory between swaths.
        """
        waypoints = []
        steps = 15
        x0, y0 = start_pt
        x1, y1 = end_pt

        for step in range(steps + 1):
            t = step / float(steps)
            # Quadratic Bezier interpolation approximating Dubins curve
            ctrl_x = (x0 + x1) / 2.0 + turn_radius_m * np.sin(np.radians(start_heading))
            ctrl_y = (y0 + y1) / 2.0 + turn_radius_m * np.cos(np.radians(start_heading))

            px = (1.0 - t)**2 * x0 + 2.0 * (1.0 - t) * t * ctrl_x + t**2 * x1
            py = (1.0 - t)**2 * y0 + 2.0 * (1.0 - t) * t * ctrl_y + t**2 * y1
            heading = (start_heading + (end_heading - start_heading) * t) % 360.0

            waypoints.append(
                VehicleGuidancePoint(
                    waypoint_index=step,
                    x_east_m=round(px, 2),
                    y_north_m=round(py, 2),
                    heading_deg=round(heading, 1),
                    curvature_m_inv=round(1.0 / turn_radius_m, 4),
                    swath_pass_number=1,
                )
            )
        return waypoints
