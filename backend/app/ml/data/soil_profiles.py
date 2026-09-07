"""
AgroPulse Soil Taxonomy, Physical Hydro-Dynamics, and Nutrient Classification Matrix.
Synthesized from USDA-NRCS Soil Survey Manual, FAO World Reference Base (WRB),
and International Soil Reference and Information Centre (ISRIC).
"""

from typing import Dict, List, Optional, Tuple
from pydantic import BaseModel, Field


class SoilHydraulicProperties(BaseModel):
    texture_class: str
    sand_pct_typical: float
    silt_pct_typical: float
    clay_pct_typical: float
    bulk_density_g_cm3: float  # Typical dry bulk density
    porosity_pct: float
    field_capacity_vol_pct: float  # Volumetric water content at -33 kPa (θ_FC)
    wilting_point_vol_pct: float   # Volumetric water content at -1500 kPa (θ_PWP)
    available_water_capacity_mm_per_m: float  # Plant available water (AWC = θ_FC - θ_PWP)
    sat_hydraulic_conductivity_mm_hr: float  # K_sat infiltration rate
    infiltration_category: str  # Very Rapid, Rapid, Moderate, Slow, Very Slow
    erodibility_k_factor: float  # USLE K-factor


class SoilTaxonomyOrder(BaseModel):
    order: str
    description: str
    major_agricultural_regions: List[str]
    inherent_fertility: str  # High, Moderate, Low, Very Low
    predominant_minerals: List[str]
    drainage_characteristics: str
    management_challenges: List[str]


