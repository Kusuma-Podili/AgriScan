"""
Integration Test Suite for Controlled Environment Agriculture and Carbon MRV.
"""

import pytest
from app.cea.greenhouse_climate import GreenhouseClimatePhysics, GreenhouseStructureSpecs
from app.cea.hydroponic_recipes import HYDROPONIC_RECIPE_DATABASE, get_hydroponic_recipe
from app.carbon_mrv.ipcc_ghg_calculator import AgriculturalGhgCalculator, FarmGhgActivityInputs
from app.carbon_mrv.rothc_simulator import RothC26_3SoilCarbonModel
from app.carbon_mrv.carbon_project_registry import CARBON_PROJECT_REGISTRY, list_all_carbon_projects


def test_greenhouse_climate_simulation():
    specs = GreenhouseStructureSpecs(
        structure_type="Multi-Span Gothic Arch",
        floor_area_m2=1000.0,
        gutter_height_m=4.5,
        ridge_height_m=6.8,
    )
    model = GreenhouseClimatePhysics(specs)
    step = model.step(ambient_temp_c=32.0, solar_radiation_w_m2=750.0, ambient_rh_pct=45.0)
    assert step.cooling_mode_active is True
    assert step.internal_air_temp_c < 32.0  # Evaporative cooling drops temperature


def test_hydroponic_recipe_database():
    recipe = get_hydroponic_recipe("recipe_tomato_fruiting")
    assert recipe is not None
    assert recipe.target_ec_ds_m > 2.0
    assert recipe.k_ppm > 200.0


def test_ipcc_ghg_emissions_calculator():
    inputs = FarmGhgActivityInputs(
        synthetic_n_fertilizer_applied_kg=1500.0,
        organic_n_manure_applied_kg=500.0,
        crop_residue_n_incorporated_kg=200.0,
        flooded_paddy_area_ha=5.0,
        flooded_paddy_cultivation_days=100,
        paddy_water_regime="multiple_drainage_awd",
        diesel_fuel_consumed_liters=1200.0,
    )
    emissions = AgriculturalGhgCalculator.calculate_emissions(inputs, total_farm_area_ha=10.0)
    assert emissions.direct_n2o_soil_tco2e > 0.0
    assert emissions.flooded_paddy_ch4_tco2e > 0.0
    assert emissions.machinery_diesel_co2_tco2e > 0.0
    assert emissions.total_gross_ghg_emissions_tco2e > 5.0


def test_rothc_soil_carbon_turnover():
    model = RothC26_3SoilCarbonModel(clay_pct=30.0)
    initial_soc = model.stocks.dpm_t_ha + model.stocks.rpm_t_ha + model.stocks.bio_t_ha + model.stocks.hum_t_ha + model.stocks.iom_t_ha

    res = model.step_month(
        month=1, t_mean_c=22.0, precip_mm=65.0, pet_mm=110.0, monthly_c_input_t_ha=0.40, is_vegetated=True
    )
    assert res.total_soc_ton_ha > 0.0
    assert res.co2_released_t_ha > 0.0


def test_carbon_project_registry():
    projects = list_all_carbon_projects()
    assert len(projects) >= 50
    for p in projects:
        assert p.total_enrolled_hectares >= 1000.0
        assert p.cumulative_verified_carbon_credits_tco2e > 0.0
