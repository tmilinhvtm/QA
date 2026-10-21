# REQUIREMENT QA ASSISTANT — ANTIGRAVITY NATIVE PLUGIN

> **Ứng viên:** Vũ Thị Mai Linh  
> **Dự án:** Trợ lý AI Phân tích Requirement & Tự động sinh Kịch bản Test 
> **Nền tảng:** Antigravity Customization Plugin (Rules, Skills, Subagents & Google Workspace MCP)  
> **Google Spreadsheet Master (Trực tiếp trên Drive):** [Xem Master Sheet tại đây](https://docs.google.com/spreadsheets/d/1BG5HNlQBEqyG_hjM9WwklrME2lZbysNFHBSggsSQetk/edit)  
> **Google Slides Thuyết Trình Phỏng Vấn:** [Xem Google Slides tại đây](https://docs.google.com/presentation/d/1h1JpMhKIRf5wjqcwC-nGmCjU5mCCH5jNxw2e2ybTyWQ/edit?usp=drivesdk)  
> **Video Demo Trực Tiếp:** [Tại đây](https://drive.google.com/file/d/1B09n2Vz652U4Ix9ivEHpQdl33lM1tOpS/view?usp=sharing)

---

* **Giới thiệu toàn bộ luồng hoạt động:**
  1. *Input:* Tester gửi requirement tự nhiên vào Antigravity IDE.
  2. *Phase 1:* Subagent `req-risk-analyst` bóc tách 4 thành tố nghiệp vụ, chất vấn BA kèm các phương án gợi ý trả lời (Option A, Option B, Recommended), phân tích 5 góc khuất kỹ thuật (Concurrency, State Drift) và đối chiếu kho bug lịch sử.
  3. *Human Gate 1:* Dừng lại chờ Tester phê duyệt & tinh chỉnh.
  4. *Phase 2:* Chuyển giao sang `test-automation-architect` thiết kế bộ kịch bản kiểm thử giả lập 3 tầng sâu (UI/API Body/DB) theo thứ tự ưu tiên P1/P2/P3, kế thừa toàn bộ data Phase 1 (BA Decisions, Technical Risks, Bug patterns) và mở rộng linh hoạt không giới hạn ở 5 test cases.
  5. *Human Gate 2 & Phase 3:* Tester duyệt, Antigravity đẩy dữ liệu tích lũy thêm mới (Append-Only) lên Google Spreadsheet Master với định dạng chuẩn Enterprise Ant Design Blue.

---

## 1. Cấu Trúc Plugin Antigravity Chuẩn (Native Customization)

Dự án được đóng gói 100% theo chuẩn **Antigravity Customization System** (không sử dụng mã nguồn backend CRUD truyền thống), đặt tại thư mục `.agents/`:

```text
QA/
├── .agents/
│   ├── rules/
│   │   └── qa-requirement-protocol.md  # Antigravity Rules (Luật điều phối 2-Phase, Human Gates & Local-First)
│   ├── skills/
│   │   └── qa-requirement-assistant/   # Master Skill Bundle
│   │       ├── references/             # Progressive Disclosure (Cẩm nang kỹ thuật chuyên sâu)
│   │       │   ├── risk-checklist.md   # Khung 5 góc khuất kỹ thuật (Concurrency, State Drift...)
│   │       │   └── test-design-matrix.md # Ma trận 5 loại kịch bản nền tảng & mở rộng động không giới hạn
│   │       └── scripts/
│   │           └── google_sheets_sync_manager.py # Đồng bộ 2 chiều Drive - Local & Styler Ant Design
│   └── agents/                         # Đặc tả chi tiết các Subagents
│       ├── req-risk-analyst.md         # Subagent Phase 1 (Phân tích & Bug retrieval)
│       └── test-automation-architect.md# Subagent Phase 2 (Thiết kế Automation Test)
├── data/                               # Local-First Cache & Persistent Storage
│   ├── bug_repository.json             # Kho bug lịch sử chuẩn hóa (đồng bộ 2 chiều với Drive)
│   ├── requirements_analysis.json      # Kết quả phân tích Phase 1 đã duyệt
│   ├── test_cases_specification.json   # Bộ kịch bản kiểm thử giả lập Phase 2
│   ├── user_preferences.json           # Cấu hình góc nhìn (business/technical/hybrid)
│   └── .sync_metadata.json             # Hash & Drive modifiedTime chống cache stale
├── docs/                               # Tài liệu thuyết trình & Minh chứng thực nghiệm
│   ├── Demo.webm                       # Video Demo vận hành thực tế hệ thống (~30MB)
│   ├── watch_demo.html                 # Trình phát Video HTML5 tương tác với bộ điều khiển tốc độ
│   ├── QA_Requirement_Assistant_Presentation.pptx # Slide thuyết trình dự phòng 7 trang
│   └── presentation_evidence_guide.md  # Cẩm nang thuyết trình 5-7 phút & Kịch bản trả lời 7 câu hỏi
├── Demo.webm                           # Symlink video demo tại thư mục gốc (tiện truy cập nhanh)
├── AGENTS.md                           # Master Rule điều phối runtime Antigravity
└── README.md                           # Tài liệu kiến trúc, báo cáo thực nghiệm & phỏng vấn
```

---

## 2. Cách Áp Dụng Trực Tiếp Trong Antigravity (How to Apply)

### 2.1. Tự động nhận diện (Zero Configuration)
Antigravity tự động quét và nạp plugin từ thư mục `.agents/` khi bạn mở workspace `/home/linh/QA`.  
Đồng thời, Skill cũng đã được đăng ký toàn cục tại `~/.gemini/config/skills/qa-requirement-assistant/SKILL.md`.

### 2.2. Các Subagents Runtime Được Antigravity Điều Phối
Hệ thống sử dụng 2 Subagents chuyên trách:
1. **`req-risk-analyst`**: Subagent chịu trách nhiệm phân tích tĩnh (Static Analysis) ở Phase 1: Bóc tách Business Rules, đặt câu hỏi phản biện BA kèm các gợi ý trả lời (Option A, B & Khuyến nghị), phát hiện 5 rủi ro kỹ thuật sâu, và đối chiếu tương quan với [Kho Bug Lịch Sử](file:///home/linh/QA/data/bug_repository.json).
2. **`test-automation-architect`**: Subagent chịu trách nhiệm thiết kế kiểm thử động (Dynamic Test Design) ở Phase 2: Kế thừa toàn bộ data Phase 1 (Business Rules, BA chốt, 5 rủi ro, bug lịch sử) để sinh bộ kịch bản kiểm thử giả lập toàn diện không giới hạn ở 5 test cases kèm xếp hạng ưu tiên (P1, P2, P3).

### 2.3. Trải nghiệm phiên làm việc (Human-in-the-loop Flow)
1. **Bước 1:** Tester gửi requirement bất kỳ vào ô chat Antigravity.
2. **Bước 2 (Phase 1 & Cổng Tương Tác Gate 1):** Antigravity kích hoạt `req-risk-analyst` phân tích 4 nhóm thông tin, đồng thời **tự động mở Modal tương tác (`ask_question`)** hiển thị danh sách câu hỏi BA kèm các options gợi ý (được gán nhãn `(Recommended)` cho giải pháp tối ưu) để Tester/BA **click chọn ngay bằng một cú nhấp chuột**, thay vì phải gõ câu trả lời thủ công.
3. **Bước 3 (Ghi nhận Lựa chọn BA Decisions Log):** Hệ thống ghi nhận chính xác các phương án mà người dùng đã chọn từ modal (hoặc ý kiến bổ sung qua chat) thành `BA Decisions Log` để làm căn cứ đầu vào bắt buộc cho Phase 2.
4. **Bước 4 (Phase 2):** Khi Tester gõ *"Đồng ý, sinh test đi"*, Antigravity chuyển giao context đã được duyệt sang `test-automation-architect` để sinh bộ kịch bản test giả lập chi tiết (bao phủ toàn bộ Business Rules, quyết định BA và rủi ro kỹ thuật, không giới hạn ở 5 test cases).
5. **Bước 5 (Gate 2 & Sync):** Khi Tester gõ *"Đẩy lên Drive"*, Antigravity sinh mã `requirement_id` duy nhất và thực hiện đồng bộ tích lũy thêm mới (**Accumulative Append-Only Update**, không reset/clear bảng cũ):
   * Lưu trữ tích lũy vào `data/requirements_analysis.json` & `data/test_cases_specification.json`.
   * Ghi nối tiếp các dòng mới (append rows) vào cuối bảng tính Google Sheets `Requirements_Analysis` và `Test_Cases_Specification`.

---

## 3. Báo Cáo Thực Nghiệm Trên 3 Requirement Mẫu (Mục 5 Đề Bài)

Hệ thống đã trải qua quá trình chạy thực nghiệm và lặp cải tiến liên tục trên cả 3 requirement mẫu theo quy chuẩn nghiêm ngặt: **Phân tích Tĩnh & Rủi ro (Phase 1) $\rightarrow$ Cổng Kiểm duyệt 1 (Human Gate 1) $\rightarrow$ Thiết kế Kịch bản Automation Test (Phase 2) $\rightarrow$ Cổng Kiểm duyệt 2 (Human Gate 2) $\rightarrow$ Lưu Trữ Cục Bộ (Local-First) & Đồng Bộ Google Workspace (Phase 3)**.

Dưới đây là báo cáo đánh giá thực nghiệm chi tiết cho từng requirement, ghi nhận trung thực những điểm làm tốt, những điểm còn thiếu sót ban đầu, và các cải tiến cụ thể về prompt, logic, mã nguồn đã được thực hiện:

---

### 3.1. Requirement A: *"Tài khoản bị khóa sau 5 lần nhập sai mật khẩu liên tiếp."*
*(Lĩnh vực: Quản lý Phiên, Bảo mật Xác thực & Máy trạng thái Tài khoản — Auth & Account Security)*

* **Mã định danh (Requirement ID):** `REQ_AUTH_LOCK_001`
* **Bộ kịch bản kiểm thử đã sinh:** 5 Test Cases (`TC_AUTH_LOCK_001` đến `TC_AUTH_LOCK_005`), bao gồm Happy Path, Biên 4 lần sai/lần 5 đúng, Negative, Concurrency đa luồng, và Thu hồi phiên đăng nhập tức thì (Force Logout / Token Revocation).

#### 1. Tool làm tốt điều gì?
* **Bóc tách nghiệp vụ & Máy trạng thái (State Machine) chuẩn xác:** Nhận diện đúng ngưỡng chuyển trạng thái tài khoản từ `ACTIVE` sang `LOCKED` khi bộ đếm `failed_attempts` đạt 5 lần liên tiếp. Làm rõ quy tắc tất định: nếu người dùng nhập đúng mật khẩu ở bất kỳ lần nào từ 1 đến 4, bộ đếm sai phải tự động reset về 0.
* **Đặt câu hỏi phản biện BA sắc bén, chạm đúng các góc khuất thực tế:**
  * *Thời hạn khóa:* Khóa tạm thời (tự mở sau 15–30 phút) hay khóa vĩnh viễn (chờ can thiệp từ Admin/CSKH)?
  * *Cửa sổ thời gian (Sliding Window / TTL):* 5 lần sai có bị giới hạn trong khung giờ (ví dụ 10 phút) hay tích lũy vô hạn qua nhiều ngày?
  * *Đăng nhập song song đa thiết bị:* Bộ đếm tính gộp theo User ID trên toàn hệ thống hay tính độc lập theo từng thiết bị (Device/IP)?
  * *Thu hồi phiên (Session Revocation):* Khi tài khoản bị khóa, các Access/Refresh Token đang hoạt động ở các thiết bị khác có bị thu hồi lập tức (Force Logout) hay vẫn cho phép thao tác?
* **Dự báo rủi ro kỹ thuật sâu & liên kết Bug lịch sử:** Dự báo chính xác nguy cơ kẻ xấu dùng script tự động bắn nhiều request sai song song trong vài mili-giây để brute-force mật khẩu (nếu thiếu Atomic Counter / Distributed Lock dẫn đến Lost Update). Đối chiếu trực tiếp với `BUG-001`, `BUG-003`, `BUG-008` trong kho bug lịch sử.

#### 2. Tool bỏ sót điều gì (Hạn chế ban đầu)?
* **Lạm dụng thuật ngữ kỹ thuật nặng (Technical Jargon Overload):** Ở phiên bản đầu tiên, Agent mặc định trả lời bằng các thuật ngữ hàn lâm (`Lost Update`, `Redis INCR`, `Race Condition`, `Distributed Lock`) khiến Tester và BA cảm thấy xa lạ, thiếu tính trực quan của nghiệp vụ thông thường.
* **Bố cục phản hồi ban đầu quá dài dòng (Text Wall):** Các đoạn văn phân tích nối dài liên tục, thiếu phân chia thị giác khiến người đọc khó nắm bắt nhanh trọng tâm.
* **Kịch bản test ban đầu bỏ sót tầng Service vệ tinh:** Kịch bản chỉ tập trung vào việc Auth Service trả về mã lỗi mà quên kiểm chứng xem các dịch vụ vệ tinh (như Giỏ hàng, Đặt hàng, Cập nhật hồ sơ) có còn chấp nhận Token của tài khoản bị khóa hay không.

#### 3. Bạn đã thay đổi prompt, code hoặc logic gì sau khi phát hiện vấn đề?
* **Thêm tính năng "Perspective Preference & Persistence" (Lựa chọn & Ghi nhớ Góc nhìn):**
  * Tạo tệp cấu hình `data/user_preferences.json` hỗ trợ 3 chế độ: `business` (Nghiệp vụ & BA), `technical` (Kỹ thuật & SDET), `hybrid` (Kết hợp).
  * Cập nhật System Prompt của `req-risk-analyst` để chuyển hóa các rủi ro kỹ thuật thành câu chuyện đời sống dễ hiểu (ví dụ: thay vì nói *"Lost Update trên bộ đếm"*, giải thích là *"Kẻ gian spam nhiều mật khẩu cùng lúc từ nhiều máy khiến hệ thống đếm sót và không khóa tài khoản kịp thời"*).
* **Tái cấu trúc bố cục sang Dạng Thẻ & Bảng Ma trận (Card & Table-Driven):**
  * Sửa prompt yêu cầu trình bày 4 phần: Thẻ tóm tắt yêu cầu, Bảng ma trận 4 thành tố Business Rules, Bảng câu hỏi cho BA kèm mức độ ảnh hưởng, và Bảng đánh giá rủi ro.
* **Bổ sung kịch bản kiểm thử Thu hồi phiên tức thì (`TC_AUTH_LOCK_005`):**
  * Yêu cầu kiểm tra sự kiện `UserAccountLockedEvent` được phát ra để đưa User ID vào Redis Token Blacklist, đảm bảo mọi request tiếp theo từ phiên cũ đều bị từ chối với mã HTTP `401 Unauthorized`.

---

### 3.2. Requirement B: *"Người dùng không được đặt mua số lượng sản phẩm lớn hơn số lượng tồn kho."*
*(Lĩnh vực: Quản lý Kho, Đặt hàng & Chống Bán Âm Kho — Inventory & Flash Sale Overselling)*

* **Mã định danh (Requirement ID):** `REQ_20261016_001` (hoặc `REQ_INV_OVERSELL_001`)
* **Bộ kịch bản kiểm thử đã sinh:** 5 Test Cases (`TC_INV_001` đến `TC_INV_005`), bao gồm kịch bản 2 người cùng tranh mua 1 sản phẩm cuối cùng ($N=1$) trong $\le 50\text{ms}$.

#### 1. Tool làm tốt điều gì?
* **Phân biệt chuẩn xác giữa Tồn kho vật lý (Physical Stock) và Tồn kho khả dụng (Available Stock):** Nhận diện điểm mấu chốt của bài toán E-Commerce: số lượng có thể đặt mua phải trừ đi số lượng đang được tạm giữ (Holding Window) bởi các đơn hàng đang chờ thanh toán.
* **Chất vấn sâu về quy trình vận hành và kịch bản biên:**
  * *Cơ chế giữ chỗ tồn kho (Hold/Reserve):* Tồn kho được giữ chỗ trong bao lâu khi khách chuyển sang cổng thanh toán bên thứ ba (VNPAY/Momo/Thẻ)? Nếu khách tắt trình duyệt thì sau bao lâu kho tự nhả?
  * *Đơn hàng đa sản phẩm (Multi-item Order):* Nếu khách mua 3 món A, B, C nhưng món B vừa hết hàng lúc bấm thanh toán thì hệ thống từ chối toàn bộ đơn hay cho phép tiếp tục mua món A và C?
  * *Xử lý đồng thời (Concurrency):* Khi tồn kho chỉ còn 1 mà có 2 khách hàng cùng bấm đặt hàng tại cùng một phần nghìn giây.
* **Liên kết chính xác với Bug lịch sử nghiêm trọng:** Ánh xạ thẳng vào `BUG-005` (Lỗi timeout giữa Order Service và Inventory Service dẫn đến đơn tạo thành công nhưng kho không trừ, gây bán âm kho - Overselling) và `BUG-007` (Tồn kho giữ chỗ không tự động giải phóng sau timeout).

#### 2. Tool bỏ sót điều gì (Hạn chế ban đầu)?
* **Gộp cụm hành động độc lập vào cùng 1 bước kiểm thử (Action Bundling):** Ban đầu, bước 1 của kịch bản test được Agent sinh ra như sau: *"Khách hàng chọn số lượng = 3, chọn thanh toán COD, bấm nút 'Đặt hàng ngay' (POST /api/v1/checkout/orders)"*. Tester đã chỉ rõ đây là lỗi thiết kế test case nghiêm trọng: dồn bước chuẩn bị dữ liệu (nhập số lượng) với bước kích hoạt (submit), khiến việc debug automation khi chạy Playwright/Selenium không thể xác định lỗi xảy ra do giao diện không nhận số hay do API thất bại.
* **Kỳ vọng API và Database quá sơ sài:** Kết quả mong đợi ban đầu chỉ ghi chung chung `HTTP 200` hoặc `HTTP 400`, không chỉ rõ các trường dữ liệu cần đối chiếu trong JSON Response Body (`order_id`, `available_stock`) và không nêu cụ thể bảng/cột Database (`inventory.available_quantity`, `inventory.reserved_quantity`).
* **Giao diện Google Drive ban đầu rất xấu và khó đọc:** Độ rộng cột bị co rúm, chữ tràn viền, thiếu cột trạng thái kiểm thử (Pass/Fail) và thiếu dòng tiêu đề cố định.

#### 3. Bạn đã thay đổi prompt, code hoặc logic gì sau khi phát hiện vấn đề?
* **Thiết lập "3 Nguyên Tắc Vàng Chuẩn QA/QC Thực Chiến" trong `AGENTS.md` và Prompt:**
  1. *Step Disaggregation (Tách bước độc lập):* Bắt buộc tách bước nhập số lượng/chuẩn bị dữ liệu và bước bấm nút gửi request thành các bước riêng biệt có số thứ tự.
  2. *Synchronized Deep Verification (Kiểm chứng sâu 3 tầng):* Kết quả mong đợi phải mô tả chi tiết: UI (thông báo lỗi, màu viền cảnh báo), API (HTTP Status Code + JSON Body chi tiết mã lỗi `OUT_OF_STOCK`), Database & Event (truy vấn bảng `inventory`, cột `quantity`, và Kafka Event `StockDeductionFailedEvent`).
  3. *Cột Trạng thái (`Status`):* Bắt buộc bổ sung cột `Status (Pass/Fail)` với giá trị mặc định là `NOT_RUN`.
* **Phát triển Script định dạng bảng tính Google Sheets chuyên nghiệp (`google_sheets_sync_manager.py`):**
  * Tự động áp dụng bộ màu Ant Design Blue (`#1677FF`), chữ trắng in đậm, cố định dòng 1 (`frozenRowCount = 1`).
  * Thiết lập độ rộng cột thoáng mắt (120px–500px), tự động xuống dòng (`WRAP`), căn lề trên (`TOP`).
  * Tích hợp Menu Dropdown chọn nhanh trạng thái (`NOT_RUN`, `PASS`, `FAIL`, `BLOCKED`) kèm luật đổi màu tự động (Conditional Formatting).

---

### 3.3. Requirement C: *"Mỗi voucher chỉ được sử dụng một lần trên mỗi tài khoản."*
*(Lĩnh vực: Khuyến mãi, Vòng đời Voucher & Phòng chống Gian lận — Promotion Abuse Prevention)*

* **Mã định danh (Requirement ID):** `REQ_20261016_001` (hoặc `REQ_VOUCHER_ONETIME_001`)
* **Bộ kịch bản kiểm thử đã sinh:** 5 Test Cases (`TC_VOUCHER_001` đến `TC_VOUCHER_005`), bao gồm kiểm thử race condition 2 tab đồng thời và bù trừ trạng thái voucher khi hủy đơn/timeout.

#### 1. Tool làm tốt điều gì?
* **Mô hình hóa toàn diện Vòng đời Voucher (Voucher Lifecycle):** Bóc tách chính xác 3 trạng thái của mã ưu đãi: `Available` (khả dụng) $\rightarrow$ `Reserved` (tạm giữ khi khách đang thanh toán) $\rightarrow$ `Committed/Used` (đã sử dụng khi đơn thành công). Đặc biệt xác định rõ luồng đảo ngược (Compensating Transaction): khi đơn bị hủy hoặc hết hạn thanh toán, voucher phải tự động được hoàn trả về trạng thái `Available` cho tài khoản.
* **Bộ câu hỏi BA toàn diện về phòng chống gian lận (Promotion Abuse):**
  * *Thời điểm chốt sử dụng:* Voucher được coi là "Đã sử dụng" khi bấm Đặt hàng, khi thanh toán online thành công, hay khi giao hàng thành công (đơn COD)?
  * *Hủy đơn / Đổi trả 1 phần:* Khi khách hoàn trả 1 món trong đơn nhiều món, giá trị voucher được phân bổ và hoàn lại tiền như thế nào? Có cấp lại voucher không?
  * *Chống lạm dụng đa tài khoản (Sybil Attack):* Có kiểm soát trùng Số điện thoại nhận hàng, cùng Thẻ ngân hàng hoặc cùng Mã định danh thiết bị (Device ID) để tránh tạo nhiều tài khoản ảo gom mã không?
* **Tương quan trực tiếp 100% với Bug lịch sử `BUG-003`:** Nhận diện ngay lỗ hổng kinh điển: Người dùng mở cùng lúc 2 tab trên trình duyệt hoặc 2 thiết bị điện thoại, cùng áp voucher 1 lần và bấm "Đặt hàng" đồng thời trong khoảng $\le 50\text{ms}$.
* **Kịch bản kiểm thử tự động giả lập chuẩn mực:**
  * `TC_VOUCHER_001` (Happy Path): Áp voucher thành công đơn đầu, xác thực bảng `user_voucher_usages` ghi nhận trạng thái `COMMITTED`.
  * `TC_VOUCHER_002` (Boundary Value): Giá trị giỏ hàng sát biên tối thiểu (199.999đ bị từ chối vs 200.000đ được áp dụng) và mốc thời gian sát giờ hết hạn (T-1s).
  * `TC_VOUCHER_003` (Negative Path): Cố tình áp dụng lại mã ở đơn thứ hai qua UI và qua API trực tiếp.
  * `TC_VOUCHER_004` (Concurrency): Mô phỏng 2 tab gửi request đồng thời trong $\le 50\text{ms}$, kiểm chứng cơ chế Distributed Lock (Redis Redlock) & ràng buộc cơ sở dữ liệu `UNIQUE(user_id, voucher_code)`.
  * `TC_VOUCHER_005` (State Conflict & Recovery): Khách hủy thanh toán online sau 15 phút, kiểm tra voucher tự động giải phóng và áp dụng thành công cho đơn mới.

#### 2. Tool bỏ sót điều gì (Hạn chế ban đầu)?
* **Bỏ sót nghiệp vụ Cấn trừ hoàn tiền một phần (Partial Refund Deduction):** Khi khách hàng mua 3 món trị giá 500k có áp voucher giảm 50k (còn 450k), sau đó khách yêu cầu trả lại 1 món trị giá 150k. Tool ban đầu chưa đặt câu hỏi về công thức cấn trừ chiết khấu cho món hàng trả lại.
* **Nguy cơ kẹt trạng thái tạm giữ vĩnh viễn (Stuck Holding Window):** Nếu khách hàng chuyển sang cổng thanh toán ngân hàng rồi tắt trình duyệt mà không thanh toán, nếu cronjob quét timeout bị chết, voucher của khách sẽ bị giam vĩnh viễn ở trạng thái `RESERVED` mà khách không dùng lại được.
* **Đồng bộ trạng thái tức thời giữa các tab trình duyệt (Realtime Tab Sync):** Kịch bản ban đầu chưa mô tả rõ việc nếu Tab 1 đã đặt hàng thành công, Tab 2 đang mở sẵn có tự động cập nhật vô hiệu hóa voucher thông qua `BroadcastChannel` hoặc `WebSocket` hay không.

#### 3. Bạn đã thay đổi prompt, code hoặc logic gì sau khi phát hiện vấn đề?
* **Mở rộng Cẩm nang Rủi ro (`risk-checklist.md`):** Thêm nhóm rủi ro *Lifecycle Reversal & Stuck State* và *Multi-item Partial Compensation* vào tài liệu tham chiếu của Subagent 1.
* **Bổ sung câu hỏi BA về chính sách cấn trừ hoàn trả (Q5, Q6):** Bắt buộc đưa vào báo cáo Phase 1 để BA và Tech Lead thống nhất công thức tính tiền hoàn trả.
* **Tích hợp Kịch bản Kiểm chứng Giao dịch Bù trừ (`TC_VOUCHER_005`):** Bổ sung bước kiểm tra bảng `user_voucher_usages` chuyển từ `RESERVED` sang `RELEASED`, kiểm tra Kafka phát `OrderCancelledEvent` kích hoạt hoàn lại voucher về ví người dùng.

---

### 3.4. Bảng Tổng Hợp So Sánh Kết Quả Thực Nghiệm 3 Requirement

| Tiêu chí | Requirement A (Khóa tài khoản 5 lần sai) | Requirement B (Chặn mua vượt tồn kho) | Requirement C (Voucher 1 lần / tài khoản) |
| :--- | :--- | :--- | :--- |
| **Phân loại Nghiệp vụ** | Authentication & Security | Inventory & Flash Sale | Promotion & Anti-Fraud |
| **Điểm làm tốt nổi bật** | Phát hiện kẽ hở thu hồi phiên (Force Logout) & Sliding Window đếm lỗi | Phân biệt Tồn kho vật lý vs Tồn kho khả dụng; giữ chỗ tồn kho | Bóc tách trọn vẹn Vòng đời Voucher & Giao dịch bù trừ (Compensating) |
| **Lỗi/Thiếu sót ban đầu** | Thuật ngữ kỹ thuật quá nặng; bố cục text wall khó nhìn | Gộp chung bước hành động; kết quả API/DB chung chung; bảng tính xấu | Bỏ sót nghiệp vụ hoàn tiền 1 phần & kẹt voucher khi timeout cron chết |
| **Cải tiến Prompt / Logic** | Thêm cơ chế ghi nhớ Góc nhìn (`user_preferences.json`); định dạng Thẻ & Bảng | Bổ sung 3 Nguyên Tắc Vàng (Tách bước, Verify 3 tầng sâu UI/API/DB, cột Status) | Mở rộng Checklist rủi ro vòng đời; bổ sung kịch bản khôi phục trạng thái |
| **Cải tiến Code / Script** | Cấu hình tham số Prompt chuyển hóa rủi ro thành ngôn ngữ đời sống | Viết script Styler chuẩn Ant Design Blue, Dropdown Validation cho Google Sheets | Tối ưu hóa cơ chế Local-First & Bidirectional Drive Sync với Traceability Key |
| **Tương quan Bug Lịch sử** | `BUG-001`, `BUG-003`, `BUG-008` (Race Condition & Lost Update) | `BUG-005`, `BUG-007` (Timeout kho, giữ chỗ không nhả) | `BUG-003`, `BUG-008`, `BUG-001` (Race condition 2 tab, đa thiết bị) |
| **Số Test Case sinh ra** | 5 Test Cases (`TC_AUTH_LOCK_001` – `005`) | 5 Test Cases (`TC_INV_001` – `005`) | 5 Test Cases (`TC_VOUCHER_001` – `005`) |
| **Độ ưu tiên cao nhất** | P1 (Critical) — Ngăn Brute-Force & Rò rỉ phiên | P1 (Critical) — Ngăn Bán âm kho (Overselling) | P1 (Critical) — Ngăn Lạm dụng voucher trùng lặp |

---

## 4. Tính Năng Tự Chọn Bổ Sung (Mục 6 Đề Bài)

### Tên tính năng:
> **"Ma Trận Truy Vết Kịch Bản Test Giả Lập & Đồng Bộ Trực Tiếp Qua Google Workspace MCP"**

### Vì sao chọn tính năng này?
1. **Giải quyết bài toán thực tế của QA:** Trong các dự án Agile, tester không chỉ dừng lại ở việc đọc requirement mà cần có tài liệu kịch bản cụ thể để chuyển giao cho đội Automation hoặc import vào hệ sinh thái quản lý test (Xray/Jira).
2. **Khắc phục việc thiếu Figma / Thiết kế chi tiết:** Vì chưa có UI selector thực tế, hệ thống tự động sinh các **Bước hành động giả lập (Simulated Steps)** và **Kết quả kỳ vọng (Expected Results 3 tầng: UI, API, Database)** kèm xếp hạng ưu tiên (P1, P2, P3).
3. **Traceability xuyên suốt không cần DB trung gian:** Khóa `requirement_id` liên kết chặt chẽ giữa bảng Phân tích và bảng Kịch bản test trên Google Drive, cập nhật thời gian thực qua giao thức MCP chuẩn Enterprise.

---

## 5. Trả Lời 7 Câu Hỏi Phỏng Vấn (Mục 7.3 Đề Bài)

### Câu 1: Bạn hiểu vấn đề cần giải quyết là gì?
* **Trả lời:** Vấn đề cốt lõi không phải là "gọi LLM để tóm tắt văn bản", mà là **thu hẹp khoảng cách nhận thức giữa BA, Dev và QA**. QA thường gặp rủi ro bỏ sót các trường hợp biên (Boundary), các nguy cơ chạy đua dữ liệu (Race condition, State drift), và quên đi các bài học đắt giá từ bug lịch sử. Công cụ này đóng vai trò như một Senior QA Agent: chủ động chất vấn kẽ hở logic, dự báo rủi ro kỹ thuật sâu, và chuẩn hóa thành các kịch bản kiểm thử tự động có thể thực thi ngay.

### Câu 2: Kiến trúc của tool gồm những phần nào?
* **Trả lời:** Kiến trúc gồm 3 tầng:
  1. *Lớp Tương Tác & Điều Phối:* Antigravity Orchestrator quản lý 2-Phase State Machine và 2 Cổng kiểm soát của con người (`rules/AGENTS.md`).
  2. *Subagents:* Subagent 1 (`req-risk-analyst`) kết hợp Bug Catalog; Subagent 2 (`test-automation-architect`) tuân thủ Test Design Matrix.
  3. *Lớp Dữ Liệu & MCP:* Kết nối với Google Workspace MCP Server để đọc tri thức từ `Bug_Repository` và lưu trữ lịch sử phân tích, kịch bản test trên Google Drive.

### Câu 3: Bạn sử dụng AI cho những công việc nào?
* **Trả lời:** AI được ứng dụng vào 4 tác vụ đòi hỏi khả năng suy luận ngữ nghĩa cao:
  1. Bóc tách và chuẩn hóa các Business Rules từ văn bản tự nhiên.
  2. Đặt các câu hỏi chất vấn mang tính phản biện dựa trên tri thức kiểm thử phần mềm.
  3. Suy luận rủi ro kỹ thuật (Concurrency, Idempotency, Eventual Consistency).
  4. Thiết kế các bước giả lập và kỳ vọng cho kịch bản Automation Test theo từng cấp độ ưu tiên.

### Câu 4: Có phần nào bạn chủ động KHÔNG giao cho AI không? Tại sao?
* **Trả lời:** Có những phần cốt lõi tôi chủ động nắm quyền kiểm soát và không giao phó cho AI:
  1. *Cách phân chia và sắp xếp kiến trúc Agent (Agent Topology & Arrangement):* AI không thể tự quyết định cách bố trí bao nhiêu tác tử, trách nhiệm từng tác tử ra sao và luồng phối hợp thế nào là hợp lý cho một quy trình kiểm thử thực tế. Tôi trực tiếp thiết kế cấu trúc phân cấp: tách bạch Subagent 1 (`req-risk-analyst` chuyên phân tích tĩnh & bóc tách rủi ro) và Subagent 2 (`test-automation-architect` chuyên thiết kế kịch bản kiểm thử), ngăn chặn hoàn toàn việc AI tự biên tự diễn sinh test case khi chưa chốt yêu cầu.
  2. *Nguồn tri thức chuẩn hóa (Authoritative Sources & Documentation URLs):* AI có xu hướng suy diễn hoặc dẫn các đường link không chuẩn xác nếu để tự do. Tôi chủ động quy định rõ tài liệu tham chiếu nào được phép nạp, cơ sở tri thức kỹ thuật lấy từ đâu (`references/`, kho bug chuẩn hóa `data/bug_repository.json`, và Google Workspace qua MCP) để đảm bảo dữ liệu đầu vào luôn có căn cứ xác thực.
  3. *Quy tắc điều phối cứng (State Machine & Gate Control):* Việc chặn cổng duyệt (Human Gate 1, Human Gate 2) và quy tắc Rollback khi đổi requirement được quản lý bằng luật tất định trong `AGENTS.md`, không cho phép AI tự ý bypass.

### Câu 5: Trong quá trình làm bài, có điều gì bạn chưa biết trước đó? Bạn đã tìm hiểu như thế nào?
* **Trả lời:** Trước khi thực hiện bài toán này, tôi chưa hiểu rõ **cách cấu trúc, thiết lập Agent chuyên sâu trên nền tảng này**. Tôi đã tìm hiểu bằng cách:
  * Nghiên cứu kỹ tài liệu hướng dẫn kiến trúc của Antigravity.
  * Học cách thiết lập một Native Customization Plugin: cơ chế phân tách tầng giữa **Rules** (`AGENTS.md` điều phối runtime), **Subagents** (`.agents/agents/*.md`), và **Skills** (`SKILL.md`).
  * Thực hiện nguyên lý **Progressive Disclosure** để tối ưu hóa context: chia nhỏ cẩm nang kỹ thuật vào thư mục `references/` (`risk-checklist.md`, `test-design-matrix.md`) thay vì nhồi nhét vào một prompt duy nhất.
### Câu 6: Có trường hợp nào AI trả lời sai hoặc chưa tốt không? Bạn phát hiện và cải thiện như thế nào?
* **Trả lời:** Có rất nhiều điểm AI xử lý chưa tốt ban đầu và tôi đã phát hiện, liên tục nắn chỉnh, cải thiện qua từng lượt trao đổi trong chat:
  1. *Về Format và cách trình bày phản hồi (Formatting & Layout):*
     * *Vấn đề:* Ban đầu AI trả lời dồn dập theo dạng khối văn bản dài ("Text Wall"), dùng quá nhiều thuật ngữ kỹ thuật hàn lâm khiến Tester và BA cảm thấy nặng nề; trên Google Sheets thì dữ liệu bị co rúm, thiếu chuyên nghiệp.
     * *Cải tiến qua chat:* Tôi yêu cầu tái cấu trúc thành **Thẻ tóm tắt & Bảng ma trận (Card & Table-Driven)**; bổ sung tệp cấu hình `user_preferences.json` để ghi nhớ góc nhìn (`business` vs `technical`); viết script `google_sheets_sync_manager.py` định dạng chuẩn Ant Design Blue và bổ sung cột `Status (Pass/Fail)` kèm Dropdown.
  2. *Về cách tổ chức và đưa ra Skill (Skill Architecture & Token Optimization):*
     * *Vấn đề:* Ban đầu có xu hướng nhét toàn bộ hướng dẫn, checklist rủi ro và ma trận test vào chung một file `SKILL.md`, dẫn đến hao tốn token cực lớn và context bị loãng.
     * *Cải tiến qua chat:* Qua phân tích lợi/hại, tôi đã bóc tách kiến thức chuyên sâu vào thư mục `references/`, áp dụng Progressive Disclosure để Agent chỉ tra cứu khi cần.
  3. *Về quy chuẩn thiết kế kịch bản test (Test Design Precision):*
     * *Vấn đề:* AI thường dồn nhiều thao tác vào 1 bước (chọn số lượng + chọn thanh toán + bấm mua) và kết quả API/DB chỉ ghi HTTP status code chung chung.
     * *Cải tiến qua chat:* Tôi đưa **3 Nguyên Tắc Vàng** vào `AGENTS.md` (Tách bước độc lập, Kiểm chứng sâu 3 tầng UI/API/DB/Event, Cột trạng thái kiểm thử).

### Câu 7: Nếu đưa tool cho 10 tester sử dụng hằng ngày, bạn sẽ cải tiến điều gì đầu tiên?
* **Trả lời:** Tôi sẽ ưu tiên 3 cải tiến sau:
  1. *Jira / Confluence Webhook Integration:* Tích hợp Jira MCP để Tester chỉ cần dán link Jira Ticket, tool tự đọc Story Description, phân tích và comment trực tiếp danh sách câu hỏi cho BA ngay trên Jira.
  2. *Feedback Loop (Upvote/Downvote):* Cho phép Tester đánh giá câu hỏi hoặc test case nào hữu ích, làm dữ liệu Few-shot tự động để Agent ngày càng thông minh hơn theo đặc thù sản phẩm của Caro.
