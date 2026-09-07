"""
AgroPulse Crop Yield Prediction & Agro-Climatic Sensitivity Simulator.
Implements the FAO-33 Doorenbos-Kassam yield response to water stress (Ky factor)
and Mitscherlich-Baule multi-nutrient law with Bayesian Monte Carlo climate simulation.
"""

import math
from typing import Dict, List, Optional, Tuple, Any
import numpy as np
from pydantic import BaseModel, Field
from app.ml.data.crop_database import CropAgronomicProfile, get_crop_by_id


class YieldSimulationScenario(BaseModel):
    scenario_name: str  # Baseline, Moderate Drought (-25% Rain), Severe Drought (-45%), Heatwave (+3°C)
    mean_expected_yield_ton_ha: float
    p10_pessimistic_yield_ton_ha: float
    p90_optimistic_yield_ton_ha: float
    expected_revenue_usd_ha: float
    expected_profit_usd_ha: float
    water_stress_penalty_pct: float
    nutrient_limitation_penalty_pct: float


class YieldEstimationReport(BaseModel):
    crop_id: str
    crop_name: str
    benchmark_yield_ton_ha: float
    simulated_baseline_yield_ton_ha: float
    water_response_ky_factor: float
    limiting_resource: str
    scenarios: List[YieldSimulationScenario]
    confidence_interval_95: Tuple[float, float]


