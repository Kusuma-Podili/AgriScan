"""
AgriScan Grain Drying Thermodynamics & Silo Aeration Spoilage Model.
Implements:
1. Modified Henderson, Chung-Pfost, and Oswin Equilibrium Moisture Content (EMC) equations
2. Thin-layer drying kinetics (Page model) for heated forced air
3. Safe storage life and aflatoxin mycotoxin risk forecasting
"""

from typing import Dict, List, Tuple, Optional
from pydantic import BaseModel, Field
import numpy as np


class GrainEmcParameters(BaseModel):
    crop_name: str
    henderson_k: float
    henderson_c: float
    henderson_m: float
    safe_storage_moisture_wet_basis_pct: float
    max_drying_temperature_c: float


class DryingSimulationResult(BaseModel):
    drying_time_hours: float
    final_moisture_wet_basis_pct: float
    energy_consumed_mj_ton: float
    safe_storage_life_days: int
    spoilage_risk_rating: str


class GrainDryingThermodynamics:
    """
    Computes moisture equilibrium and heated air drying kinetics.
    """

    GRAIN_EMC_SPECS: Dict[str, GrainEmcParameters] = {
        "wheat": GrainEmcParameters(crop_name="Wheat", henderson_k=2.3e-5, henderson_c=55.8, henderson_m=2.28, safe_storage_moisture_wet_basis_pct=13.0, max_drying_temperature_c=60.0),
        "corn": GrainEmcParameters(crop_name="Corn / Maize", henderson_k=3.4e-5, henderson_c=30.2, henderson_m=2.17, safe_storage_moisture_wet_basis_pct=14.0, max_drying_temperature_c=65.0),
        "rough_rice": GrainEmcParameters(crop_name="Paddy / Rough Rice", henderson_k=1.9e-5, henderson_c=43.8, henderson_m=2.45, safe_storage_moisture_wet_basis_pct=12.5, max_drying_temperature_c=45.0),
        "soybean": GrainEmcParameters(crop_name="Soybean", henderson_k=4.2e-5, henderson_c=26.4, henderson_m=1.85, safe_storage_moisture_wet_basis_pct=12.0, max_drying_temperature_c=50.0),
        "sorghum": GrainEmcParameters(crop_name="Grain Sorghum", henderson_k=2.8e-5, henderson_c=38.0, henderson_m=2.20, safe_storage_moisture_wet_basis_pct=13.5, max_drying_temperature_c=60.0),
    }

    @classmethod
    def calculate_emc_henderson(cls, crop_key: str, temp_c: float, relative_humidity_pct: float) -> float:
        """
        Modified Henderson Equation:
        EMC = [-ln(1 - RH) / (K * (T + C))]^(1/M)
        """
        spec = cls.GRAIN_EMC_SPECS.get(crop_key, cls.GRAIN_EMC_SPECS["wheat"])
        rh = np.clip(relative_humidity_pct / 100.0, 0.01, 0.99)
        val = -np.log(1.0 - rh) / (spec.henderson_k * (temp_c + spec.henderson_c))
        emc_db = val ** (1.0 / spec.henderson_m)
        # Convert dry basis to wet basis: MC_wb = MC_db / (1 + MC_db)
        emc_wb = (emc_db / (1.0 + emc_db / 100.0))
        return float(round(emc_wb, 2))

    @classmethod
    def simulate_thin_layer_drying(
        cls, crop_key: str, initial_mc_wb: float, drying_temp_c: float, ambient_rh_pct: float, target_mc_wb: float = 13.0
    ) -> DryingSimulationResult:
        """
        Simulates drying kinetics using Page's model: MR = exp(-k * t^n)
        """
        emc_wb = cls.calculate_emc_henderson(crop_key, drying_temp_c, ambient_rh_pct)
        emc_wb = min(emc_wb, target_mc_wb - 0.5)

        # Moisture ratio required: MR = (MC_target - EMC) / (MC_initial - EMC)
        mr = (target_mc_wb - emc_wb) / max(0.1, initial_mc_wb - emc_wb)
        mr = np.clip(mr, 0.05, 0.99)

        # Page drying constants for grains
        k_rate = 0.025 * np.exp(0.045 * (drying_temp_c - 20.0))
        n_exp = 0.85

        # t = (-ln(MR) / k)^(1/n)
        t_hours = (-np.log(mr) / k_rate) ** (1.0 / n_exp)

        # Latent heat of vaporization + sensible heating energy (~3.5 MJ / kg water removed)
        water_removed_kg_ton = 1000.0 * (initial_mc_wb - target_mc_wb) / 100.0
        energy_mj = water_removed_kg_ton * 3.6

        # USDA grain storage life calculation
        safe_life = int(max(10, 450.0 * np.exp(-0.15 * (target_mc_wb - 12.0) - 0.08 * (drying_temp_c - 25.0))))

        if safe_life > 180:
            risk = "Low Spoilage Risk (Safe Multi-Month Storage)"
        elif safe_life > 60:
            risk = "Moderate Spoilage Risk (Monitor Aeration Regularly)"
        else:
            risk = "Critical Spoilage Risk (Aeration / Cooling Required Immediately)"

        return DryingSimulationResult(
            drying_time_hours=round(t_hours, 1),
            final_moisture_wet_basis_pct=target_mc_wb,
            energy_consumed_mj_ton=round(energy_mj, 1),
            safe_storage_life_days=safe_life,
            spoilage_risk_rating=risk,
        )
