#!/usr/bin/env python3
import subprocess

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1700 780" width="1700" height="780" style="background:#F8FAFC; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <!-- Arrow Markers -->
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563EB" />
    </marker>
    <marker id="arrow-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#7C3AED" />
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#16A34A" />
    </marker>
    <marker id="arrow-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#DC2626" />
    </marker>
    <marker id="arrow-teal" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#0D9488" />
    </marker>

    <!-- Drop Shadows -->
    <filter id="card-shadow" x="-8%" y="-8%" width="116%" height="120%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0F172A" flood-opacity="0.07"/>
    </filter>
    <filter id="gate-shadow" x="-10%" y="-10%" width="120%" height="125%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#E11D48" flood-opacity="0.15"/>
    </filter>
  </defs>

  <!-- ==========================================
       TOP BAR: OVERVIEW HEADER
       ========================================== -->
  <rect x="30" y="20" width="1640" height="76" rx="12" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2" filter="url(#card-shadow)"/>
  
  <text x="56" y="52" fill="#1E40AF" font-size="18" font-weight="900">👑 SƠ ĐỒ TỔNG QUAN: QUY TRÌNH 2-PHASE STATE MACHINE &amp; 2 HUMAN GATES</text>
  <text x="56" y="76" fill="#2563EB" font-size="13" font-weight="600">Điều phối đa tác tử có kỷ luật • 2 Chốt chặn Tester chống 100% ảo giác • Lưu trữ Local-First &amp; Đồng bộ Cloud 2 chiều</text>

  <!-- Top Badges -->
  <g transform="translate(1080, 28)">
    <rect x="0" y="0" width="260" height="58" rx="8" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <text x="14" y="24" fill="#1D4ED8" font-size="12" font-weight="800">🧠 Bộ Nhớ Góc Nhìn Bền Vững</text>
    <text x="14" y="44" fill="#64748B" font-size="11">Business (BA) ↔ Technical (SDET)</text>
  </g>

  <g transform="translate(1360, 28)">
    <rect x="0" y="0" width="290" height="58" rx="8" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <text x="14" y="24" fill="#1D4ED8" font-size="12" font-weight="800">⚡ Đồng Bộ Drive &amp; Local-First</text>
    <text x="14" y="44" fill="#64748B" font-size="11">Append-Only • Không bao giờ xóa lịch sử</text>
  </g>

  <!-- ==========================================
       MAIN WORKFLOW CONTAINER
       ========================================== -->
  <rect x="30" y="116" width="1640" height="530" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="2" filter="url(#card-shadow)"/>

  <!-- ==========================================
       6 MAIN OVERVIEW BLOCKS
       ========================================== -->

  <!-- 1. BLOCK 0: PRE-FLIGHT -->
  <g transform="translate(50, 160)">
    <rect x="0" y="0" width="235" height="340" rx="14" fill="#F8FAFC" stroke="#3B82F6" stroke-width="2.5" filter="url(#card-shadow)"/>
    
    <!-- Header Badge -->
    <rect x="16" y="16" width="203" height="30" rx="6" fill="#DBEAFE"/>
    <text x="117" y="36" fill="#1E40AF" font-size="12" font-weight="900" text-anchor="middle">0. PRE-FLIGHT CHECK</text>

    <!-- Big Icon & Title -->
    <text x="117" y="105" font-size="42" text-anchor="middle">🔍⚡</text>
    <text x="117" y="142" fill="#1E293B" font-size="17" font-weight="900" text-anchor="middle">Khởi Tạo &amp; Cache</text>
    <text x="117" y="166" fill="#2563EB" font-size="12" font-weight="700" text-anchor="middle">Antigravity Engine</text>

    <!-- Key Points (High-Level Overview) -->
    <rect x="14" y="190" width="207" height="134" rx="8" fill="#FFFFFF" stroke="#BFDBFE"/>
    <text x="24" y="218" fill="#1E40AF" font-size="12" font-weight="800">• Nhận Input Requirement</text>
    <text x="24" y="246" fill="#1E40AF" font-size="12" font-weight="800">• Nạp Preferences Góc Nhìn</text>
    <text x="24" y="274" fill="#1E40AF" font-size="12" font-weight="800">• So Khớp modifiedTime Drive</text>
    <text x="24" y="302" fill="#15803D" font-size="12" font-weight="800">• Nạp 10 Bugs Ground Truth</text>
  </g>

  <!-- Arrow 0 -> 1 -->
  <path d="M 285 330 L 315 330" stroke="#3B82F6" stroke-width="3.5" fill="none" marker-end="url(#arrow-blue)"/>

  <!-- 2. BLOCK 1: PHASE 1 -->
  <g transform="translate(320, 160)">
    <rect x="0" y="0" width="245" height="340" rx="14" fill="#FAF5FF" stroke="#7C3AED" stroke-width="2.5" filter="url(#card-shadow)"/>
    
    <!-- Header Badge -->
    <rect x="16" y="16" width="213" height="30" rx="6" fill="#EDE9FE"/>
    <text x="122" y="36" fill="#6D28D9" font-size="12" font-weight="900" text-anchor="middle">PHA 1: PHÂN TÍCH RỦI RO</text>

    <!-- Big Icon & Title -->
    <text x="122" y="105" font-size="42" text-anchor="middle">🟣📋</text>
    <text x="122" y="142" fill="#1E293B" font-size="17" font-weight="900" text-anchor="middle">req-risk-analyst</text>
    <text x="122" y="166" fill="#7C3AED" font-size="12" font-weight="700" text-anchor="middle">Subagent Phân Tích Tĩnh</text>

    <!-- Key Points -->
    <rect x="14" y="190" width="217" height="134" rx="8" fill="#FFFFFF" stroke="#E9D5FF"/>
    <text x="24" y="218" fill="#6D28D9" font-size="12" font-weight="800">• Bóc Tách 4 Thành Tố Spec</text>
    <text x="24" y="246" fill="#6D28D9" font-size="12" font-weight="800">• Soạn Câu Hỏi Phản Biện BA</text>
    <text x="24" y="274" fill="#6D28D9" font-size="12" font-weight="800">• Quét 5 Rủi Ro Kỹ Thuật</text>
    
    <!-- Red Warning Pill -->
    <rect x="20" y="286" width="205" height="28" rx="6" fill="#FEE2E2" stroke="#F87171"/>
    <text x="122" y="304" fill="#991B1B" font-size="11" font-weight="900" text-anchor="middle">⛔ TUYỆT ĐỐI CẤM SINH TEST!</text>
  </g>

  <!-- Arrow 1 -> Gate 1 -->
  <path d="M 565 330 L 595 330" stroke="#7C3AED" stroke-width="3.5" fill="none" marker-end="url(#arrow-purple)"/>

  <!-- 3. BLOCK 2: HUMAN GATE 1 -->
  <g transform="translate(600, 145)">
    <rect x="0" y="0" width="225" height="370" rx="14" fill="#FFF1F2" stroke="#E11D48" stroke-width="3" filter="url(#gate-shadow)"/>
    
    <!-- Header Badge -->
    <rect x="16" y="16" width="193" height="32" rx="6" fill="#FFE4E6"/>
    <text x="112" y="37" fill="#BE123C" font-size="12.5" font-weight="900" text-anchor="middle">🛑 HUMAN GATE 1</text>

    <!-- Big Icon & Title -->
    <text x="112" y="112" font-size="44" text-anchor="middle">✋🔴</text>
    <text x="112" y="152" fill="#E11D48" font-size="18" font-weight="900" text-anchor="middle">Chốt Phân Tích</text>
    <text x="112" y="176" fill="#9F1239" font-size="12" font-weight="700" text-anchor="middle">Tester Kiểm Duyệt</text>

    <!-- Key Points -->
    <rect x="14" y="196" width="197" height="156" rx="8" fill="#FFFFFF" stroke="#FECDD3"/>
    <text x="24" y="224" fill="#991B1B" font-size="12" font-weight="900">• ĐIỂM DỪNG BẮT BUỘC</text>
    <text x="24" y="250" fill="#4C0519" font-size="11.5">• Tester phản biện với BA</text>
    <text x="24" y="274" fill="#4C0519" font-size="11.5">• Chặn 100% ảo giác logic</text>
    <text x="24" y="302" fill="#DC2626" font-size="11.5" font-weight="700">❌ Đổi spec: Sửa lại Pha 1</text>
    <text x="24" y="330" fill="#15803D" font-size="12" font-weight="900">✔ Pass: Mở cổng sang Pha 2</text>
  </g>

  <!-- Arrow Gate 1 -> Phase 2 (Green) -->
  <path d="M 825 330 L 855 330" stroke="#16A34A" stroke-width="4" fill="none" marker-end="url(#arrow-green)"/>
  <text x="840" y="318" fill="#16A34A" font-size="11" font-weight="900" text-anchor="middle">PASS</text>

  <!-- 4. BLOCK 3: PHASE 2 -->
  <g transform="translate(860, 160)">
    <rect x="0" y="0" width="250" height="340" rx="14" fill="#F0FDFA" stroke="#0D9488" stroke-width="2.5" filter="url(#card-shadow)"/>
    
    <!-- Header Badge -->
    <rect x="16" y="16" width="218" height="30" rx="6" fill="#CCFBF1"/>
    <text x="125" y="36" fill="#0F766E" font-size="12" font-weight="900" text-anchor="middle">PHA 2: THIẾT KẾ TEST</text>

    <!-- Big Icon & Title -->
    <text x="125" y="105" font-size="42" text-anchor="middle">🟢⚙️</text>
    <text x="125" y="138" fill="#1E293B" font-size="15.5" font-weight="900" text-anchor="middle">test-automation-architect</text>
    <text x="125" y="166" fill="#0D9488" font-size="12" font-weight="700" text-anchor="middle">Subagent Automation QA</text>

    <!-- Key Points -->
    <rect x="14" y="190" width="222" height="134" rx="8" fill="#FFFFFF" stroke="#99F6E4"/>
    <text x="24" y="218" fill="#0F766E" font-size="12" font-weight="800">• Ma Trận 5 Nhóm Kịch Bản</text>
    <text x="24" y="246" fill="#0F766E" font-size="12" font-weight="800">• Tách Nhỏ Bước (Disaggregate)</text>
    <text x="24" y="274" fill="#0F766E" font-size="12" font-weight="800">• Verify 3 Tầng: UI + API + DB</text>
    <text x="24" y="302" fill="#0F766E" font-size="12" font-weight="800">• Trạng Thái: NOT_RUN</text>
  </g>

  <!-- Arrow Phase 2 -> Gate 2 -->
  <path d="M 1110 330 L 1140 330" stroke="#0D9488" stroke-width="3.5" fill="none" marker-end="url(#arrow-teal)"/>

  <!-- 5. BLOCK 4: HUMAN GATE 2 -->
  <g transform="translate(1145, 145)">
    <rect x="0" y="0" width="225" height="370" rx="14" fill="#FFFBEB" stroke="#D97706" stroke-width="3" filter="url(#card-shadow)"/>
    
    <!-- Header Badge -->
    <rect x="16" y="16" width="193" height="32" rx="6" fill="#FEF3C7"/>
    <text x="112" y="37" fill="#B45309" font-size="12.5" font-weight="900" text-anchor="middle">🛑 HUMAN GATE 2</text>

    <!-- Big Icon & Title -->
    <text x="112" y="112" font-size="44" text-anchor="middle">📑⚖️</text>
    <text x="112" y="152" fill="#D97706" font-size="18" font-weight="900" text-anchor="middle">Duyệt Test Spec</text>
    <text x="112" y="176" fill="#92400E" font-size="12" font-weight="700" text-anchor="middle">Tester Nghiệm Thu</text>

    <!-- Key Points -->
    <rect x="14" y="196" width="197" height="156" rx="8" fill="#FFFFFF" stroke="#FDE68A"/>
    <text x="24" y="224" fill="#B45309" font-size="12" font-weight="900">• NGHIỆM THU TEST CASES</text>
    <text x="24" y="250" fill="#78350F" font-size="11.5">• Duyệt độ bao phủ &amp; 3 tầng</text>
    <text x="24" y="274" fill="#78350F" font-size="11.5">• Xác nhận tính khả thi E2E</text>
    <text x="24" y="302" fill="#DC2626" font-size="11.5" font-weight="800">❌ Đổi spec: Rollback Pha 1</text>
    <text x="24" y="330" fill="#15803D" font-size="12" font-weight="900">✔ Pass: Mở cổng ghi Cloud</text>
  </g>

  <!-- Arrow Gate 2 -> Phase 3 (Green) -->
  <path d="M 1370 330 L 1400 330" stroke="#16A34A" stroke-width="4" fill="none" marker-end="url(#arrow-green)"/>
  <text x="1385" y="318" fill="#16A34A" font-size="11" font-weight="900" text-anchor="middle">PASS</text>

  <!-- 6. BLOCK 5: PHASE 3 -->
  <g transform="translate(1405, 160)">
    <rect x="0" y="0" width="240" height="340" rx="14" fill="#F0FDF4" stroke="#16A34A" stroke-width="2.5" filter="url(#card-shadow)"/>
    
    <!-- Header Badge -->
    <rect x="16" y="16" width="208" height="30" rx="6" fill="#DCFCE7"/>
    <text x="120" y="36" fill="#15803D" font-size="12" font-weight="900" text-anchor="middle">PHA 3: LƯU &amp; CLOUD SYNC</text>

    <!-- Big Icon & Title -->
    <text x="120" y="105" font-size="42" text-anchor="middle">🟡☁️</text>
    <text x="120" y="142" fill="#1E293B" font-size="17" font-weight="900" text-anchor="middle">Workspace Sync</text>
    <text x="120" y="166" fill="#16A34A" font-size="12" font-weight="700" text-anchor="middle">Local-First &amp; Google Sheets</text>

    <!-- Key Points -->
    <rect x="14" y="190" width="212" height="134" rx="8" fill="#FFFFFF" stroke="#BBF7D0"/>
    <text x="24" y="218" fill="#15803D" font-size="12" font-weight="800">• 1. Lưu Cục Bộ (Append-Only)</text>
    <text x="24" y="246" fill="#0958D9" font-size="12" font-weight="800">• 2. Push Google Sheets MCP</text>
    <text x="24" y="274" fill="#15803D" font-size="12" font-weight="800">• 3. Cập Nhật Metadata Drive</text>
    <text x="24" y="302" fill="#166534" font-size="12" font-weight="900">🎉 Hoàn Tất &amp; Bàn Giao</text>
  </g>

  <!-- ==========================================
       ROLLBACK LOOPS (ELEGANT CURVES AT BOTTOM)
       ========================================== -->
  <!-- Loop 1: Gate 1 -> Phase 1 -->
  <path d="M 680 515 C 680 570, 480 570, 480 505" stroke="#DC2626" stroke-width="2.5" stroke-dasharray="6 4" fill="none" marker-end="url(#arrow-red)"/>
  <rect x="525" y="555" width="110" height="24" rx="5" fill="#FEE2E2" stroke="#FCA5A5"/>
  <text x="580" y="571" fill="#991B1B" font-size="10.5" font-weight="800" text-anchor="middle">↩️ Sửa lại Pha 1</text>

  <!-- Loop 2: Gate 2 -> Phase 1 (Major Rollback) -->
  <path d="M 1255 515 C 1255 625, 400 625, 400 505" stroke="#DC2626" stroke-width="3" stroke-dasharray="8 4" fill="none" marker-end="url(#arrow-red)"/>
  <rect x="710" y="608" width="310" height="30" rx="6" fill="#FEF2F2" stroke="#DC2626" stroke-width="1.8"/>
  <text x="865" y="628" fill="#B91C1C" font-size="12" font-weight="900" text-anchor="middle">↩️ TỰ ĐỘNG ROLLBACK VỀ PHA 1 (KHI ĐỔI REQUIREMENT)</text>

  <!-- ==========================================
       BOTTOM SUMMARY BAR
       ========================================== -->
  <rect x="30" y="666" width="1640" height="88" rx="12" fill="#0F172A" stroke="#334155" stroke-width="1.5"/>
  <text x="56" y="698" fill="#60A5FA" font-size="13.5" font-weight="900">💡 NGUYÊN TẮC VẬN HÀNH TIẾN TRÌNH TUẦN TỰ (PROGRESSIVE DISCLOSURE):</text>
  <text x="56" y="726" fill="#E2E8F0" font-size="12">
    1. Khởi tạo &amp; xác thực cache  ➔  2. Phân tích rủi ro &amp; cấm sinh test  ➔  3. Tester chốt Gate 1  ➔  4. Thiết kế test 3 tầng  ➔  5. Tester nghiệm thu Gate 2  ➔  6. Ghi nối tiếp Cloud
  </text>
  
  <rect x="1350" y="680" width="300" height="60" rx="8" fill="#1E293B" stroke="#3B82F6" stroke-width="1.5"/>
  <text x="1500" y="705" fill="#38BDF8" font-size="12" font-weight="800" text-anchor="middle">👉 CHI TIẾT TỪNG PHẦN</text>
  <text x="1500" y="725" fill="#94A3B8" font-size="10.5" text-anchor="middle">Được trình bày sâu ở các slide tiếp theo</text>

</svg>"""

with open("/home/linh/QA/docs/state_machine_diagram.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("Clean Overview SVG written successfully to docs/state_machine_diagram.svg")

# Render to high-res PNG (1700x780)
cmd = [
    "/usr/bin/google-chrome",
    "--headless",
    "--disable-gpu",
    "--screenshot=/home/linh/QA/docs/state_machine_diagram.png",
    "--window-size=1700,780",
    "/home/linh/QA/docs/state_machine_diagram.svg"
]
subprocess.run(cmd, check=True)
print("PNG rendered successfully to docs/state_machine_diagram.png")
