#!/usr/bin/env python3
"""
generate_presentation.py
Generates an executive, flowchart-centric 16:9 presentation for the QA AI Specialist interview.
Theme: 100% Light Theme - Clean White & Ant Design Blue (#1677FF), Slate (#1E293B, #64748B), Emerald (#16A34A), Rose (#E11D48).
Structure:
  Slide 1: Executive Title & Định Vị Hệ Thống (What It Does & Core Mission - Light Theme)
  Slide 2: HỆ THỐNG ĐANG LÀM GÌ? Khả Năng Xử Lý Chuyên Sâu Từng Khâu (Inputs -> Core Processing -> Outputs)
  Slide 3: HỆ THỐNG NHẰM NHIỆM VỤ GÌ? 4 Sứ Mệnh Kiểm Thử Chiến Lược (Shift-Left, Giải Phóng Thủ Công, Zero Hallucination, Automation Ready)
  Slide 4: SƠ ĐỒ LUỒNG TỔNG QUAN: 2-Phase State Machine & 2 Human Gates (Flowchart Overview)
  Slide 5: SƠ ĐỒ LUỒNG CHẶNG 0: Pre-Flight, Quản Trị Góc Nhìn & Xác Thực Cache (Flowchart Stage 0)
  Slide 6: SƠ ĐỒ LUỒNG PHA 1: Bóc Tách Yêu Cầu & Quét 5 Rủi Ro (Flowchart Phase 1)
  Slide 7: SƠ ĐỒ LUỒNG ĐIỂM CHẶN: 2 Human Gates & Cơ Chế Tự Động Rollback (Flowchart Gates)
  Slide 8: SƠ ĐỒ LUỒNG PHA 2: Thiết Kế Test Automation & 3 Tầng Sâu (Flowchart Phase 2)
  Slide 9: SƠ ĐỒ LUỒNG PHA 3: Local-First & Đồng Bộ Google Workspace 2 Chiều (Flowchart Phase 3)
  Slide 10: Minh Chứng Thực Nghiệm: Vòng Lặp Tự Nắn Chỉnh Qua 3 Bài Toán Mẫu (Auth, Inv, Voucher)
  Slide 11: Kế Hoạch Triển Khai Thực Chiến 3 Tháng
  Slide 12: Kết Luận & Cam Kết Thực Thi (Closing Callout)
"""

import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# --- Color Palette (100% Light Theme) ---
COLOR_PRIMARY = RGBColor(22, 119, 255)         # Ant Design Blue #1677FF
COLOR_PRIMARY_DARK = RGBColor(9, 88, 217)     # Deep Blue #0958D9
COLOR_PRIMARY_LIGHT = RGBColor(230, 244, 255) # Light Blue Tint #E6F4FF
COLOR_TEXT_MAIN = RGBColor(30, 41, 59)        # Slate 800 #1E293B
COLOR_TEXT_MUTED = RGBColor(100, 116, 139)    # Slate 500 #64748B
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_BG_LIGHT = RGBColor(248, 250, 252)      # Slate 50 #F8FAFC
COLOR_BORDER = RGBColor(226, 232, 240)        # Slate 200 #E2E8F0
COLOR_CARD_BORDER = RGBColor(203, 213, 225)   # Slate 300 #CBD5E1

COLOR_SUCCESS = RGBColor(22, 163, 74)         # Emerald Green #16A34A
COLOR_SUCCESS_LIGHT = RGBColor(220, 252, 231) # Green 100 #DCFCE7
COLOR_DANGER = RGBColor(225, 29, 72)          # Rose Red #E11D48
COLOR_DANGER_LIGHT = RGBColor(254, 226, 226)  # Red 100 #FEE2E2
COLOR_WARNING = RGBColor(217, 119, 6)         # Amber #D97706
COLOR_WARNING_LIGHT = RGBColor(254, 243, 199) # Amber 100 #FEF3C7
COLOR_ACCENT = RGBColor(13, 148, 136)         # Teal #0D9488
COLOR_ACCENT_LIGHT = RGBColor(204, 251, 241)  # Teal 100 #CCFBF1
COLOR_PURPLE = RGBColor(124, 58, 237)         # Purple 600 #7C3AED
COLOR_PURPLE_LIGHT = RGBColor(245, 243, 255)  # Purple 50 #F5F3FF

