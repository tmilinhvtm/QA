#!/usr/bin/env python3
"""
generate_presentation.py
Generates a professional 16:9 executive presentation for the QA AI Specialist interview.
Theme: Ant Design Blue (#1677FF), Slate (#1E293B, #64748B), Modern Enterprise QA.
"""

import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# --- Color Palette ---
COLOR_PRIMARY = RGBColor(22, 119, 255)       # Ant Design Blue #1677FF
COLOR_PRIMARY_DARK = RGBColor(9, 88, 217)   # Deep Blue #0958D9
COLOR_PRIMARY_LIGHT = RGBColor(230, 244, 255) # Light Blue Tint #E6F4FF
COLOR_TEXT_MAIN = RGBColor(30, 41, 59)      # Slate 800 #1E293B
COLOR_TEXT_MUTED = RGBColor(100, 116, 139)  # Slate 500 #64748B
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_BG_CARD = RGBColor(248, 250, 252)     # Slate 50 #F8FAFC
COLOR_BORDER = RGBColor(226, 232, 240)      # Slate 200 #E2E8F0
COLOR_SUCCESS = RGBColor(22, 163, 74)       # Emerald Green #16A34A
COLOR_SUCCESS_LIGHT = RGBColor(240, 253, 244)
COLOR_ACCENT = RGBColor(13, 148, 136)       # Teal #0D9488
COLOR_CARD_BORDER = RGBColor(203, 213, 225) # Slate 300 #CBD5E1

