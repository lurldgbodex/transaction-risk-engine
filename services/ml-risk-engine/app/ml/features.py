import numpy as np
from datetime import datetime
import math

def encode_time_of_day(timestamp: str) -> float:
    """
    Cyclical encoding of hour of day
    """
    hour = datetime.fromisoformat(timestamp).hour
    return math.sin(2 * math.pi * hour / 24)

def extract_features(payload: dict) -> np.ndarray:
    """
    Extracts model features from transaction payload.
    """
    amount = payload['amount']
    txn_frequency = payload.get('transactionFrequency', 1)
    time_of_day = encode_time_of_day(payload['timestamp'])
    geo_changed = 1 if payload.get('geoChanged', False) else 0
    channel_encoded = 1 if payload.get('channel') == 'MOBILE' else 0

    return np.array([[
        amount,
        txn_frequency,
        time_of_day,
        geo_changed,
        channel_encoded
    ]])