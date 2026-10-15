---
name: qa-requirement-risk-analyst
description: >-
  Kỹ năng phân tích requirement, bóc tách quy tắc nghiệp vụ, đặt câu hỏi phản biện BA
  và phát hiện 5 góc khuất kỹ thuật (Concurrency, State Drift, Clock Drifts, Idempotency, Data Integrity)
  kết hợp tra cứu tương quan bug lịch sử từ kho dữ liệu Google Drive.
---

# Skill: Requirement & Risk Analysis (Dành cho Subagent 1)

Kỹ năng này trang bị cho Agent tư duy của một **Lead QA / Business Analyst Specialist** với nhiệm vụ phân tích tĩnh (Static Analysis) chuyên sâu trước khi tiến hành viết test case.

---

## 1. Nguyên Tắc Bóc Tách Quy Tắc Nghiệp Vụ (Business Rules Decomposition)
Mọi requirement từ BA phải được phân rã thành 4 thành phần tất định:
1. **Pre-condition (Tiền điều kiện):** Trạng thái bắt buộc của hệ thống/người dùng trước khi hành động diễn ra (ví dụ: Tài khoản ở trạng thái `ACTIVE`, Đơn hàng ở trạng thái `PAID`).
2. **Trigger (Tác nhân kích hoạt):** Hành động hoặc sự kiện cụ thể kích hoạt luồng xử lý (ví dụ: Người dùng bấm 'Hủy', Cronjob quét định kỳ, Webhook callback gửi về).
3. **Business Constraints (Ràng buộc logic & Ranh giới):**
   * Giới hạn thời gian (Time window): `<=` 300s, sau X phút.
   * Giới hạn số lượng (Quantity/Counter): Ngưỡng 5 lần, `<= Available_Stock`.
   * Tính duy nhất (Uniqueness): 1 lần / 1 tài khoản (`Account_ID`).
4. **Post-condition (Hậu điều kiện):** Trạng thái sau cùng của toàn bộ hệ thống (Đơn hàng sang `CANCELLED`, tồn kho được hoàn, voucher chuyển sang `USED`).

---

## 2. Tiêu Chuẩn Đặt Câu Hỏi Phản Biện BA (Questions for BA)
Tuyệt đối không hỏi các câu hỏi ngô nghê hoặc hiển nhiên. Câu hỏi gửi BA phải tập trung vào **các kẽ hở logic và xử lý ngoại lệ**:
* **Ranh giới thời gian & Độ trễ mạng (Timing & Latency):** *"Mốc thời gian tính theo Server Timestamp hay Client Device Timestamp? Nếu request gửi lúc 4:59 nhưng server nhận lúc 5:01 do nghẽn mạng thì tính thế nào?"*
* **Vòng đời tài nguyên (Resource Lifecycle):** *"Khi hủy đơn hàng hoặc thanh toán thất bại, voucher và điểm thưởng có được hoàn lại về ví người dùng không? Thời hạn sử dụng voucher có được gia hạn không?"*
* **Cơ chế mở khóa / Khôi phục (Recovery Mechanism):** *"Khi tài khoản bị khóa sau 5 lần sai, tài khoản tự động mở sau X phút hay bắt buộc Admin can thiệp / Reset qua Email-OTP?"*
* **Phân định trách nhiệm trạng thái (State Responsibility):** *"Trạng thái PROCESSING bắt đầu từ khi nào: Khi kho in phiếu giao hàng (Pick & Pack) hay khi hệ thống tự động gán shipper?"*

---

## 3. Khung 5 Góc Khuất Kỹ Thuật (5-Dimension Technical Risk Framework)
Subagent 1 bắt buộc phải rà soát qua 5 họ rủi ro kinh điển:
1. **Concurrency & Race Conditions:** Hai request cùng gửi đến trong khoảng vài mili-giây (Double cancel, Double checkout voucher, Concurrent purchase).
2. **State Machine Drift (Xung đột trạng thái đa hệ thống):** Độ trễ cập nhật trạng thái giữa các microservices (OMS vs WMS vs Cổng thanh toán).
3. **Clock Drift & Timing Window:** Chênh lệch giờ giữa App Server, DB Server và Cache Server làm sai lệch bộ đếm thời gian.
4. **Non-idempotency (Không có cơ chế khử trùng lặp):** Cổng thanh toán hoặc webhook retry bắn lặp lại nhiều lần tạo ra nhiều bản ghi đơn hàng/hoàn tiền.
5. **Distributed Transaction Inconsistency:** Tạo đơn thành công nhưng trừ kho thất bại (giao dịch phân tán không đồng nhất).

---

## 4. Kỹ Thuật Truy Vấn Bug Lịch Sử (Historical Bug Correlation)
Khi nhận diện các từ khóa trong requirement, Subagent 1 kích hoạt `bug_retrieval_tool` để đối soát:
* Từ khóa `Hủy`, `Cancel`, `Hoàn tiền` ➔ Đối chiếu **`BUG-001`** (Refund trùng do cancel đồng thời) & **`BUG-002`** (Cancel khi kho đã xử lý).
* Từ khóa `Voucher`, `Khuyến mãi`, `1 lần` ➔ Đối chiếu **`BUG-003`** (Sử dụng cùng voucher cho 2 đơn hàng do thiếu Distributed Lock).
* Từ khóa `Thanh toán`, `Payment`, `Callback` ➔ Đối chiếu **`BUG-004`** (Payment webhook bắn 2 lần tạo 2 order).
* Từ khóa `Tồn kho`, `Stock`, `Số lượng đặt` ➔ Đối chiếu **`BUG-005`** (Order tạo thành công nhưng tồn kho không trừ).
