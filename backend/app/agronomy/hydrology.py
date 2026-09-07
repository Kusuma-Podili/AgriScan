"""
AgroPulse Multi-Layer Soil Hydrology & Dynamic Water Balance Simulation Engine.
Implements:
1. Daily bucket water balance with unsaturated hydraulic flow
2. FAO-56 Dual Crop Coefficient (Basal Kc + Soil Evaporation Ke)
3. Water stress coefficient Ks reduction
4. USDA Soil Conservation Service (SCS) Curve Number runoff partitioning
5. Deep percolation and capillary rise from shallow groundwater tables
"""

from typing import List, Dict, Tuple, Optional
from pydantic import BaseModel, Field
import numpy as np


class SoilLayerHydrology(BaseModel):
    layer_index: int
    thickness_mm: float
    field_capacity_mm: float
    wilting_point_mm: float
    saturation_mm: float
    current_moisture_mm: float
    ksat_mm_day: float


class DailyHydrologyInputs(BaseModel):
    day_of_year: int
    rainfall_mm: float
    irrigation_mm: float
    et0_penman_mm: float
    crop_kc_basal: float
    fraction_ground_cover: float
    root_depth_mm: float
    water_table_depth_m: Optional[float] = None


class DailyHydrologyOutputs(BaseModel):
    day_of_year: int
    surface_runoff_mm: float
    infiltration_mm: float
    soil_evaporation_ke_mm: float
    crop_transpiration_tact_mm: float
    total_et_mm: float
    deep_percolation_mm: float
    capillary_rise_mm: float
    water_stress_coefficient_ks: float
    profile_moisture_depletion_pct: float
    root_zone_moisture_mm: float