# USDA Texture Triangle Parameters & Hydraulic Constants
SOIL_HYDRAULIC_DATABASE: Dict[str, SoilHydraulicProperties] = {
    "sand": SoilHydraulicProperties(
        texture_class="Sand",
        sand_pct_typical=92.0,
        silt_pct_typical=5.0,
        clay_pct_typical=3.0,
        bulk_density_g_cm3=1.60,
        porosity_pct=39.6,
        field_capacity_vol_pct=10.0,
        wilting_point_vol_pct=4.0,
        available_water_capacity_mm_per_m=60.0,
        sat_hydraulic_conductivity_mm_hr=120.0,
        infiltration_category="Very Rapid",
        erodibility_k_factor=0.15,
    ),
    "loamy_sand": SoilHydraulicProperties(
        texture_class="Loamy Sand",
        sand_pct_typical=82.0,
        silt_pct_typical=12.0,
        clay_pct_typical=6.0,
        bulk_density_g_cm3=1.55,
        porosity_pct=41.5,
        field_capacity_vol_pct=14.0,
        wilting_point_vol_pct=6.0,
        available_water_capacity_mm_per_m=80.0,
        sat_hydraulic_conductivity_mm_hr=65.0,
        infiltration_category="Rapid",
        erodibility_k_factor=0.20,
    ),
    "sandy_loam": SoilHydraulicProperties(
        texture_class="Sandy Loam",
        sand_pct_typical=65.0,
        silt_pct_typical=25.0,
        clay_pct_typical=10.0,
        bulk_density_g_cm3=1.50,
        porosity_pct=43.4,
        field_capacity_vol_pct=20.0,
        wilting_point_vol_pct=9.0,
        available_water_capacity_mm_per_m=110.0,
        sat_hydraulic_conductivity_mm_hr=35.0,
        infiltration_category="Moderately Rapid",
        erodibility_k_factor=0.28,
    ),
    "loam": SoilHydraulicProperties(
        texture_class="Loam",
        sand_pct_typical=42.0,
        silt_pct_typical=40.0,
        clay_pct_typical=18.0,
        bulk_density_g_cm3=1.40,
        porosity_pct=47.2,
        field_capacity_vol_pct=27.0,
        wilting_point_vol_pct=12.0,
        available_water_capacity_mm_per_m=150.0,
        sat_hydraulic_conductivity_mm_hr=18.0,
        infiltration_category="Moderate",
        erodibility_k_factor=0.34,
    ),
    "silt_loam": SoilHydraulicProperties(
        texture_class="Silt Loam",
        sand_pct_typical=20.0,
        silt_pct_typical=65.0,
        clay_pct_typical=15.0,
        bulk_density_g_cm3=1.35,
        porosity_pct=49.1,
        field_capacity_vol_pct=32.0,
        wilting_point_vol_pct=13.0,
        available_water_capacity_mm_per_m=190.0,
        sat_hydraulic_conductivity_mm_hr=12.0,
        infiltration_category="Moderate",
        erodibility_k_factor=0.42,
    ),
    "silt": SoilHydraulicProperties(
        texture_class="Silt",
        sand_pct_typical=8.0,
        silt_pct_typical=85.0,
        clay_pct_typical=7.0,
        bulk_density_g_cm3=1.30,
        porosity_pct=50.9,
        field_capacity_vol_pct=33.0,
        wilting_point_vol_pct=12.0,
        available_water_capacity_mm_per_m=210.0,
        sat_hydraulic_conductivity_mm_hr=9.0,
        infiltration_category="Slow",
        erodibility_k_factor=0.48,
    ),
    "sandy_clay_loam": SoilHydraulicProperties(
        texture_class="Sandy Clay Loam",
        sand_pct_typical=55.0,
        silt_pct_typical=18.0,
        clay_pct_typical=27.0,
        bulk_density_g_cm3=1.48,
        porosity_pct=44.2,
        field_capacity_vol_pct=26.0,
        wilting_point_vol_pct=15.0,
        available_water_capacity_mm_per_m=110.0,
        sat_hydraulic_conductivity_mm_hr=10.0,
        infiltration_category="Slow",
        erodibility_k_factor=0.25,
    ),
    "clay_loam": SoilHydraulicProperties(
        texture_class="Clay Loam",
        sand_pct_typical=32.0,
        silt_pct_typical=34.0,
        clay_pct_typical=34.0,
        bulk_density_g_cm3=1.38,
        porosity_pct=47.9,
        field_capacity_vol_pct=33.0,
        wilting_point_vol_pct=18.0,
        available_water_capacity_mm_per_m=150.0,
        sat_hydraulic_conductivity_mm_hr=6.5,
        infiltration_category="Slow",
        erodibility_k_factor=0.30,
    ),
    "silty_clay_loam": SoilHydraulicProperties(
        texture_class="Silty Clay Loam",
        sand_pct_typical=12.0,
        silt_pct_typical=55.0,
        clay_pct_typical=33.0,
        bulk_density_g_cm3=1.35,
        porosity_pct=49.1,
        field_capacity_vol_pct=36.0,
        wilting_point_vol_pct=20.0,
        available_water_capacity_mm_per_m=160.0,
        sat_hydraulic_conductivity_mm_hr=4.5,
        infiltration_category="Slow",
        erodibility_k_factor=0.36,
    ),
    "sandy_clay": SoilHydraulicProperties(
        texture_class="Sandy Clay",
        sand_pct_typical=50.0,
        silt_pct_typical=8.0,
        clay_pct_typical=42.0,
        bulk_density_g_cm3=1.45,
        porosity_pct=45.3,
        field_capacity_vol_pct=31.0,
        wilting_point_vol_pct=21.0,
        available_water_capacity_mm_per_m=100.0,
        sat_hydraulic_conductivity_mm_hr=3.0,
        infiltration_category="Very Slow",
        erodibility_k_factor=0.20,
    ),
    "silty_clay": SoilHydraulicProperties(
        texture_class="Silty Clay",
        sand_pct_typical=8.0,
        silt_pct_typical=46.0,
        clay_pct_typical=46.0,
        bulk_density_g_cm3=1.32,
        porosity_pct=50.2,
        field_capacity_vol_pct=38.0,
        wilting_point_vol_pct=24.0,
        available_water_capacity_mm_per_m=140.0,
        sat_hydraulic_conductivity_mm_hr=2.0,
        infiltration_category="Very Slow",
        erodibility_k_factor=0.28,
    ),
    "clay": SoilHydraulicProperties(
        texture_class="Clay",
        sand_pct_typical=20.0,
        silt_pct_typical=22.0,
        clay_pct_typical=58.0,
        bulk_density_g_cm3=1.28,
        porosity_pct=51.7,
        field_capacity_vol_pct=42.0,
        wilting_point_vol_pct=27.0,
        available_water_capacity_mm_per_m=150.0,
        sat_hydraulic_conductivity_mm_hr=1.2,
        infiltration_category="Extremely Slow",
        erodibility_k_factor=0.22,
    ),
}


