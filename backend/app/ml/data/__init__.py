"""
Agronomic datasets and static agricultural knowledge bases.
"""

from app.ml.data.crop_database import (
    CROP_DATABASE,
    CropAgronomicProfile,
    get_crop_by_id,
    list_all_crops,
    filter_crops_by_category,
    get_crop_names,
)
from app.ml.data.soil_profiles import (
    SOIL_HYDRAULIC_DATABASE,
    TAXONOMY_ORDERS,
    NutrientRatingInterpretation,
    determine_texture_from_fractions,
)
from app.ml.data.fertilizer_db import (
    FERTILIZER_DATABASE,
    FertilizerProduct,
    get_fertilizer_by_id,
    list_fertilizers_by_category,
)
from app.ml.data.pest_disease_db import (
    PEST_DISEASE_DATABASE,
    PestDiseaseProfile,
    get_pest_disease_by_id,
    get_risks_for_crop,
)

__all__ = [
    "CROP_DATABASE",
    "CropAgronomicProfile",
    "get_crop_by_id",
    "list_all_crops",
    "filter_crops_by_category",
    "get_crop_names",
    "SOIL_HYDRAULIC_DATABASE",
    "TAXONOMY_ORDERS",
    "NutrientRatingInterpretation",
    "determine_texture_from_fractions",
    "FERTILIZER_DATABASE",
    "FertilizerProduct",
    "get_fertilizer_by_id",
    "list_fertilizers_by_category",
    "PEST_DISEASE_DATABASE",
    "PestDiseaseProfile",
    "get_pest_disease_by_id",
    "get_risks_for_crop",
]
