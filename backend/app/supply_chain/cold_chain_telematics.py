"""
AgriScan Cold Chain Thermodynamics & Post-Harvest Respiration Kinetics.
Implements Arrhenius shelf-life equations, respiration heat generation,
and Modified Atmosphere Packaging (MAP) gas transmission rates.
"""

import math
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class CropColdChainProfile(BaseModel):
    crop_name: str
    optimal_temp_c_min: float
    optimal_temp_c_max: float
    chilling_injury_threshold_c: float
    freezing_point_c: float
    optimal_rh_pct_min: float
    optimal_rh_pct_max: float
    respiration_rate_co2_mg_kg_h_0c: float
    q10_temperature_coefficient: float
    ethylene_sensitivity: str  # "Very Low", "Low", "Moderate", "High", "Very High"
    ethylene_production_rate: str
    baseline_shelf_life_days_at_optimal: float


CROP_COLD_PROFILES: Dict[str, CropColdChainProfile] = {
    "apple": CropColdChainProfile(
        crop_name="apple",
        optimal_temp_c_min=-0.5,
        optimal_temp_c_max=1.0,
        chilling_injury_threshold_c=-1.5,
        freezing_point_c=-1.8,
        optimal_rh_pct_min=90.0,
        optimal_rh_pct_max=95.0,
        respiration_rate_co2_mg_kg_h_0c=3.5,
        q10_temperature_coefficient=2.2,
        ethylene_sensitivity="High",
        ethylene_production_rate="High",
        baseline_shelf_life_days_at_optimal=180.0,
    ),
    "strawberry": CropColdChainProfile(
        crop_name="strawberry",
        optimal_temp_c_min=0.0,
        optimal_temp_c_max=0.5,
        chilling_injury_threshold_c=-0.5,
        freezing_point_c=-0.8,
        optimal_rh_pct_min=90.0,
        optimal_rh_pct_max=95.0,
        respiration_rate_co2_mg_kg_h_0c=15.0,
        q10_temperature_coefficient=2.8,
        ethylene_sensitivity="Low",
        ethylene_production_rate="Very Low",
        baseline_shelf_life_days_at_optimal=10.0,
    ),
    "banana": CropColdChainProfile(
        crop_name="banana",
        optimal_temp_c_min=13.0,
        optimal_temp_c_max=14.5,
        chilling_injury_threshold_c=12.5,
        freezing_point_c=-0.8,
        optimal_rh_pct_min=90.0,
        optimal_rh_pct_max=95.0,
        respiration_rate_co2_mg_kg_h_0c=25.0,
        q10_temperature_coefficient=2.4,
        ethylene_sensitivity="Very High",
        ethylene_production_rate="Moderate",
        baseline_shelf_life_days_at_optimal=21.0,
    ),
    "tomato": CropColdChainProfile(
        crop_name="tomato",
        optimal_temp_c_min=10.0,
        optimal_temp_c_max=12.5,
        chilling_injury_threshold_c=8.0,
        freezing_point_c=-0.5,
        optimal_rh_pct_min=85.0,
        optimal_rh_pct_max=90.0,
        respiration_rate_co2_mg_kg_h_0c=10.0,
        q10_temperature_coefficient=2.1,
        ethylene_sensitivity="Moderate",
        ethylene_production_rate="Moderate",
        baseline_shelf_life_days_at_optimal=14.0,
    ),
    "potato": CropColdChainProfile(
        crop_name="potato",
        optimal_temp_c_min=7.0,
        optimal_temp_c_max=10.0,
        chilling_injury_threshold_c=4.0,
        freezing_point_c=-1.0,
        optimal_rh_pct_min=95.0,
        optimal_rh_pct_max=98.0,
        respiration_rate_co2_mg_kg_h_0c=5.0,
        q10_temperature_coefficient=1.9,
        ethylene_sensitivity="Moderate",
        ethylene_production_rate="Very Low",
        baseline_shelf_life_days_at_optimal=240.0,
    ),
    "lettuce": CropColdChainProfile(
        crop_name="lettuce",
        optimal_temp_c_min=0.0,
        optimal_temp_c_max=1.0,
        chilling_injury_threshold_c=-0.3,
        freezing_point_c=-0.2,
        optimal_rh_pct_min=95.0,
        optimal_rh_pct_max=100.0,
        respiration_rate_co2_mg_kg_h_0c=12.0,
        q10_temperature_coefficient=2.5,
        ethylene_sensitivity="Very High",
        ethylene_production_rate="Very Low",
        baseline_shelf_life_days_at_optimal=14.0,
    ),
}


