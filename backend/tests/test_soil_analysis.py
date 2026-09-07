import pytest
from app.ml.data.soil_profiles import (
    NutrientRatingInterpretation,
    determine_texture_from_fractions,
    SOIL_HYDRAULIC_DATABASE,
)


def test_soil_texture_triangle_classification():
    """Verify USDA soil texture triangle algorithm correctly assigns texture classes."""
    # Sand test: 90% sand, 5% silt, 5% clay -> Sand
    assert determine_texture_from_fractions(90, 5, 5) == "sand"

    # Clay test: 20% sand, 20% silt, 60% clay -> Clay
    assert determine_texture_from_fractions(20, 20, 60) == "clay"

    # Silt loam test: 15% sand, 70% silt, 15% clay -> Silt loam
    assert determine_texture_from_fractions(15, 70, 15) == "silt_loam"

    # Loam test: 40% sand, 40% silt, 20% clay -> Loam
    assert determine_texture_from_fractions(40, 40, 20) == "loam"


def test_soil_chemical_ratings_and_diagnostics():
    """Verify chemical rating thresholds for Nitrogen, Phosphorus, Potassium, and pH."""
    # Nitrogen ratings
    assert "Low" in NutrientRatingInterpretation.classify_nitrogen_kg_ha(210.0)
    assert "Medium" in NutrientRatingInterpretation.classify_nitrogen_kg_ha(350.0)
    assert "High" in NutrientRatingInterpretation.classify_nitrogen_kg_ha(600.0)

    # pH ratings & amendment recommendations
    acidic_cat, acidic_diag = NutrientRatingInterpretation.classify_ph(4.2)
    assert acidic_cat == "Extremely Acidic"
    assert "liming" in acidic_diag.lower()

    alkaline_cat, alkaline_diag = NutrientRatingInterpretation.classify_ph(8.8)
    assert alkaline_cat == "Strongly Alkaline"
    assert "gypsum" in alkaline_diag.lower()

    optimal_cat, _ = NutrientRatingInterpretation.classify_ph(6.8)
    assert optimal_cat == "Neutral / Optimal"


def test_soil_hydraulic_database_integrity():
    """Ensure all USDA textures have valid physical and hydraulic parameters."""
    assert len(SOIL_HYDRAULIC_DATABASE) >= 12

    for key, props in SOIL_HYDRAULIC_DATABASE.items():
        assert props.field_capacity_vol_pct > props.wilting_point_vol_pct
        assert props.available_water_capacity_mm_per_m > 0
        assert 1.0 <= props.bulk_density_g_cm3 <= 1.8
