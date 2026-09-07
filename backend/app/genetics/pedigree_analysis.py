"""
AgriScan Pedigree Kinship & Inbreeding Matrix Calculation Engine.
Implements Wright's coefficient of relationship and Malecot genealogical kinship.
"""

from typing import Dict, List, Tuple, Set
from pydantic import BaseModel, Field
import numpy as np


class ParentalPairCompatibility(BaseModel):
    female_parent_id: str
    male_parent_id: str
    kinship_coefficient_malecot: float
    inbreeding_coefficient_offspring: float
    predicted_heterosis_pct: float
    mating_recommendation: str


class PedigreeKinshipEngine:
    """
    Computes ancestral co-ancestry and heterosis potential.
    """

    @staticmethod
    def calculate_kinship(known_common_ancestors: int, total_generations_back: int) -> float:
        if known_common_ancestors == 0:
            return 0.0
        # Wright's r = sum((1/2)^(n1 + n2))
        path_length = total_generations_back * 2
        r = known_common_ancestors * ((0.5) ** path_length)
        return float(round(r, 4))

    @classmethod
    def evaluate_mating(cls, female_id: str, male_id: str, common_ancestors: int = 0) -> ParentalPairCompatibility:
        kinship = cls.calculate_kinship(common_ancestors, total_generations_back=3)
        offspring_f = kinship / 2.0
        heterosis = float(max(5.0, 25.0 * (1.0 - kinship)))

        if kinship < 0.0625:
            rec = "Highly Recommended Cross (Maximum Heterosis & Genetic Diversity)"
        elif kinship < 0.125:
            rec = "Acceptable Cross (Standard Hybrid Vigor)"
        else:
            rec = "Caution: High Inbreeding Depression Risk (Avoid Parental Combination)"

        return ParentalPairCompatibility(
            female_parent_id=female_id,
            male_parent_id=male_id,
            kinship_coefficient_malecot=kinship,
            inbreeding_coefficient_offspring=round(offspring_f, 4),
            predicted_heterosis_pct=round(heterosis, 1),
            mating_recommendation=rec,
        )