# USDA Soil Taxonomy Major Agricultural Orders
TAXONOMY_ORDERS: Dict[str, SoilTaxonomyOrder] = {
    "vertisols": SoilTaxonomyOrder(
        order="Vertisols",
        description="Shrink-swell heavy clay soils (black cotton soils) forming deep cracks upon drying and self-inversion churning.",
        major_agricultural_regions=["Deccan Plateau India", "Gezira Plain Sudan", "Blacklands Texas", "Eastern Australia"],
        inherent_fertility="High",
        predominant_minerals=["Montmorillonite", "Smectite"],
        drainage_characteristics="Imperfectly drained to poorly drained when wet; low saturated hydraulic conductivity.",
        management_challenges=["Very narrow moisture window for tillage", "Waterlogging during monsoons", "High draft power requirement"],
    ),
    "mollisols": SoilTaxonomyOrder(
        order="Mollisols",
        description="Dark, organic-matter-rich steppe and prairie grassland soils with mollic epipedon and high base saturation (>50%).",
        major_agricultural_regions=["US Corn Belt & Great Plains", "Pampas Argentina", "Chernozem Belt Ukraine & Russia"],
        inherent_fertility="Very High",
        predominant_minerals=["Illite", "Vermiculite", "Smectite"],
        drainage_characteristics="Well drained to moderately well drained.",
        management_challenges=["Wind and water erosion under clean tillage", "Secondary salinization under excessive irrigation"],
    ),
    "alfisols": SoilTaxonomyOrder(
        order="Alfisols",
        description="Moderately leached forest soils with subsurface clay accumulation (argillic horizon) and moderate-to-high base saturation.",
        major_agricultural_regions=["Midwestern US", "Central Europe", "Southern & Eastern India", "Eastern Brazil"],
        inherent_fertility="Moderate to High",
        predominant_minerals=["Kaolinite", "Illite", "Quartz"],
        drainage_characteristics="Well drained; susceptible to surface crusting upon drying.",
        management_challenges=["Surface crusting hampering seedling emergence", "Subsurface compaction", "P-fixation in acidic variants"],
    ),
    "inceptisols": SoilTaxonomyOrder(
        order="Inceptisols",
        description="Young, developing soils with weakly differentiated horizons; widespread in active floodplains and alluvial deltas.",
        major_agricultural_regions=["Indo-Gangetic Plain", "Yangtze River Basin", "Mekong Delta", "Mississippi Alluvial Valley"],
        inherent_fertility="Moderate to Very High",
        predominant_minerals=["Mixed 2:1 and 1:1 clays", "Mica", "Feldspar"],
        drainage_characteristics="Variable; ranges from well drained on terraces to poorly drained on low floodplains.",
        management_challenges=["Periodic flood vulnerability", "Nutrient depletion under intensive multi-cropping"],
    ),
    "ultisols": SoilTaxonomyOrder(
        order="Ultisols",
        description="Intensely weathered, strongly leached acidic red and yellow soils with low base saturation (<35%) and aluminum toxicity.",
        major_agricultural_regions=["Southeastern US", "Amazon Basin fringes", "Southeast Asia", "Northeastern India"],
        inherent_fertility="Low",
        predominant_minerals=["Kaolinite", "Gibbsite", "Goethite", "Hematite"],
        drainage_characteristics="Well drained, but low effective water holding capacity.",
        management_challenges=["Subsoil aluminum toxicity (Al3+)", "Severe phosphorus fixation", "Frequent liming required"],
    ),
    "aridisols": SoilTaxonomyOrder(
        order="Aridisols",
        description="Dryland desert soils with ochric epipedon, accumulated soluble salts, gypsum, or calcium carbonate (caliche) horizons.",
        major_agricultural_regions=["Middle East", "North Africa", "Thar Desert India/Pakistan", "Western Australia", "US Desert Southwest"],
        inherent_fertility="Low to Moderate (chemically rich, biologically limited)",
        predominant_minerals=["Calcite", "Gypsum", "Halite", "Quartz"],
        drainage_characteristics="Excessively drained in sands, or impermeable calcic hardpans.",
        management_challenges=["Severe water deficit", "Salinity and sodicity hazards", "Micronutrient deficiency (Fe, Zn due to high pH)"],
    ),
}


