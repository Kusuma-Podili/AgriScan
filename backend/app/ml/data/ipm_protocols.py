"""
AgroPulse Integrated Pest Management (IPM) Protocols & Chemical Phyto-Sanitary Monographs.
Detailed economic threshold levels (ETL), bio-pesticide application protocols,
spray schedules, waiting periods / Pre-Harvest Intervals (PHI), and resistance management.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class ChemicalTreatment(BaseModel):
    trade_name_common: str
    active_ingredient: str
    formulation: str
    dosage_per_hectare: str
    dosage_per_liter_water: str
    target_stage: str
    pre_harvest_interval_days: int  # PHI waiting period between last spray and harvest
    irac_mode_of_action: str
    safety_precaution: str


class BioControlMethod(BaseModel):
    agent_name: str
    agent_type: str  # Parasitoid, Predator, Entomopathogenic Fungus, Bio-bacterium, Botanical
    release_rate_per_ha: str
    application_timing: str
    target_pests: List[str]


class CropIPMProtocol(BaseModel):
    crop_id: str
    crop_name: str
    economic_thresholds: Dict[str, str]
    cultural_sanitation_practices: List[str]
    biological_schedule: List[BioControlMethod]
    chemical_spray_roster: List[ChemicalTreatment]
    resistance_management_guidance: str


IPM_PROTOCOLS_DATABASE: Dict[str, CropIPMProtocol] = {
    "rice": CropIPMProtocol(
        crop_id="rice",
        crop_name="Rice (Paddy)",
        economic_thresholds={
            "Yellow Stem Borer": "1 egg mass/m² or 5% dead hearts at vegetative stage; 2% white ears at flowering",
            "Brown Planthopper (BPH)": "5-10 insects/hill at tillering; 15-20 insects/hill after panicle emergence",
            "Leaf Folder": "1-2 damaged leaves/hill with active larvae",
            "Rice Blast": "1-2% leaf area covered at tillering or 1% neck blast incidence at heading",
            "Bacterial Leaf Blight (BLB)": "First appearance of wavy margins at maximum tillering",
        },
        cultural_sanitation_practices=[
            "Deep summer ploughing to expose hibernating larvae and pupae to predators and sun desiccation",
            "Clip seedling tips before transplanting to destroy stem borer egg masses",
            "Formation of 'alley ways' (leaving 30 cm alleys every 2.5-3.0 m) for sunlight and aeration to deter BPH",
            "Alternate wetting and drying (AWD) irrigation regime to disrupt BPH multiplication and stem rot fungi",
            "Balanced fertilizer application: strictly split Nitrogen in 3 doses; avoid excess urea in humid spells",
        ],
        biological_schedule=[
            BioControlMethod(
                agent_name="Trichogramma japonicum",
                agent_type="Parasitoid",
                release_rate_per_ha="100,000 parasitized eggs/ha (5 Tricho-cards/ha)",
                application_timing="Release at 30, 37, and 44 days after transplanting (weekly intervals)",
                target_pests=["Yellow Stem Borer", "Leaf Folder"],
            ),
            BioControlMethod(
                agent_name="Pseudomonas fluorescens (Pfl)",
                agent_type="Bio-bacterium",
                release_rate_per_ha="Seed treatment @ 10 g/kg; root dip @ 2.5 kg/ha; foliar @ 2.5 kg/ha",
                application_timing="Nursery sowing, transplanting, and 45 DAS",
                target_pests=["Rice Blast", "Sheath Blight", "Bacterial Leaf Blight"],
            ),
            BioControlMethod(
                agent_name="Beauveria bassiana",
                agent_type="Entomopathogenic Fungus",
                release_rate_per_ha="1.5 kg/ha or 2.5 L/ha liquid formulation",
                application_timing="At first appearance of nymphal colonies at base of hills",
                target_pests=["Brown Planthopper", "Green Leafhopper"],
            ),
        ],
        chemical_spray_roster=[
            ChemicalTreatment(
                trade_name_common="Chlorantraniliprole 0.4% GR (Ferterra)",
                active_ingredient="Chlorantraniliprole",
                formulation="Granule (GR)",
                dosage_per_hectare="10.0 kg/ha",
                dosage_per_liter_water="Direct soil application with sand/fertilizer",
                target_stage="Vegetative (20-25 DAT) for stem borer and whorl maggot",
                pre_harvest_interval_days=53,
                irac_mode_of_action="Group 28: Ryanodine receptor modulators",
                safety_precaution="Ensure standing water of 2-3 cm for 24-48 hours after application",
            ),
            ChemicalTreatment(
                trade_name_common="Trifloxystrobin 25% + Tebuconazole 50% WG (Nativo)",
                active_ingredient="Trifloxystrobin + Tebuconazole",
                formulation="Water Dispersible Granule (WG)",
                dosage_per_hectare="400 g/ha",
                dosage_per_liter_water="0.8 g/L",
                target_stage="Booting and 50% panicle emergence for neck blast and sheath blight",
                pre_harvest_interval_days=21,
                irac_mode_of_action="Group 11 (QoI) + Group 3 (DMI Sterol biosynthesis)",
                safety_precaution="Wear personal protective gear; avoid spraying in rain or heavy wind",
            ),
            ChemicalTreatment(
                trade_name_common="Pymetrozine 50% WDG (Chess)",
                active_ingredient="Pymetrozine",
                formulation="Water Dispersible Granule (WDG)",
                dosage_per_hectare="300 g/ha",
                dosage_per_liter_water="0.6 g/L",
                target_stage="Aim nozzle directly at base of plant for Brown Planthopper suppression",
                pre_harvest_interval_days=19,
                irac_mode_of_action="Group 9B: Chordotonal organ TRPV channel modulators",
                safety_precaution="Safe to beneficial spiders and mirid bugs (Cyrtorhinus lividipennis)",
            ),
        ],
        resistance_management_guidance="Rotate chemical classes between IRAC Group 28 (diamides), Group 4A (neonicotinoids), and Group 9B. Never apply sub-lethal under-doses.",
    ),

    "cotton": CropIPMProtocol(
        crop_id="cotton",
        crop_name="Cotton",
        economic_thresholds={
            "Pink Bollworm": "8 moths/trap/night for 3 consecutive nights or 10% damaged green bolls with live larvae",
            "American Bollworm (Helicoverpa)": "1 larva/plant or 1 egg/plant or 5% damaged square fruiting forms",
            "Whitefly (Bemisia tabaci)": "6-8 adults/leaf or nymphs covering 10% lower leaf surface",
            "Jassids (Amrasca biguttula)": "1-2 nymphs/leaf displaying grade II leaf injury (marginal yellowing/cupping)",
            "Bacterial Blight / Black Arm": "5% angular water-soaked leaf spots",
        },
        cultural_sanitation_practices=[
            "Install pheromone traps @ 5 traps/ha for monitoring and 25 traps/ha for mass trapping of pink bollworm",
            "Plant 20% non-Bt cotton refuge seeds (refugia in bag) to preserve insect susceptibility to Cry proteins",
            "Synchronized sowing within a 15-day community window to prevent staggered pest cycles",
            "Detopping / terminal shoot nipping at 80-90 DAS to arrest vegetative growth and remove Helicoverpa egg sites",
            "Collect and destroy fallen squares, flowers, and shed green bolls daily",
        ],
        biological_schedule=[
            BioControlMethod(
                agent_name="Trichogramma bactrae",
                agent_type="Parasitoid",
                release_rate_per_ha="150,000 parasitized eggs/ha",
                application_timing="Commencing at 45 DAS at weekly intervals (5-6 releases)",
                target_pests=["Pink Bollworm", "Spotted Bollworm"],
            ),
            BioControlMethod(
                agent_name="Chrysoperla carnea (Green Lacewing)",
                agent_type="Predator",
                release_rate_per_ha="10,000 second-instar grubs/ha",
                application_timing="At 30 and 50 DAS during peak sucking pest flare-up",
                target_pests=["Whitefly", "Aphids", "Jassids", "Thrips"],
            ),
            BioControlMethod(
                agent_name="Verticillium lecanii (Lecanicillium lecanii)",
                agent_type="Entomopathogenic Fungus",
                release_rate_per_ha="2.0 kg/ha in 500 L water with 0.1% wetting agent",
                application_timing="During high relative humidity (>75%) in evening hours",
                target_pests=["Whitefly nymphs", "Mealybug colonies"],
            ),
        ],
        chemical_spray_roster=[
            ChemicalTreatment(
                trade_name_common="Spiromesifen 22.9% SC (Oberon)",
                active_ingredient="Spiromesifen",
                formulation="Suspension Concentrate (SC)",
                dosage_per_hectare="500 ml/ha",
                dosage_per_liter_water="1.0 ml/L",
                target_stage="Active vegetative through flowering against whitefly eggs and nymphs",
                pre_harvest_interval_days=25,
                irac_mode_of_action="Group 23: Inhibitors of lipid synthesis (acetyl-CoA carboxylase)",
                safety_precaution="Provides excellent ovicidal activity; spray undersides of leaves thoroughly",
            ),
            ChemicalTreatment(
                trade_name_common="Emamectin Benzoate 5% SG (Proclaim)",
                active_ingredient="Emamectin Benzoate",
                formulation="Soluble Granule (SG)",
                dosage_per_hectare="220 g/ha",
                dosage_per_liter_water="0.45 g/L",
                target_stage="Peak boll development against internal bollworm complex",
                pre_harvest_interval_days=14,
                irac_mode_of_action="Group 6: Glutamate-gated chloride channel (GluCl) allosteric modulators",
                safety_precaution="Rapid translaminar penetration; highly potent at minimal active dose",
            ),
            ChemicalTreatment(
                trade_name_common="Spinosad 45% SC (Tracer)",
                active_ingredient="Spinosad",
                formulation="Suspension Concentrate (SC)",
                dosage_per_hectare="180 ml/ha",
                dosage_per_liter_water="0.35 ml/L",
                target_stage="Flowering and boll opening against thrips and pink bollworm larvae",
                pre_harvest_interval_days=14,
                irac_mode_of_action="Group 5: Nicotinic acetylcholine receptor (nAChR) allosteric modulators",
                safety_precaution="Fermentation derived spinosyn bio-rational insecticide",
            ),
        ],
        resistance_management_guidance="Window-based chemical rotation: Early season (0-60 DAS) sucking pest bio-rationals -> Mid season (60-100 DAS) diamides/avermectins -> Late season (100+ DAS) spinosad/indoxacarb.",
    ),

    "wheat": CropIPMProtocol(
        crop_id="wheat",
        crop_name="Wheat",
        economic_thresholds={
            "Yellow / Stripe Rust": "5% flag leaf area covered with bright yellow pustule stripes",
            "Brown / Leaf Rust": "10% leaf area with scattered orange-brown pustules",
            "Loose Smut": "Any visible black smutted powdery earhead at heading",
            "Wheat Aphid": "5-10 aphids per earhead during milk/dough stage",
            "Termites": "Appearance of dry wilted seedlings easily pulled from soil",
        },
        cultural_sanitation_practices=[
            "Strict seed treatment with vitavax/tebuconazole to eliminate seed-borne loose smut",
            "Timely sowing in November (1st fortnight) to avoid terminal heat and rust epidemics",
            "Eradicate self-sown volunteer wheat plants in adjoining fields and irrigation bunds",
            "Balanced nutrition: ensure potash application to strengthen culm wall resistance",
        ],
        biological_schedule=[
            BioControlMethod(
                agent_name="Trichoderma viride",
                agent_type="Bio-fungicide",
                release_rate_per_ha="Seed treatment @ 4 g/kg seed",
                application_timing="At sowing time",
                target_pests=["Foot Rot", "Root Rot", "Seedling Blight"],
            ),
            BioControlMethod(
                agent_name="Coccinella septempunctata (Seven-spot Ladybird Beetle)",
                agent_type="Predator",
                release_rate_per_ha="Natural conservation; avoid broad-spectrum pyrethroid sprays",
                application_timing="Earhead emergence through dough stage",
                target_pests=["Wheat Aphid", "Bird Cherry-Oat Aphid"],
            ),
        ],
        chemical_spray_roster=[
            ChemicalTreatment(
                trade_name_common="Propiconazole 25% EC (Tilt)",
                active_ingredient="Propiconazole",
                formulation="Emulsifiable Concentrate (EC)",
                dosage_per_hectare="500 ml/ha",
                dosage_per_liter_water="1.0 ml/L",
                target_stage="Immediate spray upon first noticing stripe rust foci; repeat after 15 days if needed",
                pre_harvest_interval_days=30,
                irac_mode_of_action="FRAC 3: Demethylation inhibitors (DMI)",
                safety_precaution="Ensure uniform coverage of canopy flag leaves",
            ),
            ChemicalTreatment(
                trade_name_common="Tebuconazole 25.9% EC (Folicur)",
                active_ingredient="Tebuconazole",
                formulation="Emulsifiable Concentrate (EC)",
                dosage_per_hectare="500 ml/ha",
                dosage_per_liter_water="1.0 ml/L",
                target_stage="Karnal bunt and stripe rust prevention at heading",
                pre_harvest_interval_days=30,
                irac_mode_of_action="FRAC 3: Demethylation inhibitors",
                safety_precaution="Do not apply during high temperature noon hours",
            ),
        ],
        resistance_management_guidance="Plant multi-line resistant wheat cultivars containing stacked Yr and Lr genes. Rotate triazoles with strobilurins if secondary sprays are warranted.",
    ),
}


def get_ipm_protocol(crop_id: str) -> Optional[CropIPMProtocol]:
    """Retrieve complete IPM protocol and spray roster by crop identifier."""
    return IPM_PROTOCOLS_DATABASE.get(crop_id.lower().strip())
