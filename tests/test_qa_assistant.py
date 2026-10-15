"""Automated tests for QA Requirement Assistant (Compatible with both unittest and pytest)."""
import unittest
from schemas.session_context import SessionState
from agents.orchestrator import QAOrchestrator
from tools.bug_retrieval_tool import BugRetrievalTool


class TestQARequirementAssistant(unittest.TestCase):
    """Test suite covering the 6 core criteria of the QA Assistant."""

    def setUp(self):
        self.orchestrator = QAOrchestrator()

    def test_1_state_machine_sequential_transition(self):
        """Test 1: Verify strict 2-Phase state machine flow with Human-in-the-loop gates."""
        req = "Người dùng được phép hủy đơn hàng trong vòng 5 phút kể từ khi thanh toán thành công nếu đơn hàng chưa chuyển sang trạng thái PROCESSING."

        # 1. Start Session
        analysis = self.orchestrator.start_session(req)
        self.assertEqual(self.orchestrator.context.current_state, SessionState.WAITING_TESTER_PHASE_1)
        self.assertGreaterEqual(len(analysis.business_rules), 1)
        self.assertGreaterEqual(len(analysis.questions_for_ba), 1)
        self.assertGreaterEqual(len(analysis.possible_risks), 1)
        self.assertGreaterEqual(len(analysis.related_bugs), 1)

        # 2. Gate 1: Confirm Phase 1
        test_cases = self.orchestrator.confirm_phase_1_and_generate_tests()
        self.assertEqual(self.orchestrator.context.current_state, SessionState.WAITING_TESTER_PHASE_2)
        self.assertGreaterEqual(len(test_cases), 5)

        # 3. Gate 2: Confirm & Export
        analysis_row, test_rows = self.orchestrator.confirm_and_export_payload()
        self.assertEqual(self.orchestrator.context.current_state, SessionState.SYNCED)
        self.assertEqual(len(analysis_row), 8)
        self.assertGreaterEqual(len(test_rows), 5)

    def test_2_human_gate_blocks_premature_test_generation(self):
        """Test 2: Ensure test cases CANNOT be generated prematurely before Phase 1 is started."""
        with self.assertRaises(ValueError):
            self.orchestrator.confirm_phase_1_and_generate_tests()

    def test_3_bug_correlation_engine(self):
        """Test 3: Verify accurate correlation with historical bug catalog (BUG-001 -> BUG-005)."""
        tool = BugRetrievalTool()

        # Cancel order -> BUG-001 and BUG-002
        bugs_cancel = tool.find_related_bugs("Hủy đơn hàng sau khi thanh toán và kiểm tra trạng thái kho")
        bug_ids_cancel = [b.bug_id for b in bugs_cancel]
        self.assertIn("BUG-001", bug_ids_cancel)
        self.assertIn("BUG-002", bug_ids_cancel)

        # Voucher -> BUG-003
        bugs_voucher = tool.find_related_bugs("Mỗi voucher chỉ được sử dụng một lần trên mỗi tài khoản")
        bug_ids_voucher = [b.bug_id for b in bugs_voucher]
        self.assertIn("BUG-003", bug_ids_voucher)

        # Stock / Inventory -> BUG-005
        bugs_stock = tool.find_related_bugs("Người dùng không được đặt mua số lượng sản phẩm lớn hơn số lượng tồn kho")
        bug_ids_stock = [b.bug_id for b in bugs_stock]
        self.assertIn("BUG-005", bug_ids_stock)

    def test_4_generated_test_specification_has_at_least_5_cases(self):
        """Test 4: Verify test specification generates at least 5 prioritized simulated test cases."""
        req = "Tài khoản bị khóa sau 5 lần nhập sai mật khẩu liên tiếp."
        self.orchestrator.start_session(req)
        test_cases = self.orchestrator.confirm_phase_1_and_generate_tests()

        self.assertGreaterEqual(len(test_cases), 5)
        types = [tc.test_type for tc in test_cases]
        self.assertIn("Happy Path", types)
        self.assertIn("Boundary Value", types)
        self.assertIn("Negative", types)
        self.assertIn("Concurrency", types)

        for tc in test_cases:
            self.assertGreaterEqual(len(tc.steps), 1)
            self.assertNotEqual(tc.steps[0].action_and_input, "")
            self.assertNotEqual(tc.steps[0].expected_result, "")

    def test_5_context_rollback_on_requirement_change(self):
        """Test 5: Verify context rollback and cleanup of downstream tests when requirement changes."""
        self.orchestrator.start_session("Hủy đơn hàng trong 5 phút.")
        self.orchestrator.confirm_phase_1_and_generate_tests()
        self.assertGreater(len(self.orchestrator.context.test_cases), 0)
        self.assertEqual(self.orchestrator.context.current_state, SessionState.WAITING_TESTER_PHASE_2)

        # Rollback
        new_req = "Hủy đơn hàng trong 15 phút chỉ áp dụng cho thẻ tín dụng."
        self.orchestrator.rollback_to_phase_1(new_req)

        self.assertEqual(self.orchestrator.context.current_state, SessionState.WAITING_TESTER_PHASE_1)
        self.assertEqual(len(self.orchestrator.context.test_cases), 0)
        self.assertEqual(self.orchestrator.context.raw_requirement, new_req)

    def test_6_mcp_payload_formatting_integrity(self):
        """Test 6: Verify data integrity and foreign-key linking for Google Sheets sync."""
        self.orchestrator.start_session("Mỗi voucher chỉ được sử dụng một lần trên mỗi tài khoản.")
        self.orchestrator.confirm_phase_1_and_generate_tests()
        analysis_row, test_rows = self.orchestrator.confirm_and_export_payload()

        req_id = analysis_row[0]
        self.assertTrue(req_id.startswith("REQ_"))
        self.assertIn("Mỗi voucher", analysis_row[2])

        for row in test_rows:
            foreign_key = row[0]
            test_case_id = row[1]
            self.assertEqual(foreign_key, req_id)
            self.assertTrue(test_case_id.startswith("TC_"))


if __name__ == "__main__":
    unittest.main()
