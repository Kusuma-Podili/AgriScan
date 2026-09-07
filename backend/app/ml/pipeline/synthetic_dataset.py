"""
AgroPulse Synthetic Agronomic Training Data Generator.
Generates multi-variate, biologically consistent agricultural datasets across all registered crops
using constrained Gaussian mixture models, domain covariance matrices, and physiological boundaries.
"""

from typing import List, Tuple, Dict, Optional
import numpy as np
from app.ml.data.crop_database import CROP_DATABASE, CropAgronomicProfile, list_all_crops
from app.ml.pipeline.feature_engineering import RawAgroFeatures, AgroFeatureTransformer


class SyntheticAgroDataGenerator:
    """
    Synthesizes diverse crop-soil-weather training datasets mirroring global agricultural regions.
    """

    @classmethod
    def generate_crop_samples(
        cls,
        crop: CropAgronomicProfile,
        num_samples: int = 100,
        noise_level: float = 0.08,
        random_seed: Optional[int] = 42,
    ) -> List[RawAgroFeatures]:
        """
        Synthesizes realistic training observations specifically tailored to the physiological envelope of a crop.
        """
        rng = np.random.default_rng(random_seed)
        samples: List[RawAgroFeatures] = []

        # Target center points (optimal ranges)
        t_opt_mean = (crop.temp_opt_min_c + crop.temp_opt_max_c) / 2.0
        t_std = max(1.5, (crop.temp_opt_max_c - crop.temp_opt_min_c) / 3.0)

        r_opt_mean = (crop.rainfall_opt_min_mm + crop.rainfall_opt_max_mm) / 2.0
        r_std = max(25.0, (crop.rainfall_opt_max_mm - crop.rainfall_opt_min_mm) / 3.5)

        ph_opt_mean = (crop.ph_opt_min + crop.ph_opt_max) / 2.0
        ph_std = max(0.2, (crop.ph_opt_max - crop.ph_opt_min) / 3.0)

        # Baseline nutrient demands
        n_base = crop.nutrient_uptake.n_kg_per_ton * crop.benchmark_yield_ton_ha * 1.5
        p_base = crop.nutrient_uptake.p2o5_kg_per_ton * crop.benchmark_yield_ton_ha * 0.8
        k_base = crop.nutrient_uptake.k2o_kg_per_ton * crop.benchmark_yield_ton_ha * 1.2

        for _ in range(num_samples):
            # Sample temperature and clip strictly within plausible physiological boundaries
            temp = float(rng.normal(t_opt_mean, t_std * (1.0 + noise_level)))
            temp = max(crop.temp_min_c + 0.5, min(crop.temp_max_c - 0.5, temp))

            # Sample rainfall with right-skewed log-normal / normal distribution
            rain = float(rng.normal(r_opt_mean, r_std * (1.0 + noise_level)))
            rain = max(crop.rainfall_min_mm + 10.0, min(crop.rainfall_max_mm - 10.0, rain))

            # Sample pH
            ph_val = float(rng.normal(ph_opt_mean, ph_std))
            ph_val = max(crop.ph_min + 0.2, min(crop.ph_max - 0.2, ph_val))

            # Humidity inversely correlates with temperature and positively with rainfall
            rh_base = 55.0 + (rain / 20.0) - (temp * 0.3)
            rh_val = float(np.clip(rng.normal(rh_base, 8.0), 20.0, 95.0))

            # Soil Nutrients
            n_val = float(max(20.0, rng.normal(n_base, n_base * 0.25)))
            p_val = float(max(8.0, rng.normal(p_base, p_base * 0.30)))
            k_val = float(max(30.0, rng.normal(k_base, k_base * 0.25)))

            # Soil texture fractions based on suitable textures
            if "clay" in [t.lower() for t in crop.suitable_soil_textures]:
                clay = float(rng.uniform(35.0, 60.0))
                sand = float(rng.uniform(15.0, 35.0))
            elif "sandy" in [t.lower() for t in crop.suitable_soil_textures]:
                sand = float(rng.uniform(55.0, 80.0))
                clay = float(rng.uniform(8.0, 20.0))
            else:
                sand = float(rng.uniform(30.0, 50.0))
                clay = float(rng.uniform(15.0, 30.0))

            ec_val = float(max(0.2, rng.normal(crop.salinity_tolerance_ds_m * 0.4, 0.3)))
            oc_val = float(np.clip(rng.normal(0.65, 0.20), 0.15, 2.50))

            sample = RawAgroFeatures(
                n_kg_ha=round(n_val, 1),
                p_kg_ha=round(p_val, 1),
                k_kg_ha=round(k_val, 1),
                ph=round(ph_val, 2),
                organic_carbon_pct=round(oc_val, 2),
                ec_ds_m=round(ec_val, 2),
                sand_pct=round(sand, 1),
                clay_pct=round(clay, 1),
                temperature_c=round(temp, 1),
                humidity_pct=round(rh_val, 1),
                rainfall_mm=round(rain, 1),
                elevation_m=round(float(rng.uniform(50.0, 900.0)), 1),
            )
            samples.append(sample)

        return samples

    @classmethod
    def generate_full_training_set(
        cls,
        samples_per_crop: int = 60,
    ) -> Tuple[np.ndarray, np.ndarray, List[str]]:
        """
        Generates engineered feature matrix X and label vector y across all crops in CROP_DATABASE.
        Returns (X, y, crop_labels).
        """
        crops = list_all_crops()
        crop_labels = [c.id for c in crops]
        label_to_idx = {c.id: i for i, c in enumerate(crops)}

        all_raw_features: List[RawAgroFeatures] = []
        labels: List[int] = []

        for crop in crops:
            samples = cls.generate_crop_samples(crop, num_samples=samples_per_crop)
            all_raw_features.extend(samples)
            labels.extend([label_to_idx[crop.id]] * len(samples))

        x_matrix = AgroFeatureTransformer.transform_batch_numpy(all_raw_features)
        y_vector = np.array(labels, dtype=np.int64)

        return x_matrix, y_vector, crop_labels
