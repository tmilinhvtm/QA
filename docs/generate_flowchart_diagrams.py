#!/usr/bin/env python3
"""
generate_flowchart_diagrams.py
Generates 6 authentic, beautiful flowchart diagrams (SVG + high-res PNG)
for the entire QA Requirement Assistant presentation:
  1. flowchart_overview.svg: Sơ đồ luồng tổng quan 2-Phase State Machine
  2. flowchart_stage0.svg: Sơ đồ luồng Chặng 0 (Pre-Flight, Preferences & Cache)
  3. flowchart_phase1.svg: Sơ đồ luồng Pha 1 (req-risk-analyst, Bóc tách & 5 Rủi ro)
  4. flowchart_gates.svg: Sơ đồ luồng Chốt chặn (Human Gates 1 & 2 + Rollback Loop)
  5. flowchart_phase2.svg: Sơ đồ luồng Pha 2 (test-automation-architect & 3 Tầng verify)
  6. flowchart_phase3.svg: Sơ đồ luồng Pha 3 (Local-First Append-Only & Google Sheets Sync)
"""

import os
import subprocess

COMMON_DEFS = """
  <defs>
    <!-- Arrow Markers -->
    <marker id="arr-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563EB" />
    </marker>
    <marker id="arr-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#7C3AED" />
    </marker>
    <marker id="arr-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#16A34A" />
    </marker>
    <marker id="arr-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#DC2626" />
    </marker>
    <marker id="arr-teal" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#0D9488" />
    </marker>
    <marker id="arr-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#D97706" />
    </marker>
    <marker id="arr-slate" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#475569" />
    </marker>

    <!-- Filters -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
    <filter id="shadow-gate" x="-8%" y="-8%" width="116%" height="120%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#E11D48" flood-opacity="0.14"/>
    </filter>
  </defs>
"""

