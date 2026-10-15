"""Subagent 1: Requirement & Risk Analyst."""
from typing import List
from schemas.analysis_models import AnalysisResult, BugCorrelation
from tools.bug_retrieval_tool import BugRetrievalTool


class RequirementRiskAnalyst:
    """Specialized Subagent for requirement decomposition, risk forecasting, and historical bug matching."""

    def __init__(self, bug_tool: BugRetrievalTool = None):
        self.bug_tool = bug_tool or BugRetrievalTool()

    def analyze(self, requirement_text: str, custom_notes: List[str] = None) -> AnalysisResult:
        """Performs deep static analysis on the requirement text."""
        req_clean = requirement_text.strip()
        req_lower = req_clean.lower()

        # 1. Decompose Business Rules
        rules = []
        if "hủy đơn hàng" in req_lower and "5 phút" in req_lower:
            rules.append("Khoảng thời gian hủy: Đơn hàng chỉ được phép hủy trong vòng 300 giây (5 phút) kể từ thời điểm thanh toán thành công.")
            rules.append("Ràng buộc trạng thái: Chỉ cho phép hủy khi đơn hàng ở trạng thái trước PROCESSING (ví dụ: PAID, CREATED).")
            rules.append("Xử lý sau hủy: Sau khi hủy thành công, giao dịch phải được đánh dấu CANCELLED và kích hoạt luồng hoàn tiền (Refund).")
        elif "khóa sau 5 lần" in req_lower or ("mật khẩu" in req_lower and "5 lần" in req_lower):
            rules.append("Ràng buộc đếm: Hệ thống đếm số lần nhập sai mật khẩu liên tiếp; đạt ngưỡng 5 lần thì chuyển trạng thái tài khoản sang LOCKED.")
            rules.append("Điều kiện liên tiếp: Nếu nhập đúng mật khẩu ở lần thứ 1..4, bộ đếm sai mật khẩu phải được reset về 0.")
            rules.append("Chặn đăng nhập: Khi tài khoản đã ở trạng thái LOCKED, mọi yêu cầu đăng nhập tiếp theo đều bị từ chối ngay lập tức.")
        elif "tồn kho" in req_lower and ("số lượng" in req_lower or "đặt mua" in req_lower):
            rules.append("Ràng buộc số lượng: Số lượng sản phẩm khách đặt mua (Order_Quantity) phải nhỏ hơn hoặc bằng số lượng tồn kho khả dụng (Available_Stock).")
            rules.append("Chặn đặt hàng: Nếu Order_Quantity > Available_Stock, hệ thống phải chặn checkout và hiển thị thông báo lỗi vượt quá tồn kho.")
            rules.append("Khóa tồn kho: Tại thời điểm đặt hàng/thanh toán, hệ thống phải trừ hoặc giữ (hold) đúng số lượng tồn kho tương ứng.")
        elif "voucher" in req_lower:
            rules.append("Ràng buộc duy nhất: Mỗi mã voucher chỉ được áp dụng thành công tối đa 01 lần cho mỗi tài khoản người dùng (Account_ID).")
            rules.append("Kiểm tra hợp lệ: Tại thời điểm áp dụng và checkout, hệ thống phải kiểm tra lịch sử đơn hàng của tài khoản để bảo đảm voucher chưa từng được dùng.")
            rules.append("Trạng thái voucher: Khi đơn hàng hoàn tất, voucher gắn với tài khoản đó phải chuyển sang trạng thái USED.")
        else:
            rules.append(f"Quy tắc cốt lõi: Hệ thống bắt buộc tuân thủ điều kiện nêu trong requirement: '{req_clean}'.")
            rules.append("Ràng buộc tiền điều kiện: Người dùng phải đáp ứng đủ quyền hạn và trạng thái hợp lệ để thực thi hành động.")

        # 2. Extract Questions for BA / PO
        questions = []
        if "5 phút" in req_lower:
            questions.append("Thời gian 5 phút được tính theo Server Timestamp hay Client Device Timestamp? Cơ chế xử lý trường hợp Network Latency (request gửi lúc 4:59 nhưng server nhận lúc 5:01) là gì?")
            questions.append("Khi đơn hàng bị hủy, tiền được hoàn qua cổng thanh toán ban đầu hay hoàn vào ví nội bộ/điểm thưởng? Thời gian hoàn tiền là bao lâu?")
            questions.append("Nếu đơn hàng có áp dụng Voucher giảm giá, voucher có được hoàn lại và giữ nguyên hạn sử dụng cho khách hàng không?")
        elif "khóa sau 5 lần" in req_lower:
            questions.append("Cơ chế mở khóa tài khoản là gì: Tự động mở sau khoảng thời gian X phút (Timeout Lock) hay bắt buộc Admin can thiệp / Reset qua Email-OTP?")
            questions.append("Bộ đếm 5 lần có được áp dụng độc lập theo từng IP/thiết bị hay gắn chặt theo Username/Account ID (đề phòng tấn công Brute-force phân tán)?")
            questions.append("Hệ thống có gửi thông báo cảnh báo (Email/SMS) cho chủ tài khoản khi nhập sai ở lần thứ 3 hoặc khi tài khoản bị khóa không?")
        elif "tồn kho" in req_lower:
            questions.append("Cơ chế giữ tồn kho (Stock Hold): Tồn kho được trừ tại thời điểm người dùng 'Thêm vào giỏ', 'Bấm Đặt hàng', hay 'Thanh toán thành công'?")
            questions.append("Thời gian giữ chỗ tồn kho (Hold Expiration) là bao lâu nếu người dùng chưa hoàn tất thanh toán?")
            questions.append("Nếu 2 người cùng đặt mua món hàng cuối cùng tại cùng một thời điểm (Race Condition), hệ thống ưu tiên đơn nào và xử lý đơn còn lại ra sao?")
        elif "voucher" in req_lower:
            questions.append("Nếu người dùng mở 2 tab trình duyệt hoặc gửi 2 request checkout đồng thời với cùng 1 voucher, cơ chế Distributed Lock xử lý thế nào?")
            questions.append("Nếu đơn hàng sử dụng voucher bị Hủy hoặc Trả hàng, voucher có được hoàn lại về trạng thái UNUSED để dùng tiếp không?")
            questions.append("Voucher có giới hạn kết hợp với các chương trình khuyến mãi khác không?")
        else:
            questions.append("Cơ chế xử lý khi có lỗi kết nối mạng giữa chừng hoặc lỗi từ dịch vụ phụ thuộc thứ 3 là gì?")
            questions.append("Thông báo lỗi cụ thể hiển thị trên giao diện người dùng (UI/UX error message) là gì?")

        # 3. Forecast Technical Risks
        risks = []
        if "hủy" in req_lower or "cancel" in req_lower:
            risks.append("Race Condition giữa User và Kho: Khách hàng nhấn Hủy đúng lúc kho vận chuyển trạng thái sang PROCESSING -> Xung đột trạng thái (State Conflict).")
            risks.append("Double Cancel Request: Người dùng click đúp hoặc tool bắn 2 request Hủy đồng thời -> Nguy cơ hoàn tiền 2 lần (Trùng với BUG-001).")
            risks.append("Clock Drift: Lệch giờ giữa máy chủ ứng dụng (App Server) và máy chủ cơ sở dữ liệu (DB Server) dẫn đến tính sai mốc 5 phút.")
        elif "mật khẩu" in req_lower:
            risks.append("Distributed Brute Force: Kẻ tấn công sử dụng nhiều IP khác nhau cùng thử mật khẩu của một tài khoản -> Bộ đếm cần đồng bộ tập trung trên Redis thay vì memory cục bộ.")
            risks.append("Race Condition trên Bộ đếm: Nhiều request đăng nhập sai gửi cùng lúc dẫn đến dirty read / counter bị đếm thiếu.")
        elif "tồn kho" in req_lower:
            risks.append("Overselling (Bán vượt tồn kho): Race condition khi nhiều người dùng cùng checkout sản phẩm cuối cùng nếu không có Pessimistic/Optimistic Lock ở tầng Database.")
            risks.append("Distributed Transaction Failure: Tạo đơn hàng thành công nhưng cập nhật tồn kho thất bại -> Lỗi không nhất quán dữ liệu (Trùng với BUG-005).")
        elif "voucher" in req_lower:
            risks.append("Race Condition / Double Spending: Cùng một voucher được dùng cho 2 đơn hàng song song trên 2 phiên thanh toán khác nhau (Trùng với BUG-003).")
            risks.append("Voucher Leak: Voucher bị đánh dấu đã dùng dù giao dịch thanh toán cuối cùng bị thất bại.")
        else:
            risks.append("Non-idempotency: Hành động được kích hoạt nhiều lần dẫn đến dữ liệu bị sai lệch.")

        # 4. Correlate with Historical Bugs
        related_bugs = self.bug_tool.find_related_bugs(requirement_text)

        return AnalysisResult(
            requirement_text=req_clean,
            business_rules=rules,
            questions_for_ba=questions,
            possible_risks=risks,
            related_bugs=related_bugs,
            key_decisions_log=custom_notes or []
        )