class YieldResponseSimulator:
    """
    Simulates actual attainable crop yield (Ya) vs potential maximum yield (Ym).
    """

    # Empirical FAO-33 Yield Response Factors (Ky) representing yield sensitivity to water deficit
    CROP_KY_FACTORS: Dict[str, float] = {
        "maize": 1.25,     # Highly sensitive (Ky > 1.0)
        "banana": 1.20,
        "sugarcane": 1.20,
        "potato": 1.10,
        "tomato": 1.05,
        "wheat": 1.00,
        "soybean": 0.85,
        "chickpea": 0.85,
        "groundnut": 0.70,
        "cotton": 0.85,
        "rice": 1.15,
        "sorghum": 0.90,
        "pearl_millet": 0.75,  # Highly drought-tolerant (Ky < 0.8)
        "barley": 1.00,
        "alfalfa": 1.10,
    }

    # Mitscherlich-Baule nutrient curvature parameters
    C_N = 0.005
    C_P = 0.040
    C_K = 0.008

    @classmethod
    def calculate_fao33_water_yield(
        cls,
        crop_id: str,
        benchmark_yield: float,
        actual_water_mm: float,
        crop_water_req_mm: float,
    ) -> Tuple[float, float]:
        """
        Computes yield reduction from water stress via:
        (1 - Ya/Ym) = Ky * (1 - ETa/ETm)
        """
        ky = cls.CROP_KY_FACTORS.get(crop_id, 1.0)

        water_ratio = min(1.0, actual_water_mm / max(1.0, crop_water_req_mm))
        water_deficit = 1.0 - water_ratio

        # Yield reduction fraction
        yield_reduction_fraction = min(1.0, ky * water_deficit)
        attainable_yield = benchmark_yield * (1.0 - yield_reduction_fraction)
        penalty_pct = round(yield_reduction_fraction * 100.0, 1)

        return max(0.0, attainable_yield), penalty_pct

    @classmethod
    def calculate_mitscherlich_nutrient_yield(
        cls,
        benchmark_yield: float,
        n_kg_ha: float,
        p_kg_ha: float,
        k_kg_ha: float,
    ) -> Tuple[float, float]:
        """
        Mitscherlich-Baule law for simultaneous multi-nutrient plateau:
        Y = Ym * (1 - 10^(-cn*N)) * (1 - 10^(-cp*P)) * (1 - 10^(-ck*K))
        """
        frac_n = 1.0 - math.pow(10.0, -cls.C_N * n_kg_ha)
        frac_p = 1.0 - math.pow(10.0, -cls.C_P * p_kg_ha)
        frac_k = 1.0 - math.pow(10.0, -cls.C_K * k_kg_ha)

        nutrient_factor = max(0.1, min(1.0, frac_n * frac_p * frac_k))
        attainable_yield = benchmark_yield * nutrient_factor
        penalty_pct = round((1.0 - nutrient_factor) * 100.0, 1)

        return attainable_yield, penalty_pct

    @classmethod
    def run_monte_carlo_simulation(
        cls,
        crop_id: str,
        soil_n: float,
        soil_p: float,
        soil_k: float,
        rainfall_mm: float,
        mean_temp_c: float,
        num_simulations: int = 500,
        random_seed: int = 42,
    ) -> YieldEstimationReport:
        """
        Performs Bayesian Monte Carlo sampling of climate trajectories to generate yield risk distributions.
        """
        crop = get_crop_by_id(crop_id)
        if not crop:
            raise ValueError(f"Crop {crop_id} not recognized.")

        rng = np.random.default_rng(random_seed)
        benchmark_yield = crop.benchmark_yield_ton_ha
        ky = cls.CROP_KY_FACTORS.get(crop_id, 1.0)

        # Baseline Simulation
        water_yield, water_pen = cls.calculate_fao33_water_yield(
            crop_id=crop_id,
            benchmark_yield=benchmark_yield,
            actual_water_mm=rainfall_mm,
            crop_water_req_mm=crop.typical_water_req_mm,
        )

        nut_yield, nut_pen = cls.calculate_mitscherlich_nutrient_yield(
            benchmark_yield=benchmark_yield,
            n_kg_ha=soil_n,
            p_kg_ha=soil_p,
            k_kg_ha=soil_k,
        )

        # Combined Liebig law: Most limiting resource governs potential
        baseline_yield = min(water_yield, nut_yield)
        limiting = "Soil Nutrient Supply" if nut_yield < water_yield else "Water / Rainfall Availability"

        scenarios_defs = [
            ("Normal Climate Scenario", 0.0, 0.0),
            ("Moderate Drought (-25% Precipitation)", -0.25, 1.0),
            ("Severe Prolonged Drought (-45% Precipitation)", -0.45, 2.0),
            ("Extreme Heatwave (+3.5°C Mean Temp)", -0.10, 3.5),
        ]

        scenario_results: List[YieldSimulationScenario] = []

        for name, rain_delta_pct, temp_delta_c in scenarios_defs:
            simulated_yields: List[float] = []

            for _ in range(num_simulations):
                # Sample noise for seasonal rainfall and temp
                sim_rain = max(10.0, rainfall_mm * (1.0 + rain_delta_pct) * rng.normal(1.0, 0.12))
                sim_temp = mean_temp_c + temp_delta_c + float(rng.normal(0.0, 0.8))

                # Water stress component
                y_w, pen_w = cls.calculate_fao33_water_yield(
                    crop_id=crop_id,
                    benchmark_yield=benchmark_yield,
                    actual_water_mm=sim_rain,
                    crop_water_req_mm=crop.typical_water_req_mm,
                )

                # Heat stress penalty if temperature surpasses optimal max
                heat_pen = 0.0
                if sim_temp > crop.temp_opt_max_c:
                    heat_pen = min(0.60, (sim_temp - crop.temp_opt_max_c) * 0.10)

                y_final = min(y_w, nut_yield) * (1.0 - heat_pen)
                simulated_yields.append(max(0.2, y_final))

            mean_y = float(np.mean(simulated_yields))
            p10_y = float(np.percentile(simulated_yields, 10))
            p90_y = float(np.percentile(simulated_yields, 90))

            rev = mean_y * crop.market_price_usd_per_ton
            cost = crop.cost_of_cultivation_usd_ha
            prof = rev - cost

            scenario_results.append(
                YieldSimulationScenario(
                    scenario_name=name,
                    mean_expected_yield_ton_ha=round(mean_y, 2),
                    p10_pessimistic_yield_ton_ha=round(p10_y, 2),
                    p90_optimistic_yield_ton_ha=round(p90_y, 2),
                    expected_revenue_usd_ha=round(rev, 1),
                    expected_profit_usd_ha=round(prof, 1),
                    water_stress_penalty_pct=water_pen,
                    nutrient_limitation_penalty_pct=nut_pen,
                )
            )

        baseline_scen = scenario_results[0]
        ci_95 = (baseline_scen.p10_pessimistic_yield_ton_ha, baseline_scen.p90_optimistic_yield_ton_ha)

        return YieldEstimationReport(
            crop_id=crop_id,
            crop_name=crop.name,
            benchmark_yield_ton_ha=benchmark_yield,
            simulated_baseline_yield_ton_ha=round(baseline_yield, 2),
            water_response_ky_factor=ky,
            limiting_resource=limiting,
            scenarios=scenario_results,
            confidence_interval_95=ci_95,
        )