# Chemical Interpretation & Rating Thresholds
class NutrientRatingInterpretation:
    """Classifies chemical test values into standardized Low / Medium / High / Critical agronomic categories."""

    @staticmethod
    def classify_nitrogen_kg_ha(val: float) -> str:
        """Available soil Nitrogen (Alkaline KMnO4 method) in kg/ha."""
        if val < 280.0:
            return "Low (Deficit)"
        elif val <= 560.0:
            return "Medium (Adequate)"
        else:
            return "High (Surplus)"

    @staticmethod
    def classify_phosphorus_kg_ha(val: float, is_alkaline_soil: bool = False) -> str:
        """Available soil Phosphorus (Olsen P for alkaline/neutral or Bray P for acidic) in kg P2O5/ha."""
        threshold_low = 23.0 if is_alkaline_soil else 20.0
        threshold_high = 56.0 if is_alkaline_soil else 50.0

        if val < threshold_low:
            return "Low (Deficit)"
        elif val <= threshold_high:
            return "Medium (Adequate)"
        else:
            return "High (Surplus)"

    @staticmethod
    def classify_potassium_kg_ha(val: float) -> str:
        """Available soil Potassium (Neutral 1N Ammonium Acetate method) in kg K2O/ha."""
        if val < 140.0:
            return "Low (Deficit)"
        elif val <= 280.0:
            return "Medium (Adequate)"
        else:
            return "High (Surplus)"

    @staticmethod
    def classify_ph(val: float) -> Tuple[str, str]:
        """Classifies pH and provides soil reaction diagnosis and corrective amendment recommendation."""
        if val < 4.5:
            return ("Extremely Acidic", "Severe Al and Mn toxicity, P fixation. Mandatory heavy agricultural liming (CaCO3).")
        elif val < 5.5:
            return ("Strongly Acidic", "Moderate P fixation, low base saturation. Apply agricultural lime or dolomite.")
        elif val < 6.5:
            return ("Moderately Acidic", "Generally favorable for acid-loving crops (tea, potato, pulses). Light liming may benefit cereals.")
        elif val <= 7.5:
            return ("Neutral / Optimal", "Peak bioavailability for nearly all primary, secondary, and micronutrients.")
        elif val <= 8.5:
            return ("Moderately Alkaline", "Calcareous soil. Phosphorus and micronutrient (Zn, Fe, Mn) availability reduced. Use acid-forming fertilizers.")
        elif val <= 9.0:
            return ("Strongly Alkaline", "High exchangeable sodium percentage (ESP). Sodic hazard. Gypsum (CaSO4·2H2O) application required.")
        else:
            return ("Very Strongly Alkaline / Sodic", "Severe dispersion, black alkali soil. Heavy gypsum and leaching required before cultivation.")

    @staticmethod
    def classify_electrical_conductivity_ds_m(val: float) -> Tuple[str, str]:
        """Electrical conductivity of saturation extract (ECe) in dS/m at 25°C."""
        if val < 1.0:
            return ("Non-Saline", "No crop restriction; optimal for all salt-sensitive crops.")
        elif val <= 2.0:
            return ("Very Slightly Saline", "Negligible restriction; very sensitive vegetables may show mild yield decrease.")
        elif val <= 4.0:
            return ("Moderately Saline", "Yield of sensitive crops restricted. Switch to moderately tolerant cultivars.")
        elif val <= 8.0:
            return ("Saline", "Yield of many crops restricted. Only tolerant crops (barley, cotton, sugarbeet) produce economical yields.")
        else:
            return ("Severely Saline", "Only halophytes and highly tolerant crops survive. Subsurface drainage and leaching essential.")

    @staticmethod
    def classify_organic_carbon_pct(val: float) -> str:
        """Soil Organic Carbon (SOC) percentage (Walkley-Black chromic acid method)."""
        if val < 0.50:
            return "Very Low (Depleted - High response to compost/FYM)"
        elif val <= 0.75:
            return "Medium (Moderate biological activity)"
        else:
            return "High (Rich biological health & aggregation)"


def determine_texture_from_fractions(sand_pct: float, silt_pct: float, clay_pct: float) -> str:
    """
    Classify USDA soil texture triangle given Sand, Silt, and Clay percentages.
    Ensures normalized sum to 100%.
    """
    total = sand_pct + silt_pct + clay_pct
    if total <= 0:
        return "loam"

    s = (sand_pct / total) * 100.0
    si = (silt_pct / total) * 100.0
    c = (clay_pct / total) * 100.0

    if c >= 40.0:
        if s >= 45.0:
            return "sandy_clay"
        elif si >= 40.0:
            return "silty_clay"
        else:
            return "clay"
    elif c >= 27.0:
        if s >= 45.0:
            return "sandy_clay_loam"
        elif s <= 20.0:
            return "silty_clay_loam"
        else:
            return "clay_loam"
    elif c >= 7.0:
        if si >= 50.0:
            return "silt_loam"
        elif s >= 52.0:
            return "sandy_loam"
        else:
            return "loam"
    else:  # Clay < 7%
        if si >= 80.0:
            return "silt"
        elif s >= 85.0:
            return "sand"
        elif s >= 70.0:
            return "loamy_sand"
        else:
            return "sandy_loam"
