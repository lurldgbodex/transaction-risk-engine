# API Contracts & Event Schemas

## API GATEWAY (NestJS)

### Endpoint: Create Transaction

```bash
POST /api/v1/transactions
```

### Request

```json
{
  "userId": "uuid",
  "amount": 250.75,
  "currency": "USD",
  "transactionType": "TRANSFER",
  "channel": "MOBILE",
  "metadata": {
    "deviceId": "string",
    "ipAddress": "102.89.23.1",
    "country": "NG"
  }
}
```

### Validation Rules

- amount > 0
- currency = [USD, NGN, EUR]
- transactionType enum
- channel enum
- ipAddress valid IPV4

### Response (Accepted)

```json
{
  "transactionId": "uuid",
  "status": "PENDING_RISK_EVALUATION"
}
```

## Transaction Service (NestJS)

### Responsibilities

- Persist transaction
- Publish event to RabbitMQ
- Idempotency handling

### Event: `transaction.created`

```json
{
  "eventId": "uuid",
  "eventType": "TRANSACTION_CREATED",
  "timestamp": "2026-01-01T10:00:00Z",
  "payload": {
    "transactionId": "uuid",
    "userId": "uuid",
    "amount": 250.75,
    "currency": "USD",
    "transactionType": "TRANSFER",
    "channel": "MOBILE",
    "country": "NG"
  }
}
```

## ML Risk Engine (FastAPI)

### Endpoint: Score Transaction

```bash
POST /risk/score
```

### Request

```json
{
  "transactionId": "uuid",
  "userId": "uuid",
  "amount": 250.75,
  "currency": "USD",
  "transactionType": "TRANSFER",
  "channel": "MOBILE",
  "country": "NG"
}
```

### Response

```json
{
  "transactionId": "uuid",
  "riskScore": 0.91,
  "riskLevel": "HIGH",
  "modelVersion": "v1.0.0",
  "inferenceTimeMs": 47
}
```

### Risk Thresholds (Configurable)

| **Score** | **Level** |
| :-------- | :-------: |
| <0.4      |    LOW    |
| 0.4 - 0.7 |  MEDIUM   |
| >0.7      |   HIGH    |

## Decision Service (NestJS)

### Rules Engine

```ts
if (riskLevel === "HIGH") decision = "BLOCK";
else if (riskLevel === "MEDIUM") decision = "REVIEW";
else decision = "ALLOW";
```

### Event: transaction.risk_evaluated

```json
{
  "transactionId": "uuid",
  "decision": "BLOCK",
  "riskScore": 0.91,
  "modelVersion": "v1.0.0",
  "evaluatedAt": "2026-01-01T10:00:01Z"
}
```

### Error Handling

- ML service timeout - retry (max 3)
- Persistent failure - DLQ
- Transaction remains in `RISK_EVALUATION_FAILED`

## Observability

**Each service exposes**

```bash
GET /metrics
```

**Metrics**

- request_latency_ms
- inference_latency_ms
- messages_processed_total
- failed_inferences_total
- risk_distribution
