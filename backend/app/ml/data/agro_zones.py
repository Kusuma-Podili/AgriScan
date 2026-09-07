"""
AgroPulse Agro-Ecological Zones (AEZ) and Cropping Systems Matrix.
Detailed regional classifications according to ICAR, FAO, and USDA agro-climatic zoning.
Includes soil associations, rainfall patterns, predominant cropping sequences, and contingent drought plans.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class AgroClimaticZone(BaseModel):
    zone_id: str
    zone_name: str
    geographical_region: str
    annual_rainfall_min_mm: float
    annual_rainfall_max_mm: float
    major_soil_types: List[str]
    temperature_summer_mean_c: float
    temperature_winter_mean_c: float
    growing_season_length_days: int
    predominant_kharif_crops: List[str]
    predominant_rabi_crops: List[str]
    predominant_zaid_summer_crops: List[str]
    contingent_drought_crops: List[str]
    irrigation_coverage_pct: float
    groundwater_status: str  # Safe, Semi-critical, Critical, Over-exploited
    primary_agronomic_constraints: List[str]
    recommended_intercropping_systems: List[str]


AGRO_ECOLOGICAL_ZONES: Dict[str, AgroClimaticZone] = {
    "zone_01_western_himalayan": AgroClimaticZone(
        zone_id="zone_01_western_himalayan",
        zone_name="Western Himalayan Cold Sub-Humid Zone",
        geographical_region="Jammu & Kashmir, Himachal Pradesh, Uttarakhand Hills",
        annual_rainfall_min_mm=1000.0,
        annual_rainfall_max_mm=2200.0,
        major_soil_types=["Brown Hill Soils", "Mountain Meadow Soils", "Podsolic Soils", "Skeletal Soils"],
        temperature_summer_mean_c=22.0,
        temperature_winter_mean_c=4.0,
        growing_season_length_days=150,
        predominant_kharif_crops=["maize", "rice", "finger_millet", "soybean"],
        predominant_rabi_crops=["wheat", "barley", "mustard", "lentil"],
        predominant_zaid_summer_crops=["vegetables", "fodder"],
        contingent_drought_crops=["barley", "buckwheat", "amaranth", "foxtail_millet"],
        irrigation_coverage_pct=22.0,
        groundwater_status="Safe (Spring fed)",
        primary_agronomic_constraints=["Steep slope erosion", "Severe winter frost", "Acidic soil reaction (pH 5.0-5.8)", "Micronutrient boron and zinc deficiency"],
        recommended_intercropping_systems=["Maize + Soybean (2:1 row ratio)", "Apple Orchard + Red Clover Grass cover", "Wheat + Mustard (8:1)"],
    ),

    "zone_02_eastern_himalayan": AgroClimaticZone(
        zone_id="zone_02_eastern_himalayan",
        zone_name="Eastern Himalayan Warm Per-Humid Zone",
        geographical_region="Assam, Arunachal Pradesh, Meghalaya, Nagaland, Manipur, Tripura, Mizoram, Sikkim",
        annual_rainfall_min_mm=1800.0,
        annual_rainfall_max_mm=4000.0,
        major_soil_types=["Red Sandy Soils", "Laterite Soils", "Alluvial Riverine Soils"],
        temperature_summer_mean_c=28.0,
        temperature_winter_mean_c=12.0,
        growing_season_length_days=300,
        predominant_kharif_crops=["rice", "jute", "tea", "maize"],
        predominant_rabi_crops=["mustard", "potato", "lentil", "wheat"],
        predominant_zaid_summer_crops=["blackgram", "vegetables"],
        contingent_drought_crops=["foxtail_millet", "greengram"],
        irrigation_coverage_pct=15.0,
        groundwater_status="Safe",
        primary_agronomic_constraints=["Severe soil acidity (pH 4.2-5.2)", "High aluminum toxicity", "Flash floods during monsoon", "Shifting cultivation (Jhum) degradation"],
        recommended_intercropping_systems=["Rice + Fish + Azolla integrated farming", "Tea + Silver Oak Shade Trees", "Maize + Blackgram (2:2)"],
    ),

    "zone_03_lower_gangetic_plain": AgroClimaticZone(
        zone_id="zone_03_lower_gangetic_plain",
        zone_name="Lower Gangetic Plain Wet Alluvial Zone",
        geographical_region="West Bengal Delta, Coastal Sundarbans",
        annual_rainfall_min_mm=1400.0,
        annual_rainfall_max_mm=2000.0,
        major_soil_types=["Deltaic Alluvium", "Coastal Saline Clay Soils", "Laterite Soils"],
        temperature_summer_mean_c=31.0,
        temperature_winter_mean_c=17.0,
        growing_season_length_days=320,
        predominant_kharif_crops=["rice", "jute"],
        predominant_rabi_crops=["potato", "mustard", "rice", "wheat"],
        predominant_zaid_summer_crops=["sesame", "greengram", "sunflower"],
        contingent_drought_crops=["sesame", "greengram"],
        irrigation_coverage_pct=62.0,
        groundwater_status="Semi-critical to Critical (Arsenic contamination zones)",
        primary_agronomic_constraints=["Coastal salinity ingress during dry season", "Waterlogging in saucer basins", "Arsenic contamination in shallow groundwater"],
        recommended_intercropping_systems=["Jute followed by Aman Paddy relay", "Potato + Maize relay", "Rice + Sesame"],
    ),

    "zone_04_middle_gangetic_plain": AgroClimaticZone(
        zone_id="zone_04_middle_gangetic_plain",
        zone_name="Middle Gangetic Plain Moist Sub-Humid Zone",
        geographical_region="Eastern Uttar Pradesh, Bihar",
        annual_rainfall_min_mm=1000.0,
        annual_rainfall_max_mm=1450.0,
        major_soil_types=["Deep Loamy Alluvial Soils", "Calcareous Silt Loam (Bhat)", "Clayey Alluvium (Kharagpur / Karail)"],
        temperature_summer_mean_c=34.0,
        temperature_winter_mean_c=14.0,
        growing_season_length_days=270,
        predominant_kharif_crops=["rice", "maize", "pigeonpea", "sugarcane"],
        predominant_rabi_crops=["wheat", "chickpea", "lentil", "mustard", "potato"],
        predominant_zaid_summer_crops=["greengram", "maize", "vegetables"],
        contingent_drought_crops=["pearl_millet", "sorghum", "greengram"],
        irrigation_coverage_pct=68.0,
        groundwater_status="Safe to Semi-critical",
        primary_agronomic_constraints=["Calcareous chlorosis (high free CaCO3 binding Zinc and Iron)", "Floods in north of Ganges, terminal heat stress in rabi wheat"],
        recommended_intercropping_systems=["Sugarcane + Potato (1:2)", "Maize + Pigeonpea (1:1)", "Wheat + Mustard (9:1)"],
    ),

    "zone_05_upper_gangetic_plain": AgroClimaticZone(
        zone_id="zone_05_upper_gangetic_plain",
        zone_name="Upper Gangetic Plain Sub-Humid Deep Alluvial Zone",
        geographical_region="Central & Western Uttar Pradesh",
        annual_rainfall_min_mm=750.0,
        annual_rainfall_max_mm=1100.0,
        major_soil_types=["Alluvial Loam", "Sandy Loam", "Saline-Alkali Usar Soils"],
        temperature_summer_mean_c=35.0,
        temperature_winter_mean_c=12.0,
        growing_season_length_days=240,
        predominant_kharif_crops=["rice", "sugarcane", "maize", "pearl_millet", "pigeonpea"],
        predominant_rabi_crops=["wheat", "mustard", "potato", "chickpea"],
        predominant_zaid_summer_crops=["greengram", "fodder_sorghum"],
        contingent_drought_crops=["pearl_millet", "sorghum", "cluster_bean"],
        irrigation_coverage_pct=85.0,
        groundwater_status="Critical to Over-exploited",
        primary_agronomic_constraints=["Rapidly declining water table due to heavy tube well pumping", "Soil sodicity (high ESP)", "High burning of crop residues"],
        recommended_intercropping_systems=["Sugarcane + Mustard (autumn)", "Pigeonpea + Greengram (1:2)", "Wheat + Chickpea (4:2)"],
    ),

    "zone_06_trans_gangetic_plain": AgroClimaticZone(
        zone_id="zone_06_trans_gangetic_plain",
        zone_name="Trans-Gangetic Plain Semi-Arid Intensive Zone",
        geographical_region="Punjab, Haryana, Delhi, Chandigarh, Northern Rajasthan",
        annual_rainfall_min_mm=400.0,
        annual_rainfall_max_mm=750.0,
        major_soil_types=["Deep Alluvial Loam", "Calcareous Sandy Loam", "Desert Sands in South"],
        temperature_summer_mean_c=36.0,
        temperature_winter_mean_c=10.0,
        growing_season_length_days=210,
        predominant_kharif_crops=["rice", "cotton", "maize", "pearl_millet", "sugarcane"],
        predominant_rabi_crops=["wheat", "mustard", "barley", "chickpea", "potato"],
        predominant_zaid_summer_crops=["greengram", "sunflower", "fodder"],
        contingent_drought_crops=["pearl_millet", "moth_bean", "cluster_bean"],
        irrigation_coverage_pct=95.0,
        groundwater_status="Over-exploited (>140% extraction)",
        primary_agronomic_constraints=["Severe groundwater depletion", "Rice-wheat monoculture soil fatigue", "Subsoil compaction hardpan at 20 cm", "Terminal heat stress"],
        recommended_intercropping_systems=["Cotton + Greengram (1:2)", "Wheat + Mustard (8:1)", "Sugarcane + Onion"],
    ),

    "zone_07_eastern_plateau_hills": AgroClimaticZone(
        zone_id="zone_07_eastern_plateau_hills",
        zone_name="Eastern Plateau & Hills Sub-Humid Red & Laterite Zone",
        geographical_region="Jharkhand, Chhota Nagpur, Chhattisgarh Hills, Western Odisha",
        annual_rainfall_min_mm=1200.0,
        annual_rainfall_max_mm=1600.0,
        major_soil_types=["Red Gravelly Soils", "Laterite Soils", "Red & Yellow Loams"],
        temperature_summer_mean_c=33.0,
        temperature_winter_mean_c=15.0,
        growing_season_length_days=200,
        predominant_kharif_crops=["rice", "maize", "finger_millet", "pigeonpea", "groundnut"],
        predominant_rabi_crops=["chickpea", "lentil", "mustard", "wheat", "linseed"],
        predominant_zaid_summer_crops=["vegetables", "watermelon"],
        contingent_drought_crops=["finger_millet", "blackgram", "niger_seed", "horse_gram"],
        irrigation_coverage_pct=20.0,
        groundwater_status="Safe (Low storage hard rock aquifer)",
        primary_agronomic_constraints=["High surface runoff on undulating terrain", "Severe soil erosion", "Low moisture retention in upland soils", "Soil acidity and phosphorus fixation"],
        recommended_intercropping_systems=["Upland Rice + Pigeonpea (3:1)", "Finger Millet + Red Gram (4:2)", "Groundnut + Pigeonpea (3:1)"],
    ),

    "zone_08_central_plateau_hills": AgroClimaticZone(
        zone_id="zone_08_central_plateau_hills",
        zone_name="Central Plateau & Hills Semi-Arid Black & Red Zone",
        geographical_region="Madhya Pradesh, Bundelkhand, Southern Uttar Pradesh, Southeastern Rajasthan",
        annual_rainfall_min_mm=750.0,
        annual_rainfall_max_mm=1200.0,
        major_soil_types=["Medium Black Clay Soils (Vertic Inceptisols)", "Mixed Red & Black Soils", "Shallow Skeletal Soils"],
        temperature_summer_mean_c=36.0,
        temperature_winter_mean_c=14.0,
        growing_season_length_days=180,
        predominant_kharif_crops=["soybean", "cotton", "pigeonpea", "blackgram", "sorghum"],
        predominant_rabi_crops=["wheat", "chickpea", "mustard", "coriander", "garlic"],
        predominant_zaid_summer_crops=["greengram", "groundnut"],
        contingent_drought_crops=["sorghum", "pearl_millet", "cluster_bean", "blackgram"],
        irrigation_coverage_pct=38.0,
        groundwater_status="Semi-critical to Critical",
        primary_agronomic_constraints=["Soil crusting on red soils", "Waterlogging followed by deep shrinkage cracking on vertisols", "Recurrent mid-season dry spells in Bundelkhand"],
        recommended_intercropping_systems=["Soybean + Pigeonpea (4:2)", "Sorghum + Pigeonpea (2:1)", "Chickpea + Mustard (6:1)"],
    ),

    "zone_09_western_plateau_hills": AgroClimaticZone(
        zone_id="zone_09_western_plateau_hills",
        zone_name="Western Plateau & Hills Semi-Arid Vertisol Zone",
        geographical_region="Maharashtra (Vidarbha, Marathwada, Khandesh), Malwa MP",
        annual_rainfall_min_mm=600.0,
        annual_rainfall_max_mm=1000.0,
        major_soil_types=["Deep Black Soils (Vertisols)", "Medium Black Soils", "Shallow Murrum Soils"],
        temperature_summer_mean_c=37.0,
        temperature_winter_mean_c=16.0,
        growing_season_length_days=160,
        predominant_kharif_crops=["cotton", "soybean", "pigeonpea", "sorghum", "greengram"],
        predominant_rabi_crops=["chickpea", "sorghum", "wheat", "safflower", "onion"],
        predominant_zaid_summer_crops=["groundnut", "vegetables"],
        contingent_drought_crops=["pearl_millet", "sorghum", "pigeonpea", "sesame"],
        irrigation_coverage_pct=24.0,
        groundwater_status="Critical (Deccan trap basalt fractures)",
        primary_agronomic_constraints=["Rainshadow drought vulnerability", "Heavy clay vertisol workability challenges", "Pink bollworm in cotton", "Terminal drought during rabi"],
        recommended_intercropping_systems=["Cotton + Greengram / Blackgram (1:2)", "Soybean + Pigeonpea (4:2)", "Rabi Sorghum + Safflower (3:1)"],
    ),

    "zone_10_southern_plateau_hills": AgroClimaticZone(
        zone_id="zone_10_southern_plateau_hills",
        zone_name="Southern Plateau & Hills Semi-Arid Red Sandy Loam Zone",
        geographical_region="Telangana, Rayalaseema AP, North & Central Karnataka, Western Tamil Nadu",
        annual_rainfall_min_mm=550.0,
        annual_rainfall_max_mm=950.0,
        major_soil_types=["Red Sandy Loam (Chalka)", "Medium Black Soils", "Deep Red Soils"],
        temperature_summer_mean_c=36.0,
        temperature_winter_mean_c=19.0,
        growing_season_length_days=150,
        predominant_kharif_crops=["groundnut", "cotton", "maize", "pigeonpea", "finger_millet"],
        predominant_rabi_crops=["chickpea", "sorghum", "sunflower", "safflower"],
        predominant_zaid_summer_crops=["groundnut", "sesame"],
        contingent_drought_crops=["foxtail_millet", "pearl_millet", "horse_gram", "castor"],
        irrigation_coverage_pct=32.0,
        groundwater_status="Over-exploited in granite hard rocks",
        primary_agronomic_constraints=["Frequent prolonged dry spells during flowering", "Low soil water holding capacity of red soils", "Zinc and iron chlorosis in alkaline black patches"],
        recommended_intercropping_systems=["Groundnut + Pigeonpea (7:1 or 8:2)", "Finger Millet + Pigeonpea (8:2)", "Cotton + Cluster Bean (1:1)"],
    ),

    "zone_11_east_coast_plains": AgroClimaticZone(
        zone_id="zone_11_east_coast_plains",
        zone_name="East Coast Plains & Hills Deltaic Sub-Humid Zone",
        geographical_region="Coastal Odisha, Coastal Andhra Pradesh, Coastal Tamil Nadu",
        annual_rainfall_min_mm=1000.0,
        annual_rainfall_max_mm=1500.0,
        major_soil_types=["Coastal Alluvium", "Deltaic Clayey Alluvium", "Saline Coastal Soils"],
        temperature_summer_mean_c=34.0,
        temperature_winter_mean_c=22.0,
        growing_season_length_days=290,
        predominant_kharif_crops=["rice", "sugarcane", "cotton", "blackgram"],
        predominant_rabi_crops=["rice", "blackgram", "greengram", "groundnut", "maize"],
        predominant_zaid_summer_crops=["sesame", "vegetables"],
        contingent_drought_crops=["sesame", "greengram", "pearl_millet"],
        irrigation_coverage_pct=72.0,
        groundwater_status="Semi-critical to Saline Intrusion",
        primary_agronomic_constraints=["Cyclonic storms and inundation during October-November Northeast Monsoon", "Saline coastal water intrusion", "Poor drainage in delta tails"],
        recommended_intercropping_systems=["Rice followed by Rice Fallow Blackgram (Zero tillage relay)", "Sugarcane + Sunn Hemp (green manure)", "Coconut + Banana + Turmeric multi-tier"],
    ),

    "zone_12_west_coast_plains_ghats": AgroClimaticZone(
        zone_id="zone_12_west_coast_plains_ghats",
        zone_name="West Coast Plains & Ghats Humid Tropical Zone",
        geographical_region="Konkan, Goa, Coastal Karnataka, Kerala, Nilgiris",
        annual_rainfall_min_mm=2200.0,
        annual_rainfall_max_mm=3800.0,
        major_soil_types=["Laterite Soils", "Red Sandy Clay Soils", "Coastal Sandy Alluvium"],
        temperature_summer_mean_c=31.0,
        temperature_winter_mean_c=23.0,
        growing_season_length_days=310,
        predominant_kharif_crops=["rice", "coconut", "rubber", "arecanut", "black_pepper", "cardamom", "tea", "coffee"],
        predominant_rabi_crops=["rice", "pulses", "sweet_potato", "vegetables"],
        predominant_zaid_summer_crops=["sesame", "cowpea"],
        contingent_drought_crops=["finger_millet", "cowpea"],
        irrigation_coverage_pct=40.0,
        groundwater_status="Safe (Rapid surface discharge into Arabian Sea)",
        primary_agronomic_constraints=["Heavy nutrient leaching (K, Ca, Mg) under torrential monsoon rainfall", "High soil acidity and aluminum/iron toxicity", "Quick wilt and fungal epidemics"],
        recommended_intercropping_systems=["Coconut + Black Pepper on palms + Banana + Pineapple multi-tier", "Arecanut + Cocoa + Nutmeg", "Rubber + Pineapple (first 3 years)"],
    ),

    "zone_13_gujarat_plains_hills": AgroClimaticZone(
        zone_id="zone_13_gujarat_plains_hills",
        zone_name="Gujarat Plains & Hills Semi-Arid Commercial Zone",
        geographical_region="Gujarat, Saurashtra, Kutch",
        annual_rainfall_min_mm=350.0,
        annual_rainfall_max_mm=950.0,
        major_soil_types=["Medium Black Clay Soils", "Alluvial Sandy Loams (Goradu)", "Coastal Saline Marsh Soils (Bhal)"],
        temperature_summer_mean_c=37.0,
        temperature_winter_mean_c=16.0,
        growing_season_length_days=150,
        predominant_kharif_crops=["cotton", "groundnut", "castor", "sesame", "pearl_millet"],
        predominant_rabi_crops=["wheat", "mustard", "cumin", "fennel", "chickpea", "potato"],
        predominant_zaid_summer_crops=["pearl_millet", "groundnut", "sesame"],
        contingent_drought_crops=["pearl_millet", "cluster_bean", "moth_bean", "castor"],
        irrigation_coverage_pct=48.0,
        groundwater_status="Critical in Mehsana / North Gujarat, Saline in Coastal Saurashtra",
        primary_agronomic_constraints=["Severe coastal salinity and inland sodicity", "High fluoride and TDS in irrigation groundwater", "High climate volatility and recurrent droughts in Saurashtra/Kutch"],
        recommended_intercropping_systems=["Cotton + Groundnut (1:2)", "Castor + Greengram (1:2)", "Groundnut + Pigeonpea (3:1)"],
    ),

    "zone_14_western_dry": AgroClimaticZone(
        zone_id="zone_14_western_dry",
        zone_name="Western Dry Arid Desert Zone",
        geographical_region="Western Rajasthan (Thar Desert - Jodhpur, Bikaner, Jaisalmer, Barmer, Churu)",
        annual_rainfall_min_mm=100.0,
        annual_rainfall_max_mm=380.0,
        major_soil_types=["Desert Dune Sands", "Gypsiferous Soils", "Calcareous Lithosols"],
        temperature_summer_mean_c=43.0,
        temperature_winter_mean_c=8.0,
        growing_season_length_days=90,
        predominant_kharif_crops=["pearl_millet", "cluster_bean", "moth_bean", "sesame"],
        predominant_rabi_crops=["mustard", "chickpea", "wheat", "cumin", "isabgol"],
        predominant_zaid_summer_crops=["fodder"],
        contingent_drought_crops=["moth_bean", "cluster_bean", "cenchrus_grass"],
        irrigation_coverage_pct=26.0,
        groundwater_status="Extremely Deep & Saline; Indira Gandhi Canal (IGNP) Command",
        primary_agronomic_constraints=["Severe water scarcity and hyper-aridity", "Wind erosion and shifting sand dunes", "Extremes of diurnal temperature (-2°C to 49°C)", "Soil salinity"],
        recommended_intercropping_systems=["Pearl Millet + Cluster Bean (2:1)", "Moth Bean + Pearl Millet (2:1)", "Khejri (Prosopis cineraria) Agroforestry + Pearl Millet"],
    ),

    "zone_15_island_zone": AgroClimaticZone(
        zone_id="zone_15_island_zone",
        zone_name="Island Equatorial Zone",
        geographical_region="Andaman & Nicobar Islands, Lakshadweep Archipelago",
        annual_rainfall_min_mm=2600.0,
        annual_rainfall_max_mm=3200.0,
        major_soil_types=["Coral Sands (Lakshadweep)", "Marine Alluvium", "Humid Red Loams"],
        temperature_summer_mean_c=30.0,
        temperature_winter_mean_c=24.0,
        growing_season_length_days=340,
        predominant_kharif_crops=["coconut", "rice", "arecanut", "banana", "tapioca"],
        predominant_rabi_crops=["pulses", "vegetables"],
        predominant_zaid_summer_crops=["fruits"],
        contingent_drought_crops=["cowpea", "sweet_potato"],
        irrigation_coverage_pct=8.0,
        groundwater_status="Fragile thin freshwater lens floating on seawater",
        primary_agronomic_constraints=["Extremely thin freshwater aquifer (vulnerable to salinization)", "Heavy maritime wind storms", "Phosphorus deficiency in coral sands"],
        recommended_intercropping_systems=["Coconut + Banana + Gliricidia green manure", "Arecanut + Spices multi-tier", "Marine Algal Bio-farming"],
    ),
}


def get_zone_by_id(zone_id: str) -> Optional[AgroClimaticZone]:
    """Retrieve agro-climatic zone parameters by identifier."""
    return AGRO_ECOLOGICAL_ZONES.get(zone_id.lower().strip())


def find_zone_by_region_keyword(keyword: str) -> List[AgroClimaticZone]:
    """Search zones matching state or region keyword."""
    kw = keyword.lower().strip()
    return [z for z in AGRO_ECOLOGICAL_ZONES.values() if kw in z.geographical_region.lower() or kw in z.zone_name.lower()]
