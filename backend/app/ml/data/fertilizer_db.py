"""
AgroPulse Commercial Fertilizer Specifications, Nutrient Densities, and Formulations Database.
Provides stoichiometric elemental compositions, solubility, salt index, and application split recommendations.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class FertilizerProduct(BaseModel):
    id: str
    name: str
    chemical_formula: str
    category: str  # Straight-N, Straight-P, Straight-K, Complex-NPK, Micronutrient, Organic
    n_pct: float = Field(0.0, description="Available Nitrogen content %")
    p2o5_pct: float = Field(0.0, description="Available P2O5 (Phosphate) content %")
    k2o_pct: float = Field(0.0, description="Available K2O (Potash) content %")
    s_pct: float = Field(0.0, description="Available Sulphur content %")
    ca_pct: float = Field(0.0, description="Available Calcium content %")
    mg_pct: float = Field(0.0, description="Available Magnesium content %")
    zn_pct: float = Field(0.0, description="Zinc content %")
    fe_pct: float = Field(0.0, description="Iron content %")
    b_pct: float = Field(0.0, description="Boron content %")

    physical_state: str  # Granular, Prilled, Crystalline, Liquid, Powder
    solubility_g_per_l_20c: float  # Solubility in water at 20°C
    salt_index: float  # Relative salt index (Sodium nitrate = 100)
    acid_base_equivalent_kg_caco3: float  # Negative denotes acidifying, positive denotes basic/alkalizing
    recommended_methods: List[str]  # Basal Broadcast, Band Placement, Fertigation, Foliar Spray
    timing_rules: str
    handling_notes: str


FERTILIZER_DATABASE: Dict[str, FertilizerProduct] = {
    # -------------------------------------------------------------
    # 1. STRAIGHT NITROGENOUS FERTILIZERS
    # -------------------------------------------------------------
    "urea": FertilizerProduct(
        id="urea",
        name="Urea (Prilled / Granular)",
        chemical_formula="CO(NH2)2",
        category="Straight-N",
        n_pct=46.0,
        physical_state="Prilled",
        solubility_g_per_l_20c=1080.0,
        salt_index=75.4,
        acid_base_equivalent_kg_caco3=-80.0,  # Acid-forming (requires 80 kg CaCO3 per 100 kg Urea)
        recommended_methods=["Basal Soil Incorporation", "Top Dressing", "Fertigation", "Foliar Spray (1-2% max)"],
        timing_rules="Always split into 2-3 split doses coinciding with rapid vegetative flushes and panicle initiation. Never broadcast on dry or water-saturated bare surface to minimize volatilization losses.",
        handling_notes="Hygroscopic; store in moisture-proof HDPE bags. Biuret content must be below 1.5% (below 0.5% for foliar use).",
    ),

    "ammonium_sulphate": FertilizerProduct(
        id="ammonium_sulphate",
        name="Ammonium Sulphate",
        chemical_formula="(NH4)2SO4",
        category="Straight-N",
        n_pct=20.5,
        s_pct=24.0,
        physical_state="Crystalline",
        solubility_g_per_l_20c=750.0,
        salt_index=69.0,
        acid_base_equivalent_kg_caco3=-110.0,  # Strongly acid-forming
        recommended_methods=["Basal Placement", "Top Dressing", "Fertigation"],
        timing_rules="Outstanding for sulfur-responsive crops (oilseeds, pulses, brassicas) and alkaline/calcareous soils needing local acidification.",
        handling_notes="Resistant to moisture uptake compared to urea. Excellent shelf-life.",
    ),

    "calcium_ammonium_nitrate": FertilizerProduct(
        id="calcium_ammonium_nitrate",
        name="Calcium Ammonium Nitrate (CAN / Nitro-Limestone)",
        chemical_formula="5Ca(NO3)2·NH4NO3·10H2O",
        category="Straight-N",
        n_pct=25.0,
        ca_pct=8.0,
        physical_state="Granular",
        solubility_g_per_l_20c=600.0,
        salt_index=61.0,
        acid_base_equivalent_kg_caco3=0.0,  # Neutral physiological reaction
        recommended_methods=["Top Dressing", "Side Dressing"],
        timing_rules="Contains 50% ammoniacal and 50% immediate nitrate nitrogen. Ideal for neutral/acidic soils where urea acidification is detrimental.",
        handling_notes="Prilled granules; absorbs moisture if exposed to high relative humidity.",
    ),

    # -------------------------------------------------------------
    # 2. STRAIGHT PHOSPHATIC FERTILIZERS
    # -------------------------------------------------------------
    "single_super_phosphate": FertilizerProduct(
        id="single_super_phosphate",
        name="Single Super Phosphate (SSP)",
        chemical_formula="Ca(H2PO4)2·H2O + 2CaSO4·2H2O",
        category="Straight-P",
        p2o5_pct=16.0,
        s_pct=12.0,
        ca_pct=19.5,
        physical_state="Granular",
        solubility_g_per_l_20c=20.0,
        salt_index=7.8,
        acid_base_equivalent_kg_caco3=0.0,  # Neutral
        recommended_methods=["Basal Band Placement"],
        timing_rules="Apply 100% as basal dose placed 3-5 cm below and to the side of seed to maximize early root interception.",
        handling_notes="Contains gypsum byproduct providing valuable Calcium and Sulphur at no extra cost.",
    ),

    "triple_super_phosphate": FertilizerProduct(
        id="triple_super_phosphate",
        name="Triple Super Phosphate (TSP)",
        chemical_formula="Ca(H2PO4)2·H2O",
        category="Straight-P",
        p2o5_pct=46.0,
        ca_pct=14.0,
        physical_state="Granular",
        solubility_g_per_l_20c=40.0,
        salt_index=10.1,
        acid_base_equivalent_kg_caco3=0.0,
        recommended_methods=["Basal Placement"],
        timing_rules="Full dose at planting time. Highly concentrated source of water-soluble phosphate.",
        handling_notes="Non-hygroscopic, excellent physical storage qualities.",
    ),

    # -------------------------------------------------------------
    # 3. STRAIGHT POTASSIC FERTILIZERS
    # -------------------------------------------------------------
    "muriate_of_potash": FertilizerProduct(
        id="muriate_of_potash",
        name="Muriate of Potash (MOP / Potassium Chloride)",
        chemical_formula="KCl",
        category="Straight-K",
        k2o_pct=60.0,
        physical_state="Granular (Pink/White)",
        solubility_g_per_l_20c=340.0,
        salt_index=116.3,
        acid_base_equivalent_kg_caco3=0.0,
        recommended_methods=["Basal Incorporation", "Split Dressing in light sandy soils", "Fertigation"],
        timing_rules="Apply full dose basal in heavy textured soils. Split into 2 applications in light sands to prevent leaching.",
        handling_notes="Avoid application to chloride-sensitive crops (tobacco, grapes, potato, strawberry).",
    ),

    "potassium_sulphate": FertilizerProduct(
        id="potassium_sulphate",
        name="Sulphate of Potash (SOP)",
        chemical_formula="K2SO4",
        category="Straight-K",
        k2o_pct=50.0,
        s_pct=17.5,
        physical_state="Crystalline Powder",
        solubility_g_per_l_20c=110.0,
        salt_index=46.1,
        acid_base_equivalent_kg_caco3=0.0,
        recommended_methods=["Basal Placement", "Fertigation", "Foliar Spray"],
        timing_rules="Preferred potassic source for chloride-sensitive crops and soils with salinity concerns.",
        handling_notes="Low salt index makes it the safest fertilizer for drip fertigation and seedling beds.",
    ),

    # -------------------------------------------------------------
    # 4. COMPLEX & MULTI-NUTRIENT FERTILIZERS
    # -------------------------------------------------------------
    "di_ammonium_phosphate": FertilizerProduct(
        id="di_ammonium_phosphate",
        name="Di-Ammonium Phosphate (DAP)",
        chemical_formula="(NH4)2HPO4",
        category="Complex-NPK",
        n_pct=18.0,
        p2o5_pct=46.0,
        physical_state="Granular",
        solubility_g_per_l_20c=580.0,
        salt_index=34.2,
        acid_base_equivalent_kg_caco3=-74.0,
        recommended_methods=["Basal Placement"],
        timing_rules="Apply 100% at sowing time. High water-soluble P2O5 (over 85%) promotes rapid root vigor.",
        handling_notes="Temporary alkaline micro-zone around granule can volatilize ammonia if placed immediately next to seeds in high pH soils.",
    ),

    "npk_10_26_26": FertilizerProduct(
        id="npk_10_26_26",
        name="Complex NPK 10:26:26",
        chemical_formula="Granular Composite",
        category="Complex-NPK",
        n_pct=10.0,
        p2o5_pct=26.0,
        k2o_pct=26.0,
        physical_state="Granular",
        solubility_g_per_l_20c=320.0,
        salt_index=55.0,
        acid_base_equivalent_kg_caco3=-20.0,
        recommended_methods=["Basal Placement", "Band Placement"],
        timing_rules="Balanced PK ratio ideal for legumes, oilseeds, sugarcane, and root crops needing low initial N and high PK.",
        handling_notes="Homogeneous uniform granules prevent nutrient segregation.",
    ),

    "npk_12_32_16": FertilizerProduct(
        id="npk_12_32_16",
        name="Complex NPK 12:32:16",
        chemical_formula="Granular Composite",
        category="Complex-NPK",
        n_pct=12.0,
        p2o5_pct=32.0,
        k2o_pct=16.0,
        physical_state="Granular",
        solubility_g_per_l_20c=340.0,
        salt_index=48.0,
        acid_base_equivalent_kg_caco3=-30.0,
        recommended_methods=["Basal Soil Placement"],
        timing_rules="Standard basal grade for wheat, maize, and paddy in medium-K soils.",
        handling_notes="Excellent physical hardness and flowability in mechanical seed drills.",
    ),

    "npk_19_19_19": FertilizerProduct(
        id="npk_19_19_19",
        name="Water Soluble NPK 19:19:19",
        chemical_formula="100% Water Soluble Salt Blend",
        category="Complex-NPK",
        n_pct=19.0,
        p2o5_pct=19.0,
        k2o_pct=19.0,
        physical_state="Crystalline Powder",
        solubility_g_per_l_20c=990.0,
        salt_index=65.0,
        acid_base_equivalent_kg_caco3=-15.0,
        recommended_methods=["Drip Fertigation", "Foliar Spray (0.5% - 1.0%)"],
        timing_rules="Applied in weekly/biweekly fertigation schedules during vegetative through fruit development stages.",
        handling_notes="100% soluble with zero residue; will not clog drip emitters.",
    ),

    # -------------------------------------------------------------
    # 5. MICRONUTRIENTS & AMENDMENTS
    # -------------------------------------------------------------
    "zinc_sulphate_hepta": FertilizerProduct(
        id="zinc_sulphate_hepta",
        name="Zinc Sulphate Heptahydrate (21% Zn)",
        chemical_formula="ZnSO4·7H2O",
        category="Micronutrient",
        s_pct=10.0,
        zn_pct=21.0,
        physical_state="Crystalline",
        solubility_g_per_l_20c=960.0,
        salt_index=30.0,
        acid_base_equivalent_kg_caco3=-10.0,
        recommended_methods=["Basal Soil Broadcast (25 kg/ha)", "Foliar Spray (0.5% with 0.25% lime)"],
        timing_rules="Apply once every 2-3 crop seasons for soils showing DTPA-Zn < 0.6 ppm. Never mix directly with phosphatic fertilizers in spray tank to prevent zinc phosphate precipitation.",
        handling_notes="Keep dry; readily soluble.",
    ),

    "borax": FertilizerProduct(
        id="borax",
        name="Borax (Sodium Tetraborate Decahydrate - 10.5% B)",
        chemical_formula="Na2B4O7·10H2O",
        category="Micronutrient",
        b_pct=10.5,
        physical_state="Granular / Powder",
        solubility_g_per_l_20c=50.0,
        salt_index=20.0,
        acid_base_equivalent_kg_caco3=0.0,
        recommended_methods=["Basal Soil Application (10 kg/ha)", "Foliar Spray (0.2% Borax / Solubor)"],
        timing_rules="Critical for sunflower, mustard, cauliflower, and fruit crops to prevent hollow stem and flower drop. Narrow safety margin between deficiency and toxicity.",
        handling_notes="Ensure uniform distribution across field.",
    ),

    # -------------------------------------------------------------
    # 6. ORGANIC AMENDMENTS & BIOFERTILIZERS
    # -------------------------------------------------------------
    "farmyard_manure": FertilizerProduct(
        id="farmyard_manure",
        name="Well-Decomposed Farmyard Manure (FYM)",
        chemical_formula="Decomposed Bovine Residue",
        category="Organic",
        n_pct=0.5,
        p2o5_pct=0.25,
        k2o_pct=0.5,
        ca_pct=0.3,
        physical_state="Organic Compost",
        solubility_g_per_l_20c=0.0,
        salt_index=2.0,
        acid_base_equivalent_kg_caco3=10.0,  # Buffer effect
        recommended_methods=["Pre-sowing Soil Broadcast & Incorporation (10-15 t/ha)"],
        timing_rules="Incorporate 3-4 weeks prior to sowing to permit full microbial mineralization.",
        handling_notes="Improves soil organic carbon, CEC, moisture retention, and microbial biodiversity.",
    ),

    "vermicompost": FertilizerProduct(
        id="vermicompost",
        name="Earthworm Castings / Vermicompost",
        chemical_formula="Eisenia fetida Bio-humus",
        category="Organic",
        n_pct=1.8,
        p2o5_pct=1.2,
        k2o_pct=1.5,
        physical_state="Fine Granular Humus",
        solubility_g_per_l_20c=0.0,
        salt_index=3.0,
        acid_base_equivalent_kg_caco3=15.0,
        recommended_methods=["Basal Band Application (2-5 t/ha)", "Potting Substrate"],
        timing_rules="Direct application around root zone at transplanting.",
        handling_notes="Rich in humic acid, fulvic acid, growth hormones, and beneficial mycorrhizae.",
    ),
}


def get_fertilizer_by_id(product_id: str) -> Optional[FertilizerProduct]:
    """Lookup commercial fertilizer by ID slug."""
    return FERTILIZER_DATABASE.get(product_id.lower().strip())


def list_fertilizers_by_category(category: str) -> List[FertilizerProduct]:
    """Filter fertilizers by product classification category."""
    return [f for f in FERTILIZER_DATABASE.values() if f.category.lower() == category.lower().strip()]
