from typing import List, Optional
from fastapi import APIRouter, HTTPException, status, Query
from app.ml.data.crop_database import (
    CROP_DATABASE,
    CropAgronomicProfile,
    get_crop_by_id,
    list_all_crops,
    filter_crops_by_category,
)

router = APIRouter()


@router.get("/", response_model=List[CropAgronomicProfile])
def list_crops(
    category: Optional[str] = Query(None, description="Filter by crop category"),
    search: Optional[str] = Query(None, description="Search by common or scientific name"),
):
    """Retrieve full catalog of 120+ crops with climatic, soil, and nutrient parameters."""
    crops = list_all_crops()
    if category:
        crops = [c for c in crops if c.category.lower() == category.lower().strip()]
    if search:
        q = search.lower().strip()
        crops = [c for c in crops if q in c.name.lower() or q in c.scientific_name.lower() or q in c.id.lower()]
    return crops


@router.get("/categories/all", response_model=List[str])
def get_all_categories():
    """List all available agricultural crop categories."""
    categories = sorted(list(set(c.category for c in CROP_DATABASE.values())))
    return categories


@router.get("/{crop_id}", response_model=CropAgronomicProfile)
def get_crop_profile(crop_id: str):
    """Get complete agronomic profile for a specific crop."""
    crop = get_crop_by_id(crop_id)
    if not crop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Crop '{crop_id}' not found in the agronomic database.",
        )
    return crop
