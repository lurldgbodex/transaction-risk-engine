import json
import pika
import threading
from fastapi import APIRouter
from app.core.config import RABBITMQ_URL
from app.ml.inference import RiskModel

router = APIRouter()
model = RiskModel()

def consume_transactions():
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()

    channel.queue_declare(queue="transaction.created", durable=True)
    channel.queue_declare(queue="transaction.risk_evaluated", durable=True)

    def callback(ch, method, properties, body):
        event = json.loads(body)
        payload = event['payload']

        result = model.score(payload)

        response_event = {
            'transaction_id': payload['transaction_id'],
            'risk_score': result['risk_score'],
            'risk_level': result['risk_level'],
            'inference_time_ms': result['inference_time_ms'],
            'model_version': result['model_version'],
        }

        channel.basic_publish(
            exchange="",
            routing_key="transaction.risk_evaluated",
            body=json.dumps({"event": response_event}),
            properties=pika.BasicProperties(delivery_mode=2)
        )

        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(
        queue="transaction.created", 
        on_message_callback=callback, 
    )

    channel.start_consuming()

@router.on_event("startup")
def startup_event():
    threading.Thread(target=consume_transactions, daemon=True).start()