class ColdChainSimulationResult(BaseModel):
    crop_name: str
    transit_hours: float
    effective_shelf_life_days_remaining: float
    shelf_life_loss_pct: float
    chilling_injury_risk: bool
    microbial_growth_multiplier: float
    respiration_heat_generated_kj_ton: float
    reefer_cooling_load_kw_ton: float


class ColdChainThermodynamics:
    """
    Simulates dynamic shelf-life loss during reefer truck or maritime container transport.
    """

    @classmethod
    def calculate_respiration_heat_watts(cls, crop: str, temp_c: float, tonnage_metric: float) -> float:
        prof = CROP_COLD_PROFILES.get(crop.lower(), CROP_COLD_PROFILES["apple"])
        # Q10 equation: R(T) = R_0 * Q10^(T / 10)
        r_t = prof.respiration_rate_co2_mg_kg_h_0c * (prof.q10_temperature_coefficient ** (temp_c / 10.0))
        # 1 mg CO2 = ~10.7 Joules of respiration heat energy
        # Watts = (mg CO2 / kg / h) * 1000 kg/ton * 10.7 J / 3600 s
        heat_w_per_ton = (r_t * 1000.0 * 10.7) / 3600.0
        return heat_w_per_ton * tonnage_metric

    @classmethod
    def simulate_transit_quality(
        cls,
        crop: str,
        transit_hours: float,
        mean_reefer_temp_c: float,
        temp_excursion_hours: float = 0.0,
        excursion_temp_c: float = 22.0,
    ) -> ColdChainSimulationResult:
        prof = CROP_COLD_PROFILES.get(crop.lower(), CROP_COLD_PROFILES["apple"])
        opt_temp = (prof.optimal_temp_c_min + prof.optimal_temp_c_max) / 2.0

        # Chilling injury test
        chilling_risk = mean_reefer_temp_c < prof.chilling_injury_threshold_c

        # Base Arrhenius shelf-life loss
        # k_deg(T) = k_ref * Q10^((T - T_opt)/10)
        base_hours = transit_hours - temp_excursion_hours
        q10 = prof.q10_temperature_coefficient

        accel_base = q10 ** ((mean_reefer_temp_c - opt_temp) / 10.0)
        accel_excur = q10 ** ((excursion_temp_c - opt_temp) / 10.0) if temp_excursion_hours > 0 else 1.0

        equiv_optimal_days_used = (
            (base_hours * accel_base) + (temp_excursion_hours * accel_excur)
        ) / 24.0

        remaining_days = max(0.0, prof.baseline_shelf_life_days_at_optimal - equiv_optimal_days_used)
        loss_pct = min(100.0, round((equiv_optimal_days_used / prof.baseline_shelf_life_days_at_optimal) * 100.0, 1))

        # Respiration heat
        resp_w_ton = cls.calculate_respiration_heat_watts(crop, mean_reefer_temp_c, 1.0)
        total_kj_ton = resp_w_ton * (transit_hours * 3600.0) / 1000.0
        reefer_load_kw = (resp_w_ton / 1000.0) * 1.8  # safety factor for container conduction

        # Microbial growth relative multiplier (Ratkowsky square root model)
        t_zero = -5.0  # Tmin microbial growth
        if mean_reefer_temp_c > t_zero:
            microb_mult = ((mean_reefer_temp_c - t_zero) / (opt_temp - t_zero)) ** 2
        else:
            microb_mult = 0.05

        return ColdChainSimulationResult(
            crop_name=crop,
            transit_hours=transit_hours,
            effective_shelf_life_days_remaining=round(remaining_days, 1),
            shelf_life_loss_pct=loss_pct,
            chilling_injury_risk=chilling_risk,
            microbial_growth_multiplier=round(microb_mult, 2),
            respiration_heat_generated_kj_ton=round(total_kj_ton, 1),
            reefer_cooling_load_kw_ton=round(reefer_load_kw, 3),
        )
