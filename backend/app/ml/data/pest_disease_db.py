"""
AgroPulse Agricultural Pest and Plant Pathogen Knowledge Base.
Epidemiological models, microclimatic disease risk indices, and IPM advisory protocols.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class PestDiseaseProfile(BaseModel):
    id: str
    name: str
    scientific_name: str
    organism_type: str  # Fungus, Bacterium, Virus, Insect Pest, Nematode, Oomycete
    target_crops: List[str]

    # Epidemiological Weather Triggers
    temp_min_c: float
    temp_opt_min_c: float
    temp_opt_max_c: float
    temp_max_c: float
    humidity_min_pct: float
    leaf_wetness_hours_threshold: float  # Continuous hours of free moisture/dew needed for spore germination
    rainfall_correlation: str  # Positive (requires splashing), Negative, Neutral

    # Symptoms & Diagnostics
    symptoms_vegetative: str
    symptoms_reproductive: str

    # Integrated Pest Management (IPM) Controls
    biological_controls: List[str]
    cultural_controls: List[str]
    chemical_active_ingredients: List[str]
    economic_threshold_level: str


PEST_DISEASE_DATABASE: Dict[str, PestDiseaseProfile] = {
    # -------------------------------------------------------------
    # 1. MAJOR FUNGAL & OOMYCETE DISEASES
    # -------------------------------------------------------------
    "rice_blast": PestDiseaseProfile(
        id="rice_blast",
        name="Rice Blast (Magnaporthe oryzae)",
        scientific_name="Magnaporthe oryzae (Pyricularia oryzae)",
        organism_type="Fungus",
        target_crops=["rice", "finger_millet"],
        temp_min_c=17.0,
        temp_opt_min_c=22.0,
        temp_opt_max_c=28.0,
        temp_max_c=32.0,
        humidity_min_pct=88.0,
        leaf_wetness_hours_threshold=8.0,
        rainfall_correlation="Positive",
        symptoms_vegetative="Spindle-shaped lesions with brown borders and grey centers on leaf blades. Severe coalescence causes leaf blighting.",
        symptoms_reproductive="Neck blast attacks the panicle node causing blackening, panicle breakage, and complete grain chaffiness.",
        biological_controls=["Pseudomonas fluorescens seed treatment (10 g/kg) and foliar spray (0.2%)"],
        cultural_controls=["Avoid excessive nitrogenous fertilizer application", "Drain excess standing water periodically", "Burn infected stubbles"],
        chemical_active_ingredients=["Tricyclazole 75% WP @ 0.6 g/L", "Azoxystrobin 18.2% + Difenoconazole 11.4% SC @ 1 ml/L", "Isoprothiolane 40% EC @ 1.5 ml/L"],
        economic_threshold_level="1-2% leaf area covered at tillering or 1% neck blast incidence at heading.",
    ),

    "potato_late_blight": PestDiseaseProfile(
        id="potato_late_blight",
        name="Late Blight of Potato & Tomato",
        scientific_name="Phytophthora infestans",
        organism_type="Oomycete",
        target_crops=["potato", "tomato"],
        temp_min_c=8.0,
        temp_opt_min_c=15.0,
        temp_opt_max_c=21.0,
        temp_max_c=26.0,
        humidity_min_pct=90.0,
        leaf_wetness_hours_threshold=10.0,
        rainfall_correlation="Positive",
        symptoms_vegetative="Water-soaked dark necrotic lesions starting from leaf tips and margins. White cottony downy growth on undersides of leaves during humid mornings.",
        symptoms_reproductive="Purplish-brown dry rot on tubers; foul odor following secondary bacterial invasion.",
        biological_controls=["Trichoderma viride soil application", "Bio-fungicides based on Bacillus subtilis"],
        cultural_controls=["Certified disease-free seed tubers", "Wide row spacing to maximize airflow", "Dehaulming 10-12 days prior to harvest"],
        chemical_active_ingredients=["Mancozeb 75% WP (prophylactic) @ 2.5 g/L", "Metalaxyl 8% + Mancozeb 64% WP @ 2.5 g/L", "Cymoxanil 8% + Mancozeb 64% WP @ 2.0 g/L", "Dimethomorph 50% WP @ 1.0 g/L"],
        economic_threshold_level="First appearance of sporadic water-soaked lesions in vicinity under cool humid weather.",
    ),

    "wheat_rust_complex": PestDiseaseProfile(
        id="wheat_rust_complex",
        name="Wheat Stripe / Yellow Rust",
        scientific_name="Puccinia striiformis f.sp. tritici",
        organism_type="Fungus",
        target_crops=["wheat", "barley"],
        temp_min_c=2.0,
        temp_opt_min_c=10.0,
        temp_opt_max_c=16.0,
        temp_max_c=23.0,
        humidity_min_pct=85.0,
        leaf_wetness_hours_threshold=6.0,
        rainfall_correlation="Positive",
        symptoms_vegetative="Bright yellow pustules (uredinia) arranged in distinct parallel stripes/stripes along the leaf veins.",
        symptoms_reproductive="Pustules can develop on leaf sheaths, stems, and glumes, starving grain filling.",
        biological_controls=["Resistant cultivars (Yr genes pyramiding)"],
        cultural_controls=["Timely sowing in November", "Eradication of self-sown volunteer wheat plants"],
        chemical_active_ingredients=["Propiconazole 25% EC @ 1 ml/L", "Tebuconazole 25.9% EC @ 1 ml/L"],
        economic_threshold_level="5-10% rust pustule coverage on flag leaves.",
    ),

    "downy_mildew_grape": PestDiseaseProfile(
        id="downy_mildew_grape",
        name="Grapevine Downy Mildew",
        scientific_name="Plasmopara viticola",
        organism_type="Oomycete",
        target_crops=["grapes"],
        temp_min_c=12.0,
        temp_opt_min_c=20.0,
        temp_opt_max_c=26.0,
        temp_max_c=32.0,
        humidity_min_pct=85.0,
        leaf_wetness_hours_threshold=8.0,
        rainfall_correlation="Positive",
        symptoms_vegetative="'Oil spot' translucent yellow lesions on upper leaf surface, with dense white downy sporulation underneath.",
        symptoms_reproductive="Infected bunches shrivel, turn brown, and become hard mummies.",
        biological_controls=["Trichoderma harzianum sprays"],
        cultural_controls=["Canopy management and canopy leaf stripping to optimize aeration and sunlight penetration"],
        chemical_active_ingredients=["Bordeaux mixture (1%)", "Copper oxychloride 50% WP @ 2.5 g/L", "Mandipropamid 23.4% SC @ 0.8 ml/L"],
        economic_threshold_level="Rule of 'Three 10s': 10 cm shoot growth, 10 mm rainfall, 10°C minimum temperature.",
    ),

    # -------------------------------------------------------------
    # 2. BACTERIAL & VIRAL PATHOGENS
    # -------------------------------------------------------------
    "bacterial_leaf_blight": PestDiseaseProfile(
        id="bacterial_leaf_blight",
        name="Bacterial Leaf Blight (BLB) of Rice",
        scientific_name="Xanthomonas oryzae pv. oryzae",
        organism_type="Bacterium",
        target_crops=["rice"],
        temp_min_c=20.0,
        temp_opt_min_c=26.0,
        temp_opt_max_c=32.0,
        temp_max_c=38.0,
        humidity_min_pct=80.0,
        leaf_wetness_hours_threshold=6.0,
        rainfall_correlation="Positive",
        symptoms_vegetative="Water-soaked to yellowish-white wavy stripes extending from leaf tips along leaf margins. Bacterial oozing in morning drops.",
        symptoms_reproductive="Kresek (seedling wilting) in early stages; premature ripening with partially filled grains.",
        biological_controls=["Pseudomonas fluorescens root dip and foliar spray"],
        cultural_controls=["Avoid clipping seedling tips at transplanting", "Balanced fertilization with split potash application"],
        chemical_active_ingredients=["Streptocycline 90:10 (Streptomycin sulphate + Tetracycline hydrochloride) @ 0.1 g/L + Copper Oxychloride @ 1.5 g/L"],
        economic_threshold_level="First sign of translucent wavy lesions at maximum tillering stage.",
    ),

    "yellow_mosaic_virus": PestDiseaseProfile(
        id="yellow_mosaic_virus",
        name="Mungbean / Legume Yellow Mosaic Virus (MYMV)",
        scientific_name="Begomovirus (Whitefly-transmitted)",
        organism_type="Virus",
        target_crops=["blackgram", "greengram", "soybean", "pigeonpea"],
        temp_min_c=22.0,
        temp_opt_min_c=28.0,
        temp_opt_max_c=36.0,
        temp_max_c=42.0,
        humidity_min_pct=50.0,
        leaf_wetness_hours_threshold=0.0,
        rainfall_correlation="Negative",  # Vector whitefly thrives in warm, dry weather
        symptoms_vegetative="Small yellow specks along leaf veinlets expanding into confluent bright yellow and green mosaic patches.",
        symptoms_reproductive="Stunted plant growth; reduced flower and pod setting, pods are small, distorted with wrinkled seeds.",
        biological_controls=["Chrysoperla carnea (Green lacewing) predators", "Verticillium lecanii bio-insecticide"],
        cultural_controls=["Roughing out infected plants within first 30 DAS", "Yellow sticky traps (15-20 traps/ha)"],
        chemical_active_ingredients=["Thiamethoxam 25% WG @ 0.3 g/L (vector control)", "Spiromesifen 22.9% SC @ 1 ml/L", "Neem oil 10,000 ppm @ 2 ml/L"],
        economic_threshold_level="5-10 whiteflies per plant or initial mosaic spotting on 2% seedlings.",
    ),

    # -------------------------------------------------------------
    # 3. MAJOR INSECT PESTS
    # -------------------------------------------------------------
    "fall_armyworm": PestDiseaseProfile(
        id="fall_armyworm",
        name="Fall Armyworm (FAW)",
        scientific_name="Spodoptera frugiperda",
        organism_type="Insect Pest",
        target_crops=["maize", "sorghum", "sugarcane", "rice"],
        temp_min_c=12.0,
        temp_opt_min_c=24.0,
        temp_opt_max_c=32.0,
        temp_max_c=38.0,
        humidity_min_pct=40.0,
        leaf_wetness_hours_threshold=0.0,
        rainfall_correlation="Neutral",
        symptoms_vegetative="Extensive window-paning on leaf whorls with heavy presence of coarse yellowish-brown sawdust-like frass.",
        symptoms_reproductive="Boring through ear silks into developing kernels and cobs.",
        biological_controls=["Trichogramma pretiosum egg parasitoids", "Nomuraea rileyi / Metarhizium anisopliae entomopathogenic fungi"],
        cultural_controls=["Deep summer ploughing", "Intercropping with pulses / desmodium (push-pull strategy)", "Sand + ash whorl application"],
        chemical_active_ingredients=["Chlorantraniliprole 18.5% SC @ 0.4 ml/L", "Emamectin Benzoate 5% SG @ 0.4 g/L", "Spinetoram 11.7% SC @ 0.5 ml/L"],
        economic_threshold_level="5% damaged plants at seedling stage; 10-20% damaged whorls up to knee-high stage.",
    ),

    "pink_bollworm": PestDiseaseProfile(
        id="pink_bollworm",
        name="Pink Bollworm of Cotton",
        scientific_name="Pectinophora gossypiella",
        organism_type="Insect Pest",
        target_crops=["cotton"],
        temp_min_c=16.0,
        temp_opt_min_c=25.0,
        temp_opt_max_c=34.0,
        temp_max_c=40.0,
        humidity_min_pct=45.0,
        leaf_wetness_hours_threshold=0.0,
        rainfall_correlation="Neutral",
        symptoms_vegetative="Rosette flowers (intertwined petals that do not open fully due to larval webbing).",
        symptoms_reproductive="Bored entry holes sealed by larva inside developing bolls; feeding destroys internal locules, staining lint brownish-pink.",
        biological_controls=["Trichogramma bactrae egg parasitoid", "Pheromone mating disruption (Gossyplure dispensers)"],
        cultural_controls=["Terminating cotton crop by December/January to prevent diapause carryover", "Shredding and destroying cotton stalks"],
        chemical_active_ingredients=["Profenofos 50% EC @ 2 ml/L", "Indoxacarb 14.5% SC @ 1 ml/L", "Spinosad 45% SC @ 0.3 ml/L"],
        economic_threshold_level="8 moths/trap/night for 3 consecutive nights or 10% damaged green bolls with live larvae.",
    ),
}


def get_pest_disease_by_id(pid: str) -> Optional[PestDiseaseProfile]:
    """Retrieve pest or pathogen profile by identifier."""
    return PEST_DISEASE_DATABASE.get(pid.lower().strip())


def get_risks_for_crop(crop_id: str) -> List[PestDiseaseProfile]:
    """Return all known pest and disease threats for a designated crop."""
    target = crop_id.lower().strip()
    return [p for p in PEST_DISEASE_DATABASE.values() if target in p.target_crops]
