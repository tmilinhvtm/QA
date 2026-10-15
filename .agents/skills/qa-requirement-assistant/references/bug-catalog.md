# Historical Bug Knowledge Base

This catalog defines known production bugs that must be cross-checked during Phase 1 analysis:

| Bug ID | Title & Description | Technical Root Cause | Correlated Triggers |
| :--- | :--- | :--- | :--- |
| **`BUG-001`** | Hai request cancel được gửi gần như đồng thời và hệ thống tạo hai refund. | Race Condition / Non-atomic transaction / Missing Idempotency Key on refund action. | `cancel`, `hủy`, `refund`, `hoàn tiền`, `đồng thời` |
| **`BUG-002`** | Người dùng vẫn cancel được order sau khi warehouse đã bắt đầu xử lý. | State Machine Inconsistency / Distributed State Drift between OMS and WMS. | `cancel`, `hủy`, `processing`, `kho`, `warehouse`, `trạng thái` |
| **`BUG-003`** | Một user sử dụng cùng voucher cho hai đơn hàng. | Concurrency / Missing Distributed Lock on promotion code per Account ID. | `voucher`, `khuyến mãi`, `coupon`, `tài khoản`, `1 lần` |
| **`BUG-004`** | Payment callback được gửi hai lần và tạo ra hai order. | Non-idempotent Webhook Callback / Missing duplicate payment filter. | `thanh toán`, `payment`, `callback`, `webhook`, `cổng thẻ` |
| **`BUG-005`** | Order được tạo thành công nhưng tồn kho không bị trừ. | Distributed Transaction Failure / Asynchronous inventory decrement failure. | `tồn kho`, `kho`, `inventory`, `số lượng`, `đặt mua`, `stock` |
