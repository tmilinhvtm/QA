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
         │          • Ask sharp Questions for BA (timing window, rollback lifecycle, failure modes)
         │          • Analyze 5 Technical Risks using [Risk Checklist](./references/risk-checklist.md)
         │          • Correlate with historical bugs read from local `data/bug_repository.json`
         │
         ├───► [GATE 1] Await Tester Confirmation (Human-in-the-loop checkpoint)
         │
         ├───► Pillar 2: Prioritized Simulated Test Specification (Invoke 'test-automation-architect')
         │          • Generate 5 mandatory scenario types from [Test Design Matrix](./references/test-design-matrix.md)
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

### Step 1: Phase 1 Analysis (Subagent `req-risk-analyst`)
1. Extract raw requirement text and load the current perspective preference from `data/user_preferences.json`.
2. Delegate to subagent `req-risk-analyst` via `invoke_subagent`:
   * Provide the validated bug list from `data/bug_repository.json`.
   * Pass the active `analysis_perspective` to adapt the tone, terminology, and depth (e.g. functional explanations for `business`, deep architecture terms for `technical`, balanced dual-section for `hybrid`).
   * **Technical Risk Analysis:** Consult [Risk Checklist](./references/risk-checklist.md) for 5 dimensions (*Concurrency, State Drift, Clock Drift, Non-idempotency, Distributed Transaction Failure*).
3. Output the 4 mandatory sections:
   * **1. Business Rules** (Pre-condition, Trigger, Constraints, Post-condition)
   * **2. Questions for BA** (Logic gaps, edge cases, latency, compensation flows)
   * **3. Possible Risks** (5 technical risk dimensions tailored to the requirement)
   * **4. Related Historical Bugs** (Đối chiếu ngữ nghĩa với các bug patterns từ local `data/bug_repository.json`)
4. **STOP AND PROMPT TESTER:**
   Ask the tester: *"Bạn xem các điểm phân tích trên đã chuẩn chưa, có cần điều chỉnh gì trước khi tiến hành thiết kế bộ kịch bản Automation Test không?"*
   **DO NOT GENERATE TEST CASES YET.**

### Step 2: Handle Tester Feedback (Human Gate 1)
* If tester provides critiques, adjustments, or additional constraints:
  * Update analysis and re-present.
* If tester modifies the requirement scope entirely:
  * Invalidate downstream context and restart Phase 1.
* Only when tester confirms ("ok", "chốt", "tiếp tục"):
  * Proceed to Step 3.

### Step 3: Phase 2 Test Specification (Subagent `test-automation-architect`)
1. Pass the finalized Phase 1 context to subagent `test-automation-architect`.
2. Follow the [Test Design Matrix](./references/test-design-matrix.md) to generate at least 5 test cases:
   * `TC_xxx_001`: **Happy Path** (P1)
   * `TC_xxx_002`: **Boundary Value** (P2)
   * `TC_xxx_003`: **Negative Path** (P1)
   * `TC_xxx_004`: **Concurrency / Race Condition** (P1)
   * `TC_xxx_005`: **State Conflict / Recovery** (P2)
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
   * Append/upsert the 5 new structured test cases into `data/test_cases_specification.json` (Tuyệt đối KHÔNG overwrite/reset xóa các test cases cũ).
3. **Push Accumulative Changes to Google Spreadsheet & Apply Styling:**
   * Run sync script: `python3 .agents/skills/qa-requirement-assistant/scripts/google_sheets_sync_manager.py sync_all`.
   * Script sẽ tự động kiểm tra các dòng hiện có trên Google Sheet và **ghi nối tiếp (append rows)** các bản ghi mới vào cuối bảng tính mà không bao giờ xóa hay làm trắng sheet (`never clear`).
   * Schema 10 cột `Test_Cases_Specification`: `Requirement ID`, `Test Case ID`, `Scenario Name`, `Test Type`, `Priority`, `Status (Pass/Fail)`, `Pre-conditions`, `Bước thực hiện (Steps)`, `Kết quả mong đợi (UI/API/DB)`, `Notes / Defect ID`.
   * Schema 8 cột `Requirements_Analysis`: `Requirement ID`, `Analyzed At`, `Requirement Text`, `Business Rules`, `Questions for BA`, `Possible Risks`, `Related Bugs`, `Key Decisions Log`.
   * Enterprise Styling: Header Ant Design Blue `#1677FF`, chữ trắng in đậm, cao 45px, đóng băng dòng 1 (`frozenRowCount = 1`), wrap text, Dropdown Data Validation (`NOT_RUN`, `PASS`, `FAIL`, `BLOCKED`), và Conditional Formatting màu sắc nổi bật.
4. **Finalize Metadata:**
   * Query the latest `modifiedTime` from Drive and update `data/.sync_metadata.json`.
   * Provide the clickable Google Spreadsheet link to the tester.

