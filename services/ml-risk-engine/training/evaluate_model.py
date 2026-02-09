import numpy as np
import pandas as pd
import joblib

MODEL_PATH = "../models/isolation_forest_v1.pkl"
DATA_PATH = "../data/training_dataset.csv"

def evaluate():
    model = joblib.load(MODEL_PATH)
    df = pd.read_csv(DATA_PATH)

    X = df.sample(100)
    scores = model.decision_function(X)

    print("Score Stats:")
    print(f"Min: {scores.min():.4f}")
    print(f"Max: {scores.max():.4f}")
    print(f"Mean: {scores.mean():.4f}")

if __name__ == "__main__":
    evaluate()