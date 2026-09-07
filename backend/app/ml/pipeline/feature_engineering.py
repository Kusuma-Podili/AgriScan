"""
AgroPulse Agricultural Feature Engineering & Preprocessing Pipeline.
Constructs domain-specific agronomic indices, stoichiometric nutrient ratios,
moisture stress ratios, and bio-climatic interaction terms.
"""

import math
from typing import Dict, List, Optional, Tuple, Any
import numpy as np
from pydantic import BaseModel, Field


class RawAgroFeatures(BaseModel):
    n_kg_ha: float = Field(..., ge=0, description="Available Soil Nitrogen (kg/ha)")
    p_kg_ha: float = Field(..., ge=0, description="Available Soil Phosphorus (kg/ha)")
    k_kg_ha: float = Field(..., ge=0, description="Available Soil Potassium (kg/ha)")
    ph: float = Field(..., ge=3.0, le=12.0, description="Soil pH")
    organic_carbon_pct: float = Field(0.5, ge=0.0, le=10.0, description="Soil Organic Carbon %")
    ec_ds_m: float = Field(0.8, ge=0.0, description="Soil EC in dS/m")
    sand_pct: float = Field(40.0, ge=0.0, le=100.0, description="Sand percentage")
    clay_pct: float = Field(20.0, ge=0.0, le=100.0, description="Clay percentage")
    temperature_c: float = Field(..., ge=-10.0, le=55.0, description="Mean growing season temperature (°C)")
    temp_max_c: Optional[float] = Field(None, description="Maximum day temperature (°C)")
    temp_min_c: Optional[float] = Field(None, description="Minimum night temperature (°C)")
    humidity_pct: float = Field(..., ge=5.0, le=100.0, description="Relative humidity %")
    rainfall_mm: float = Field(..., ge=0.0, le=5000.0, description="Total season rainfall / water availability (mm)")
    elevation_m: float = Field(150.0, ge=-50.0, le=5000.0, description="Elevation above sea level (m)")


class EngineeredFeatureVector(BaseModel):
    feature_names: List[str]
    values: List[float]
    summary_dict: Dict[str, float]