def create_deck():
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Helper: Add Standard Header
    def add_header(slide, title_text, category_tag, subtitle_text=None):
        # Top accent bar
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = COLOR_PRIMARY
        top_bar.line.fill.background()

        # Category Tag badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.4), Inches(2.2), Inches(0.35))
        badge.fill.solid()
        badge.fill.fore_color.rgb = COLOR_PRIMARY_LIGHT
        badge.line.color.rgb = COLOR_PRIMARY
        badge.line.width = Pt(1)
        tf_b = badge.text_frame
        tf_b.word_wrap = True
        p_b = tf_b.paragraphs[0]
        p_b.text = category_tag.upper()
        p_b.font.size = Pt(10)
        p_b.font.bold = True
        p_b.font.color.rgb = COLOR_PRIMARY_DARK
        p_b.alignment = PP_ALIGN.CENTER

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.7))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_MAIN

        if subtitle_text:
            p2 = tf.add_paragraph()
            p2.text = subtitle_text
            p2.font.size = Pt(12)
            p2.font.color.rgb = COLOR_TEXT_MUTED

    # =========================================================================
    # SLIDE 1: Title Slide (Executive Dark & Clean)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    
    # Background full shape
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = RGBColor(15, 23, 42) # Slate 900
    bg1.line.fill.background()

    # Accent glow top bar
    bar1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.2))
    bar1.fill.solid()
    bar1.fill.fore_color.rgb = COLOR_PRIMARY
    bar1.line.fill.background()

    # Title container
    tbox = s1.shapes.add_textbox(Inches(1.2), Inches(1.5), Inches(11.0), Inches(4.5))
    tf1 = tbox.text_frame
    tf1.word_wrap = True

    # Tag
    p_tag = tf1.paragraphs[0]
    p_tag.text = "CHIẾN LƯỢC ỨNG DỤNG AI TRONG KIỂM THỬ PHẦN MỀM (AI-DRIVEN QA LEAD)"
    p_tag.font.size = Pt(13)
    p_tag.font.bold = True
    p_tag.font.color.rgb = COLOR_PRIMARY
    p_tag.space_after = Pt(14)

    # Main Headline
    p_main = tf1.add_paragraph()
    p_main.text = "Tối Ưu Năng Suất (Effort) & Đảm Bảo Tính Đúng Đắn\nBộ Dữ Liệu QA Bằng Tác Tử AI Trong 3 Tháng"
    p_main.font.size = Pt(30)
    p_main.font.bold = True
    p_main.font.color.rgb = COLOR_WHITE
    p_main.space_after = Pt(18)

    # Subtitle
    p_sub = tf1.add_paragraph()
    p_sub.text = "Mô hình thực chiến: Antigravity Native Plugin • 2-Phase State Machine • 3 Tầng Kiểm Chứng Sâu"
    p_sub.font.size = Pt(15)
    p_sub.font.color.rgb = RGBColor(148, 163, 184) # Slate 400
    p_sub.space_after = Pt(36)

    # Candidate Meta
    p_meta = tf1.add_paragraph()
    p_meta.text = "Ứng viên: Vũ Thị Mai Linh  |  Vị trí: AI QA Specialist / Senior QA Engineer  |  Tháng 10/2026"
    p_meta.font.size = Pt(13)
    p_meta.font.color.rgb = RGBColor(203, 213, 225)

    # Highlight Card on Slide 1
    card_kpi = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(5.6), Inches(10.9), Inches(1.2))
    card_kpi.fill.solid()
    card_kpi.fill.fore_color.rgb = RGBColor(30, 41, 59)
    card_kpi.line.color.rgb = COLOR_PRIMARY
    card_kpi.line.width = Pt(1.5)
    tf_kpi = card_kpi.text_frame
    tf_kpi.word_wrap = True
    p_kpi1 = tf_kpi.paragraphs[0]
    p_kpi1.text = "🎯 MỤC TIÊU 90 NGÀY CAM KẾT VỚI DOANH NGHIỆP:"
    p_kpi1.font.size = Pt(11)
    p_kpi1.font.bold = True
    p_kpi1.font.color.rgb = COLOR_PRIMARY
    p_kpi2 = tf_kpi.add_paragraph()
    p_kpi2.text = "1. Nâng Effort (Throughput) Team lên gấp 2.5x  •  2. Độ Chính Xác (Accuracy/Ground Truth) Bộ Dữ Liệu Đầu Ra ≥ 92%  •  3. Giảm 50% Defect Lọt Sang Dev/Prod"
    p_kpi2.font.size = Pt(12)
    p_kpi2.font.bold = True
    p_kpi2.font.color.rgb = COLOR_WHITE

    # =========================================================================
    # SLIDE 2: Bối Cảnh, Nỗi Đau & Bài Toán Cốt Lõi
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Bối Cảnh & Bài Toán Cốt Lõi: Năng Suất (Effort) vs. Độ Đúng Sai Dữ Liệu", "1. Problem & Opportunity",
               "Vì sao các giải pháp AI Test Case thông thường đều thất bại và tiêu chuẩn mới của chúng ta là gì?")

    # 3 Column Cards
    col_width = Inches(3.7)
    col_gap = Inches(0.3)
    col_top = Inches(1.8)
    col_height = Inches(5.1)

    # Card 1: Nỗi đau QA truyền thống
    c1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), col_top, col_width, col_height)
    c1.fill.solid()
    c1.fill.fore_color.rgb = COLOR_BG_CARD
    c1.line.color.rgb = COLOR_CARD_BORDER
    tf_c1 = c1.text_frame
    tf_c1.word_wrap = True
    
    p = tf_c1.paragraphs[0]
    p.text = "🚨 NỖI ĐAU EFFORT HIỆN TẠI"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RGBColor(225, 29, 72)
    p.space_after = Pt(10)
    
    bullets_1 = [
        "60-70% Thời gian QA bị chôn vào việc đọc requirement mập mờ và gõ test case thủ công lặp lại.",
        "Năng suất thấp: Trung bình 1 QA chỉ phân tích được 2-3 User Stories phức tạp mỗi sprint.",
        "Thiếu chiều sâu kỹ thuật: Bỏ sót các lỗi rủi ro kiến trúc cao (Race Condition, State Drift, Timeout).",
        "Tắc nghẽn bàn giao: Dev chờ Test Case, QA chờ BA chốt yêu cầu, kéo dài lead-time release."
    ]
    for b in bullets_1:
        p_b = tf_c1.add_paragraph()
        p_b.text = "• " + b
        p_b.font.size = Pt(11)
        p_b.font.color.rgb = COLOR_TEXT_MAIN
        p_b.space_after = Pt(8)

    # Card 2: Cạm bẫy khi dùng AI ngây thơ (Naive AI)
    c2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + col_width + col_gap, col_top, col_width, col_height)
    c2.fill.solid()
    c2.fill.fore_color.rgb = COLOR_BG_CARD
    c2.line.color.rgb = COLOR_CARD_BORDER
    tf_c2 = c2.text_frame
    tf_c2.word_wrap = True
    
    p = tf_c2.paragraphs[0]
    p.text = "⚠️ BẪY 'ẢO GIÁC' CỦA AI CHUNG CHUNG"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RGBColor(217, 119, 6) # Amber
    p.space_after = Pt(10)
    
    bullets_2 = [
        "Vấn đề 'Garbage In - Garbage Out': Requirement thiếu ngữ cảnh dẫn đến test case sinh ra sai hoàn toàn.",
        "Ảo giác (Hallucination): Tự bịa API endpoint, tự suy diễn quy tắc sai so với luồng nghiệp vụ thực tế.",
        "Gộp cụm hành động (Action Bundling): Dồn chọn số lượng + thanh toán + click vào 1 bước, dev không thể chạy Automation.",
        "Kỳ vọng chung chung: Chỉ ghi 'Verify HTTP 200' mà không có JSON Body hay thay đổi dữ liệu Database."
    ]
    for b in bullets_2:
        p_b = tf_c2.add_paragraph()
        p_b.text = "• " + b
        p_b.font.size = Pt(11)
        p_b.font.color.rgb = COLOR_TEXT_MAIN
        p_b.space_after = Pt(8)

    # Card 3: Giải pháp kiến trúc của chúng ta
    c3 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + (col_width + col_gap)*2, col_top, col_width, col_height)
    c3.fill.solid()
    c3.fill.fore_color.rgb = COLOR_PRIMARY_LIGHT
    c3.line.color.rgb = COLOR_PRIMARY
    c3.line.width = Pt(1.5)
    tf_c3 = c3.text_frame
    tf_c3.word_wrap = True
    
    p = tf_c3.paragraphs[0]
    p.text = "✨ GIẢI PHÁP ĐỘT PHÁ CỦA REPO"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(10)
    
    bullets_3 = [
        "Strict 2-Phase State Machine: Chặn cổng duyệt người (Human Gate 1), yêu cầu chốt logic trước khi sinh test.",
        "3 Nguyên Tắc Vàng QA/QC: Step Disaggregation (Tách bước) + 3 Tầng kiểm chứng sâu (UI/API Body/DB State).",
        "Anchoring Kho Bug Thực Tế: Đối chiếu 10 Bug Production Patterns chuẩn hóa chống ảo giác.",
        "Local-First & Drive Sync: Lưu trữ tích lũy (Append-Only) và đẩy lên Google Sheets Enterprise thời gian thực."
    ]
    for b in bullets_3:
        p_b = tf_c3.add_paragraph()
        p_b.text = "✔ " + b
        p_b.font.size = Pt(11)
        p_b.font.bold = True
        p_b.font.color.rgb = COLOR_TEXT_MAIN
        p_b.space_after = Pt(8)

    # =========================================================================
    # SLIDE 3: Kiến Trúc Hệ Thống: 2-Phase State Machine & Subagents
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Kiến Trúc Tác Tử: 2-Phase State Machine & Human Gates", "2. Architecture & Design",
               "Hệ thống Native Plugin không cần Backend cồng kềnh - Vận hành bằng Orchestrator và 2 Subagents độc lập.")

    # Left Column: State Machine Flow
    w_left = Inches(5.7)
    c_left = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), w_left, Inches(5.1))
    c_left.fill.solid()
    c_left.fill.fore_color.rgb = COLOR_BG_CARD
    c_left.line.color.rgb = COLOR_CARD_BORDER
    tf_l = c_left.text_frame
    tf_l.word_wrap = True

    p = tf_l.paragraphs[0]
    p.text = "🔄 QUY TRÌNH ĐIỀU PHỐI 2 PHA NGHIÊM NGẶT"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    p.space_after = Pt(8)

    steps = [
        ("BƯỚC 0: PRE-FLIGHT CACHE VALIDATION", "Kiểm tra Drive modifiedTime vs .sync_metadata.json. Offline Fallback tự động khi mất mạng."),
        ("PHASE 1: STATIC ANALYSIS (req-risk-analyst)", "Bóc tách 4 thành tố Business Rules • Đặt câu hỏi phản biện BA • Quét 5 rủi ro kỹ thuật sâu • Đối chiếu 10 Bug lịch sử."),
        ("🛑 HUMAN GATE 1 (CỔNG KIỂM SOÁT 1)", "BẮT BUỘC DỪNG! Tester duyệt & tinh chỉnh logic. Rollback ngay nếu requirement thay đổi."),
        ("PHASE 2: TEST DESIGN (test-automation-architect)", "Sinh 5 kịch bản chuẩn: Happy Path, Boundary, Negative, Concurrency (≤50ms), State Conflict & Recovery."),
        ("🛑 HUMAN GATE 2 & SYNC CLOUD", "Tester xác nhận kịch bản -> Append vào local JSON -> Đẩy lên Google Sheets Master qua MCP.")
    ]
    for stitle, sdesc in steps:
        p_st = tf_l.add_paragraph()
        p_st.text = stitle
        p_st.font.size = Pt(10)
        p_st.font.bold = True
        p_st.font.color.rgb = COLOR_TEXT_MAIN
        
        p_sd = tf_l.add_paragraph()
        p_sd.text = sdesc
        p_sd.font.size = Pt(9.5)
        p_sd.font.color.rgb = COLOR_TEXT_MUTED
        p_sd.space_after = Pt(6)

    # Right Column: Subagents & Specialization
    w_right = Inches(5.7)
    c_right = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), w_right, Inches(5.1))
    c_right.fill.solid()
    c_right.fill.fore_color.rgb = COLOR_WHITE
    c_right.line.color.rgb = COLOR_PRIMARY
    c_right.line.width = Pt(1.5)
    tf_r = c_right.text_frame
    tf_r.word_wrap = True

    p = tf_r.paragraphs[0]
    p.text = "🤖 PHÂN QUYỀN TÁC TỬ & BỘ NHỚ GÓC NHÌN"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(10)

    subagent_items = [
        ("Subagent 1: req-risk-analyst", 
         "Đảm nhiệm Static Analysis. Tham chiếu risk-checklist.md bao gồm 5 góc khuất: Concurrency, State Drift, Clock Drift, Non-Idempotency, Distributed Transaction Failure. Tuyệt đối không sinh test case."),
        ("Subagent 2: test-automation-architect", 
         "Chỉ được kích hoạt khi Phase 1 đã duyệt. Áp dụng test-design-matrix.md để xếp hạng độ ưu tiên P1/P2/P3 và mô tả chi tiết bước giả lập 3 tầng."),
        ("Bộ nhớ góc nhìn (Perspective Persistence)", 
         "Lưu tại user_preferences.json: Hỗ trợ 3 chế độ: 'business' (ngôn ngữ đời sống trực quan cho BA), 'technical' (thuật ngữ SDET chuyên sâu), 'hybrid'. Tự động ghi nhớ qua các phiên."),
        ("Cơ chế Progressive Disclosure", 
         "Tối ưu hóa Token & Context Window: Cẩm nang kỹ thuật được chia nhỏ vào thư mục references/ thay vì nhồi nhét vào prompt chính, tránh làm loãng context.")
    ]
    for stitle, sdesc in subagent_items:
        p_st = tf_r.add_paragraph()
        p_st.text = "🔹 " + stitle
        p_st.font.size = Pt(11)
        p_st.font.bold = True
        p_st.font.color.rgb = COLOR_PRIMARY_DARK
        
        p_sd = tf_r.add_paragraph()
        p_sd.text = sdesc
        p_sd.font.size = Pt(9.5)
        p_sd.font.color.rgb = COLOR_TEXT_MAIN
        p_sd.space_after = Pt(6)

    # =========================================================================
    # SLIDE 4: Đánh Giá Tính Đúng - Sai Của Bộ Dữ Liệu Đầu Ra (Core Evaluation)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Khung Đánh Giá & Kiểm Định Độ Đúng Sai Của Dữ Liệu Đầu Ra", "3. Quality & Accuracy Assurance",
               "Làm thế nào để đo lường, kiểm soát ảo giác và đảm bảo dữ liệu sinh ra đạt chuẩn kiểm thử thực tế?")

    # Top KPI 4 Cards
    kpi_w = Inches(2.7)
    kpi_h = Inches(1.3)
    kpi_gap = Inches(0.3)
    kpi_top = Inches(1.8)

    metrics = [
        ("SEMANTIC ACCURACY", "≥ 92%", "Tính đúng đắn logic & quy tắc nghiệp vụ", COLOR_PRIMARY),
        ("SCHEMA VALIDITY", "100%", "Chuẩn 3 tầng UI/API Body/DB & Disaggregation", COLOR_SUCCESS),
        ("RISK COVERAGE", "100%", "Bao phủ đủ 5 nhóm kịch bản & 5 góc khuất", COLOR_PRIMARY_DARK),
        ("HALLUCINATION", "< 5%", "Tỷ lệ suy diễn sai lệch so với requirement", RGBColor(225, 29, 72))
    ]
    for i, (mtitle, mval, msub, mcol) in enumerate(metrics):
        box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + (kpi_w + kpi_gap)*i, kpi_top, kpi_w, kpi_h)
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_BG_CARD
        box.line.color.rgb = mcol
        box.line.width = Pt(1.5)
        tf_m = box.text_frame
        tf_m.word_wrap = True
        
        p1 = tf_m.paragraphs[0]
        p1.text = mtitle
        p1.font.size = Pt(9)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_TEXT_MUTED
        
        p2 = tf_m.add_paragraph()
        p2.text = mval
        p2.font.size = Pt(22)
        p2.font.bold = True
        p2.font.color.rgb = mcol
        
        p3 = tf_m.add_paragraph()
        p3.text = msub
        p3.font.size = Pt(8.5)
        p3.font.color.rgb = COLOR_TEXT_MAIN

    # Bottom Split: 3 Golden Principles vs. Verification Framework
    b_top = Inches(3.35)
    b_h = Inches(3.6)
    b_w = Inches(5.7)

    # Box 1: 3 Nguyên Tắc Vàng
    c_gp = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), b_top, b_w, b_h)
    c_gp.fill.solid()
    c_gp.fill.fore_color.rgb = COLOR_WHITE
    c_gp.line.color.rgb = COLOR_CARD_BORDER
    tf_gp = c_gp.text_frame
    tf_gp.word_wrap = True
    
    p = tf_gp.paragraphs[0]
    p.text = "💎 3 NGUYÊN TẮC VÀNG CHUẨN QA/QC THỰC CHIẾN"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    p.space_after = Pt(8)

    gp_items = [
        ("1. Step Disaggregation (Không gom cụm hành động):",
         "Tách biệt hoàn toàn bước chuẩn bị dữ liệu (nhập input/chọn option) và bước kích hoạt (submit). Đưa tiền đề vào Pre-conditions để Automation chạy ổn định."),
        ("2. Synchronized Deep Verification (Kiểm chứng sâu 3 tầng):",
         "UI: Thông báo, highlight, ID hiển thị.\nAPI: HTTP Status + trường cụ thể trong Response Body (ví dụ: order_id khớp UI).\nDB & Broker: Tên bảng, tên cột, giá trị cập nhật và Kafka event phát ra."),
        ("3. Trạng thái thực thi rõ ràng (Execution Status):",
         "Mặc định là NOT_RUN kèm dropdown Pass/Fail/Blocked và Conditional Formatting giúp theo dõi tiến độ trực quan.")
    ]
    for gtitle, gdesc in gp_items:
        p_t = tf_gp.add_paragraph()
        p_t.text = gtitle
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN
        p_d = tf_gp.add_paragraph()
        p_d.text = gdesc
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = COLOR_TEXT_MUTED
        p_d.space_after = Pt(4)

    # Box 2: Cơ Chế Đánh Giá Thực Tế (Evaluation Loop)
    c_ev = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), b_top, b_w, b_h)
    c_ev.fill.solid()
    c_ev.fill.fore_color.rgb = COLOR_WHITE
    c_ev.line.color.rgb = COLOR_CARD_BORDER
    tf_ev = c_ev.text_frame
    tf_ev.word_wrap = True
    
    p = tf_ev.paragraphs[0]
    p.text = "🛡️ CƠ CHẾ ĐẢM BẢO CHẤT LƯỢNG DỮ LIỆU ĐẦU RA"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT
    p.space_after = Pt(8)

    ev_items = [
        ("Anchor bằng Ground Truth (Kho 10 Bug Lịch Sử):",
         "Agent luôn đối chiếu rủi ro với các bug thực chiến đã xảy ra trên hệ thống (BUG-001 đến BUG-010), buộc AI căn cứ vào bài học thực tế thay vì suy diễn viển vông."),
        ("Syntactic & Schema Validator:",
         "Quy chuẩn kiểm tra tự động: Mọi test case thiếu bảng DB hoặc thiếu trường API Response Body đều bị từ chối trước khi hiển thị cho Tester."),
        ("Human-in-the-Loop Feedback Loop:",
         "Tester là 'Quality Gatekeeper' cuối cùng. Mọi câu hỏi BA và rủi ro được Tester xác nhận, tạo dữ liệu chuẩn xác cho Phase 2 sinh kịch bản."),
        ("Traceability Không Rời Rạc:",
         "Khóa ngoại requirement_id kết nối xuyên suốt từ bảng Phân tích Yêu cầu sang bảng Kịch bản Test, đảm bảo 100% test case đều truy vết được nguồn gốc.")
    ]
    for etitle, edesc in ev_items:
        p_t = tf_ev.add_paragraph()
        p_t.text = etitle
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN
        p_d = tf_ev.add_paragraph()
        p_d.text = edesc
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = COLOR_TEXT_MUTED
        p_d.space_after = Pt(4)

    # =========================================================================
    # SLIDE 5: Minh Chứng Thực Nghiệm Trên 3 Requirement Mẫu
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Minh Chứng Thực Nghiệm: Bắt Lỗ Hổng & Tự Nắn Chỉnh Qua Thực Tế", "4. Experimental Proof Points",
               "Bằng chứng cụ thể từ Repo: Những điểm làm tốt, sai sót ban đầu được phát hiện và khắc phục ra sao.")

    # Table of 3 Case Studies
    rows = 4
    cols = 4
    left_t = Inches(0.8)
    top_t = Inches(1.8)
    w_t = Inches(11.7)
    h_t = Inches(5.1)

    table_shape = s5.shapes.add_table(rows, cols, left_t, top_t, w_t, h_t)
    table = table_shape.table

    # Column widths
    table.columns[0].width = Inches(2.2) # Tiêu chí
    table.columns[1].width = Inches(3.1) # Req A (Auth)
    table.columns[2].width = Inches(3.2) # Req B (Inventory)
    table.columns[3].width = Inches(3.2) # Req C (Voucher)

    headers_table = ["TIÊU CHÍ ĐÁNH GIÁ", "REQ A: KHÓA TÀI KHOẢN (Auth)", "REQ B: CHỐNG BÁN ÂM KHO (Inventory)", "REQ C: VOUCHER 1 LẦN (Promotion)"]
    for j, htext in enumerate(headers_table):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_PRIMARY
        p = cell.text_frame.paragraphs[0]
        p.text = htext
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

    row_data = [
        ("Điểm làm tốt nổi bật",
         "• Phát hiện kẽ hở Force Logout / Thu hồi Token tức thì trên thiết bị khác.\n• Đặt câu hỏi Sliding Window đếm sai.\n• Liên kết BUG-001, BUG-003, BUG-008.",
         "• Phân biệt rõ Tồn kho vật lý vs Tồn kho khả dụng (Holding Window).\n• Thiết kế test Concurrency: 2 user tranh mua 1 hàng cuối (N=1) trong ≤50ms.\n• Ánh xạ BUG-005, BUG-007.",
         "• Bóc tách trọn vẹn Vòng đời Voucher & Giao dịch bù trừ (Compensating Transaction) khi hủy đơn/timeout.\n• Bắt lỗi Race condition 2 tab đồng thời.\n• Ánh xạ BUG-003 chuẩn 100%."),
        ("Sai sót ban đầu phát hiện",
         "• Lạm dụng thuật ngữ hàn lâm (Lost Update, Redis INCR) khiến BA khó hiểu.\n• Bố cục dạng khối văn bản dài (Text Wall).\n• Bỏ sót kiểm tra Token trên service vệ tinh.",
         "• Gom cụm hành động: dồn chọn số lượng + checkout vào 1 bước.\n• Kỳ vọng API/DB sơ sài (chỉ ghi HTTP 200/400, không chỉ rõ tên bảng/cột).\n• Bảng Sheets ban đầu bị co rúm, xấu.",
         "• Bỏ sót chính sách hoàn tiền 1 phần khi mua nhiều món có áp voucher.\n• Bỏ sót nguy cơ kẹt voucher vĩnh viễn ở trạng thái tạm khóa (RESERVED) nếu cronjob timeout chết."),
        ("Cải tiến Prompt & Code",
         "• Thêm cấu hình user_preferences.json ghi nhớ góc nhìn (business vs technical).\n• Tái cấu trúc sang dạng Thẻ & Bảng Ma trận.\n• Bổ sung kịch bản kiểm tra Event thu hồi Token.",
         "• Đưa 3 Nguyên Tắc Vàng vào prompt & AGENTS.md (Tách bước, Verify 3 tầng).\n• Viết script Styler Ant Design Blue tự động định dạng Sheets, thêm Dropdown Status.",
         "• Mở rộng risk-checklist.md thêm rủi ro Lifecycle Reversal & Partial Refund.\n• Bổ sung kịch bản kiểm chứng khôi phục voucher tự động khi hết hạn giữ chỗ.")
    ]

    for i, row in enumerate(row_data):
        for j, val in enumerate(row):
            cell = table.cell(i+1, j)
            cell.fill.solid()
            if j == 0:
                cell.fill.fore_color.rgb = COLOR_BG_CARD
            else:
                cell.fill.fore_color.rgb = COLOR_WHITE
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(9.5)
            if j == 0:
                p.font.bold = True
                p.font.color.rgb = COLOR_PRIMARY_DARK
            else:
                p.font.color.rgb = COLOR_TEXT_MAIN

    # =========================================================================
    # SLIDE 6: Kế Hoạch 3 Tháng Nâng Vọt Effort Của Team (The 90-Day Roadmap)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Lộ Trình 3 Tháng: Nâng 2.5x Effort Của Team QA", "5. The 90-Day Roadmap",
               "Kế hoạch triển khai thực chiến từng giai đoạn để biến AI thành bệ phóng năng suất cho toàn bộ QA Team.")

    r_w = Inches(3.7)
    r_gap = Inches(0.3)
    r_top = Inches(1.8)
    r_h = Inches(5.1)

    # Month 1
    m1 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), r_top, r_w, r_h)
    m1.fill.solid()
    m1.fill.fore_color.rgb = COLOR_BG_CARD
    m1.line.color.rgb = COLOR_CARD_BORDER
    tf_m1 = m1.text_frame
    tf_m1.word_wrap = True
    
    p = tf_m1.paragraphs[0]
    p.text = "THÁNG 1: FOUNDATION & BASELINE"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    p_sub = tf_m1.add_paragraph()
    p_sub.text = "Chuẩn Hóa Quy Trình & Pilot Thử Nghiệm"
    p_sub.font.size = Pt(13)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_TEXT_MAIN
    p_sub.space_after = Pt(8)

    m1_points = [
        ("Xây dựng Golden Dataset:", "Chuẩn bị 50 User Stories thực tế kèm kịch bản mẫu của dự án làm thước đo Ground Truth."),
        ("Đóng gói Agentic Plugin:", "Cài đặt bộ Rules, Skills, Subagents cho 1 Scrum Team (3-5 QA) thử nghiệm."),
        ("Training & Guideline:", "Đào tạo QA cách review Phase 1, chất vấn BA và phê duyệt kịch bản giả lập."),
        ("🎯 KPI Tháng 1:", "• Độ chính xác dữ liệu ≥ 85%\n• Giảm 40% thời gian viết test case\n• Bắt sớm ít nhất 5 lỗi logic ngay khâu review requirement.")
    ]
    for ptitle, pdesc in m1_points:
        p_t = tf_m1.add_paragraph()
        p_t.text = "• " + ptitle
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_PRIMARY_DARK if "KPI" in ptitle else COLOR_TEXT_MAIN
        p_d = tf_m1.add_paragraph()
        p_d.text = pdesc
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = COLOR_SUCCESS if "KPI" in ptitle else COLOR_TEXT_MUTED
        p_d.space_after = Pt(4)

    # Month 2
    m2 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + r_w + r_gap, r_top, r_w, r_h)
    m2.fill.solid()
    m2.fill.fore_color.rgb = COLOR_BG_CARD
    m2.line.color.rgb = COLOR_CARD_BORDER
    tf_m2 = m2.text_frame
    tf_m2.word_wrap = True
    
    p = tf_m2.paragraphs[0]
    p.text = "THÁNG 2: INTEGRATION & SCALING"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT
    p_sub = tf_m2.add_paragraph()
    p_sub.text = "Tích Hợp Hệ Sinh Thái & Mở Rộng"
    p_sub.font.size = Pt(13)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_TEXT_MAIN
    p_sub.space_after = Pt(8)

    m2_points = [
        ("Tích hợp Jira / Xray MCP:", "Kết nối trực tiếp Jira để đọc Story Description và sync ngược Test Cases lên Xray/TestRail."),
        ("Cơ chế Feedback Loop:", "Thêm tính năng Upvote/Downvote test case để liên tục nắn chỉnh Prompt theo văn hóa công ty."),
        ("Mở rộng ra toàn bộ QA Team:", "Áp dụng cho 10-15 QA trên toàn bộ các squad."),
        ("🎯 KPI Tháng 2:", "• Độ chính xác dữ liệu ≥ 92%\n• Giảm 60% lead-time phân tích & test design\n• Tăng gấp 3 lần số kịch bản Concurrency & Edge-case được bao phủ.")
    ]
    for ptitle, pdesc in m2_points:
        p_t = tf_m2.add_paragraph()
        p_t.text = "• " + ptitle
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_ACCENT if "KPI" in ptitle else COLOR_TEXT_MAIN
        p_d = tf_m2.add_paragraph()
        p_d.text = pdesc
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = COLOR_SUCCESS if "KPI" in ptitle else COLOR_TEXT_MUTED
        p_d.space_after = Pt(4)

    # Month 3
    m3 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + (r_w + r_gap)*2, r_top, r_w, r_h)
    m3.fill.solid()
    m3.fill.fore_color.rgb = COLOR_PRIMARY_LIGHT
    m3.line.color.rgb = COLOR_PRIMARY
    m3.line.width = Pt(1.5)
    tf_m3 = m3.text_frame
    tf_m3.word_wrap = True
    
    p = tf_m3.paragraphs[0]
    p.text = "THÁNG 3: AUTONOMOUS MULTIPLIER"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p_sub = tf_m3.add_paragraph()
    p_sub.text = "Sinh Automation Code & Đột Phá Effort"
    p_sub.font.size = Pt(13)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_TEXT_MAIN
    p_sub.space_after = Pt(8)

    m3_points = [
        ("Simulated to Executable Code:", "Chuyển đổi các bước giả lập 3 tầng thành Playwright Script / k6 Load Script chạy trực tiếp."),
        ("CI/CD Regression Trigger:", "Tự động chạy test case P1 ngay khi Dev tạo Pull Request."),
        ("Đo lường & Báo cáo ROI:", "Dashboard đo lường Defect Leakage Rate, QA Throughput và Man-hours saved."),
        ("🎯 KPI Tháng 3:", "• Nâng Effort (Throughput) Team lên GẤP 2.5X\n• Giảm 50% bug lọt sang môi trường Staging/Prod\n• Tiết kiệm 15-20 giờ làm việc/QA/sprint.")
    ]
    for ptitle, pdesc in m3_points:
        p_t = tf_m3.add_paragraph()
        p_t.text = "• " + ptitle
        p_t.font.size = Pt(10)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_PRIMARY_DARK if "KPI" in ptitle else COLOR_TEXT_MAIN
        p_d = tf_m3.add_paragraph()
        p_d.text = pdesc
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = COLOR_SUCCESS if "KPI" in ptitle else COLOR_TEXT_MUTED
        p_d.space_after = Pt(4)

    # =========================================================================
    # SLIDE 7: Kết Luận & Định Hướng Đóng Góp (Closing & Value Proposition)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Kết Luận: Chuyển Dịch Vị Thế QA Từ 'Thủ Công' Sang 'AI Orchestrator'", "6. Strategic Conclusion",
               "Giá trị mang lại cho đội ngũ và định hướng phát triển sự nghiệp tại doanh nghiệp.")

    # 3 Summary Pillar Cards
    c_w7 = Inches(3.7)
    c_gap7 = Inches(0.3)
    c_top7 = Inches(1.8)
    c_h7 = Inches(4.0)

    # Card 1: Tư duy sản phẩm
    card1 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), c_top7, c_w7, c_h7)
    card1.fill.solid()
    card1.fill.fore_color.rgb = COLOR_BG_CARD
    card1.line.color.rgb = COLOR_CARD_BORDER
    tf_c1 = card1.text_frame
    tf_c1.word_wrap = True
    p = tf_c1.paragraphs[0]
    p.text = "🎯 TƯ DUY KIỂM ĐỊNH SỚM (SHIFT-LEFT)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    p.space_after = Pt(10)
    texts_1 = [
        "AI không chỉ giúp viết test nhanh hơn, mà giúp QA chặn đứng lỗi ngay từ khâu viết requirement.",
        "Bộ câu hỏi chất vấn BA sắc bén giúp cả team Dev & Product cùng nhìn thấy góc khuất trước khi viết code.",
        "Chi phí sửa lỗi ở giai đoạn Requirement rẻ hơn gấp 10-30 lần so với sửa lỗi ở Production."
    ]
    for t in texts_1:
        p_t = tf_c1.add_paragraph()
        p_t.text = "• " + t
        p_t.font.size = Pt(10.5)
        p_t.font.color.rgb = COLOR_TEXT_MAIN
        p_t.space_after = Pt(8)

    # Card 2: Chất lượng dữ liệu
    card2 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + c_w7 + c_gap7, c_top7, c_w7, c_h7)
    card2.fill.solid()
    card2.fill.fore_color.rgb = COLOR_BG_CARD
    card2.line.color.rgb = COLOR_CARD_BORDER
    tf_c2 = card2.text_frame
    tf_c2.word_wrap = True
    p = tf_c2.paragraphs[0]
    p.text = "🛡️ DỮ LIỆU ĐÚNG ĐẮN LÀ TỐI THƯỢNG"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_SUCCESS
    p.space_after = Pt(10)
    texts_2 = [
        "Không đánh đổi tốc độ lấy ảo giác (hallucination). Human-in-the-loop là nguyên tắc bất di bất dịch.",
        "Quy chuẩn kiểm chứng sâu 3 tầng (UI/API Body/DB Schema) giúp test case có thể tự động hóa ngay mà không cần làm lại.",
        "Cơ chế Local-First & Cloud Sync giúp dữ liệu được tích lũy bền vững, không bao giờ mất mát."
    ]
    for t in texts_2:
        p_t = tf_c2.add_paragraph()
        p_t.text = "• " + t
        p_t.font.size = Pt(10.5)
        p_t.font.color.rgb = COLOR_TEXT_MAIN
        p_t.space_after = Pt(8)

    # Card 3: Nâng tầm vai trò QA
    card3 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + (c_w7 + c_gap7)*2, c_top7, c_w7, c_h7)
    card3.fill.solid()
    card3.fill.fore_color.rgb = COLOR_PRIMARY_LIGHT
    card3.line.color.rgb = COLOR_PRIMARY
    card3.line.width = Pt(1.5)
    tf_c3 = card3.text_frame
    tf_c3.word_wrap = True
    p = tf_c3.paragraphs[0]
    p.text = "🚀 NÂNG TẦM VỊ THẾ CỦA QA"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(10)
    texts_3 = [
        "QA không còn là 'người gõ test case thủ công' mà trở thành 'AI QA Orchestrator & System Thinker'.",
        "Giải phóng 60% thời gian cơ bắp để QA tập trung vào Exploratory Testing, Security, Performance và AI Tuning.",
        "Sẵn sàng dẫn dắt team QA của quý công ty chuyển đổi số thành công bằng các công cụ AI thực chiến."
    ]
    for t in texts_3:
        p_t = tf_c3.add_paragraph()
        p_t.text = "✔ " + t
        p_t.font.size = Pt(10.5)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN
        p_t.space_after = Pt(8)

    # Bottom Callout on Slide 7
    callout = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.0), Inches(11.7), Inches(1.0))
    callout.fill.solid()
    callout.fill.fore_color.rgb = RGBColor(15, 23, 42)
    callout.line.color.rgb = COLOR_PRIMARY
    tf_call = callout.text_frame
    tf_call.word_wrap = True
    p_c1 = tf_call.paragraphs[0]
    p_c1.text = "💬 'Mục tiêu của tôi không phải là thay thế QA bằng AI, mà là biến mỗi QA trong team thành một Super QA có năng suất và tầm nhìn gấp 3 lần.'"
    p_c1.font.size = Pt(12)
    p_c1.font.bold = True
    p_c1.font.color.rgb = COLOR_WHITE
    p_c1.alignment = PP_ALIGN.CENTER
    p_c2 = tf_call.add_paragraph()
    p_c2.text = "Sẵn sàng trao đổi chi tiết và thực chiến cùng quý công ty ngay ngày mai!"
    p_c2.font.size = Pt(11)
    p_c2.font.color.rgb = RGBColor(148, 163, 184)
    p_c2.alignment = PP_ALIGN.CENTER

    # Save presentation
    output_path = "/home/linh/code/QA/docs/QA_AI_Assistant_Interview_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to {output_path}")

if __name__ == "__main__":
    create_deck()
