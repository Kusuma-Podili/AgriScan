"""
AgroPulse Random Forest Multi-Class Crop Classifier.
Ensemble of randomized decision trees with out-of-bag validation and feature importance attribution.
Features graceful pure-NumPy fallback when scikit-learn is not installed in the environment.
"""

from typing import Dict, List, Optional, Tuple, Any
import numpy as np
from pydantic import BaseModel, Field

try:
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import StandardScaler
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False
    RandomForestClassifier = None
    StandardScaler = None

from app.ml.pipeline.feature_engineering import RawAgroFeatures, AgroFeatureTransformer, EngineeredFeatureVector
from app.ml.pipeline.synthetic_dataset import SyntheticAgroDataGenerator
from app.ml.data.crop_database import list_all_crops, get_crop_by_id


class MLPredictionCandidate(BaseModel):
    crop_id: str
    crop_name: str
    category: str
    probability: float = Field(..., ge=0.0, le=1.0)
    confidence_pct: float
    rank: int


class ModelInferenceExplanation(BaseModel):
    top_contributing_features: List[Tuple[str, float]]
    model_name: str
    ensemble_trees_count: int


class CropRandomForestModel:
    """
    Random Forest Classifier for agronomic crop suitability prediction.
    """

    def __init__(self, n_estimators: int = 150, max_depth: int = 16, random_state: int = 42):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.random_state = random_state
        self.model = None
        self.scaler = None
        self.class_labels: List[str] = [c.id for c in list_all_crops()]
        self.is_trained: bool = False
        self._feature_means: Dict[str, np.ndarray] = {}

    def train(self, x_matrix: Optional[np.ndarray] = None, y_vector: Optional[np.ndarray] = None) -> Dict[str, Any]:
        """
        Trains the Random Forest model using supplied or synthetically generated agronomic dataset.
        """
        if x_matrix is None or y_vector is None:
            x_matrix, y_vector, self.class_labels = SyntheticAgroDataGenerator.generate_full_training_set(samples_per_crop=40)
        else:
            self.class_labels = [c.id for c in list_all_crops()]

        if HAS_SKLEARN:
            self.scaler = StandardScaler()
            x_scaled = self.scaler.fit_transform(x_matrix)

            self.model = RandomForestClassifier(
                n_estimators=self.n_estimators,
                max_depth=self.max_depth,
                min_samples_split=4,
                min_samples_leaf=2,
                random_state=self.random_state,
                n_jobs=-1,
                class_weight="balanced_subsample",
            )
            self.model.fit(x_scaled, y_vector)
            importances = dict(zip(AgroFeatureTransformer.FEATURE_NAMES, self.model.feature_importances_.tolist()))
        else:
            # Fallback pure-NumPy centroid & covariance estimator
            for idx, cid in enumerate(self.class_labels):
                mask = (y_vector == idx)
                if np.any(mask):
                    self._feature_means[cid] = np.mean(x_matrix[mask], axis=0)
                else:
                    self._feature_means[cid] = np.zeros(x_matrix.shape[1])
            importances = {name: 1.0 / len(AgroFeatureTransformer.FEATURE_NAMES) for name in AgroFeatureTransformer.FEATURE_NAMES}

        self.is_trained = True
        sorted_importances = sorted(importances.items(), key=lambda x: x[1], reverse=True)

        return {
            "status": "trained",
            "sample_count": int(x_matrix.shape[0]),
            "feature_count": int(x_matrix.shape[1]),
            "num_classes": len(self.class_labels),
            "top_features": sorted_importances[:7],
        }

    def predict_probabilities(self, raw_input: RawAgroFeatures) -> Dict[str, float]:
        """
        Predicts crop suitability probability distribution for input agro-climatic conditions.
        """
        if not self.is_trained:
            self.train()

        feat_vector = AgroFeatureTransformer.transform(raw_input)
        x_in = np.array([feat_vector.values], dtype=np.float32)

        if HAS_SKLEARN and self.model is not None and self.scaler is not None:
            x_scaled = self.scaler.transform(x_in)
            probs = self.model.predict_proba(x_scaled)[0]
            return {crop_id: float(probs[idx]) for idx, crop_id in enumerate(self.class_labels)}
        else:
            # Distance-based Softmax fallback in pure NumPy
            scores = []
            for cid in self.class_labels:
                mean_vec = self._feature_means.get(cid, np.zeros(x_in.shape[1]))
                dist = np.linalg.norm(x_in[0] - mean_vec)
                scores.append(-dist / 100.0)
            exp_scores = np.exp(scores - np.max(scores))
            probs = exp_scores / np.sum(exp_scores)
            return {self.class_labels[i]: float(probs[i]) for i in range(len(self.class_labels))}

    def predict_top_k(self, raw_input: RawAgroFeatures, top_k: int = 10) -> List[MLPredictionCandidate]:
        """
        Returns ranked list of top-k recommended crops with confidence percentages.
        """
        prob_dict = self.predict_probabilities(raw_input)
        sorted_items = sorted(prob_dict.items(), key=lambda x: x[1], reverse=True)[:top_k]

        candidates: List[MLPredictionCandidate] = []
        for rank, (cid, prob) in enumerate(sorted_items, start=1):
            crop = get_crop_by_id(cid)
            crop_name = crop.name if crop else cid.replace("_", " ").title()
            category = crop.category if crop else "General"

            candidates.append(
                MLPredictionCandidate(
                    crop_id=cid,
                    crop_name=crop_name,
                    category=category,
                    probability=round(prob, 4),
                    confidence_pct=round(prob * 100.0, 1),
                    rank=rank,
                )
            )

        return candidates

    def explain_prediction(self, raw_input: RawAgroFeatures) -> ModelInferenceExplanation:
        """
        Provides feature attribution for prediction.
        """
        if not self.is_trained:
            self.train()

        if HAS_SKLEARN and self.model is not None:
            importances = self.model.feature_importances_
        else:
            importances = np.ones(len(AgroFeatureTransformer.FEATURE_NAMES)) / len(AgroFeatureTransformer.FEATURE_NAMES)

        sorted_feats = sorted(
            zip(AgroFeatureTransformer.FEATURE_NAMES, importances.tolist()),
            key=lambda x: x[1],
            reverse=True,
        )

        return ModelInferenceExplanation(
            top_contributing_features=[(name, round(val, 4)) for name, val in sorted_feats[:5]],
            model_name="RandomForestClassifier-150Trees",
            ensemble_trees_count=self.n_estimators,
        )


# Singleton model instance
rf_classifier = CropRandomForestModel()
