# Antigravity Rules: QA Requirement Assistant Protocol

Whenever the user or tester asks to analyze a requirement, review business rules, or generate test cases, you MUST follow this protocol:

## 1. The Strict 2-Phase State Machine with Local-First & Bidirectional Sync
The workflow consists of sequential phases separated by mandatory human checkpoints and bidirectional cache validation:

```text
[Input Requirement]
        │
        ▼
[PRE-FLIGHT: Drive Cache Validation]
        │  * Check Drive modifiedTime via MCP search_drive_files vs data/.sync_metadata.json
        │  * If modifiedTime matches -> Read directly from local data/bug_repository.json
        │  * If modifiedTime differs (or missing cache) -> Pull from Drive to local data/ -> Read local
        │  * If offline/MCP failure -> Fallback to local data/ and notify tester
        ▼
[PHASE 1: Requirement & Risk Analysis (Invoke req-risk-analyst)]
        │  * Read validated historical bugs from local data/bug_repository.json
        │  * Must consult risk-checklist.md
        ▼
[HUMAN GATE 1: Tester Critique & Approval] ◄── STOP! Do not generate test cases!
        │
        ▼
[PHASE 2: Automation Test Design & Priority (Invoke test-automation-architect)]
        │  * Must follow test-design-matrix.md
        ▼
[HUMAN GATE 2: Tester Test Specification Approval]
        │
        ▼
[PHASE 3: Local-First Update & Sync to Google Workspace]
        │  * Step 1: Update local data/requirements_analysis.json & data/test_cases_specification.json
        │  * Step 2: Push changes to Google Spreadsheet via MCP modify_sheet_values
        │  * Step 3: Refresh & record latest Drive modifiedTime in data/.sync_metadata.json
```

## 2. Non-Negotiable Rules

1. **No Premature Test Generation:**
   * NEVER generate test cases in the first turn.
   * You must complete Phase 1 first (Business Rules, Questions for BA, 5 Technical Risks, Related Historical Bugs).
   * Ask the user/tester to review and confirm Phase 1 before proceeding.

2. **Local-First with Bidirectional Drive Sync & Cache Validation:**
   * Dữ liệu bug và requirement được lưu trữ cục bộ tại thư mục `data/` (`data/bug_repository.json`, `data/requirements_analysis.json`, `data/test_cases_specification.json`).
   * **Đầu phiên:** Kiểm tra `modifiedTime` trên Google Drive. Nếu trùng khớp với `data/.sync_metadata.json`, đọc trực tiếp từ local `data/`. Nếu Drive có thay đổi, đồng bộ từ Drive về local trước khi thực hiện tác vụ.
   * **Cơ chế dự phòng (Offline Fallback):** Nếu không thể kết nối tới Google Workspace MCP hoặc mất mạng, tự động đọc từ tệp local hiện có và hiển thị cảnh báo cho tester.
   * **Cuối phiên:** Sau khi tester duyệt kịch bản ở Phase 2, bắt buộc cập nhật vào local `data/` trước, sau đó đồng bộ lên Google Drive qua MCP `modify_sheet_values`, và cập nhật lại metadata.

3. **Perspective Preference & Persistence (Lựa chọn & Ghi nhớ Góc nhìn):**
   * Hệ thống hỗ trợ 3 góc nhìn phân tích chính:
     - `business`: **Góc nhìn Nghiệp vụ & BA** (ngôn ngữ trực quan, tập trung vào hành vi người dùng và luồng nghiệp vụ, chuyển hóa lỗi kỹ thuật thành câu giải thích đời sống, tránh thuật ngữ hàn lâm).
     - `technical`: **Góc nhìn Kỹ thuật & SDET** (đi sâu vào Race Condition, Lost Update, Distributed Lock, State Drift, Clock Drift, Idempotency, JWT Revocation, 3-tier payloads).
     - `hybrid`: **Góc nhìn Kết hợp Toàn diện** (trình bày song song cả góc nhìn Nghiệp vụ lẫn Kiến trúc Kỹ thuật).
   * **Lưu trữ bền vững:** Cấu hình được lưu tại `data/user_preferences.json`. Sau khi người dùng chọn lần đầu, hệ thống tự động ghi nhớ và áp dụng cho các lần phân tích tiếp theo mà không hỏi lại.
   * **Cho phép đổi vai trò bất kỳ lúc nào:** Bất cứ khi nào người dùng có ý muốn thay đổi vai trò/góc nhìn (ví dụ: *"đổi vai trò"*, *"đổi góc nhìn sang kỹ thuật"*, *"chuyển về nghiệp vụ"*), hệ thống phải lập tức cập nhật lại `data/user_preferences.json` và lưu lại cấu hình mới này.

4. **Rollback on Requirement Change:**
   * If the user modifies, adds, or cancels requirements while in Phase 2 or between phases, immediately invalidate Phase 2 test cases.
   * Rollback the state to Phase 1 and re-analyze with the new scope.

5. **Subagent Delegation:**
   * Delegate Phase 1 analysis to subagent `req-risk-analyst` (subagent đọc bug từ tệp cục bộ `data/bug_repository.json` và áp dụng đúng góc nhìn đã lưu).
   * Delegate Phase 2 test generation to subagent `test-automation-architect`.

