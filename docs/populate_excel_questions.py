#!/usr/bin/env python3
"""
populate_excel_questions.py
Populates the Google Spreadsheet 'Interview QA - Tester Data & Automation' (ID: 1lTZIfQ_6V_bLWI6J5f066C-pGx1zIED_D9t7cj1MxOs)
with comprehensive questions, challenges, and answers for AI in QA, Data Accuracy, and 3-Month Effort Scaling.
"""

import json
import os
import sys

# Data rows
ROWS = [
    # -------------------------------------------------------------
    # PHẦN 1: 10 CÂU HỎI PHỎNG VẤN TRỌNG TÂM
    # -------------------------------------------------------------
    [
        "Câu 1",
        "Câu hỏi phỏng vấn",
        "Đo lường & Đánh giá Tính Đúng Sai của Bộ Dữ Liệu AI trả ra (Data Accuracy & Ground Truth)",
        "Team chúng tôi đánh giá chất lượng vị trí này dựa trên 'tính đúng sai của bộ dữ liệu do AI trả ra'. Bạn định nghĩa 'đúng - sai' ở đây như thế nào? Quy trình đo lường định lượng và các chỉ số (metrics) cụ thể bạn sẽ áp dụng để chứng minh bộ dữ liệu test sinh ra là chuẩn xác?",
        "1. Đánh giá tư duy thiết kế khung đo lường chất lượng dữ liệu AI (Data Quality Framework).\n2. Phân biệt rõ giữa cú pháp (syntax) và ngữ nghĩa nghiệp vụ (semantics).\n3. Phương pháp xây dựng Ground Truth / Golden Dataset để benchmark định kỳ.\n4. Red Flags: Chỉ trả lời chung chung 'review bằng mắt' mà không có công thức, threshold hoặc tầng kiểm tra tự động.",
        "1. Khung Đo Lường Chất Lượng Dữ Liệu 3 Tầng:\n"
        "- Tầng 1: Cú pháp & Cấu trúc (Schema Validity - Mục tiêu 100%):\n"
        "  + Dùng Rule-based / Pydantic Validator kiểm tra tự động: Kịch bản có bị gom cụm bước không? Có đủ 3 tầng kỳ vọng (UI, API JSON Body, DB assertion) không? Khóa `requirement_id` có hợp lệ không?\n"
        "  + Nếu vi phạm bất kỳ tiêu chí cấu trúc nào -> Đánh giá FAIL ngay lập tức.\n"
        "- Tầng 2: Ngữ nghĩa & Nghiệp vụ (Semantic Accuracy - Mục tiêu ≥ 92%):\n"
        "  + Đo lường trên bộ 'Golden Dataset' (Tập 50 User Story chuẩn đã có sẵn đáp án do Lead QA và PO phê duyệt).\n"
        "  + Precision (Độ chuẩn): Tỷ lệ các quy tắc và kịch bản test AI sinh ra thực sự đúng và có giá trị.\n"
        "  + Recall (Độ bao phủ): Tỷ lệ các ràng buộc biên (boundary) và rủi ro bắt buộc được phát hiện đầy đủ.\n"
        "- Tầng 3: Kiểm soát Ảo giác (Hallucination Rate - Mục tiêu < 5%):\n"
        "  + Tỷ lệ các trường hợp AI tự suy diễn API endpoint không có thật, hoặc tự bịa ra logic mâu thuẫn với requirement gốc.\n\n"
        "2. Cơ Chế Kiểm Định Thực Tế:\n"
        "- Áp dụng Strict 2-Phase State Machine: Chặn ở Human Gate 1 (Tester chốt logic nghiệp vụ) trước khi cho phép sinh test case ở Phase 2, triệt tiêu nguy cơ rác lan truyền sang kịch bản test."
    ],
    [
        "Câu 2",
        "Câu hỏi phỏng vấn",
        "Chiến lược Nâng Effort (Throughput) Team QA gấp 2.5x trong 3 Tháng",
        "Mục tiêu cam kết của vị trí này là trong 3 tháng phải nâng 'effort' của team lên rõ rệt. Bạn hiểu 'nâng effort' ở đây là gì? Hãy trình bày kế hoạch hành động chi tiết 30-60-90 ngày để tăng năng suất làm việc của cả đội ngũ mà không làm giảm chất lượng kiểm thử?",
        "1. Hiểu đúng bản chất của Effort: Tăng dung lượng xử lý (Capacity / Throughput) và giảm lead-time trên mỗi User Story.\n2. Lộ trình triển khai 3 giai đoạn khả thi, có mốc thời gian (milestones) và KPIs định lượng.\n3. Năng lực kết hợp giữa công cụ AI và quy trình Agile/Scrum của doanh nghiệp.\n4. Red Flags: Đưa ra lời hứa mơ hồ, không có số liệu đo lường giờ làm việc tiết kiệm được.",
        "1. Định nghĩa Nâng Effort:\n"
        "- Không phải bắt tester làm thêm giờ (OT), mà là NÂNG DUNG LƯỢNG XỬ LÝ (Throughput) của team lên gấp 2.5x: từ trung bình 2-3 stories/sprint lên 6-8 stories/sprint trên mỗi QA nhờ giải phóng 60-70% thời gian soạn thảo thủ công.\n\n"
        "2. Lộ Trình Hành Động 90 Ngày:\n"
        "- Tháng 1 (Foundation & Baseline):\n"
        "  + Xây dựng Golden Dataset 50 stories chuẩn làm thước đo Ground Truth.\n"
        "  + Đóng gói Agentic Plugin (Rules, Skills, Subagents) và Pilot trên 1 Scrum Team (3-5 QA).\n"
        "  + KPI Tháng 1: Độ chính xác dữ liệu ≥ 85%, giảm 40% thời gian viết test case ban đầu, phát hiện sớm 5 lỗi logic ở khâu requirement.\n"
        "- Tháng 2 (Integration & Ecosystem Scaling):\n"
        "  + Tích hợp Jira/Xray MCP: Tự động đọc ticket từ Jira, sync kết quả lên Xray/Google Sheets mà không cần copy-paste tay.\n"
        "  + Thêm cơ chế Feedback Loop (Upvote/Downvote) để prompt tự tiến hóa theo văn hóa cty.\n"
        "  + Mở rộng ra toàn bộ 10-15 QA. KPI Tháng 2: Độ chính xác ≥ 92%, giảm 60% lead-time phân tích.\n"
        "- Tháng 3 (Autonomous Multiplier & ROI Report):\n"
        "  + Tự động chuyển đổi kịch bản giả lập 3 tầng thành code Playwright / k6 chạy trực tiếp trên CI/CD.\n"
        "  + KPI Tháng 3: Nâng Throughput team lên GẤP 2.5X, giảm 50% bug lọt sang Prod, tiết kiệm 15-20 man-hours/QA/sprint."
    ],
    [
        "Câu 3",
        "Câu hỏi phỏng vấn",
        "Kỹ thuật Triệt tiêu Ảo giác (Hallucination Control) & Grounding Tri Thức",
        "Ảo giác (Hallucination) là rào cản lớn nhất khiến các team QA mất niềm tin vào AI (AI tự bịa tham số API, suy diễn sai quy tắc nghiệp vụ). Bạn đã áp dụng những kỹ thuật kiến trúc nào trong dự án của mình để khống chế tỷ lệ ảo giác dưới 5%?",
        "1. Kỹ năng thiết kế Prompting & Agent Architecture cấp cao (không dùng prompt ngây thơ).\n2. Áp dụng các nguyên lý: Strict Knowledge Grounding, Decoupling, Progressive Disclosure.\n3. Khả năng thiết lập quy tắc phủ định tất định (Deterministic Negative Constraints).\n4. Red Flags: Tin tưởng hoàn toàn vào model hoặc chỉ dùng câu lệnh chung chung 'hãy cẩn thận đừng nói dối'.",
        "1. 4 Kỹ Thuật Triệt Tiêu Ảo Giác Trong Repo:\n"
        "- Kỹ thuật 1 - Strict Knowledge Grounding (Neo giữ tri thức xác thực):\n"
        "  + Agent bị giới hạn nghiêm ngặt trong 3 tài liệu chuẩn: Cẩm nang 5 góc khuất (`risk-checklist.md`), Ma trận 5 loại kịch bản (`test-design-matrix.md`), và Kho 10 Bug Lịch Sử thực tế (`bug_repository.json`). Tuyệt đối không để AI tự do suy diễn ngoài Internet.\n"
        "- Kỹ thuật 2 - 2-Phase Decoupling (Tách rời 2 pha độc lập):\n"
        "  + Cấm tuyệt đối việc sinh test case ở lượt đầu tiên. Bắt buộc hoàn thành Phase 1 (bóc tách Business Rules & câu hỏi phản biện BA), dừng lại ở Human Gate 1 chờ Tester duyệt.\n"
        "- Kỹ thuật 3 - Progressive Disclosure (Tối ưu Context Window):\n"
        "  + Bóc tách cẩm nang kỹ thuật vào thư mục `references/`, chỉ nạp khi cần tra cứu thay vì nhồi nhét mega-prompt làm loãng context dẫn đến ảo giác.\n"
        "- Kỹ thuật 4 - Deterministic Negative Constraints (Quy tắc phủ định tất định):\n"
        "  + Luật cứng trong `AGENTS.md`: Cấm gom cụm bước, cấm chỉ ghi HTTP Status chung chung mà thiếu JSON Body hoặc bảng Database."
    ],
    [
        "Câu 4",
        "Câu hỏi phỏng vấn",
        "3 Nguyên Tắc Vàng QA/QC Thực Chiến & Tại sao phải Step Disaggregation?",
        "Trong repo bạn nêu '3 Nguyên Tắc Vàng Chuẩn QA/QC Thực Chiến', đặc biệt nhấn mạnh 'Step Disaggregation (Tách bước độc lập)'. Tại sao việc tách bước này lại quan trọng đến vậy đối với đội ngũ Automation và việc bảo trì kịch bản test?",
        "1. Kinh nghiệm thực chiến sâu sắc về Automation Testing (Playwright, Selenium, Cypress).\n2. Hiểu rõ nguyên nhân gốc khiến các kịch bản test tự động bị 'flaky' hoặc khó debug.\n3. Tiêu chuẩn đặc tả kết quả kỳ vọng 3 tầng (UI, API Body, Database/Broker).\n4. Red Flags: Cho rằng viết test dồn bước cho ngắn gọn là tốt.",
        "1. Tầm Quan Trọng Của Step Disaggregation (Nguyên Tắc 1):\n"
        "- Lỗi kinh điển của AI là dồn hành động: 'Người dùng chọn số lượng = 3, chọn thanh toán COD, bấm nút Đặt hàng'.\n"
        "- Hậu quả: Khi chạy Automation, nếu test case FAIL, tester/dev hoàn toàn không biết lỗi do UI không chọn được số lượng, do radio button thanh toán hỏng, hay do API checkout timeout.\n"
        "- Chuẩn hóa: Đưa tiền đề vào Pre-conditions; Bước 1 là chuẩn bị dữ liệu; Bước 2 là click trigger. Đảm bảo tính nguyên tử (atomic), xác định đúng 100% vị trí lỗi khi debug.\n\n"
        "2. Synchronized Deep Verification 3 Tầng (Nguyên Tắc 2):\n"
        "- Không bao giờ dừng lại ở 'HTTP 200'. Bắt buộc kiểm tra 3 tầng:\n"
        "  + UI: Thông báo, màu sắc viền cảnh báo, mã đơn hiển thị.\n"
        "  + API: HTTP Status kèm trường dữ liệu cốt lõi trong Response Body (`order_id` phải khớp với UI).\n"
        "  + Database & Event: Tên bảng, tên cột, giá trị biến động (ví dụ `orders.status = 'PENDING'`, tồn kho giảm từ 10 xuống 7), và Kafka Event phát ra.\n\n"
        "3. Execution Status Rõ Ràng (Nguyên Tắc 3):\n"
        "- Mặc định là `NOT_RUN`, đi kèm Data Validation Dropdown (Pass/Fail/Blocked) và Conditional Formatting trên Google Sheets."
    ],
    [
        "Câu 5",
        "Câu hỏi phỏng vấn",
        "Agent Topology & Những Khâu Chủ Động KHÔNG Giao Cho AI",
        "Trong kiến trúc hệ thống của bạn, có phần nào bạn CHỦ ĐỘNG KHÔNG GIAO CHO AI không? Tại sao một kỹ sư AI QA Lead lại cần nắm quyền kiểm soát những khâu đó thay vì để AI tự động hóa 100%?",
        "1. Nhận thức trưởng thành về ranh giới giữa Tự động hóa (Automation) và Kiểm soát con người (Governance).\n2. Năng lực thiết kế cấu trúc tác tử (Agent Topology) phù hợp với quy trình kiểm thử thực tế.\n3. Tư duy quản trị rủi ro chất lượng phần mềm.\n4. Red Flags: Ảo tưởng 'Full Autopilot' không cần con người can thiệp.",
        "1. 3 Khâu Cốt Lõi Chủ Động KHÔNG Giao Cho AI:\n"
        "- Khâu 1: Thiết kế Kiến trúc Tác tử & Phân quyền (Agent Topology):\n"
        "  + AI không thể tự quyết định nên chia bao nhiêu Subagents và ranh giới trách nhiệm thế nào. Tôi trực tiếp phân chia 2 Subagents độc lập: `req-risk-analyst` (chỉ phân tích tĩnh) và `test-automation-architect` (chỉ thiết kế test sau khi Gate 1 duyệt) để tránh xung đột ngữ cảnh.\n"
        "- Khâu 2: Cổng Phê Duyệt Quyết Định Nghiệp Vụ (Human Gates):\n"
        "  + AI chỉ đóng vai trò 'Suggester' (Người đề xuất), Tester là 'Gatekeeper' (Người ra quyết định). Việc chốt xem quy tắc nghiệp vụ đã đủ chưa và kịch bản test có đạt chuẩn đưa vào sprint không bắt buộc phải có sự xác nhận của Tester tại Gate 1 và Gate 2.\n"
        "- Khâu 3: Nguồn Tri Thức Chuẩn Hóa (Authoritative Sources):\n"
        "  + Kho bug lịch sử (`data/bug_repository.json`), tài liệu API và bảng giá cước phải do con người kiểm duyệt và cung cấp, tuyệt đối không để AI tự ý tìm kiếm lung tung trên mạng."
    ],
    [
        "Câu 6",
        "Câu hỏi phỏng vấn",
        "Cơ Chế Rollback & Quản Lý Tính Nhất Quán Khi Requirement Thay Đổi",
        "Trong môi trường Agile, requirement thường xuyên bị thay đổi giữa chừng (ví dụ: BA đổi quy định từ khóa tài khoản sau 5 lần sai thành 3 lần sai khi bạn đang thiết kế test case). Hệ thống của bạn xử lý tình huống này thế nào để tránh sai lệch dữ liệu?",
        "1. Khả năng thiết kế State Machine có cơ chế quản lý vòng đời và vô hiệu hóa trạng thái (State Invalidation).\n2. Tư duy chống ô nhiễm dữ liệu kiểm thử (Test Pollution).\n3. Hiểu rõ sự nguy hiểm của việc giữ context cũ khi requirement đã đổi.",
        "1. Cơ Chế Rollback Tất Định (Rule 4 trong AGENTS.md):\n"
        "- Khi người dùng/tester thay đổi, bổ sung hoặc hủy bỏ requirement khi đang ở Phase 2 hoặc giữa các pha:\n"
        "  + Hệ thống NGAY LẬP TỨC VÔ HIỆU HÓA (Invalidate) toàn bộ các test case đã sinh ở Phase 2.\n"
        "  + Rollback toàn bộ trạng thái trở về Phase 1 để bóc tách lại Business Rules, cập nhật lại Questions for BA và rà soát lại 5 rủi ro kỹ thuật theo phạm vi mới.\n"
        "  + Chỉ khi Tester duyệt lại Phase 1 mới, Phase 2 mới được kích hoạt tái tạo kịch bản.\n\n"
        "2. Ý Nghĩa Thực Tế:\n"
        "- Ngăn chặn triệt để tình trạng 'Kịch bản test râu ông nọ cắm cằm bà kia' — lỗi rất phổ biến khi QA chat tự do với ChatGPT mà không có cơ chế quản lý trạng thái."
    ],
    [
        "Câu 7",
        "Câu hỏi phỏng vấn",
        "Perspective Persistence: Giải Quyết Rào Cản Giao Tiếp Giữa BA và SDET",
        "Trong repo có tính năng 'Perspective Preference & Persistence' (`user_preferences.json`). Tính năng này giải quyết vấn đề gì trong giao tiếp nội bộ giữa BA, QA và Developer?",
        "1. Kỹ năng giao tiếp đa đối tượng (Stakeholder Communication).\n2. Thấu hiểu tâm lý người dùng sản phẩm (User Adoption Barrier).\n3. Năng lực cá nhân hóa trải nghiệm AI cho từng vai trò trong dự án.",
        "1. Bài Toán Thực Tế:\n"
        "- Trong một Scrum Team, đối tượng đọc kết quả phân tích có 2 nhóm rất khác biệt:\n"
        "  + BA & Product Owner: Quan tâm luồng nghiệp vụ, trải nghiệm khách hàng. Nếu AI nói 'Race condition', 'Redis INCR', 'Lost update', họ sẽ cảm thấy xa lạ và bỏ qua phản biện.\n"
        "  + SDET & Backend Dev: Cần biết chính xác góc khuất kỹ thuật: Lock ở đâu, Distributed Transaction có rollback không, Token có bị revoke tức thì không.\n\n"
        "2. Giải Pháp Trong Repo:\n"
        "- Cấu hình `user_preferences.json` hỗ trợ 3 chế độ:\n"
        "  + `business`: Chuyển hóa rủi ro thành câu chuyện đời sống dễ hiểu (ví dụ thay vì nói 'Lost Update', giải thích 'Kẻ gian spam nhiều mật khẩu cùng lúc khiến hệ thống đếm sót và không khóa tài khoản').\n"
        "  + `technical`: Phân tích sâu kiến trúc phân tán cho SDET.\n"
        "  + `hybrid`: Trình bày song song cả hai.\n"
        "- Tự động ghi nhớ cấu hình qua các phiên, không bắt người dùng phải cấu hình lại mỗi lần chat."
    ],
    [
        "Câu 8",
        "Câu hỏi phỏng vấn",
        "Local-First & Bidirectional Sync: Bảo Toàn Dữ Liệu Tích Lũy Bền Vững",
        "Tại sao bạn lại chọn kiến trúc 'Local-First' kết hợp đồng bộ 2 chiều với Google Sheets qua MCP thay vì dùng Database truyền thống? 'Accumulative Append-Only' mang lại lợi ích gì cho việc quản trị tri thức kiểm thử?",
        "1. Hiểu biết về kiến trúc dữ liệu phân tán (Local-First Architecture).\n2. Quản trị tính toàn vẹn dữ liệu (Data Integrity, Disaster Recovery).\n3. Khả năng tích hợp công cụ văn phòng doanh nghiệp (Google Workspace MCP).",
        "1. Lợi Ích Của Local-First:\n"
        "- Zero Downtime: Dữ liệu requirement và test case luôn được lưu ở local (`data/`) trước. Nếu mất mạng hoặc API Google Drive gặp sự cố, tester vẫn làm việc bình thường, hệ thống tự động fallback đọc từ local cache.\n"
        "- Tối ưu hóa API Call: Tệp `.sync_metadata.json` lưu `modifiedTime` trên Drive. Đầu phiên chỉ gọi 1 request kiểm tra timestamp; nếu không đổi thì đọc local, tránh gọi API Drive liên tục gây chậm.\n\n"
        "2. Giá Trị Của Accumulative Append-Only:\n"
        "- Cấm tuyệt đối lệnh `clear()` làm trắng bảng tính. Mọi requirement và test case mới đều được cấp mã `requirement_id` duy nhất và ghi nối tiếp vào cuối bảng.\n"
        "- Google Spreadsheet trở thành một KHO TRI THỨC KIỂM THỬ TÍCH LŨY XUYÊN SUỐT (Cumulative Test Repository) của toàn công ty, phục vụ việc tra cứu và audit sau này."
    ],
    [
        "Câu 9",
        "Câu hỏi phỏng vấn",
        "Đào Tạo & Chuẩn Hóa Ứng Dụng AI Cho Toàn Bộ Đội Ngũ QA Trong 90 Ngày",
        "Nếu được tuyển dụng, làm thế nào bạn đào tạo và chuyển giao năng lực ứng dụng AI cho 10-15 tester trong công ty để đảm bảo năng lực của team không bị phụ thuộc vào một cá nhân?",
        "1. Kỹ năng lãnh đạo kỹ thuật và chuyển giao tri thức (Leadership & Knowledge Transfer).\n2. Xây dựng tài liệu quy chuẩn (SOP, Prompt Library, Definition of Done).\n3. Kế hoạch đào tạo thực tế, có phương pháp kèm cặp (Pair Testing).",
        "1. Lộ Trình Chuyển Giao 90 Ngày:\n"
        "- Tuần 1-2: Khảo sát kỹ năng hiện tại của team QA; ban hành tài liệu 'SOP: Tiêu chuẩn Ứng dụng AI trong Kiểm thử Phần mềm' (quy định rõ bảo mật PII, 3 Nguyên Tắc Vàng).\n"
        "- Tuần 3-6: Xây dựng Thư viện Prompt chuẩn (Prompt Library) trên Confluence; tổ chức chuỗi Workshop thực hành hàng tuần trên User Story thật của sprint.\n"
        "- Tuần 7-10: Áp dụng cơ chế 'Pair Testing' (Tester có thế mạnh AI kèm tester chưa quen); tích hợp công cụ vào quy trình làm việc chuẩn (Definition of Done - DoD).\n"
        "- Tuần 11-12: Đo lường và đánh giá: 100% QA trong team tự chủ phân tích requirement và sinh test case đạt chuẩn; không phụ thuộc vào cá nhân Lead."
    ],
    [
        "Câu 10",
        "Câu hỏi phỏng vấn",
        "Tính Toán ROI & Chứng Minh Hiệu Quả Đầu Tư AI Với Ban Giám Đốc",
        "Ban Giám đốc hỏi bạn: 'Làm sao chứng minh được việc áp dụng AI này mang lại lợi tức đầu tư (ROI) cụ thể bằng tiền hoặc thời gian cho doanh nghiệp?'. Bạn sẽ trình bày bài toán kinh tế này như thế nào?",
        "1. Tư duy kinh doanh (Business Acumen) của một cấp Lead/Specialist.\n2. Khả năng quy đổi hiệu quả kỹ thuật thành giá trị tài chính cụ thể.\n3. Đánh giá chi phí tổn thất chất lượng (Cost of Poor Quality).",
        "1. Bài Toán ROI Định Lượng Cụ Thể Sau 90 Ngày:\n"
        "- Tiết kiệm chi phí nhân công trực tiếp (Direct Man-hour Savings):\n"
        "  + Tiết kiệm 15-20 giờ làm việc/QA/sprint (tương đương 35-40 giờ/tháng/QA).\n"
        "  + Với team 10 QA, tiết kiệm khoảng 350-400 man-hours mỗi tháng — tương đương năng suất của 2-2.5 kỹ sư QA full-time (~40-50 triệu VNĐ/tháng chi phí nhân sự mà không phải tuyển mới).\n"
        "- Giảm thiểu chi phí sửa lỗi Production (Cost of Poor Quality):\n"
        "  + Chi phí sửa lỗi Race Condition, Bán âm kho hoặc Lỗi tính cước trên Prod đắt gấp 10-30 lần so với bắt ở khâu phân tích requirement.\n"
        "  + Việc phát hiện sớm các lỗ hổng như BUG-001, BUG-003 giúp doanh nghiệp tránh thiệt hại tài chính hàng trăm triệu đồng bồi hoàn khách hàng.\n"
        "- Rút ngắn Time-to-Market: Chu kỳ kiểm thử hồi quy giảm từ 3 ngày xuống dưới 4 giờ, giúp công ty phát hành tính năng mới nhanh hơn đối thủ ít nhất 1 tuần."
    ],

    # -------------------------------------------------------------
    # PHẦN 2: 6 VẤN ĐỀ KỸ THUẬT & THÁCH THỨC THỰC TẾ
    # -------------------------------------------------------------
    [
        "Vấn đề 1",
        "Vấn đề kỹ thuật / Thách thức",
        "Bẫy 'Garbage In - Garbage Out': Requirement Sơ Sài Khiến AI Sinh Kịch Bản Sai Lệch",
        "THÁCH THỨC: User Story của BA thường viết rất ngắn ngủi (ví dụ: 'Cho phép khách áp voucher giảm giá khi thanh toán'), không có Acceptance Criteria rõ ràng. Nếu đưa thẳng vào LLM thông thường, AI sẽ tự suy diễn các quy tắc không có thật, sinh test case sai hoàn toàn với logic hệ thống.",
        "1. Nhận diện nguyên nhân gốc của lỗi ảo giác nghiệp vụ.\n2. Phương pháp giải quyết bài toán thiếu thông tin đầu vào bằng AI.\n3. Tiêu chuẩn đánh giá câu hỏi chất vấn BA có trọng tâm hay không.",
        "GIẢI PHÁP KỸ THUẬT ĐÃ TRIỂN KHAI TRONG REPO:\n"
        "1. Cơ Chế Static Analysis & Đặt Câu Hỏi Phản Biện (Subagent 1 - `req-risk-analyst`):\n"
        "- Không vội sinh test case ngay. Agent tự động phân tích bóc tách 4 thành tố: Pre-condition, Trigger, Constraints, Post-condition.\n"
        "- Đặt ra danh sách 5-6 câu hỏi chất vấn BA sắc bén xoay quanh các vùng xám (Grey Areas):\n"
        "  + Voucher được chốt 'đã dùng' tại thời điểm nào (click Đặt hàng hay thanh toán thành công)?\n"
        "  + Khi khách chuyển sang cổng thanh toán rồi tắt app thì voucher bị tạm giữ bao lâu?\n"
        "  + Khách hoàn trả 1 phần đơn hàng thì tính chiết khấu thế nào?\n"
        "2. Chặn Cổng Human Gate 1: Tester mang danh sách câu hỏi này làm rõ với BA/PO trước. Khi requirement đã có thông tin chuẩn xác, mới chuyển giao context sang Phase 2 sinh kịch bản."
    ],
    [
        "Vấn đề 2",
        "Vấn đề kỹ thuật / Thách thức",
        "Lỗi Gom Cụm Hành Động (Action Bundling) Làm Hỏng Kịch Bản Automation Test",
        "THÁCH THỨC: AI mặc định có xu hướng dồn nhiều hành động vào một bước duy nhất (ví dụ: 'Chọn số lượng hàng = 5, nhập địa chỉ, chọn thanh toán thẻ, bấm Đặt hàng'). Khi bàn giao kịch bản này cho đội Automation hoặc chuyển thành Playwright/Cypress script, kịch bản hoàn toàn không thể thực thi tự động ổn định.",
        "1. Kỹ năng thiết kế test case chuẩn cho Automation (Atomic Test Steps).\n2. Khả năng thiết lập Rule điều phối nắn chỉnh hành vi của AI.\n3. Tiêu chuẩn bàn giao giữa Functional QA và Automation Engineer.",
        "GIẢI PHÁP KỸ THUẬT ĐÃ TRIỂN KHAI TRONG REPO:\n"
        "1. Đưa Luật Cấm Cứng Vào Prompt & AGENTS.md:\n"
        "- Ban hành nguyên tắc Step Disaggregation: Mọi tiền đề chuẩn bị đưa vào Pre-conditions. Bước nhập liệu (Bước 1) và Bước kích hoạt gửi request (Bước 2) bắt buộc phải là 2 bước riêng biệt.\n"
        "2. Cấu Trúc Bảng Kiểm Thử Chuẩn Hóa:\n"
        "- Bảng kịch bản gồm 4 cột: `STT` | `Bước thực hiện` | `Kết quả mong đợi` | `Trạng thái`.\n"
        "- Tách rõ: Bước 1: Khách hàng chọn voucher giảm giá -> UI hiển thị nhãn voucher được áp dụng; Bước 2: Bấm nút 'Thanh toán' (POST /api/v1/checkout) -> HTTP 200, DB tạo order mới.\n"
        "- Giúp kỹ sư Automation dễ dàng map trực tiếp từng bước thành các hàm tương tác `locator.click()`, `locator.fill()` và assertion tương ứng."
    ],
    [
        "Vấn đề 3",
        "Vấn đề kỹ thuật / Thách thức",
        "Lệch Pha Ngôn Ngữ & Quá Tải Thuật Ngữ Hàn Lâm (Technical Jargon Overload)",
        "THÁCH THỨC: Khi phân tích rủi ro kỹ thuật, AI có thói quen xổ ra hàng loạt thuật ngữ kỹ thuật hàn lâm (như 'Redis INCR', 'Optimistic Lock', 'Distributed Transaction Saga', 'Lost Update') khiến Product Owner, BA và Manual Tester cảm thấy nặng nề, khó hiểu và từ chối sử dụng công cụ.",
        "1. Nhận thức về rào cản ứng dụng (Adoption Barrier) của người dùng nội bộ.\n2. Khả năng dịch chuyển linh hoạt giữa ngôn ngữ kỹ thuật và ngôn ngữ nghiệp vụ.\n3. Thiết kế giải pháp kỹ thuật có tính bền vững (Persistence Configuration).",
        "GIẢI PHÁP KỸ THUẬT ĐÃ TRIỂN KHAI TRONG REPO:\n"
        "1. Xây Dựng Tệp Cấu Hình Ghi Nhớ Góc Nhìn (`user_preferences.json`):\n"
        "- Hỗ trợ 3 góc nhìn: `business`, `technical`, `hybrid`.\n"
        "2. Kỹ Thuật 'Storytelling Prompting' Cho Góc Nhìn Nghiệp Vụ:\n"
        "- Thay vì nói: 'Nguy cơ Lost Update do thiếu Distributed Lock trên Redis Counter'.\n"
        "- Agent diễn giải thành: 'Kẻ gian có thể mở 2 tab cùng lúc và bấm thanh toán đồng thời trong tích tắc, khiến hệ thống đếm sót và cho phép mua hàng vượt quá tồn kho thực tế'.\n"
        "- Giúp BA và PO nắm bắt ngay rủi ro kinh doanh để đưa ra quyết định mà không cần kiến thức chuyên sâu về hạ tầng."
    ],
    [
        "Vấn đề 4",
        "Vấn đề kỹ thuật / Thách thức",
        "Lỗi Bỏ Sót Các Rủi Ro Kiến Trúc Phân Tán (Concurrency, State Drift, Clock Drift)",
        "THÁCH THỨC: Khi kiểm thử thủ công, tester thường chỉ tập trung vào luồng Happy Path và các ca biên đơn giản. Các lỗi chạy đua dữ liệu (Concurrency trong 10-50ms), lệch trạng thái giữa các Microservices (State Drift) hoặc lệch đồng hồ hệ thống (Clock Drift) hầu như luôn bị bỏ sót và chỉ phát nổ trên Production.",
        "1. Hiểu biết sâu sắc về kiến trúc hệ thống phân tán (Microservices Architecture).\n2. Năng lực xây dựng cẩm nang rủi ro chuyên sâu (Technical Risk Checklist).\n3. Kỹ thuật mô phỏng kiểm thử đa luồng (Simulated Concurrency Testing).",
        "GIẢI PHÁP KỸ THUẬT ĐÃ TRIỂN KHAI TRONG REPO:\n"
        "1. Xây Dựng Khung Cẩm Nang 5 Góc Khuất Kỹ Thuật (`risk-checklist.md`):\n"
        "- Bắt buộc mọi requirement đều phải rà soát qua 5 lăng kính: (1) Concurrency & Race Condition, (2) State Machine Drift, (3) Clock Drift & Timing Window, (4) Non-Idempotency on Retry, (5) Lifecycle Reversal Failure.\n"
        "2. Bắt Buộc Sinh Kịch Bản Concurrency (P1 Critical):\n"
        "- Ví dụ: `TC_INV_004` mô phỏng 2 request gửi đồng thời trong ≤ 50ms tranh mua sản phẩm cuối cùng ($N=1$), kiểm tra Redis Redlock và ràng buộc CSDL.\n"
        "3. Anchoring Vào Kho 10 Bug Lịch Sử Thực Tế:\n"
        "- Đối chiếu với `BUG-001` (Double refund khi bấm hủy nhanh), `BUG-003` (Voucher 2 tab), buộc AI phải đề xuất phương án phòng ngừa các lỗi đau đớn này."
    ],
    [
        "Vấn đề 5",
        "Vấn đề kỹ thuật / Thách thức",
        "Nguy Cơ Mất Dữ Liệu Hoặc Làm Trắng Bảng Tính Khi Đồng Bộ Lên Đám Mây",
        "THÁCH THỨC: Các script đồng bộ Google Sheets thông thường thường gọi lệnh `clear()` hoặc ghi đè toàn bộ sheet. Khi nhiều tester cùng làm việc hoặc chạy nhiều phiên khác nhau, dữ liệu phân tích của các requirement trước đó sẽ bị xóa sạch, gây mất mát lịch sử kiểm thử nghiêm trọng.",
        "1. Kỹ năng quản trị dữ liệu đám mây an toàn (Data Loss Prevention).\n2. Cơ chế khóa định danh (Traceability Key) và kiểm soát bộ nhớ đệm (Cache Hash).\n3. Thiết kế bảng tính chuyên nghiệp chuẩn Enterprise (Ant Design Blue Styler).",
        "GIẢI PHÁP KỸ THUẬT ĐÃ TRIỂN KHAI TRONG REPO:\n"
        "1. Quy Tắc Bất Di Bất Dịch: Accumulative Append-Only (Tích Lũy Bền Vững):\n"
        "- Cấm tuyệt đối lệnh `clear()`. Mọi requirement mới sinh đều được cấp mã định danh duy nhất (ví dụ `REQ_AUTH_LOCK_001`, `REQ_INV_001`).\n"
        "- Script tự động kiểm tra số dòng hiện có trên Google Sheets và ghi nối tiếp (append rows) vào các dòng trống tiếp theo ở cuối bảng.\n"
        "2. Kiểm Tra Cache Timestamp Qua Metadata:\n"
        "- File `.sync_metadata.json` lưu trữ `last_modified_time_drive`. Chỉ đồng bộ khi có sự thay đổi thực tế, bảo toàn 100% dữ liệu lịch sử của toàn bộ các phiên làm việc trước."
    ],
    [
        "Vấn đề 6",
        "Vấn đề kỹ thuật / Thách thức",
        "Đồng Bộ Kỳ Vọng API & Database Bị Sơ Sài (Chỉ Ghi Chung Chung HTTP 200/400)",
        "THÁCH THỨC: AI thường sinh kết quả kỳ vọng rất lười biếng: 'Hệ thống trả về HTTP 200'. Trong thực tế, HTTP 200 vẫn có thể trả về dữ liệu rác hoặc không cập nhật Database, khiến việc kiểm thử trở nên vô nghĩa.",
        "1. Tiêu chuẩn kiểm thử End-to-End thực chiến (Deep Assertion).\n2. Khả năng thiết lập quy chuẩn kỳ vọng kết quả bắt buộc 3 tầng.\n3. Kỹ năng truy vấn CSDL và kiểm tra tính toàn vẹn dữ liệu.",
        "GIẢI PHÁP KỸ THUẬT ĐÃ TRIỂN KHAI TRONG REPO:\n"
        "1. Thiết Lập Quy Chuẩn Synchronized Deep Verification Trong Prompt & Code:\n"
        "- Cấm chỉ ghi HTTP Status Code đơn thuần.\n"
        "- Bắt buộc chỉ rõ: Các trường cốt lõi trong Response Body (ví dụ: trường `order_id` phải trùng khớp với mã đơn hiển thị trên UI; trường `available_stock = 0`).\n"
        "- Bắt buộc chỉ rõ: Tên bảng, tên cột Database và giá trị mới (ví dụ bảng `inventory`, cột `quantity` giảm từ 1 xuống 0; bảng `orders`, cột `status` chuyển thành `PENDING_PAYMENT`).\n"
        "- Kiểm chứng Event Broker: Kafka topic `OrderPlacedEvent` được phát ra đồng bộ."
    ],

    # -------------------------------------------------------------
    # PHẦN 3: 4 BÀI TEST TÌNH HUỐNG / ĐỀ BÀI THỰC CHIẾN
    # -------------------------------------------------------------
    [
        "Tình huống 1",
        "Bài test tình huống",
        "Xây Dựng Bộ 'Golden Dataset' 50 Stories Để Benchmark Chất Lượng AI Định Kỳ",
        "ĐỀ BÀI: Để đảm bảo bộ dữ liệu AI sinh ra đạt độ đúng đắn ≥ 92% theo yêu cầu của team, bạn hãy thiết kế phương pháp xây dựng bộ 'Golden Dataset' (Ground Truth) gồm 50 User Stories mẫu và quy trình kiểm tra tự động hóa (Automated Benchmark Pipeline) chạy định kỳ mỗi tuần.",
        "1. Phương pháp luận xây dựng bộ dữ liệu kiểm định chuẩn (Ground Truth Curation).\n2. Kỹ năng thiết kế script đo lường tự động (Automated Evaluation Harness).\n3. Năng lực thiết lập các ngưỡng cảnh báo (Alerting Thresholds) khi model bị drift.",
        "GIẢI PHÁP & KẾ HOẠCH TRIỂN KHAI:\n"
        "1. Tiêu Chí Chọn Lọc 50 User Stories Cho Golden Dataset:\n"
        "- 20 Stories về Nghiệp vụ Cốt lõi (Core Flows): Đặt hàng, thanh toán, hủy đơn, hoàn tiền.\n"
        "- 15 Stories về Khuyến mãi & Giỏ hàng: Voucher, flash sale, tính cước lẻ, cộng dồn ưu đãi.\n"
        "- 10 Stories về Bảo mật & Tài khoản: Khóa tài khoản, xác thực 2FA, thu hồi phiên làm việc.\n"
        "- 5 Stories có lỗi logic cố tình gài bẫy (Tricky Specs): Yêu cầu mâu thuẫn hoặc thiếu thông tin để test khả năng đặt câu hỏi của AI.\n\n"
        "2. Pipeline Đánh Giá Tự Động (Eval Pipeline):\n"
        "- Chạy batch 50 stories qua Agentic Workflow mỗi tối Chủ Nhật.\n"
        "- Chạy Rule Validator kiểm tra 100% cú pháp và schema 3 tầng.\n"
        "- So sánh bộ Business Rules bóc tách với ground truth qua thuật toán Semantic Similarity (Cosine Similarity ≥ 0.88).\n"
        "- Nếu tổng điểm Accuracy < 90% -> Gửi cảnh báo lên Telegram để Lead QA hiệu chỉnh lại Prompt/Rules trước tuần làm việc mới."
    ],
    [
        "Tình huống 2",
        "Bài test tình huống",
        "Thiết Kế Workflow Tự Động Hóa Kéo Ticket Từ Jira & Phản Hồi Câu Hỏi Cho BA",
        "ĐỀ BÀI: Hãy thiết kế một luồng làm việc tự động (Workflow) kết nối giữa Jira và Antigravity Native Plugin qua MCP Server: Khi BA chuyển trạng thái Jira Ticket sang 'Ready for Grooming', hệ thống tự động phân tích Phase 1 và post comment danh sách câu hỏi chất vấn trực tiếp lên ticket.",
        "1. Khả năng tích hợp hệ sinh thái quản lý dự án (Jira REST API / Jira MCP).\n2. Tư duy tự động hóa quy trình Shift-Left giảm thiểu thời gian họp hành.\n3. Kỹ năng format dữ liệu Markdown chuyên nghiệp trên Jira Comment.",
        "GIẢI PHÁP THỰC THI:\n"
        "1. Kiến Trúc Luồng Tự Động Hóa (Jira Webhook / MCP):\n"
        "- Trigger: Jira Webhook bắt sự kiện `jira:issue_updated` với điều kiện `status = 'Ready for Grooming'`.\n"
        "- Orchestrator nhận payload, trích xuất `issue_key`, `summary`, `description`.\n"
        "- Kích hoạt Subagent `req-risk-analyst` phân tích Phase 1 (bóc tách 4 thành tố Business Rules, đối chiếu bug lịch sử, quét 5 rủi ro kỹ thuật).\n"
        "- Format kết quả thành bảng Markdown chuyên nghiệp: Thẻ tóm tắt, Bảng ma trận quy tắc, Danh sách câu hỏi cho BA kèm mức độ ảnh hưởng (Critical / Medium).\n"
        "- Gọi Jira MCP tool `add_issue_comment` post trực tiếp vào ticket.\n"
        "- Kết quả: BA nhận được câu hỏi chất vấn ngay trong vòng 2 phút, giải quyết mọi kẽ hở logic trước buổi họp Grooming 1 ngày."
    ],
    [
        "Tình huống 3",
        "Bài test tình huống",
        "Chuyển Hóa Kịch Bản Giả Lập 3 Tầng Thành Code Playwright & k6 Thực Thi",
        "ĐỀ BÀI: Cho kịch bản kiểm thử giả lập `TC_INV_004` (Kiểm tra Race Condition 2 người cùng mua sản phẩm cuối cùng N=1 trong ≤ 50ms). Hãy viết script tự động hóa hoàn chỉnh: 1 kịch bản Playwright E2E kiểm tra giao diện và 1 kịch bản k6 Load Test kiểm tra API concurrency.",
        "1. Khả năng hiện thực hóa kịch bản giả lập thành mã kiểm thử tự động thực thi.\n2. Thành thạo công cụ Playwright (UI) và k6 (API Concurrency/Performance).\n3. Kỹ thuật assert sâu ở tầng API Response Body và Database.",
        "GIẢI PHÁP & MÃ NGUỒN MẪU:\n"
        "1. Kịch Bản k6 Concurrency Test (`concurrency_checkout.js`):\n"
        "```javascript\n"
        "import http from 'k6/http';\n"
        "import { check } from 'k6';\n"
        "export const options = { vus: 2, iterations: 2 }; // 2 luồng bắn đồng thời\n"
        "export default function () {\n"
        "  const payload = JSON.stringify({ product_id: 'PROD_LAST_ONE', quantity: 1 });\n"
        "  const res = http.post('https://api.staging.vn/orders/checkout', payload, {\n"
        "    headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer TOKEN_${__VU}` }\n"
        "  });\n"
        "  // 1 người phải thành công (201), 1 người phải bị từ chối hết hàng (409/400)\n"
        "  check(res, { 'Status hợp lệ (201 hoặc 409)': (r) => r.status === 201 || r.status === 409 });\n"
        "}\n"
        "```\n"
        "2. Kiểm Tra Database Sau Chạy Test:\n"
        "Chạy query: `SELECT quantity FROM inventory WHERE product_id = 'PROD_LAST_ONE'` -> Bắt buộc `quantity = 0`, tuyệt đối không được âm (`quantity >= 0`)."
    ],
    [
        "Tình huống 4",
        "Bài test tình huống",
        "Xây Dựng Dashboard Theo Dõi 3 Chỉ Số Vàng Đánh Giá Hiệu Quả Sau 90 Ngày",
        "ĐỀ BÀI: Để báo cáo trước Ban Giám đốc và toàn bộ team QA sau 3 tháng, bạn hãy thiết kế cấu trúc một Dashboard theo dõi 3 chỉ số vàng: (1) Defect Escape Rate, (2) QA Man-hours Saved, (3) Team Throughput Multiplier. Nêu rõ nguồn dữ liệu và công thức tính toán.",
        "1. Năng lực xây dựng hệ thống báo cáo quản trị chất lượng (Executive Quality Dashboard).\n2. Công thức tính toán các chỉ số kiểm thử chuẩn quốc tế.\n3. Kỹ năng trình bày dữ liệu trực quan phục vụ ra quyết định kinh doanh.",
        "CẤU TRÚC DASHBOARD & CÔNG THỨC ĐO LƯỜNG:\n"
        "1. Chỉ Số 1: Defect Escape Rate (DER - Tỷ Lệ Lỗi Lọt Ra Prod):\n"
        "- Công thức: `DER = (Bugs_Production / Tổng_Bugs) * 100%`.\n"
        "- Mục tiêu 90 ngày: Giảm từ mức baseline 18% xuống dưới 8% (giảm > 50% lỗi lọt nhờ bắt sớm ở khâu requirement).\n\n"
        "2. Chỉ Số 2: QA Man-hours Saved (Số Giờ Làm Việc Tiết Kiệm Được):\n"
        "- Công thức: `Hours_Saved = (Lead_Time_Trước - Lead_Time_Sau) * Số_User_Stories`.\n"
        "- Dữ liệu thực tế: Giảm từ 16h xuống 4.5h trên mỗi story phức tạp -> Tiết kiệm 11.5 giờ/story. Với 30 stories/tháng của team, tiết kiệm ~345 man-hours/tháng (~45 triệu VNĐ).\n\n"
        "3. Chỉ Số 3: Team Throughput Multiplier (Hệ Số Nâng Effort):\n"
        "- Công thức: `Throughput_Ratio = Tổng_Stories_Release_Sprint_Hiện_Tại / Baseline_Sprint_Cũ`.\n"
        "- Mục tiêu 90 ngày: Đạt hệ số 2.5x (team gánh được khối lượng công việc gấp 2.5 lần mà không cần tuyển thêm nhân sự)."
    ]
]

print(f"Total rows to insert: {len(ROWS)}")
