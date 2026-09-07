"""
AgroPulse Site-Specific Nutrient Management (SSNM) and Fertilizer Optimization Engine.
Calculates targeted nutrient balancing based on crop yield goals, indigenous soil nutrient supply,
fertilizer recovery efficiencies, and linear optimization into commercial formulations.
"""

from typing import Dict, List, Optional, Tuple
from pydantic import BaseModel, Field
from app.ml.data.crop_database import CropAgronomicProfile, get_crop_by_id
from app.ml.data.fertilizer_db import FERTILIZER_DATABASE, FertilizerProduct


class SoilTestValues(BaseModel):
    available_n_kg_ha: float = Field(..., ge=0, description="Available Soil Nitrogen (KMnO4 method) in kg/ha")
    available_p2o5_kg_ha: float = Field(..., ge=0, description="Available Soil Phosphorus (Olsen / Bray) in kg P2O5/ha")
    available_k2o_kg_ha: float = Field(..., ge=0, description="Available Soil Potassium (NH4OAc) in kg K2O/ha")
    organic_carbon_pct: float = Field(0.50, ge=0, le=10, description="Soil Organic Carbon %")
    ph: float = Field(7.0, ge=3.0, le=12.0, description="Soil pH (1:2.5 water)")
    electrical_conductivity_ds_m: float = Field(0.5, ge=0, description="Soil EC in dS/m")
    soil_texture: str = Field("loam", description="USDA soil texture class")
    zinc_ppm: Optional[float] = Field(None, description="DTPA-extractable Zinc (ppm)")
    boron_ppm: Optional[float] = Field(None, description="Hot water extractable Boron (ppm)")
    iron_ppm: Optional[float] = Field(None, description="DTPA-extractable Iron (ppm)")


class NutrientBalanceSheet(BaseModel):
    target_yield_ton_ha: float
    total_demand_n_kg: float
    total_demand_p2o5_kg: float
    total_demand_k2o_kg: float
    indigenous_supply_n_kg: float
    indigenous_supply_p2o5_kg: float
    indigenous_supply_k2o_kg: float
    net_deficit_n_kg: float
    net_deficit_p2o5_kg: float
    net_deficit_k2o_kg: float
    fertilizer_requirement_n_kg: float
    fertilizer_requirement_p2o5_kg: float
    fertilizer_requirement_k2o_kg: float


class FertilizerDoseItem(BaseModel):
    product_id: str
    product_name: str
    rate_kg_ha: float
    rate_kg_acre: float
    bags_50kg_ha: float
    bags_50kg_acre: float
    timing_stage: str  # Basal, Tillering / First Top Dress, Flowering / Second Top Dress
    application_method: str
    estimated_cost_usd: float


class FertilizerRecommendationSchedule(BaseModel):
    crop_id: str
    crop_name: str
    yield_goal_ton_ha: float
    strategy_name: str  # e.g., "DAP + Urea + MOP Strategy" or "Straight SSP + Urea + MOP"
    balance_sheet: NutrientBalanceSheet
    doses: List[FertilizerDoseItem]
    micronutrient_advisories: List[str]
    total_estimated_fertilizer_cost_usd_ha: float
    total_estimated_fertilizer_cost_usd_acre: float
    soil_amendment_recommendation: Optional[str] = None


