"""
AgroPulse Agro-Meteorological Core: FAO-56 Penman-Monteith Evapotranspiration & GDD Engine.
Strict mathematical implementation conforming to the Food and Agriculture Organization (FAO)
Irrigation and Drainage Paper No. 56 standards.
"""

import math
from typing import Dict, Optional, Tuple
from pydantic import BaseModel, Field


class WeatherInputDaily(BaseModel):
    temp_max_c: float = Field(..., description="Daily maximum temperature in °C")
    temp_min_c: float = Field(..., description="Daily minimum temperature in °C")
    humidity_mean_pct: Optional[float] = Field(None, description="Daily mean relative humidity % (0-100)")
    humidity_max_pct: Optional[float] = Field(None, description="Daily maximum relative humidity %")
    humidity_min_pct: Optional[float] = Field(None, description="Daily minimum relative humidity %")
    wind_speed_m_s: float = Field(2.0, description="Wind speed at 2m height in m/s (default 2.0 m/s if unmeasured)")
    solar_radiation_mj_m2_day: Optional[float] = Field(None, description="Global solar radiation Rs in MJ/m²/day")
    sunshine_hours: Optional[float] = Field(None, description="Actual bright sunshine hours n")
    rainfall_mm: float = Field(0.0, description="Daily total precipitation in mm")
    elevation_m: float = Field(100.0, description="Station elevation above sea level in meters")
    latitude_deg: float = Field(20.0, description="Latitude in decimal degrees (positive North, negative South)")
    day_of_year: int = Field(180, ge=1, le=366, description="Julian day of year (1 to 366)")


class ET0Result(BaseModel):
    et0_mm_day: float = Field(..., description="FAO-56 reference evapotranspiration in mm/day")
    net_radiation_mj_m2_day: float = Field(..., description="Net radiation Rn at the grass surface")
    solar_radiation_rs: float = Field(..., description="Incoming solar radiation Rs (measured or calculated)")
    vapor_pressure_deficit_kpa: float = Field(..., description="Vapor pressure deficit (es - ea)")
    slope_vapor_pressure_kpa_c: float = Field(..., description="Slope of saturation vapor pressure curve Delta")
    psychrometric_constant_kpa_c: float = Field(..., description="Psychrometric constant gamma")
    effective_rainfall_mm: float = Field(..., description="Usable precipitation retained in crop root zone")


class CropEvapotranspirationResult(BaseModel):
    crop_id: str
    stage: str  # initial, mid, end
    kc_applied: float
    et0_mm_day: float
    etc_mm_day: float
    irrigation_deficit_mm_day: float
    effective_rainfall_mm: float


