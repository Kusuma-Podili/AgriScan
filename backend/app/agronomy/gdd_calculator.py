"""
Growing Degree Days (GDD) & Thermal Unit Accumulation Engine.

Calculates heat units and stage transitions for major crops:
Wheat, Rice, Maize, Sorghum, Cotton.
"""

from typing import Dict, Any
from dataclasses import dataclass


@dataclass
class CropGDDParameters:
    crop_name: str
    base_temp_c: float
    cutoff_temp_c: float
    gdd_emergence: float
    gdd_vegetative: float
    gdd_anthesis: float
    gdd_maturity: float


CROP_GDD_DATABASE: Dict[str, CropGDDParameters] = {
    "wheat": CropGDDParameters("Wheat", 4.0, 30.0, 120.0, 550.0, 1100.0, 1850.0),
    "rice": CropGDDParameters("Rice", 10.0, 35.0, 100.0, 650.0, 1300.0, 2100.0),
    "maize": CropGDDParameters("Maize (Corn)", 10.0, 34.0, 90.0, 700.0, 1250.0, 2400.0),
    "cotton": CropGDDParameters("Cotton", 15.5, 38.0, 110.0, 850.0, 1550.0, 2600.0),
    "sorghum": CropGDDParameters("Sorghum", 10.0, 35.0, 95.0, 600.0, 1200.0, 2050.0),
}


def calculate_daily_gdd(t_max: float, t_min: float, t_base: float, t_cutoff: float) -> float:
    t_max_adj = min(t_cutoff, max(t_base, t_max))
    t_min_adj = min(t_cutoff, max(t_base, t_min))
    t_mean = (t_max_adj + t_min_adj) / 2.0
    return max(0.0, t_mean - t_base)


def estimate_phenology_stage(crop_key: str, accumulated_gdd: float) -> Dict[str, Any]:
    crop = CROP_GDD_DATABASE.get(crop_key.lower())
    if not crop:
        return {"error": f"Crop '{crop_key}' not in GDD database"}

    if accumulated_gdd < crop.gdd_emergence:
        stage = "Germination / Emergence"
        progress = (accumulated_gdd / crop.gdd_emergence) * 100.0
    elif accumulated_gdd < crop.gdd_vegetative:
        stage = "Vegetative Growth & Tillering/Stem Elongation"
        progress = ((accumulated_gdd - crop.gdd_emergence) / (crop.gdd_vegetative - crop.gdd_emergence)) * 100.0
    elif accumulated_gdd < crop.gdd_anthesis:
        stage = "Reproductive / Flowering / Anthesis"
        progress = ((accumulated_gdd - crop.gdd_vegetative) / (crop.gdd_anthesis - crop.gdd_vegetative)) * 100.0
    elif accumulated_gdd < crop.gdd_maturity:
        stage = "Grain Filling / Ripening"
        progress = ((accumulated_gdd - crop.gdd_anthesis) / (crop.gdd_maturity - crop.gdd_anthesis)) * 100.0
    else:
        stage = "Physiological Maturity / Harvest Ready"
        progress = 100.0

    return {
        "crop_name": crop.crop_name,
        "accumulated_gdd": accumulated_gdd,
        "current_phenological_stage": stage,
        "stage_completion_pct": round(min(100.0, progress), 1),
        "total_required_gdd": crop.gdd_maturity,
        "remaining_gdd_to_harvest": max(0.0, crop.gdd_maturity - accumulated_gdd),
    }
