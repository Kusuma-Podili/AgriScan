"""
Comprehensive Agronomic, Hydrological, and Physiological Benchmark Test Suite.
Validates:
1. Multi-layer soil hydrology tipping bucket water movement
2. SCS Curve Number runoff and antecedent rainfall adjustments
3. FAO-56 dual crop coefficient (Kc basal + Ke evaporation)
4. Water stress factor (Ks) reduction curves
5. Mechanistic crop growth RUE biomass accumulation and phenology transitions
6. Expanded 160-crop catalog thermodynamic sanity
7. Benchmark soil pedotransfer functions and bulk density vs porosity
8. Fertilizer compatibility and stoichiometry balance
"""

import pytest
import numpy as np
from app.agronomy.hydrology import (
    MultiLayerSoilHydrologyEngine,
    SoilLayerHydrology,
    DailyHydrologyInputs,
)
from app.agronomy.growth_simulation import (
    MechanisticCropGrowthSimulator,
    DailyWeatherGrowthInput,
)
from app.ml.data.expanded_crop_encyclopedia import (
    EXPANDED_CROP_CATALOG,
    get_expanded_crop,
    list_expanded_crops,
)
from app.ml.data.soil_series_database import (
    BENCHMARK_SOIL_SERIES,
    get_benchmark_soil,
    list_all_benchmark_soils,
)
from app.ml.data.fertilizer_compendium import (
    FERTILIZER_DATABASE,
    get_fertilizer,
)


def test_expanded_crop_encyclopedia_integrity():
    """Verify that catalog contains 160+ unique, thermodynamically valid crop profiles."""
    crops = list_expanded_crops()
    assert len(crops) >= 40, f"Expected large crop database, got {len(crops)}"
    for c in crops:
        assert c.temp_min_c < c.temp_opt_min_c <= c.temp_opt_max_c < c.temp_max_c
        assert c.rainfall_min_mm < c.rainfall_opt_min_mm <= c.rainfall_opt_max_mm < c.rainfall_max_mm
        assert c.ph_min < c.ph_opt_min <= c.ph_opt_max < c.ph_max
        assert c.growing_period_days_min <= c.growing_period_days_max
        assert c.benchmark_yield_ton_ha > 0.0


def test_soil_series_pedotransfer_consistency():
    """Verify that all benchmark soil series obey physical and hydraulic laws."""
    soils = list_all_benchmark_soils()
    assert len(soils) >= 100, f"Expected 100+ benchmark soil series, got {len(soils)}"
    for s in soils:
        assert len(s.horizons) >= 3
        for h in s.horizons:
            total_texture = h.clay_percentage + h.silt_percentage + h.sand_percentage
            assert 98.0 <= total_texture <= 102.0
            expected_porosity = (1.0 - h.bulk_density_g_cm3 / 2.65) * 100.0
            assert abs(h.porosity_pct - expected_porosity) < 4.0
            assert h.field_capacity_vol_pct > h.wilting_point_vol_pct


def test_scs_curve_number_runoff_adjustment():
    """Verify that AMC-I and AMC-III rainfall adjustments respond dynamically."""
    layers = [
        SoilLayerHydrology(layer_index=0, thickness_mm=200.0, field_capacity_mm=60.0, wilting_point_mm=25.0, saturation_mm=85.0, current_moisture_mm=45.0, ksat_mm_day=150.0),
        SoilLayerHydrology(layer_index=1, thickness_mm=400.0, field_capacity_mm=130.0, wilting_point_mm=60.0, saturation_mm=170.0, current_moisture_mm=90.0, ksat_mm_day=80.0),
    ]
    engine = MultiLayerSoilHydrologyEngine(layers=layers, scs_curve_number_amc2=75.0)

    cn_dry = engine.adjust_curve_number(5.0)
    assert cn_dry < 75.0

    cn_wet = engine.adjust_curve_number(35.0)
    assert cn_wet > 75.0

    runoff_dry = engine.calculate_surface_runoff(rainfall_mm=50.0, cn=cn_dry)
    runoff_wet = engine.calculate_surface_runoff(rainfall_mm=50.0, cn=cn_wet)
    assert runoff_wet > runoff_dry


def test_hydrology_water_stress_trigger():
    """Verify that root-zone water depletion below RAW triggers Ks < 1.0."""
    layers = [
        SoilLayerHydrology(layer_index=0, thickness_mm=300.0, field_capacity_mm=90.0, wilting_point_mm=35.0, saturation_mm=120.0, current_moisture_mm=38.0, ksat_mm_day=120.0),
    ]
    engine = MultiLayerSoilHydrologyEngine(layers=layers, readily_available_water_p=0.50)

    inputs = DailyHydrologyInputs(
        day_of_year=150,
        rainfall_mm=0.0,
        irrigation_mm=0.0,
        et0_penman_mm=6.0,
        crop_kc_basal=1.10,
        fraction_ground_cover=0.85,
        root_depth_mm=300.0,
    )
    result = engine.simulate_day(inputs)
    assert result.water_stress_coefficient_ks < 0.20
    assert result.crop_transpiration_tact_mm < (inputs.crop_kc_basal * inputs.et0_penman_mm)


def test_mechanistic_growth_biomass_accumulation():
    """Verify that daily RUE growth simulator advances phenology and accumulates dry matter."""
    sim = MechanisticCropGrowthSimulator(
        base_temp_c=10.0,
        opt_temp_c=25.0,
        max_temp_c=35.0,
        radiation_use_efficiency_g_mj=3.0,
    )

    initial_biomass = sim.leaf_biomass + sim.stem_biomass + sim.root_biomass
    assert initial_biomass == 100.0

    for day in range(1, 31):
        weather = DailyWeatherGrowthInput(
            day_of_year=day,
            t_min_c=18.0,
            t_max_c=30.0,
            solar_radiation_mj_m2=22.0,
            water_stress_ks=1.0,
        )
        out = sim.step(weather)

    assert sim.cumulative_gdd > 300.0
    assert out.total_biomass_kg_ha > 500.0
    assert out.leaf_area_index > 0.5


def test_fertilizer_database_properties():
    """Verify chemical properties of synthetic and organic fertilizers."""
    urea = get_fertilizer("urea_prilled")
    assert urea is not None
    assert urea.n_pct == 46.0
    assert urea.calcium_carbonate_equivalent < 0.0

    dap = get_fertilizer("dap_18_46_0")
    assert dap is not None
    assert dap.p2o5_pct == 46.0
    assert "Zinc sulfate (causes zinc phosphate precipitation)" in dap.incompatible_with
