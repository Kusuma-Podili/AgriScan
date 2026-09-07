"""
AgriScan Controlled Environment Agriculture (CEA) Greenhouse Energy & DLI Engine.
Models polyhouse heat balance, evaporative pad-fan cooling, and supplemental LED lighting.
"""

from typing import Dict, List, Tuple, Optional
from pydantic import BaseModel, Field
import numpy as np


class GreenhouseStructureSpecs(BaseModel):
    structure_type: str  # Multi-span Gothic Arch, Venlo Glass, Quonset Tunnel
    floor_area_m2: float
    gutter_height_m: float
    ridge_height_m: float
    glazing_transmissivity: float = 0.72  # Solar transmittance of PE film / glass
    overall_u_value_w_m2_k: float = 4.8    # Heat loss coefficient
    ventilation_fan_capacity_m3_s: float = 25.0
    evaporative_pad_efficiency: float = 0.80


class GreenhouseSimulationStepResult(BaseModel):
    internal_air_temp_c: float
    cooling_mode_active: bool
    heating_required_kw: float
    canopy_transpiration_l_hr: float
    target_dli_achieved: float
    supplemental_ppfd_umol_m2_s: float


class GreenhouseClimatePhysics:
    """
    Simulates dynamic greenhouse energy and mass balance.
    """

    def __init__(self, specs: GreenhouseStructureSpecs):
        self.specs = specs

    def calculate_pad_fan_cooling(self, ambient_drybulb_c: float, ambient_rh_pct: float) -> float:
        """
        Calculates cooled air temperature after wet pad passage.
        Twb approximated via Stull psychrometric formula.
        """
        t = ambient_drybulb_c
        rh = ambient_rh_pct
        twb = t * np.arctan(0.151977 * np.sqrt(rh + 8.313659)) + np.arctan(t + rh) - np.arctan(rh - 1.676331) + 0.00391838 * (rh**1.5) * np.arctan(0.023101 * rh) - 4.686035
        # Cooled pad temperature: Tpad = Tdry - eta * (Tdry - Twb)
        t_pad = t - self.specs.evaporative_pad_efficiency * (t - twb)
        return float(round(t_pad, 1))

    def step(self, ambient_temp_c: float, solar_radiation_w_m2: float, ambient_rh_pct: float, target_temp_c: float = 24.0, target_dli_mol_m2_day: float = 22.0) -> GreenhouseSimulationStepResult:
        solar_heat_gain_kw = (solar_radiation_w_m2 * self.specs.floor_area_m2 * self.specs.glazing_transmissivity) / 1000.0
        q_loss_kw = (self.specs.overall_u_value_w_m2_k * self.specs.floor_area_m2 * (target_temp_c - ambient_temp_c)) / 1000.0

        net_kw = solar_heat_gain_kw - q_loss_kw
        cooling_active = bool(net_kw > 0 and ambient_temp_c > 18.0)
        heating_kw = max(0.0, -net_kw)

        if cooling_active:
            internal_t = self.calculate_pad_fan_cooling(ambient_temp_c, ambient_rh_pct) + 3.0
        else:
            internal_t = max(ambient_temp_c, target_temp_c)

        # Transpiration estimation (~70% of solar radiation converted to latent heat)
        transp_l_hr = (solar_heat_gain_kw * 0.70 * 3600.0) / 2450.0

        # Supplemental PPFD requirement
        solar_ppfd = solar_radiation_w_m2 * 2.1 * self.specs.glazing_transmissivity
        supp_ppfd = max(0.0, 350.0 - solar_ppfd)

        return GreenhouseSimulationStepResult(
            internal_air_temp_c=round(internal_t, 1),
            cooling_mode_active=cooling_active,
            heating_required_kw=round(heating_kw, 1),
            canopy_transpiration_l_hr=round(transp_l_hr, 1),
            target_dli_achieved=target_dli_mol_m2_day,
            supplemental_ppfd_umol_m2_s=round(supp_ppfd, 1),
        )