class MultiLayerSoilHydrologyEngine:
    """
    Simulates multi-layer unsaturated moisture transport and crop water extraction.
    """

    def __init__(
        self,
        layers: List[SoilLayerHydrology],
        scs_curve_number_amc2: float = 75.0,
        readily_available_water_p: float = 0.55,
    ):
        self.layers = layers
        self.cn2 = scs_curve_number_amc2
        self.p_depletion_factor = readily_available_water_p

    def adjust_curve_number(self, five_day_antecedent_rainfall_mm: float) -> float:
        """
        Adjusts SCS Curve Number for Antecedent Moisture Condition (AMC-I, AMC-II, AMC-III).
        """
        if five_day_antecedent_rainfall_mm < 12.5:
            return (4.2 * self.cn2) / (10.0 - 0.058 * self.cn2)
        elif five_day_antecedent_rainfall_mm > 27.5:
            return (23.0 * self.cn2) / (10.0 + 0.13 * self.cn2)
        else:
            return self.cn2

    def calculate_surface_runoff(self, rainfall_mm: float, cn: float) -> float:
        """
        Calculates surface runoff using the USDA SCS-CN equation: Q = (P - Ia)^2 / (P - Ia + S)
        """
        if rainfall_mm <= 0.0:
            return 0.0

        potential_retention_s = (25400.0 / cn) - 254.0
        initial_abstraction_ia = 0.2 * potential_retention_s

        if rainfall_mm <= initial_abstraction_ia:
            return 0.0

        runoff_q = ((rainfall_mm - initial_abstraction_ia) ** 2) / (
            rainfall_mm - initial_abstraction_ia + potential_retention_s
        )
        return float(np.clip(runoff_q, 0.0, rainfall_mm))

    def calculate_capillary_rise(
        self, water_table_depth_m: Optional[float], top_layer_moisture_deficit_mm: float
    ) -> float:
        """
        Darcy-Buckingham capillary rise approximation from a shallow water table.
        """
        if water_table_depth_m is None or water_table_depth_m > 3.0:
            return 0.0

        flux = 2.5 * np.exp(-1.8 * water_table_depth_m)
        return float(min(flux, top_layer_moisture_deficit_mm * 0.3))

    def simulate_day(
        self, inputs: DailyHydrologyInputs, recent_rainfall_mm: float = 0.0
    ) -> DailyHydrologyOutputs:
        """
        Executes a complete 24-hour hydrological step.
        """
        cn = self.adjust_curve_number(recent_rainfall_mm)
        runoff = self.calculate_surface_runoff(inputs.rainfall_mm, cn)
        infiltration = (inputs.rainfall_mm - runoff) + inputs.irrigation_mm

        excess_flux = infiltration
        for layer in self.layers:
            capacity = layer.field_capacity_mm - layer.current_moisture_mm
            if capacity > 0:
                water_absorbed = min(excess_flux, capacity)
                layer.current_moisture_mm += water_absorbed
                excess_flux -= water_absorbed
            if excess_flux <= 0:
                break

        deep_percolation = excess_flux

        accumulated_depth = 0.0
        rz_moisture = 0.0
        rz_fc = 0.0
        rz_wp = 0.0

        for layer in self.layers:
            accumulated_depth += layer.thickness_mm
            rz_moisture += layer.current_moisture_mm
            rz_fc += layer.field_capacity_mm
            rz_wp += layer.wilting_point_mm
            if accumulated_depth >= inputs.root_depth_mm:
                break

        taw = max(1.0, rz_fc - rz_wp)
        dr = max(0.0, rz_fc - rz_moisture)
        raw = self.p_depletion_factor * taw

        if dr <= raw:
            ks = 1.0
        elif dr < taw:
            ks = float((taw - dr) / ((1.0 - self.p_depletion_factor) * taw))
            ks = float(np.clip(ks, 0.0, 1.0))
        else:
            ks = 0.0

        top_layer = self.layers[0]
        top_fc = top_layer.field_capacity_mm
        top_wp = top_layer.wilting_point_mm
        top_moisture = top_layer.current_moisture_mm
        top_depletion = max(0.0, top_fc - top_moisture)
        rew = 0.5 * (top_fc - top_wp)

        if top_depletion <= rew:
            kr = 1.0
        else:
            kr = float((top_fc - top_wp - top_depletion) / max(1.0, (top_fc - top_wp - rew)))
            kr = float(np.clip(kr, 0.0, 1.0))

        ke_max = max(0.0, 1.2 - inputs.crop_kc_basal)
        ke = kr * (1.0 - inputs.fraction_ground_cover) * ke_max
        soil_evap = min(ke * inputs.et0_penman_mm, top_moisture - top_wp)
        soil_evap = max(0.0, soil_evap)

        crop_transp = ks * inputs.crop_kc_basal * inputs.et0_penman_mm
        total_et = soil_evap + crop_transp

        top_layer.current_moisture_mm -= soil_evap

        remaining_transp = crop_transp
        for layer in self.layers:
            available_in_layer = max(0.0, layer.current_moisture_mm - layer.wilting_point_mm)
            if available_in_layer > 0:
                extract = min(remaining_transp, available_in_layer)
                layer.current_moisture_mm -= extract
                remaining_transp -= extract
            if remaining_transp <= 0:
                break

        cap_rise = self.calculate_capillary_rise(inputs.water_table_depth_m, top_depletion)
        top_layer.current_moisture_mm += cap_rise

        depletion_pct = float(np.clip((dr / taw) * 100.0, 0.0, 100.0))

        return DailyHydrologyOutputs(
            day_of_year=inputs.day_of_year,
            surface_runoff_mm=round(runoff, 2),
            infiltration_mm=round(infiltration, 2),
            soil_evaporation_ke_mm=round(soil_evap, 2),
            crop_transpiration_tact_mm=round(crop_transp, 2),
            total_et_mm=round(total_et, 2),
            deep_percolation_mm=round(deep_percolation, 2),
            capillary_rise_mm=round(cap_rise, 2),
            water_stress_coefficient_ks=round(ks, 3),
            profile_moisture_depletion_pct=round(depletion_pct, 1),
            root_zone_moisture_mm=round(rz_moisture, 1),
        )
