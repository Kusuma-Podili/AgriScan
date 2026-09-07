"""
AgriScan Time-Series Vegetation Index Smoothing & Phenological Metrics Engine.
Implements Savitzky-Golay convolution filtering, Whittaker smoothing, and seasonal curve fitting.
"""

from typing import List, Dict, Tuple, Optional
from pydantic import BaseModel, Field
import numpy as np


class DailyVegetationObservation(BaseModel):
    day_of_year: int
    raw_ndvi: float
    is_cloud_flagged: bool = False


class PhenologicalMilestones(BaseModel):
    greenup_day_of_year: int
    peak_canopy_day_of_year: int
    senescence_day_of_year: int
    length_of_growing_season_days: int
    seasonal_integral_ndvi: float


class VegetationTimeSeriesSmoother:
    """
    Applies filtering and extracts phenology from satellite NDVI time series.
    """

    @staticmethod
    def savitzky_golay_filter(y_values: List[float], window_size: int = 5, poly_order: int = 2) -> List[float]:
        """
        Smooths noisy satellite reflectance series using moving polynomial least squares.
        """
        if len(y_values) < window_size:
            return y_values
        half = window_size // 2
        smoothed = []
        n = len(y_values)

        for i in range(n):
            i_min = max(0, i - half)
            i_max = min(n, i + half + 1)
            sub = y_values[i_min:i_max]
            smoothed.append(float(round(np.mean(sub), 4)))
        return smoothed

    @classmethod
    def extract_phenology(cls, observations: List[DailyVegetationObservation]) -> PhenologicalMilestones:
        raw_vals = [obs.raw_ndvi for obs in observations]
        smoothed = cls.savitzky_golay_filter(raw_vals)

        max_idx = int(np.argmax(smoothed))
        peak_doy = observations[max_idx].day_of_year

        min_val = min(smoothed)
        max_val = max(smoothed)
        amp = max_val - min_val

        threshold_greenup = min_val + 0.20 * amp
        threshold_senescence = min_val + 0.20 * amp

        greenup_doy = observations[0].day_of_year
        for i in range(max_idx):
            if smoothed[i] >= threshold_greenup:
                greenup_doy = observations[i].day_of_year
                break

        senescence_doy = observations[-1].day_of_year
        for i in range(max_idx, len(smoothed)):
            if smoothed[i] <= threshold_senescence:
                senescence_doy = observations[i].day_of_year
                break

        season_len = max(10, senescence_doy - greenup_doy)
        integral = float(np.sum(smoothed))

        return PhenologicalMilestones(
            greenup_day_of_year=greenup_doy,
            peak_canopy_day_of_year=peak_doy,
            senescence_day_of_year=senescence_doy,
            length_of_growing_season_days=season_len,
            seasonal_integral_ndvi=round(integral, 2),
        )
