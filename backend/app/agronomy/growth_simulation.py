"""
AgroPulse Mechanistic Daily Crop Growth & Canopy Dynamics Simulator.
Based on Monteith Radiation Use Efficiency (RUE), Thermal GDD Development,
Leaf Area Index (LAI) Expansion, and Partitioning to Economic Yield.
"""

from typing import List, Dict, Optional
from pydantic import BaseModel, Field
import numpy as np


class DailyWeatherGrowthInput(BaseModel):
    day_of_year: int
    t_min_c: float
    t_max_c: float
    solar_radiation_mj_m2: float
    water_stress_ks: float = 1.0


class CropPhenologyStage(BaseModel):
    stage_name: str
    gdd_required_cumulative: float
    kc_basal: float
    partitioning_leaf_pct: float
    partitioning_stem_pct: float
    partitioning_root_pct: float
    partitioning_grain_pct: float


class DailyGrowthOutput(BaseModel):
    day_of_year: int
    current_stage: str
    cumulative_gdd: float
    leaf_area_index: float
    par_intercepted_mj_m2: float
    biomass_increment_kg_ha: float
    total_biomass_kg_ha: float
    grain_yield_kg_ha: float


class MechanisticCropGrowthSimulator:
    """
    Daily physiological simulator computing light interception, biomass growth,
    and sink-source economic grain partitioning.
    """

    def __init__(
        self,
        base_temp_c: float,
        opt_temp_c: float,
        max_temp_c: float,
        radiation_use_efficiency_g_mj: float = 2.8,
        light_extinction_coefficient_k: float = 0.65,
        max_lai: float = 6.0,
        stages: Optional[List[CropPhenologyStage]] = None,
    ):
        self.t_base = base_temp_c
        self.t_opt = opt_temp_c
        self.t_max = max_temp_c
        self.rue = radiation_use_efficiency_g_mj
        self.k_ext = light_extinction_coefficient_k
        self.max_lai = max_lai

        if stages is None:
            self.stages = [
                CropPhenologyStage(stage_name="Emergence", gdd_required_cumulative=120.0, kc_basal=0.30, partitioning_leaf_pct=0.50, partitioning_stem_pct=0.20, partitioning_root_pct=0.30, partitioning_grain_pct=0.0),
                CropPhenologyStage(stage_name="Vegetative", gdd_required_cumulative=550.0, kc_basal=0.85, partitioning_leaf_pct=0.45, partitioning_stem_pct=0.35, partitioning_root_pct=0.20, partitioning_grain_pct=0.0),
                CropPhenologyStage(stage_name="Flowering", gdd_required_cumulative=900.0, kc_basal=1.15, partitioning_leaf_pct=0.15, partitioning_stem_pct=0.25, partitioning_root_pct=0.10, partitioning_grain_pct=0.50),
                CropPhenologyStage(stage_name="Grain Filling", gdd_required_cumulative=1450.0, kc_basal=1.00, partitioning_leaf_pct=0.0, partitioning_stem_pct=0.05, partitioning_root_pct=0.05, partitioning_grain_pct=0.90),
                CropPhenologyStage(stage_name="Maturity", gdd_required_cumulative=1800.0, kc_basal=0.50, partitioning_leaf_pct=0.0, partitioning_stem_pct=0.0, partitioning_root_pct=0.0, partitioning_grain_pct=1.00),
            ]
        else:
            self.stages = stages

        self.cumulative_gdd = 0.0
        self.lai = 0.1
        self.leaf_biomass = 50.0
        self.stem_biomass = 20.0
        self.root_biomass = 30.0
        self.grain_biomass = 0.0

    def calculate_daily_gdd(self, tmin: float, tmax: float) -> float:
        """
        Calculates daily thermal degree days with upper threshold truncation.
        """
        tmean = (max(self.t_base, tmin) + min(self.t_max, tmax)) / 2.0
        gdd = max(0.0, tmean - self.t_base)
        return float(gdd)

    def calculate_temp_factor(self, tmean: float) -> float:
        """
        Cardano bell-curve temperature response factor (0 to 1).
        """
        if tmean <= self.t_base or tmean >= self.t_max:
            return 0.0
        elif tmean <= self.t_opt:
            return (tmean - self.t_base) / max(0.1, self.t_opt - self.t_base)
        else:
            return (self.t_max - tmean) / max(0.1, self.t_max - self.t_opt)

    def determine_current_stage(self) -> CropPhenologyStage:
        for stage in self.stages:
            if self.cumulative_gdd <= stage.gdd_required_cumulative:
                return stage
        return self.stages[-1]

    def step(self, weather: DailyWeatherGrowthInput) -> DailyGrowthOutput:
        """
        Advances crop growth state by one calendar day.
        """
        gdd = self.calculate_daily_gdd(weather.t_min_c, weather.t_max_c)
        self.cumulative_gdd += gdd

        stage = self.determine_current_stage()

        par_incident = 0.50 * weather.solar_radiation_mj_m2
        fraction_intercepted = 1.0 - np.exp(-self.k_ext * self.lai)
        par_intercepted = par_incident * fraction_intercepted

        tmean = (weather.t_min_c + weather.t_max_c) / 2.0
        temp_factor = self.calculate_temp_factor(tmean)

        biomass_increment = par_intercepted * self.rue * 10.0 * temp_factor * weather.water_stress_ks
        biomass_increment = max(0.0, float(biomass_increment))

        d_leaf = biomass_increment * stage.partitioning_leaf_pct
        d_stem = biomass_increment * stage.partitioning_stem_pct
        d_root = biomass_increment * stage.partitioning_root_pct
        d_grain = biomass_increment * stage.partitioning_grain_pct

        self.leaf_biomass += d_leaf
        self.stem_biomass += d_stem
        self.root_biomass += d_root
        self.grain_biomass += d_grain

        specific_leaf_area = 22.0 / 10000.0
        if stage.stage_name in ["Emergence", "Vegetative"]:
            self.lai = min(self.max_lai, self.lai + d_leaf * specific_leaf_area * 10.0)
        elif stage.stage_name in ["Grain Filling", "Maturity"]:
            self.lai = max(0.2, self.lai - 0.025 * gdd)

        total_biomass = self.leaf_biomass + self.stem_biomass + self.root_biomass + self.grain_biomass

        return DailyGrowthOutput(
            day_of_year=weather.day_of_year,
            current_stage=stage.stage_name,
            cumulative_gdd=round(self.cumulative_gdd, 1),
            leaf_area_index=round(self.lai, 2),
            par_intercepted_mj_m2=round(par_intercepted, 2),
            biomass_increment_kg_ha=round(biomass_increment, 1),
            total_biomass_kg_ha=round(total_biomass, 1),
            grain_yield_kg_ha=round(self.grain_biomass, 1),
        )
