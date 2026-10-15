"""MCP Google Workspace Client Helper."""
from typing import List, Dict, Any
from datetime import datetime

from config.settings import SPREADSHEET_ID, GOOGLE_ACCOUNT_EMAIL, TAB_REQUIREMENTS_ANALYSIS, TAB_TEST_SPECIFICATION
from schemas.analysis_models import AnalysisResult
from schemas.test_case_models import TestCaseSpecification


class MCPWorkspaceFormatter:
    """Formats analysis results and test specifications into structured 2D arrays for Google Sheets."""

    @staticmethod
    def format_analysis_row(analysis: AnalysisResult) -> List[str]:
        """Formats an AnalysisResult into a single row for the Requirements_Analysis tab."""
        rules_text = "\n".join(f"• {r}" for r in analysis.business_rules)
        questions_text = "\n".join(f"• {q}" for q in analysis.questions_for_ba)
        risks_text = "\n".join(f"• {r}" for r in analysis.possible_risks) if hasattr(analysis, "possible_risks") else ""
        bugs_text = "\n".join(f"[{b.bug_id}]: {b.reason}" for b in analysis.related_bugs)
        decisions_text = "\n".join(f"- {d}" for d in analysis.key_decisions_log) if analysis.key_decisions_log else "Chốt bởi Tester"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return [
            analysis.requirement_id or "REQ_UNSET",
            timestamp,
            analysis.requirement_text,
            rules_text,
            questions_text,
            risks_text,
            bugs_text,
            decisions_text
        ]

    @staticmethod
    def format_test_case_rows(test_cases: List[TestCaseSpecification]) -> List[List[str]]:
        """Formats a list of TestCaseSpecification into 2D rows for the Test_Cases_Specification tab."""
        rows = []
        for tc in test_cases:
            steps_text = "\n".join(f"Bước {s.step_number}: {s.action_and_input}" for s in tc.steps)
            expected_text = "\n".join(f"Kỳ vọng {s.step_number}: {s.expected_result}" for s in tc.steps)
            rows.append([
                tc.requirement_id,
                tc.test_case_id,
                tc.scenario_name,
                tc.test_type,
                tc.priority,
                tc.priority_reason,
                steps_text,
                expected_text
            ])
        return rows
