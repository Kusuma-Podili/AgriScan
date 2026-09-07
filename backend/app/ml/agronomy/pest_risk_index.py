"""
AgroPulse Microclimatic Pest and Disease Risk Forecasting Engine.
Calculates continuous pathogen infection risk indices based on ambient temperature,
relative humidity, leaf wetness duration, and rainfall splashing dynamics.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from app.ml.data.pest_disease_db import PEST_DISEASE_DATABASE, PestDiseaseProfile, get_risks_for_crop


class CurrentMicroclimate(BaseModel):
    temperature_c: float
    humidity_pct: float
    rainfall_mm: float
    consecutive_rainy_days: int = 0
    estimated_leaf_wetness_hours: float = 6.0


class IndividualThreatRisk(BaseModel):
    pest_disease_id: str
    name: str
    organism_type: str
    risk_score_pct: float = Field(..., ge=0.0, le=100.0)
    risk_category: str  # Low, Moderate, High, Critical / Outbreak Imminent
    favorable_factors: List[str]
    active_symptoms: str
    recommended_ipm_measures: List[str]
    chemical_actives: List[str]


class CropPestRiskReport(BaseModel):
    crop_id: str
    composite_pest_risk_index: float
    overall_alert_level: str  # Normal, Watch, Warning, Emergency
    threats: List[IndividualThreatRisk]


class PestRiskForecaster:
    """
    Computes disease risk based on epidemiological growth curves and weather suitability.
    """

    @classmethod
    def evaluate_threat(
        cls,
        threat: PestDiseaseProfile,
        weather: CurrentMicroclimate,
    ) -> IndividualThreatRisk:
        """
        Evaluates weather suitability for an individual pathogen or insect pest.
        """
        favorable_factors: List[str] = []

        # 1. Temperature Suitability (0 to 40 points)
        temp_score = 0.0
        if threat.temp_opt_min_c <= weather.temperature_c <= threat.temp_opt_max_c:
            temp_score = 40.0
            favorable_factors.append(f"Temperature ({weather.temperature_c}°C) is in peak optimal proliferation range [{threat.temp_opt_min_c}-{threat.temp_opt_max_c}°C]")
        elif threat.temp_min_c <= weather.temperature_c <= threat.temp_max_c:
            temp_score = 22.0
            favorable_factors.append(f"Temperature ({weather.temperature_c}°C) permits viable pathogen activity")
        else:
            temp_score = 0.0

        # 2. Humidity Suitability (0 to 35 points)
        humidity_score = 0.0
        if weather.humidity_pct >= threat.humidity_min_pct:
            excess = weather.humidity_pct - threat.humidity_min_pct
            humidity_score = min(35.0, 20.0 + excess * 1.0)
            favorable_factors.append(f"Relative humidity ({weather.humidity_pct}%) satisfies required moisture threshold (>={threat.humidity_min_pct}%)")
        else:
            # Below threshold
            humidity_score = max(0.0, 20.0 - (threat.humidity_min_pct - weather.humidity_pct) * 1.5)

        # 3. Leaf Wetness / Precipitation Suitability (0 to 25 points)
        wetness_score = 0.0
        if threat.leaf_wetness_hours_threshold > 0:
            if weather.estimated_leaf_wetness_hours >= threat.leaf_wetness_hours_threshold:
                wetness_score += 15.0
                favorable_factors.append(f"Dew/leaf wetness ({weather.estimated_leaf_wetness_hours}h) enables fungal spore germination (>={threat.leaf_wetness_hours_threshold}h)")

        if threat.rainfall_correlation == "Positive" and weather.rainfall_mm > 2.0:
            wetness_score += 10.0
            favorable_factors.append(f"Precipitation ({weather.rainfall_mm}mm) facilitates spore splash dispersal")
        elif threat.rainfall_correlation == "Negative" and weather.rainfall_mm == 0.0:
            wetness_score += 10.0
            favorable_factors.append("Dry spell accelerates insect vector population multiplication")
        elif threat.rainfall_correlation == "Neutral":
            wetness_score += 8.0

        total_score = min(100.0, temp_score + humidity_score + wetness_score)
        total_score = round(total_score, 1)

        # Category
        if total_score >= 75.0:
            category = "Critical (Outbreak Alert)"
        elif total_score >= 50.0:
            category = "High Risk (Preventative Spray Required)"
        elif total_score >= 30.0:
            category = "Moderate (Field Scouting Recommended)"
        else:
            category = "Low Risk (Favorable Conditions)"

        ipm = threat.cultural_controls[:2] + threat.biological_controls[:1]

        return IndividualThreatRisk(
            pest_disease_id=threat.id,
            name=threat.name,
            organism_type=threat.organism_type,
            risk_score_pct=total_score,
            risk_category=category,
            favorable_factors=favorable_factors,
            active_symptoms=f"{threat.symptoms_vegetative} | {threat.symptoms_reproductive}",
            recommended_ipm_measures=ipm,
            chemical_actives=threat.chemical_active_ingredients,
        )

    @classmethod
    def evaluate_crop_risks(
        cls,
        crop_id: str,
        weather: CurrentMicroclimate,
    ) -> CropPestRiskReport:
        """
        Evaluates all potential pest and disease threats for the specified crop.
        """
        threats = get_risks_for_crop(crop_id)
        threat_evals = [cls.evaluate_threat(t, weather) for t in threats]
        threat_evals.sort(key=lambda x: x.risk_score_pct, reverse=True)

        if threat_evals:
            max_risk = max(t.risk_score_pct for t in threat_evals)
            avg_risk = sum(t.risk_score_pct for t in threat_evals) / len(threat_evals)
            composite_index = round((max_risk * 0.7) + (avg_risk * 0.3), 1)
        else:
            composite_index = 10.0

        if composite_index >= 75.0:
            alert = "Emergency (Active Outbreak Threat)"
        elif composite_index >= 50.0:
            alert = "Warning (High Inoculum Pressure)"
        elif composite_index >= 30.0:
            alert = "Watch (Moderate Activity)"
        else:
            alert = "Normal (Low Pathogen Pressure)"

        return CropPestRiskReport(
            crop_id=crop_id,
            composite_pest_risk_index=composite_index,
            overall_alert_level=alert,
            threats=threat_evals,
        )
