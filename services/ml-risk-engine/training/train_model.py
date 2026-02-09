import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from datetime import datetime

DATA_PATH = "../data/training_dataset.csv"
MODEL_OUTPUT_DIR = "../models"

def train():
    df = pd.read_csv(DATA_PATH)

    X = df[
        [
            "amount",
            "transaction_frequency",
            "time_of_day",
            "geo_changed",
            "channel"
        ]
    ]

    pipeline = Pipeline(
        steps = [
            ("scaler", StandardScaler()),
            ("model", IsolationForest(
                n_estimators=200,
                contamination=0.05,
                random_state=42
            ))
        ]
    )

    pipeline.fit(X)

    version = datetime.utcnow().strftime("v%Y%m%d%H%M")
    model_path = f'{MODEL_OUTPUT_DIR}/isolation_forest_{version}.pkl'

    joblib.dump(pipeline, model_path)
    
    print(f"Model trained and saved to {model_path}")


if __name__ == "__main__":
    train()