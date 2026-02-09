import joblib
import time
from app.ml.features import extract_features
from app.core.config import (
    MODEL_PATH,
    LOW_RISK_THRESHOLD,
    HIGH_RISK_THRESHOLD,
)

class RiskModel:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def score(self, payload: dict):
        start = time.time()

        features = extract_features(payload)
        raw_score = self.model.decision_function(features)[0]

        # Normalize score to 0-1
        risk_score = min(max(raw_score, 0), 1)

        if risk_score > HIGH_RISK_THRESHOLD:
            risk_level = "HIGH"
        elif risk_score > LOW_RISK_THRESHOLD:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        inference_time = int((time.time() - start) * 1000)

        return {
            "risk_score": round(risk_score, 2),
            "risk_level": risk_level,
            "inference_time_ms": inference_time,
            "model_version": "v1.0.0",
        }
