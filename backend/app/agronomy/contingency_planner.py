"""
AgroPulse Real-Time Agricultural Contingency & Climate Shock Response Engine.
Formulates dynamic contingency cropping plans, mid-season moisture conservation tactics,
and post-calamity rehabilitation advisories for:
1. Delayed onset of monsoon (>2 to 6 weeks delay)
2. Mid-season dry spells / extended rainfall breaks (>15 to 30 days)
3. Early monsoon withdrawal
4. Terminal heat shocks (>35 C during grain filling)
5. Flash flood inundation and post-submergence recovery
"""

from typing import List, Dict, Optional
from pydantic import BaseModel, Field


class ClimateShockScenario(BaseModel):
    region_id: str
    target_crop_original: str
    planned_sowing_window: str
    delay_weeks: int = 0
    dry_spell_duration_days: int = 0
    is_flooded: bool = False
    inundation_days: int = 0
    heat_wave_max_temp_c: float = 30.0


class ContingencyPrescription(BaseModel):
    scenario_type: str
    recommended_contingent_crops: List[str]
    alternate_varieties_short_duration: List[str]
    agronomic_mitigation_actions: List[str]
    foliar_spray_emergency_recipe: str
    irrigation_contingency_protocol: str
    expected_yield_loss_mitigated_pct: float


class AgroContingencyEngine:
    """
    Expert rule matrix for climate risk management and emergency cropping plans.
    """

    @classmethod
    def evaluate_shock(cls, scenario: ClimateShockScenario) -> ContingencyPrescription:
        # Case 1: Severe Delayed Onset (>4 weeks)
        if scenario.delay_weeks >= 4:
            return ContingencyPrescription(
                scenario_type="Severe Monsoon Delay (Over 4 Weeks)",
                recommended_contingent_crops=["pearl_millet", "greengram", "blackgram", "sesame_til", "horse_gram"],
                alternate_varieties_short_duration=["Greengram Pusa Vishal (60d)", "Pearl Millet HHB 67 (65d)", "Blackgram Pant U-31 (70d)"],
                agronomic_mitigation_actions=[
                    "Abandon long-duration paddy; shift immediately to direct-seeded pulses or millets",
                    "Adopt ridge and furrow sowing method for maximum in-situ rainwater harvesting",
                    "Increase seed rate by 20% to compensate for suboptimal germination",
                    "Apply anti-transpirant spray (Kaolin 5%) to reduce seedling transpiration shock",
                ],
                foliar_spray_emergency_recipe="Foliar spray of 2% Urea or 1% Potassium Nitrate (KNO3) to revive drought-stressed seedlings",
                irrigation_contingency_protocol="Provide life-saving irrigation at alternate furrows (deficit furrow irrigation)",
                expected_yield_loss_mitigated_pct=65.0,
            )

        # Case 2: Prolonged Mid-Season Dry Spell (>20 days)
        if scenario.dry_spell_duration_days >= 20:
            return ContingencyPrescription(
                scenario_type="Severe Mid-Season Drought Break",
                recommended_contingent_crops=["Retain standing crop with thinning"],
                alternate_varieties_short_duration=["In-situ moisture retention"],
                agronomic_mitigation_actions=[
                    "Perform crop thinning: remove alternate plants or alternate rows to conserve soil moisture",
                    "Remove older lower leaves (defoliation up to 25%) to minimize canopy transpiration area",
                    "Immediate inter-row dust mulching or organic straw mulching at 5 tons/ha",
                    "Spray Kaolin clay @ 50 g/L or Salicylic Acid @ 100 ppm to induce stomatal closure",
                ],
                foliar_spray_emergency_recipe="Foliar spray of 2% KCl (MOP) to induce osmotic adjustment and guard cell turgor maintenance",
                irrigation_contingency_protocol="Micro-drip irrigation scheduled exclusively during night hours to avert evaporative losses",
                expected_yield_loss_mitigated_pct=45.0,
            )

        # Case 3: Flash Flood / Inundation
        if scenario.is_flooded:
            return ContingencyPrescription(
                scenario_type="Flash Flood Inundation & Silt Encrustation",
                recommended_contingent_crops=["rice_swarna_sub1", "grass_pea", "field_pea", "maize_sweet"],
                alternate_varieties_short_duration=["Submergence tolerant cultivars", "Paira/utera relay pulses"],
                agronomic_mitigation_actions=[
                    "Dig drainage channels at field margins to evacuate standing surface water within 48 hours",
                    "Wash mud and silt deposit off crop leaves using clean water sprayers to restore photosynthetic activity",
                    "Hoeing and inter-cultivation as soon as soil reaches workable condition to break surface crust and aerate roots",
                    "Broadcast sprouted seeds of lathyrus or lentil into standing receding floodwaters (relay paira cropping)",
                ],
                foliar_spray_emergency_recipe="Foliar spray of 1% DAP + 0.5% ZnSO4 + 0.5% Urea to accelerate root restoration after anoxia",
                irrigation_contingency_protocol="Withhold irrigation; install sub-surface tile perforated drains to lower shallow water table",
                expected_yield_loss_mitigated_pct=50.0,
            )

        # Case 4: Terminal Heat Shock (>35 C at flowering/grain fill)
        if scenario.heat_wave_max_temp_c >= 35.0:
            return ContingencyPrescription(
                scenario_type="Terminal Heat Stress at Anthesis / Grain Fill",
                recommended_contingent_crops=["heat_tolerant_cultivars"],
                alternate_varieties_short_duration=["Wheat DBW 187", "Wheat HD 3086"],
                agronomic_mitigation_actions=[
                    "Light frequent sprinkler irrigations during peak afternoon hours to lower canopy temperature by 2-4 C",
                    "Foliar spray of alpha-tocopherol (Vitamin E) @ 150 ppm or Glycine betaine @ 1000 ppm",
                    "Avoid late afternoon harvesting; operate combine harvesters during cool night or early morning hours",
                ],
                foliar_spray_emergency_recipe="Spray 0.2% Borax + 1% Potassium Nitrate at flag leaf emergence to protect pollen viability",
                irrigation_contingency_protocol="Mist or micro-sprinkler misting for 15 minutes at 1:00 PM and 3:00 PM",
                expected_yield_loss_mitigated_pct=55.0,
            )

        # Normal condition
        return ContingencyPrescription(
            scenario_type="Normal Agronomic Advisory",
            recommended_contingent_crops=[scenario.target_crop_original],
            alternate_varieties_short_duration=["Standard Regional High Yielding Varieties"],
            agronomic_mitigation_actions=["Follow standard integrated crop management package of practices"],
            foliar_spray_emergency_recipe="Balanced micronutrient cocktail (Zn + Fe + B) at 45 DAS",
            irrigation_contingency_protocol="Irrigate according to FAO-56 depletion threshold (50% RAW)",
            expected_yield_loss_mitigated_pct=95.0,
        )
