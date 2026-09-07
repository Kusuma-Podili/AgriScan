"""
AgroPulse Gradient Boosted Decision Tree (GBDT) Crop Classifier.
Implements multi-class stage-wise additive gradient boosting with shrinkage and tree regularization.
Includes graceful pure-NumPy fallback when scikit-learn is not installed.
"""

from typing import Dict, List, Optional, Tuple, Any
import numpy as np
from pydantic import BaseModel, Field

try:
    from sklearn.ensemble import HistGradientBoostingClassifier
    from sklearn.preprocessing import StandardScaler
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False
    HistGradientBoostingClassifier = None
    StandardScaler = None

from app.ml.pipeline.feature_engineering import RawAgroFeatures, AgroFeatureTransformer
from app.ml.pipeline.synthetic_dataset import SyntheticAgroDataGenerator
from app.ml.data.crop_database import list_all_crops, get_crop_by_id
from app.ml.classifiers.random_forest import MLPredictionCandidate


class CropGradientBoostingModel:
    """
    Gradient Boosted Trees Classifier for agro-ecological pattern discovery.
    """

    def __init__(self, max_iter: int = 100, learning_rate: float = 0.08, max_depth: int = 8, random_state: int = 42):
        self.max_iter = max_iter
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.random_state = random_state
        self.model = None
        self.scaler = None
        self.class_labels: List[str] = [c.id for c in list_all_crops()]
        self.is_trained: bool = False
        self._feature_means: Dict[str, np.ndarray] = {}

    def train(self, x_matrix: Optional[np.ndarray] = None, y_vector: Optional[np.ndarray] = None) -> Dict[str, Any]:
        """
        Trains HistGradientBoosting model.
        """
        if x_matrix is None or y_vector is None:
            x_matrix, y_vector, self.class_labels = SyntheticAgroDataGenerator.generate_full_training_set(samples_per_crop=40)
        else:
            self.class_labels = [c.id for c in list_all_crops()]

        if HAS_SKLEARN:
            self.scaler = StandardScaler()
            x_scaled = self.scaler.fit_transform(x_matrix)

            self.model = HistGradientBoostingClassifier(
                max_iter=self.max_iter,
                learning_rate=self.learning_rate,
                max_depth=self.max_depth,
                min_samples_leaf=3,
                l2_regularization=0.1,
                random_state=self.random_state,
            )
            self.model.fit(x_scaled, y_vector)
        else:
            for idx, cid in enumerate(self.class_labels):
                mask = (y_vector == idx)
                if np.any(mask):
                    self._feature_means[cid] = np.mean(x_matrix[mask], axis=0)
                else:
                    self._feature_means[cid] = np.zeros(x_matrix.shape[1])

        self.is_trained = True

        return {
            "status": "trained",
            "model_type": "HistGradientBoostingClassifier" if HAS_SKLEARN else "NumPyFallbackCentroidModel",
            "iterations": self.max_iter,
            "sample_count": int(x_matrix.shape[0]),
            "num_classes": len(self.class_labels),
        }

    def predict_probabilities(self, raw_input: RawAgroFeatures) -> Dict[str, float]:
        """
        Predicts suitability probability distribution via gradient boosted trees.
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
            scores = []
            for cid in self.class_labels:
                mean_vec = self._feature_means.get(cid, np.zeros(x_in.shape[1]))
                dist = np.linalg.norm(x_in[0] - mean_vec)
                scores.append(-dist / 120.0)
            exp_scores = np.exp(scores - np.max(scores))
            probs = exp_scores / np.sum(exp_scores)
            return {self.class_labels[i]: float(probs[i]) for i in range(len(self.class_labels))}

    def predict_top_k(self, raw_input: RawAgroFeatures, top_k: int = 10) -> List[MLPredictionCandidate]:
        """
        Returns ranked list of top recommended crops from GBDT model.
        """
        probs = self.predict_probabilities(raw_input)
        sorted_items = sorted(probs.items(), key=lambda x: x[1], reverse=True)[:top_k]

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


# Singleton GBDT model instance
gbdt_classifier = CropGradientBoostingModel()
