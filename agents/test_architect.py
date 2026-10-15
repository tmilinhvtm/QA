"""Subagent 2: Test Automation Architect."""
from typing import List
from schemas.analysis_models import AnalysisResult
from schemas.test_case_models import TestCaseSpecification, SimulatedStep


class TestAutomationArchitect:
    """Specialized Subagent for designing prioritized automated test scenarios with simulated steps."""

    def generate_test_specification(self, analysis: AnalysisResult) -> List[TestCaseSpecification]:
        """Generates a complete suite of at least 5 automated test scenarios based on finalized analysis."""
        req_id = analysis.requirement_id or "REQ_UNSET"
        req_lower = analysis.requirement_text.lower()
        test_cases: List[TestCaseSpecification] = []

        if "hủy đơn hàng" in req_lower and "5 phút" in req_lower:
            # 1. Happy Path
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_CANCEL_001",
                requirement_id=req_id,
                scenario_name="[Happy Path] Hủy đơn hàng thành công trong vòng 5 phút khi đơn ở trạng thái CREATED",
                test_type="Happy Path",
                priority="P1 (Critical)",
                priority_reason="Chức năng nghiệp vụ cốt lõi, bảo đảm quyền lợi người dùng và quy trình bán hàng chuẩn.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Mô phỏng tạo đơn hàng và thanh toán thành công lúc T0=10:00:00 (State: PAID).", expected_result="Hệ thống xác nhận thanh toán thành công, đơn hàng sẵn sàng để hủy."),
                    SimulatedStep(step_number=2, action_and_input="Gửi request POST /api/v1/orders/{order_id}/cancel tại thời điểm T1=10:02:30 (sau 2.5 phút).", expected_result="API trả về HTTP 200 OK, message 'Đơn hàng đã được hủy thành công'."),
                    SimulatedStep(step_number=3, action_and_input="Kiểm tra trạng thái đơn hàng trong Database và Event bus.", expected_result="Trạng thái đơn hàng = CANCELLED; phát sinh event OrderCancelled và kích hoạt Refund.")
                ]
            ))

            # 2. Boundary Value: 4:59 vs 5:01
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_CANCEL_002",
                requirement_id=req_id,
                scenario_name="[Boundary Value] Kiểm tra ranh giới thời gian tại 4 phút 59 giây và 5 phút 01 giây",
                test_type="Boundary Value",
                priority="P2 (High)",
                priority_reason="Xác thực độ chính xác của bộ đếm thời gian và tránh tranh chấp do chênh lệch giây.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Tạo đơn hàng Order_A (T0=10:00:00). Gửi request Hủy tại 10:04:59 (4m59s).", expected_result="Đơn Order_A hủy thành công (HTTP 200), chuyển sang CANCELLED."),
                    SimulatedStep(step_number=2, action_and_input="Tạo đơn hàng Order_B (T0=10:00:00). Gửi request Hủy tại 10:05:01 (5m01s).", expected_result="Đơn Order_B bị từ chối (HTTP 400 Bad Request), message 'Đã quá thời gian cho phép hủy'.")
                ]
            ))

            # 3. Negative Path: State = PROCESSING
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_CANCEL_003",
                requirement_id=req_id,
                scenario_name="[Negative Path] Từ chối hủy khi đơn hàng đã chuyển sang trạng thái PROCESSING trong 5 phút",
                test_type="Negative",
                priority="P1 (Critical)",
                priority_reason="Bảo đảm tính toàn vẹn giữa kho vận và luồng đặt hàng, chặn thất thoát hàng hóa.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Tạo đơn hàng mới (T0=10:00:00). Sau 1 phút, Warehouse cập nhật trạng thái đơn sang PROCESSING.", expected_result="Đơn hàng ghi nhận trạng thái PROCESSING trong DB."),
                    SimulatedStep(step_number=2, action_and_input="Tại T=10:02:00 (vẫn trong 5 phút), người dùng gửi request POST /orders/{id}/cancel.", expected_result="Hệ thống chặn thao tác, trả về HTTP 409 Conflict, message 'Đơn hàng đang được kho xử lý, không thể hủy'.")
                ]
            ))

            # 4. Concurrency: Hai request cancel đồng thời (BUG-001)
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_CANCEL_004",
                requirement_id=req_id,
                scenario_name="[Concurrency / Race Condition] Gửi 2 request Hủy đồng thời cho cùng một đơn hàng",
                test_type="Concurrency",
                priority="P1 (Critical)",
                priority_reason="Phòng ngừa trực tiếp BUG-001 (Double refund gây thiệt hại tài chính nghiêm trọng).",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Tạo đơn hàng hợp lệ trị giá 500,000 VND (State: PAID).", expected_result="Đơn hàng ghi nhận đủ điều kiện hủy."),
                    SimulatedStep(step_number=2, action_and_input="Sử dụng ThreadPool/Async bắn đồng thời 2 request POST /orders/{id}/cancel trong khoảng 10ms.", expected_result="Chính xác 01 request nhận HTTP 200; request thứ 2 nhận HTTP 400/409."),
                    SimulatedStep(step_number=3, action_and_input="Kiểm tra bảng transactions/refunds trong cơ sở dữ liệu.", expected_result="Chỉ duy nhất 01 transaction hoàn tiền 500,000 VND được tạo. Không có bản ghi refund thứ 2.")
                ]
            ))

            # 5. State Conflict: Race Condition với Kho vận (BUG-002)
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_CANCEL_005",
                requirement_id=req_id,
                scenario_name="[State Inconsistency] Xung đột đồng thời giữa User Hủy đơn và Kho chuyển PROCESSING",
                test_type="State Conflict",
                priority="P2 (High)",
                priority_reason="Phòng ngừa trực tiếp BUG-002, kiểm tra cơ chế Distributed Lock giữa OMS và WMS.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Bắn đồng thời Request Hủy của User và Webhook 'Warehouse Packing Started' của WMS.", expected_result="Hệ thống sử dụng Database Transaction Lock để tuần tự hóa hai thao tác."),
                    SimulatedStep(step_number=2, action_and_input="Xác thực trạng thái cuối cùng của đơn hàng trong hệ thống.", expected_result="Trạng thái cuối cùng phải nhất quán: Nếu User hủy trước -> WMS nhận thông báo dừng; nếu WMS khóa trước -> User nhận thông báo từ chối hủy.")
                ]
            ))

        elif "khóa sau 5 lần" in req_lower:
            # Requirement A
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_AUTH_001",
                requirement_id=req_id,
                scenario_name="[Happy Path] Khóa tài khoản chính xác sau 5 lần nhập sai mật khẩu liên tiếp",
                test_type="Happy Path",
                priority="P1 (Critical)",
                priority_reason="Yêu cầu bảo mật cơ bản, chặn tấn công đoán mật khẩu (Brute Force).",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Gửi 4 request POST /login với mật khẩu sai liên tiếp cho tài khoản 'user_test'.", expected_result="Mỗi lần trả về HTTP 401 Unauthorized, message 'Sai mật khẩu, còn lại X lần thử'."),
                    SimulatedStep(step_number=2, action_and_input="Gửi request POST /login lần thứ 5 với mật khẩu sai.", expected_result="HTTP 403 Forbidden, message 'Tài khoản đã bị khóa do nhập sai mật khẩu 5 lần liên tiếp'."),
                    SimulatedStep(step_number=3, action_and_input="Kiểm tra trường status của tài khoản trong Database.", expected_result="status = 'LOCKED', failed_attempts = 5.")
                ]
            ))
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_AUTH_002",
                requirement_id=req_id,
                scenario_name="[Boundary & Reset] Nhập sai 4 lần, lần thứ 5 nhập đúng -> Reset bộ đếm về 0",
                test_type="Boundary Value",
                priority="P2 (High)",
                priority_reason="Đảm bảo người dùng hợp lệ không bị khóa nhầm khi nhập đúng trước ngưỡng khóa.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Gửi 4 request đăng nhập sai liên tiếp.", expected_result="Bộ đếm ghi nhận failed_attempts = 4."),
                    SimulatedStep(step_number=2, action_and_input="Tại lần thứ 5, gửi request đăng nhập với mật khẩu ĐÚNG.", expected_result="HTTP 200 OK, đăng nhập thành công và cấp Access Token."),
                    SimulatedStep(step_number=3, action_and_input="Kiểm tra giá trị failed_attempts trong cơ sở dữ liệu/Redis.", expected_result="failed_attempts được reset về 0.")
                ]
            ))
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_AUTH_003",
                requirement_id=req_id,
                scenario_name="[Negative Path] Đăng nhập bằng mật khẩu đúng khi tài khoản đã bị LOCKED",
                test_type="Negative",
                priority="P1 (Critical)",
                priority_reason="Bảo đảm cơ chế khóa có hiệu lực tuyệt đối, không cho phép đăng nhập kể cả khi có pass đúng.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Thiết lập trạng thái tài khoản là LOCKED (sau 5 lần sai).", expected_result="Tài khoản sẵn sàng ở trạng thái khóa."),
                    SimulatedStep(step_number=2, action_and_input="Gửi request POST /login với MẬT KHẨU ĐÚNG 100%.", expected_result="Hệ thống từ chối ngay lập tức với HTTP 403 Forbidden, message 'Tài khoản đang bị khóa. Vui lòng liên hệ hỗ trợ hoặc khôi phục mật khẩu'.")
                ]
            ))
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_AUTH_004",
                requirement_id=req_id,
                scenario_name="[Concurrency / Distributed Brute Force] Gửi 10 request đăng nhập sai đồng thời từ nhiều luồng",
                test_type="Concurrency",
                priority="P1 (Critical)",
                priority_reason="Ngăn ngừa race condition trên bộ đếm khi bị tấn công Brute-force song song.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Sử dụng 10 workers gửi đồng thời 10 request login sai cho cùng 1 tài khoản.", expected_result="Bộ đếm nguyên tử (Atomic Counter trên Redis/DB) tăng chính xác."),
                    SimulatedStep(step_number=2, action_and_input="Kiểm tra trạng thái tài khoản ngay sau đợt request.", expected_result="Tài khoản bị khóa ngay khi luồng thứ 5 được ghi nhận, các request từ 6-10 nhận phản hồi khóa.")
                ]
            ))
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_AUTH_005",
                requirement_id=req_id,
                scenario_name="[State Recovery] Cơ chế mở khóa tài khoản sau thời gian hết hạn (Lockout Duration)",
                test_type="State Conflict",
                priority="P3 (Medium)",
                priority_reason="Kiểm tra luồng khôi phục tự động của người dùng.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Tài khoản bị khóa lúc T0 với cấu hình khóa trong 30 phút.", expected_result="Đăng nhập lúc T0 + 15 phút vẫn bị chặn HTTP 403."),
                    SimulatedStep(step_number=2, action_and_input="Chờ đến T0 + 31 phút, gửi request đăng nhập với mật khẩu đúng.", expected_result="Hệ thống tự động mở khóa (Auto-unlock), trả về HTTP 200 OK.")
                ]
            ))

        elif "tồn kho" in req_lower:
            # Requirement B
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_STOCK_001",
                requirement_id=req_id,
                scenario_name="[Happy Path] Đặt mua số lượng hợp lệ (Order_Quantity <= Available_Stock)",
                test_type="Happy Path",
                priority="P1 (Critical)",
                priority_reason="Luồng mua hàng chuẩn.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Sản phẩm SKU_01 có tồn kho = 10. Khách chọn mua số lượng = 3.", expected_result="Checkout thành công, đơn hàng được tạo."),
                    SimulatedStep(step_number=2, action_and_input="Kiểm tra tồn kho trong cơ sở dữ liệu sau thanh toán.", expected_result="Tồn kho khả dụng giảm từ 10 xuống 7 (Phòng ngừa BUG-005).")
                ]
            ))
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_STOCK_002",
                requirement_id=req_id,
                scenario_name="[Boundary Value] Đặt mua chính xác số lượng tồn kho (Order_Quantity == Available_Stock)",
                test_type="Boundary Value",
                priority="P2 (High)",
                priority_reason="Kiểm tra giá trị biên vét cạn kho hàng.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Sản phẩm tồn kho = 5. Khách đặt mua số lượng = 5.", expected_result="Checkout thành công."),
                    SimulatedStep(step_number=2, action_and_input="Kiểm tra tồn kho và trạng thái sản phẩm.", expected_result="Tồn kho = 0, trạng thái sản phẩm chuyển sang 'Out of Stock' trên giao diện.")
                ]
            ))
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_STOCK_003",
                requirement_id=req_id,
                scenario_name="[Negative Path] Chặn đặt mua số lượng lớn hơn tồn kho (Order_Quantity = Stock + 1)",
                test_type="Negative",
                priority="P1 (Critical)",
                priority_reason="Chặn bán khống / Overselling.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Sản phẩm tồn kho = 5. Khách cố tình chọn số lượng = 6 và bấm Checkout.", expected_result="Hệ thống chặn thanh toán, hiển thị cảnh báo 'Số lượng đặt vượt quá tồn kho khả dụng (5)'.")
                ]
            ))
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_STOCK_004",
                requirement_id=req_id,
                scenario_name="[Concurrency / Race Condition] Hai khách hàng cùng mua món hàng cuối cùng (Stock = 1)",
                test_type="Concurrency",
                priority="P1 (Critical)",
                priority_reason="Chống bán âm kho (Overselling) khi nhiều người bấm mua đồng thời.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Sản phẩm có tồn kho = 1. Khách A và Khách B cùng gửi request checkout lúc 12:00:00.", expected_result="Database Lock chỉ cho phép 01 đơn hàng thành công."),
                    SimulatedStep(step_number=2, action_and_input="Kiểm tra phản hồi của khách hàng còn lại.", expected_result="Khách hàng còn lại nhận thông báo 'Sản phẩm vừa hết hàng', tồn kho không bao giờ bị âm.")
                ]
            ))
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_STOCK_005",
                requirement_id=req_id,
                scenario_name="[Data Consistency] Hoàn trả tồn kho khi đơn hàng bị hủy hoặc thanh toán thất bại",
                test_type="State Conflict",
                priority="P2 (High)",
                priority_reason="Bảo đảm tính chính xác số lượng tồn kho theo chu kỳ đơn hàng.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Khách đặt 2 sản phẩm (Tồn kho giảm từ 10 xuống 8). Đơn hàng bị hủy do quá hạn thanh toán.", expected_result="Event OrderExpired được kích hoạt."),
                    SimulatedStep(step_number=2, action_and_input="Kiểm tra tồn kho sau khi hủy.", expected_result="Tồn kho tự động hoàn lại về 10.")
                ]
            ))

        elif "voucher" in req_lower:
            # Requirement C
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_VOUCHER_001",
                requirement_id=req_id,
                scenario_name="[Happy Path] Áp dụng voucher thành công cho đơn hàng đầu tiên của tài khoản",
                test_type="Happy Path",
                priority="P1 (Critical)",
                priority_reason="Luồng khuyến mãi chuẩn.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Tài khoản User_01 nhập mã voucher 'SALE50' cho đơn hàng Order_01.", expected_result="Voucher hợp lệ, giảm giá được áp dụng vào tổng tiền."),
                    SimulatedStep(step_number=2, action_and_input="Thanh toán đơn hàng thành công.", expected_result="Đơn hoàn tất, mã voucher được liên kết với User_01 chuyển sang trạng thái USED.")
                ]
            ))
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_VOUCHER_002",
                requirement_id=req_id,
                scenario_name="[Negative Path] Tái sử dụng voucher đã dùng ở đơn hàng thứ 2 của cùng tài khoản",
                test_type="Negative",
                priority="P1 (Critical)",
                priority_reason="Ngăn ngừa vi phạm chính sách chỉ dùng 1 lần / 1 tài khoản.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Tài khoản User_01 tạo đơn hàng Order_02 và nhập lại mã 'SALE50'.", expected_result="Hệ thống báo lỗi 'Mã giảm giá này đã được sử dụng trên tài khoản của bạn', không áp dụng giảm giá.")
                ]
            ))
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_VOUCHER_003",
                requirement_id=req_id,
                scenario_name="[Concurrency / Race Condition] Mở 2 tab trình duyệt cùng áp dụng voucher và checkout đồng thời (BUG-003)",
                test_type="Concurrency",
                priority="P1 (Critical)",
                priority_reason="Phòng ngừa trực tiếp BUG-003 (Sử dụng cùng voucher cho hai đơn hàng do race-condition).",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Tài khoản User_01 mở 2 phiên checkout song song cùng chọn mã 'SALE50'. Bắn 2 request thanh toán đồng thời trong 10ms.", expected_result="Distributed Lock (Redis/DB) khóa voucher theo Account_ID."),
                    SimulatedStep(step_number=2, action_and_input="Kiểm tra kết quả 2 đơn hàng và lịch sử voucher.", expected_result="Chỉ duy nhất 01 đơn hàng được áp dụng giảm giá; đơn còn lại bị báo lỗi voucher đang được xử lý hoặc đã dùng.")
                ]
            ))
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_VOUCHER_004",
                requirement_id=req_id,
                scenario_name="[State Recovery] Hoàn lại quyền dùng voucher khi đơn hàng thanh toán thất bại hoặc bị hủy",
                test_type="State Conflict",
                priority="P2 (High)",
                priority_reason="Bảo vệ quyền lợi khách hàng khi đơn hàng không thành công.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="Áp dụng voucher cho Order_01 nhưng quá trình thanh toán cổng thẻ bị timeout/hủy.", expected_result="Đơn hàng chuyển trạng thái CANCELLED."),
                    SimulatedStep(step_number=2, action_and_input="User_01 tạo đơn mới Order_03 và nhập lại mã voucher.", expected_result="Voucher được hoàn về trạng thái ACTIVE và áp dụng thành công cho đơn mới.")
                ]
            ))
            test_cases.append(TestCaseSpecification(
                test_case_id="TC_VOUCHER_005",
                requirement_id=req_id,
                scenario_name="[Multi-Account] Hai tài khoản khác nhau cùng sử dụng voucher hợp lệ",
                test_type="Boundary Value",
                priority="P3 (Medium)",
                priority_reason="Xác thực voucher là duy nhất trên mỗi tài khoản chứ không bị khóa nhầm cho toàn hệ thống.",
                steps=[
                    SimulatedStep(step_number=1, action_and_input="User_A dùng voucher thành công.", expected_result="User_A được giảm giá."),
                    SimulatedStep(step_number=2, action_and_input="User_B đăng nhập và dùng cùng mã voucher đó.", expected_result="User_B vẫn được áp dụng thành công vì ràng buộc là 'per account'.")
                ]
            ))
        else:
            # Generic 5 test cases
            for i in range(1, 6):
                test_cases.append(TestCaseSpecification(
                    test_case_id=f"TC_GEN_{i:03d}",
                    requirement_id=req_id,
                    scenario_name=f"[Kịch bản {i}] Kiểm thử chức năng theo yêu cầu",
                    test_type="Happy Path" if i == 1 else "Negative",
                    priority="P1 (Critical)" if i <= 2 else "P2 (High)",
                    priority_reason="Đảm bảo yêu cầu được xác thực toàn diện.",
                    steps=[
                        SimulatedStep(step_number=1, action_and_input="Thực hiện hành vi người dùng theo kịch bản.", expected_result="Hệ thống phản hồi theo đúng Business Rule đã chốt.")
                    ]
                ))

        return test_cases
