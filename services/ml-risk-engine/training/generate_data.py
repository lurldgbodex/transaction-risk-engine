import numpy as np
import pandas as pd
import datetime
import random
import math

def generate_transactions(n=10000):
    data = []

    for _ in range(n):
        amount = np.random.lognormal(mean=4, sigma=0.5)
        txn_freq = np.random.poisson(lam=3)
        hour = random.randint(0, 23)
        time_of_day = math.sin(2 * math.pi * hour / 24)
        geo_changed = np.random.choice([0, 1], p=[0.9, 0.1])
        channel = np.random.choice([0, 1], p=[0.4, 0.6])  # 0: WEB, 1: MOBILE

        # Inject anomalies
        if random.random() < 0.05:
            amount *= random.randint(10, 50)
            txn_freq += random.randint(10, 30)
            geo_changed = 1

        data.append({
            "amount": amount,
            "txn_freq": txn_freq,
            "time_of_day": time_of_day,
            "geo_changed": geo_changed,
            "channel": channel
        })

    return pd.DataFrame(data, columns=["amount", "transaction_frequency", "time_of_day", "geo_changed", "channel"])

if __name__ == "__main__":
    df = generate_transactions()
    df.to_csv("../data/training_dataset.csv", index=False)
