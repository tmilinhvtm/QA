"""Script to run analysis on Sample + Req A, B, C and produce rows for Google Sheets."""
import json
from agents.orchestrator import QAOrchestrator

REQUIREMENTS = [
    {
        "id": "REQ_SAMPLE_CANCEL_01",
        "text": "Người dùng được phép hủy đơn hàng trong vòng 5 phút kể từ khi thanh toán thành công nếu đơn hàng chưa chuyển sang trạng thái PROCESSING.",
        "note": "Xác nhận tính theo Server Timestamp; bổ sung kiểm tra hoàn voucher và webhook kho vận."
    },
    {
        "id": "REQ_A_AUTH_LOCK_01",
        "text": "Tài khoản bị khóa sau 5 lần nhập sai mật khẩu liên tiếp.",
        "note": "Bổ sung cơ chế reset counter về 0 khi nhập đúng ở lần 4; kiểm tra tấn công Brute-force đa luồng."
    },
    {
        "id": "REQ_B_STOCK_LIMIT_01",
        "text": "Người dùng không được đặt mua số lượng sản phẩm lớn hơn số lượng tồn kho.",
        "note": "Bổ sung kiểm tra Concurrency khi 2 khách cùng mua món hàng cuối cùng (Overselling); liên hệ BUG-005."
    },
    {
        "id": "REQ_C_VOUCHER_ONCE_01",
        "text": "Mỗi voucher chỉ được sử dụng một lần trên mỗi tài khoản.",
        "note": "Bổ sung Distributed Lock chống race-condition 2 tab trình duyệt checkout đồng thời; liên hệ BUG-003."
    }
]

def generate_all_payloads():
    all_analysis_rows = []
    all_test_rows = []

    for item in REQUIREMENTS:
        orch = QAOrchestrator()
        orch.context.requirement_id = item["id"]
        orch.start_session(item["text"])
        orch.refine_phase_1(item["note"])
        test_cases = orch.confirm_phase_1_and_generate_tests()
        a_row, t_rows = orch.confirm_and_export_payload()
        all_analysis_rows.append(a_row)
        all_test_rows.extend(t_rows)

    return all_analysis_rows, all_test_rows

if __name__ == "__main__":
    a_rows, t_rows = generate_all_payloads()
    print(f"Generated {len(a_rows)} analysis rows and {len(t_rows)} test case rows.")
    with open("payload_cache.json", "w", encoding="utf-8") as f:
        json.dump({"analysis_rows": a_rows, "test_rows": t_rows}, f, ensure_ascii=False, indent=2)
