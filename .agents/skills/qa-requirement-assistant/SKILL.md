---
name: qa-requirement-assistant
description: >-
  Use this skill whenever the user or tester provides a software requirement, user story,
  or feature description for an E-Commerce or digital service system, and asks to analyze business rules, identify technical risks,
  correlate historical bugs from local storage and Google Drive via MCP, or design prioritized simulated automation test specifications synced to Google Drive.
---

# QA Requirement Assistant Framework (Local-First & Bidirectional Sync)

This skill guides the AI Agent to act as a **Lead QA Engineer & Agent Orchestrator** managing requirement decomposition, risk discovery via specialized reference manuals, local-first historical bug retrieval with bidirectional Google Drive synchronization, human-in-the-loop validation gates, and prioritized automated test design.

---

## 🏛️ The 3 Pillars of Execution

```text
[Requirement Input]
         │
         ├───► Pre-Flight: Cache Validation (Google Drive vs Local data/)
         │          • Read config (spreadsheet_id, user_google_email) from `data/.sync_metadata.json`
         │          • Query Drive `modifiedTime` via MCP `search_drive_files`
         │          • Compare against `last_modified_time_drive` in metadata
         │          • If match: read local `data/bug_repository.json`
         │          • If changed: pull fresh bugs from Drive to local -> read local
         │          • If offline/MCP failure: fallback to local cache & warn tester
         │
         ├───► Pillar 1: Static Requirement & Risk Analysis (Invoke 'req-risk-analyst')
         │          • Decompose 4 Business Rules: Pre-condition, Trigger, Constraints, Post-condition
         │          • Ask sharp Questions for BA kèm các phương án gợi ý trả lời (Option A, Option B, Recommended)
         │          • Analyze 5 Technical Risks using [Risk Checklist](./references/risk-checklist.md)
         │          • Correlate with historical bugs read from local `data/bug_repository.json`
         │
         ├───► Phase 1A: Business Rules & Questions for BA (Direct Main Chat Rendering)
         │
         ├───► [GATE 1] Interactive Modal via 'ask_question' (Tester/BA click chọn phương án)
         │          • Ghi nhận các lựa chọn vào BA Decisions Log
         │
         ├───► Phase 1B: 5 Technical Risks & Historical Bugs (Chạy tiếp sau khi có lựa chọn BA)
         │
         ├───► Pillar 2: Prioritized Simulated Test Specification (Invoke 'test-automation-architect')
         │          • Generate comprehensive test scenarios from [Test Design Matrix](./references/test-design-matrix.md)
         │          • Inherit ALL approved Phase 1 data: Business Rules, BA Decisions Log, 5 Technical Risks, Historical Bugs
         │          • 5 Baseline Categories with UNLIMITED dynamic expansion (not capped at 5)
         │          • Risk-based Priority Ranking: P1 (Critical), P2 (High), P3 (Medium)
         │          • Specify Simulated Actions (API/Payload) and 3-Tier Expected Results (UI + DB + Event)
         │
         ├───► [GATE 2] Await Tester Approval
         │
         └───► Pillar 3: Local-First Persistence & Cloud Sync (Google Workspace MCP)
                    • Assign unique `requirement_id`
                    • Step 3.1: Save new requirement to `data/requirements_analysis.json` & test cases to `data/test_cases_specification.json`
                    • Step 3.2: Push append rows to Google Spreadsheet via MCP `modify_sheet_values`
                    • Step 3.3: Update latest `modifiedTime` in `data/.sync_metadata.json`
```

---

## 📋 Step-by-Step Execution Workflow

### Step 0: Pre-Flight Cache Validation & Local Sync
1. Read configuration from local file `data/.sync_metadata.json` to get `spreadsheet_id`, `spreadsheet_name`, and `user_google_email`.
2. Call tool `google-workspace:search_drive_files`:
   * `query`: `name = '<spreadsheet_name>' and trashed = false`
   * `user_google_email`: `<user_google_email>`
   * `detailed`: `true`
