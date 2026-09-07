"""
AgriScan Supply Chain, Cold Chain Logistics, and Actuarial Insurance Unit Tests.
"""

from datetime import datetime
import pytest
from app.supply_chain.traceability_engine import (
    FarmTraceabilityEngine,
    EPCISEvent,
    EPCISEventType,
    SupplyChainAction,
    BusinessStep,
    DispositionStatus,
    SensorReading,
)
from app.supply_chain.cold_chain_telematics import ColdChainThermodynamics
from app.supply_chain.storage_facility_catalog import list_all_storage_facilities, get_storage_facility
from app.actuarial.crop_insurance_models import (
    AgriculturalActuarialEngine,
    AreaYieldPolicyConfig,
    WeatherIndexTrigger,
)
from app.actuarial.peril_risk_database import list_all_peril_zones, get_peril_zone


def test_epcis_harvest_to_retail_traceability():
    engine = FarmTraceabilityEngine()
    lot = "LOT_2026_APL_8890"

    # Event 1: Harvest
    ev1 = EPCISEvent(
        event_id="EV_001",
        event_type=EPCISEventType.OBJECT_EVENT,
        action=SupplyChainAction.ADD,
        business_step=BusinessStep.HARVESTING,
        disposition=DispositionStatus.IN_PROGRESS,
        event_time=datetime(2026, 9, 1, 6, 0),
        read_point_gln="0841234000101",
        biz_location_gln="0841234000101",
        lot_number=lot,
        crop_variety="Honeycrisp Apple",
        quantity_kg=2400.0,
    )
    engine.register_event(ev1)

    # Event 2: Cooling & Packing
    ev2 = EPCISEvent(
        event_id="EV_002",
        event_type=EPCISEventType.OBJECT_EVENT,
        action=SupplyChainAction.OBSERVE,
        business_step=BusinessStep.COOLING,
        disposition=DispositionStatus.CONFORMING,
        event_time=datetime(2026, 9, 1, 14, 0),
        read_point_gln="0841234000102",
        biz_location_gln="0841234000102",
        lot_number=lot,
        sensor_telemetry=[
            SensorReading(sensor_type="Temperature", reading_value=1.5, uom="degC", recorded_at=datetime(2026, 9, 1, 14, 0), within_safe_threshold=True)
        ],
    )
    engine.register_event(ev2)

    trace = engine.trace_batch(lot)
    assert trace is not None
    assert trace.total_events == 2
    assert trace.provenance_verified is True
    assert trace.haccp_compliant is True
    assert trace.critical_temperature_excursions == 0


def test_cold_chain_shelf_life_kinetics():
    res = ColdChainThermodynamics.simulate_transit_quality(
        crop="apple",
        transit_hours=72.0,
        mean_reefer_temp_c=1.0,
        temp_excursion_hours=4.0,
        excursion_temp_c=15.0,
    )
    assert res.effective_shelf_life_days_remaining > 100.0
    assert res.shelf_life_loss_pct < 15.0
    assert res.chilling_injury_risk is False
    assert res.respiration_heat_generated_kj_ton > 0.0
    assert res.reefer_cooling_load_kw_ton > 0.0


def test_cold_storage_facility_catalog():
    facs = list_all_storage_facilities()
    assert len(facs) >= 200
    fac1 = get_storage_facility("FAC_US_CA_001")
    assert fac1 is not None
    assert fac1.storage_type == "Controlled Atmosphere (CA)"
    assert fac1.capacity_metric_tons > 10000.0


def test_actuarial_area_yield_insurance_pricing():
    cfg = AreaYieldPolicyConfig(
        policy_id="POL_IA_CRN_2026",
        crop_name="Corn",
        historical_county_yields=[9.8, 10.5, 11.2, 8.4, 11.8, 10.9, 12.1, 9.2, 11.5, 12.4],
        coverage_level_pct=85.0,
        projected_price_usd_per_ton=220.0,
        insured_hectares=150.0,
    )
    quote = AgriculturalActuarialEngine.quote_area_yield_insurance(cfg)
    assert quote.guaranteed_yield_ton_ha > 8.0
    assert quote.pure_risk_premium_rate_pct > 1.0
    assert quote.gross_premium_usd_ha > quote.pure_premium_usd_ha
    assert quote.total_premium_payable_usd > 0.0
    assert quote.max_liability_usd > 100000.0


def test_weather_index_insurance_drought_payout():
    trig = WeatherIndexTrigger(
        peril_name="Agricultural Drought",
        trigger_threshold_value=250.0,  # mm
        exit_threshold_value=120.0,    # mm (100% max payout)
        max_sum_insured_usd_per_ha=800.0,
        unit_of_measure="mm",
    )
    # Scenario 1: Rainfall = 300 mm (No drought, 0 payout)
    p1, tot1 = AgriculturalActuarialEngine.evaluate_weather_index_payout(trig, realized_index_value=300.0, insured_hectares=50.0)
    assert p1 == 0.0
    assert tot1 == 0.0

    # Scenario 2: Rainfall = 185 mm (Mid drought payout)
    p2, tot2 = AgriculturalActuarialEngine.evaluate_weather_index_payout(trig, realized_index_value=185.0, insured_hectares=50.0)
    assert p2 == 400.0
    assert tot2 == 20000.0

    # Scenario 3: Extreme drought = 100 mm (100% exit payout)
    p3, tot3 = AgriculturalActuarialEngine.evaluate_weather_index_payout(trig, realized_index_value=100.0, insured_hectares=50.0)
    assert p3 == 800.0
    assert tot3 == 40000.0


def test_peril_risk_database_zones():
    zones = list_all_peril_zones()
    assert len(zones) >= 200
    z = get_peril_zone("ZON_US_IA_001")
    assert z is not None
    assert z.major_crop == "Corn"
    assert len(z.ten_year_historical_yields_ton_ha) == 10
