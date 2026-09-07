"""
Micronutrient Diagnostics & Soil Availability Assessment Module.

Provides critical concentration boundaries (DTPA-extractable) for zinc (Zn),
iron (Fe), manganese (Mn), copper (Cu), and boron (hot water extractable),
along with soil and foliar correction advisories.
"""

from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class MicronutrientThreshold:
    element: str
    symbol: str
    unit: str
    critical_deficient: float
    adequate_low: float
    adequate_high: float
    toxic_threshold: Optional[float]
    deficiency_symptom: str
    corrective_product: str
    recommended_dose_kg_ha: float


MICRONUTRIENT_THRESHOLDS: Dict[str, MicronutrientThreshold] = {
    "zinc": MicronutrientThreshold(
        element="Zinc",
        symbol="Zn",
        unit="mg/kg (ppm)",
        critical_deficient=0.6,
        adequate_low=1.0,
        adequate_high=3.0,
        toxic_threshold=20.0,
        deficiency_symptom="Interveinal chlorosis in upper leaves, little leaf syndrome, stunted growth.",
        corrective_product="Zinc Sulphate Heptahydrate (ZnSO4·7H2O 21% Zn)",
        recommended_dose_kg_ha=25.0,
    ),
    "iron": MicronutrientThreshold(
        element="Iron",
        symbol="Fe",
        unit="mg/kg (ppm)",
        critical_deficient=4.5,
        adequate_low=6.5,
        adequate_high=20.0,
        toxic_threshold=150.0,
        deficiency_symptom="Severe yellowing/bleaching of youngest leaves while veins remain green.",
        corrective_product="Ferrous Sulphate (FeSO4·7H2O 19% Fe) / Fe-EDDHA (6% Fe)",
        recommended_dose_kg_ha=30.0,
    ),
    "manganese": MicronutrientThreshold(
        element="Manganese",
        symbol="Mn",
        unit="mg/kg (ppm)",
        critical_deficient=2.0,
        adequate_low=3.5,
        adequate_high=15.0,
        toxic_threshold=80.0,
        deficiency_symptom="Grey speck in oats, marsh spot in peas, checkered interveinal chlorosis.",
        corrective_product="Manganese Sulphate (MnSO4·H2O 30.5% Mn)",
        recommended_dose_kg_ha=15.0,
    ),
    "copper": MicronutrientThreshold(
        element="Copper",
        symbol="Cu",
        unit="mg/kg (ppm)",
        critical_deficient=0.2,
        adequate_low=0.4,
        adequate_high=2.5,
        toxic_threshold=15.0,
        deficiency_symptom="Dieback of terminal twigs, withered leaf tips, exanthema in fruit trees.",
        corrective_product="Copper Sulphate (CuSO4·5H2O 24% Cu)",
        recommended_dose_kg_ha=5.0,
    ),
    "boron": MicronutrientThreshold(
        element="Boron",
        symbol="B",
        unit="mg/kg (ppm)",
        critical_deficient=0.5,
        adequate_low=0.7,
        adequate_high=2.0,
        toxic_threshold=5.0,
        deficiency_symptom="Hollow heart in cauliflower, poor fruit setting, brittle terminal buds.",
        corrective_product="Borax (Na2B4O7·10H2O 10.5% B) / Solubor (20.5% B)",
        recommended_dose_kg_ha=10.0,
    ),
}


def evaluate_micronutrient_status(
    zn_ppm: float,
    fe_ppm: float,
    mn_ppm: float,
    cu_ppm: float,
    b_ppm: float,
    soil_ph: float = 7.0,
) -> Dict[str, Any]:
    """
    Evaluates soil micronutrient levels against DTPA critical thresholds
    and adjusts advisory based on soil reaction pH.
    """
    inputs = {
        "zinc": zn_ppm,
        "iron": fe_ppm,
        "manganese": mn_ppm,
        "copper": cu_ppm,
        "boron": b_ppm,
    }

    results = {}
    deficient_count = 0
    advisories = []

    for key, val in inputs.items():
        thresh = MICRONUTRIENT_THRESHOLDS[key]
        if val < thresh.critical_deficient:
            status = "Deficient"
            deficient_count += 1
            rate = thresh.recommended_dose_kg_ha
            if soil_ph > 7.8 and key in ["zinc", "iron", "manganese"]:
                rate *= 1.25
                advisories.append(
                    f"{thresh.element}: Highly deficient ({val:.2f} ppm). High pH ({soil_ph:.1f}) reduces bioavailability; consider foliar spray (0.5% chelated) or soil application of {rate:.1f} kg/ha {thresh.corrective_product}."
                )
            else:
                advisories.append(
                    f"{thresh.element}: Deficient ({val:.2f} ppm). Apply {rate:.1f} kg/ha {thresh.corrective_product} to soil before sowing."
                )
        elif val < thresh.adequate_low:
            status = "Marginal"
            advisories.append(
                f"{thresh.element}: Marginal ({val:.2f} ppm). Monitor foliage during vegetative peak."
            )
        elif thresh.toxic_threshold and val > thresh.toxic_threshold:
            status = "Toxic"
            advisories.append(
                f"{thresh.element}: High/Toxicity Risk ({val:.2f} ppm). Avoid products containing {thresh.element}; ensure proper drainage and organic matter addition."
            )
        else:
            status = "Adequate"

        results[key] = {
            "element": thresh.element,
            "measured_ppm": val,
            "unit": thresh.unit,
            "status": status,
            "critical_threshold": thresh.critical_deficient,
            "adequate_range": f"{thresh.adequate_low} - {thresh.adequate_high}",
        }

    return {
        "overall_micronutrient_health": "Optimal" if deficient_count == 0 else f"{deficient_count} Elements Deficient",
        "soil_ph": soil_ph,
        "elements": results,
        "advisory_notes": advisories,
    }
