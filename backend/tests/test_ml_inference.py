import pytest
import numpy as np
from app.ml.pipeline.feature_engineering import RawAgroFeatures, AgroFeatureTransformer
from app.ml.classifiers.random_forest import rf_classifier
from app.ml.classifiers.gradient_boosted import gbdt_classifier
from app.ml.classifiers.neural_mlp import neural_mlp_classifier
from app.ml.pipeline.ensemble import crop_ensemble_engine


@pytest.fixture()
def standard_paddy_soil():
    return RawAgroFeatures(
        n_kg_ha=320.0,
        p_kg_ha=35.0,
        k_kg_ha=200.0,
        ph=6.2,
        organic_carbon_pct=0.75,
        ec_ds_m=0.8,
        temperature_c=28.0,
        humidity_pct=82.0,
        rainfall_mm=1600.0,
        elevation_m=40.0,
    )


def test_feature_engineering_pipeline(standard_paddy_soil):
    """Verify feature engineering produces the expected 26-dimensional feature vector."""
    transformed = AgroFeatureTransformer.transform(standard_paddy_soil)

    assert len(transformed.feature_names) == 26
    assert len(transformed.values) == 26
    assert transformed.summary_dict["total_npk_sum"] == 555.0
    assert transformed.summary_dict["n_p_ratio"] > 0
    assert transformed.summary_dict["moisture_adequacy_index"] > 1.0


def test_random_forest_inference(standard_paddy_soil):
    """Verify Random Forest model inference and top-k ranking."""
    top_crops = rf_classifier.predict_top_k(standard_paddy_soil, top_k=5)

    assert len(top_crops) == 5
    assert top_crops[0].rank == 1
    assert top_crops[0].probability > 0
    assert 0 <= top_crops[0].confidence_pct <= 100


def test_gradient_boosting_inference(standard_paddy_soil):
    """Verify Gradient Boosted Decision Tree inference."""
    top_crops = gbdt_classifier.predict_top_k(standard_paddy_soil, top_k=5)

    assert len(top_crops) == 5
    assert sum(c.probability for c in top_crops) <= 1.0


def test_neural_mlp_inference(standard_paddy_soil):
    """Verify Deep Multi-Layer Perceptron forward pass and probability sum."""
    probs = neural_mlp_classifier.predict_probabilities(standard_paddy_soil)

    assert len(probs) >= 20
    # Softmax probabilities should sum to approximately 1.0
    total_p = sum(probs.values())
    assert pytest.approx(total_p, abs=1e-2) == 1.0


def test_hybrid_ensemble_recommender(standard_paddy_soil):
    """Verify hybrid ensemble combines ML probabilities and EcoCrop suitability."""
    result = crop_ensemble_engine.recommend(standard_paddy_soil, top_k=5)

    assert len(result.recommendations) == 5
    top_rec = result.recommendations[0]

    assert top_rec.rank == 1
    assert 0 <= top_rec.composite_suitability_score <= 100
    assert top_rec.estimated_yield_ton_ha > 0
    assert top_rec.fao_suitability_class is not None
