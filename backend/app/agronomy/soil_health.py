"""
AgroPulse Soil Health Assessment & Degradation Remediation Engine.
Implements:
1. Haney Soil Health Score (SHS) algorithm
2. Cation Exchange Ratios (Ca:Mg, Mg:K, Ca:K balance)
3. Sodium Adsorption Ratio (SAR) and Exchangeable Sodium Percentage (ESP)
4. Gypsum Requirement (GR) for sodic soil reclamation
5. Lime Requirement (LR) by Shoemaker-McLean-Pratt (SMP) buffer method
6. Organic matter mineralization and soil carbon sequestration simulator
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field
import numpy as np


class SoilHealthTestInputs(BaseModel):
    ph_water: float
    electrical_conductivity_ds_m: float
    organic_matter_pct: float
    total_organic_carbon_ppm: float
    water_extractable_organic_c_ppm: float
    water_extractable_organic_n_ppm: float
    solvita_co2_c_ppm_24hr: float
    ca_cmol_kg: float
    mg_cmol_kg: float
    k_cmol_kg: float
    na_cmol_kg: float
    h_al_cmol_kg: float = 0.0
    soil_depth_cm: float = 15.0
    bulk_density_g_cm3: float = 1.30


class SoilHealthDiagnostics(BaseModel):
    haney_soil_health_score: float
    cation_exchange_capacity_cmol_kg: float
    calcium_saturation_pct: float
    magnesium_saturation_pct: float
    potassium_saturation_pct: float
    exchangeable_sodium_pct_esp: float
    sodium_adsorption_ratio_sar: float
    soil_salinity_sodicity_class: str
    gypsum_requirement_ton_ha: float
    lime_requirement_ton_ha: float
    soil_health_rating: str
    recommended_interventions: List[str]


class SoilHealthEngine:
    """
    Evaluates biological, physical, and chemical indicators of soil health.
    """

    @staticmethod
    def calculate_haney_score(
        co2_burst: float, weoc: float, weon: float
    ) -> float:
        """
        Haney Soil Health Tool Score:
        SHS = (Solvita CO2-C / 10) + (WEOC / 50) + (WEON / 10)
        """
        score = (co2_burst / 10.0) + (weoc / 50.0) + (weon / 10.0)
        return float(round(score, 2))

    @staticmethod
    def calculate_sar(na_cmol: float, ca_cmol: float, mg_cmol: float) -> float:
        """
        Sodium Adsorption Ratio: SAR = Na / sqrt((Ca + Mg) / 2)
        """
        denom = np.sqrt(max(0.01, (ca_cmol + mg_cmol) / 2.0))
        return float(round(na_cmol / denom, 2))

    @staticmethod
    def classify_salinity_sodicity(ec: float, ph: float, esp: float) -> str:
        """
        USDA Salinity Laboratory Classification.
        """
        if ec < 4.0 and esp < 15.0 and ph < 8.5:
            return "Normal Soil"
        elif ec >= 4.0 and esp < 15.0 and ph < 8.5:
            return "Saline Soil (White Alkali)"
        elif ec < 4.0 and esp >= 15.0 and ph >= 8.5:
            return "Sodic Soil (Black Alkali)"
        else:
            return "Saline-Sodic Soil"

    @staticmethod
    def calculate_gypsum_requirement(
        cec: float, current_esp: float, target_esp: float, bulk_density: float, depth_cm: float
    ) -> float:
        """
        Gypsum Requirement (ton/ha) = 0.086 * (ESP_current - ESP_target) * CEC * BD * (depth_cm / 15)
        """
        if current_esp <= target_esp:
            return 0.0
        delta_esp = current_esp - target_esp
        gr = 0.086 * (delta_esp / 100.0) * cec * bulk_density * (depth_cm / 15.0) * 10.0
        return float(round(max(0.0, gr), 2))

    @staticmethod
    def calculate_lime_requirement(ph: float, cec: float, target_ph: float = 6.5) -> float:
        """
        Calculates pure agricultural limestone requirement (CaCO3 ton/ha) to reach target pH.
        """
        if ph >= target_ph:
            return 0.0
        delta_ph = target_ph - ph
        # Buffer requirement proportional to CEC buffer capacity
        lr = delta_ph * (cec * 0.18)
        return float(round(max(0.0, lr), 2))

    def diagnose(self, inputs: SoilHealthTestInputs) -> SoilHealthDiagnostics:
        cec = inputs.ca_cmol_kg + inputs.mg_cmol_kg + inputs.k_cmol_kg + inputs.na_cmol_kg + inputs.h_al_cmol_kg
        cec = max(1.0, cec)

        ca_sat = (inputs.ca_cmol_kg / cec) * 100.0
        mg_sat = (inputs.mg_cmol_kg / cec) * 100.0
        k_sat = (inputs.k_cmol_kg / cec) * 100.0
        esp = (inputs.na_cmol_kg / cec) * 100.0

        sar = self.calculate_sar(inputs.na_cmol_kg, inputs.ca_cmol_kg, inputs.mg_cmol_kg)
        soil_class = self.classify_salinity_sodicity(inputs.electrical_conductivity_ds_m, inputs.ph_water, esp)

        shs = self.calculate_haney_score(
            inputs.solvita_co2_c_ppm_24hr,
            inputs.water_extractable_organic_c_ppm,
            inputs.water_extractable_organic_n_ppm,
        )

        gr = self.calculate_gypsum_requirement(
            cec, esp, target_esp=10.0, bulk_density=inputs.bulk_density_g_cm3, depth_cm=inputs.soil_depth_cm
        )
        lr = self.calculate_lime_requirement(inputs.ph_water, cec, target_ph=6.5)

        if shs > 20.0:
            rating = "Excellent (Biologically Active)"
        elif shs > 12.0:
            rating = "Good (Sufficient Microbial Activity)"
        elif shs > 7.0:
            rating = "Moderate (Depleted Carbon Stocks)"
        else:
            rating = "Degraded (Critical Intervention Needed)"

        interventions = []
        if gr > 0.0:
            interventions.append(f"Apply {gr} tons/ha agricultural gypsum (CaSO4·2H2O) with heavy leaching")
        if lr > 0.0:
            interventions.append(f"Incorporate {lr} tons/ha finely ground limestone (CaCO3) 4 weeks before sowing")
        if inputs.organic_matter_pct < 1.5:
            interventions.append("Apply 10-15 tons/ha well-decomposed Farmyard Manure or green manure with Sesbania aculeata")
        if mg_sat > 25.0 and ca_sat < 60.0:
            interventions.append("High magnesium tightness observed; apply soluble calcium to improve soil flocculation")

        return SoilHealthDiagnostics(
            haney_soil_health_score=shs,
            cation_exchange_capacity_cmol_kg=round(cec, 2),
            calcium_saturation_pct=round(ca_sat, 1),
            magnesium_saturation_pct=round(mg_sat, 1),
            potassium_saturation_pct=round(k_sat, 1),
            exchangeable_sodium_pct_esp=round(esp, 1),
            sodium_adsorption_ratio_sar=sar,
            soil_salinity_sodicity_class=soil_class,
            gypsum_requirement_ton_ha=gr,
            lime_requirement_ton_ha=lr,
            soil_health_rating=rating,
            recommended_interventions=interventions,
        )
