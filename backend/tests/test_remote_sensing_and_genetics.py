"""
Integration Test Suite for Remote Sensing and Crop Genetics.
"""

import pytest
from app.remote_sensing.spectral_indices import (
    SpectralIndexProcessor,
    MultispectralReflectanceBands,
)
from app.remote_sensing.timeseries_smoothing import (
    VegetationTimeSeriesSmoother,
    DailyVegetationObservation,
)
from app.remote_sensing.zonal_statistics import ParcelZonalStatsProcessor
from app.genetics.marker_database import (
    GENOMIC_MARKER_REGISTRY,
    get_marker,
    list_all_markers,
)
from app.genetics.pedigree_analysis import PedigreeKinshipEngine


def test_spectral_indices_calculation():
    processor = SpectralIndexProcessor()
    bands = MultispectralReflectanceBands(
        blue=0.035,
        green=0.075,
        red=0.045,
        red_edge_1=0.180,
        nir_broad=0.520,
        swir_1=0.210,
        swir_2=0.090,
    )
    res = processor.evaluate_all(bands)
    assert 0.80 <= res.ndvi <= 0.90
    assert res.ndre is not None and 0.40 <= res.ndre <= 0.60
    assert res.evi > 0.50
    assert "High Canopy Vigor" in res.vigor_classification


def test_timeseries_smoothing_and_phenology():
    obs = [
        DailyVegetationObservation(day_of_year=100 + i * 10, raw_ndvi=0.20 + 0.55 * (-( (i - 7) / 4.0 ) ** 2 + 1.0))
        for i in range(15)
    ]
    pheno = VegetationTimeSeriesSmoother.extract_phenology(obs)
    assert pheno.greenup_day_of_year >= 100
    assert pheno.peak_canopy_day_of_year == 170
    assert pheno.length_of_growing_season_days > 40


def test_parcel_zonal_statistics():
    pixel_values = [0.25, 0.45, 0.65, 0.72, 0.80, 0.82, 0.78, 0.55, 0.35, 0.68]
    metrics = ParcelZonalStatsProcessor.compute_zonal_stats("PARCEL_A", pixel_values)
    assert metrics.total_pixel_count == 10
    assert metrics.mean_ndvi > 0.50
    assert metrics.uniformity_coefficient_pct > 50.0


def test_genomic_marker_registry():
    markers = list_all_markers()
    assert len(markers) >= 100
    sub1 = get_marker("qtl_sub1a")
    assert sub1 is not None
    assert sub1.target_gene == "Sub1A"
    assert sub1.phenotypic_variance_explained_r2_pct > 50.0


def test_pedigree_kinship_evaluation():
    cross = PedigreeKinshipEngine.evaluate_mating("Female_Line_A", "Male_Line_B", common_ancestors=0)
    assert cross.kinship_coefficient_malecot == 0.0
    assert cross.predicted_heterosis_pct >= 20.0
