import math
import pytest
from app.ml.agronomy.penman_monteith import (
    FAOPenmanMonteith,
    WeatherInputDaily,
    GrowingDegreeDaysCalculator,
)


def test_fao56_atmospheric_pressure_and_psychrometric():
    """Verify atmospheric pressure and psychrometric constant decay with elevation."""
    # Sea level (0m)
    p_sea = FAOPenmanMonteith.calculate_atmospheric_pressure(0.0)
    assert pytest.approx(p_sea, rel=1e-2) == 101.3

    # High altitude (1800m)
    p_high = FAOPenmanMonteith.calculate_atmospheric_pressure(1800.0)
    assert p_high < p_sea
    assert 80.0 < p_high < 85.0

    # Psychrometric constant at sea level ~ 0.067 kPa/°C
    gamma_sea = FAOPenmanMonteith.calculate_psychrometric_constant(p_sea)
    assert pytest.approx(gamma_sea, abs=0.005) == 0.0674


def test_fao56_penman_monteith_reference_et0():
    """Verify reference evapotranspiration ET0 matches expected empirical ranges."""
    # Typical warm subhumid summer day
    weather = WeatherInputDaily(
        temp_max_c=34.0,
        temp_min_c=22.0,
        humidity_mean_pct=60.0,
        wind_speed_m_s=2.5,
        solar_radiation_mj_m2_day=22.0,
        rainfall_mm=0.0,
        elevation_m=120.0,
        latitude_deg=22.5,
        day_of_year=180,
    )
    result = FAOPenmanMonteith.calculate_daily_et0(weather)

    # In summer conditions at 34°C with high solar radiation, ET0 typically ranges 5.0 to 7.5 mm/day
    assert 4.5 <= result.et0_mm_day <= 8.5
    assert result.net_radiation_mj_m2_day > 0
    assert result.vapor_pressure_deficit_kpa > 0


def test_usda_effective_rainfall():
    """Verify USDA Soil Conservation Service effective precipitation calculations."""
    # Zero or negligible rain gives 0 effective rain
    assert FAOPenmanMonteith.calculate_effective_rainfall_usda(0.0) == 0.0
    assert FAOPenmanMonteith.calculate_effective_rainfall_usda(8.0) == 0.0

    # Moderate rain: 50mm rain -> ~46mm effective
    eff_50 = FAOPenmanMonteith.calculate_effective_rainfall_usda(50.0)
    assert 40.0 <= eff_50 <= 48.0

    # Heavy rain: 200mm rain -> runoff fraction increases
    eff_200 = FAOPenmanMonteith.calculate_effective_rainfall_usda(200.0)
    assert eff_200 < 200.0


def test_growing_degree_days():
    """Verify thermal accumulation (GDD) with base temperature and cutoff."""
    # Wheat (T_base = 4.5°C): Max 22°C, Min 10°C -> Mean 16°C -> GDD = 11.5
    gdd_wheat = GrowingDegreeDaysCalculator.calculate_daily_gdd(
        t_max_c=22.0, t_min_c=10.0, t_base_c=4.5
    )
    assert pytest.approx(gdd_wheat, abs=0.1) == 11.5

    # Freezing day: Max 2°C, Min -5°C -> Below base -> GDD = 0
    gdd_cold = GrowingDegreeDaysCalculator.calculate_daily_gdd(
        t_max_c=2.0, t_min_c=-5.0, t_base_c=5.0
    )
    assert gdd_cold == 0.0