class FAOPenmanMonteith:
    """
    FAO-56 Reference Evapotranspiration Calculator.
    Calculates the rate of evapotranspiration from a hypothetical reference crop
    (well-watered cool-season grass of uniform 0.12 m height, surface resistance 70 s/m, albedo 0.23).
    """

    STEFAN_BOLTZMANN_CONSTANT = 4.903e-9  # MJ / (K^4 * m^2 * day)
    ALBEDO_REFERENCE_GRASS = 0.23

    @staticmethod
    def calculate_atmospheric_pressure(elevation_m: float) -> float:
        """
        Atmospheric pressure P (kPa) as a function of altitude z (m).
        Equation 7 in FAO-56.
        """
        return 101.3 * math.pow((293.0 - 0.0065 * elevation_m) / 293.0, 5.26)

    @staticmethod
    def calculate_psychrometric_constant(pressure_kpa: float) -> float:
        """
        Psychrometric constant gamma (kPa/°C).
        Equation 8 in FAO-56.
        """
        return 0.000665 * pressure_kpa

    @staticmethod
    def calculate_saturation_vapor_pressure(temp_c: float) -> float:
        """
        Saturation vapor pressure e°(T) in kPa at temperature T (°C).
        Equation 11 in FAO-56 (Tetens formula).
        """
        return 0.6108 * math.exp((17.27 * temp_c) / (temp_c + 237.3))

    @classmethod
    def calculate_mean_saturation_vapor_pressure(cls, t_max_c: float, t_min_c: float) -> float:
        """
        Mean saturation vapor pressure es (kPa).
        Equation 12 in FAO-56.
        """
        e_tmax = cls.calculate_saturation_vapor_pressure(t_max_c)
        e_tmin = cls.calculate_saturation_vapor_pressure(t_min_c)
        return (e_tmax + e_tmin) / 2.0

    @classmethod
    def calculate_actual_vapor_pressure(
        cls,
        t_max_c: float,
        t_min_c: float,
        rh_mean_pct: Optional[float] = None,
        rh_max_pct: Optional[float] = None,
        rh_min_pct: Optional[float] = None,
    ) -> float:
        """
        Actual vapor pressure ea (kPa).
        Uses Equations 17, 19, or dewpoint assumption if RH unavailable.
        """
        e_tmax = cls.calculate_saturation_vapor_pressure(t_max_c)
        e_tmin = cls.calculate_saturation_vapor_pressure(t_min_c)

        if rh_max_pct is not None and rh_min_pct is not None:
            # Equation 17 in FAO-56 (Most accurate)
            return ((e_tmin * rh_max_pct / 100.0) + (e_tmax * rh_min_pct / 100.0)) / 2.0
        elif rh_mean_pct is not None:
            # Equation 19 in FAO-56
            es = (e_tmax + e_tmin) / 2.0
            return (rh_mean_pct / 100.0) * es
        else:
            # When humidity data is completely absent, assume Tdew ≈ Tmin in subhumid/humid zones (Equation 48)
            return cls.calculate_saturation_vapor_pressure(t_min_c)

    @classmethod
    def calculate_slope_vapor_pressure_curve(cls, t_mean_c: float) -> float:
        """
        Slope of saturation vapor pressure curve Delta (kPa/°C).
        Equation 13 in FAO-56.
        """
        numerator = 4098.0 * (0.6108 * math.exp((17.27 * t_mean_c) / (t_mean_c + 237.3)))
        denominator = math.pow(t_mean_c + 237.3, 2)
        return numerator / denominator

    @staticmethod
    def calculate_extraterrestrial_radiation(latitude_deg: float, day_of_year: int) -> Tuple[float, float, float]:
        """
        Extraterrestrial radiation Ra (MJ/m²/day), solar declination delta (rad), sunset hour angle omega_s (rad).
        Equations 21, 23, 24, 28 in FAO-56.
        """
        phi = (math.pi / 180.0) * latitude_deg  # Latitude in radians
        # Inverse relative distance Earth-Sun dr (Equation 23)
        dr = 1.0 + 0.033 * math.cos((2.0 * math.pi / 365.0) * day_of_year)
        # Solar declination delta (Equation 24)
        delta = 0.409 * math.sin(((2.0 * math.pi / 365.0) * day_of_year) - 1.39)
        # Sunset hour angle omega_s (Equation 25)
        val = -math.tan(phi) * math.tan(delta)
        # Clamp to [-1, 1] to avoid math domain errors at polar latitudes
        val = max(-1.0, min(1.0, val))
        omega_s = math.acos(val)

        # Extraterrestrial radiation Ra (Equation 21)
        # Solar constant Gsc = 0.0820 MJ/m²/min
        gsc = 0.0820
        ra = ((24.0 * 60.0) / math.pi) * gsc * dr * (
            (omega_s * math.sin(phi) * math.sin(delta)) + (math.cos(phi) * math.cos(delta) * math.sin(omega_s))
        )
        return ra, delta, omega_s

    @classmethod
    def estimate_solar_radiation(
        cls,
        ra: float,
        sunshine_hours: Optional[float] = None,
        omega_s: Optional[float] = None,
        t_max_c: Optional[float] = None,
        t_min_c: Optional[float] = None,
        is_coastal: bool = False,
    ) -> float:
        """
        Incoming global solar radiation Rs (MJ/m²/day).
        Uses Angstrom-Prescott formula (Eq 35) or Hargreaves radiation formula (Eq 50).
        """
        if sunshine_hours is not None and omega_s is not None:
            # Daylight hours N (Equation 34)
            daylight_hours = (24.0 / math.pi) * omega_s
            # Angstrom regression constants as = 0.25, bs = 0.50
            as_const = 0.25
            bs_const = 0.50
            ratio = max(0.0, min(1.0, sunshine_hours / daylight_hours))
            return (as_const + bs_const * ratio) * ra
        elif t_max_c is not None and t_min_c is not None:
            # Hargreaves-Samani radiation formula (Equation 50)
            k_rs = 0.19 if is_coastal else 0.16
            delta_t = max(0.0, t_max_c - t_min_c)
            return k_rs * math.sqrt(delta_t) * ra
        else:
            # Fallback assumption 60% of Ra
            return 0.60 * ra

    @classmethod
    def calculate_net_radiation(
        cls,
        rs: float,
        ra: float,
        elevation_m: float,
        t_max_c: float,
        t_min_c: float,
        ea_kpa: float,
    ) -> float:
        """
        Net radiation Rn (MJ/m²/day) = Rns - Rnl.
        Equations 38-40 in FAO-56.
        """
        # Net solar shortwave radiation Rns (Equation 38)
        rns = (1.0 - cls.ALBEDO_REFERENCE_GRASS) * rs

        # Clear-sky solar radiation Rso (Equation 37)
        rso = (0.75 + (2.0e-5 * elevation_m)) * ra
        if rso <= 0:
            rso = 0.001

        # Relative shortwave radiation ratio Rs / Rso (clamped to [0.3, 1.0])
        rel_rs = max(0.3, min(1.0, rs / rso))

        # Absolute temperatures in Kelvin
        t_max_k4 = math.pow(t_max_c + 273.16, 4)
        t_min_k4 = math.pow(t_min_c + 273.16, 4)
        mean_t_k4 = (t_max_k4 + t_min_k4) / 2.0

        # Net outgoing longwave radiation Rnl (Equation 39)
        rnl = (
            cls.STEFAN_BOLTZMANN_CONSTANT
            * mean_t_k4
            * (0.34 - 0.14 * math.sqrt(max(0.0, ea_kpa)))
            * (1.35 * rel_rs - 0.35)
        )

        return rns - rnl

    @classmethod
    def calculate_daily_et0(cls, inp: WeatherInputDaily) -> ET0Result:
        """
        Computes standard FAO-56 Reference Evapotranspiration (ET0) in mm/day.
        """
        t_mean_c = (inp.temp_max_c + inp.temp_min_c) / 2.0
        pressure_kpa = cls.calculate_atmospheric_pressure(inp.elevation_m)
        gamma = cls.calculate_psychrometric_constant(pressure_kpa)
        delta = cls.calculate_slope_vapor_pressure_curve(t_mean_c)
        es = cls.calculate_mean_saturation_vapor_pressure(inp.temp_max_c, inp.temp_min_c)
        ea = cls.calculate_actual_vapor_pressure(
            inp.temp_max_c, inp.temp_min_c, inp.humidity_mean_pct, inp.humidity_max_pct, inp.humidity_min_pct
        )
        vpd = max(0.0, es - ea)

        ra, _, omega_s = cls.calculate_extraterrestrial_radiation(inp.latitude_deg, inp.day_of_year)

        if inp.solar_radiation_mj_m2_day is not None and inp.solar_radiation_mj_m2_day > 0:
            rs = inp.solar_radiation_mj_m2_day
        else:
            rs = cls.estimate_solar_radiation(
                ra=ra,
                sunshine_hours=inp.sunshine_hours,
                omega_s=omega_s,
                t_max_c=inp.temp_max_c,
                t_min_c=inp.temp_min_c,
            )

        rn = cls.calculate_net_radiation(
            rs=rs,
            ra=ra,
            elevation_m=inp.elevation_m,
            t_max_c=inp.temp_max_c,
            t_min_c=inp.temp_min_c,
            ea_kpa=ea,
        )

        # Soil heat flux G = 0 for daily intervals (Equation 42)
        g = 0.0

        # FAO-56 Penman-Monteith Equation (Equation 6)
        radiation_term = 0.408 * delta * (rn - g)
        wind_aerodynamic_term = gamma * (900.0 / (t_mean_c + 273.0)) * inp.wind_speed_m_s * vpd
        denominator = delta + gamma * (1.0 + 0.34 * inp.wind_speed_m_s)

        et0 = (radiation_term + wind_aerodynamic_term) / denominator
        et0_clamped = max(0.05, et0)

        # Calculate USDA-SCS effective precipitation
        effective_rain = cls.calculate_effective_rainfall_usda(inp.rainfall_mm)

        return ET0Result(
            et0_mm_day=round(et0_clamped, 2),
            net_radiation_mj_m2_day=round(rn, 2),
            solar_radiation_rs=round(rs, 2),
            vapor_pressure_deficit_kpa=round(vpd, 3),
            slope_vapor_pressure_kpa_c=round(delta, 4),
            psychrometric_constant_kpa_c=round(gamma, 4),
            effective_rainfall_mm=round(effective_rain, 2),
        )

    @staticmethod
    def calculate_effective_rainfall_usda(rainfall_mm: float) -> float:
        """
        Calculates USDA Soil Conservation Service (SCS) effective rainfall.
        P_eff represents the fraction of precipitation that infiltrates and remains in the root zone.
        """
        if rainfall_mm <= 0:
            return 0.0
        elif rainfall_mm < 12.5:  # Light surface wetting lost to direct evaporation
            return 0.0
        elif rainfall_mm <= 167.0:
            return (rainfall_mm * (125.0 - 0.2 * rainfall_mm)) / 125.0
        else:
            return (125.0 / 3.0) + (0.1 * rainfall_mm)

    @classmethod
    def calculate_crop_etc(
        cls,
        crop_id: str,
        stage: str,
        kc_value: float,
        weather: WeatherInputDaily,
    ) -> CropEvapotranspirationResult:
        """
        Calculates crop evapotranspiration under standard conditions ETc = Kc * ET0,
        and determines net irrigation water deficit.
        """
        et0_res = cls.calculate_daily_et0(weather)
        etc = kc_value * et0_res.et0_mm_day
        deficit = max(0.0, etc - et0_res.effective_rainfall_mm)

        return CropEvapotranspirationResult(
            crop_id=crop_id,
            stage=stage,
            kc_applied=kc_value,
            et0_mm_day=et0_res.et0_mm_day,
            etc_mm_day=round(etc, 2),
            irrigation_deficit_mm_day=round(deficit, 2),
            effective_rainfall_mm=et0_res.effective_rainfall_mm,
        )


class GrowingDegreeDaysCalculator:
    """
    Computes physiological thermal time accumulation (Growing Degree Days - GDD)
    using base temperature (T_base) and upper threshold cutoff limits.
    """

    @staticmethod
    def calculate_daily_gdd(
        t_max_c: float,
        t_min_c: float,
        t_base_c: float,
        t_upper_cutoff_c: float = 35.0,
        method: str = "standard",
    ) -> float:
        """
        Standard modified thermal accumulation formula:
        GDD = max(0, ((min(T_max, T_upper) + max(T_min, T_base)) / 2) - T_base)
        """
        # Apply biological upper and lower thresholds
        effective_tmax = min(t_max_c, t_upper_cutoff_c)
        effective_tmin = max(t_min_c, t_base_c)

        if effective_tmax < t_base_c:
            return 0.0

        t_mean = (effective_tmax + effective_tmin) / 2.0
        gdd = t_mean - t_base_c
        return max(0.0, round(gdd, 2))
