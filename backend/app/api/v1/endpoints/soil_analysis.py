from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.models.farm import Farm
from app.models.soil_sample import SoilSample
from app.schemas.soil import SoilSampleCreate, SoilSampleResponse, SoilHealthCardSummary
from app.ml.data.soil_profiles import NutrientRatingInterpretation, determine_texture_from_fractions
from app.api.deps import get_current_user

router = APIRouter()


@router.post("/samples", response_model=SoilSampleResponse, status_code=status.HTTP_201_CREATED)
def record_soil_sample(
    sample_in: SoilSampleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Record laboratory chemical soil test results."""
    farm = db.query(Farm).filter(Farm.id == sample_in.farm_id, Farm.owner_id == current_user.id).first()
    if not farm:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Associated farm not found")

    # Automatically derive USDA texture class if fractions are provided
    texture = sample_in.texture_class
    if sample_in.sand_pct > 0 and sample_in.clay_pct > 0:
        texture = determine_texture_from_fractions(
            sample_in.sand_pct, sample_in.silt_pct, sample_in.clay_pct
        ).replace("_", " ").title()

    sample = SoilSample(
        farm_id=sample_in.farm_id,
        field_parcel_id=sample_in.field_parcel_id,
        sample_code=sample_in.sample_code,
        depth_cm=sample_in.depth_cm,
        nitrogen_kg_ha=sample_in.nitrogen_kg_ha,
        phosphorus_kg_ha=sample_in.phosphorus_kg_ha,
        potassium_kg_ha=sample_in.potassium_kg_ha,
        ph=sample_in.ph,
        electrical_conductivity_ds_m=sample_in.electrical_conductivity_ds_m,
        organic_carbon_pct=sample_in.organic_carbon_pct,
        texture_class=texture,
        sand_pct=sample_in.sand_pct,
        silt_pct=sample_in.silt_pct,
        clay_pct=sample_in.clay_pct,
        sulphur_ppm=sample_in.sulphur_ppm,
        zinc_ppm=sample_in.zinc_ppm,
        boron_ppm=sample_in.boron_ppm,
        iron_ppm=sample_in.iron_ppm,
        laboratory_name=sample_in.laboratory_name,
        notes=sample_in.notes,
    )
    db.add(sample)
    db.commit()
    db.refresh(sample)
    return sample


@router.get("/samples/farm/{farm_id}", response_model=List[SoilSampleResponse])
def list_farm_soil_samples(
    farm_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Retrieve all recorded soil sample tests for a farm."""
    farm = db.query(Farm).filter(Farm.id == farm_id, Farm.owner_id == current_user.id).first()
    if not farm:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Farm not found")
    return db.query(SoilSample).filter(SoilSample.farm_id == farm_id).order_by(SoilSample.sampling_date.desc()).all()


@router.get("/samples/{sample_id}/health-card", response_model=SoilHealthCardSummary)
def generate_soil_health_card(
    sample_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Generate official Soil Health Card diagnostic ratings and corrective prescriptions."""
    sample = db.query(SoilSample).filter(SoilSample.id == sample_id).first()
    if not sample:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Soil sample not found")

    ph_cat, ph_diag = NutrientRatingInterpretation.classify_ph(sample.ph)
    ec_cat, ec_diag = NutrientRatingInterpretation.classify_electrical_conductivity_ds_m(sample.electrical_conductivity_ds_m)
    n_cat = NutrientRatingInterpretation.classify_nitrogen_kg_ha(sample.nitrogen_kg_ha)
    p_cat = NutrientRatingInterpretation.classify_phosphorus_kg_ha(sample.phosphorus_kg_ha, is_alkaline_soil=(sample.ph > 7.5))
    k_cat = NutrientRatingInterpretation.classify_potassium_kg_ha(sample.potassium_kg_ha)
    oc_cat = NutrientRatingInterpretation.classify_organic_carbon_pct(sample.organic_carbon_pct)

    # Compute overall composite health score (0 to 100)
    score = 100.0
    if "Acidic" in ph_cat or "Alkaline" in ph_cat:
        score -= 15.0
    if "Saline" in ec_cat:
        score -= 20.0
    if "Low" in n_cat:
        score -= 12.0
    if "Low" in p_cat:
        score -= 10.0
    if "Low" in k_cat:
        score -= 8.0
    if "Low" in oc_cat:
        score -= 10.0

    amendment = None
    if sample.ph < 5.5:
        amendment = f"Apply Agricultural Lime (CaCO3) @ 2.0 t/ha to correct acidity ({sample.ph})."
    elif sample.ph > 8.5:
        amendment = f"Apply Agricultural Gypsum (CaSO4·2H2O) @ 2.5 t/ha with ponded leaching to neutralize sodicity ({sample.ph})."

    return SoilHealthCardSummary(
        sample_id=sample.id,
        sample_code=sample.sample_code,
        ph_rating=ph_cat,
        ph_diagnosis=ph_diag,
        ec_rating=ec_cat,
        ec_diagnosis=ec_diag,
        oc_rating=oc_cat,
        nitrogen_rating=n_cat,
        phosphorus_rating=p_cat,
        potassium_rating=k_cat,
        texture_class=sample.texture_class,
        overall_health_score_pct=max(20.0, score),
        amendment_prescription=amendment,
    )