class SSNMEngine:
    """
    Site-Specific Nutrient Management Engine conforming to IPNI / IRRI QueFTS models.
    """

    # Typical agronomic recovery efficiency coefficients (RE)
    RECOVERY_EFFICIENCY_N = 0.40   # 40% of applied N taken up by crop in current season
    RECOVERY_EFFICIENCY_P = 0.25   # 25% of applied P2O5 taken up (high soil fixation)
    RECOVERY_EFFICIENCY_K = 0.60   # 60% of applied K2O taken up

    # Soil contribution factors to crop uptake (indigenous supply)
    SOIL_SUPPLY_FACTOR_N = 0.30
    SOIL_SUPPLY_FACTOR_P = 0.45
    SOIL_SUPPLY_FACTOR_K = 0.35

    @classmethod
    def calculate_nutrient_balance(
        cls,
        crop: CropAgronomicProfile,
        soil: SoilTestValues,
        target_yield_ton_ha: Optional[float] = None,
    ) -> NutrientBalanceSheet:
        """
        Computes nutrient removal demand, indigenous supply, and net fertilizer requirements.
        """
        yield_target = target_yield_ton_ha if target_yield_ton_ha else crop.benchmark_yield_ton_ha

        # Total crop nutrient demand (TND) for target yield
        tnd_n = yield_target * crop.nutrient_uptake.n_kg_per_ton
        tnd_p = yield_target * crop.nutrient_uptake.p2o5_kg_per_ton
        tnd_k = yield_target * crop.nutrient_uptake.k2o_kg_per_ton

        # pH and texture adjustment modifiers on indigenous availability
        ph_factor_p = 1.0
        if soil.ph < 5.5:
            # Acidic fixation by Fe/Al oxides
            ph_factor_p = 0.70
        elif soil.ph > 8.0:
            # Alkaline precipitation as Ca3(PO4)2
            ph_factor_p = 0.75

        # Organic matter nitrogen bonus
        oc_multiplier = max(0.5, min(2.0, soil.organic_carbon_pct / 0.50))

        # Indigenous Soil Supply (INS, IPS, IKS)
        ins = soil.available_n_kg_ha * cls.SOIL_SUPPLY_FACTOR_N * oc_multiplier
        ips = soil.available_p2o5_kg_ha * cls.SOIL_SUPPLY_FACTOR_P * ph_factor_p
        iks = soil.available_k2o_kg_ha * cls.SOIL_SUPPLY_FACTOR_K

        # Net deficit to be supplemented via fertilizer
        deficit_n = max(0.0, tnd_n - ins)
        deficit_p = max(0.0, tnd_p - ips)
        deficit_k = max(0.0, tnd_k - iks)

        # Fertilizer elemental requirement considering recovery efficiency
        # Ensure minimum maintenance dose (starter dose) even if test is high
        fert_n = max(20.0, deficit_n / cls.RECOVERY_EFFICIENCY_N)
        fert_p = max(15.0, deficit_p / cls.RECOVERY_EFFICIENCY_P)
        fert_k = max(15.0, deficit_k / cls.RECOVERY_EFFICIENCY_K)

        return NutrientBalanceSheet(
            target_yield_ton_ha=round(yield_target, 2),
            total_demand_n_kg=round(tnd_n, 1),
            total_demand_p2o5_kg=round(tnd_p, 1),
            total_demand_k2o_kg=round(tnd_k, 1),
            indigenous_supply_n_kg=round(ins, 1),
            indigenous_supply_p2o5_kg=round(ips, 1),
            indigenous_supply_k2o_kg=round(iks, 1),
            net_deficit_n_kg=round(deficit_n, 1),
            net_deficit_p2o5_kg=round(deficit_p, 1),
            net_deficit_k2o_kg=round(deficit_k, 1),
            fertilizer_requirement_n_kg=round(fert_n, 1),
            fertilizer_requirement_p2o5_kg=round(fert_p, 1),
            fertilizer_requirement_k2o_kg=round(fert_k, 1),
        )

    @classmethod
    def generate_fertilizer_schedule(
        cls,
        crop_id: str,
        soil: SoilTestValues,
        target_yield_ton_ha: Optional[float] = None,
        strategy: str = "dap_urea_mop",
    ) -> FertilizerRecommendationSchedule:
        """
        Generates commercial fertilizer formulation schedule with stage-wise split applications.
        """
        crop = get_crop_by_id(crop_id)
        if not crop:
            raise ValueError(f"Crop {crop_id} not found in database.")

        balance = cls.calculate_nutrient_balance(crop, soil, target_yield_ton_ha)
        doses: List[FertilizerDoseItem] = []
        micronutrient_advisories: List[str] = []

        req_n = balance.fertilizer_requirement_n_kg
        req_p = balance.fertilizer_requirement_p2o5_kg
        req_k = balance.fertilizer_requirement_k2o_kg

        # Conversion constant 1 ha = 2.47105 acres -> 1 acre = 0.404686 ha
        ha_to_acre = 0.404686

        if strategy == "dap_urea_mop":
            # Formulation 1: Di-Ammonium Phosphate (DAP 18:46:0) + Urea (46% N) + Muriate of Potash (MOP 60% K2O)
            dap = FERTILIZER_DATABASE["di_ammonium_phosphate"]
            urea = FERTILIZER_DATABASE["urea"]
            mop = FERTILIZER_DATABASE["muriate_of_potash"]

            # 1. Supply 100% P via DAP
            dap_rate_ha = (req_p / dap.p2o5_pct) * 100.0
            n_from_dap = dap_rate_ha * (dap.n_pct / 100.0)

            # 2. Balance N via Urea
            remaining_n = max(0.0, req_n - n_from_dap)
            urea_rate_ha = (remaining_n / urea.n_pct) * 100.0

            # 3. Supply K via MOP (or SOP if crop is chloride-sensitive)
            potash_prod = mop
            if crop_id in ["tobacco", "grapes", "potato"]:
                potash_prod = FERTILIZER_DATABASE["potassium_sulphate"]
            k_rate_ha = (req_k / potash_prod.k2o_pct) * 100.0

            # Schedule Splits:
            # - Basal: 100% DAP + 100% Potash (or 50% in light soils) + 30% of Urea
            basal_urea_ha = urea_rate_ha * 0.30
            top1_urea_ha = urea_rate_ha * 0.40
            top2_urea_ha = urea_rate_ha * 0.30

            # DAP Dose (Basal)
            doses.append(
                FertilizerDoseItem(
                    product_id=dap.id,
                    product_name=dap.name,
                    rate_kg_ha=round(dap_rate_ha, 1),
                    rate_kg_acre=round(dap_rate_ha * ha_to_acre, 1),
                    bags_50kg_ha=round(dap_rate_ha / 50.0, 1),
                    bags_50kg_acre=round((dap_rate_ha * ha_to_acre) / 50.0, 1),
                    timing_stage="Basal (At Sowing / Planting)",
                    application_method="Band placement 3-5 cm below and beside the seed line",
                    estimated_cost_usd=round(dap_rate_ha * 0.65, 2),
                )
            )

            # Potash Dose (Basal)
            doses.append(
                FertilizerDoseItem(
                    product_id=potash_prod.id,
                    product_name=potash_prod.name,
                    rate_kg_ha=round(k_rate_ha, 1),
                    rate_kg_acre=round(k_rate_ha * ha_to_acre, 1),
                    bags_50kg_ha=round(k_rate_ha / 50.0, 1),
                    bags_50kg_acre=round((k_rate_ha * ha_to_acre) / 50.0, 1),
                    timing_stage="Basal (At Sowing)",
                    application_method="Soil incorporation during final land preparation",
                    estimated_cost_usd=round(k_rate_ha * 0.55, 2),
                )
            )

            # Urea Split 1 (Basal)
            if basal_urea_ha > 0:
                doses.append(
                    FertilizerDoseItem(
                        product_id=urea.id,
                        product_name=f"{urea.name} (Basal Split)",
                        rate_kg_ha=round(basal_urea_ha, 1),
                        rate_kg_acre=round(basal_urea_ha * ha_to_acre, 1),
                        bags_50kg_ha=round(basal_urea_ha / 50.0, 1),
                        bags_50kg_acre=round((basal_urea_ha * ha_to_acre) / 50.0, 1),
                        timing_stage="Basal (At Sowing)",
                        application_method="Broadcast and incorporated into topsoil",
                        estimated_cost_usd=round(basal_urea_ha * 0.30, 2),
                    )
                )

            # Urea Split 2 (Active Vegetative / Tillering)
            if top1_urea_ha > 0:
                doses.append(
                    FertilizerDoseItem(
                        product_id=urea.id,
                        product_name=f"{urea.name} (1st Top-Dress)",
                        rate_kg_ha=round(top1_urea_ha, 1),
                        rate_kg_acre=round(top1_urea_ha * ha_to_acre, 1),
                        bags_50kg_ha=round(top1_urea_ha / 50.0, 1),
                        bags_50kg_acre=round((top1_urea_ha * ha_to_acre) / 50.0, 1),
                        timing_stage="Active Tillering / Rapid Vegetative (25-30 DAS)",
                        application_method="Broadcast over moist soil, followed by light hoeing or irrigation",
                        estimated_cost_usd=round(top1_urea_ha * 0.30, 2),
                    )
                )

            # Urea Split 3 (Panicle Initiation / Flowering)
            if top2_urea_ha > 0:
                doses.append(
                    FertilizerDoseItem(
                        product_id=urea.id,
                        product_name=f"{urea.name} (2nd Top-Dress)",
                        rate_kg_ha=round(top2_urea_ha, 1),
                        rate_kg_acre=round(top2_urea_ha * ha_to_acre, 1),
                        bags_50kg_ha=round(top2_urea_ha / 50.0, 1),
                        bags_50kg_acre=round((top2_urea_ha * ha_to_acre) / 50.0, 1),
                        timing_stage="Panicle Initiation / Pre-Flowering (45-55 DAS)",
                        application_method="Side dressing along crop rows",
                        estimated_cost_usd=round(top2_urea_ha * 0.30, 2),
                    )
                )

            strategy_title = "DAP + Urea + Potash Integrated Regime"

        else:
            # Formulation 2: Straight Fertilizers (SSP + Urea + MOP)
            ssp = FERTILIZER_DATABASE["single_super_phosphate"]
            urea = FERTILIZER_DATABASE["urea"]
            mop = FERTILIZER_DATABASE["muriate_of_potash"]

            ssp_rate_ha = (req_p / ssp.p2o5_pct) * 100.0
            urea_rate_ha = (req_n / urea.n_pct) * 100.0
            k_rate_ha = (req_k / mop.k2o_pct) * 100.0

            doses.append(
                FertilizerDoseItem(
                    product_id=ssp.id,
                    product_name=ssp.name,
                    rate_kg_ha=round(ssp_rate_ha, 1),
                    rate_kg_acre=round(ssp_rate_ha * ha_to_acre, 1),
                    bags_50kg_ha=round(ssp_rate_ha / 50.0, 1),
                    bags_50kg_acre=round((ssp_rate_ha * ha_to_acre) / 50.0, 1),
                    timing_stage="Basal (At Sowing)",
                    application_method="Broadcast and incorporated deep into furrow bed",
                    estimated_cost_usd=round(ssp_rate_ha * 0.22, 2),
                )
            )

            doses.append(
                FertilizerDoseItem(
                    product_id=mop.id,
                    product_name=mop.name,
                    rate_kg_ha=round(k_rate_ha, 1),
                    rate_kg_acre=round(k_rate_ha * ha_to_acre, 1),
                    bags_50kg_ha=round(k_rate_ha / 50.0, 1),
                    bags_50kg_acre=round((k_rate_ha * ha_to_acre) / 50.0, 1),
                    timing_stage="Basal (At Sowing)",
                    application_method="Soil incorporation",
                    estimated_cost_usd=round(k_rate_ha * 0.55, 2),
                )
            )

            doses.append(
                FertilizerDoseItem(
                    product_id=urea.id,
                    product_name=f"{urea.name} (Split across 3 applications)",
                    rate_kg_ha=round(urea_rate_ha, 1),
                    rate_kg_acre=round(urea_rate_ha * ha_to_acre, 1),
                    bags_50kg_ha=round(urea_rate_ha / 50.0, 1),
                    bags_50kg_acre=round((urea_rate_ha * ha_to_acre) / 50.0, 1),
                    timing_stage="Split (30% Basal, 40% Tillering, 30% Heading)",
                    application_method="Top-dressing over moist soil",
                    estimated_cost_usd=round(urea_rate_ha * 0.30, 2),
                )
            )
            strategy_title = "Single Super Phosphate (SSP) + Urea + Potash Regime"

        # Check micronutrient diagnostics
        if soil.zinc_ppm is not None and soil.zinc_ppm < 0.60:
            micronutrient_advisories.append(
                "Critical Zinc Deficiency (<0.60 ppm DTPA-Zn): Apply Zinc Sulphate Heptahydrate (21% Zn) @ 25 kg/ha at basal land preparation. Do not mix directly with DAP."
            )
        elif soil.ph > 8.0:
            micronutrient_advisories.append(
                "High pH (>8.0) restricts Zinc bioavailability: Prophylactic spray of 0.5% ZnSO4 + 0.25% lime at 30 and 45 DAS is recommended."
            )

        if soil.boron_ppm is not None and soil.boron_ppm < 0.50:
            micronutrient_advisories.append(
                "Boron Deficiency (<0.50 ppm): Apply Borax (10.5% B) @ 10 kg/ha to prevent hollow stem and flower abortion."
            )

        # Soil pH amendment advice
        amendment = None
        if soil.ph < 5.2:
            amendment = f"Strongly Acidic Soil (pH {soil.ph}): Broadcast and incorporate Agricultural Lime (CaCO3) @ 2.5 t/ha 3 weeks before sowing."
        elif soil.ph > 8.6:
            amendment = f"Sodic / Strongly Alkaline Soil (pH {soil.ph}): Apply Agricultural Gypsum (CaSO4·2H2O) @ 3.0 t/ha with ponded leaching."

        total_cost_ha = sum(d.estimated_cost_usd for d in doses)
        total_cost_acre = total_cost_ha * ha_to_acre

        return FertilizerRecommendationSchedule(
            crop_id=crop.id,
            crop_name=crop.name,
            yield_goal_ton_ha=balance.target_yield_ton_ha,
            strategy_name=strategy_title,
            balance_sheet=balance,
            doses=doses,
            micronutrient_advisories=micronutrient_advisories,
            total_estimated_fertilizer_cost_usd_ha=round(total_cost_ha, 2),
            total_estimated_fertilizer_cost_usd_acre=round(total_cost_acre, 2),
            soil_amendment_recommendation=amendment,
        )
