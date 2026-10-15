# Test Design Matrix & Priority Guide

Every requirement must generate at least 5 prioritized automated test scenarios:

### 1. Mandatory 5 Test Types

| Test Type | Objective | Priority Standard |
| :--- | :--- | :--- |
| **Happy Path** | Validates mainstream user journey with valid prerequisites. | `P1 (Critical)` |
| **Boundary Value** | Validates exact edge values (e.g. 4m59s vs 5m01s; Order_Quantity == Available_Stock). | `P2 (High)` |
| **Negative Path** | Deliberately violates business constraints or state preconditions. | `P1 (Critical)` |
| **Concurrency** | Simulates parallel multi-threaded requests within a 10ms window. | `P1 (Critical)` |
| **State Conflict & Recovery** | Validates cross-service race condition and resource recovery/reversal. | `P2 (High)` |

### 2. Simulated Step & Expected Result Format
Each test case step must follow this structure:
```text
Step X: [Action & Input]
  - Endpoint/UI Action: POST /api/v1/orders/{id}/cancel
  - Payload/Headers: { "idempotency_key": "uuid", "reason": "user_cancelled" }
  - Timing: T0 + 150 seconds

Expected Result X:
  - API Level: HTTP 200 OK, response body contains { "status": "CANCELLED" }
  - Database Level: `orders.status` updated to 'CANCELLED', `refunds` table records 1 refund entry
  - Event Bus Level: `OrderCancelledEvent` emitted to Kafka/RabbitMQ
```
