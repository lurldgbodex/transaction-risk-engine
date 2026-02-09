import numpy as np

class DriftDetection:
    def __init__(self):
        self.baseline_mean = None

    def detect(self, features: np.ndarray):
        current_mean = features.mean()

        if self.baseline_mean is None:
            self.baseline_mean = current_mean
            return False

        drift = abs(current_mean - self.baseline_mean) > 0.3
        return drift