class AgroFeatureTransformer:
    """
    Transforms raw agronomic & meteorological measurements into advanced feature vectors.
    """

    FEATURE_NAMES = [
        # Raw Base Features (10)
        "soil_n",
        "soil_p",
        "soil_k",
        "soil_ph",
        "soil_oc",
        "soil_ec",
        "sand_pct",
        "clay_pct",
        "temperature",
        "humidity",
        "rainfall",
        "elevation",
        # Engineered Stoichiometric Nutrient Ratios (5)
        "n_p_ratio",
        "n_k_ratio",
        "p_k_ratio",
        "total_npk_sum",
        "npk_fertility_index",
        # Bio-Climatic & Hydro-Thermal Features (6)
        "diurnal_temp_range",
        "vapor_pressure_deficit_est",
        "temp_humidity_index",
        "rain_per_degree_c",
        "moisture_adequacy_index",
        "soil_water_holding_capacity_est",
        # Soil Chemical Availability Modifiers (3)
        "ph_acidity_penalty",
        "ph_alkalinity_penalty",
        "salinity_stress_index",
    ]

    @classmethod
    def transform(cls, raw: RawAgroFeatures) -> EngineeredFeatureVector:
        """
        Executes feature transformation pipeline on raw measurements.
        """
        # 1. Nutrient Stoichiometric Ratios
        safe_p = max(0.1, raw.p_kg_ha)
        safe_k = max(0.1, raw.k_kg_ha)
        n_p_ratio = raw.n_kg_ha / safe_p
        n_k_ratio = raw.n_kg_ha / safe_k
        p_k_ratio = raw.p_kg_ha / safe_k
        total_npk = raw.n_kg_ha + raw.p_kg_ha + raw.k_kg_ha

        # Normalized fertility index (0 to 10 scale)
        fertility_index = (
            min(raw.n_kg_ha / 350.0, 1.0) * 4.0
            + min(raw.p_kg_ha / 35.0, 1.0) * 3.0
            + min(raw.k_kg_ha / 250.0, 1.0) * 3.0
        )

        # 2. Diurnal Temperature Range & Thermal Metrics
        t_max = raw.temp_max_c if raw.temp_max_c is not None else raw.temperature_c + 5.0
        t_min = raw.temp_min_c if raw.temp_min_c is not None else raw.temperature_c - 5.0
        dtr = max(1.0, t_max - t_min)

        # Approximate saturated vapor pressure (Tetens) and VPD
        es = 0.6108 * math.exp((17.27 * raw.temperature_c) / (raw.temperature_c + 237.3))
        ea = es * (raw.humidity_pct / 100.0)
        vpd_est = max(0.0, es - ea)

        # Temperature-Humidity Index (THI)
        thi = (0.8 * raw.temperature_c) + ((raw.humidity_pct / 100.0) * (raw.temperature_c - 14.4)) + 46.4

        # Rainfall per degree Celsius thermal efficiency
        rain_per_degree = raw.rainfall_mm / max(5.0, raw.temperature_c)

        # Moisture Adequacy Index: Ratio of rainfall to empirical potential evapotranspiration
        # Thornthwaite / Hargreaves approximation: PET ~ 4.5 mm/day * 120 days = 540 mm benchmark
        moisture_adequacy = min(3.0, raw.rainfall_mm / 540.0)

        # Estimated Available Water Holding Capacity (AWC) based on Clay %
        # Heavy clay soils hold more water (~150-180 mm/m) compared to sands (~50-80 mm/m)
        awc_est = 60.0 + (raw.clay_pct * 1.8) - (raw.sand_pct * 0.4)
        awc_est = max(40.0, min(220.0, awc_est))

        # 3. Soil Reaction (pH) Penalties
        # Optimal pH is centered at 6.8
        ph_acidity_penalty = max(0.0, 6.0 - raw.ph) ** 1.5
        ph_alkalinity_penalty = max(0.0, raw.ph - 7.5) ** 1.5

        # Salinity Stress Index (threshold = 2.0 dS/m)
        salinity_stress = max(0.0, raw.ec_ds_m - 2.0) ** 1.2

        feature_map = {
            "soil_n": float(raw.n_kg_ha),
            "soil_p": float(raw.p_kg_ha),
            "soil_k": float(raw.k_kg_ha),
            "soil_ph": float(raw.ph),
            "soil_oc": float(raw.organic_carbon_pct),
            "soil_ec": float(raw.ec_ds_m),
            "sand_pct": float(raw.sand_pct),
            "clay_pct": float(raw.clay_pct),
            "temperature": float(raw.temperature_c),
            "humidity": float(raw.humidity_pct),
            "rainfall": float(raw.rainfall_mm),
            "elevation": float(raw.elevation_m),
            "n_p_ratio": round(n_p_ratio, 2),
            "n_k_ratio": round(n_k_ratio, 2),
            "p_k_ratio": round(p_k_ratio, 2),
            "total_npk_sum": round(total_npk, 1),
            "npk_fertility_index": round(fertility_index, 2),
            "diurnal_temp_range": round(dtr, 2),
            "vapor_pressure_deficit_est": round(vpd_est, 3),
            "temp_humidity_index": round(thi, 2),
            "rain_per_degree_c": round(rain_per_degree, 2),
            "moisture_adequacy_index": round(moisture_adequacy, 3),
            "soil_water_holding_capacity_est": round(awc_est, 1),
            "ph_acidity_penalty": round(ph_acidity_penalty, 3),
            "ph_alkalinity_penalty": round(ph_alkalinity_penalty, 3),
            "salinity_stress_index": round(salinity_stress, 3),
        }

        values = [feature_map[name] for name in cls.FEATURE_NAMES]

        return EngineeredFeatureVector(
            feature_names=cls.FEATURE_NAMES,
            values=values,
            summary_dict=feature_map,
        )

    @classmethod
    def transform_batch_numpy(cls, features_list: List[RawAgroFeatures]) -> np.ndarray:
        """
        Batch transformation returning 2D NumPy array of shape (N_samples, N_features).
        """
        transformed = [cls.transform(f).values for f in features_list]
        return np.array(transformed, dtype=np.float32)
