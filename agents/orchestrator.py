"""Master Agent: QA Orchestrator."""
import uuid
from typing import Optional, List, Tuple
from datetime import datetime

from schemas.session_context import SessionContext, SessionState
from schemas.analysis_models import AnalysisResult
from schemas.test_case_models import TestCaseSpecification
from agents.req_risk_analyst import RequirementRiskAnalyst
from agents.test_architect import TestAutomationArchitect
from tools.mcp_workspace_client import MCPWorkspaceFormatter


class QAOrchestrator:
    """Master Orchestrator managing session lifecycle, state gates, subagents, and persistence."""

    def __init__(self, analyst: RequirementRiskAnalyst = None, architect: TestAutomationArchitect = None):
        self.analyst = analyst or RequirementRiskAnalyst()
        self.architect = architect or TestAutomationArchitect()
        self.context = SessionContext(session_id=str(uuid.uuid4())[:8])

    def start_session(self, requirement_text: str) -> AnalysisResult:
        """Entrypoint: Receives raw requirement, starts Phase 1 analysis, and transitions to WAITING_TESTER_PHASE_1."""
        self.context.raw_requirement = requirement_text.strip()
        self.context.current_state = SessionState.PHASE_1_ANALYSIS

        # Run Subagent 1
        analysis = self.analyst.analyze(self.context.raw_requirement)
        self.context.analysis = analysis
        self.context.current_state = SessionState.WAITING_TESTER_PHASE_1
        return analysis

    def refine_phase_1(self, feedback: str) -> AnalysisResult:
        """Refines Phase 1 analysis based on Tester's critique and feedback."""
        if self.context.current_state != SessionState.WAITING_TESTER_PHASE_1:
            raise ValueError(f"Không thể chỉnh sửa Phase 1 khi đang ở trạng thái {self.context.current_state}")

        # Record decision log and re-analyze or augment
        if not self.context.analysis.key_decisions_log:
            self.context.analysis.key_decisions_log = []
        self.context.analysis.key_decisions_log.append(feedback)

        # Trigger Subagent 1 refinement
        self.context.analysis = self.analyst.analyze(
            self.context.raw_requirement,
            custom_notes=self.context.analysis.key_decisions_log
        )
        return self.context.analysis

    def confirm_phase_1_and_generate_tests(self) -> List[TestCaseSpecification]:
        """Human Gate 1: Tester confirms Phase 1. Transitions to PHASE_2_TEST_GEN and generates test specification."""
        if self.context.current_state != SessionState.WAITING_TESTER_PHASE_1:
            raise ValueError("Chưa hoàn tất hoặc chưa ở trạng thái chờ duyệt Phase 1!")

        self.context.current_state = SessionState.PHASE_2_TEST_GEN

        # Generate unique requirement ID if not set
        if not self.context.requirement_id:
            date_str = datetime.now().strftime("%Y%m%d")
            self.context.requirement_id = f"REQ_{date_str}_{self.context.session_id.upper()}"
        
        self.context.analysis.requirement_id = self.context.requirement_id

        # Trigger Subagent 2
        test_cases = self.architect.generate_test_specification(self.context.analysis)
        for tc in test_cases:
            tc.requirement_id = self.context.requirement_id
        self.context.test_cases = test_cases
        self.context.current_state = SessionState.WAITING_TESTER_PHASE_2
        return test_cases

    def rollback_to_phase_1(self, new_requirement: Optional[str] = None) -> AnalysisResult:
        """Rollbacks session state to Phase 1 when requirement changes, clearing downstream test cases."""
        if new_requirement:
            self.context.raw_requirement = new_requirement.strip()
        self.context.test_cases = []
        self.context.current_state = SessionState.PHASE_1_ANALYSIS

        analysis = self.analyst.analyze(self.context.raw_requirement)
        self.context.analysis = analysis
        self.context.current_state = SessionState.WAITING_TESTER_PHASE_1
        return analysis

    def confirm_and_export_payload(self) -> Tuple[List[str], List[List[str]]]:
        """Human Gate 2: Tester approves test specification. Prepares payload for Google Sheets via MCP."""
        if self.context.current_state != SessionState.WAITING_TESTER_PHASE_2:
            raise ValueError("Kịch bản test chưa được tạo hoặc chưa ở trạng thái chờ duyệt Phase 2!")

        # Format payload using MCP formatter
        analysis_row = MCPWorkspaceFormatter.format_analysis_row(self.context.analysis)
        test_case_rows = MCPWorkspaceFormatter.format_test_case_rows(self.context.test_cases)

        self.context.current_state = SessionState.SYNCED
        return analysis_row, test_case_rows
