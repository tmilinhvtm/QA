# REQUIREMENT QA ASSISTANT — ANTIGRAVITY NATIVE PLUGIN

> **Ứng viên:** Vũ Thị Mai Linh  
> **Dự án:** Trợ lý AI Phân tích Requirement & Tự động sinh Kịch bản Automation Test (Chuyên biệt cho QA)  
> **Nền tảng:** Antigravity Customization Plugin (Rules, Skills, Subagents & Google Workspace MCP)  
> **Google Spreadsheet Master (Trực tiếp trên Drive):** [Xem Master Sheet tại đây](https://docs.google.com/spreadsheets/d/1BG5HNlQBEqyG_hjM9WwklrME2lZbysNFHBSggsSQetk/edit)

---

## 1. Cấu Trúc Plugin Antigravity Chuẩn (Native Customization)

Dự án được đóng gói 100% theo chuẩn **Antigravity Customization System** (không sử dụng mã nguồn backend CRUD truyền thống), đặt tại thư mục `.agents/`:

```text
/home/linh/QA/
├── .agents/
│   ├── plugin.json                     # Antigravity Plugin Manifest
│   ├── rules/
│   │   └── AGENTS.md                   # Antigravity Rules (Luật điều phối 2-Phase & Human Gates)
│   └── skills/
│       └── qa-requirement-assistant/   # Master Skill Bundle
│           └── references/             # Progressive Disclosure (Cẩm nang kỹ thuật chuyên sâu)
│               ├── risk-checklist.md   # Khung 5 góc khuất kỹ thuật (Concurrency, State Drift...)
│               └── test-design-matrix.md # Ma trận 5 loại kịch bản & chuẩn bước giả lập
│           # (Bug lịch sử được truy vấn trực tiếp từ Google Drive qua MCP, không dùng file tĩnh)
│   └── subagents/                      # Đặc tả chi tiết các Subagents
│       ├── req-risk-analyst.md         # Subagent Phase 1 (Phân tích & Bug retrieval)
│       └── test-automation-architect.md# Subagent Phase 2 (Thiết kế Automation Test)
└── README.md                           # Tài liệu kiến trúc, báo cáo thực nghiệm & phỏng vấn
```

---

## 2. Cách Áp Dụng Trực Tiếp Trong Antigravity (How to Apply)

### 2.1. Tự động nhận diện (Zero Configuration)
Antigravity tự động quét và nạp plugin từ thư mục `.agents/` khi bạn mở workspace `/home/linh/QA`.  
Đồng thời, Skill cũng đã được đăng ký toàn cục tại `~/.gemini/config/skills/qa-requirement-assistant/SKILL.md`.

### 2.2. Các Subagents Runtime Được Antigravity Điều Phối
Hệ thống sử dụng 2 Subagents chuyên trách:
1. **`req-risk-analyst`**: Subagent chịu trách nhiệm phân tích tĩnh (Static Analysis) ở Phase 1: Bóc tách Business Rules, đặt câu hỏi phản biện BA, phát hiện 5 rủi ro kỹ thuật sâu, và đối chiếu tương quan với [Bug Catalog](file:///home/linh/QA/.agents/skills/qa-requirement-assistant/references/bug-catalog.md).
2. **`test-automation-architect`**: Subagent chịu trách nhiệm thiết kế kiểm thử động (Dynamic Test Design) ở Phase 2: Sinh đúng 5 kịch bản kiểm thử giả lập (Happy, Boundary, Negative, Concurrency, State Conflict) kèm xếp hạng ưu tiên (P1, P2, P3).

### 2.3. Trải nghiệm phiên làm việc (Human-in-the-loop Flow)
1. **Bước 1:** Tester gửi requirement bất kỳ vào ô chat Antigravity.
2. **Bước 2 (Phase 1):** Antigravity kích hoạt `req-risk-analyst` để phân tích 4 nhóm thông tin bắt buộc và **dừng lại tại Cổng kiểm duyệt 1 (Human Gate 1)**.
3. **Bước 3 (Thảo luận & Tinh chỉnh):** Tester phản biện hoặc bổ sung nghiệp vụ. Agent cập nhật lại context.
4. **Bước 4 (Phase 2):** Khi Tester gõ *"Đồng ý, sinh test đi"*, Antigravity chuyển giao context đã được duyệt sang `test-automation-architect` để sinh 5 kịch bản test giả lập chi tiết.
5. **Bước 5 (Gate 2 & Sync):** Khi Tester gõ *"Đẩy lên Drive"*, Antigravity sinh mã `requirement_id` và gọi công cụ MCP `google-workspace` (`modify_sheet_values`) để ghi nhận đồng bộ thời gian thực vào [Google Master Sheet](https://docs.google.com/spreadsheets/d/1BG5HNlQBEqyG_hjM9WwklrME2lZbysNFHBSggsSQetk/edit).

---

## 3. Báo Cáo Thực Nghiệm Trên 3 Requirement Mẫu (Mục 5 Đề Bài)

Toàn bộ kết quả thực nghiệm và kịch bản test tương ứng đã được ghi nhận trực tiếp vào [Google Master Sheet](https://docs.google.com/spreadsheets/d/1BG5HNlQBEqyG_hjM9WwklrME2lZbysNFHBSggsSQetk/edit):

### 3.1. Requirement A: *"Tài khoản bị khóa sau 5 lần nhập sai mật khẩu liên tiếp."*
* **Tool làm tốt:**
  * Bóc tách chuẩn xác ngưỡng 5 lần và điều kiện "liên tiếp".
  * Thiết kế kịch bản Reset counter khi nhập đúng ở lần thứ 4 (`TC_AUTH_002`) và chặn đăng nhập tuyệt đối khi đã `LOCKED` (`TC_AUTH_003`).
  * Phát hiện rủi ro tấn công dò mật khẩu phân tán (*Distributed Brute Force*) qua nhiều worker đồng thời (`TC_AUTH_004`).
* **Tool bỏ sót ban đầu:**
  * Chưa làm rõ cơ chế mở khóa: Khóa vĩnh viễn (Admin can thiệp) hay Khóa tạm thời (Timeout-based lock sau X phút).
  * Chưa bao quát trường hợp tấn công đa luồng cùng lúc làm sai lệch bộ đếm do Race Condition (Dirty read).
* **Tinh chỉnh Prompt & Logic sau khi phát hiện:**
  * Bổ sung quy tắc trong `SKILL.md` và `risk-checklist.md`: *"Với các trạng thái đếm giới hạn (Counter limits), bắt buộc chất vấn cơ chế Reset, cơ chế Mở khóa (Unlock Lifecycle) và rủi ro Concurrency trên Counter"*.
  * Bổ sung kịch bản `TC_AUTH_005` kiểm thử tự động mở khóa sau khi hết thời hạn khóa.

### 3.2. Requirement B: *"Người dùng không được đặt mua số lượng sản phẩm lớn hơn số lượng tồn kho."*
* **Tool làm tốt:**
  * Xác định chính xác ràng buộc bất đẳng thức: `Order_Quantity <= Available_Stock`.
  * Bao phủ kiểm thử giá trị biên vét cạn kho hàng (`TC_STOCK_002` khi đặt mua chính xác bằng tồn kho).
  * Liên hệ trực tiếp và cảnh báo nguy cơ tái diễn **BUG-005** (*Order tạo thành công nhưng tồn kho không bị trừ*).
* **Tool bỏ sót ban đầu:**
  * Bỏ sót tình huống **Bán vượt tồn kho (Overselling / Race Condition)** khi 2 khách hàng cùng đặt mua sản phẩm cuối cùng tại cùng một giây.
  * Chưa hỏi BA về thời điểm trừ tồn kho (Giữ chỗ khi thêm vào giỏ hay chỉ trừ khi thanh toán).
* **Tinh chỉnh Prompt & Logic sau khi phát hiện:**
  * Bổ sung kịch bản `TC_STOCK_004`: Mô phỏng 2 request gửi đồng thời tại 12:00:00, yêu cầu Database Lock chỉ cho phép đúng 1 đơn thành công, chặn đứng bán âm kho.
  * Bổ sung câu hỏi chất vấn BA về cơ chế *Stock Hold Expiration* (thời gian giữ chỗ thanh toán).

### 3.3. Requirement C: *"Mỗi voucher chỉ được sử dụng một lần trên mỗi tài khoản."*
* **Tool làm tốt:**
  * Xác định phạm vi áp dụng duy nhất theo `Account_ID`.
  * Ánh xạ chính xác tới **BUG-003** (*Một user sử dụng cùng voucher cho hai đơn hàng do race-condition*).
  * Thiết kế kịch bản `TC_VOUCHER_003` mô phỏng 2 tab trình duyệt cùng checkout voucher đồng thời.
* **Tool bỏ sót ban đầu:**
  * Chưa tính đến vòng đời hoàn voucher: Nếu đơn hàng áp dụng voucher bị hủy hoặc thanh toán thất bại, voucher có được hoàn lại về trạng thái `ACTIVE` hay không.
  * Bỏ sót trường hợp kiểm thử biên đa tài khoản (User A dùng xong thì User B vẫn phải dùng được bình thường).
* **Tinh chỉnh Prompt & Logic sau khi phát hiện:**
  * Bổ sung kịch bản `TC_VOUCHER_004` (State Recovery khi đơn hàng bị hủy).
  * Bổ sung kịch bản `TC_VOUCHER_005` (Xác thực tính độc lập giữa các tài khoản).

---

## 4. Tính Năng Tự Chọn Bổ Sung (Mục 6 Đề Bài)

### Tên tính năng:
> **"Ma Trận Truy Vết Kịch Bản Automation Test Giả Lập & Đồng Bộ Trực Tiếp Qua Google Workspace MCP"**

### Vì sao chọn tính năng này?
1. **Giải quyết bài toán thực tế của QA:** Trong các dự án Agile, tester không chỉ dừng lại ở việc đọc requirement mà cần có tài liệu kịch bản cụ thể để chuyển giao cho đội Automation hoặc import vào hệ sinh thái quản lý test (Xray/Jira).
2. **Khắc phục việc thiếu Figma / Thiết kế chi tiết:** Vì chưa có UI selector thực tế, hệ thống tự động sinh các **Bước hành động giả lập (Simulated Steps)** và **Kết quả kỳ vọng (Expected Results 3 tầng: UI, API, Database)** kèm xếp hạng ưu tiên (P1, P2, P3).
3. **Traceability xuyên suốt không cần DB trung gian:** Khóa `requirement_id` liên kết chặt chẽ giữa bảng Phân tích và bảng Kịch bản test trên Google Drive, cập nhật thời gian thực qua giao thức MCP chuẩn Enterprise.

---

## 5. Trả Lời 7 Câu Hỏi Phỏng Vấn (Mục 7.3 Đề Bài)

### Câu 1: Bạn hiểu vấn đề cần giải quyết là gì?
* **Trả lời:** Vấn đề cốt lõi không phải là "gọi LLM để tóm tắt văn bản", mà là **thu hẹp khoảng cách nhận thức giữa BA, Dev và QA**. QA thường gặp rủi ro bỏ sót các trường hợp biên (Boundary), các nguy cơ chạy đua dữ liệu (Race condition, State drift), và quên đi các bài học đắt giá từ bug lịch sử. Công cụ này đóng vai trò như một Senior QA Co-pilot: chủ động chất vấn kẽ hở logic, dự báo rủi ro kỹ thuật sâu, và chuẩn hóa thành các kịch bản kiểm thử tự động có thể thực thi ngay.

### Câu 2: Kiến trúc của tool gồm những phần nào?
* **Trả lời:** Kiến trúc gồm 3 tầng:
  1. *Lớp Tương Tác & Điều Phối:* Antigravity Orchestrator quản lý 2-Phase State Machine và 2 Cổng kiểm soát của con người (`rules/AGENTS.md`).
  2. *Lớp Vệ Tinh Chuyên Trách (Subagents):* Subagent 1 (`req-risk-analyst`) kết hợp Bug Catalog; Subagent 2 (`test-automation-architect`) tuân thủ Test Design Matrix.
  3. *Lớp Dữ Liệu & MCP:* Kết nối với Google Workspace MCP Server để đọc tri thức từ `Bug_Repository` và lưu trữ lịch sử phân tích, kịch bản test trên Google Drive.

### Câu 3: Bạn sử dụng AI cho những công việc nào?
* **Trả lời:** AI được ứng dụng vào 4 tác vụ đòi hỏi khả năng suy luận ngữ nghĩa cao:
  1. Bóc tách và chuẩn hóa các Business Rules từ văn bản tự nhiên.
  2. Đặt các câu hỏi chất vấn mang tính phản biện dựa trên tri thức kiểm thử phần mềm.
  3. Suy luận rủi ro kỹ thuật (Concurrency, Idempotency, Eventual Consistency).
  4. Thiết kế các bước giả lập và kỳ vọng cho kịch bản Automation Test theo từng cấp độ ưu tiên.

### Câu 4: Có phần nào bạn chủ động KHÔNG giao cho AI không? Tại sao?
* **Trả lời:** Có 3 phần tôi chủ động kiểm soát bằng quy tắc tất định:
  1. *State Machine & Gate Control:* Việc chuyển pha (Phase 1 sang Phase 2) hoặc Rollback khi đổi requirement bắt buộc phải tuân thủ nghiêm ngặt theo luật trong `AGENTS.md`, không để AI tự ý suy đoán.
  2. *Cấu trúc dữ liệu & Format ô:* Quy chuẩn hiển thị trên Google Sheets được định dạng cố định để đảm bảo tính thẩm mỹ và dễ đọc.
  3. *Khóa liên kết Traceability:* Việc sinh mã `requirement_id` và gán Foreign Key vào các dòng test case được định danh chuẩn mực để đảm bảo tính nhất quán 100%.

### Câu 5: Trong quá trình làm bài, có điều gì bạn chưa biết trước đó? Bạn đã tìm hiểu như thế nào?
* **Trả lời:** Trước đây tôi chủ yếu làm việc với API RESTful truyền thống hoặc gọi OpenAI API trực tiếp. Khi giải quyết bài toán này, tôi đã tìm hiểu sâu về:
  * Mô hình điều phối tác tử **Human-in-the-loop State Machine** trong Antigravity để ngăn ngừa hiện tượng "Garbage In, Garbage Out".
  * Cơ chế kết nối công cụ qua **Model Context Protocol (MCP)** của Anthropic/Google để thao tác trực tiếp trên Cloud Storage (Google Drive / Sheets) thay vì phụ thuộc vào thư viện file local.

### Câu 6: Có trường hợp nào AI trả lời sai hoặc chưa tốt không? Bạn phát hiện và cải thiện như thế nào?
* **Trả lời:** Có. Ban đầu AI chỉ phân tích các luồng Happy Path và bỏ sót hoàn toàn rủi ro **Overselling (bán âm kho)** ở Requirement B và **Race Condition 2 tab** ở Requirement C.  
  * *Cách phát hiện:* Qua quá trình kiểm tra đối soát chéo với các bug lịch sử (BUG-003, BUG-005).
  * *Cách cải thiện:* Tôi đưa vào System Prompt của Subagent 1 một bộ **Risk Checklist 5 điểm** (bắt buộc luôn soi chiếu Concurrency, State Drift, Clock Latency, Idempotency, Data Integrity) và cơ chế tự động tra cứu Bug Repository để ép Agent phải liên hệ trước khi trả kết quả.

### Câu 7: Nếu đưa tool cho 10 tester sử dụng hằng ngày, bạn sẽ cải tiến điều gì đầu tiên?
* **Trả lời:** Tôi sẽ ưu tiên 3 cải tiến sau:
  1. *Jira / Confluence Webhook Integration:* Tester chỉ cần dán link Jira Ticket, tool tự đọc Story Description, phân tích và comment trực tiếp danh sách câu hỏi cho BA ngay trên Jira.
  2. *Vector Database & Dynamic RAG cho Bug Lịch Sử:* Nâng cấp kho bug từ file tĩnh lên ChromaDB/Qdrant với hàng nghìn ticket bug của công ty để Agent tìm bug tương quan theo độ tương đồng ngữ nghĩa (Cosine Similarity).
  3. *Feedback Loop (Upvote/Downvote):* Cho phép Tester đánh giá câu hỏi hoặc test case nào hữu ích, làm dữ liệu Few-shot tự động để Agent ngày càng thông minh hơn theo đặc thù sản phẩm của Caro.
