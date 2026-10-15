# 5-Dimension Technical Risk Framework

When analyzing any requirement, evaluate these 5 critical architectural vulnerabilities:

### 1. Concurrency & Race Conditions
* Multiple user actions or API calls occurring within a 10ms–100ms window.
* Examples: Double-clicking "Cancel", parallel checkout from two browser tabs, concurrent purchase of the last stock item.
* Mitigation check: Distributed locking (Redis Redlock), Database Row-level locking (`SELECT FOR UPDATE`), Unique compound database indexes.

### 2. State Machine Drift & Distributed Consistency
* Discrepancies between independent microservices (e.g. Order Service vs Warehouse Management System vs Payment Gateway).
* Examples: Order shows "PAID" while warehouse marked "CANCELLED", or warehouse begins packing while user sends cancel.
* Mitigation check: Two-Phase Commit, Saga Pattern, Idempotent event consumers, Optimistic concurrency control (`version` column).

### 3. Clock Drift & Timing Window Latency
* Timestamp discrepancies between Client devices, App servers, and Database servers.
* Network latency: Request sent at `04:59` arrives at the server at `05:01`.
* Mitigation check: Enforce strictly authoritative Server Timestamps, UTC standard, and grace-period tolerance buffers.

### 4. Non-Idempotency
* Duplicate execution of non-idempotent operations (payment capture, order creation, refund initiation).
* Examples: Payment gateway retries webhook 3 times, creating duplicate orders.
* Mitigation check: Enforce unique `Idempotency-Key` headers, request deduplication cache.

### 5. Data Integrity & Lifecycle Reversal
* Failure to properly roll back secondary resources when primary operations fail or cancel.
* Examples: Order is canceled, but promotion voucher remains `USED`, or inventory is not re-credited.
* Mitigation check: Atomic compensation transactions, transactional outbox pattern.
