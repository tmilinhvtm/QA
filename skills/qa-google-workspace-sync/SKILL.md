---
name: qa-google-workspace-sync
description: >-
  Kỹ năng quản lý phiên làm việc tập trung (State Machine Lifecycle), điều phối Human-in-the-loop Gates,
  và đồng bộ dữ liệu thời gian thực lên Google Drive qua MCP Server google-workspace.
---

# Skill: State Machine Orchestration & Google Workspace Sync (Dành cho Master Orchestrator)

Kỹ năng này trang bị cho Master Agent khả năng kiểm soát toàn bộ vòng đời phiên làm việc, thiết lập rào chắn kiểm duyệt của con người, và duy trì tính toàn vẹn dữ liệu khi đẩy lên Google Sheets qua giao thức MCP.

---

## 1. Cơ Chế Điều Phối 2-Phase State Machine
Master Agent phải thực thi nghiêm ngặt chu trình chuyển trạng thái sau:

```text
[IDLE] 
  │  (Nhận requirement từ Tester)
  ▼
[PHASE_1_ANALYSIS] 
  │  (Subagent 1 phân tích xong)
  ▼
[WAITING_TESTER_PHASE_1] ◄──── CỔNG KIỂM SOÁT 1 (Tester phản biện & chốt)
  │  (Tester gõ 'ok' / 'chốt')
  ▼
[PHASE_2_TEST_GEN] 
  │  (Subagent 2 sinh 5+ test cases xong)
  ▼
[WAITING_TESTER_PHASE_2] ◄──── CỔNG KIỂM SOÁT 2 (Tester duyệt kịch bản)
  │  (Tester gõ 'export' / 'lưu')
  ▼
[SYNCED] 
```

### Quy tắc bất di bất dịch:
1. **Không nhảy cóc (No Premature Execution):** Tuyệt đối không được kích hoạt Subagent 2 sinh test case khi Tester chưa chốt Phase 1.
2. **Cơ chế Rollback (Context Invalidation):** Nếu Tester thay đổi nội dung requirement ở bất kỳ thời điểm nào, Orchestrator phải xóa sạch toàn bộ test case đã sinh ở Phase 2, đưa trạng thái về `PHASE_1_ANALYSIS` để phân tích lại từ đầu, ngăn chặn ô nhiễm ngữ cảnh (Context Pollution).

---

## 2. Chuẩn Đồng Bộ Google Workspace MCP (MCP Persistence Rules)
Khi Tester xác nhận xuất dữ liệu, Orchestrator sử dụng tool MCP `modify_sheet_values` để ghi vào đúng 2 Tab liên kết:

### Tab 1: `Requirements_Analysis`
* Ghi 1 dòng gồm 8 cột: `[requirement_id, timestamp, requirement_text, business_rules, questions_for_ba, possible_risks, related_bugs, key_decisions_log]`.
* Format: Các điểm gạch đầu dòng phân cách bằng dấu xuống dòng (`\n• `) để Google Sheets hiển thị rõ ràng.

### Tab 2: `Test_Cases_Specification`
* Ghi danh sách 5+ dòng tương ứng với các test case đã duyệt.
* Ràng buộc khóa ngoại: Cột đầu tiên bắt buộc phải là `requirement_id` trùng khớp với Tab 1 để bảo đảm tính toàn vẹn truy vết (Requirements Traceability Matrix - RTM).
* Cột `Simulated Steps` và `Expected Results` được format tuần tự theo từng bước `Bước X:` và `Kỳ vọng X:`.
