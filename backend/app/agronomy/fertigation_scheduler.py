"""
AgroPulse Precision Fertigation & Daily Drip Nutrient Injection Engine.
Computes daily crop uptake curves, injection pump flow rates, tank dilution recipes,
and chemical precipitation risk mitigation for automated fertigation rigs.
"""

from typing import Dict, List, Optional, Tuple
from pydantic import BaseModel, Field
import numpy as np


class FertigationCropRequirement(BaseModel):
    crop_name: str
    target_yield_ton_ha: float
    total_n_kg_ha: float
    total_p2o5_kg_ha: float
    total_k2o_kg_ha: float
    crop_cycle_days: int
    vegetative_days: int
    flowering_days: int
    fruiting_days: int
    maturation_days: int


class DailyFertigationDose(BaseModel):
    day_number: int
    growth_phase: str
    n_kg_ha_day: float
    p2o5_kg_ha_day: float
    k2o_kg_ha_day: float
    target_ec_ds_m: float
    target_ph: float
    stock_tank_a_fertilizers: List[str]
    stock_tank_b_fertilizers: List[str]


class PrecisionFertigationScheduler:
    """
    Generates stage-by-stage split fertigation regimens.
    Separates Calcium/Nitrate (Tank A) from Sulfates/Phosphates (Tank B) to prevent gypsum/phosphate clogging.
    """

    def __init__(self, requirement: FertigationCropRequirement):
        self.req = requirement

    def get_phase_partitioning(self) -> Dict[str, Tuple[float, float, float]]:
        """
        Returns fraction of (N, P2O5, K2O) allocated across phenological stages:
        (Vegetative, Flowering, Fruiting/Bulking, Maturation)
        """
        return {
            "Vegetative": (0.35, 0.40, 0.20),
            "Flowering": (0.30, 0.35, 0.30),
            "Fruiting": (0.25, 0.20, 0.40),
            "Maturation": (0.10, 0.05, 0.10),
        }

    def generate_full_schedule(self) -> List[DailyFertigationDose]:
        schedule = []
        parts = self.get_phase_partitioning()

        veg_end = self.req.vegetative_days
        flo_end = veg_end + self.req.flowering_days
        fru_end = flo_end + self.req.fruiting_days
        mat_end = self.req.crop_cycle_days

        for day in range(1, self.req.crop_cycle_days + 1):
            if day <= veg_end:
                phase = "Vegetative"
                duration = max(1, self.req.vegetative_days)
                ec = 1.4
            elif day <= flo_end:
                phase = "Flowering"
                duration = max(1, self.req.flowering_days)
                ec = 1.8
            elif day <= fru_end:
                phase = "Fruiting"
                duration = max(1, self.req.fruiting_days)
                ec = 2.2
            else:
                phase = "Maturation"
                duration = max(1, self.req.maturation_days)
                ec = 1.5

            fn, fp, fk = parts[phase]
            daily_n = round((self.req.total_n_kg_ha * fn) / duration, 3)
            daily_p = round((self.req.total_p2o5_kg_ha * fp) / duration, 3)
            daily_k = round((self.req.total_k2o_kg_ha * fk) / duration, 3)

            # Assign to safe tanks
            tank_a = [f"Calcium Nitrate 15.5-0-0 ({round(daily_n * 0.4, 2)} kg/ha)", "Iron Chelated Fe-EDTA"]
            tank_b = [f"Mono Potassium Phosphate 0-52-34 ({round(daily_p * 0.8, 2)} kg/ha)", f"Potassium Nitrate 13-0-45 ({round(daily_k * 0.6, 2)} kg/ha)"]

            schedule.append(
                DailyFertigationDose(
                    day_number=day,
                    growth_phase=phase,
                    n_kg_ha_day=daily_n,
                    p2o5_kg_ha_day=daily_p,
                    k2o_kg_ha_day=daily_k,
                    target_ec_ds_m=ec,
                    target_ph=6.0,
                    stock_tank_a_fertilizers=tank_a,
                    stock_tank_b_fertilizers=tank_b,
                )
            )

        return schedule
