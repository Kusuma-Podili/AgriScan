"""
AgroPulse 1D & Multi-Variable Kalman Filter for IoT Soil Probe Telemetry Noise Filtering.
Removes electrical noise and transient spikes from FDR/TDR capacitance soil probes.
"""

from typing import Optional


class SoilTelemetryKalmanFilter:
    """
    Recursive 1D Kalman filter estimating true state from noisy sensor telemetry.
    """

    def __init__(
        self,
        process_variance_q: float = 1e-3,
        measurement_variance_r: float = 0.05,
        estimated_error_p: float = 1.0,
        initial_value: float = 25.0,
    ):
        self.q = process_variance_q
        self.r = measurement_variance_r
        self.p = estimated_error_p
        self.x = initial_value
        self.k = 0.0

    def update(self, measurement: float) -> float:
        """
        Executes prediction and measurement update steps:
        1. Time update (prediction): P = P + Q
        2. Measurement update: K = P / (P + R)
           X = X + K * (Z - X)
           P = (1 - K) * P
        """
        # Prediction update
        self.p = self.p + self.q

        # Measurement update
        self.k = self.p / (self.p + self.r)
        self.x = self.x + self.k * (measurement - self.x)
        self.p = (1.0 - self.k) * self.p

        return round(self.x, 2)
