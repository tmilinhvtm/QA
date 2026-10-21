# E-Commerce Test Design Matrix & Priority Guide

Every software requirement must be comprehensively validated based on **ALL approved Phase 1 data** (Business Rules, BA Decisions, 5 Technical Risks, and Historical Bugs). The 5 core test types serve as **architectural baseline categories**, and the total number of test cases is **dynamically expandable without being capped at 5**:

---

### 1. Architectural Baseline Categories (5 Nhóm Kiểm Thử Cốt Lõi)

| Test Type | Objective & Scope | Priority Standard |
| :--- | :--- | :--- |
| **Happy Path** | Validates the mainstream success journey under standard valid conditions and prerequisites. | `P1 (Critical)` |
| **Boundary Value** | Validates exact business threshold boundaries (e.g. Min/Max order amount, stock edge values, timer thresholds T-1s / T+1s, item quantity limits). | `P2 (High)` |
| **Negative Path** | Deliberately violates business constraints, invalid state preconditions, unauthorized roles, or insufficient balance/inventory. | `P1 (Critical)` |
| **Concurrency & Race Condition** | Simulates parallel multi-threaded requests (2+ threads within <= 10ms–50ms) competing for a shared resource (inventory, single-use voucher, wallet balance, flash sale slot). | `P1 (Critical)` |
| **State Conflict & Recovery** | Simulates cross-service state discrepancies (e.g. Cart vs Order vs Warehouse WMS vs Payment) and verifies atomic rollback / compensation transactions. | `P2 (High)` |

> [!NOTE]
> **Quy Tắc Mở Rộng Không Giới Hạn (Unlimited Dynamic Test Expansion):**
> Ngoài 5 kịch bản đại diện cho 5 nhóm trên, kiến trúc sư kiểm thử BẮT BUỘC sinh thêm các kịch bản kiểm thử phụ thuộc trực tiếp vào:
> 1. Từng quyết định/lựa chọn cụ thể mà BA/Tester đã chốt từ các gợi ý trả lời (BA Decisions Log).
> 2. Các rủi ro kỹ thuật phân tán chuyên sâu (ví dụ: mất kết nối bên thứ 3, token expiration, idempotency retry).
> 3. Các kịch bản phòng chống tái diễn lỗi từ kho bug lịch sử (`bug_repository.json`).
> Tổng số test cases được sinh ra là linh hoạt (ví dụ: 6, 8, 10+ test cases) nhằm bao phủ triệt để mọi ngóc ngách của requirement.

---

### 2. Golden Principles for Test Design (3 Nguyên Tắc Vàng)

1. **Step Disaggregation (Không gom cụm hành động độc lập):**
   - Đưa các tiền đề chuẩn bị vào **Pre-conditions (Điều kiện tiên quyết)**.
   - Phân tách rõ ràng bước chuẩn bị/lựa chọn dữ liệu và bước kích hoạt gửi request (`Submit / Trigger Action`). Tránh tình huống Dev lỗi ở bước nhập liệu làm chặn đứng toàn bộ bước kiểm thử sau.

2. **Synchronized Deep Verification (Kết quả mong đợi đồng bộ sâu):**
   - **UI:** Trạng thái trực quan, nội dung thông báo, trường hiển thị, hoặc mã định danh sinh ra.
   - **API:** Phải nêu rõ HTTP Status Code kèm **các trường dữ liệu cốt lõi trong Response Body** (ví dụ: trường `order_id` phải khớp hoàn toàn với mã đơn hiển thị trên UI).

3. **Database & System State Verification (Bắt buộc kiểm chứng trạng thái Database):**
   - Mọi hành động có biến động dữ liệu phải nêu rõ kiểm tra bảng nào, cột nào, giá trị mới là gì (ví dụ: `orders.order_status = 'Pending'`, `inventory.available_stock` giảm từ 10 xuống 7).
   - Kiểm chứng Event phát ra trên Broker (`OrderPlacedEvent`, `StockReservedEvent`).

---

### 3. Standard Test Case Presentation Format

Mỗi kịch bản kiểm thử được trình bày theo cấu trúc chuẩn:

```markdown
### [TC_ID]: [[Test Type]] [Scenario Name]
- **Mức độ ưu tiên:** P1 / P2 / P3 - *[Lý do xếp hạng]*
- **Điều kiện tiên quyết (Pre-conditions):** [Trạng thái tài nguyên, tài khoản đăng nhập, cấu hình hệ thống]
- **Trạng thái tổng thể:** `NOT_RUN` (Pass / Fail / Blocked)

| STT | Bước thực hiện (Steps) | Kết quả mong đợi (Expected Results) | Trạng thái |
| :---: | :--- | :--- | :---: |
| 1 | Thao tác nhập liệu / chọn phương thức | **[UI]** Giá trị hiển thị đúng, trường được chọn | NOT_RUN |
| 2 | Bấm nút kích hoạt hành động chính<br>*(Endpoint: `POST /api/v1/...`)* | **[UI]** Màn hình kết quả, mã giao dịch hiển thị<br><br>**[API]** HTTP 201/200, Response Body chứa đúng `id`<br><br>**[Database]** Bảng `xyz` sinh bản ghi mới trạng thái `ABC`, cột số lượng cập nhật tương ứng<br><br>**[Event]** Kafka topic phát sự kiện đồng bộ | NOT_RUN |
```

