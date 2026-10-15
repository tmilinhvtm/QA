# Antigravity Rules: QA Requirement Assistant Protocol

Whenever the user or tester asks to analyze a requirement, review business rules, or generate test cases, you MUST follow this protocol:

## 1. The Strict 2-Phase State Machine
The workflow consists of two sequential phases separated by mandatory human checkpoints:

```text
[Input Requirement]
        │
        ▼
[PHASE 1: Requirement & Risk Analysis]
        │
        ▼
[HUMAN GATE 1: Tester Critique & Approval] ◄── STOP! Do not generate test cases!
        │
        ▼
[PHASE 2: Automation Test Design & Priority]
        │
        ▼
[HUMAN GATE 2: Tester Test Specification Approval]
        │
        ▼
[PHASE 3: Sync to Google Workspace Spreadsheet via MCP]
```

## 2. Non-Negotiable Rules

1. **No Premature Test Generation:**
   * NEVER generate test cases in the first turn.
   * You must complete Phase 1 first (Business Rules, Questions for BA, 5 Technical Risks, Related Historical Bugs).
   * Ask the user/tester to review and confirm Phase 1 before proceeding.

2. **Rollback on Requirement Change:**
   * If the user modifies, adds, or cancels requirements while in Phase 2 or between phases, immediately invalidate Phase 2 test cases.
   * Rollback the state to Phase 1 and re-analyze with the new scope.

3. **Subagent Delegation:**
   * Delegate Phase 1 analysis to the defined subagent `req-risk-analyst`.
   * Delegate Phase 2 test generation to the defined subagent `test-automation-architect`.

4. **Persistence & Traceability:**
   * Every analysis must have a unique `requirement_id` (e.g. `REQ_20261015_001`).
   * Every generated test case must reference `requirement_id` as a foreign key.
   * Persist directly to Google Spreadsheet via `google-workspace` MCP tools (`modify_sheet_values`).
