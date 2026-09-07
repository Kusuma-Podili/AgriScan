"""
Integration Test Suite for Telematics and Post-Harvest Grain Storage.
"""

import pytest
from app.telematics.isobus_parser import IsobusTaskController
from app.telematics.canbus_telematics import ISOBUS_DDI_CATALOG, get_isobus_ddi
from app.telematics.tractor_fleet_database import TRACTOR_FLEET_DATABASE, list_all_tractors
from app.post_harvest.grain_drying import GrainDryingThermodynamics
from app.economics.commodity_pricing import COMMODITY_EXCHANGE_REGISTRY, get_commodity_contract


def test_isobus_j1939_telemetry_decoding():
    raw_bytes = [0x00, 0x00, 150, 0x00, 0x20, 0x4E]
    rpm, torque = IsobusTaskController.decode_j1939_eec1(raw_bytes)
    assert torque == 25.0  # 150 - 125
    assert rpm > 0.0


def test_pwm_duty_cycle_for_variable_rate():
    duty = IsobusTaskController.calculate_pwm_duty_cycle(
        target_l_ha=150.0, ground_speed_kmh=12.0, nozzle_spacing_m=0.5, nozzle_flow_l_min=1.8
    )
    assert 10.0 <= duty <= 100.0


def test_dubins_vehicle_path_generation():
    pts = IsobusTaskController.generate_dubins_headland_turn(
        start_pt=(0.0, 0.0), start_heading=0.0, end_pt=(15.0, 0.0), end_heading=180.0, turn_radius_m=6.5
    )
    assert len(pts) == 16
    assert pts[0].heading_deg == 0.0
    assert pts[-1].heading_deg == 180.0


def test_grain_drying_emc_henderson():
    emc = GrainDryingThermodynamics.calculate_emc_henderson("wheat", temp_c=25.0, relative_humidity_pct=65.0)
    assert 12.0 <= emc <= 15.0

    res = GrainDryingThermodynamics.simulate_thin_layer_drying(
        "corn", initial_mc_wb=22.0, drying_temp_c=55.0, ambient_rh_pct=50.0, target_mc_wb=14.0
    )
    assert res.drying_time_hours > 1.0
    assert res.safe_storage_life_days >= 30


def test_tractor_fleet_and_commodity_catalogs():
    tractors = list_all_tractors()
    assert len(tractors) >= 100

    cbot_corn = get_commodity_contract("CBOT_ZC")
    assert cbot_corn is not None
    assert cbot_corn.contract_size == 5000.0
