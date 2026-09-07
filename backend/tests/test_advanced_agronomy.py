"""
Automated Test Suite for Advanced Agronomic Engines.
Validates:
1. Haney Soil Health Score calculations and sodicity classifications
2. Gypsum and Lime requirement formula boundaries
3. Precision fertigation stage partitioning and tank compatibility
4. Soil thermal diffusivity and 1-D damping depth physics
5. Agro-contingency planner rule engine outputs under weather shocks
6. 30-year historical agro-climatic normal integrity
7. Cultivar database schema consistency
"""

import pytest
from app.agronomy.soil_health import (
    SoilHealthEngine,
    SoilHealthTestInputs,
)
from app.agronomy.fertigation_scheduler import (
    PrecisionFertigationScheduler,
    FertigationCropRequirement,
)
from app.agronomy.thermal_microclimate import (
    ThermalMicroclimateModel,
    MicroclimateInputs,
)
from app.agronomy.contingency_planner import (
    AgroContingencyEngine,
    ClimateShockScenario,
)
from app.ml.data.agro_climatic_historical import (
    AGRO_CLIMATIC_STATIONS,
    get_station_normals,
    list_all_stations,
)
from app.ml.data.cultivar_catalog import (
    CULTIVAR_DATABASE,
    get_cultivar,
    list_all_cultivars,
)


def test_soil_health_diagnostic_engine():
    engine = SoilHealthEngine()
    # Test sodic soil scenario
    inputs = SoilHealthTestInputs(
        ph_water=8.8,
        electrical_conductivity_ds_m=2.2,
        organic_matter_pct=0.8,
        total_organic_carbon_ppm=4800.0,
        water_extractable_organic_c_ppm=120.0,
        water_extractable_organic_n_ppm=18.0,
        solvita_co2_c_ppm_24hr=25.0,
        ca_cmol_kg=12.0,
        mg_cmol_kg=6.0,
        k_cmol_kg=1.0,
        na_cmol_kg=5.5,
        bulk_density_g_cm3=1.40,
    )
    res = engine.diagnose(inputs)
    assert res.soil_salinity_sodicity_class == "Sodic Soil (Black Alkali)"
    assert res.exchangeable_sodium_pct_esp > 15.0
    assert res.gypsum_requirement_ton_ha > 0.0
    assert len(res.recommended_interventions) >= 2


def test_fertigation_schedule_generation():
    req = FertigationCropRequirement(
        crop_name="Drip Tomato",
        target_yield_ton_ha=80.0,
        total_n_kg_ha=180.0,
        total_p2o5_kg_ha=90.0,
        total_k2o_kg_ha=240.0,
        crop_cycle_days=100,
        vegetative_days=25,
        flowering_days=25,
        fruiting_days=35,
        maturation_days=15,
    )
    scheduler = PrecisionFertigationScheduler(req)
    sched = scheduler.generate_full_schedule()
    assert len(sched) == 100
    assert sched[0].growth_phase == "Vegetative"
    assert sched[30].growth_phase == "Flowering"
    assert sched[60].growth_phase == "Fruiting"
    assert sched[95].growth_phase == "Maturation"

    # Verify tank separation
    for day in sched:
        assert len(day.stock_tank_a_fertilizers) > 0
        assert len(day.stock_tank_b_fertilizers) > 0


def test_thermal_microclimate_profiling():
    model = ThermalMicroclimateModel()
    inputs = MicroclimateInputs(
        air_temp_mean_c=28.0,
        air_temp_amplitude_c=12.0,
        surface_solar_radiation_mj_m2=24.0,
        soil_moisture_vol_pct=25.0,
        relative_humidity_pct=50.0,
        crop_canopy_cover_fraction=0.80,
    )
    res = model.simulate(inputs)
    assert res.vapor_pressure_deficit_kpa > 0.5
    assert res.damping_depth_cm > 5.0
    assert len(res.depth_temperature_profile) == 5
    # Deeper soil should have attenuated amplitude
    assert res.depth_temperature_profile[0].damping_factor > res.depth_temperature_profile[-1].damping_factor


def test_contingency_planner_shock_scenarios():
    # Delayed monsoon
    shock1 = ClimateShockScenario(
        region_id="punjab_arid",
        target_crop_original="rice_indica",
        planned_sowing_window="June 1-15",
        delay_weeks=5,
    )
    p1 = AgroContingencyEngine.evaluate_shock(shock1)
    assert "Severe Monsoon Delay" in p1.scenario_type
    assert "pearl_millet" in p1.recommended_contingent_crops

    # Mid-season drought
    shock2 = ClimateShockScenario(
        region_id="deccan_vertisol",
        target_crop_original="soybean_yellow",
        planned_sowing_window="July 1",
        dry_spell_duration_days=25,
    )
    p2 = AgroContingencyEngine.evaluate_shock(shock2)
    assert "Drought Break" in p2.scenario_type


def test_agro_climatic_historical_integrity():
    stations = list_all_stations()
    assert len(stations) >= 50
    for s in stations:
        assert len(s.monthly_normals) == 12
        for m in s.monthly_normals:
            assert m.t_min_c <= m.t_mean_c <= m.t_max_c
            assert m.precipitation_mm >= 0.0
            assert m.et0_penman_monteith_mm_day > 0.0


def test_cultivar_registry_consistency():
    cultivars = list_all_cultivars()
    assert len(cultivars) >= 100
    for c in cultivars:
        assert c.release_year >= 1990
        assert c.maturity_days > 50
        assert c.yield_potential_ton_ha > 0.5
