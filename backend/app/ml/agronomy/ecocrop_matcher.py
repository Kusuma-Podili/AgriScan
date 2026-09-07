"""
AgroPulse FAO EcoCrop Suitability Engine.
Implements the continuous mathematical response curve formulation of the FAO EcoCrop model
to evaluate agro-climatic and edaphic suitability across 120+ crops.
"""

import math
from typing import Dict, List, Optional, Tuple
from pydantic import BaseModel, Field
from app.ml.data.crop_database import CropAgronomicProfile, CROP_DATABASE, list_all_crops


class EnvironmentalConditions(BaseModel):
    mean_temperature_c: float = Field(..., ge=-20.0, le=60.0, description="Mean growing season temperature (°C)")
    min_temperature_c: Optional[float] = Field(None, description="Absolute minimum night temperature (°C)")
    max_temperature_c: Optional[float] = Field(None, description="Absolute maximum day temperature (°C)")
    total_rainfall_mm: float = Field(..., ge=0.0, le=6000.0, description="Total rainfall + irrigation availability (mm)")
    soil_ph: float = Field(..., ge=3.0, le=12.0, description="Soil pH")
    soil_salinity_ec_ds_m: float = Field(0.8, ge=0.0, le=40.0, description="Soil Electrical Conductivity ECe in dS/m")
    soil_texture: str = Field("loam", description="USDA soil texture class")
    drainage_class: str = Field("Well drained", description="Soil drainage class")


class FactorSuitabilityScore(BaseModel):
    score: float = Field(..., ge=0.0, le=100.0, description="Suitability percentage for this factor (0-100%)")
    status: str  # Optimal, Sub-optimal, Marginally viable, Unsuitable (Lethal)
    limiting_message: Optional[str] = None


class CropSuitabilityEvaluation(BaseModel):
    crop_id: str
    crop_name: str
    category: str
    overall_suitability_score: float = Field(..., ge=0.0, le=100.0)
    fao_suitability_class: str  # S1 (Highly), S2 (Moderately), S3 (Marginally), N1 (Currently not), N2 (Permanently not)
    temperature_suitability: FactorSuitabilityScore
    rainfall_suitability: FactorSuitabilityScore
    ph_suitability: FactorSuitabilityScore
    salinity_suitability: FactorSuitabilityScore
    texture_suitability: FactorSuitabilityScore
    primary_limiting_factor: str
    agronomic_advisory: str