def create_deck():
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Helper: Add Standard Header (Light Theme)
    def add_header(slide, title_text, category_tag, subtitle_text=None):
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.1))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = COLOR_PRIMARY
        top_bar.line.fill.background()

        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.32), Inches(3.6), Inches(0.32))
        badge.fill.solid()
        badge.fill.fore_color.rgb = COLOR_PRIMARY_LIGHT
        badge.line.color.rgb = COLOR_PRIMARY
        badge.line.width = Pt(1)
        tf_b = badge.text_frame
        tf_b.word_wrap = True
        p_b = tf_b.paragraphs[0]
        p_b.text = category_tag.upper()
        p_b.font.size = Pt(9.5)
        p_b.font.bold = True
        p_b.font.color.rgb = COLOR_PRIMARY_DARK
        p_b.alignment = PP_ALIGN.CENTER

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.7), Inches(0.72))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_MAIN

        if subtitle_text:
            p2 = tf.add_paragraph()
            p2.text = subtitle_text
            p2.font.size = Pt(10.5)
            p2.font.color.rgb = COLOR_TEXT_MUTED

    # Helper: Embed Flowchart Image
    def embed_flowchart(slide, png_filename):
        png_path = os.path.join(current_dir, png_filename)
        if os.path.exists(png_path):
            slide.shapes.add_picture(png_path, Inches(0.8), Inches(1.58), Inches(11.733), Inches(4.99))

    # =========================================================================
    # SLIDE 1: Title Slide (100% Light Theme + Định Vị Hệ Thống & Sứ Mệnh)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_BG_LIGHT
    bg1.line.fill.background()

    # Top accent bar
    bar1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.15))
    bar1.fill.solid()
    bar1.fill.fore_color.rgb = COLOR_PRIMARY
    bar1.line.fill.background()

    # Badge & Title Box
    tbox = s1.shapes.add_textbox(Inches(0.8), Inches(0.55), Inches(11.7), Inches(1.8))
    tf1 = tbox.text_frame
    tf1.word_wrap = True

    p_badge = tf1.paragraphs[0]
    p_badge.text = "CHIẾN LƯỢC ỨNG DỤNG AI TRONG KIỂM THỬ (AI-DRIVEN QA SYSTEM)"
    p_badge.font.size = Pt(10.5)
    p_badge.font.bold = True
    p_badge.font.color.rgb = COLOR_PRIMARY_DARK
    p_badge.space_after = Pt(4)

    p_title = tf1.add_paragraph()
    p_title.text = "QA REQUIREMENT & RISK ASSISTANT\nHệ Tác Tử Tự Động Phân Tích Yêu Cầu & Thiết Kế Kiểm Thử Thực Chiến"
    p_title.font.size = Pt(24)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_TEXT_MAIN
    p_title.space_after = Pt(4)

    p_sub = tf1.add_paragraph()
    p_sub.text = "Chuyển hóa tài liệu yêu cầu thô thành Test Suite chuẩn 3 tầng UI/API/DB • Chặn đứng lỗi sớm • Chuẩn hóa dữ liệu QA"
    p_sub.font.size = Pt(12)
    p_sub.font.color.rgb = COLOR_TEXT_MUTED

    # Center Box: 2 Columns (What It Does vs Core Mission)
    c_outer = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.55), Inches(11.7), Inches(2.6))
    c_outer.fill.solid()
    c_outer.fill.fore_color.rgb = COLOR_WHITE
    c_outer.line.color.rgb = COLOR_CARD_BORDER
    c_outer.line.width = Pt(1.5)

    # Left Sub-box: HỆ THỐNG ĐANG LÀM GÌ?
    b_left = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(2.75), Inches(5.5), Inches(2.2))
    b_left.fill.solid()
    b_left.fill.fore_color.rgb = COLOR_PRIMARY_LIGHT
    b_left.line.color.rgb = COLOR_PRIMARY
    b_left.line.width = Pt(1.5)
    tf_l = b_left.text_frame
    tf_l.word_wrap = True
    p_lh = tf_l.paragraphs[0]
    p_lh.text = "🤖 HỆ THỐNG ĐANG LÀM GÌ? (WHAT IT DOES)"
    p_lh.font.size = Pt(11)
    p_lh.font.bold = True
    p_lh.font.color.rgb = COLOR_PRIMARY_DARK
    p_lh.space_after = Pt(6)

    l_items = [
        ("• Tiếp nhận tài liệu thô:", "User Story, PRD, API Swagger chưa rõ nét hoặc thiếu kịch bản biên."),
        ("• Bóc tách 4 thành tố:", "Tự động phân tách Business Rules, Boundary Limits, Exceptions & User Flow."),
        ("• Quét 5 rủi ro kiến trúc:", "Phát hiện lỗi ngầm: Concurrency (<=50ms), Lost Update, Deadlock, JWT Drift."),
        ("• Thiết kế Test 3 tầng sâu:", "Sinh kịch bản tách bước kiểm chứng UI + API Body + DB & Sync Google Sheets.")
    ]
    for it_h, it_d in l_items:
        p_it = tf_l.add_paragraph()
        p_it.text = it_h + " " + it_d
        p_it.font.size = Pt(9.5)
        p_it.font.color.rgb = COLOR_TEXT_MAIN
        p_it.space_after = Pt(3)

    # Right Sub-box: NHIỆM VỤ TRỌNG TÂM CỦA HỆ THỐNG
    b_right = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.75), Inches(5.5), Inches(2.2))
    b_right.fill.solid()
    b_right.fill.fore_color.rgb = COLOR_SUCCESS_LIGHT
    b_right.line.color.rgb = COLOR_SUCCESS
    b_right.line.width = Pt(1.5)
    tf_r = b_right.text_frame
    tf_r.word_wrap = True
    p_rh = tf_r.paragraphs[0]
    p_rh.text = "🎯 NHIỆM VỤ TRỌNG TÂM CỦA HỆ THỐNG (SYSTEM MISSIONS)"
    p_rh.font.size = Pt(11)
    p_rh.font.bold = True
    p_rh.font.color.rgb = RGBColor(21, 128, 61)
    p_rh.space_after = Pt(6)

    r_items = [
        ("• Shift-Left QA:", "Chặn đứng 50% lỗi ngay từ khâu phân tích yêu cầu trước khi Dev code."),
        ("• Giải phóng thao tác thủ công:", "Tự động hóa toàn diện khâu đọc hiểu tài liệu và soạn đặc tả kịch bản."),
        ("• Triệt tiêu 100% ảo giác:", "Ép AI bám sát 10 bugs production thực tế, Tester phê duyệt qua 2 cổng."),
        ("• Chuẩn hóa tài sản kiểm thử:", "Lưu trữ tích lũy bền vững và làm bệ phóng trực tiếp cho Playwright E2E.")
    ]
    for it_h, it_d in r_items:
        p_it = tf_r.add_paragraph()
        p_it.text = it_h + " " + it_d
        p_it.font.size = Pt(9.5)
        p_it.font.color.rgb = COLOR_TEXT_MAIN
        p_it.space_after = Pt(3)

    # 3 Strategic Focus Cards at Bottom (Light Theme)
    focus_items = [
        ("🎯 ĐỘ CHÍNH XÁC DỮ LIỆU", "≥ 92%", "Kiểm chứng sâu 3 tầng, 0 ảo giác", COLOR_PRIMARY),
        ("🛡️ CHẤT LƯỢNG RELEASE", "Giảm 50% Defect", "Chặn đứng lỗi sớm ngay khâu Spec", COLOR_SUCCESS),
        ("⚡ TỰ ĐỘNG HÓA QUY TRÌNH", "80% Tác Vụ", "Tự động hóa đọc hiểu & viết test case", COLOR_WARNING)
    ]
    k_w = Inches(3.7)
    k_gap = Inches(0.3)
    for i, (ktitle, kval, kdesc, kcol) in enumerate(focus_items):
        kbox = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + i*(k_w + k_gap), Inches(5.35), k_w, Inches(1.5))
        kbox.fill.solid()
        kbox.fill.fore_color.rgb = COLOR_WHITE
        kbox.line.color.rgb = COLOR_CARD_BORDER
        kbox.line.width = Pt(1.5)
        tf_k = kbox.text_frame
        tf_k.word_wrap = True
        
        p1 = tf_k.paragraphs[0]
        p1.text = ktitle
        p1.font.size = Pt(9.5)
        p1.font.bold = True
        p1.font.color.rgb = kcol
        
        p2 = tf_k.add_paragraph()
        p2.text = kval
        p2.font.size = Pt(18)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_TEXT_MAIN
        
        p3 = tf_k.add_paragraph()
        p3.text = kdesc
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = COLOR_TEXT_MUTED

    # =========================================================================
    # SLIDE 2: HỆ THỐNG ĐANG LÀM GÌ? (What The System Does - Capabilities & Pipeline)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Hệ Thống Đang Làm Gì? Khả Năng Xử Lý Chuyên Sâu Từng Khâu",
               "1. ĐỊNH DANH HỆ THỐNG",
               "Cơ chế tự động hóa toàn diện từ lúc nhận tài liệu yêu cầu thô đến khi xuất ra bộ test suite hoàn chỉnh.")

    c_w = Inches(3.7)
    c_gap = Inches(0.3)
    top_pos = Inches(1.6)
    card_h = Inches(5.4)

    s2_cards = [
        {
            "badge": "📥 GIAI ĐOẠN 1: ĐẦU VÀO",
            "title": "Tiếp Nhận & Đọc Hiểu Spec",
            "subtitle": "Xử lý đa dạng mọi nguồn tài liệu dự án",
            "border_color": COLOR_PRIMARY,
            "items": [
                ("📄 User Story & Acceptance Criteria:", "Đọc hiểu bối cảnh người dùng, tiêu chí nghiệm thu còn sơ sài hoặc diễn đạt mơ hồ."),
                ("📑 Tài liệu BA / PRD Chi Tiết:", "Phân tích tài liệu nghiệp vụ dài, phức tạp nhiều phân hệ chức năng."),
                ("⚙️ API Swagger / JSON Schema:", "Đọc hiểu method HTTP, headers, request body, query params và response schema."),
                ("🧠 Bộ nhớ góc nhìn (user_preferences):", "Tự động điều chỉnh giọng văn phân tích: Business (dễ hiểu) vs Technical (chuyên sâu).")
            ]
        },
        {
            "badge": "⚙️ GIAI ĐOẠN 2: TÁC VỤ THỰC HIỆN",
            "title": "Phân Tích, Phản Biện & Thiết Kế",
            "subtitle": "5 tác vụ AI chuyên sâu thay thế công việc thủ công",
            "border_color": COLOR_PURPLE,
            "items": [
                ("📋 Bóc tách 4 thành tố cốt lõi:", "Tự động phân tách Rules, Boundary Limits, Exception Flows và User Journey."),
                ("❓ Soạn câu hỏi phản biện cho BA:", "Chỉ ra các điểm hở tài liệu, mâu thuẫn logic để chốt sớm với BA/PO."),
                ("🔍 Quét 5 rủi ro kiến trúc sâu:", "Race condition (<=50ms), Lost Update, Concurrency Deadlock, JWT Drift, Clock Drift."),
                ("🗄️ Đối chiếu 10 Bugs Ground Truth:", "Gắn mã Defect ID tương đồng từ kho bug thực tế để neo chuẩn logic."),
                ("💎 3 Nguyên Tắc Vàng QA:", "Tách bước độc lập (Disaggregation), Verify 3 tầng sâu (UI/API/DB), Gán Status NOT_RUN.")
            ]
        },
        {
            "badge": "📤 GIAI ĐOẠN 3: ĐẦU RA BÀN GIAO",
            "title": "Sản Phẩm Bàn Giao Sạch 100%",
            "subtitle": "Trực quan hóa Google Sheets & Lưu trữ bền vững",
            "border_color": COLOR_SUCCESS,
            "items": [
                ("📊 Google Sheets Master Ant Design Blue:", "Tự động ghi nối tiếp vào 2 tab Requirements & Test Cases, Header xanh #1677FF, freeze row 1."),
                ("🎯 Dropdown Status & Conditional Format:", "Menu chọn nhanh PASS/FAIL/BLOCKED/NOT_RUN tự đổi màu tiện lợi cho Tester."),
                ("💾 Local-First Append-Only:", "Lưu tích lũy vào file JSON cục bộ, bảo toàn 100% lịch sử các sprint trước, cấm reset."),
                ("🤖 Sẵn sàng Playwright E2E Automation:", "Kịch bản đã chia nhỏ bước, code tự động hóa ngay mà không cần viết lại.")
            ]
        }
    ]

    for i, c in enumerate(s2_cards):
        left_pos = Inches(0.8) + i * (c_w + c_gap)
        box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, top_pos, c_w, card_h)
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_WHITE
        box.line.color.rgb = c["border_color"]
        box.line.width = Pt(1.5)
        
        tf = box.text_frame
        tf.word_wrap = True
        
        p_badge = tf.paragraphs[0]
        p_badge.text = c["badge"]
        p_badge.font.size = Pt(9.5)
        p_badge.font.bold = True
        p_badge.font.color.rgb = c["border_color"]
        p_badge.space_after = Pt(2)
        
        p_t = tf.add_paragraph()
        p_t.text = c["title"]
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN
        p_t.space_after = Pt(2)
        
        p_s = tf.add_paragraph()
        p_s.text = c["subtitle"]
        p_s.font.size = Pt(9)
        p_s.font.color.rgb = COLOR_TEXT_MUTED
        p_s.space_after = Pt(8)
        
        for item_title, item_desc in c["items"]:
            p_it = tf.add_paragraph()
            p_it.text = item_title
            p_it.font.size = Pt(9.5)
            p_it.font.bold = True
            p_it.font.color.rgb = COLOR_TEXT_MAIN
            
            p_id = tf.add_paragraph()
            p_id.text = item_desc
            p_id.font.size = Pt(8.5)
            p_id.font.color.rgb = COLOR_TEXT_MUTED
            p_id.space_after = Pt(5)

    # =========================================================================
    # SLIDE 3: HỆ THỐNG NHẰM NHIỆM VỤ GÌ? (4 Core Missions)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Hệ Thống Nhằm Nhiệm Vụ Gì? 4 Sứ Mệnh Kiểm Thử Chiến Lược",
               "2. NHIỆM VỤ TRỌNG TÂM CỦA HỆ THỐNG",
               "Giải quyết triệt để các nút thắt cổ chai về chất lượng phần mềm, phát hiện lỗi sớm và chuẩn hóa dữ liệu.")

    c_w3 = Inches(2.7)
    c_gap3 = Inches(0.3)
    s3_cards = [
        {
            "badge": "🎯 NHIỆM VỤ 1",
            "title": "Shift-Left QA\nChặn Đứng Lỗi Sớm",
            "subtitle": "Phát hiện kẽ hở ngay tại Spec",
            "border_color": COLOR_PRIMARY,
            "items": [
                ("⚠️ Thực trạng:", "70% lỗi phần mềm xuất phát từ yêu cầu mơ hồ, thiếu biên, mâu thuẫn logic."),
                ("💡 Nhiệm vụ:", "Bắt lỗi và kẽ hở nghiệp vụ ngay trong Sprint Planning trước khi Dev viết code."),
                ("💰 Giá trị ROI:", "Chi phí sửa lỗi tại Spec rẻ hơn 10 - 30 lần so với sửa lỗi tại UAT hoặc Production."),
                ("🤝 Hợp tác:", "Tạo cầu nối phản biện chủ động giữa QA, BA và Tech Lead.")
            ]
        },
        {
            "badge": "🚀 NHIỆM VỤ 2",
            "title": "Tối Ưu Chu Trình QA\nGiải Phóng Thủ Công",
            "subtitle": "Tự động hóa đọc hiểu & viết test",
            "border_color": COLOR_ACCENT,
            "items": [
                ("⚠️ Thực trạng:", "QA mất nhiều thời gian sprint chỉ để đọc spec dài, kẻ bảng excel, format sheet."),
                ("💡 Nhiệm vụ:", "Tự động hóa 80% khâu đọc hiểu, bóc tách rules và viết đặc tả test cases."),
                ("⏳ Tốc độ vượt trội:", "Chuẩn bị test suite hoàn chỉnh trong vài phút thay vì cả buổi làm việc."),
                ("🧠 Nâng tầm QA:", "Dành thời gian tập trung vào Exploratory Testing, Security & UX.")
            ]
        },
        {
            "badge": "🛡️ NHIỆM VỤ 3",
            "title": "Triệt Tiêu Ảo Giác\nChính Xác Dữ Liệu",
            "subtitle": "Kiểm chứng 3 tầng & Con người duyệt",
            "border_color": COLOR_DANGER,
            "items": [
                ("⚠️ Thực trạng:", "Prompt AI tự do luôn tạo test case hời hợt 'HTTP 200', bịa endpoint giả."),
                ("💡 Nhiệm vụ:", "Kiểm chứng sâu 3 tầng UI + API Body + DB State & Event."),
                ("🛑 Human-in-the-Loop:", "2 Chốt chặn Human Gates trao quyền kiểm soát tối cao cho Tester."),
                ("↩️ Tự động Rollback:", "Đổi requirement là tự động hủy test cũ và phân tích lại từ đầu.")
            ]
        },
        {
            "badge": "📈 NHIỆM VỤ 4",
            "title": "Chuẩn Hóa Tri Thức\nBệ Phóng E2E Auto",
            "subtitle": "Tài sản kiểm thử tích lũy lâu dài",
            "border_color": COLOR_SUCCESS,
            "items": [
                ("⚠️ Thực trạng:", "Tri thức kiểm thử nằm rải rác trên máy cá nhân, dễ thất thoát khi đổi nhân sự."),
                ("💡 Nhiệm vụ:", "Tích lũy bền vững vào Local JSON & Google Sheets Master theo cơ chế Append-Only."),
                ("🔒 Bảo toàn lịch sử:", "Không bao giờ xóa/reset, truy vết toàn diện theo requirement_id."),
                ("🤖 Cầu nối Automation:", "Cung cấp đầu vào hoàn hảo để framework Playwright E2E chạy tự động.")
            ]
        }
    ]

    for i, c in enumerate(s3_cards):
        left_pos = Inches(0.8) + i * (c_w3 + c_gap3)
        box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, top_pos, c_w3, card_h)
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_WHITE
        box.line.color.rgb = c["border_color"]
        box.line.width = Pt(1.5)
        
        tf = box.text_frame
        tf.word_wrap = True
        
        p_badge = tf.paragraphs[0]
        p_badge.text = c["badge"]
        p_badge.font.size = Pt(9.5)
        p_badge.font.bold = True
        p_badge.font.color.rgb = c["border_color"]
        p_badge.space_after = Pt(2)
        
        p_t = tf.add_paragraph()
        p_t.text = c["title"]
        p_t.font.size = Pt(12)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN
        p_t.space_after = Pt(2)
        
        p_s = tf.add_paragraph()
        p_s.text = c["subtitle"]
        p_s.font.size = Pt(8.5)
        p_s.font.color.rgb = COLOR_TEXT_MUTED
        p_s.space_after = Pt(8)
        
        for item_title, item_desc in c["items"]:
            p_it = tf.add_paragraph()
            p_it.text = item_title
            p_it.font.size = Pt(9)
            p_it.font.bold = True
            p_it.font.color.rgb = COLOR_TEXT_MAIN
            
            p_id = tf.add_paragraph()
            p_id.text = item_desc
            p_id.font.size = Pt(8.5)
            p_id.font.color.rgb = COLOR_TEXT_MUTED
            p_id.space_after = Pt(5)

    # =========================================================================
    # SLIDE 4: SƠ ĐỒ LUỒNG TỔNG QUAN (Flowchart Overview)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Sơ Đồ Luồng Tổng Quan: 2-Phase State Machine, 2 Human Gates & Cloud Sync",
               "3. KIẾN TRÚC TỔNG QUAN",
               "Sơ đồ luồng trạng thái tuần tự: Điểm rẽ nhánh điều kiện, 2 điểm dừng Tester và cơ chế tự động Rollback.")
    embed_flowchart(s4, "flowchart_overview.png")

    # =========================================================================
    # SLIDE 5: SƠ ĐỒ LUỒNG CHẶNG 0: PRE-FLIGHT (Flowchart Stage 0)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Sơ Đồ Luồng Chặng 0: Quản Trị Góc Nhìn & Xác Thực Cache Hai Chiều",
               "3A. ĐI SÂU CHẶNG 0: PRE-FLIGHT",
               "Sơ đồ luồng kiểm tra cache: Nhánh trùng khớp (<50ms), nhánh Drive thay đổi và cơ chế Offline Fallback.")
    embed_flowchart(s5, "flowchart_stage0.png")

    # =========================================================================
    # SLIDE 6: SƠ ĐỒ LUỒNG PHA 1: REQ-RISK-ANALYST (Flowchart Phase 1)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Sơ Đồ Luồng Pha 1: Bóc Tách Yêu Cầu & Quét 5 Rủi Ro Kỹ Thuật",
               "3B. ĐI SÂU PHA 1: REQ-RISK-ANALYST",
               "Sơ đồ luồng phân tích tĩnh: Bóc tách 4 thành tố, rẽ nhánh phát hiện kẽ hở BA, quét 5 rủi ro và điểm chặn cấm sinh test.")
    embed_flowchart(s6, "flowchart_phase1.png")

    # =========================================================================
    # SLIDE 7: SƠ ĐỒ LUỒNG ĐIỂM CHẶN: 2 HUMAN GATES & ROLLBACK (Flowchart Gates)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Sơ Đồ Luồng Điểm Chặn: 2 Human Gates & Cơ Chế Tự Động Rollback",
               "3C. KIỂM SOÁT CON NGƯỜI (HUMAN-IN-THE-LOOP)",
               "Sơ đồ luồng quyết định của Tester: Duyệt logic Gate 1, nghiệm thu test Gate 2 và luồng Rollback xóa test case khi đổi spec.")
    embed_flowchart(s7, "flowchart_gates.png")

    # =========================================================================
    # SLIDE 8: SƠ ĐỒ LUỒNG PHA 2: TEST DESIGN & 3 TẦNG SÂU (Flowchart Phase 2)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Sơ Đồ Luồng Pha 2: Thiết Kế Test Automation & 3 Tầng Kiểm Chứng Sâu",
               "3D. ĐI SÂU PHA 2: TEST-AUTOMATION-ARCHITECT",
               "Sơ đồ luồng thiết kế kịch bản: Tách bước độc lập, rẽ nhánh 5 nhóm ma trận và kiểm chứng sâu UI + API Body + DB.")
    embed_flowchart(s8, "flowchart_phase2.png")

    # =========================================================================
    # SLIDE 9: SƠ ĐỒ LUỒNG PHA 3: LOCAL-FIRST & GOOGLE SHEETS (Flowchart Phase 3)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Sơ Đồ Luồng Pha 3: Cơ Chế Local-First & Đồng Bộ Google Workspace 2 Chiều",
               "3E. ĐI SÂU PHA 3: WORKSPACE SYNC MANAGER",
               "Sơ đồ luồng lưu trữ & đồng bộ: Bước 1 Append local, Bước 2 Push Sheets qua MCP và Bước 3 Cập nhật cache metadata.")
    embed_flowchart(s9, "flowchart_phase3.png")

    # =========================================================================
    # SLIDE 10: Minh Chứng Thực Nghiệm & Vòng Lặp Tự Nắn Chỉnh (Self-Correction)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Minh Chứng Thực Nghiệm: Vòng Lặp Tự Nắn Chỉnh Qua 3 Bài Toán Mẫu",
               "4. MINH CHỨNG THỰC NGHIỆM",
               "Bằng chứng thực tế từ Repo: Cách hệ thống tự phát hiện sai sót, nắn chỉnh prompt và chuẩn hóa kết quả đầu ra.")

    top_loop = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(11.7), Inches(0.55))
    top_loop.fill.solid()
    top_loop.fill.fore_color.rgb = COLOR_BG_LIGHT
    top_loop.line.color.rgb = COLOR_PRIMARY
    tf_loop = top_loop.text_frame
    p_l = tf_loop.paragraphs[0]
    p_l.text = "🔄 VÒNG LẶP NẮN CHỈNH:   [1. Chạy Thực Nghiệm]  ➔  [2. Phát Hiện Sai Sót]  ➔  [3. Nắn Chỉnh Rules & Code]  ➔  [4. Chuẩn Hóa Bền Vững]"
    p_l.font.size = Pt(10)
    p_l.font.bold = True
    p_l.font.color.rgb = COLOR_PRIMARY_DARK
    p_l.alignment = PP_ALIGN.CENTER

    c_w5 = Inches(3.7)
    c_gap5 = Inches(0.3)
    c_top5 = Inches(2.45)
    c_h5 = Inches(4.5)

    cases = [
        ("🔐 REQ A: KHÓA TÀI KHOẢN (Auth)",
         "Sai mật khẩu 5 lần liên tiếp",
         "✔ Điểm sáng:",
         "Bắt kẽ hở Force Logout trên thiết bị khác; liên kết BUG-001 & BUG-003.",
         "⚠️ Sai sót ban đầu:",
         "Dùng từ ngữ quá hàn lâm (Lost Update, Redis INCR) khiến BA khó hiểu.",
         "🛠️ Nắn chỉnh kỹ thuật:",
         "Thêm user_preferences.json ghi nhớ góc nhìn BA vs SDET; bổ sung kịch bản kiểm tra Event thu hồi Token."),
        ("📦 REQ B: BÁN ÂM KHO (Inventory)",
         "Flash Sale Concurrency cao",
         "✔ Điểm sáng:",
         "Phân biệt Tồn kho vật lý vs Khả dụng; sinh test 2 user tranh mua N=1 trong ≤50ms.",
         "⚠️ Sai sót ban đầu:",
         "Gom cụm bước (chọn số lượng + checkout dồn 1 bước); verify API sơ sài.",
         "🛠️ Nắn chỉnh kỹ thuật:",
         "Đưa 3 Nguyên Tắc Vàng vào Rules cứng; viết script Styler tự động kẻ viền & format Sheets."),
        ("🎟️ REQ C: VOUCHER 1 LẦN (Promo)",
         "Áp mã thanh toán giỏ hàng",
         "✔ Điểm sáng:",
         "Thiết kế Race condition ≤50ms; verify hoàn tiền rollback voucher khi hủy đơn.",
         "⚠️ Sai sót ban đầu:",
         "Format sheet chưa đẹp; chưa có cột Status Pass/Fail tiện dụng cho Tester.",
         "🛠️ Nắn chỉnh kỹ thuật:",
         "Bổ sung Dropdown Data Validation PASS/FAIL/BLOCKED/NOT_RUN và Conditional Formatting màu tự động.")
    ]

    for i, (ctitle, csub, cs1, cd1, cs2, cd2, cs3, cd3) in enumerate(cases):
        cbox = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + i*(c_w5 + c_gap5), c_top5, c_w5, c_h5)
        cbox.fill.solid()
        cbox.fill.fore_color.rgb = COLOR_WHITE
        cbox.line.color.rgb = COLOR_CARD_BORDER
        cbox.line.width = Pt(1.5)
        tf_c = cbox.text_frame
        tf_c.word_wrap = True
        
        p = tf_c.paragraphs[0]
        p.text = ctitle
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY
        p.space_after = Pt(2)
        
        p_sub = tf_c.add_paragraph()
        p_sub.text = csub
        p_sub.font.size = Pt(9.5)
        p_sub.font.color.rgb = COLOR_TEXT_MUTED
        p_sub.space_after = Pt(6)
        
        sections = [(cs1, cd1, COLOR_SUCCESS), (cs2, cd2, COLOR_DANGER), (cs3, cd3, COLOR_PRIMARY_DARK)]
        for stitle, sdesc, scol in sections:
            p_s = tf_c.add_paragraph()
            p_s.text = stitle
            p_s.font.size = Pt(10)
            p_s.font.bold = True
            p_s.font.color.rgb = scol
            
            p_sd = tf_c.add_paragraph()
            p_sd.text = sdesc
            p_sd.font.size = Pt(8.5)
            p_sd.font.color.rgb = COLOR_TEXT_MAIN
            p_sd.space_after = Pt(5)

    # =========================================================================
    # SLIDE 11: Kế Hoạch Triển Khai Thực Chiến 3 Tháng
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Kế Hoạch Triển Khai Thực Chiến Trong 3 Tháng: Từng Bước Vững Chắc",
               "5. KẾ HOẠCH TRIỂN KHAI THỰC CHIẾN",
               "Lộ trình cụ thể để đưa hệ thống vào dự án thực tế, từ Pilot, mở rộng toàn team đến tối ưu hóa tự động.")

    m_w6 = Inches(3.7)
    m_gap6 = Inches(0.3)
    m_top6 = Inches(1.75)
    m_h6 = Inches(5.2)

    months = [
        ("THÁNG 1: PILOT & CHUẨN HÓA DỮ LIỆU",
         "Mục tiêu: Đưa vào 1 squad thử nghiệm, chuẩn hóa Rules",
         COLOR_PRIMARY,
         [("Tuần 1: Setup & Ground Truth", "Triển khai Antigravity Native Plugin; nạp 10-20 bug production của dự án vào bug_repository.json."),
          ("Tuần 2: Pilot 1 Squad", "Áp dụng cho 1 squad kiểm thử (2 Tester + 1 BA). Chạy song song AI và thủ công để đối soát."),
          ("Tuần 3-4: Đánh Giá & Nắn Chỉnh", "Đo lường độ chính xác Semantic Accuracy. Bổ sung các quy tắc nghiệp vụ đặc thù của công ty vào Rules.")]),
        ("THÁNG 2: MỞ RỘNG TOÀN DỰ ÁN & CI/CD",
         "Mục tiêu: Đào tạo toàn bộ QA Team & kết nối pipeline",
         COLOR_ACCENT,
         [("Tuần 5-6: Workshop Đào Tạo QA", "Hướng dẫn đội ngũ Tester cách review phân tích Pha 1, kiểm duyệt kịch bản Pha 2 và sử dụng Google Sheets."),
          ("Tuần 7: Tích Hợp Jira / Confluence", "Kết nối tự động kéo User Story từ Jira và đẩy kết quả phân tích ngược lại Ticket."),
          ("Tuần 8: Tự Động Hóa 50% Test", "Chuyển giao các test case đã tách bước sang Playwright E2E để tự động chạy trên CI/CD.")]),
        ("THÁNG 3: ĐO LƯỜNG HIỆU QUẢ & TỰ ĐỘNG HÓA",
         "Mục tiêu: Hoàn thiện quy trình tự động hóa kiểm thử & Giảm 50% Defect",
         COLOR_SUCCESS,
         [("Tuần 9-10: Tự Nắn Chỉnh Mô Hình", "Xây dựng cơ chế tự động học từ các lỗi Tester sửa trên Sheets để cập nhật lại bug repository."),
          ("Tuần 11: Đo Lường Hiệu Quả (ROI)", "Tổng hợp dữ liệu: Rút ngắn thời gian chuẩn bị kịch bản; Số lỗi lọt sang UAT giảm 50%."),
          ("Tuần 12: Báo Cáo Ban Lãnh Đạo", "Trình bày báo cáo ROI toàn diện và đề xuất mở rộng mô hình cho các dự án khác.")])
    ]

    for i, (mtitle, msub, mcol, msteps) in enumerate(months):
        mbox = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + i*(m_w6 + m_gap6), m_top6, m_w6, m_h6)
        mbox.fill.solid()
        mbox.fill.fore_color.rgb = COLOR_WHITE
        mbox.line.color.rgb = mcol
        mbox.line.width = Pt(1.5)
        tf_m = mbox.text_frame
        tf_m.word_wrap = True
        
        p = tf_m.paragraphs[0]
        p.text = mtitle
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = mcol
        p.space_after = Pt(2)
        
        p_sub = tf_m.add_paragraph()
        p_sub.text = msub
        p_sub.font.size = Pt(9)
        p_sub.font.color.rgb = COLOR_TEXT_MUTED
        p_sub.space_after = Pt(8)
        
        for stitle, sdesc in msteps:
            p_s = tf_m.add_paragraph()
            p_s.text = "📌 " + stitle
            p_s.font.size = Pt(9.5)
            p_s.font.bold = True
            p_s.font.color.rgb = COLOR_TEXT_MAIN
            
            p_sd = tf_m.add_paragraph()
            p_sd.text = sdesc
            p_sd.font.size = Pt(8.5)
            p_sd.font.color.rgb = COLOR_TEXT_MUTED
            p_sd.space_after = Pt(6)

    # =========================================================================
    # SLIDE 12: Q&A & Cam Kết Thực Thi (Light Theme Callout)
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Cam Kết Thực Thi & Sẵn Sàng Đồng Hành Cùng Doanh Nghiệp",
               "6. CAM KẾT & KẾT LUẬN",
               "Tổng kết giá trị cốt lõi và khẳng định tính sẵn sàng triển khai ngay từ ngày đầu tiên nhận việc.")

    p_w7 = Inches(3.7)
    p_gap7 = Inches(0.3)
    p_top7 = Inches(1.75)
    p_h7 = Inches(4.2)

    pillars = [
        ("🎯 NĂNG LỰC THỰC CHIẾN",
         "Không chỉ nói lý thuyết suông — Đã xây dựng hoàn chỉnh Plugin, State Machine, Rules, Script và đồng bộ Google Workspace sẵn sàng hoạt động.",
         COLOR_PRIMARY,
         ["• Đã kiểm chứng qua 3 bài toán khó (Auth, Kho, Voucher)",
          "• Hiểu sâu kiến trúc Microservices & Distributed System",
          "• Tự động hóa E2E từ Spec đến Google Sheets"]),
        ("🤝 TINH THẦN ĐỒNG HÀNH",
         "Xem AI là trợ thủ đắc lực nâng tầm con người chứ không phải công cụ thay thế. Giúp đội ngũ QA hiện tại tăng trưởng kỹ năng và năng lực kiểm soát.",
         COLOR_ACCENT,
         ["• Đào tạo, chuyển giao tri thức tận tâm cho đồng nghiệp",
          "• Lắng nghe phản hồi từ BA/PO/Dev để hoàn thiện quy trình",
          "• Tinh thần trách nhiệm cao nhất với chất lượng release"]),
        ("📈 CAM KẾT HIỆU QUẢ RÕ RÀNG",
         "Mang lại giá trị đo đếm được ngay trong tháng đầu tiên và tối ưu hóa chi phí vận hành cho toàn bộ tổ chức.",
         COLOR_SUCCESS,
         ["• Rút ngắn thời gian chuẩn bị test suite hoàn chỉnh",
          "• Độ chính xác dữ liệu kiểm thử đạt >= 92%",
          "• Giảm 50% lỗi lọt sang môi trường Production"])
    ]

    for i, (ptitle, pdesc, pcol, ppoints) in enumerate(pillars):
        pbox = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + i*(p_w7 + p_gap7), p_top7, p_w7, p_h7)
        pbox.fill.solid()
        pbox.fill.fore_color.rgb = COLOR_WHITE
        pbox.line.color.rgb = pcol
        pbox.line.width = Pt(1.5)
        tf_p = pbox.text_frame
        tf_p.word_wrap = True
        
        p = tf_p.paragraphs[0]
        p.text = ptitle
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = pcol
        p.space_after = Pt(4)
        
        p = tf_p.add_paragraph()
        p.text = pdesc
        p.font.size = Pt(9.5)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_after = Pt(8)

        for pt in ppoints:
            p_pt = tf_p.add_paragraph()
            p_pt.text = pt
            p_pt.font.size = Pt(9)
            p_pt.font.color.rgb = COLOR_TEXT_MUTED
            p_pt.space_after = Pt(3)

    # Light Theme Callout
    callout = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.15), Inches(11.7), Inches(0.85))
    callout.fill.solid()
    callout.fill.fore_color.rgb = COLOR_PRIMARY_LIGHT
    callout.line.color.rgb = COLOR_PRIMARY
    callout.line.width = Pt(1.5)
    tf_call = callout.text_frame
    tf_call.word_wrap = True
    
    p_c1 = tf_call.paragraphs[0]
    p_c1.text = "💬 \"Tôi không thay thế tester bằng AI — Tôi biến mỗi tester thành một Super QA có năng lực phân tích sâu, làm chủ công nghệ và kiểm soát chất lượng toàn diện!\""
    p_c1.font.size = Pt(11)
    p_c1.font.bold = True
    p_c1.font.color.rgb = COLOR_PRIMARY_DARK
    p_c1.alignment = PP_ALIGN.CENTER
    
    p_c2 = tf_call.add_paragraph()
    p_c2.text = "Sẵn sàng cống hiến và đồng hành cùng quý công ty ngay từ tuần đầu tiên 🤝"
    p_c2.font.size = Pt(10)
    p_c2.font.color.rgb = COLOR_PRIMARY
    p_c2.alignment = PP_ALIGN.CENTER

    out_interview = os.path.join(current_dir, "QA_AI_Assistant_Interview_Presentation.pptx")
    out_requirement = os.path.join(current_dir, "QA_Requirement_Assistant_Presentation.pptx")
    
    prs.save(out_interview)
    prs.save(out_requirement)
    print(f"Presentation saved successfully to:")
    print(f"  - {out_interview}")
    print(f"  - {out_requirement}")

if __name__ == "__main__":
    create_deck()
