from fastapi import FastAPI
from app.api.routes import router
from app.core.logging import setup_logging
from prometheus_client import start_http_server
import threading

app = FastAPI(title="ML Risk Engine")

setup_logging()
app.include_router(router)

def start_metrics():
    start_http_server(8001)

threading.Thread(target=start_metrics, daemon=True).start()
