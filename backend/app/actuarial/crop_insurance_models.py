"""
AgriScan Agricultural Actuarial Models & Parametric Insurance Engine.
Implements Area-Yield Index Insurance (AYII), Weather-Index Insurance (WII),
Burning Cost pure premium rate modeling, and Parametric Drought Trigger curves.
"""

import math
from typing import Dict, List, Optional, Tuple
from pydantic import BaseModel, Field
import numpy as np


class AreaYieldPolicyConfig(BaseModel):
    policy_id: str
    crop_name: str
    historical_county_yields: List[float]
    coverage_level_pct: float = 85.0  # 70%, 75%, 80%, 85%, 90%
    projected_price_usd_per_ton: float = 240.0
    insured_hectares: float = 100.0
    loss_adjustment_expense_pct: float = 8.0


class WeatherIndexTrigger(BaseModel):
    peril_name: str  # "Deficit Rainfall (Drought)", "Excess Rainfall", "Late Frost"
    trigger_threshold_value: float
    exit_threshold_value: float  # Value where 100% max payout occurs
    max_sum_insured_usd_per_ha: float
    unit_of_measure: str


class InsurancePremiumQuote(BaseModel):
    policy_id: str
    guaranteed_yield_ton_ha: float
    pure_risk_premium_rate_pct: float
    pure_premium_usd_ha: float
    gross_premium_usd_ha: float
    total_premium_payable_usd: float
    max_liability_usd: float


class ActuarialLossDistribution(BaseModel):
    mean_yield_ton_ha: float
    yield_standard_deviation: float
    coefficient_of_variation_pct: float
    skewness: float
    prob_loss_occurrence_pct: float
    expected_loss_cost_ratio_pct: float
    var_95_loss_cost_pct: float
    tvar_95_tail_value_at_risk_pct: float


class AgriculturalActuarialEngine:
    """
    Calculates actuarial loss costs, burning cost premiums, and index insurance payouts.
    """

    @classmethod
    def calculate_yield_distribution(cls, yields: List[float]) -> ActuarialLossDistribution:
        arr = np.array(yields, dtype=float)
        n = len(arr)
        mean = float(np.mean(arr))
        std = float(np.std(arr, ddof=1)) if n > 1 else 0.1
        cv = (std / mean) * 100.0 if mean > 0 else 0.0

        # Skewness
        if n > 2 and std > 0:
            skew = float(np.sum((arr - mean) ** 3) / ((n - 1) * (std ** 3)))
        else:
            skew = 0.0

        # Burning cost loss-cost ratio over historical series (against 85% coverage)
        guar = mean * 0.85
        losses = np.maximum(0.0, guar - arr)
        loss_costs = (losses / guar) * 100.0
        exp_loss_cost = float(np.mean(loss_costs))
        prob_loss = float(np.sum(losses > 0) / n) * 100.0

        # VaR and TVaR (Tail Value at Risk at 95th percentile)
        sorted_lc = np.sort(loss_costs)
        idx_95 = int(math.ceil(0.95 * n)) - 1
        idx_95 = min(max(0, idx_95), n - 1)
        var_95 = float(sorted_lc[idx_95])
        tail = sorted_lc[idx_95:]
        tvar_95 = float(np.mean(tail)) if len(tail) > 0 else var_95

        return ActuarialLossDistribution(
            mean_yield_ton_ha=round(mean, 2),
            yield_standard_deviation=round(std, 2),
            coefficient_of_variation_pct=round(cv, 1),
            skewness=round(skew, 3),
            prob_loss_occurrence_pct=round(prob_loss, 1),
            expected_loss_cost_ratio_pct=round(exp_loss_cost, 2),
            var_95_loss_cost_pct=round(var_95, 2),
            tvar_95_tail_value_at_risk_pct=round(tvar_95, 2),
        )

    @classmethod
    def quote_area_yield_insurance(cls, config: AreaYieldPolicyConfig) -> InsurancePremiumQuote:
        dist = cls.calculate_yield_distribution(config.historical_county_yields)
        guar_yield = dist.mean_yield_ton_ha * (config.coverage_level_pct / 100.0)
        max_liab = guar_yield * config.projected_price_usd_per_ton * config.insured_hectares

        # Pure risk rate = Expected Loss Cost + Risk Load (20% of standard deviation of loss cost)
        pure_rate = max(1.5, dist.expected_loss_cost_ratio_pct * 1.15)
        pure_prem_ha = (pure_rate / 100.0) * (guar_yield * config.projected_price_usd_per_ton)

        # Gross rate includes Loss Adjustment Expense (LAE) & catastrophe capital charge
        expense_load = config.loss_adjustment_expense_pct / 100.0
        gross_prem_ha = pure_prem_ha / (1.0 - expense_load)
        total_prem = gross_prem_ha * config.insured_hectares

        return InsurancePremiumQuote(
            policy_id=config.policy_id,
            guaranteed_yield_ton_ha=round(guar_yield, 2),
            pure_risk_premium_rate_pct=round(pure_rate, 2),
            pure_premium_usd_ha=round(pure_prem_ha, 2),
            gross_premium_usd_ha=round(gross_prem_ha, 2),
            total_premium_payable_usd=round(total_prem, 2),
            max_liability_usd=round(max_liab, 2),
        )

    @classmethod
    def evaluate_weather_index_payout(
        cls,
        trigger: WeatherIndexTrigger,
        realized_index_value: float,
        insured_hectares: float,
    ) -> Tuple[float, float]:
        """
        Returns (payout_usd_per_ha, total_claim_usd).
        Linear parametric indemnity payoff between trigger and exit values.
        """
        t = trigger.trigger_threshold_value
        e = trigger.exit_threshold_value

        # Drought trigger (deficit condition: realized < trigger)
        if t > e:  # Lower value = worse condition (e.g. cumulative mm rainfall)
            if realized_index_value >= t:
                rate = 0.0
            elif realized_index_value <= e:
                rate = 1.0
            else:
                rate = (t - realized_index_value) / (t - e)
        else:  # Higher value = worse condition (e.g. consecutive frost days or high heat)
            if realized_index_value <= t:
                rate = 0.0
            elif realized_index_value >= e:
                rate = 1.0
            else:
                rate = (realized_index_value - t) / (e - t)

        rate = min(1.0, max(0.0, rate))
        payout_ha = rate * trigger.max_sum_insured_usd_per_ha
        total_claim = payout_ha * insured_hectares
        return (round(payout_ha, 2), round(total_claim, 2))
