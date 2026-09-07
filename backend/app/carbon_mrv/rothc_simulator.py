"""
AgriScan RothC-26.3 Soil Organic Carbon (SOC) Turnover Model.
Simulates 5 carbon pools:
- DPM: Decomposable Plant Material (k = 10.0 yr-1)
- RPM: Resistant Plant Material (k = 0.3 yr-1)
- BIO: Microbial Biomass (k = 0.66 yr-1)
- HUM: Humified Organic Matter (k = 0.02 yr-1)
- IOM: Inert Organic Matter (stable inert radiocarbon pool)
"""

from typing import Dict, List, Tuple, Optional
from pydantic import BaseModel, Field
import numpy as np


class RothCPoolStocks(BaseModel):
    dpm_t_ha: float = 1.2
    rpm_t_ha: float = 8.5
    bio_t_ha: float = 1.8
    hum_t_ha: float = 38.0
    iom_t_ha: float = 2.5


class MonthlyRothCResult(BaseModel):
    month: int
    total_soc_ton_ha: float
    dpm_ton_ha: float
    rpm_ton_ha: float
    bio_ton_ha: float
    hum_ton_ha: float
    co2_released_t_ha: float
    soil_carbon_sequestration_rate_t_ha_yr: float


class RothC26_3SoilCarbonModel:
    """
    Simulates multi-annual soil organic carbon turnover according to RothC-26.3.
    """

    def __init__(self, clay_pct: float = 25.0, initial_stocks: Optional[RothCPoolStocks] = None):
        self.clay = clay_pct
        if initial_stocks is None:
            self.stocks = RothCPoolStocks()
        else:
            self.stocks = initial_stocks

        # Decomposition rate constants per year
        self.k_dpm = 10.0
        self.k_rpm = 0.30
        self.k_bio = 0.66
        self.k_hum = 0.02

        # Partitioning coefficient based on clay content:
        # x = 1.67 * (1.85 + 1.60 * exp(-0.0786 * clay))
        self.x_ratio = 1.67 * (1.85 + 1.60 * np.exp(-0.0786 * self.clay))

    def calculate_temp_factor(self, t_mean_c: float) -> float:
        """
        fT = 47.9 / (1 + exp(106 / (T + 18.3)))
        """
        if t_mean_c < -15.0:
            return 0.0
        return float(47.9 / (1.0 + np.exp(106.0 / (t_mean_c + 18.3))))

    def step_month(
        self, month: int, t_mean_c: float, precip_mm: float, pet_mm: float, monthly_c_input_t_ha: float = 0.25, is_vegetated: bool = True
    ) -> MonthlyRothCResult:
        ft = self.calculate_temp_factor(t_mean_c)
        fw = float(np.clip(precip_mm / max(1.0, pet_mm), 0.2, 1.0))
        fc = 0.6 if is_vegetated else 1.0
        mod = ft * fw * fc

        # Agricultural residue DPM/RPM ratio is typically 1.44 (59% DPM, 41% RPM)
        dpm_in = monthly_c_input_t_ha * 0.59
        rpm_in = monthly_c_input_t_ha * 0.41

        # Decomposing amounts this month (rate / 12)
        dt = 1.0 / 12.0
        decomp_dpm = self.stocks.dpm_t_ha * (1.0 - np.exp(-self.k_dpm * mod * dt))
        decomp_rpm = self.stocks.rpm_t_ha * (1.0 - np.exp(-self.k_rpm * mod * dt))
        decomp_bio = self.stocks.bio_t_ha * (1.0 - np.exp(-self.k_bio * mod * dt))
        decomp_hum = self.stocks.hum_t_ha * (1.0 - np.exp(-self.k_hum * mod * dt))

        total_decomp = decomp_dpm + decomp_rpm + decomp_bio + decomp_hum

        # Fraction of decomposing C released as CO2 vs synthesized into BIO + HUM
        # CO2 fraction = x / (x + 1)
        co2_frac = self.x_ratio / (self.x_ratio + 1.0)
        co2_released = total_decomp * co2_frac
        c_synthesized = total_decomp * (1.0 - co2_frac)

        # 46% of synthesized C becomes Microbial Biomass (BIO), 54% becomes Humus (HUM)
        new_bio = c_synthesized * 0.46
        new_hum = c_synthesized * 0.54

        self.stocks.dpm_t_ha = self.stocks.dpm_t_ha - decomp_dpm + dpm_in
        self.stocks.rpm_t_ha = self.stocks.rpm_t_ha - decomp_rpm + rpm_in
        self.stocks.bio_t_ha = self.stocks.bio_t_ha - decomp_bio + new_bio
        self.stocks.hum_t_ha = self.stocks.hum_t_ha - decomp_hum + new_hum

        total_soc = self.stocks.dpm_t_ha + self.stocks.rpm_t_ha + self.stocks.bio_t_ha + self.stocks.hum_t_ha + self.stocks.iom_t_ha
        seq_rate = (monthly_c_input_t_ha - co2_released) * 12.0

        return MonthlyRothCResult(
            month=month,
            total_soc_ton_ha=round(total_soc, 2),
            dpm_ton_ha=round(self.stocks.dpm_t_ha, 2),
            rpm_ton_ha=round(self.stocks.rpm_t_ha, 2),
            bio_ton_ha=round(self.stocks.bio_t_ha, 2),
            hum_ton_ha=round(self.stocks.hum_t_ha, 2),
            co2_released_t_ha=round(co2_released, 3),
            soil_carbon_sequestration_rate_t_ha_yr=round(seq_rate, 2),
        )
