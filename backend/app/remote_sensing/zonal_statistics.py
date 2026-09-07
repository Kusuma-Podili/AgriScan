"""
AgriScan Spatial Zonal Statistics & Canopy Anomaly Classifier.
Calculates polygon-level pixel distributions, nitrogen deficiency zones, and prescription grids.
"""

from typing import List, Dict, Tuple
from pydantic import BaseModel, Field
import numpy as np


class FieldParcelZonalMetrics(BaseModel):
    parcel_id: str
    total_pixel_count: int
    mean_ndvi: float
    std_ndvi: float
    min_ndvi: float
    max_ndvi: float
    p10_ndvi: float
    p90_ndvi: float
    uniformity_coefficient_pct: float
    high_vigor_area_pct: float
    low_vigor_stressed_area_pct: float


class ParcelZonalStatsProcessor:
    @staticmethod
    def compute_zonal_stats(parcel_id: str, pixel_ndvi_values: List[float]) -> FieldParcelZonalMetrics:
        arr = np.array(pixel_ndvi_values, dtype=float)
        mean_v = float(np.mean(arr))
        std_v = float(np.std(arr))
        cv = (std_v / max(0.01, mean_v)) * 100.0
        uniformity = float(np.clip(100.0 - cv, 0.0, 100.0))

        p10 = float(np.percentile(arr, 10))
        p90 = float(np.percentile(arr, 90))

        high_pct = float(np.mean(arr > 0.65) * 100.0)
        low_pct = float(np.mean(arr < 0.35) * 100.0)

        return FieldParcelZonalMetrics(
            parcel_id=parcel_id,
            total_pixel_count=len(pixel_ndvi_values),
            mean_ndvi=round(mean_v, 3),
            std_ndvi=round(std_v, 3),
            min_ndvi=round(float(np.min(arr)), 3),
            max_ndvi=round(float(np.max(arr)), 3),
            p10_ndvi=round(p10, 3),
            p90_ndvi=round(p90, 3),
            uniformity_coefficient_pct=round(uniformity, 1),
            high_vigor_area_pct=round(high_pct, 1),
            low_vigor_stressed_area_pct=round(low_pct, 1),
        )
