"""Interactive CLI for Requirement QA Assistant."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config.settings import SPREADSHEET_URL, SPREADSHEET_ID
from schemas.session_context import SessionState
from agents.orchestrator import QAOrchestrator


def print_banner():
    print("=" * 80)
    print("🚀 REQUIREMENT QA ASSISTANT — SPECIALIZED AGENT SYSTEM")
    print(f"📊 Google Master Sheet: {SPREADSHEET_URL}")
    print("=" * 80)


def display_phase_1(analysis):
    print("\n" + "─" * 80)
    print("📋 [PHASE 1] KẾT QUẢ PHÂN TÍCH NGHIỆP VỤ & RỦI RO (Subagent 1)")
    print("─" * 80)
    print("\n📌 1. BUSINESS RULES (Quy tắc nghiệp vụ):")
    for r in analysis.business_rules:
        print(f"  • {r}")

    print("\n❓ 2. QUESTIONS FOR BA (Câu hỏi chất vấn BA / PO):")
    for q in analysis.questions_for_ba:
        print(f"  • {q}")

    print("\n⚠️ 3. POSSIBLE RISKS (Rủi ro kỹ thuật sâu):")
    for rk in analysis.possible_risks:
        print(f"  • {rk}")

    print("\n🐞 4. RELATED HISTORICAL BUGS (Bug lịch sử đối chiếu):")
    if analysis.related_bugs:
        for b in analysis.related_bugs:
            print(f"  • [{b.bug_id}] {b.description}")
            print(f"    ↳ Lý do liên quan: {b.reason}")
    else:
        print("  • Chưa phát hiện bug tương quan trực tiếp.")

    if analysis.key_decisions_log:
        print("\n📝 GHI CHÚ ĐIỀU CHỈNH CỦA TESTER:")
        for d in analysis.key_decisions_log:
            print(f"  - {d}")
    print("─" * 80)


def display_phase_2(test_cases):
    print("\n" + "─" * 80)
    print(f"🧪 [PHASE 2] BỘ KỊCH BẢN AUTOMATION TEST GIẢ LẬP ({len(test_cases)} Test Cases) (Subagent 2)")
    print("─" * 80)
    for tc in test_cases:
        print(f"\n🔹 {tc.test_case_id}: {tc.scenario_name}")
        print(f"   Loại test: {tc.test_type} | Độ ưu tiên: {tc.priority}")
        print(f"   Lý do xếp hạng: {tc.priority_reason}")
        print("   Các bước giả lập & Kết quả mong muốn:")
        for s in tc.steps:
            print(f"     Step {s.step_number}: [Hành động] {s.action_and_input}")
            print(f"             ↳ [Kỳ vọng] {s.expected_result}")
    print("─" * 80)


def run_interactive_session():
    print_banner()
    orchestrator = QAOrchestrator()

    print("\n💡 Mời Tester nhập Requirement cần phân tích:")
    req = input("> ").strip()
    if not req:
        print("Requirement không được để trống!")
        return

    # Phase 1
    analysis = orchestrator.start_session(req)
    display_phase_1(analysis)

    # Gate 1 Loop
    while orchestrator.context.current_state == SessionState.WAITING_TESTER_PHASE_1:
        print("\n👉 Tester làm gì tiếp theo?")
        print("   - Gõ 'ok' hoặc 'chot': Xác nhận Phase 1 và kích hoạt sinh Automation Test.")
        print("   - Gõ nội dung phản biện/bổ sung: Để Agent tinh chỉnh lại phân tích.")
        action = input("> ").strip()
        if not action:
            continue

        if action.lower() in ["ok", "chot", "chốt", "tiep", "tiếp"]:
            print("\n⏳ Đang chuyển giao Context sang Subagent 2 (Test Automation Architect)...")
            test_cases = orchestrator.confirm_phase_1_and_generate_tests()
            display_phase_2(test_cases)
            break
        else:
            print(f"\n⏳ Đang ghi nhận phản biện '{action}' và tái phân tích...")
            analysis = orchestrator.refine_phase_1(action)
            display_phase_1(analysis)

    # Gate 2 Loop
    while orchestrator.context.current_state == SessionState.WAITING_TESTER_PHASE_2:
        print("\n👉 Tester làm gì tiếp theo?")
        print("   - Gõ 'export' hoặc 'luu': Đóng gói dữ liệu và xuất sang Google Sheets.")
        print("   - Gõ 'rollback': Hủy bỏ test cases và quay lại Phase 1 sửa requirement.")
        action = input("> ").strip()
        if not action:
            continue

        if action.lower() in ["export", "luu", "lưu", "sync"]:
            analysis_row, test_rows = orchestrator.confirm_and_export_payload()
            print("\n🎉 ĐÃ ĐÓNG GÓI THÀNH CÔNG DỮ LIỆU ĐỂ SYNC LÊN GOOGLE DRIVE:")
            print(f"   • Mã Requirement: {orchestrator.context.requirement_id}")
            print(f"   • Số lượng Test Cases: {len(test_rows)}")
            print(f"   • Google Sheet Master: {SPREADSHEET_URL}")
            break
        elif action.lower() in ["rollback", "quay lai"]:
            print("\n🔄 Đang rollback về Phase 1. Nhập requirement mới (hoặc bấm Enter để giữ cũ):")
            new_r = input("> ").strip()
            analysis = orchestrator.rollback_to_phase_1(new_r if new_r else None)
            display_phase_1(analysis)
            break


if __name__ == "__main__":
    run_interactive_session()
