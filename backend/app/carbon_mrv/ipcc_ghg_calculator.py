"""
AgriScan Agricultural Greenhouse Gas (GHG) Accounting Engine.
Implements IPCC 2019 Refinement Tier 1 & Tier 2 equations for:
1. Soil N2O direct and indirect emissions from fertilizers and crop residues
2. CH4 methane emissions from flooded rice cultivation
3. Scope 1 tractor diesel fuel CO2 emissions
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field
import numpy as np


class FarmGhgActivityInputs(BaseModel):
    synthetic_n_fertilizer_applied_kg: float
    organic_n_manure_applied_kg: float
    crop_residue_n_incorporated_kg: float
    flooded_paddy_area_ha: float = 0.0
    flooded_paddy_cultivation_days: int = 0
    paddy_water_regime: str = "continuous_flooding"  # continuous_flooding, single_drainage, multiple_drainage_awd
    diesel_fuel_consumed_liters: float = 0.0


class GhgEmissionBreakdown(BaseModel):
    direct_n2o_soil_tco2e: float
    indirect_n2o_atmospheric_deposition_tco2e: float
    indirect_n2o_leaching_runoff_tco2e: float
    flooded_paddy_ch4_tco2e: float
    machinery_diesel_co2_tco2e: float
    total_gross_ghg_emissions_tco2e: float
    carbon_intensity_kg_co2e_per_ha: float


class AgriculturalGhgCalculator:
    """
    Computes Scope 1 agricultural greenhouse gas emissions in metric tons CO2 equivalent (tCO2e).
    """

    # Global Warming Potentials (IPCC AR6 100-year GWP):
    GWP_N2O = 273.0
    GWP_CH4 = 28.0
    DIESEL_EMISSION_FACTOR_KG_CO2_PER_LITER = 2.68

    @classmethod
    def calculate_emissions(cls, inputs: FarmGhgActivityInputs, total_farm_area_ha: float = 10.0) -> GhgEmissionBreakdown:
        # 1. Direct N2O emissions: EF1 = 0.01 (1% of N input converted to N2O-N)
        total_n = inputs.synthetic_n_fertilizer_applied_kg + inputs.organic_n_manure_applied_kg + inputs.crop_residue_n_incorporated_kg
        direct_n2o_kg = total_n * 0.01 * (44.0 / 28.0)
        direct_n2o_tco2e = (direct_n2o_kg * cls.GWP_N2O) / 1000.0

        # 2. Indirect N2O: Atmospheric volatilization (FracGASF = 0.11, EF4 = 0.01)
        volatilized_n = inputs.synthetic_n_fertilizer_applied_kg * 0.11 + inputs.organic_n_manure_applied_kg * 0.21
        indir_volat_kg = volatilized_n * 0.01 * (44.0 / 28.0)
        indir_volat_tco2e = (indir_volat_kg * cls.GWP_N2O) / 1000.0

        # 3. Indirect N2O: Leaching / runoff (FracLEACH = 0.24, EF5 = 0.011)
        leached_n = total_n * 0.24
        indir_leach_kg = leached_n * 0.011 * (44.0 / 28.0)
        indir_leach_tco2e = (indir_leach_kg * cls.GWP_N2O) / 1000.0

        # 4. Flooded Paddy Methane CH4:
        # Baseline EFc = 1.30 kg CH4 / ha / day
        # Scaling factor: continuous = 1.0, single drain = 0.71, AWD multiple = 0.52
        if inputs.paddy_water_regime == "multiple_drainage_awd":
            sf_w = 0.52
        elif inputs.paddy_water_regime == "single_drainage":
            sf_w = 0.71
        else:
            sf_w = 1.0

        daily_ef = 1.30 * sf_w
        total_ch4_kg = inputs.flooded_paddy_area_ha * inputs.flooded_paddy_cultivation_days * daily_ef
        paddy_ch4_tco2e = (total_ch4_kg * cls.GWP_CH4) / 1000.0

        # 5. Farm Machinery Diesel Combustion
        diesel_tco2e = (inputs.diesel_fuel_consumed_liters * cls.DIESEL_EMISSION_FACTOR_KG_CO2_PER_LITER) / 1000.0

        total_tco2e = direct_n2o_tco2e + indir_volat_tco2e + indir_leach_tco2e + paddy_ch4_tco2e + diesel_tco2e
        area = max(0.1, total_farm_area_ha)
        intensity = (total_tco2e * 1000.0) / area

        return GhgEmissionBreakdown(
            direct_n2o_soil_tco2e=round(direct_n2o_tco2e, 3),
            indirect_n2o_atmospheric_deposition_tco2e=round(indir_volat_tco2e, 3),
            indirect_n2o_leaching_runoff_tco2e=round(indir_leach_tco2e, 3),
            flooded_paddy_ch4_tco2e=round(paddy_ch4_tco2e, 3),
            machinery_diesel_co2_tco2e=round(diesel_tco2e, 3),
            total_gross_ghg_emissions_tco2e=round(total_tco2e, 3),
            carbon_intensity_kg_co2e_per_ha=round(intensity, 1),
        )
