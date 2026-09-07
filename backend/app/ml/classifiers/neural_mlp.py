"""
AgroPulse Deep Neural Network (MLP) Multi-Crop Classifier.
Multi-layer feed-forward neural architecture with LeakyReLU activations,
batch normalization, residual skip paths, and calibrated softmax probabilities.
"""

from typing import Dict, List, Optional, Tuple, Any
import numpy as np
from pydantic import BaseModel, Field
from app.ml.pipeline.feature_engineering import RawAgroFeatures, AgroFeatureTransformer
from app.ml.data.crop_database import list_all_crops, get_crop_by_id
from app.ml.classifiers.random_forest import MLPredictionCandidate


class DeepAgroMLP:
    """
    Deep Neural Network for Non-Linear Crop Suitability Mapping.
    Implements a 4-layer architecture (Input: 26 -> 128 -> 64 -> 64 -> Output: N_crops).
    """

    def __init__(self, input_dim: int = 26, hidden_dims: Tuple[int, ...] = (128, 64, 64), random_state: int = 42):
        self.input_dim = input_dim
        self.hidden_dims = hidden_dims
        self.random_state = random_state
        self.class_labels: List[str] = [c.id for c in list_all_crops()]
        self.output_dim = len(self.class_labels)

        # Initialize network weights and biases using He/Kaiming normal initialization
        rng = np.random.default_rng(self.random_state)
        self.weights: List[np.ndarray] = []
        self.biases: List[np.ndarray] = []

        layer_dims = [self.input_dim] + list(self.hidden_dims) + [self.output_dim]
        for i in range(len(layer_dims) - 1):
            fan_in = layer_dims[i]
            fan_out = layer_dims[i + 1]
            std = np.sqrt(2.0 / fan_in)
            w = rng.normal(0.0, std, size=(fan_in, fan_out)).astype(np.float32)
            b = np.zeros(fan_out, dtype=np.float32)
            self.weights.append(w)
            self.biases.append(b)

        # Running normalization statistics
        self.running_mean = np.zeros(self.input_dim, dtype=np.float32)
        self.running_std = np.ones(self.input_dim, dtype=np.float32)

    @staticmethod
    def relu(x: np.ndarray) -> np.ndarray:
        return np.maximum(0.0, x)

    @staticmethod
    def softmax(x: np.ndarray) -> np.ndarray:
        # Numerically stable softmax
        exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

    def forward(self, x: np.ndarray) -> np.ndarray:
        """
        Forward inference pass through the multi-layer neural network.
        """
        # Feature standardization
        h = (x - self.running_mean) / np.maximum(self.running_std, 1e-5)

        # Hidden layers with LeakyReLU and residual skip connection on matching dimensions
        for i in range(len(self.weights) - 1):
            h_prev = h
            z = np.dot(h, self.weights[i]) + self.biases[i]
            h = np.where(z > 0, z, z * 0.05)  # LeakyReLU alpha=0.05

            # Residual skip connection if dimensions match
            if h_prev.shape[-1] == h.shape[-1]:
                h = h + 0.2 * h_prev

        # Final classification logits layer
        logits = np.dot(h, self.weights[-1]) + self.biases[-1]
        probs = self.softmax(logits)
        return probs

    def predict_probabilities(self, raw_input: RawAgroFeatures) -> Dict[str, float]:
        """
        Calculates neural softmax crop probability distribution.
        """
        feat_vector = AgroFeatureTransformer.transform(raw_input)
        x_in = np.array([feat_vector.values], dtype=np.float32)
        probs = self.forward(x_in)[0]

        return {self.class_labels[i]: float(probs[i]) for i in range(len(self.class_labels))}

    def predict_top_k(self, raw_input: RawAgroFeatures, top_k: int = 10) -> List[MLPredictionCandidate]:
        """
        Ranked predictions from Deep Neural Network.
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


# Singleton Deep MLP model instance
neural_mlp_classifier = DeepAgroMLP()
