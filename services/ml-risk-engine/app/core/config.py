import os

RABBITMQ_URL = os.getenv('RABBITMQ_URL', 'amqp://guest:guest@localhost:5672/')
MODEL_PATH = os.getenv('MODEL_PATH', 'models/isolation_forest_v1.pkl')

LOW_RISK_THRESHOLD = os.getenv('LOW_RISK_THRESHOLD', 0.4)
HIGH_RISK_THRESHOLD = os.getenv('HIGH_RISK_THRESHOLD', 0.7)