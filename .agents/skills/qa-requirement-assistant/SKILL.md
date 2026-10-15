---
name: qa-requirement-assistant
description: >-
  Use this skill whenever the user or tester provides a software requirement, user story,
  or feature description and asks to analyze business rules, identify risks, match historical bugs from Google Drive via MCP,
  or design prioritized simulated automation test specifications synced to Google Drive.
---

# QA Requirement Assistant Framework

This skill guides the AI Agent to act as a **Lead QA Engineer & Agent Orchestrator** managing requirement decomposition, risk discovery via specialized reference manuals, live historical bug retrieval from Google Drive, human-in-the-loop validation gates, and prioritized automated test design.

---

## 🏛️ The 3 Pillars of Execution

```text
[Requirement Input]
         │
         ├───► Pillar 1: Static Requirement & Risk Analysis (Invoke 'req-risk-analyst')
         │          • Decompose 4 Business Rules: Pre-condition, Trigger, Constraints, Post-condition
         │          • Ask sharp Questions for BA (timing window, rollback lifecycle, failure modes)
         │          • Analyze 5 Technical Risks using [Risk Checklist](./references/risk-checklist.md)
         │          • Query LIVE bugs from Google Drive via MCP `read_sheet_values` ('Bug_Repository!A2:D')
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
         └───► Pillar 3: Cloud Workspace Synchronization (Google Workspace MCP)
                    • Generate unique `requirement_id`
                    • Sync to Google Spreadsheet via `google-workspace` MCP tool `modify_sheet_values`
                    • Maintain foreign-key traceability between Analysis and Test Cases
```

---

## 📋 Step-by-Step Execution Workflow

### Step 1: Phase 1 Analysis (Subagent `req-risk-analyst`)
1. Extract the raw requirement text.
2. Delegate to subagent `req-risk-analyst` via `invoke_subagent` or execute using:
   * **Technical Risk Analysis:** Consult [Risk Checklist](./references/risk-checklist.md) for 5 dimensions (*Concurrency, State Drift, Clock Drift, Non-idempotency, Distributed Transaction Failure*).
   * **Live Bug Retrieval from Google Drive:** Call tool `google-workspace:read_sheet_values`:
     * `spreadsheet_id`: `1BG5HNlQBEqyG_hjM9WwklrME2lZbysNFHBSggsSQetk`
     * `range_name`: `Bug_Repository!A2:D`
     * `user_google_email`: `tmi.linhvtm@gmail.com`
     * Read live bug rows dynamically and perform semantic domain matching.
3. Output the 4 mandatory sections:
   * **1. Business Rules**
   * **2. Questions for BA**
   * **3. Possible Risks**
   * **4. Related Historical Bugs (queried live from Google Drive)**
4. **STOP AND PROMPT TESTER:**
   Ask the tester: *"Bạn xem các điểm phân tích trên đã chuẩn chưa, có cần điều chỉnh gì trước khi tiến hành thiết kế bộ kịch bản Automation Test không?"*
   **DO NOT GENERATE TEST CASES YET.**

### Step 2: Handle Tester Feedback (Human Gate 1)
* If tester provides critiques, adjustments, or additional constraints (e.g., voucher rules, server timestamps):
  * Update `key_decisions_log`.
  * Re-evaluate risks and re-present the updated Phase 1 analysis.
* If tester modifies the requirement scope entirely:
  * Invalidate any downstream context and restart Phase 1.
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
3. For each test case, describe:
   * Test Case ID & Scenario Name
   * Test Type & Priority (P1/P2/P3 with explicit justification)
   * Simulated Steps: Action, Input Payload, Simulated Endpoint
   * Expected Results: HTTP Status, DB Record State, Event Bus Message
4. **STOP AND PROMPT TESTER:**
   Ask the tester: *"Bạn duyệt bộ kịch bản test này chưa? Nếu đồng ý, tôi sẽ tạo mã requirement_id và đồng bộ toàn bộ lên Google Drive qua MCP."*

### Step 4: Sync to Google Workspace Spreadsheet via MCP
1. Assign `requirement_id` (format: `REQ_<YYYYMMDD>_<ID>`).
2. Call MCP `google-workspace` tool `modify_sheet_values`:
   * Append 1 row to `Requirements_Analysis` tab.
   * Append 5+ rows to `Test_Cases_Specification` tab (with `requirement_id` as foreign key).
3. Provide the direct clickable Google Spreadsheet link to the tester.
