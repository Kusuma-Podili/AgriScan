from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.models.farm import Farm, FieldParcel
from app.schemas.farm import FarmCreate, FarmUpdate, FarmResponse, FieldParcelCreate, FieldParcelResponse
from app.api.deps import get_current_user

router = APIRouter()


@router.post("/", response_model=FarmResponse, status_code=status.HTTP_201_CREATED)
def create_farm(
    farm_in: FarmCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a new farm holding with boundary coordinates and GIS polygon."""
    farm = Farm(
        owner_id=current_user.id,
        name=farm_in.name,
        state=farm_in.state,
        district=farm_in.district,
        latitude=farm_in.latitude,
        longitude=farm_in.longitude,
        elevation_m=farm_in.elevation_m,
        total_area_hectares=farm_in.total_area_hectares,
        irrigation_source=farm_in.irrigation_source,
        soil_type_primary=farm_in.soil_type_primary,
        polygon_geojson=farm_in.polygon_geojson,
    )
    db.add(farm)
    db.commit()
    db.refresh(farm)
    return farm


@router.get("/", response_model=List[FarmResponse])
def list_farms(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Retrieve all farms belonging to the authenticated user."""
    return db.query(Farm).filter(Farm.owner_id == current_user.id).all()


@router.get("/{farm_id}", response_model=FarmResponse)
def get_farm_detail(
    farm_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get single farm details including sub-parcels."""
    farm = db.query(Farm).filter(Farm.id == farm_id, Farm.owner_id == current_user.id).first()
    if not farm:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Farm holding not found")
    return farm


@router.post("/{farm_id}/parcels", response_model=FieldParcelResponse, status_code=status.HTTP_201_CREATED)
def add_field_parcel(
    farm_id: str,
    parcel_in: FieldParcelCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Add a subdivided field parcel to an existing farm."""
    farm = db.query(Farm).filter(Farm.id == farm_id, Farm.owner_id == current_user.id).first()
    if not farm:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Farm holding not found")

    parcel = FieldParcel(
        farm_id=farm.id,
        name=parcel_in.name,
        area_hectares=parcel_in.area_hectares,
        current_crop=parcel_in.current_crop,
        sowing_date=parcel_in.sowing_date,
        irrigation_system=parcel_in.irrigation_system,
        polygon_geojson=parcel_in.polygon_geojson,
    )
    db.add(parcel)
    db.commit()
    db.refresh(parcel)
    return parcel
