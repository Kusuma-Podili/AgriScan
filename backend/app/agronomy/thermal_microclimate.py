"""
AgroPulse Soil Thermal Diffusion & Boundary Layer Microclimate Profiler.
Simulates 1-D soil heat conduction, damping depth, diurnal surface temperature amplitude,
canopy temperature depression (CTD), and vapor pressure deficit (VPD).
"""

from typing import List, Dict, Tuple
from pydantic import BaseModel, Field
import numpy as np


class MicroclimateInputs(BaseModel):
    air_temp_mean_c: float
    air_temp_amplitude_c: float
    surface_solar_radiation_mj_m2: float
    soil_bulk_density_g_cm3: float = 1.35
    soil_moisture_vol_pct: float = 22.0
    relative_humidity_pct: float = 65.0
    crop_canopy_cover_fraction: float = 0.70


class SoilDepthTemperature(BaseModel):
    depth_cm: float
    t_min_c: float
    t_max_c: float
    t_mean_c: float
    damping_factor: float


class MicroclimateDiagnostics(BaseModel):
    vapor_pressure_deficit_kpa: float
    dew_point_temp_c: float
    canopy_temperature_c: float
    canopy_temperature_depression_c: float
    soil_thermal_diffusivity_m2_s: float
    damping_depth_cm: float
    depth_temperature_profile: List[SoilDepthTemperature]


class ThermalMicroclimateModel:
    """
    Computes soil temperature wave attenuation with depth using Fourier's heat law.
    T(z, t) = T_mean + A_0 * exp(-z / D) * sin(omega * t - z / D)
    """

    @staticmethod
    def calculate_vapor_pressure_deficit(t_air: float, rh: float) -> Tuple[float, float]:
        """
        Tetens formula for saturation vapor pressure es(T) in kPa.
        """
        es = 0.61078 * np.exp((17.27 * t_air) / (t_air + 237.3))
        ea = es * (rh / 100.0)
        vpd = max(0.0, es - ea)
        dew_point = (237.3 * np.log(ea / 0.61078)) / (17.27 - np.log(ea / 0.61078))
        return float(round(vpd, 2)), float(round(dew_point, 1))

    @staticmethod
    def calculate_soil_thermal_diffusivity(moisture_vol_pct: float, bulk_density: float) -> float:
        """
        Thermal diffusivity alpha = k / (rho * Cp).
        Ranges from ~0.2e-6 m2/s in dry sand to ~0.8e-6 m2/s in moist loam.
        """
        theta = moisture_vol_pct / 100.0
        # Volumetric heat capacity: C_s ~ 1.9e6 * BD/2.65 + 4.18e6 * theta
        cv = 1.9e6 * (bulk_density / 2.65) + 4.184e6 * theta
        # Thermal conductivity: Johansen model approximation
        k_therm = 0.25 + 1.25 * theta
        alpha = k_therm / cv
        return float(alpha)

    def simulate(self, inputs: MicroclimateInputs) -> MicroclimateDiagnostics:
        vpd, dew_pt = self.calculate_vapor_pressure_deficit(inputs.air_temp_mean_c, inputs.relative_humidity_pct)

        alpha = self.calculate_soil_thermal_diffusivity(inputs.soil_moisture_vol_pct, inputs.soil_bulk_density_g_cm3)
        # Daily angular frequency: omega = 2 * pi / 86400 s
        omega = 2.0 * np.pi / 86400.0
        # Damping depth: D = sqrt(2 * alpha / omega)
        damping_depth_m = np.sqrt((2.0 * alpha) / omega)
        damping_depth_cm = float(round(damping_depth_m * 100.0, 1))

        # Surface amplitude damped by crop canopy cover
        surface_amp = inputs.air_temp_amplitude_c * (1.0 - 0.6 * inputs.crop_canopy_cover_fraction)

        depths = [5.0, 10.0, 20.0, 50.0, 100.0]
        profile = []
        for z in depths:
            att = np.exp(-z / max(1.0, damping_depth_cm))
            tmin = inputs.air_temp_mean_c - surface_amp * att
            tmax = inputs.air_temp_mean_c + surface_amp * att
            profile.append(
                SoilDepthTemperature(
                    depth_cm=z,
                    t_min_c=round(tmin, 1),
                    t_max_c=round(tmax, 1),
                    t_mean_c=round(inputs.air_temp_mean_c, 1),
                    damping_factor=round(float(att), 3),
                )
            )

        # Canopy temperature depression (CTD) = T_air - T_canopy
        # Evaporative cooling drops canopy 2-5 C below air when unstressed
        cooling = min(4.5, vpd * 1.5)
        canopy_temp = inputs.air_temp_mean_c - cooling
        ctd = cooling

        return MicroclimateDiagnostics(
            vapor_pressure_deficit_kpa=vpd,
            dew_point_temp_c=dew_pt,
            canopy_temperature_c=round(canopy_temp, 1),
            canopy_temperature_depression_c=round(ctd, 1),
            soil_thermal_diffusivity_m2_s=float(f"{alpha:.2e}"),
            damping_depth_cm=damping_depth_cm,
            depth_temperature_profile=profile,
        )
