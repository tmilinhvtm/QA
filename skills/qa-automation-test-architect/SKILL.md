---
name: qa-automation-test-architect
description: >-
  Kỹ năng thiết kế kịch bản kiểm thử tự động giả lập (Simulated Automation Test Specification)
  với ma trận 5 kịch bản bao phủ (Happy, Boundary, Negative, Concurrency, State Conflict),
  xếp hạng độ ưu tiên rủi ro (P1, P2, P3) và kỳ vọng 3 tầng (UI, API, Database).
---

# Skill: Automation Test Specification (Dành cho Subagent 2)

Kỹ năng này trang bị cho Agent tư duy của một **Senior Automation Test Architect**, chuyển hóa tri thức nghiệp vụ đã được duyệt từ Phase 1 thành các kịch bản kiểm thử tự động có khả năng chuyển giao cho đội ngũ Playwright / Selenium / Cypress thực thi.

---

## 1. Ma Trận 5 Kịch Bản Bắt Buộc (The 5-Scenario Coverage Matrix)
Đối với bất kỳ requirement nào, Subagent 2 bắt buộc phải thiết kế đủ 5 loại kịch bản:

| Loại Kịch Bản | Mục Tiêu Kiểm Thử | Ví Dụ Điển Hình |
| :--- | :--- | :--- |
| **1. Happy Path** | Xác thực luồng chuẩn mực của người dùng bình thường khi thỏa mãn toàn bộ điều kiện. | Hủy đơn thành công ở phút thứ 2 khi đơn ở trạng thái CREATED. |
| **2. Boundary Value** | Kiểm tra ranh giới chính xác của các biến số thời gian / số lượng. | So sánh kết quả tại đúng 4 phút 59 giây vs 5 phút 01 giây; Đặt mua đúng bằng tồn kho. |
| **3. Negative Path** | Cố tình vi phạm các ràng buộc nghiệp vụ để xác thực cơ chế phòng vệ của hệ thống. | Cố hủy khi đơn đã chuyển sang PROCESSING; Nhập mật khẩu đúng khi tài khoản đã bị LOCKED. |
| **4. Concurrency / Race Condition** | Mô phỏng các tác vụ đồng thời ở cấp độ micro-second bằng Multi-threading/Async API calls. | Bắn 2 request Cancel cùng lúc trong 10ms; Mở 2 tab trình duyệt cùng checkout 1 voucher. |
| **5. State Conflict & Recovery** | Kiểm tra xung đột trạng thái giữa các hệ thống và cơ chế phục hồi dữ liệu khi có sự cố. | User hủy đơn đúng lúc Kho bấm đóng gói; Hoàn lại voucher/tồn kho khi thanh toán bị timeout. |

---

## 2. Tiêu Chí Xếp Hạng Độ Ưu Tiên (Risk-Based Priority Ranking)
Không phải test case nào cũng có giá trị như nhau. Subagent 2 phải phân loại độ ưu tiên rõ ràng kèm lý do:
* **`P1 (Critical)`**:
  * Các kịch bản liên quan đến **Thiệt hại tài chính** (Double refund, thất thoát tồn kho, clone voucher).
  * Các lỗ hổng **Bảo mật & Race Condition** (Brute-force bypass, Overselling).
  * Luồng nghiệp vụ cốt lõi (Happy path chính của hệ thống).
  * *Bắt buộc phải có Automation Test tự động chạy trong CI/CD pipeline trước khi release.*
* **`P2 (High)`**:
  * Các giá trị biên (Boundary) và xử lý ngoại lệ nghiệp vụ chính.
  * Tính nhất quán dữ liệu giữa OMS, WMS và Payment Gateway.
* **`P3 (Medium)`**:
  * Kiểm tra hiển thị thông báo lỗi trên giao diện (UI Toast/Alert message).
  * Cơ chế auto-unlock sau thời gian timeout.

---

## 3. Quy Chuẩn Đặc Tả Bước Giả Lập & Kỳ Vọng 3 Tầng (Simulated Steps Standard)
Vì giai đoạn phân tích requirement thường chưa có bản thiết kế Figma hoặc DOM Selector cụ thể, mỗi bước kiểm thử phải được mô tả độc lập theo chuẩn:
* **Action & Input Payload (Hành động giả lập):**
  * Mô tả rõ API Endpoint (e.g. `POST /api/v1/orders/{id}/cancel`), tham số truyền lên (`headers`, `idempotency-key`, `body payload`) hoặc hành vi người dùng mô phỏng.
* **Expected Result 3 Tầng (Kỳ vọng kết quả):**
  1. *Tầng API:* Mã HTTP Status (`200 OK`, `400 Bad Request`, `409 Conflict`) và cấu trúc Error Message.
  2. *Tầng Database:* Trạng thái bản ghi (Field `status = 'CANCELLED'`, `failed_attempts = 5`, `stock = 7`).
  3. *Tầng Event / Async Message:* Phát sinh Event bus tương ứng (`OrderCancelledEvent`, `RefundTriggeredEvent`).