# =============================================================================
# 1. FLOWCHART OVERVIEW (Slide 3)
# =============================================================================
svg_overview = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 680" width="1600" height="680" style="background:#FFFFFF; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
{COMMON_DEFS}

  <!-- Header Banner -->
  <rect x="20" y="16" width="1560" height="64" rx="10" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.8" filter="url(#shadow)"/>
  <text x="44" y="44" fill="#1E40AF" font-size="16" font-weight="900">👑 SƠ ĐỒ LUỒNG TỔNG QUAN: QUY TRÌNH STATE MACHINE 2-PHASE &amp; 2 HUMAN GATES</text>
  <text x="44" y="66" fill="#2563EB" font-size="12" font-weight="600">Luồng tuần tự có kiểm soát • 2 Điểm chặn Tester chống ảo giác • Cơ chế tự động Rollback khi đổi Requirement</text>

  <!-- Start Pill -->
  <rect x="25" y="270" width="140" height="60" rx="30" fill="#F1F5F9" stroke="#64748B" stroke-width="2" filter="url(#shadow)"/>
  <text x="95" y="296" fill="#1E293B" font-size="12" font-weight="800" text-anchor="middle">📄 BẮT ĐẦU</text>
  <text x="95" y="315" fill="#64748B" font-size="10.5" text-anchor="middle">Input Spec thô</text>

  <path d="M 165 300 L 205 300" stroke="#2563EB" stroke-width="2.5" fill="none" marker-end="url(#arr-blue)"/>

  <!-- Step 0: Pre-Flight -->
  <g transform="translate(210, 230)">
    <rect x="0" y="0" width="180" height="140" rx="10" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2" filter="url(#shadow)"/>
    <rect x="10" y="10" width="160" height="22" rx="4" fill="#DBEAFE"/>
    <text x="90" y="25" fill="#1E40AF" font-size="10" font-weight="900" text-anchor="middle">0. PRE-FLIGHT</text>
    <text x="90" y="58" font-size="24" text-anchor="middle">🔍⚡</text>
    <text x="90" y="85" fill="#1E293B" font-size="12.5" font-weight="800" text-anchor="middle">Cache &amp; Preferences</text>
    <text x="90" y="105" fill="#475569" font-size="10" text-anchor="middle">• Đọc user_preferences</text>
    <text x="90" y="122" fill="#475569" font-size="10" text-anchor="middle">• So khớp Drive modifiedTime</text>
  </g>

  <path d="M 390 300 L 430 300" stroke="#7C3AED" stroke-width="2.5" fill="none" marker-end="url(#arr-purple)"/>

  <!-- Step 1: Phase 1 -->
  <g transform="translate(435, 230)">
    <rect x="0" y="0" width="195" height="140" rx="10" fill="#FAF5FF" stroke="#7C3AED" stroke-width="2" filter="url(#shadow)"/>
    <rect x="10" y="10" width="175" height="22" rx="4" fill="#EDE9FE"/>
    <text x="97" y="25" fill="#6D28D9" font-size="10" font-weight="900" text-anchor="middle">PHA 1: req-risk-analyst</text>
    <text x="97" y="58" font-size="24" text-anchor="middle">🟣📋</text>
    <text x="97" y="85" fill="#1E293B" font-size="12.5" font-weight="800" text-anchor="middle">Phân Tích &amp; Rủi Ro</text>
    <text x="97" y="105" fill="#6D28D9" font-size="10" text-anchor="middle">• Bóc tách 4 thành tố</text>
    <text x="97" y="122" fill="#6D28D9" font-size="10" text-anchor="middle">• Câu hỏi BA &amp; 5 Rủi ro kỹ thuật</text>
  </g>

  <path d="M 630 300 L 670 300" stroke="#7C3AED" stroke-width="2.5" fill="none" marker-end="url(#arr-purple)"/>

  <!-- Decision Node: Human Gate 1 (Rhombus/Diamond) -->
  <g transform="translate(675, 220)">
    <polygon points="80,0 160,80 80,160 0,80" fill="#FFF1F2" stroke="#E11D48" stroke-width="2.5" filter="url(#shadow-gate)"/>
    <text x="80" y="60" fill="#BE123C" font-size="10" font-weight="900" text-anchor="middle">🛑 GATE 1</text>
    <text x="80" y="80" fill="#E11D48" font-size="12" font-weight="900" text-anchor="middle">Tester Chốt</text>
    <text x="80" y="98" fill="#E11D48" font-size="12" font-weight="900" text-anchor="middle">Phân Tích?</text>
  </g>

  <!-- Gate 1: Rejection / Edit Arrow back to Phase 1 -->
  <path d="M 755 220 C 755 160, 532 160, 532 225" stroke="#DC2626" stroke-width="2.2" stroke-dasharray="5 3" fill="none" marker-end="url(#arr-red)"/>
  <rect x="580" y="148" width="125" height="22" rx="4" fill="#FEE2E2" stroke="#FCA5A5"/>
  <text x="642" y="163" fill="#991B1B" font-size="9.5" font-weight="800" text-anchor="middle">❌ Chưa đạt / Đổi spec</text>

  <!-- Gate 1: Approved Arrow to Phase 2 -->
  <path d="M 835 300 L 880 300" stroke="#16A34A" stroke-width="3" fill="none" marker-end="url(#arr-green)"/>
  <rect x="838" y="278" width="38" height="18" rx="3" fill="#DCFCE7"/>
  <text x="857" y="291" fill="#15803D" font-size="9.5" font-weight="900" text-anchor="middle">PASS</text>

  <!-- Step 2: Phase 2 -->
  <g transform="translate(885, 230)">
    <rect x="0" y="0" width="205" height="140" rx="10" fill="#F0FDFA" stroke="#0D9488" stroke-width="2" filter="url(#shadow)"/>
    <rect x="10" y="10" width="185" height="22" rx="4" fill="#CCFBF1"/>
    <text x="102" y="25" fill="#0F766E" font-size="9.5" font-weight="900" text-anchor="middle">PHA 2: test-architect</text>
    <text x="102" y="58" font-size="24" text-anchor="middle">🟢⚙️</text>
    <text x="102" y="85" fill="#1E293B" font-size="12.5" font-weight="800" text-anchor="middle">Thiết Kế Test Auto</text>
    <text x="102" y="105" fill="#0F766E" font-size="10" text-anchor="middle">• Tách bước (Disaggregation)</text>
    <text x="102" y="122" fill="#0F766E" font-size="10" text-anchor="middle">• Ma trận 5 nhóm + 3 Tầng verify</text>
  </g>

  <path d="M 1090 300 L 1130 300" stroke="#0D9488" stroke-width="2.5" fill="none" marker-end="url(#arr-teal)"/>

  <!-- Decision Node: Human Gate 2 (Rhombus/Diamond) -->
  <g transform="translate(1135, 220)">
    <polygon points="80,0 160,80 80,160 0,80" fill="#FFFBEB" stroke="#D97706" stroke-width="2.5" filter="url(#shadow)"/>
    <text x="80" y="60" fill="#B45309" font-size="10" font-weight="900" text-anchor="middle">🛑 GATE 2</text>
    <text x="80" y="80" fill="#D97706" font-size="12" font-weight="900" text-anchor="middle">Tester Duyệt</text>
    <text x="80" y="98" fill="#D97706" font-size="12" font-weight="900" text-anchor="middle">Test Spec?</text>
  </g>

  <!-- Gate 2: Edit Arrow back to Phase 2 -->
  <path d="M 1215 220 C 1215 160, 987 160, 987 225" stroke="#D97706" stroke-width="2" stroke-dasharray="4 3" fill="none" marker-end="url(#arr-amber)"/>
  <rect x="1040" y="148" width="125" height="22" rx="4" fill="#FEF3C7" stroke="#FDE68A"/>
  <text x="1102" y="163" fill="#B45309" font-size="9.5" font-weight="800" text-anchor="middle">⚠️ Bổ sung kịch bản</text>

  <!-- Major Rollback Arrow from Gate 2 back to Phase 1 -->
  <path d="M 1215 380 C 1215 520, 532 520, 532 375" stroke="#DC2626" stroke-width="3" stroke-dasharray="8 4" fill="none" marker-end="url(#arr-red)"/>
  <rect x="740" y="495" width="270" height="28" rx="5" fill="#FEF2F2" stroke="#DC2626" stroke-width="1.5"/>
  <text x="875" y="514" fill="#B91C1C" font-size="11" font-weight="900" text-anchor="middle">↩️ TỰ ĐỘNG ROLLBACK VỀ PHA 1 (KHI ĐỔI REQUIREMENT)</text>

  <!-- Gate 2: Approved Arrow to Phase 3 -->
  <path d="M 1295 300 L 1340 300" stroke="#16A34A" stroke-width="3" fill="none" marker-end="url(#arr-green)"/>
  <rect x="1298" y="278" width="38" height="18" rx="3" fill="#DCFCE7"/>
  <text x="1317" y="291" fill="#15803D" font-size="9.5" font-weight="900" text-anchor="middle">PASS</text>

  <!-- Step 3: Phase 3 -->
  <g transform="translate(1345, 230)">
    <rect x="0" y="0" width="185" height="140" rx="10" fill="#F0FDF4" stroke="#16A34A" stroke-width="2" filter="url(#shadow)"/>
    <rect x="10" y="10" width="165" height="22" rx="4" fill="#DCFCE7"/>
    <text x="92" y="25" fill="#15803D" font-size="10" font-weight="900" text-anchor="middle">PHA 3: SYNC MANAGER</text>
    <text x="92" y="58" font-size="24" text-anchor="middle">🟡☁️</text>
    <text x="92" y="85" fill="#1E293B" font-size="12.5" font-weight="800" text-anchor="middle">Lưu &amp; Cloud Sync</text>
    <text x="92" y="105" fill="#15803D" font-size="10" text-anchor="middle">• Local Append-Only</text>
    <text x="92" y="122" fill="#15803D" font-size="10" text-anchor="middle">• Push Sheets &amp; Update Cache</text>
  </g>

  <!-- Finish Pill -->
  <path d="M 1437 370 L 1437 410" stroke="#16A34A" stroke-width="2.5" fill="none" marker-end="url(#arr-green)"/>
  <rect x="1362" y="415" width="150" height="50" rx="25" fill="#DCFCE7" stroke="#16A34A" stroke-width="2" filter="url(#shadow)"/>
  <text x="1437" y="438" fill="#166534" font-size="11.5" font-weight="900" text-anchor="middle">🎉 HOÀN TẤT</text>
  <text x="1437" y="454" fill="#15803D" font-size="9.5" text-anchor="middle">Bàn giao sạch 100%</text>

  <!-- Bottom Guidelines -->
  <rect x="20" y="575" width="1560" height="85" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5"/>
  <text x="44" y="608" fill="#60A5FA" font-size="13" font-weight="900">💡 4 NGUYÊN TẮC BẤT BIẾN CỦA LUỒNG KIỂM THỬ TÁC TỬ:</text>
  <text x="44" y="636" fill="#F1F5F9" font-size="11.5">
    1. Pre-Flight luôn kiểm tra Cache &amp; Góc nhìn  •  2. Subagent 1 tuyệt đối CẤM tự ý sinh test case sớm  •  3. Tester giữ chốt chặn phê duyệt tại Gate 1 &amp; Gate 2  •  4. Đổi Requirement là Rollback tức thì
  </text>
</svg>"""


# =============================================================================
# 2. FLOWCHART STAGE 0 (Slide 4: Pre-Flight Flowchart)
# =============================================================================
svg_stage0 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 680" width="1600" height="680" style="background:#FFFFFF; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
{COMMON_DEFS}

  <!-- Header Banner -->
  <rect x="20" y="16" width="1560" height="64" rx="10" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.8" filter="url(#shadow)"/>
  <text x="44" y="44" fill="#1E40AF" font-size="16" font-weight="900">🔍 SƠ ĐỒ LUỒNG CHẶNG 0: PRE-FLIGHT, QUẢN TRỊ GÓC NHÌN &amp; XÁC THỰC CACHE</text>
  <text x="44" y="66" fill="#2563EB" font-size="12" font-weight="600">Khởi tạo phiên làm việc chuẩn xác • Ghi nhớ vai trò người dùng • Kiểm tra modifiedTime Drive và cơ chế Offline Fallback</text>

  <!-- Left: Start & Input -->
  <rect x="40" y="270" width="160" height="65" rx="32" fill="#F1F5F9" stroke="#64748B" stroke-width="2" filter="url(#shadow)"/>
  <text x="120" y="298" fill="#1E293B" font-size="12.5" font-weight="800" text-anchor="middle">📄 NHẬN INPUT</text>
  <text x="120" y="318" fill="#64748B" font-size="10.5" text-anchor="middle">Spec / User Story / API</text>

  <path d="M 200 302 L 250 302" stroke="#2563EB" stroke-width="2.5" fill="none" marker-end="url(#arr-blue)"/>

  <!-- Preference Decision Flow -->
  <g transform="translate(255, 232)">
    <rect x="0" y="0" width="220" height="140" rx="10" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2" filter="url(#shadow)"/>
    <text x="110" y="28" fill="#1E40AF" font-size="12" font-weight="900" text-anchor="middle">1. Đọc user_preferences.json</text>
    <text x="110" y="48" fill="#64748B" font-size="10" text-anchor="middle">Tự ghi nhớ góc nhìn đã lưu</text>
    
    <rect x="15" y="60" width="190" height="22" rx="4" fill="#DBEAFE"/>
    <text x="110" y="75" fill="#1D4ED8" font-size="9.5" font-weight="800" text-anchor="middle">Business: Ngôn ngữ BA đời sống</text>
    
    <rect x="15" y="86" width="190" height="22" rx="4" fill="#EDE9FE"/>
    <text x="110" y="101" fill="#6D28D9" font-size="9.5" font-weight="800" text-anchor="middle">Technical: Race condition, Lock, JWT</text>
    
    <rect x="15" y="112" width="190" height="22" rx="4" fill="#E0F2FE"/>
    <text x="110" y="127" fill="#0369A1" font-size="9.5" font-weight="800" text-anchor="middle">Hybrid: Song song BA &amp; SDET</text>
  </g>

  <path d="M 475 302 L 530 302" stroke="#2563EB" stroke-width="2.5" fill="none" marker-end="url(#arr-blue)"/>

  <!-- Diamond: Cache Validation -->
  <g transform="translate(535, 212)">
    <polygon points="100,0 200,90 100,180 0,90" fill="#F0FDF4" stroke="#16A34A" stroke-width="2.5" filter="url(#shadow)"/>
    <text x="100" y="68" fill="#15803D" font-size="10.5" font-weight="900" text-anchor="middle">2. SO SÁNH CACHE</text>
    <text x="100" y="88" fill="#166534" font-size="11.5" font-weight="800" text-anchor="middle">modifiedTime Drive vs</text>
    <text x="100" y="106" fill="#166534" font-size="11" font-weight="700" text-anchor="middle">.sync_metadata.json</text>
  </g>

  <!-- Branch 1: Match (Up) -->
  <path d="M 635 212 L 635 155 L 775 155" stroke="#16A34A" stroke-width="2.5" fill="none" marker-end="url(#arr-green)"/>
  <rect x="645" y="140" width="110" height="22" rx="4" fill="#DCFCE7"/>
  <text x="700" y="155" fill="#15803D" font-size="10" font-weight="900" text-anchor="middle">✔ Trùng khớp</text>

  <g transform="translate(780, 115)">
    <rect x="0" y="0" width="280" height="80" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.8" filter="url(#shadow)"/>
    <text x="15" y="28" fill="#15803D" font-size="12" font-weight="900">Đọc trực tiếp local bug_repository.json</text>
    <text x="15" y="48" fill="#334155" font-size="10.5">• Tốc độ phản hồi cực nhanh (&lt; 50ms)</text>
    <text x="15" y="66" fill="#334155" font-size="10.5">• Loại bỏ hoàn toàn độ trễ gọi API mạng</text>
  </g>

  <!-- Branch 2: Differs (Middle) -->
  <path d="M 735 302 L 775 302" stroke="#2563EB" stroke-width="2.5" fill="none" marker-end="url(#arr-blue)"/>
  <rect x="645" y="292" width="115" height="22" rx="4" fill="#DBEAFE"/>
  <text x="702" y="307" fill="#1D4ED8" font-size="10" font-weight="900" text-anchor="middle">🔄 Có thay đổi</text>

  <g transform="translate(780, 262)">
    <rect x="0" y="0" width="280" height="80" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.8" filter="url(#shadow)"/>
    <text x="15" y="28" fill="#1E40AF" font-size="12" font-weight="900">Kéo dữ liệu mới từ Google Drive</text>
    <text x="15" y="48" fill="#334155" font-size="10.5">• Gọi MCP search_drive_files lấy tệp mới</text>
    <text x="15" y="66" fill="#334155" font-size="10.5">• Ghi đè cập nhật local data/ và sync metadata</text>
  </g>

  <!-- Branch 3: Offline / MCP Error (Down) -->
  <path d="M 635 392 L 635 450 L 775 450" stroke="#DC2626" stroke-width="2.5" fill="none" marker-end="url(#arr-red)"/>
  <rect x="645" y="438" width="115" height="22" rx="4" fill="#FEE2E2"/>
  <text x="702" y="453" fill="#991B1B" font-size="10" font-weight="900" text-anchor="middle">⚠️ Mất mạng / Lỗi</text>

  <g transform="translate(780, 410)">
    <rect x="0" y="0" width="280" height="80" rx="8" fill="#FFF1F2" stroke="#E11D48" stroke-width="1.8" filter="url(#shadow)"/>
    <text x="15" y="28" fill="#BE123C" font-size="12" font-weight="900">Kích hoạt Offline Fallback</text>
    <text x="15" y="48" fill="#4C0519" font-size="10.5">• Tự động đọc dữ liệu local hiện có</text>
    <text x="15" y="66" fill="#4C0519" font-size="10.5">• Phát cảnh báo màu cam cho Tester trên UI</text>
  </g>

  <!-- Converge Arrows to Ground Truth -->
  <path d="M 1060 155 L 1120 155 L 1120 280" stroke="#16A34A" stroke-width="2" fill="none"/>
  <path d="M 1060 302 L 1140 302" stroke="#2563EB" stroke-width="2" fill="none"/>
  <path d="M 1060 450 L 1120 450 L 1120 324" stroke="#DC2626" stroke-width="2" fill="none"/>
  <path d="M 1120 302 L 1150 302" stroke="#16A34A" stroke-width="2.5" fill="none" marker-end="url(#arr-green)"/>

  <!-- Step 3: Ground Truth Box -->
  <g transform="translate(1155, 222)">
    <rect x="0" y="0" width="230" height="160" rx="10" fill="#F0FDFA" stroke="#0D9488" stroke-width="2" filter="url(#shadow)"/>
    <rect x="15" y="12" width="200" height="24" rx="4" fill="#CCFBF1"/>
    <text x="115" y="28" fill="#0F766E" font-size="11" font-weight="900" text-anchor="middle">3. NẠP GROUND TRUTH</text>
    <text x="15" y="62" fill="#1E293B" font-size="12" font-weight="800">10 Bugs Production Chuẩn Hóa</text>
    <text x="15" y="84" fill="#0F766E" font-size="10.5">• BUG-001: Race redis counter</text>
    <text x="15" y="102" fill="#0F766E" font-size="10.5">• BUG-004: Bán âm tồn kho</text>
    <text x="15" y="120" fill="#0F766E" font-size="10.5">• BUG-008: Voucher replay</text>
    <text x="15" y="142" fill="#15803D" font-size="10.5" font-weight="800">🎯 Mỏ neo chống ảo giác cho AI</text>
  </g>

  <!-- Output Pill to Phase 1 -->
  <path d="M 1385 302 L 1435 302" stroke="#7C3AED" stroke-width="3" fill="none" marker-end="url(#arr-purple)"/>
  <rect x="1440" y="270" width="130" height="65" rx="32" fill="#FAF5FF" stroke="#7C3AED" stroke-width="2" filter="url(#shadow)"/>
  <text x="1505" y="298" fill="#6D28D9" font-size="12" font-weight="900" text-anchor="middle">BÀN GIAO</text>
  <text x="1505" y="318" fill="#7C3AED" font-size="10.5" text-anchor="middle">Sang Pha 1</text>

  <!-- Bottom Guidelines -->
  <rect x="20" y="580" width="1560" height="80" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5"/>
  <text x="44" y="612" fill="#60A5FA" font-size="13" font-weight="900">💡 ĐIỂM CỐT LÕI CỦA CHẶNG 0:</text>
  <text x="44" y="638" fill="#F1F5F9" font-size="11.5">
    • Tự động ghi nhớ vai trò người dùng (không hỏi lại)  •  Bảo toàn tính đồng nhất giữa Local và Cloud  •  Không bao giờ sụp đổ luồng khi mất kết nối mạng.
  </text>
</svg>"""


# =============================================================================
# 3. FLOWCHART PHASE 1 (Slide 5: req-risk-analyst Flowchart)
# =============================================================================
svg_phase1 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 680" width="1600" height="680" style="background:#FFFFFF; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
{COMMON_DEFS}

  <!-- Header Banner -->
  <rect x="20" y="16" width="1560" height="64" rx="10" fill="#FAF5FF" stroke="#7C3AED" stroke-width="1.8" filter="url(#shadow)"/>
  <text x="44" y="44" fill="#6D28D9" font-size="16" font-weight="900">🟣 SƠ ĐỒ LUỒNG PHA 1: BÓC TÁCH YÊU CẦU &amp; QUÉT 5 RỦI RO KỸ THUẬT (req-risk-analyst)</text>
  <text x="44" y="66" fill="#7C3AED" font-size="12" font-weight="600">Phân tích tĩnh toàn diện • Soạn câu hỏi phản biện BA/PO • Tham chiếu 10 Bugs lịch sử • Ràng buộc cứng cấm sinh test case</text>

  <!-- Start Pill -->
  <rect x="30" y="270" width="150" height="65" rx="32" fill="#F1F5F9" stroke="#64748B" stroke-width="2" filter="url(#shadow)"/>
  <text x="105" y="298" fill="#1E293B" font-size="12" font-weight="800" text-anchor="middle">GÓI DỮ LIỆU</text>
  <text x="105" y="318" fill="#64748B" font-size="10.5" text-anchor="middle">Từ Chặng 0</text>

  <path d="M 180 302 L 230 302" stroke="#7C3AED" stroke-width="2.5" fill="none" marker-end="url(#arr-purple)"/>

  <!-- Step 1: 4 Core Elements -->
  <g transform="translate(235, 212)">
    <rect x="0" y="0" width="240" height="180" rx="10" fill="#FAF5FF" stroke="#7C3AED" stroke-width="2" filter="url(#shadow)"/>
    <rect x="15" y="12" width="210" height="24" rx="4" fill="#EDE9FE"/>
    <text x="120" y="28" fill="#6D28D9" font-size="11" font-weight="900" text-anchor="middle">1. BÓC TÁCH 4 THÀNH TỐ</text>
    
    <text x="18" y="60" fill="#1E293B" font-size="11" font-weight="800">⚙️ Core Business Rules</text>
    <text x="24" y="76" fill="#64748B" font-size="10">Điều kiện kích hoạt, logic nghiệp vụ</text>
    
    <text x="18" y="98" fill="#1E293B" font-size="11" font-weight="800">📏 Boundary Limits</text>
    <text x="24" y="114" fill="#64748B" font-size="10">Biên số liệu, TTL token, giới hạn số dư</text>
    
    <text x="18" y="136" fill="#1E293B" font-size="11" font-weight="800">⚠️ Exceptions &amp; Flow</text>
    <text x="24" y="152" fill="#64748B" font-size="10">Xử lý lỗi mạng, timeout, luồng người dùng</text>
  </g>

  <path d="M 475 302 L 530 302" stroke="#7C3AED" stroke-width="2.5" fill="none" marker-end="url(#arr-purple)"/>

  <!-- Diamond: Missing requirements / ambiguities? -->
  <g transform="translate(535, 212)">
    <polygon points="100,0 200,90 100,180 0,90" fill="#FFF1F2" stroke="#E11D48" stroke-width="2.5" filter="url(#shadow)"/>
    <text x="100" y="68" fill="#991B1B" font-size="10.5" font-weight="900" text-anchor="middle">2. PHÁT HIỆN</text>
    <text x="100" y="88" fill="#BE123C" font-size="11.5" font-weight="800" text-anchor="middle">Kẽ hở tài liệu /</text>
    <text x="100" y="106" fill="#BE123C" font-size="11" font-weight="700" text-anchor="middle">Điểm mơ hồ?</text>
  </g>

  <!-- Branch: Yes (Top) -> Questions for BA -->
  <path d="M 635 212 L 635 155 L 775 155" stroke="#E11D48" stroke-width="2.5" fill="none" marker-end="url(#arr-red)"/>
  <rect x="645" y="140" width="115" height="22" rx="4" fill="#FEE2E2"/>
  <text x="702" y="155" fill="#991B1B" font-size="10" font-weight="900" text-anchor="middle">✔ Có điểm mờ</text>

  <g transform="translate(780, 115)">
    <rect x="0" y="0" width="280" height="80" rx="8" fill="#FFF1F2" stroke="#E11D48" stroke-width="1.8" filter="url(#shadow)"/>
    <text x="15" y="28" fill="#BE123C" font-size="12" font-weight="900">Soạn Bộ Câu Hỏi Phản Biện BA/PO</text>
    <text x="15" y="48" fill="#4C0519" font-size="10.5">• "Xử lý thế nào khi 2 user submit cùng lúc?"</text>
    <text x="15" y="66" fill="#4C0519" font-size="10.5">• "Khi thanh toán lỗi, voucher có rollback ngay?"</text>
  </g>

  <!-- Converge to Technical Risks Scan -->
  <path d="M 735 302 L 775 302" stroke="#7C3AED" stroke-width="2.5" fill="none" marker-end="url(#arr-purple)"/>
  <rect x="645" y="292" width="115" height="22" rx="4" fill="#EDE9FE"/>
  <text x="702" y="307" fill="#6D28D9" font-size="10" font-weight="900" text-anchor="middle">Spec đã rõ</text>

  <path d="M 1060 155 L 1110 155 L 1110 270" stroke="#E11D48" stroke-width="2" fill="none"/>

  <!-- Step 3: Scan 5 Technical Risks & Map Bugs -->
  <g transform="translate(780, 242)">
    <rect x="0" y="0" width="280" height="150" rx="10" fill="#FAF5FF" stroke="#7C3AED" stroke-width="2" filter="url(#shadow)"/>
    <rect x="15" y="12" width="250" height="24" rx="4" fill="#EDE9FE"/>
    <text x="140" y="28" fill="#6D28D9" font-size="11" font-weight="900" text-anchor="middle">3. QUÉT 5 RỦI RO &amp; MAP BUG</text>
    
    <text x="15" y="60" fill="#1E293B" font-size="10.5">• 1. Race Condition (Lost Update)</text>
    <text x="15" y="78" fill="#1E293B" font-size="10.5">• 2. Concurrency Deadlock</text>
    <text x="15" y="96" fill="#1E293B" font-size="10.5">• 3. JWT State Drift &amp; Revocation</text>
    <text x="15" y="114" fill="#1E293B" font-size="10.5">• 4. Clock Drift &amp; Distributed Lock</text>
    <text x="15" y="134" fill="#6D28D9" font-size="10.5" font-weight="800">🗂️ Map tương đồng: BUG-001, BUG-004...</text>
  </g>

  <!-- Hard Constraint Warning Box -->
  <path d="M 1060 317 L 1130 317" stroke="#DC2626" stroke-width="2.5" fill="none" marker-end="url(#arr-red)"/>

  <g transform="translate(1135, 232)">
    <rect x="0" y="0" width="235" height="170" rx="12" fill="#FEE2E2" stroke="#DC2626" stroke-width="2.5" filter="url(#shadow-gate)"/>
    <text x="117" y="38" font-size="28" text-anchor="middle">⛔🛑</text>
    <text x="117" y="68" fill="#991B1B" font-size="13" font-weight="900" text-anchor="middle">RÀNG BUỘC CỨNG (RULE 1)</text>
    
    <rect x="15" y="82" width="205" height="40" rx="6" fill="#FFFFFF" stroke="#F87171"/>
    <text x="117" y="98" fill="#7F1D1D" font-size="10.5" font-weight="900" text-anchor="middle">TUYỆT ĐỐI CẤM TỰ Ý</text>
    <text x="117" y="114" fill="#7F1D1D" font-size="10.5" font-weight="900" text-anchor="middle">SINH TEST CASE SỚM!</text>
    
    <text x="117" y="140" fill="#991B1B" font-size="10" text-anchor="middle">Bắt buộc ngưng chạy &amp; xuất báo cáo</text>
    <text x="117" y="156" fill="#991B1B" font-size="10" font-weight="800" text-anchor="middle">Chờ Tester phê duyệt tại Gate 1</text>
  </g>

  <!-- Output Pill to Gate 1 -->
  <path d="M 1370 317 L 1420 317" stroke="#DC2626" stroke-width="3" fill="none" marker-end="url(#arr-red)"/>
  <rect x="1425" y="285" width="145" height="65" rx="32" fill="#FFF1F2" stroke="#E11D48" stroke-width="2" filter="url(#shadow)"/>
  <text x="1497" y="313" fill="#BE123C" font-size="12" font-weight="900" text-anchor="middle">CHUYỂN SANG</text>
  <text x="1497" y="333" fill="#E11D48" font-size="10.5" font-weight="800" text-anchor="middle">Human Gate 1</text>

  <!-- Bottom Guidelines -->
  <rect x="20" y="580" width="1560" height="80" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5"/>
  <text x="44" y="612" fill="#60A5FA" font-size="13" font-weight="900">💡 GIÁ TRỊ CỐT LÕI CỦA PHA 1 (SHIFT-LEFT QA):</text>
  <text x="44" y="638" fill="#F1F5F9" font-size="11.5">
    • Phát hiện lỗi logic ngay khâu tài liệu thay vì đợi code xong  •  Buộc AI giải thích rõ kẽ hở bằng ngôn ngữ nghiệp vụ  •  Không sinh rác test case bừa bãi.
  </text>
</svg>"""


# =============================================================================
# 4. FLOWCHART GATES & ROLLBACK (Slide 6: Human Gates Flowchart)
# =============================================================================
svg_gates = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 680" width="1600" height="680" style="background:#FFFFFF; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
{COMMON_DEFS}

  <!-- Header Banner -->
  <rect x="20" y="16" width="1560" height="64" rx="10" fill="#FFF1F2" stroke="#E11D48" stroke-width="1.8" filter="url(#shadow)"/>
  <text x="44" y="44" fill="#BE123C" font-size="16" font-weight="900">🛑 SƠ ĐỒ LUỒNG ĐIỂM CHẶN: 2 HUMAN GATES &amp; CƠ CHẾ TỰ ĐỘNG ROLLBACK</text>
  <text x="44" y="66" fill="#E11D48" font-size="12" font-weight="600">Tester giữ toàn quyền phê duyệt • Kiểm soát 100% ảo giác • Tự động vô hiệu hóa và rollback khi Requirement thay đổi</text>

  <!-- Input from Phase 1 -->
  <rect x="40" y="270" width="160" height="65" rx="32" fill="#FAF5FF" stroke="#7C3AED" stroke-width="2" filter="url(#shadow)"/>
  <text x="120" y="298" fill="#6D28D9" font-size="12" font-weight="800" text-anchor="middle">BÁO CÁO PHA 1</text>
  <text x="120" y="318" fill="#7C3AED" font-size="10.5" text-anchor="middle">Rules, Q&amp;A, 5 Rủi ro</text>

  <path d="M 200 302 L 250 302" stroke="#E11D48" stroke-width="3" fill="none" marker-end="url(#arr-red)"/>

  <!-- Gate 1 Box & Diamond -->
  <g transform="translate(255, 212)">
    <polygon points="100,0 200,90 100,180 0,90" fill="#FFF1F2" stroke="#E11D48" stroke-width="2.8" filter="url(#shadow-gate)"/>
    <text x="100" y="65" fill="#BE123C" font-size="11" font-weight="900" text-anchor="middle">🛑 HUMAN GATE 1</text>
    <text x="100" y="85" fill="#E11D48" font-size="12.5" font-weight="900" text-anchor="middle">Tester Chốt</text>
    <text x="100" y="105" fill="#E11D48" font-size="12" font-weight="800" text-anchor="middle">Logic Yêu Cầu?</text>
  </g>

  <!-- Gate 1 Rejection -> Loop back to Phase 1 -->
  <path d="M 355 212 L 355 140 L 120 140 L 120 262" stroke="#DC2626" stroke-width="2.5" stroke-dasharray="6 3" fill="none" marker-end="url(#arr-red)"/>
  <rect x="180" y="125" width="145" height="24" rx="4" fill="#FEE2E2" stroke="#F87171"/>
  <text x="252" y="141" fill="#991B1B" font-size="10" font-weight="800" text-anchor="middle">❌ Yêu cầu sửa / Đổi spec</text>

  <!-- Gate 1 Approved -> Move to Phase 2 -->
  <path d="M 455 302 L 530 302" stroke="#16A34A" stroke-width="3" fill="none" marker-end="url(#arr-green)"/>
  <rect x="465" y="280" width="45" height="20" rx="4" fill="#DCFCE7"/>
  <text x="487" y="294" fill="#15803D" font-size="10.5" font-weight="900" text-anchor="middle">PASS</text>

  <!-- Phase 2 Processing Block -->
  <g transform="translate(535, 222)">
    <rect x="0" y="0" width="220" height="160" rx="10" fill="#F0FDFA" stroke="#0D9488" stroke-width="2" filter="url(#shadow)"/>
    <rect x="12" y="12" width="196" height="24" rx="4" fill="#CCFBF1"/>
    <text x="110" y="28" fill="#0F766E" font-size="10.5" font-weight="900" text-anchor="middle">TIẾN HÀNH PHA 2</text>
    <text x="15" y="60" fill="#1E293B" font-size="12" font-weight="800">test-automation-architect</text>
    <text x="15" y="82" fill="#0F766E" font-size="10.5">• Sinh 5 nhóm kịch bản kiểm thử</text>
    <text x="15" y="102" fill="#0F766E" font-size="10.5">• Tách bước độc lập (Disaggregate)</text>
    <text x="15" y="122" fill="#0F766E" font-size="10.5">• Verify 3 tầng: UI + API + DB</text>
    <text x="15" y="142" fill="#0F766E" font-size="10.5">• Gán trạng thái NOT_RUN</text>
  </g>

  <path d="M 755 302 L 830 302" stroke="#D97706" stroke-width="3" fill="none" marker-end="url(#arr-amber)"/>

  <!-- Gate 2 Box & Diamond -->
  <g transform="translate(835, 212)">
    <polygon points="100,0 200,90 100,180 0,90" fill="#FFFBEB" stroke="#D97706" stroke-width="2.8" filter="url(#shadow)"/>
    <text x="100" y="65" fill="#B45309" font-size="11" font-weight="900" text-anchor="middle">🛑 HUMAN GATE 2</text>
    <text x="100" y="85" fill="#D97706" font-size="12.5" font-weight="900" text-anchor="middle">Tester Nghiệm Thu</text>
    <text x="100" y="105" fill="#D97706" font-size="12" font-weight="800" text-anchor="middle">Đặc Tả Test Cases?</text>
  </g>

  <!-- Gate 2 Branch A: Minor Fix -> Back to Phase 2 -->
  <path d="M 935 212 L 935 140 L 645 140 L 645 214" stroke="#D97706" stroke-width="2.2" stroke-dasharray="5 3" fill="none" marker-end="url(#arr-amber)"/>
  <rect x="730" y="125" width="135" height="24" rx="4" fill="#FEF3C7" stroke="#FDE68A"/>
  <text x="797" y="141" fill="#B45309" font-size="10" font-weight="800" text-anchor="middle">⚠️ Cần bổ sung test case</text>

  <!-- Gate 2 Branch B: Major Requirement Change -> Rollback to Phase 1 -->
  <path d="M 935 392 L 935 480 L 120 480 L 120 342" stroke="#DC2626" stroke-width="3" stroke-dasharray="8 4" fill="none" marker-end="url(#arr-red)"/>
  <rect x="420" y="465" width="350" height="30" rx="6" fill="#FEF2F2" stroke="#DC2626" stroke-width="1.8"/>
  <text x="595" y="485" fill="#B91C1C" font-size="11.5" font-weight="900" text-anchor="middle">↩️ REQUIREMENT THAY ĐỔI: TỰ ĐỘNG ROLLBACK VỀ PHA 1</text>
  <text x="595" y="515" fill="#DC2626" font-size="10.5" font-weight="700" text-anchor="middle">(Vô hiệu hóa toàn bộ Test Cases cũ • Phân tích lại từ đầu theo phạm vi mới)</text>

  <!-- Gate 2 Approved -> Phase 3 Sync -->
  <path d="M 1035 302 L 1110 302" stroke="#16A34A" stroke-width="3" fill="none" marker-end="url(#arr-green)"/>
  <rect x="1045" y="280" width="45" height="20" rx="4" fill="#DCFCE7"/>
  <text x="1067" y="294" fill="#15803D" font-size="10.5" font-weight="900" text-anchor="middle">PASS</text>

  <!-- Destination Block: Phase 3 -->
  <g transform="translate(1115, 222)">
    <rect x="0" y="0" width="230" height="160" rx="10" fill="#F0FDF4" stroke="#16A34A" stroke-width="2" filter="url(#shadow)"/>
    <rect x="15" y="12" width="200" height="24" rx="4" fill="#DCFCE7"/>
    <text x="115" y="28" fill="#15803D" font-size="11" font-weight="900" text-anchor="middle">MỞ CỔNG PHA 3</text>
    <text x="15" y="60" fill="#1E293B" font-size="12" font-weight="800">Lưu Trữ &amp; Đồng Bộ</text>
    <text x="15" y="82" fill="#15803D" font-size="10.5">• Local-First Append-Only</text>
    <text x="15" y="102" fill="#15803D" font-size="10.5">• Push nối tiếp lên Google Sheets</text>
    <text x="15" y="122" fill="#15803D" font-size="10.5">• Cập nhật cache metadata</text>
    <text x="15" y="142" fill="#15803D" font-size="10.5" font-weight="800">🎉 Bàn giao test suite sẵn sàng chạy</text>
  </g>

  <!-- Finish Pill -->
  <path d="M 1345 302 L 1395 302" stroke="#16A34A" stroke-width="3" fill="none" marker-end="url(#arr-green)"/>
  <rect x="1400" y="270" width="160" height="65" rx="32" fill="#DCFCE7" stroke="#16A34A" stroke-width="2" filter="url(#shadow)"/>
  <text x="1480" y="298" fill="#166534" font-size="12" font-weight="900" text-anchor="middle">AN TOÀN 100%</text>
  <text x="1480" y="318" fill="#15803D" font-size="10.5" text-anchor="middle">0 Lỗi phân kỳ trạng thái</text>

  <!-- Bottom Guidelines -->
  <rect x="20" y="580" width="1560" height="80" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5"/>
  <text x="44" y="612" fill="#60A5FA" font-size="13" font-weight="900">💡 TRIẾT LÝ HUMAN-IN-THE-LOOP:</text>
  <text x="44" y="638" fill="#F1F5F9" font-size="11.5">
    • AI chỉ là máy đề xuất thông minh — Tester mới là người ra quyết định  •  Cơ chế Rollback ngăn chặn tuyệt đối tình trạng rác test case tồn đọng khi dự án thay đổi spec.
  </text>
</svg>"""


# =============================================================================
# 5. FLOWCHART PHASE 2 (Slide 7: test-automation-architect Flowchart)
# =============================================================================
svg_phase2 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 680" width="1600" height="680" style="background:#FFFFFF; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
{COMMON_DEFS}

  <!-- Header Banner -->
  <rect x="20" y="16" width="1560" height="64" rx="10" fill="#F0FDFA" stroke="#0D9488" stroke-width="1.8" filter="url(#shadow)"/>
  <text x="44" y="44" fill="#0F766E" font-size="16" font-weight="900">🟢 SƠ ĐỒ LUỒNG PHA 2: THIẾT KẾ TEST AUTOMATION &amp; KIỂM CHỨNG SÂU 3 TẦNG</text>
  <text x="44" y="66" fill="#0D9488" font-size="12" font-weight="600">Áp dụng test-design-matrix.md • Tách bước độc lập (Disaggregation) • Kiểm chứng sâu UI + API Body + DB &amp; Event</text>

  <!-- Input Pill -->
  <rect x="30" y="270" width="150" height="65" rx="32" fill="#DCFCE7" stroke="#16A34A" stroke-width="2" filter="url(#shadow)"/>
  <text x="105" y="298" fill="#166534" font-size="12" font-weight="800" text-anchor="middle">APPROVED</text>
  <text x="105" y="318" fill="#15803D" font-size="10.5" text-anchor="middle">Từ Gate 1</text>

  <path d="M 180 302 L 230 302" stroke="#0D9488" stroke-width="2.5" fill="none" marker-end="url(#arr-teal)"/>

  <!-- Step 1: Step Disaggregation -->
  <g transform="translate(235, 212)">
    <rect x="0" y="0" width="250" height="180" rx="10" fill="#F0FDFA" stroke="#0D9488" stroke-width="2" filter="url(#shadow)"/>
    <rect x="15" y="12" width="220" height="24" rx="4" fill="#CCFBF1"/>
    <text x="125" y="28" fill="#0F766E" font-size="11" font-weight="900" text-anchor="middle">1. TÁCH BƯỚC ĐỘC LẬP</text>
    
    <text x="18" y="60" fill="#1E293B" font-size="11" font-weight="800">❌ Không gom cụm bước:</text>
    <text x="24" y="78" fill="#64748B" font-size="10.5">Cấm dồn chọn số lượng + checkout</text>
    
    <text x="18" y="104" fill="#15803D" font-size="11" font-weight="800">✔ Tách bạch 2 giai đoạn:</text>
    <text x="24" y="122" fill="#334155" font-size="10.5">• Bước 1: Nhập liệu / Chuẩn bị</text>
    <text x="24" y="138" fill="#334155" font-size="10.5">• Bước 2: Kích hoạt / Gửi request</text>
    <text x="24" y="156" fill="#0F766E" font-size="10" font-weight="800">👉 Tiền đề chuyển vào Pre-conditions</text>
  </g>

  <path d="M 485 302 L 535 302" stroke="#0D9488" stroke-width="2.5" fill="none" marker-end="url(#arr-teal)"/>

  <!-- Step 2: 5 Scenario Groups Matrix -->
  <g transform="translate(540, 192)">
    <rect x="0" y="0" width="280" height="220" rx="10" fill="#FFFFFF" stroke="#0D9488" stroke-width="2" filter="url(#shadow)"/>
    <rect x="15" y="12" width="250" height="24" rx="4" fill="#CCFBF1"/>
    <text x="140" y="28" fill="#0F766E" font-size="11" font-weight="900" text-anchor="middle">2. MA TRẬN 5 NHÓM TEST</text>
    
    <rect x="15" y="46" width="250" height="28" rx="4" fill="#F0FDF4" stroke="#86EFAC"/>
    <text x="25" y="64" fill="#15803D" font-size="10.5" font-weight="800">1. Happy Path: Luồng chuẩn nghiệp vụ</text>
    
    <rect x="15" y="80" width="250" height="28" rx="4" fill="#EFF6FF" stroke="#93C5FD"/>
    <text x="25" y="98" fill="#1D4ED8" font-size="10.5" font-weight="800">2. Boundary Limit: Giới hạn biên N=0, N=1</text>
    
    <rect x="15" y="114" width="250" height="28" rx="4" fill="#FFF1F2" stroke="#FECDD3"/>
    <text x="25" y="132" fill="#BE123C" font-size="10.5" font-weight="800">3. Negative Flow: Dữ liệu sai, injection</text>
    
    <rect x="15" y="148" width="250" height="28" rx="4" fill="#FAF5FF" stroke="#D8B4FE"/>
    <text x="25" y="166" fill="#6D28D9" font-size="10.5" font-weight="800">4. Concurrency: Tranh mua &lt;= 50ms</text>
    
    <rect x="15" y="182" width="250" height="28" rx="4" fill="#FEF3C7" stroke="#FDE68A"/>
    <text x="25" y="200" fill="#B45309" font-size="10.5" font-weight="800">5. State Conflict &amp; Disaster Recovery</text>
  </g>

  <path d="M 820 302 L 870 302" stroke="#0D9488" stroke-width="2.5" fill="none" marker-end="url(#arr-teal)"/>

  <!-- Step 3: 3-Tier Deep Verification Stack -->
  <g transform="translate(875, 192)">
    <rect x="0" y="0" width="310" height="220" rx="10" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2" filter="url(#shadow)"/>
    <rect x="15" y="12" width="280" height="24" rx="4" fill="#DBEAFE"/>
    <text x="155" y="28" fill="#1E40AF" font-size="11" font-weight="900" text-anchor="middle">3. KIỂM CHỨNG SÂU 3 TẦNG</text>
    
    <!-- Tier 1 -->
    <rect x="15" y="46" width="280" height="46" rx="4" fill="#FFFFFF" stroke="#BFDBFE"/>
    <text x="25" y="64" fill="#1D4ED8" font-size="10.5" font-weight="800">🖥️ Tầng 1: UI / Client Toast &amp; Alert</text>
    <text x="25" y="80" fill="#64748B" font-size="9.5">Toast alert, border đỏ #EF4444, order_id hiển thị</text>
    
    <!-- Tier 2 -->
    <rect x="15" y="98" width="280" height="50" rx="4" fill="#FFFFFF" stroke="#99F6E4"/>
    <text x="25" y="116" fill="#0F766E" font-size="10.5" font-weight="800">⚙️ Tầng 2: API Gateway Response Body</text>
    <text x="25" y="132" fill="#64748B" font-size="9.5">HTTP 423 | JSON: {{&quot;error&quot;: &quot;ERR_LOCKED&quot;, &quot;retry&quot;: 300}}</text>
    
    <!-- Tier 3 -->
    <rect x="15" y="154" width="280" height="50" rx="4" fill="#FFFFFF" stroke="#DDD6FE"/>
    <text x="25" y="172" fill="#5B21B6" font-size="10.5" font-weight="800">🗄️ Tầng 3: Database &amp; Event Broker</text>
    <text x="25" y="188" fill="#64748B" font-size="9.5">users.is_locked = TRUE | Event: AccountLockedEvent</text>
  </g>

  <path d="M 1185 302 L 1235 302" stroke="#0D9488" stroke-width="2.5" fill="none" marker-end="url(#arr-teal)"/>

  <!-- Step 4: Output Spec Schema -->
  <g transform="translate(1240, 212)">
    <rect x="0" y="0" width="200" height="180" rx="10" fill="#F0FDF4" stroke="#16A34A" stroke-width="2" filter="url(#shadow)"/>
    <rect x="15" y="12" width="170" height="24" rx="4" fill="#DCFCE7"/>
    <text x="100" y="28" fill="#15803D" font-size="10.5" font-weight="900" text-anchor="middle">4. GÁN THUỘC TÍNH</text>
    <text x="15" y="60" fill="#1E293B" font-size="11" font-weight="800">• Requirement ID:</text>
    <text x="25" y="76" fill="#64748B" font-size="10">Foreign key truy vết</text>
    <text x="15" y="96" fill="#1E293B" font-size="11" font-weight="800">• Priority Matrix:</text>
    <text x="25" y="112" fill="#64748B" font-size="10">P1 Critical, P2 High, P3</text>
    <text x="15" y="132" fill="#15803D" font-size="11" font-weight="900">• Status Mặc Định:</text>
    <text x="25" y="148" fill="#15803D" font-size="11" font-weight="900">NOT_RUN</text>
    <text x="25" y="166" fill="#64748B" font-size="9.5">(Hỗ trợ PASS/FAIL/BLOCKED)</text>
  </g>

  <!-- Output Pill to Gate 2 -->
  <path d="M 1440 302 L 1480 302" stroke="#D97706" stroke-width="3" fill="none" marker-end="url(#arr-amber)"/>
  <rect x="1485" y="270" width="100" height="65" rx="32" fill="#FFFBEB" stroke="#D97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="1535" y="298" fill="#B45309" font-size="11.5" font-weight="900" text-anchor="middle">SANG</text>
  <text x="1535" y="318" fill="#D97706" font-size="11" font-weight="800" text-anchor="middle">Gate 2</text>

  <!-- Bottom Guidelines -->
  <rect x="20" y="580" width="1560" height="80" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5"/>
  <text x="44" y="612" fill="#60A5FA" font-size="13" font-weight="900">💡 XÓA BỎ HOÀN TOÀN TEST CASE HỜI HỢT "HTTP 200":</text>
  <text x="44" y="638" fill="#F1F5F9" font-size="11.5">
    • Kiểm chứng sâu 3 tầng loại trừ 100% bug ngầm ở DB  •  Tách bước độc lập giúp Playwright Automation code được ngay mà không cần sửa kịch bản.
  </text>
</svg>"""


# =============================================================================
# 6. FLOWCHART PHASE 3 (Slide 8: Workspace Sync Manager Flowchart)
# =============================================================================
svg_phase3 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 680" width="1600" height="680" style="background:#FFFFFF; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
{COMMON_DEFS}

  <!-- Header Banner -->
  <rect x="20" y="16" width="1560" height="64" rx="10" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.8" filter="url(#shadow)"/>
  <text x="44" y="44" fill="#15803D" font-size="16" font-weight="900">🟡 SƠ ĐỒ LUỒNG PHA 3: LOCAL-FIRST &amp; ĐỒNG BỘ GOOGLE WORKSPACE 2 CHIỀU</text>
  <text x="44" y="66" fill="#16A34A" font-size="12" font-weight="600">Bảo toàn 100% lịch sử (Append-Only) • Push dòng mới lên Google Sheets qua MCP • Cập nhật metadata hoàn tất</text>

  <!-- Input Pill -->
  <rect x="30" y="270" width="150" height="65" rx="32" fill="#FEF3C7" stroke="#D97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="105" y="298" fill="#B45309" font-size="12" font-weight="800" text-anchor="middle">NGHIỆM THU</text>
  <text x="105" y="318" fill="#92400E" font-size="10.5" text-anchor="middle">Từ Gate 2</text>

  <path d="M 180 302 L 230 302" stroke="#16A34A" stroke-width="2.5" fill="none" marker-end="url(#arr-green)"/>

  <!-- Step 1: Local-First Append-Only -->
  <g transform="translate(235, 192)">
    <rect x="0" y="0" width="320" height="220" rx="10" fill="#F0FDF4" stroke="#16A34A" stroke-width="2" filter="url(#shadow)"/>
    <rect x="15" y="12" width="290" height="24" rx="4" fill="#DCFCE7"/>
    <text x="160" y="28" fill="#15803D" font-size="11" font-weight="900" text-anchor="middle">BƯỚC 1: LOCAL-FIRST APPEND-ONLY</text>
    
    <text x="18" y="60" fill="#1E293B" font-size="11.5" font-weight="800">💾 Nạp mảng dữ liệu local hiện có:</text>
    <text x="24" y="78" fill="#334155" font-size="10.5">• data/requirements_analysis.json</text>
    <text x="24" y="96" fill="#334155" font-size="10.5">• data/test_cases_specification.json</text>
    
    <rect x="15" y="112" width="290" height="42" rx="4" fill="#FEE2E2" stroke="#F87171"/>
    <text x="160" y="128" fill="#991B1B" font-size="10" font-weight="900" text-anchor="middle">🔒 RÀNG BUỘC: KHÔNG XÓA / RESET</text>
    <text x="160" y="144" fill="#7F1D1D" font-size="9.5" text-anchor="middle">Bảo toàn 100% lịch sử các phiên trước đó</text>
    
    <text x="18" y="174" fill="#15803D" font-size="11" font-weight="800">➕ Append bản ghi mới:</text>
    <text x="24" y="192" fill="#334155" font-size="10">Ghi nối tiếp requirement_id &amp; test cases mới</text>
  </g>

  <path d="M 555 302 L 610 302" stroke="#16A34A" stroke-width="2.5" fill="none" marker-end="url(#arr-green)"/>

  <!-- Step 2: Push Google Sheets via MCP -->
  <g transform="translate(615, 182)">
    <rect x="0" y="0" width="370" height="240" rx="10" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2" filter="url(#shadow)"/>
    <rect x="15" y="12" width="340" height="24" rx="4" fill="#DBEAFE"/>
    <text x="185" y="28" fill="#1E40AF" font-size="11" font-weight="900" text-anchor="middle">BƯỚC 2: PUSH GOOGLE SHEETS QUA MCP</text>
    
    <text x="18" y="60" fill="#1E293B" font-size="11.5" font-weight="800">📊 Gọi tool modify_sheet_values (Append Rows):</text>
    <text x="24" y="78" fill="#334155" font-size="10.5">• Nối tiếp vào Tab Requirements_Analysis</text>
    <text x="24" y="96" fill="#334155" font-size="10.5">• Nối tiếp vào Tab Test_Cases_Specification (10 cột)</text>
    
    <rect x="15" y="110" width="340" height="54" rx="4" fill="#FFFFFF" stroke="#BFDBFE"/>
    <text x="25" y="128" fill="#0958D9" font-size="10.5" font-weight="800">🎨 Visual Header Ant Design Blue #1677FF</text>
    <text x="25" y="144" fill="#64748B" font-size="9.5">Chữ trắng in đậm, freeze dòng 1, căn giữa, pixelSize 120-500px</text>
    <text x="25" y="158" fill="#64748B" font-size="9.5">Viền nhạt #CBD5E1, tự động xuống dòng toàn ô (WRAP)</text>
    
    <rect x="15" y="172" width="340" height="42" rx="4" fill="#FFFFFF" stroke="#86EFAC"/>
    <text x="25" y="190" fill="#15803D" font-size="10.5" font-weight="800">🎯 Dropdown Menu &amp; Conditional Formatting</text>
    <text x="25" y="206" fill="#334155" font-size="9.5">Status: PASS (Xanh) | FAIL (Đỏ) | BLOCKED (Cam) | NOT_RUN (Xám)</text>
  </g>

  <path d="M 985 302 L 1040 302" stroke="#16A34A" stroke-width="2.5" fill="none" marker-end="url(#arr-green)"/>

  <!-- Step 3: Refresh Metadata -->
  <g transform="translate(1045, 212)">
    <rect x="0" y="0" width="280" height="180" rx="10" fill="#F0FDFA" stroke="#0D9488" stroke-width="2" filter="url(#shadow)"/>
    <rect x="15" y="12" width="250" height="24" rx="4" fill="#CCFBF1"/>
    <text x="140" y="28" fill="#0F766E" font-size="11" font-weight="900" text-anchor="middle">BƯỚC 3: CẬP NHẬT METADATA</text>
    
    <text x="18" y="60" fill="#1E293B" font-size="11.5" font-weight="800">🔄 Làm mới .sync_metadata.json:</text>
    <text x="24" y="80" fill="#334155" font-size="10.5">• Lấy modifiedTime mới nhất từ Drive</text>
    <text x="24" y="98" fill="#334155" font-size="10.5">• Ghi nhận mốc thời gian last_synced_at</text>
    
    <text x="18" y="128" fill="#0F766E" font-size="11" font-weight="800">⚡ Sẵn sàng cho phiên làm việc sau:</text>
    <text x="24" y="146" fill="#64748B" font-size="10">Nhận diện cache trùng khớp tức thời (&lt;50ms)</text>
    <text x="24" y="164" fill="#0F766E" font-size="9.5" font-weight="800">✔ Không cần kéo lại dữ liệu từ mạng</text>
  </g>

  <!-- Finish Pill -->
  <path d="M 1325 302 L 1380 302" stroke="#16A34A" stroke-width="3" fill="none" marker-end="url(#arr-green)"/>
  <rect x="1385" y="260" width="180" height="85" rx="42" fill="#DCFCE7" stroke="#16A34A" stroke-width="2.5" filter="url(#shadow)"/>
  <text x="1475" y="296" fill="#166534" font-size="13" font-weight="900" text-anchor="middle">🎉 HOÀN TẤT</text>
  <text x="1475" y="316" fill="#15803D" font-size="11" font-weight="800" text-anchor="middle">ĐỒNG BỘ 100%</text>
  <text x="1475" y="332" fill="#166534" font-size="9.5" text-anchor="middle">Bàn giao Tester &amp; Dev</text>

  <!-- Bottom Guidelines -->
  <rect x="20" y="580" width="1560" height="80" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5"/>
  <text x="44" y="612" fill="#60A5FA" font-size="13" font-weight="900">💡 NGUYÊN TẮC LƯU TRỮ TÍCH LŨY (HISTORICAL PRESERVATION):</text>
  <text x="44" y="638" fill="#F1F5F9" font-size="11.5">
    • Cả file cục bộ và Google Sheets đều là kho lưu trữ lịch sử xuyên suốt  •  Tuyệt đối không clear/reset bảng  •  Đảm bảo khả năng truy vết 100% các vòng release.
  </text>
</svg>"""

DIAGRAMS = [
    ("flowchart_overview.svg", "flowchart_overview.png", svg_overview),
    ("flowchart_stage0.svg", "flowchart_stage0.png", svg_stage0),
    ("flowchart_phase1.svg", "flowchart_phase1.png", svg_phase1),
    ("flowchart_gates.svg", "flowchart_gates.png", svg_gates),
    ("flowchart_phase2.svg", "flowchart_phase2.png", svg_phase2),
    ("flowchart_phase3.svg", "flowchart_phase3.png", svg_phase3),
]

current_dir = os.path.dirname(os.path.abspath(__file__))

for svg_name, png_name, content in DIAGRAMS:
    svg_path = os.path.join(current_dir, svg_name)
    png_path = os.path.join(current_dir, png_name)
    
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Wrote {svg_path}")
    
    cmd = [
        "/usr/bin/google-chrome",
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--screenshot={png_path}",
        "--window-size=1600,680",
        svg_path
    ]
    subprocess.run(cmd, check=True)
    print(f"Rendered {png_path}")

print("All 6 flowchart diagrams successfully generated and rendered!")