class FAOEcoCropMatcher:
    """
    Mathematical evaluator conforming to FAO EcoCrop trapezoidal response curves.
    """

    @staticmethod
    def calculate_trapezoid_suitability(
        x: float,
        abs_min: float,
        opt_min: float,
        opt_max: float,
        abs_max: float,
    ) -> Tuple[float, str, Optional[str]]:
        """
        Computes 0-100 continuous suitability score for parameter x against
        [abs_min, opt_min, opt_max, abs_max] envelope.
        """
        if x < abs_min:
            deficit = abs_min - x
            return (0.0, "Unsuitable (Lethal Min)", f"Value {x:.1f} is {deficit:.1f} below minimum threshold ({abs_min:.1f})")
        elif x > abs_max:
            excess = x - abs_max
            return (0.0, "Unsuitable (Lethal Max)", f"Value {x:.1f} exceeds absolute upper threshold ({abs_max:.1f}) by {excess:.1f}")
        elif opt_min <= x <= opt_max:
            return (100.0, "Optimal", None)
        elif abs_min <= x < opt_min:
            # Ascending ramp
            ratio = (x - abs_min) / (opt_min - abs_min)
            score = ratio * 100.0
            return (round(score, 1), "Sub-optimal (Low)", f"Value {x:.1f} is below optimum range [{opt_min:.1f} - {opt_max:.1f}]")
        else:  # opt_max < x <= abs_max
            # Descending ramp
            ratio = (abs_max - x) / (abs_max - opt_max)
            score = ratio * 100.0
            return (round(score, 1), "Sub-optimal (High)", f"Value {x:.1f} is above optimum range [{opt_min:.1f} - {opt_max:.1f}]")

    @classmethod
    def evaluate_crop(
        cls,
        crop: CropAgronomicProfile,
        env: EnvironmentalConditions,
    ) -> CropSuitabilityEvaluation:
        """
        Evaluates a single crop against environmental parameters and computes weighted composite index.
        """
        # 1. Temperature Suitability
        t_score, t_status, t_msg = cls.calculate_trapezoid_suitability(
            x=env.mean_temperature_c,
            abs_min=crop.temp_min_c,
            opt_min=crop.temp_opt_min_c,
            opt_max=crop.temp_opt_max_c,
            abs_max=crop.temp_max_c,
        )

        # 2. Moisture / Rainfall Suitability
        r_score, r_status, r_msg = cls.calculate_trapezoid_suitability(
            x=env.total_rainfall_mm,
            abs_min=crop.rainfall_min_mm,
            opt_min=crop.rainfall_opt_min_mm,
            opt_max=crop.rainfall_opt_max_mm,
            abs_max=crop.rainfall_max_mm,
        )

        # 3. Soil pH Suitability
        ph_score, ph_status, ph_msg = cls.calculate_trapezoid_suitability(
            x=env.soil_ph,
            abs_min=crop.ph_min,
            opt_min=crop.ph_opt_min,
            opt_max=crop.ph_opt_max,
            abs_max=crop.ph_max,
        )

        # 4. Salinity Suitability (Threshold curve)
        if env.soil_salinity_ec_ds_m <= crop.salinity_tolerance_ds_m:
            ec_score = 100.0
            ec_status = "Optimal"
            ec_msg = None
        else:
            # Linear degradation past threshold: 12% yield decline per dS/m past threshold
            excess_ec = env.soil_salinity_ec_ds_m - crop.salinity_tolerance_ds_m
            ec_score = max(0.0, 100.0 - (excess_ec * 15.0))
            ec_status = "Salinity Stress" if ec_score > 0 else "Lethal Salinity"
            ec_msg = f"Soil salinity EC ({env.soil_salinity_ec_ds_m:.1f} dS/m) exceeds tolerance threshold ({crop.salinity_tolerance_ds_m:.1f} dS/m)"

        # 5. Soil Texture Suitability
        norm_texture = env.soil_texture.replace("_", " ").lower().strip()
        matched = any(norm_texture in t.lower() or t.lower() in norm_texture for t in crop.suitable_soil_textures)
        if matched:
            text_score = 100.0
            text_status = "Optimal Texture"
            text_msg = None
        else:
            text_score = 65.0  # Still cultivable with proper management
            text_status = "Sub-optimal Texture"
            text_msg = f"Soil texture '{env.soil_texture}' is sub-optimal for {crop.name}"

        # Combine scores using Weighted Multi-Criteria Decision Analysis (MCDA)
        # Weights: Temperature: 0.30, Moisture: 0.30, pH: 0.20, Salinity: 0.10, Texture: 0.10
        composite_score = (
            (t_score * 0.30)
            + (r_score * 0.30)
            + (ph_score * 0.20)
            + (ec_score * 0.10)
            + (text_score * 0.10)
        )

        # If any primary factor (temp, moisture, pH) is 0 (lethal), cap total score to < 20%
        if t_score == 0.0 or r_score == 0.0 or ph_score == 0.0:
            composite_score = min(composite_score, 18.0)

        composite_score = round(composite_score, 1)

        # Classify into FAO Land Suitability Classification
        if composite_score >= 80.0:
            fao_class = "S1 - Highly Suitable"
        elif composite_score >= 60.0:
            fao_class = "S2 - Moderately Suitable"
        elif composite_score >= 40.0:
            fao_class = "S3 - Marginally Suitable"
        elif composite_score >= 20.0:
            fao_class = "N1 - Currently Not Suitable"
        else:
            fao_class = "N2 - Permanently Not Suitable"

        # Determine the primary limiting constraint
        scores_map = {
            "Temperature": t_score,
            "Rainfall / Moisture": r_score,
            "Soil pH": ph_score,
            "Salinity": ec_score,
            "Soil Texture": text_score,
        }
        min_factor = min(scores_map, key=scores_map.get)
        limiting_desc = f"{min_factor} (Score: {scores_map[min_factor]:.1f}%)"

        return CropSuitabilityEvaluation(
            crop_id=crop.id,
            crop_name=crop.name,
            category=crop.category,
            overall_suitability_score=composite_score,
            fao_suitability_class=fao_class,
            temperature_suitability=FactorSuitabilityScore(score=t_score, status=t_status, limiting_message=t_msg),
            rainfall_suitability=FactorSuitabilityScore(score=r_score, status=r_status, limiting_message=r_msg),
            ph_suitability=FactorSuitabilityScore(score=ph_score, status=ph_status, limiting_message=ph_msg),
            salinity_suitability=FactorSuitabilityScore(score=ec_score, status=ec_status, limiting_message=ec_msg),
            texture_suitability=FactorSuitabilityScore(score=text_score, status=text_status, limiting_message=text_msg),
            primary_limiting_factor=limiting_desc,
            agronomic_advisory=crop.agronomic_advisory,
        )

    @classmethod
    def rank_all_crops(
        cls,
        env: EnvironmentalConditions,
        category_filter: Optional[str] = None,
        top_k: int = 15,
    ) -> List[CropSuitabilityEvaluation]:
        """
        Evaluates and ranks all crops in the knowledge base from most suitable to least suitable.
        """
        crops = list_all_crops()
        if category_filter:
            crops = [c for c in crops if c.category.lower() == category_filter.lower().strip()]

        evaluations = [cls.evaluate_crop(crop, env) for crop in crops]
        # Sort descending by suitability score
        evaluations.sort(key=lambda x: x.overall_suitability_score, reverse=True)
        return evaluations[:top_k]