3. Extract `modifiedTime` from the Drive response.
4. Compare `modifiedTime` with `last_modified_time_drive` in `data/.sync_metadata.json`:
   * **Cache Hit (Drive unmodified):** Read `data/bug_repository.json` directly from local storage.
   * **Cache Invalidation (Drive modified or missing local):**
     * Call MCP `read_sheet_values` on `Bug_Repository!A1:D` and `Requirements_Analysis!A1:Z`.
     * Update `data/bug_repository.json`, `data/requirements_analysis.json`.
     * Update `data/.sync_metadata.json` with the new `last_modified_time_drive`.
     * Read from local files to proceed.
   * **Offline Fallback:** If MCP tool call errors or network is unavailable, read from local `data/bug_repository.json` and append a prominent notice:
     `> [!WARNING] Đang hoạt động ở chế độ Offline: Sử dụng dữ liệu Bug & Requirement cục bộ từ thư mục data/.`

### Step 0.1: Analysis Perspective Preference & Persistence
1. Check `data/user_preferences.json`:
   * If exists: Load `analysis_perspective` (`business`, `technical`, or `hybrid`).
   * If missing or empty: Prompt user using `ask_question` or interactive choice to select their preferred perspective (`business`, `technical`, `hybrid`), save to `data/user_preferences.json`, and inform user that their choice is saved.
2. If user requests to switch roles/perspectives at any time (e.g. "đổi vai trò", "đổi góc nhìn sang kỹ thuật"):
   * Immediately update `data/user_preferences.json` and persist the new choice.

### Step 1: Phase 1A Analysis (Business Rules, Questions for BA & Modal Chọn Ngay)
1. **Phân tích Phase 1A:** Bóc tách 4 thành tố Business Rules và đặt Questions for BA kèm các options gợi ý (đặt phương án tối ưu lên đầu với tiền tố `(Recommended)`).
2. **Hiển thị trực tiếp ra Luồng Chat Chính (Direct Main Chat Rendering):**
   * Orchestrator in toàn văn trực tiếp ra luồng chat chính:
     * **1. Business Rules** (Pre-condition, Trigger, Constraints, Post-condition)
     * **2. Questions for BA** (Các câu hỏi chất vấn kèm gợi ý trả lời Option A, Option B... và Khuyến nghị)
   * Tuyệt đối KHÔNG ẩn trong collapsible card hay file artifact.
3. **KÍCH HOẠT MODAL CHỌN NGAY VIA `ask_question` & TẠM DỪNG:**
   * Ngay sau khi in xong Phần 1 & Phần 2 ra chat chính, Orchestrator **BẮT BUỘC GỌI NGAY CÔNG CỤ `ask_question`** đưa danh sách câu hỏi BA lên Modal tương tác.
   * Tester / BA **click chọn ngay bằng chuột** trên Modal. Tiến trình tạm dừng chờ người dùng submit.

### Step 2: Handle BA Choices & Phase 1B Deep-Dive (Technical Risks & Bugs)
1. **Ghi nhận lựa chọn (BA Decisions Log):** Trích xuất các phương án người dùng đã click chọn từ modal `ask_question` để tổng hợp thành bản ghi `BA Decisions Log`.
2. **Phase 1B — Chạy tiếp Phần 3 & Phần 4 trực tiếp ra luồng chat chính:**
   * Ngay sau khi có quyết định chốt của BA từ modal, Orchestrator in tiếp trực tiếp ra luồng chat chính:
     * **3. Possible Risks (5 Technical Risks):** Đào sâu 5 góc khuất kỹ thuật (Concurrency, State Drift, Clock Drift, Non-Idempotency, Distributed Tx) bám sát theo chính các phương án BA vừa chọn!
     * **4. Related Historical Bugs:** Đối chiếu ngữ nghĩa với các bug patterns từ local `data/bug_repository.json` nhằm ngăn chặn tái diễn lỗi.
3. **Chốt duyệt & Chuyển giao sang Phase 2:**
   * Hỏi Tester xác nhận: *"Bạn duyệt toàn bộ phân tích nghiệp vụ và rủi ro trên chưa? Nếu đồng ý, tôi sẽ tiến hành thiết kế bộ kịch bản Automation Test."*
   * Chỉ khi Tester xác nhận ("ok", "chốt", "tiếp tục"), tiến hành Step 3 (chuyển giao toàn bộ Business Rules, BA Decisions Log, 5 Technical Risks, Bug Repository sang Phase 2).

