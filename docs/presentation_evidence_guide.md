# CẨM NANG THUYẾT TRÌNH & BỘ CÂU HỎI PHỎNG VẤN VỊ TRÍ AI QA SPECIALIST / LEAD
> **Ứng viên:** Vũ Thị Mai Linh  
> **Dự án thực nghiệm:** Antigravity Native QA Assistant (Requirement Analysis & Simulated Test Specification)  
> **Mục tiêu trọng tâm:** Đảm bảo tính đúng đắn của dữ liệu đầu ra & Đột phá Effort (Năng suất) của Team QA trong 3 tháng.  
> **Google Slides Trực Tiếp Trên Drive:** [Mở Google Slides tại đây](https://docs.google.com/presentation/d/1h1JpMhKIRf5wjqcwC-nGmCjU5mCCH5jNxw2e2ybTyWQ/edit?usp=drivesdk)

---

## PHẦN I: CHIẾN LƯỢC PHỎNG VẤN TỔNG THỂ (THE STRATEGIC GAME PLAN)

### 1. Định Vị Bản Thân
* Bạn **KHÔNG** xuất hiện như một Tester thông thường chỉ biết gõ prompt "Hãy viết test case cho tôi".
* Bạn xuất hiện với tư cách là một **AI QA Specialist / System Thinker & Architect**: Người làm chủ kiến trúc tác tử (Agent Topology), thiết lập kỷ luật điều phối (State Machine & Human Gates), xây dựng khung đánh giá độ chính xác dữ liệu (Data Correctness Framework), và có năng lực lãnh đạo chuyển đổi số (Change Management) giúp nâng tầm năng lực toàn bộ đội ngũ QA trong 90 ngày.

### 2. Thấu Cảm Nỗi Đau & Kỳ Vọng Của Người Phỏng Vấn
* **Họ sợ điều gì nhất?** Họ sợ AI "ảo giác" (hallucination), sinh ra hàng trăm test case rác, chung chung ("Verify HTTP 200"), dồn cụm hành động, sai lệch nghiệp vụ khiến tester mất thêm thời gian sửa và làm Dev mất niềm tin vào QA.
* **Họ mong đợi điều gì nhất?**
  1. **Tính đúng sai của dữ liệu (Data Fidelity & Accuracy):** Phải có cơ chế kiểm soát, đo lường bằng số liệu (Ground truth, Semantic correctness, 3 tầng kiểm chứng sâu).
  2. **Nâng cao Effort (Throughput & Efficiency):** Trong 3 tháng, công cụ này giúp team gánh được khối lượng công việc gấp đôi, gấp ba (từ 2-3 stories/sprint lên 6-8 stories/sprint), giải phóng tester khỏi các tác vụ cơ bắp để tập trung vào kiểm thử chất lượng cao.

---

## PHẦN II: KỊCH BẢN THUYẾT TRÌNH 5-7 PHÚT (PITCH SCRIPT THEO SLIDE)

*Lưu ý khi trình bày: Mở slide trình chiếu tại tệp [docs/presentation.html](file:///home/linh/QA/docs/presentation.html) trên trình duyệt hoặc dùng [docs/QA_AI_Assistant_Interview_Presentation.pptx](file:///home/linh/QA/docs/QA_AI_Assistant_Interview_Presentation.pptx).*

---

### 🎙️ Slide 1: Giới Thiệu & Cam Kết 90 Ngày (Thời lượng: ~45 giây)
> *"Chào các anh/chị trong hội đồng phỏng vấn. Tôi là Vũ Thị Mai Linh. Hôm nay tôi rất hào hứng được trình bày giải pháp: **'Ứng dụng Tác Tử AI Nâng Cao Effort & Đảm Bảo Tính Đúng Đắn Của Dữ Liệu Kiểm Thử Trong 3 Tháng'**.*
>
> *Dự án này không phải là một ý tưởng lý thuyết trên giấy, mà đã được tôi đóng gói và chạy thực nghiệm hoàn chỉnh dưới dạng một **Native Plugin trên nền tảng Antigravity**, kết hợp Google Workspace MCP Server.*
>
> *Khi nhận đề bài về việc team đánh giá hiệu quả dựa trên tính đúng sai của dữ liệu và đặt mục tiêu nâng effort trong 3 tháng, tôi cam kết 3 chỉ số cốt lõi: **Nâng dung lượng xử lý của team lên gấp 2.5 lần**, **Đảm bảo độ chính xác của bộ dữ liệu đầu ra đạt trên 92%**, và **Giảm 50% lỗi lọt sang giai đoạn phát triển** nhờ tư duy kiểm định sớm Shift-Left."*

---

### 🎙️ Slide 2: Bối Cảnh, Nỗi Đau & Bài Toán Cốt Lõi (Thời lượng: ~60 giây)
> *"Nhìn vào thực tế công việc của đội ngũ QA hiện nay, có đến **60-70% thời gian của tester bị chôn vùi vào hai việc thủ công**: cố gắng đọc hiểu những requirement mập mờ, và gõ đi gõ lại các kịch bản test lặp đi lặp lại. Hậu quả là mỗi sprint, một QA chỉ gánh được 2 đến 3 User Story phức tạp, đồng thời dễ dàng bỏ sót các lỗi kiến trúc ngầm như Race Condition, State Drift hay Timeout giữa các Microservices.*
>
> *Nhiều người nghĩ ngay đến việc đưa ChatGPT hay LLM vào viết test. Nhưng cách làm ngây thơ đó thường thất bại vì **bẫy ảo giác (Hallucination)**: AI tự bịa endpoint, suy diễn quy tắc sai so với thực tế, và tệ nhất là **Gom cụm hành động (Action Bundling)** — ví dụ dồn cả bước chọn hàng, thanh toán và click submit vào một bước kiểm thử duy nhất. Kịch bản như vậy hoàn toàn vô giá trị với đội Automation.*
>
> *Giải pháp tôi xây dựng trong repo giải quyết triệt để vấn đề này bằng một **Strict 2-Phase State Machine kết hợp 3 Nguyên Tắc Vàng QA thực chiến**, đảm bảo dữ liệu sinh ra sạch, chuẩn và thực thi được ngay."*

---

### 🎙️ Slide 3: Kiến Trúc Tác Tử & 2-Phase State Machine (Thời lượng: ~90 giây)
> *"Về mặt kiến trúc, tôi chủ động **không xây dựng một hệ thống backend CRUD cồng kềnh**, mà ứng dụng mô hình Native Customization Plugin với sự điều phối của Orchestrator và 2 Subagents độc lập:*
>
> * **Phase 1 (Static Analysis):** Do Subagent `req-risk-analyst` phụ trách. Agent này bóc tách 4 thành tố nghiệp vụ, đặt câu hỏi phản biện BA, đối chiếu với Cẩm nang 5 góc khuất kỹ thuật (`risk-checklist.md`), và liên kết với Kho 10 Bug Lịch Sử chuẩn hóa (`bug_repository.json`). Quan trọng nhất: **Agent này tuyệt đối không được tự ý sinh test case!**
> * **🛑 Human Gate 1 (Cổng kiểm soát 1):** Hệ thống bắt buộc dừng lại. Tester trực tiếp phản biện, chỉnh sửa logic. Nếu phát hiện requirement đổi, hệ thống sẽ rollback toàn bộ.
> * **Phase 2 (Dynamic Test Design):** Chỉ khi Tester bấm duyệt ở Gate 1, Subagent `test-automation-architect` mới được kích hoạt để sinh đúng 5 kịch bản theo Ma trận kiểm thử (`test-design-matrix.md`): Happy Path, Boundary Value, Negative, Concurrency đa luồng, và State Conflict & Recovery.
> * **Phase 3 (Local-First & Cloud Sync):** Tester duyệt ở Gate 2, toàn bộ dữ liệu được lưu tích lũy nối tiếp (Append-Only) vào local JSON và đồng bộ ngay lập tức lên Google Sheets Master thông qua MCP Server với giao diện chuẩn Ant Design Blue.
>
> *Ngoài ra, hệ thống tích hợp **Bộ nhớ góc nhìn (`user_preferences.json`)**, cho phép linh hoạt chuyển đổi giữa góc nhìn Nghiệp vụ (ngôn ngữ đời sống cho BA) và góc nhìn Kỹ thuật (thuật ngữ chuyên sâu cho SDET) mà vẫn tự động ghi nhớ qua các phiên làm việc."*

---

### 🎙️ Slide 4: Khung Đánh Giá Tính Đúng - Sai Của Dữ Liệu (Thời lượng: ~90 giây)
> *"Bây giờ, xin phép trả lời trực diện vào tiêu chí quan trọng nhất của hội đồng: **'Làm sao đánh giá tính đúng sai của bộ dữ liệu trả ra?'**.*
>
> *Tôi thiết lập bộ 4 chỉ số đo lường chất lượng dữ liệu:
> 1. **Semantic Accuracy (Độ đúng nghiệp vụ ≥ 92%):** Đo lường tỷ lệ quy tắc nghiệp vụ và câu hỏi BA được PO/BA xác nhận là chính xác và có giá trị.
> 2. **Schema Validity (Chuẩn cấu trúc 100%):** Bắt buộc tuân thủ 3 tầng kiểm chứng: UI hiển thị gì, API Response Body trả về trường nào cụ thể, và Database cập nhật bảng nào, cột nào, sự kiện Kafka gì phát ra.
> 3. **Risk Coverage (Độ bao phủ rủi ro 100%):** Bao phủ đủ 5 loại kịch bản kiểm thử bắt buộc và 5 góc khuất kỹ thuật.
> 4. **Hallucination Rate (< 5%):** Khống chế tỷ lệ suy diễn sai lệch dưới 5%.
>
> *Để đạt được điều này, hệ thống áp dụng **3 Nguyên Tắc Vàng Chuẩn QA/QC Thực Chiến**:
> * **Nguyên tắc 1 - Step Disaggregation:** Phân tách rạch ròi bước chuẩn bị dữ liệu và bước kích hoạt. Không bao giờ dồn thao tác.
> * **Nguyên tắc 2 - Synchronized Deep Verification:** Không chỉ ghi HTTP Status chung chung, mà kiểm tra sâu tính đồng bộ giữa UI, Payload API và dữ liệu thực tế trong Database.
> * **Nguyên tắc 3 - Anchoring bằng Kho Bug Lịch Sử:** Agent luôn đối chiếu yêu cầu với các mẫu bug thực chiến trong kho bug (`BUG-001` đến `BUG-010`) như một bộ Ground Truth ngữ nghĩa, buộc AI phải bám rễ vào thực tế thay vì tưởng tượng viển vông."*

---

### 🎙️ Slide 5: Minh Chứng Thực Nghiệm Trên 3 Requirement Mẫu (Thời lượng: ~60 giây)
> *"Minh chứng rõ nhất cho tính đúng đắn của giải pháp nằm ở kết quả thực nghiệm trên 3 requirement thực tế trong repo:
> 1. **Với bài toán Khóa tài khoản sau 5 lần sai mật khẩu (`REQ_AUTH_LOCK_001`):** Tool đã phát hiện ngay kẽ hở Force Logout — nếu tài khoản bị khóa thì các Token đang hoạt động ở thiết bị khác có bị thu hồi tức thì không, đồng thời đối chiếu chính xác với `BUG-001` và `BUG-003`.
> 2. **Với bài toán Chống bán âm kho (`REQ_INV_001`):** Tool phân biệt chính xác Tồn kho vật lý và Tồn kho khả dụng, sinh kịch bản Concurrency mô phỏng 2 người tranh mua sản phẩm cuối cùng ($N=1$) trong vòng dưới 50ms, liên kết `BUG-005`.
> 3. **Với bài toán Voucher dùng 1 lần (`REQ_20261016_001`):** Tool mô hình hóa trọn vẹn vòng đời voucher và kịch bản Giao dịch bù trừ (Compensating Transaction) khi khách hủy đơn hoặc timeout.
>
> *Điều tôi tâm đắc nhất là **quá trình tự nắn chỉnh thực tế**: Ban đầu AI trả lời bằng văn bản dài và dùng từ ngữ quá hàn lâm, tôi đã bổ sung bộ cấu hình ghi nhớ góc nhìn và chuyển sang định dạng Thẻ & Bảng Ma trận trực quan. Ban đầu AI dồn bước, tôi đã đưa 3 Nguyên Tắc Vàng vào Prompt và Rules cứng để chuẩn hóa 100% test case sinh ra."*

---

### 🎙️ Slide 6: Lộ Trình 3 Tháng Nâng Vọt Effort Của Team (Thời lượng: ~60 giây)
> *"Để biến công cụ này thành bệ phóng nâng vọt Effort của team trong 90 ngày, tôi đã vạch sẵn lộ trình 3 giai đoạn rõ ràng:
> * **Tháng 1 (Foundation & Baseline):** Xây dựng bộ 'Golden Dataset' gồm 50 User Story chuẩn làm thước đo Ground Truth. Triển khai pilot trên 1 Scrum Team (3-5 QA). Mục tiêu Tháng 1: Đạt độ chính xác dữ liệu $\ge 85\%$ và giảm ngay 40% thời gian viết test case ban đầu.
> * **Tháng 2 (Integration & Scaling):** Tích hợp Jira/Xray MCP để tự động đọc ticket và đồng bộ kịch bản test. Thiết lập cơ chế Feedback Loop (Upvote/Downvote) để prompt tự tiến hóa theo đặc thù sản phẩm của công ty. Mở rộng ra toàn bộ 10-15 QA. Mục tiêu Tháng 2: Độ chính xác $\ge 92\%$, giảm 60% lead-time phân tích.
> * **Tháng 3 (Autonomous Multiplier):** Tận dụng các bước giả lập 3 tầng đã chuẩn hóa để tự động sinh mã kiểm thử Automation thực thi (Playwright / k6). Tích hợp vào CI/CD. **Mục tiêu Tháng 3: Nâng dung lượng xử lý (Effort) của team lên gấp 2.5 lần**, giảm 50% bug lọt sang môi trường Staging/Production, và tiết kiệm 15-20 giờ làm việc cho mỗi QA trong từng sprint."*

---

### 🎙️ Slide 7: Kết Luận & Định Hướng Đóng Góp (Thời lượng: ~30 giây)
> *"Tóm lại, triết lý của tôi khi ứng dụng AI trong QA không phải là thay thế con người, mà là **chuyển dịch vị thế của QA từ người gõ test case thủ công thành một AI QA Orchestrator & System Thinker**.
>
> *Bằng cách giải phóng 60% thời gian cơ bắp, QA sẽ có thêm không gian để tập trung vào Exploratory Testing, Security, Performance và tối ưu chất lượng sản phẩm. Với toàn bộ nền tảng, mã nguồn và kinh nghiệm thực chiến đã có sẵn trong repo này, tôi tự tin có thể bắt tay vào triển khai và mang lại giá trị đo đếm được cho công ty ngay từ tuần đầu tiên.
>
> *Xin cảm ơn các anh/chị và tôi rất mong nhận được câu hỏi từ hội đồng!"*

---

## PHẦN III: BỘ 10 CÂU HỎI PHỎNG VẤN HÓC BÚA NHẤT & KỊCH BẢN TRẢ LỜI

### Câu 1: Team chúng tôi đánh giá hiệu quả dựa trên "tính đúng sai của bộ dữ liệu trả ra". Bạn định nghĩa và đo lường độ đúng sai này bằng phương pháp cụ thể nào?
* **Điểm mấu chốt cần thể hiện:** Không trả lời chung chung theo cảm tính. Phải đưa ra công thức, bộ chỉ số (Metric) và quy trình đo kiểm định lượng.
* **Kịch bản trả lời mẫu:**
  > *"Để đánh giá tính đúng sai của bộ dữ liệu do AI trả ra một cách khách quan, tôi chia chất lượng dữ liệu thành 3 tầng đo lường độc lập:*
  >
  > 1. *Tầng Cú pháp & Cấu trúc (Syntactic Validity - 100%): Dùng Rule-based Validator để kiểm tra tự động xem dữ liệu có vi phạm schema không: Test case có bị gom cụm bước không? Có đủ 3 tầng kỳ vọng UI, API JSON Body, và Database assertion không? Trạng thái có đúng định dạng không? Nếu vi phạm bất kỳ tiêu chí nào, điểm cấu trúc là Fail.*
  > 2. *Tầng Ngữ nghĩa & Nghiệp vụ (Semantic Correctness - Target ≥ 92%): Tôi đo lường dựa trên **Bộ Ground Truth (Golden Dataset)**. Khi một requirement được đưa vào, kết quả bóc tách Business Rules và kịch bản test sẽ được đối chiếu với tập đáp án chuẩn đã được Lead QA và PO phê duyệt trước đó, đo lường theo tỷ lệ Precision (kịch bản sinh ra có đúng không) và Recall (có bao phủ hết các rule bắt buộc không).*
  > 3. *Tầng Kiểm soát Ảo giác (Hallucination Rate - Target < 5%): Đo lường tỷ lệ các trường hợp AI tự suy diễn các API endpoint không có thật, hoặc tự bịa ra các ràng buộc logic mâu thuẫn với requirement gốc.*
  >
  > *Nhờ quy trình 2-Phase State Machine có Cổng kiểm soát của con người (Human Gate 1), bất kỳ sai lệch nghiệp vụ nào đều bị tester chặn lại ngay từ khâu phân tích tĩnh, triệt tiêu hoàn toàn nguy cơ rác lọt sang bộ kịch bản test ở Phase 2."*

---

### Câu 2: Trong 3 tháng, làm thế nào để bạn nâng "Effort" (năng suất) của team lên gấp đôi hoặc gấp ba mà không làm giảm chất lượng?
* **Điểm mấu chốt cần thể hiện:** Chứng minh được sự chuyển đổi từ "làm việc thủ công cơ bắp" sang "làm việc đòn bẩy AI", có lộ trình từng tháng rõ ràng.
* **Kịch bản trả lời mẫu:**
  > *"Nâng effort ở đây bản chất là **nâng dung lượng xử lý (Capacity / Throughput) của team QA trên cùng một đơn vị thời gian** mà không cần tuyển thêm nhân sự. Tôi đạt được mục tiêu này qua 3 đòn bẩy trong 90 ngày:*
  >
  > * *Đòn bẩy 1: Rút ngắn 60-70% thời gian soạn thảo ban đầu (Tháng 1).* Bình thường tester mất từ 1-2 ngày để đọc spec, hình dung ca kiểm thử và gõ từng dòng test case lên Excel/Jira. Với Agent, bản thảo Phase 1 và 5 kịch bản Phase 2 được sinh trong vòng chưa đầy 2 phút. Tester chỉ đóng vai trò là 'Reviewer & Approver', rút ngắn thời gian chuẩn bị xuống còn 2-3 giờ/story.
  > * *Đòn bẩy 2: Tích hợp hệ sinh thái & Loại bỏ thao tác nhập liệu thủ công (Tháng 2).* Kết nối Jira và Xray qua MCP. Tester chỉ cần nhập Issue Key, toàn bộ kịch bản được sync tự động lên bảng tính hoặc Jira Test Execution mà không phải copy-paste tay.
  > * *Đòn bẩy 3: Chuyển đổi kịch bản giả lập thành Automation Script thực thi (Tháng 3).* Nhờ nguyên tắc Step Disaggregation và đặc tả API/DB sâu ở Phase 2, các bước giả lập có cấu trúc đồng nhất để sinh thẳng ra file kịch bản Playwright hoặc k6.
  >
  > *Khi giải phóng được khoảng 15-20 giờ làm việc mỗi sprint cho mỗi tester, dung lượng xử lý của team sẽ tự nhiên tăng vọt từ 2.5 đến 3 lần, trong khi độ bao phủ ca biên và ca concurrency lại cao hơn nhiều so với trước đây."*

---

### Câu 3: "Ảo giác" (Hallucination) là vấn đề nhức nhối nhất của LLM. Trong dự án của bạn, bạn đã áp dụng những kỹ thuật gì để triệt tiêu ảo giác?
* **Điểm mấu chốt cần thể hiện:** Phân tích kỹ thuật (Grounding, State Machine, Reference Manuals, Few-shot Anchoring).
* **Kịch bản trả lời mẫu:**
  > *"Để triệt tiêu ảo giác, tôi không trông chờ vào việc 'năn nỉ LLM đừng nói dối trong prompt', mà thiết lập một **Kiến trúc phòng vệ nhiều lớp (Defense-in-depth Architecture)**:*
  >
  > 1. *Ràng buộc nguồn tri thức xác thực (Strict Knowledge Grounding):* Agent không suy diễn tự do trên Internet, mà được neo giữ (anchored) vào 3 nguồn tri thức chuẩn trong repo: Cẩm nang 5 góc khuất kỹ thuật (`risk-checklist.md`), Ma trận 5 loại kịch bản (`test-design-matrix.md`), và Kho 10 Bug Lịch Sử thực tế (`bug_repository.json`).
  > 2. *Tách rời 2 pha (2-Phase Decoupling):* Không bao giờ cho AI sinh test case ngay ở lượt đầu tiên. Bắt buộc hoàn thành Phase 1 (Business Rules & BA Questions) và phải có sự gật đầu của Tester tại Human Gate 1. Nếu logic đầu vào sai, hệ thống dừng lại ngay lập tức, không cho phép rác lan truyền sang Phase 2.
  > 3. *Tách nhỏ Context theo nguyên lý Progressive Disclosure:* Thay vì nhồi một mega-prompt hàng nghìn dòng khiến LLM bị loãng ngữ cảnh và bắt đầu bịa chuyện, tôi bóc tách kiến thức thành các module nhỏ trong thư mục `references/`, chỉ nạp khi cần tra cứu.
  > 4. *Quy tắc phủ định tất định (Deterministic Negative Constraints):* Trong rules điều phối `AGENTS.md`, tôi đặt các luật cấm cứng: Cấm gom cụm bước, cấm trả lời chung chung không có tên bảng/cột Database, cấm bypass qua Gate khi chưa có sự xác nhận của con người."*

---

### Câu 4: Giải thích rõ hơn về "3 Nguyên Tắc Vàng Chuẩn QA/QC Thực Chiến" trong repo của bạn? Vì sao bạn lại coi trọng Step Disaggregation đến vậy?
* **Điểm mấu chốt cần thể hiện:** Thể hiện kinh nghiệm thực chiến dày dặn về Automation Testing và bảo trì kịch bản.
* **Kịch bản trả lời mẫu:**
  > *"3 Nguyên tắc này được đúc rút từ chính những thất bại khi đưa AI vào các dự án kiểm thử thực tế:*
  >
  > 1. *Nguyên tắc 1: Step Disaggregation (Tách bước độc lập).* Lỗi phổ biến nhất của AI là dồn hành động: 'Người dùng chọn số lượng = 3, chọn thanh toán COD, bấm Đặt hàng'. Khi đưa kịch bản này cho đội Automation hoặc khi chạy test tự động, nếu bước này Fail, tester không thể biết hệ thống chết vì UI không nhận số lượng, hay do radio button thanh toán lỗi, hay do API checkout timeout. Việc tách riêng: Tiền đề đưa vào Pre-condition, Bước 1 là chọn dữ liệu, Bước 2 là click trigger giúp test case có tính nguyên tử (atomic), xác định đúng 100% vị trí lỗi.
  > 2. *Nguyên tắc 2: Synchronized Deep Verification (Kiểm chứng sâu 3 tầng).* Một test case chuyên nghiệp không thể chỉ ghi 'Verify HTTP 200'. Nó phải kiểm tra 3 tầng: UI hiển thị thông báo gì và mã đơn nào; API trả về HTTP Status và trường JSON nào cụ thể (ví dụ trường `order_id` phải khớp với UI); và Database có ghi nhận bản ghi mới không, cột tồn kho giảm bao nhiêu, Kafka có phát sự kiện gì không.
  > 3. *Nguyên tắc 3: Cột Trạng thái kiểm thử (Execution Status).* Bắt buộc có cột trạng thái với giá trị mặc định là `NOT_RUN`, đi kèm Data Validation Dropdown (Pass/Fail/Blocked) và tô màu tự động trên Google Sheets, giúp việc quản trị tiến độ và báo cáo defect minh bạch tuyệt đối."*

---

### Câu 5: Có phần nào trong quy trình mà bạn CHỦ ĐỘNG KHÔNG GIAO CHO AI không? Tại sao?
* **Điểm mấu chốt cần thể hiện:** Nhận thức rõ ràng về giới hạn của AI và trách nhiệm tối cao của con người trong kiểm thử phần mềm.
* **Kịch bản trả lời mẫu:**
  > *"Có 3 phần cốt lõi tôi chủ động nắm quyền kiểm soát tuyệt đối và không bao giờ giao phó cho AI:*
  >
  > 1. *Thiết kế Kiến trúc Tác tử & Phân quyền (Agent Topology):* AI không thể tự quyết định nên có bao nhiêu Subagents, nhiệm vụ từng tác tử ra sao và ranh giới trách nhiệm thế nào. Tôi trực tiếp thiết kế mô hình 2 Subagents tách biệt (`req-risk-analyst` chỉ phân tích tĩnh, `test-automation-architect` chỉ thiết kế test) để đảm bảo tính chuyên môn hóa và kiểm soát context.
  > 2. *Cổng Phê Duyệt Quyết Định Nghiệp Vụ (Human Gates):* AI chỉ là người đề xuất (Suggester), con người luôn là người quyết định (Decider). Việc chốt xem quy tắc nghiệp vụ đã đúng chưa, rủi ro có chấp nhận được không và kịch bản test có được đẩy lên hệ sinh thái chung của công ty không bắt buộc phải qua sự phê duyệt của Tester tại Gate 1 và Gate 2.
  > 3. *Nguồn Tri Thức Chuẩn Hóa (Authoritative Sources):* Toàn bộ tài liệu tham chiếu, quy tắc tính tiền, bảng lỗi lịch sử (`data/bug_repository.json`) phải do con người kiểm duyệt và cung cấp, tuyệt đối không để AI tự ý tìm kiếm hay suy đoán lung tung trên mạng."*

---

### Câu 6: Trong repo, bạn có cơ chế "Lựa chọn & Ghi nhớ Góc nhìn" (Perspective Persistence). Tính năng này giải quyết bài toán gì trên thực tế?
* **Điểm mấu chốt cần thể hiện:** Khả năng giao tiếp đa đối tượng (Stakeholder Communication) và giải quyết rào cản ứng dụng (Adoption Barrier).
* **Kịch bản trả lời mẫu:**
  > *"Trong một squad phát triển phần mềm, đối tượng đọc kết quả phân tích yêu cầu có 2 nhóm người rất khác nhau:*
  >
  > * *Nhóm 1 là Product Owner và BA:* Họ quan tâm đến hành vi người dùng, luồng kinh doanh, điều kiện khuyến mãi. Nếu Agent trả lời bằng các từ như 'Race Condition', 'Lost Update', 'Redis INCR', 'Clock Drift', họ sẽ cảm thấy xa lạ và không muốn đọc tiếp.
  > * *Nhóm 2 là SDET và Backend Dev:* Họ cần biết chính xác điểm nghẽn kỹ thuật nằm ở đâu: Lock ở tầng nào, Transaction có bị phân tán không, JWT Token có bị thu hồi không.
  >
  > *Tính năng `user_preferences.json` cho phép hệ thống linh hoạt chuyển đổi giữa 3 góc nhìn: `business` (chuyển hóa rủi ro kỹ thuật thành câu chuyện đời sống dễ hiểu), `technical` (đi sâu vào kiến trúc phân tán), và `hybrid` (trình bày song song cả hai). Điều đặc biệt là hệ thống tự động ghi nhớ tùy chọn này của người dùng qua các phiên làm việc, giúp công cụ thích nghi hoàn hảo với văn hóa làm việc của từng thành viên trong team."*

---

### Câu 7: Nếu một requirement bị thay đổi giữa chừng (ví dụ BA đổi ý từ khóa 5 lần thành khóa 3 lần), hệ thống của bạn xử lý thế nào?
* **Điểm mấu chốt cần thể hiện:** Cơ chế Rollback và quản lý tính nhất quán trạng thái (State Invalidation).
* **Kịch bản trả lời mẫu:**
  > *"Đây chính là lý do tôi xây dựng **Luật Rollback khi đổi Requirement (Rule 4 trong AGENTS.md)**.*
  >
  > *Nếu Tester hoặc BA thay đổi, bổ sung hoặc hủy bỏ yêu cầu khi đang ở Phase 2 hoặc giữa các pha, hệ thống lập tức **Vô hiệu hóa (Invalidate)** toàn bộ các test case đã sinh ở Phase 2. Toàn bộ state được rollback trở về Phase 1 để bóc tách lại Business Rules và phân tích lại 5 góc khuất kỹ thuật dựa trên phạm vi mới.
  >
  > *Chỉ khi Tester phê duyệt lại kết quả Phase 1 mới, Phase 2 mới được phép tái sinh kịch bản. Cơ chế này ngăn chặn triệt để tình trạng 'Kịch bản test râu ông nọ cắm cằm bà kia' — một lỗi rất phổ biến khi QA dùng AI chat tự do mà không có State Machine quản lý."*

---

### Câu 8: Bạn thiết kế cơ chế lưu trữ "Local-First & Bidirectional Sync" với Google Workspace như thế nào và tại sao lại dùng "Accumulative Append-Only"?
* **Điểm mấu chốt cần thể hiện:** Tính bền vững của dữ liệu (Data Integrity & Disaster Recovery).
* **Kịch bản trả lời mẫu:**
  > *"Hệ thống được thiết kế theo triết lý **Local-First kết hợp Đồng bộ 2 chiều qua MCP Server**:
  >
  > 1. *Tại sao Local-First:* Dữ liệu luôn được lưu trữ và cập nhật vào các tệp JSON cục bộ (`data/`) trước. Nếu mất mạng hoặc MCP gặp sự cố, hệ thống tự động fallback đọc từ local, đảm bảo công việc kiểm thử của QA không bao giờ bị gián đoạn (Zero Downtime).
  > 2. *Chống Cache Stale bằng Metadata:* Tệp `.sync_metadata.json` lưu trữ `modifiedTime` của Google Drive. Đầu mỗi phiên, hệ thống kiểm tra nhanh `modifiedTime` qua API; nếu Drive có thay đổi thì mới pull về local, tối ưu hóa tối đa số lượng request gọi lên Drive.
  > 3. *Chế độ Tích Lũy Bền Vững (Accumulative Append-Only):* Tuyệt đối không bao giờ dùng lệnh `clear()` làm trắng bảng tính. Mọi requirement và test case mới đều được cấp mã định danh duy nhất (`requirement_id`) và ghi nối tiếp vào các dòng tiếp theo ở cuối bảng. Điều này biến Google Spreadsheet thành một **Kho Tri Thức Kiểm Thử Tích Lũy Xuyên Suốt (Cumulative Test Repository)** của toàn bộ tổ chức qua thời gian."*

---

### Câu 9: Trong quá trình chạy thực nghiệm với 3 requirement mẫu trong repo, bài học kinh nghiệm sâu sắc nhất mà bạn rút ra là gì?
* **Điểm mấu chốt cần thể hiện:** Sự trung thực, khả năng tự soi chiếu (Reflective Thinking) và năng lực giải quyết vấn đề thực tế.
* **Kịch bản trả lời mẫu:**
  > *"Bài học sâu sắc nhất của tôi là: **'Một prompt tốt không bằng một quy chuẩn cấu trúc tốt'**.*
  >
  > *Ở phiên bản đầu tiên, tôi nghĩ chỉ cần viết một System Prompt thật dài, thật chi tiết là AI sẽ làm tốt. Nhưng thực tế chứng minh:
  > * AI sinh ra những đoạn văn phân tích dài dằng dặc như một bức tường chữ (Text Wall), không ai có kiên nhẫn đọc hết.
  > * Dữ liệu đẩy lên Google Sheets bị co rúm, tràn viền, không có dòng tiêu đề cố định trông rất thiếu chuyên nghiệp.
  > * Kịch bản test dồn bước khiến việc thực thi tự động gặp bế tắc.
  >
  > *Tôi đã giải quyết dứt điểm bằng cách:
  > * Tái cấu trúc phản hồi thành dạng **Thẻ tóm tắt & Bảng Ma trận (Card & Table-Driven)** để thông tin đập vào mắt ngay lập tức.
  > * Đưa 3 Nguyên Tắc Vàng vào luật điều phối runtime.
  > * Viết riêng script `google_sheets_sync_manager.py` tự động áp dụng bộ màu Ant Design Blue (`#1677FF`), tự động wrap text, set pixel cột rộng rãi, tích hợp Data Validation Dropdown và Conditional Formatting.
  >
  > *Kết quả là bộ kịch bản test không chỉ đúng về mặt logic mà còn đạt chuẩn thẩm mỹ và tính khả dụng của một phần mềm doanh nghiệp cấp độ Enterprise."*

---

### Câu 10: Giả sử ban giám đốc hỏi bạn: "Làm sao chứng minh được khoản đầu tư vào AI cho QA này mang lại ROI (Lợi tức đầu tư) thực tế?", bạn sẽ trả lời thế nào?
* **Điểm mấu chốt cần thể hiện:** Tư duy kinh doanh (Business Acumen) và khả năng quy đổi kết quả kỹ thuật thành giá trị tài chính.
* **Kịch bản trả lời mẫu:**
  > *"Tôi sẽ chứng minh ROI dựa trên 3 con số tài chính cụ thể sau 90 ngày:*
  >
  > 1. *Tiết kiệm chi phí nhân công trực tiếp (Direct Man-Hour Savings):* Với việc giảm 60% thời gian soạn thảo test case và họp làm rõ requirement, mỗi tester tiết kiệm được khoảng 15-20 giờ làm việc/sprint (tương đương 35-40 giờ/tháng). Với một team 10 QA, chúng ta tiết kiệm được khoảng 350-400 man-hours mỗi tháng — tương đương với năng suất làm việc của 2-2.5 kỹ sư QA full-time mà không cần phát sinh chi phí tuyển dụng hay bảo hiểm.
  > 2. *Giảm thiểu tổn thất do Defect lọt sang Production (Cost of Poor Quality):* Chi phí sửa một lỗi Concurrency hoặc bán âm kho khi đã lọt lên Production cao gấp 10 đến 30 lần so với việc bắt được ngay ở khâu phân tích tĩnh (chưa kể thiệt hại về uy tín thương hiệu và bồi thường khách hàng). Việc bắt được các kẽ hở như BUG-001 (Double refund) hay BUG-003 (Voucher race condition) ngay từ ngày đầu tiên của sprint mang lại giá trị bảo vệ tài chính vô cùng lớn.
  > 3. *Tăng tốc độ phát hành tính năng (Time-to-Market):* Khi kịch bản test được chuẩn hóa và sẵn sàng cho Automation ngay từ Phase 2, chu kỳ kiểm thử hồi quy (Regression Test Cycle) giảm từ 3 ngày xuống còn dưới 4 giờ, giúp doanh nghiệp phát hành tính năng mới nhanh hơn đối thủ cạnh tranh ít nhất 1 tuần mỗi chu kỳ release."*

---

## PHẦN IV: BỘ 5 CÂU HỎI THÔNG MINH ỨNG VIÊN HỎI LẠI NHÀ TUYỂN DỤNG

*(Hỏi những câu này ở cuối buổi phỏng vấn sẽ ngay lập tức khẳng định vị thế Senior/Lead của bạn — biến bạn từ người bị chất vấn thành một đối tác tư vấn chiến lược cho doanh nghiệp).*

1. **Về Hiện Trạng & Baseline:**
   > *"Hiện tại team QA của công ty mình đang dành trung bình bao nhiêu % thời gian cho việc phân tích requirement và viết test case thủ công so với thời gian dành cho Automation và Exploratory Testing?"*
   > *(Mục đích: Khảo sát chính xác 'điểm nghẽn' về effort của họ để ướm thử mức độ cải thiện khi áp dụng giải pháp của mình).*

2. **Về Tiêu Chí Đánh Giá Tính Đúng Sai:**
   > *"Khi team đánh giá hiệu quả dựa trên tính đúng sai của bộ dữ liệu AI trả ra, hiện tại công ty đã có sẵn bộ Golden Dataset (Tập đề thi chuẩn) để benchmark định kỳ chưa, hay đang đánh giá qua việc review thủ công của các Senior QA?"*
   > *(Mục đích: Cho thấy bạn rất am hiểu về kỹ thuật đo lường AI chuẩn mực và sẵn sàng giúp họ xây dựng bộ Golden Dataset nếu họ chưa có).*

3. **Về Hệ Sinh Thái & Tooling:**
   > *"Hạ tầng quản lý kiểm thử hiện tại của công ty (như Jira, Xray, TestRail) đã mở các cổng API hoặc Webhook để sẵn sàng tích hợp các Agent điều phối hai chiều tự động chưa?"*
   > *(Mục đích: Đánh giá độ sẵn sàng về hạ tầng kỹ thuật của doanh nghiệp để chuẩn bị cho Giai đoạn 2 của lộ trình 90 ngày).*

4. **Về Vấn Đề Chất Lượng Lớn Nhất:**
   > *"Trong các đợt release gần đây, nhóm lỗi nào khiến team đau đầu nhất: Lỗi sai lệch logic nghiệp vụ giữa BA và Dev, hay các lỗi chạy đua dữ liệu (Concurrency, Timeout) ở tầng kiến trúc phân tán?"*
   > *(Mục đích: Kéo sự chú ý của họ vào đúng thế mạnh bóc tách 5 góc khuất kỹ thuật mà công cụ của bạn đã giải quyết xuất sắc trong repo).*

5. **Về Định Hướng Kỳ Vọng 90 Ngày:**
   > *"Nếu tôi gia nhập và trong 90 ngày giúp nâng dung lượng xử lý của team lên gấp 2.5 lần đồng thời kiểm soát độ chính xác dữ liệu trên 92%, điều đó sẽ đóng góp quan trọng nhất vào mục tiêu chiến lược nào của ban lãnh đạo trong năm nay?"*
   > *(Mục đích: Đóng lại buổi phỏng vấn bằng một câu hỏi mang tính cam kết kết quả và liên kết chặt chẽ với tầm nhìn lãnh đạo).*

---
*Chúc bạn có một buổi phỏng vấn xuất sắc và thuyết phục tuyệt đối vào ngày mai!*