6. **Persistence & Traceability:**
   * Every analysis must have a unique `requirement_id` (e.g. `REQ_AUTH_001`, `REQ_INV_001`, `REQ_VOUCHER_001`, `REQ_20261015_001`).
   * Every generated test case must reference `requirement_id` as a foreign key.
   * Write to local files first via accumulative append/upsert, then push append rows to Google Spreadsheet tabs `Requirements_Analysis` and `Test_Cases_Specification`.

7. **Test Case Disaggregation & Deep Verification (Chuẩn Test Case QA/QC Thực Chiến):**
   * **Không gom cụm hành động:** Tuyệt đối không dồn các thao tác độc lập (ví dụ: chọn số lượng -> chọn thanh toán -> bấm submit) vào cùng một bước. Tách bước nhập liệu/chuẩn bị và bước kích hoạt gửi dữ liệu (hoặc đưa vào `Pre-conditions`).
   * **Đồng bộ sâu kết quả mong đợi với API:** API không chỉ ghi HTTP Status Code chung chung, bắt buộc chỉ rõ các trường dữ liệu quan trọng trong Response Body (ví dụ: `order_id` phải trùng khớp với mã hiển thị trên UI).
   * **Bắt buộc kiểm chứng Database & Trạng thái Hệ thống:** Mọi bước có tác động dữ liệu phải nêu rõ kiểm tra bảng nào, cột nào, giá trị mới là gì (bảng `orders`, `inventory`...) và sự kiện Event phát ra.
   * **Cột Trạng thái (`Pass/Fail`):** Bắt buộc có cột trạng thái kiểm thử, mặc định là `NOT_RUN` (hỗ trợ `PASS`, `FAIL`, `BLOCKED`).
   * **Trình bày dạng bảng chi tiết:** `STT` | `Bước thực hiện (Steps)` | `Kết quả mong đợi (Expected Results: UI/API/DB)` | `Trạng thái`.

8. **Google Drive & Sheets Visual Standards (Định Dạng Bảng Tính Chuyên Nghiệp Cho Cả 3 Sheet):**
   * **Header Chuẩn:** Áp dụng đồng bộ cho cả 3 tab (`Test_Cases_Specification`, `Requirements_Analysis`, `Bug_Repository`): Nền xanh Ant Design Blue `#1677FF`, chữ trắng in đậm, cỡ 11, căn giữa (`CENTER` & `MIDDLE`), chiều cao dòng 45px, đóng băng dòng 1 (`frozenRowCount = 1`).
   * **Độ Rộng & Trình Bày Ô:** Các cột phải được set `pixelSize` rộng rãi thoáng mắt (120px - 500px), căn lề trên (`TOP`), tự động xuống dòng (`WRAP`) toàn bộ, viền lưới kẻ nhạt `#CBD5E1`.
   * **Schema 10 Cột Sheet Test Case:** `Requirement ID`, `Test Case ID`, `Scenario Name`, `Test Type`, `Priority`, `Status (Pass/Fail)`, `Pre-conditions`, `Bước thực hiện (Steps)`, `Kết quả mong đợi (UI/API/DB)`, `Notes / Defect ID`.
   * **Schema 5 Cột Sheet Bug Repository:** `Bug ID`, `Description` (rộng 500px), `Root Cause Domain`, `Impacted Flow`, `Severity` (P1 Critical, P2 High).
   * **Tương Tác Dropdown & Màu Sắc:** Cột `Status (Pass/Fail)` có Data Validation menu chọn nhanh và Conditional Formatting (Xanh: PASS, Đỏ: FAIL, Cam: BLOCKED, Xám: NOT_RUN).

9. **Chế Độ Cập Nhật Tích Lũy Thêm Mới (Accumulative Append-Only Records - Tuyệt Đối Không Reset/Clear):**
   * **Bảo toàn toàn bộ lịch sử (Historical Preservation):** Cả tệp cục bộ (`data/`) lẫn Google Spreadsheet đều là kho lưu trữ tích lũy xuyên suốt các phiên làm việc. Tuyệt đối KHÔNG xóa, reset hoặc ghi đè mất các requirement và test case đã phân tích trước đó.
   * **File Local (`data/requirements_analysis.json` & `data/test_cases_specification.json`):** Bắt buộc nạp dữ liệu mảng hiện có, thêm mới (append) các bản ghi của requirement hiện tại vào mảng (nếu trùng ID thì cập nhật/upsert, nếu ID mới thì append). Cấm dùng `write_to_file` với nội dung chỉ chứa 1 requirement đơn lẻ làm mất dữ liệu cũ.
   * **Đồng bộ Google Sheets (`Requirements_Analysis` & `Test_Cases_Specification`):** Tuyệt đối KHÔNG gọi `values().clear()` làm trắng sheet. Giữ nguyên Header ở Row 1 và toàn bộ dữ liệu lịch sử các dòng trước, ghi nối tiếp (append rows) các requirement và test case mới vào các dòng trống tiếp theo ở cuối bảng. Nếu record đã có trên Sheet thì cập nhật đúng dòng đó.
   * **Định danh Duy nhất (`requirement_id`):** Mỗi requirement mới phân tích bắt buộc sinh `requirement_id` duy nhất (ví dụ: `REQ_AUTH_001`, `REQ_INV_001`, `REQ_VOUCHER_001`, `REQ_YYYYMMDD_xxx`). Tuyệt đối không dùng trùng ID của requirement cũ.