### Step 3: Phase 2 Test Specification (Subagent `test-automation-architect`)
1. Pass the finalized Phase 1 context (Business Rules, BA Decisions Log, 5 Technical Risks, Historical Bugs) to subagent `test-automation-architect`.
2. Follow the [Test Design Matrix](./references/test-design-matrix.md) to generate a comprehensive test suite:
   * **Inherit ALL Phase 1 data:** Every scenario must directly validate Business Rules, BA choices, 5 Technical Risks, or Historical Bug prevention.
   * **5 Baseline Categories:** Cover Happy Path (P1), Boundary Value (P2), Negative Path (P1), Concurrency / Race Condition (P1), and State Conflict / Recovery (P2).
   * **Unlimited Dynamic Expansion:** Do NOT cap at 5 test cases. Expand dynamically to N test cases (e.g. 6, 8, 10+ test cases) based on requirement complexity and BA decisions.
3. For each test case, apply the **3 Golden Testing Principles**:
   * **Step Disaggregation:** Đưa tiền đề vào `Pre-conditions`. Tách riêng bước chọn dữ liệu (Bước 1) và bước kích hoạt gửi dữ liệu (Bước 2).
   * **Synchronized Deep Verification:** UI hiển thị gì, API có HTTP Status + **Response Body fields cụ thể** (ví dụ `order_id` phải khớp với UI).
   * **Database & System State Verification:** Chỉ rõ bảng, cột, giá trị biến động trong DB và Event phát sinh.
   * **Execution Status:** Mặc định `NOT_RUN` (hỗ trợ `PASS`, `FAIL`, `BLOCKED`).
   * Trình bày dạng bảng trực quan: `STT` | `Bước thực hiện (Steps)` | `Kết quả mong đợi (Expected Results: UI/API/DB)` | `Trạng thái`.
4. **STOP AND PROMPT TESTER:**
   Ask the tester: *"Bạn duyệt bộ kịch bản test này chưa? Nếu đồng ý, tôi sẽ cập nhật vào file local và đồng bộ toàn bộ lên Google Drive qua MCP."*

### Step 4: Local-First Update & Sync to Google Workspace (Accumulative Append-Only)
1. Assign unique `requirement_id` (format: `REQ_<MODULE>_<ID>` hoặc `REQ_<YYYYMMDD>_<ID>`).
2. **Update Local Data First (Append-Only Accumulation):**
   * Load existing arrays from `data/requirements_analysis.json` & `data/test_cases_specification.json`.
   * Append/upsert the new requirement record into `data/requirements_analysis.json` (Tuyệt đối KHÔNG overwrite/reset xóa các requirement cũ).
   * Append/upsert all newly generated structured test cases into `data/test_cases_specification.json` (Tuyệt đối KHÔNG overwrite/reset xóa các test cases cũ).
3. **Push Accumulative Changes to Google Spreadsheet & Apply Styling:**
   * Run sync script: `python3 .agents/skills/qa-requirement-assistant/scripts/google_sheets_sync_manager.py sync_all`.
   * Script sẽ tự động kiểm tra các dòng hiện có trên Google Sheet và **ghi nối tiếp (append rows)** các bản ghi mới vào cuối bảng tính mà không bao giờ xóa hay làm trắng sheet (`never clear`).
   * Schema 10 cột `Test_Cases_Specification`: `Requirement ID`, `Test Case ID`, `Scenario Name`, `Test Type`, `Priority`, `Status (Pass/Fail)`, `Pre-conditions`, `Bước thực hiện (Steps)`, `Kết quả mong đợi (UI/API/DB)`, `Notes / Defect ID`.
   * Schema 8 cột `Requirements_Analysis`: `Requirement ID`, `Analyzed At`, `Requirement Text`, `Business Rules`, `Questions for BA`, `Possible Risks`, `Related Bugs`, `Key Decisions Log`.
   * Enterprise Styling: Header Ant Design Blue `#1677FF`, chữ trắng in đậm, cao 45px, đóng băng dòng 1 (`frozenRowCount = 1`), wrap text, Dropdown Data Validation (`NOT_RUN`, `PASS`, `FAIL`, `BLOCKED`), và Conditional Formatting màu sắc nổi bật.
4. **Finalize Metadata:**
   * Query the latest `modifiedTime` from Drive and update `data/.sync_metadata.json`.
   * Provide the clickable Google Spreadsheet link to the tester.

