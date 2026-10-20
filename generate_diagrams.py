import os

def create_html_wrapper(svg_content, title, width=1560, height=1150):
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #f1f5f9;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 30px;
    }}
    .diagram-card {{
      background: #ffffff;
      border-radius: 20px;
      box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
      border: 1px solid #cbd5e1;
      padding: 24px 28px 32px 28px;
      display: inline-block;
    }}
    .header {{
      margin-bottom: 20px;
      border-bottom: 2px solid #e2e8f0;
      padding-bottom: 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .title {{
      font-size: 22px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.3px;
    }}
    .badge {{
      background: #2563eb;
      color: white;
      font-size: 13px;
      font-weight: 700;
      padding: 6px 16px;
      border-radius: 9999px;
      letter-spacing: 0.5px;
    }}
  </style>
</head>
<body>
  <div class="diagram-card">
    <div class="header">
      <div class="title">{title}</div>
      <div class="badge">HỆ CƠ SỞ DỮ LIỆU • ERD MODEL</div>
    </div>
    {svg_content}
  </div>
</body>
</html>
"""

# Diagram 1: Step 4 Initial ERD (Flawless coordinates)
svg_step4 = """<svg width="1440" height="960" viewBox="0 0 1440 960" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border-radius: 12px;">
  <defs>
    <filter id="shadow" x="-8%" y="-8%" width="120%" height="120%">
      <feDropShadow dx="2" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
    <linearGradient id="entGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e40af"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>
    <linearGradient id="entGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f766e"/>
      <stop offset="100%" stop-color="#14b8a6"/>
    </linearGradient>
    <linearGradient id="relGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#b45309"/>
      <stop offset="100%" stop-color="#f59e0b"/>
    </linearGradient>
    <linearGradient id="relGradGiao" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c2410c"/>
      <stop offset="100%" stop-color="#f97316"/>
    </linearGradient>
  </defs>

  <style>
    .line { stroke: #475569; stroke-width: 2.5; fill: none; }
    .cardinality { font-size: 14px; font-weight: 800; fill: #dc2626; }
    .attr-line { stroke: #94a3b8; stroke-width: 1.5; stroke-dasharray: 2 2; }
    .ent-title { font-size: 14px; font-weight: 800; fill: #ffffff; text-anchor: middle; }
    .rel-title { font-size: 13px; font-weight: 800; fill: #ffffff; text-anchor: middle; }
    .attr-text { font-size: 12px; fill: #1e293b; text-anchor: middle; }
    .pk-attr { text-decoration: underline; font-weight: 800; fill: #0f172a; }
  </style>

  <!-- Title Banner -->
  <rect x="20" y="15" width="1400" height="42" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" />
  <text x="720" y="42" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">
    BƯỚC 4: SƠ ĐỒ MÔ HÌNH THỰC THỂ LIÊN KẾT ERD BAN ĐẦU (CHƯA RÚT GỌN)
  </text>

  <!-- Connectors -->
  <!-- ĐƠN VỊ ĐH (180, 175) -> THUỘC (180, 275) -> NGƯỜI ĐẶT (180, 395) -->
  <line x1="180" y1="200" x2="180" y2="245" class="line" />
  <line x1="180" y1="305" x2="180" y2="370" class="line" />
  <text x="195" y="225" class="cardinality">1</text>
  <text x="195" y="345" class="cardinality">N</text>

  <!-- NGƯỜI ĐẶT (180, 395) -> ĐẶT (440, 395) -> HÀNG (720, 395) -->
  <line x1="260" y1="395" x2="380" y2="395" class="line" />
  <line x1="500" y1="395" x2="640" y2="395" class="line" />
  <text x="290" y="385" class="cardinality">1</text>
  <text x="610" y="385" class="cardinality">N</text>

  <!-- HÀNG (720, 395) -> GIAO (720, 640) -->
  <line x1="720" y1="420" x2="720" y2="590" class="line" />
  <text x="735" y="450" class="cardinality">N</text>

  <!-- NGƯỜI GIAO (180, 640) -> GIAO (720, 640) -->
  <line x1="260" y1="640" x2="650" y2="640" class="line" />
  <text x="290" y="630" class="cardinality">1</text>

  <!-- NƠI GIAO (440, 810) -> GIAO (720, 640) -->
  <line x1="440" y1="785" x2="680" y2="665" class="line" />
  <text x="460" y="760" class="cardinality">1</text>

  <!-- NGƯỜI NHẬN (1040, 640) -> GIAO (720, 640) -->
  <line x1="960" y1="640" x2="790" y2="640" class="line" />
  <text x="930" y="630" class="cardinality">1</text>

  <!-- ĐƠN VỊ KH (1240, 395) -> THUỘC (1240, 520) -> NGƯỜI NHẬN (1040, 640) -->
  <line x1="1240" y1="420" x2="1240" y2="490" class="line" />
  <line x1="1240" y1="550" x2="1100" y2="615" class="line" />
  <text x="1255" y="450" class="cardinality">1</text>
  <text x="1135" y="595" class="cardinality">N</text>

  <!-- ==================== ENTITIES & RELATIONSHIPS ==================== -->

  <!-- 1. ĐƠN VỊ ĐH -->
  <g filter="url(#shadow)">
    <rect x="100" y="150" width="160" height="50" rx="8" fill="url(#entGrad1)" />
    <text x="180" y="180" class="ent-title">ĐƠN VỊ ĐH</text>
  </g>
  <line x1="180" y1="150" x2="105" y2="95" class="attr-line" />
  <line x1="180" y1="150" x2="180" y2="85" class="attr-line" />
  <line x1="180" y1="150" x2="255" y2="95" class="attr-line" />
  <line x1="100" y1="175" x2="35" y2="175" class="attr-line" />

  <ellipse cx="105" cy="95" rx="42" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="105" y="99" class="attr-text pk-attr">Mã ĐV</text>

  <ellipse cx="180" cy="85" rx="42" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="180" y="89" class="attr-text">Tên ĐV</text>

  <ellipse cx="255" cy="95" rx="42" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="255" y="99" class="attr-text">Địa chỉ</text>

  <ellipse cx="35" cy="175" rx="42" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="35" y="179" class="attr-text">Điện thoại</text>

  <!-- 2. THUỘC (ĐV ĐH) -->
  <g filter="url(#shadow)">
    <polygon points="180,245 225,275 180,305 135,275" fill="url(#relGrad)" />
    <text x="180" y="279" class="rel-title">THUỘC</text>
  </g>

  <!-- 3. NGƯỜI ĐẶT -->
  <g filter="url(#shadow)">
    <rect x="100" y="370" width="160" height="50" rx="8" fill="url(#entGrad1)" />
    <text x="180" y="400" class="ent-title">NGƯỜI ĐẶT</text>
  </g>
  <line x1="100" y1="395" x2="35" y2="365" class="attr-line" />
  <line x1="100" y1="395" x2="35" y2="425" class="attr-line" />

  <ellipse cx="35" cy="365" rx="44" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="35" y="369" class="attr-text pk-attr">Mã số NĐ</text>

  <ellipse cx="35" cy="425" rx="44" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="35" y="429" class="attr-text">Họ tên NĐ</text>

  <!-- 4. ĐẶT -->
  <g filter="url(#shadow)">
    <polygon points="440,355 500,395 440,435 380,395" fill="url(#relGrad)" />
    <text x="440" y="399" class="rel-title">ĐẶT</text>
  </g>
  <line x1="440" y1="355" x2="370" y2="300" class="attr-line" />
  <line x1="440" y1="355" x2="440" y2="290" class="attr-line" />
  <line x1="440" y1="355" x2="510" y2="300" class="attr-line" />

  <ellipse cx="370" cy="300" rx="40" ry="16" fill="#fffbeb" stroke="#d97706" stroke-width="1.5" />
  <text x="370" y="304" class="attr-text" font-weight="700">Số ĐH</text>

  <ellipse cx="440" cy="290" rx="40" ry="16" fill="#fffbeb" stroke="#d97706" stroke-width="1.5" />
  <text x="440" y="294" class="attr-text" font-weight="700">Ngày đặt</text>

  <ellipse cx="510" cy="300" rx="40" ry="16" fill="#fffbeb" stroke="#d97706" stroke-width="1.5" />
  <text x="510" y="304" class="attr-text" font-weight="700">Số lượng</text>

  <!-- 5. HÀNG -->
  <g filter="url(#shadow)">
    <rect x="640" y="370" width="160" height="50" rx="8" fill="url(#entGrad2)" />
    <text x="720" y="400" class="ent-title">HÀNG</text>
  </g>
  <line x1="720" y1="370" x2="680" y2="310" class="attr-line" />
  <line x1="720" y1="370" x2="760" y2="310" class="attr-line" />
  <line x1="800" y1="385" x2="880" y2="365" class="attr-line" />
  <line x1="800" y1="405" x2="880" y2="420" class="attr-line" />

  <ellipse cx="680" cy="310" rx="42" ry="16" fill="#f0fdf4" stroke="#059669" stroke-width="1.5" />
  <text x="680" y="314" class="attr-text pk-attr">Mã hàng</text>

  <ellipse cx="760" cy="310" rx="42" ry="16" fill="#f0fdf4" stroke="#059669" stroke-width="1.5" />
  <text x="760" y="314" class="attr-text">Tên hàng</text>

  <ellipse cx="880" cy="365" rx="42" ry="16" fill="#f0fdf4" stroke="#059669" stroke-width="1.5" />
  <text x="880" y="369" class="attr-text">Đv tính</text>

  <ellipse cx="880" cy="420" rx="46" ry="16" fill="#f0fdf4" stroke="#059669" stroke-width="1.5" />
  <text x="880" y="424" class="attr-text">Mô tả hàng</text>

  <!-- 6. GIAO -->
  <g filter="url(#shadow)">
    <polygon points="720,590 790,640 720,690 650,640" fill="url(#relGradGiao)" />
    <text x="720" y="644" class="rel-title">GIAO</text>
  </g>
  <line x1="720" y1="690" x2="630" y2="760" class="attr-line" />
  <line x1="720" y1="690" x2="685" y2="785" class="attr-line" />
  <line x1="720" y1="690" x2="740" y2="785" class="attr-line" />
  <line x1="720" y1="690" x2="795" y2="760" class="attr-line" />
  <line x1="720" y1="690" x2="855" y2="725" class="attr-line" />

  <ellipse cx="630" cy="760" rx="40" ry="16" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5" />
  <text x="630" y="764" class="attr-text" font-weight="700">Số PG</text>

  <ellipse cx="685" cy="785" rx="40" ry="16" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5" />
  <text x="685" y="789" class="attr-text" font-weight="700">Ngày giao</text>

  <ellipse cx="740" cy="785" rx="40" ry="16" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5" />
  <text x="740" y="789" class="attr-text" font-weight="700">Số lượng</text>

  <ellipse cx="795" cy="760" rx="40" ry="16" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5" />
  <text x="795" y="764" class="attr-text" font-weight="700">Đơn giá</text>

  <ellipse cx="855" cy="725" rx="44" ry="16" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5" />
  <text x="855" y="729" class="attr-text" font-weight="700">Thành tiền</text>

  <!-- 7. NGƯỜI GIAO -->
  <g filter="url(#shadow)">
    <rect x="100" y="615" width="160" height="50" rx="8" fill="url(#entGrad1)" />
    <text x="180" y="645" class="ent-title">NGƯỜI GIAO</text>
  </g>
  <line x1="100" y1="640" x2="35" y2="610" class="attr-line" />
  <line x1="100" y1="640" x2="35" y2="670" class="attr-line" />

  <ellipse cx="35" cy="610" rx="44" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="35" y="614" class="attr-text pk-attr">Mã số NG</text>

  <ellipse cx="35" cy="670" rx="44" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="35" y="674" class="attr-text">Họ tên NG</text>

  <!-- 8. NƠI GIAO -->
  <g filter="url(#shadow)">
    <rect x="360" y="785" width="160" height="50" rx="8" fill="url(#entGrad1)" />
    <text x="440" y="815" class="ent-title">NƠI GIAO</text>
  </g>
  <line x1="440" y1="835" x2="380" y2="885" class="attr-line" />
  <line x1="440" y1="835" x2="500" y2="885" class="attr-line" />

  <ellipse cx="380" cy="885" rx="46" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="380" y="889" class="attr-text pk-attr">Mã số ĐĐG</text>

  <ellipse cx="500" cy="885" rx="46" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="500" y="889" class="attr-text">Tên nơi giao</text>

  <!-- 9. NGƯỜI NHẬN -->
  <g filter="url(#shadow)">
    <rect x="960" y="615" width="160" height="50" rx="8" fill="url(#entGrad1)" />
    <text x="1040" y="645" class="ent-title">NGƯỜI NHẬN</text>
  </g>
  <line x1="1040" y1="665" x2="1000" y2="720" class="attr-line" />
  <line x1="1040" y1="665" x2="1080" y2="720" class="attr-line" />

  <ellipse cx="1000" cy="720" rx="44" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="1000" y="724" class="attr-text pk-attr">Mã số NN</text>

  <ellipse cx="1080" cy="720" rx="44" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="1080" y="724" class="attr-text">Họ tên NN</text>

  <!-- 10. THUỘC (ĐV KH) -->
  <g filter="url(#shadow)">
    <polygon points="1240,490 1285,520 1240,550 1195,520" fill="url(#relGrad)" />
    <text x="1240" y="524" class="rel-title">THUỘC</text>
  </g>

  <!-- 11. ĐƠN VỊ KH -->
  <g filter="url(#shadow)">
    <rect x="1160" y="370" width="160" height="50" rx="8" fill="url(#entGrad1)" />
    <text x="1240" y="400" class="ent-title">ĐƠN VỊ KH</text>
  </g>
  <line x1="1240" y1="370" x2="1165" y2="310" class="attr-line" />
  <line x1="1240" y1="370" x2="1240" y2="300" class="attr-line" />
  <line x1="1240" y1="370" x2="1315" y2="310" class="attr-line" />

  <ellipse cx="1165" cy="310" rx="42" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="1165" y="314" class="attr-text pk-attr">Mã ĐV</text>

  <ellipse cx="1240" cy="300" rx="42" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="1240" y="304" class="attr-text">Tên ĐV</text>

  <ellipse cx="1315" cy="310" rx="42" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="1315" y="314" class="attr-text">Địa chỉ</text>

  <!-- Legend -->
  <g transform="translate(1020, 800)">
    <rect width="380" height="135" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" />
    <text x="15" y="24" font-size="12" font-weight="800" fill="#1e293b">QUY ƯỚC KÝ HIỆU ERD (PETER CHEN):</text>
    <rect x="15" y="35" width="28" height="15" rx="3" fill="#2563eb" />
    <text x="52" y="47" font-size="11.5" fill="#475569">Hình chữ nhật: Thực thể (Entities)</text>
    <polygon points="25,58 35,66 25,74 15,66" fill="#f59e0b" />
    <text x="52" y="70" font-size="11.5" fill="#475569">Hình thoi: Mối quan hệ (Relationships)</text>
    <ellipse cx="25" cy="90" rx="14" ry="8" fill="#f8fafc" stroke="#3b82f6" />
    <text x="52" y="93" font-size="11.5" fill="#475569">Hình Elip: Thuộc tính (<tspan text-decoration="underline" font-weight="bold">Gạch chân</tspan>: Khóa chính PK)</text>
    <text x="15" y="118" font-size="11.5" font-weight="700" fill="#dc2626">1 : N, N : M : Bản số / Lực lượng tham gia (Cardinality)</text>
  </g>
</svg>
"""

# Diagram 2: Step 5 Normalized ERD (Gộp Đơn vị khách)
svg_step5 = """<svg width="1440" height="960" viewBox="0 0 1440 960" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border-radius: 12px;">
  <defs>
    <filter id="shadow5" x="-8%" y="-8%" width="120%" height="120%">
      <feDropShadow dx="2" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
    <linearGradient id="entGradCustomer" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3730a3"/>
      <stop offset="100%" stop-color="#4f46e5"/>
    </linearGradient>
    <linearGradient id="entGradEntity" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e40af"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>
    <linearGradient id="entGradProduct" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f766e"/>
      <stop offset="100%" stop-color="#14b8a6"/>
    </linearGradient>
    <linearGradient id="relGradNorm" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#b45309"/>
      <stop offset="100%" stop-color="#f59e0b"/>
    </linearGradient>
    <linearGradient id="relGradNormGiao" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c2410c"/>
      <stop offset="100%" stop-color="#f97316"/>
    </linearGradient>
  </defs>

  <style>
    .line { stroke: #475569; stroke-width: 2.5; fill: none; }
    .cardinality { font-size: 14px; font-weight: 800; fill: #dc2626; }
    .attr-line { stroke: #94a3b8; stroke-width: 1.5; stroke-dasharray: 2 2; }
    .ent-title { font-size: 14px; font-weight: 800; fill: #ffffff; text-anchor: middle; }
    .rel-title { font-size: 13px; font-weight: 800; fill: #ffffff; text-anchor: middle; }
    .attr-text { font-size: 12px; fill: #1e293b; text-anchor: middle; }
    .pk-attr { text-decoration: underline; font-weight: 800; fill: #0f172a; }
  </style>

  <!-- Title Banner -->
  <rect x="20" y="15" width="1400" height="42" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5" />
  <text x="720" y="42" font-size="15" font-weight="800" fill="#166534" text-anchor="middle">
    BƯỚC 5: SƠ ĐỒ MÔ HÌNH ERD SAU KHI CHUẨN HÓA, RÚT GỌN (GỘP THÀNH "ĐƠN VỊ KHÁCH")
  </text>

  <!-- Subtitle notification banner -->
  <rect x="360" y="65" width="720" height="30" rx="6" fill="#e0e7ff" stroke="#a5b4fc" stroke-width="1" />
  <text x="720" y="85" font-size="12.5" font-weight="700" fill="#3730a3" text-anchor="middle">
    ✓ Chuẩn hóa: Đơn vị ĐH &amp; Đơn vị KH gộp thành 1 thực thể duy nhất: ĐƠN VỊ KHÁCH (Mã ĐV, Tên ĐV, Địa chỉ, Điện thoại)
  </text>

  <!-- Connectors -->
  <!-- ĐƠN VỊ KHÁCH (720, 180) -> THUỘC 1 (420, 240) -> NGƯỜI ĐẶT (180, 395) -->
  <line x1="610" y1="180" x2="470" y2="230" class="line" />
  <line x1="390" y1="260" x2="230" y2="370" class="line" />
  <text x="560" y="195" class="cardinality">1</text>
  <text x="270" y="340" class="cardinality">N</text>

  <!-- ĐƠN VỊ KHÁCH (720, 180) -> THUỘC 2 (1020, 240) -> NGƯỜI NHẬN (1240, 395) -->
  <line x1="830" y1="180" x2="970" y2="230" class="line" />
  <line x1="1050" y1="260" x2="1190" y2="370" class="line" />
  <text x="870" y="195" class="cardinality">1</text>
  <text x="1155" y="340" class="cardinality">N</text>

  <!-- NGƯỜI ĐẶT (180, 395) -> ĐẶT (440, 395) -> HÀNG (720, 395) -->
  <line x1="260" y1="395" x2="380" y2="395" class="line" />
  <line x1="500" y1="395" x2="640" y2="395" class="line" />
  <text x="290" y="385" class="cardinality">1</text>
  <text x="610" y="385" class="cardinality">N</text>

  <!-- HÀNG (720, 395) -> GIAO (720, 640) -->
  <line x1="720" y1="420" x2="720" y2="590" class="line" />
  <text x="735" y="450" class="cardinality">N</text>

  <!-- NGƯỜI GIAO (180, 640) -> GIAO (720, 640) -->
  <line x1="260" y1="640" x2="650" y2="640" class="line" />
  <text x="290" y="630" class="cardinality">1</text>

  <!-- NƠI GIAO (440, 810) -> GIAO (720, 640) -->
  <line x1="440" y1="785" x2="680" y2="665" class="line" />
  <text x="460" y="760" class="cardinality">1</text>

  <!-- NGƯỜI NHẬN (1240, 395) -> GIAO (720, 640) -->
  <line x1="1210" y1="420" x2="780" y2="625" class="line" />
  <text x="1150" y="450" class="cardinality">1</text>


  <!-- ==================== ENTITIES ==================== -->

  <!-- GỘP THÀNH: ĐƠN VỊ KHÁCH (720, 180) -->
  <g filter="url(#shadow5)">
    <rect x="610" y="150" width="220" height="60" rx="10" fill="url(#entGradCustomer)" stroke="#312e81" stroke-width="2" />
    <text x="720" y="186" font-size="16" font-weight="800" fill="#ffffff" text-anchor="middle">ĐƠN VỊ KHÁCH</text>
  </g>
  <!-- Attributes for ĐƠN VỊ KHÁCH -->
  <line x1="610" y1="165" x2="520" y2="125" class="attr-line" />
  <line x1="670" y1="150" x2="630" y2="105" class="attr-line" />
  <line x1="770" y1="150" x2="810" y2="105" class="attr-line" />
  <line x1="830" y1="165" x2="920" y2="125" class="attr-line" />

  <ellipse cx="520" cy="125" rx="44" ry="16" fill="#eef2ff" stroke="#6366f1" stroke-width="1.5" />
  <text x="520" y="129" class="attr-text pk-attr">Mã ĐV</text>

  <ellipse cx="630" cy="105" rx="44" ry="16" fill="#eef2ff" stroke="#6366f1" stroke-width="1.5" />
  <text x="630" y="109" class="attr-text">Tên ĐV</text>

  <ellipse cx="810" cy="105" rx="44" ry="16" fill="#eef2ff" stroke="#6366f1" stroke-width="1.5" />
  <text x="810" y="109" class="attr-text">Địa chỉ</text>

  <ellipse cx="920" cy="125" rx="46" ry="16" fill="#eef2ff" stroke="#6366f1" stroke-width="1.5" />
  <text x="920" y="129" class="attr-text">Điện thoại</text>


  <!-- THUỘC (1) -->
  <g filter="url(#shadow5)">
    <polygon points="420,210 465,240 420,270 375,240" fill="url(#relGradNorm)" />
    <text x="420" y="244" class="rel-title">THUỘC</text>
  </g>

  <!-- THUỘC (2) -->
  <g filter="url(#shadow5)">
    <polygon points="1020,210 1065,240 1020,270 975,240" fill="url(#relGradNorm)" />
    <text x="1020" y="244" class="rel-title">THUỘC</text>
  </g>


  <!-- NGƯỜI ĐẶT -->
  <g filter="url(#shadow5)">
    <rect x="100" y="370" width="160" height="50" rx="8" fill="url(#entGradEntity)" />
    <text x="180" y="400" class="ent-title">NGƯỜI ĐẶT</text>
  </g>
  <line x1="100" y1="395" x2="35" y2="365" class="attr-line" />
  <line x1="100" y1="395" x2="35" y2="425" class="attr-line" />

  <ellipse cx="35" cy="365" rx="44" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="35" y="369" class="attr-text pk-attr">Mã số NĐ</text>

  <ellipse cx="35" cy="425" rx="44" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="35" y="429" class="attr-text">Họ tên NĐ</text>


  <!-- ĐẶT -->
  <g filter="url(#shadow5)">
    <polygon points="440,355 500,395 440,435 380,395" fill="url(#relGradNorm)" />
    <text x="440" y="399" class="rel-title">ĐẶT</text>
  </g>
  <line x1="440" y1="435" x2="370" y2="490" class="attr-line" />
  <line x1="440" y1="435" x2="440" y2="505" class="attr-line" />
  <line x1="440" y1="435" x2="510" y2="490" class="attr-line" />

  <ellipse cx="370" cy="490" rx="40" ry="16" fill="#fffbeb" stroke="#d97706" stroke-width="1.5" />
  <text x="370" y="494" class="attr-text" font-weight="700">Số ĐH</text>

  <ellipse cx="440" cy="505" rx="40" ry="16" fill="#fffbeb" stroke="#d97706" stroke-width="1.5" />
  <text x="440" y="509" class="attr-text" font-weight="700">Ngày đặt</text>

  <ellipse cx="510" cy="490" rx="40" ry="16" fill="#fffbeb" stroke="#d97706" stroke-width="1.5" />
  <text x="510" y="494" class="attr-text" font-weight="700">Số lượng</text>


  <!-- HÀNG -->
  <g filter="url(#shadow5)">
    <rect x="640" y="370" width="160" height="50" rx="8" fill="url(#entGradProduct)" />
    <text x="720" y="400" class="ent-title">HÀNG</text>
  </g>
  <line x1="720" y1="370" x2="680" y2="310" class="attr-line" />
  <line x1="720" y1="370" x2="760" y2="310" class="attr-line" />
  <line x1="800" y1="385" x2="880" y2="365" class="attr-line" />
  <line x1="800" y1="405" x2="880" y2="420" class="attr-line" />

  <ellipse cx="680" cy="310" rx="42" ry="16" fill="#f0fdf4" stroke="#059669" stroke-width="1.5" />
  <text x="680" y="314" class="attr-text pk-attr">Mã hàng</text>

  <ellipse cx="760" cy="310" rx="42" ry="16" fill="#f0fdf4" stroke="#059669" stroke-width="1.5" />
  <text x="760" y="314" class="attr-text">Tên hàng</text>

  <ellipse cx="880" cy="365" rx="42" ry="16" fill="#f0fdf4" stroke="#059669" stroke-width="1.5" />
  <text x="880" y="369" class="attr-text">Đv tính</text>

  <ellipse cx="880" cy="420" rx="46" ry="16" fill="#f0fdf4" stroke="#059669" stroke-width="1.5" />
  <text x="880" y="424" class="attr-text">Mô tả hàng</text>


  <!-- NGƯỜI NHẬN -->
  <g filter="url(#shadow5)">
    <rect x="1160" y="370" width="160" height="50" rx="8" fill="url(#entGradEntity)" />
    <text x="1240" y="400" class="ent-title">NGƯỜI NHẬN</text>
  </g>
  <line x1="1320" y1="395" x2="1385" y2="365" class="attr-line" />
  <line x1="1320" y1="395" x2="1385" y2="425" class="attr-line" />

  <ellipse cx="1385" cy="365" rx="44" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="1385" y="369" class="attr-text pk-attr">Mã số NN</text>

  <ellipse cx="1385" cy="425" rx="44" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="1385" y="429" class="attr-text">Họ tên NN</text>


  <!-- GIAO (Relationship) -->
  <g filter="url(#shadow5)">
    <polygon points="720,590 790,640 720,690 650,640" fill="url(#relGradNormGiao)" />
    <text x="720" y="644" class="rel-title">GIAO</text>
  </g>
  <!-- Attributes of GIAO -->
  <line x1="720" y1="690" x2="630" y2="760" class="attr-line" />
  <line x1="720" y1="690" x2="685" y2="785" class="attr-line" />
  <line x1="720" y1="690" x2="740" y2="785" class="attr-line" />
  <line x1="720" y1="690" x2="795" y2="760" class="attr-line" />
  <line x1="720" y1="690" x2="855" y2="725" class="attr-line" />

  <ellipse cx="630" cy="760" rx="40" ry="16" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5" />
  <text x="630" y="764" class="attr-text" font-weight="700">Số PG</text>

  <ellipse cx="685" cy="785" rx="40" ry="16" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5" />
  <text x="685" y="789" class="attr-text" font-weight="700">Ngày giao</text>

  <ellipse cx="740" cy="785" rx="40" ry="16" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5" />
  <text x="740" y="789" class="attr-text" font-weight="700">Số lượng</text>

  <ellipse cx="795" cy="760" rx="40" ry="16" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5" />
  <text x="795" y="764" class="attr-text" font-weight="700">Đơn giá</text>

  <ellipse cx="855" cy="725" rx="44" ry="16" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5" />
  <text x="855" y="729" class="attr-text" font-weight="700">Thành tiền</text>


  <!-- NGƯỜI GIAO -->
  <g filter="url(#shadow5)">
    <rect x="100" y="615" width="160" height="50" rx="8" fill="url(#entGradEntity)" />
    <text x="180" y="645" class="ent-title">NGƯỜI GIAO</text>
  </g>
  <line x1="100" y1="640" x2="35" y2="610" class="attr-line" />
  <line x1="100" y1="640" x2="35" y2="670" class="attr-line" />

  <ellipse cx="35" cy="610" rx="44" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="35" y="614" class="attr-text pk-attr">Mã số NG</text>

  <ellipse cx="35" cy="670" rx="44" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="35" y="674" class="attr-text">Họ tên NG</text>


  <!-- NƠI GIAO -->
  <g filter="url(#shadow5)">
    <rect x="360" y="785" width="160" height="50" rx="8" fill="url(#entGradEntity)" />
    <text x="440" y="815" class="ent-title">NƠI GIAO</text>
  </g>
  <line x1="440" y1="835" x2="380" y2="885" class="attr-line" />
  <line x1="440" y1="835" x2="500" y2="885" class="attr-line" />

  <ellipse cx="380" cy="885" rx="46" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="380" y="889" class="attr-text pk-attr">Mã số ĐĐG</text>

  <ellipse cx="500" cy="885" rx="46" ry="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" />
  <text x="500" y="889" class="attr-text">Tên nơi giao</text>

  <!-- Legend Box (Step 5 Specific) -->
  <g transform="translate(1000, 785)">
    <rect width="400" height="150" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" />
    <text x="20" y="26" font-size="13" font-weight="800" fill="#1e293b">Ý NGHĨA CHUẨN HÓA BƯỚC 5:</text>
    <text x="20" y="52" font-size="12" fill="#334155">1. Gộp ĐƠN VỊ ĐH &amp; ĐƠN VỊ KH thành ĐƠN VỊ KHÁCH</text>
    <text x="20" y="74" font-size="12" fill="#334155">2. Loại bỏ dư thừa dữ liệu danh mục khách hàng đối tác</text>
    <text x="20" y="96" font-size="12" fill="#334155">3. Người đặt &amp; Người nhận cùng thuộc về Đơn vị khách</text>
    <text x="20" y="118" font-size="12" fill="#334155">4. Mối quan hệ ĐẶT &amp; GIAO bám sát quy trình chứng từ</text>
    <text x="20" y="138" font-size="12" font-weight="700" fill="#16a34a">✓ Sơ đồ hoàn chỉnh, tối ưu chuẩn 3NF</text>
  </g>

</svg>
"""

# Diagram 3: Relational Schema (Clean spacing & fully contained summary)
svg_tables = """<svg width="1440" height="980" viewBox="0 0 1440 980" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border-radius: 12px;">
  <defs>
    <filter id="shadowTbl" x="-8%" y="-8%" width="120%" height="120%">
      <feDropShadow dx="2" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <style>
    .tbl-title { font-size: 13px; font-weight: 800; fill: #ffffff; }
    .col-pk { font-size: 12px; font-weight: 800; fill: #b91c1c; }
    .col-fk { font-size: 12px; font-weight: 700; fill: #2563eb; }
    .col-norm { font-size: 12px; fill: #1e293b; }
    .col-type { font-size: 11px; fill: #64748b; text-anchor: end; font-family: monospace; }
  </style>

  <!-- Title Banner -->
  <rect x="20" y="15" width="1400" height="42" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" />
  <text x="720" y="42" font-size="15" font-weight="800" fill="#0f172a" text-anchor="middle">
    LƯỢC ĐỒ CƠ SỞ DỮ LIỆU QUAN HỆ (RELATIONAL SCHEMA) TỪ MÔ HÌNH ERD
  </text>

  <!-- TABLE 1: DON_VI_KHACH -->
  <g transform="translate(60, 80)" filter="url(#shadowTbl)">
    <rect width="250" height="150" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 242,0 Q 250,0 250,8 L 250,32 L 0,32 Z" fill="#4338ca" />
    <text x="15" y="21" class="tbl-title">🏢 DON_VI_KHACH</text>
    
    <text x="15" y="55" class="col-pk">🔑 MaDV (PK)</text>
    <text x="235" y="55" class="col-type">VARCHAR(20)</text>
    <line x1="10" y1="65" x2="240" y2="65" stroke="#f1f5f9" />

    <text x="15" y="85" class="col-norm">TenDV</text>
    <text x="235" y="85" class="col-type">NVARCHAR(100)</text>
    <line x1="10" y1="95" x2="240" y2="95" stroke="#f1f5f9" />

    <text x="15" y="115" class="col-norm">DiaChi</text>
    <text x="235" y="115" class="col-type">NVARCHAR(200)</text>
    <line x1="10" y1="125" x2="240" y2="125" stroke="#f1f5f9" />

    <text x="15" y="142" class="col-norm">DienThoai</text>
    <text x="235" y="142" class="col-type">VARCHAR(15)</text>
  </g>

  <!-- TABLE 2: NGUOI_DAT -->
  <g transform="translate(400, 80)" filter="url(#shadowTbl)">
    <rect width="250" height="125" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 242,0 Q 250,0 250,8 L 250,32 L 0,32 Z" fill="#1e40af" />
    <text x="15" y="21" class="tbl-title">👤 NGUOI_DAT</text>
    
    <text x="15" y="55" class="col-pk">🔑 MaSoND (PK)</text>
    <text x="235" y="55" class="col-type">VARCHAR(20)</text>
    <line x1="10" y1="65" x2="240" y2="65" stroke="#f1f5f9" />

    <text x="15" y="85" class="col-norm">HoTenND</text>
    <text x="235" y="85" class="col-type">NVARCHAR(100)</text>
    <line x1="10" y1="95" x2="240" y2="95" stroke="#f1f5f9" />

    <text x="15" y="115" class="col-fk">🔗 MaDV (FK)</text>
    <text x="235" y="115" class="col-type">VARCHAR(20)</text>
  </g>

  <!-- TABLE 3: NGUOI_NHAN -->
  <g transform="translate(740, 80)" filter="url(#shadowTbl)">
    <rect width="250" height="125" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 242,0 Q 250,0 250,8 L 250,32 L 0,32 Z" fill="#1e40af" />
    <text x="15" y="21" class="tbl-title">👤 NGUOI_NHAN</text>
    
    <text x="15" y="55" class="col-pk">🔑 MaSoNN (PK)</text>
    <text x="235" y="55" class="col-type">VARCHAR(20)</text>
    <line x1="10" y1="65" x2="240" y2="65" stroke="#f1f5f9" />

    <text x="15" y="85" class="col-norm">HoTenNN</text>
    <text x="235" y="85" class="col-type">NVARCHAR(100)</text>
    <line x1="10" y1="95" x2="240" y2="95" stroke="#f1f5f9" />

    <text x="15" y="115" class="col-fk">🔗 MaDV (FK)</text>
    <text x="235" y="115" class="col-type">VARCHAR(20)</text>
  </g>

  <!-- TABLE 4: NGUOI_GIAO -->
  <g transform="translate(1080, 80)" filter="url(#shadowTbl)">
    <rect width="250" height="100" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 242,0 Q 250,0 250,8 L 250,32 L 0,32 Z" fill="#0f766e" />
    <text x="15" y="21" class="tbl-title">🚚 NGUOI_GIAO</text>
    
    <text x="15" y="55" class="col-pk">🔑 MaSoNG (PK)</text>
    <text x="235" y="55" class="col-type">VARCHAR(20)</text>
    <line x1="10" y1="65" x2="240" y2="65" stroke="#f1f5f9" />

    <text x="15" y="85" class="col-norm">HoTenNG</text>
    <text x="235" y="85" class="col-type">NVARCHAR(100)</text>
  </g>


  <!-- TABLE 5: DON_DAT_HANG -->
  <g transform="translate(400, 290)" filter="url(#shadowTbl)">
    <rect width="250" height="125" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 242,0 Q 250,0 250,8 L 250,32 L 0,32 Z" fill="#b45309" />
    <text x="15" y="21" class="tbl-title">📋 DON_DAT_HANG</text>
    
    <text x="15" y="55" class="col-pk">🔑 SoDH (PK)</text>
    <text x="235" y="55" class="col-type">VARCHAR(20)</text>
    <line x1="10" y1="65" x2="240" y2="65" stroke="#f1f5f9" />

    <text x="15" y="85" class="col-norm">NgayDat</text>
    <text x="235" y="85" class="col-type">DATE</text>
    <line x1="10" y1="95" x2="240" y2="95" stroke="#f1f5f9" />

    <text x="15" y="115" class="col-fk">🔗 MaSoND (FK)</text>
    <text x="235" y="115" class="col-type">VARCHAR(20)</text>
  </g>

  <!-- TABLE 6: HANG -->
  <g transform="translate(60, 480)" filter="url(#shadowTbl)">
    <rect width="250" height="150" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 242,0 Q 250,0 250,8 L 250,32 L 0,32 Z" fill="#047857" />
    <text x="15" y="21" class="tbl-title">📦 HANG_HOA</text>
    
    <text x="15" y="55" class="col-pk">🔑 MaHang (PK)</text>
    <text x="235" y="55" class="col-type">VARCHAR(20)</text>
    <line x1="10" y1="65" x2="240" y2="65" stroke="#f1f5f9" />

    <text x="15" y="85" class="col-norm">TenHang</text>
    <text x="235" y="85" class="col-type">NVARCHAR(100)</text>
    <line x1="10" y1="95" x2="240" y2="95" stroke="#f1f5f9" />

    <text x="15" y="115" class="col-norm">DvTinh</text>
    <text x="235" y="115" class="col-type">NVARCHAR(30)</text>
    <line x1="10" y1="125" x2="240" y2="125" stroke="#f1f5f9" />

    <text x="15" y="142" class="col-norm">MoTaHang</text>
    <text x="235" y="142" class="col-type">NVARCHAR(255)</text>
  </g>

  <!-- TABLE 7: CHI_TIET_DAT_HANG -->
  <g transform="translate(400, 480)" filter="url(#shadowTbl)">
    <rect width="250" height="125" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 242,0 Q 250,0 250,8 L 250,32 L 0,32 Z" fill="#b45309" />
    <text x="15" y="21" class="tbl-title">📝 CHI_TIET_DAT_HANG</text>
    
    <text x="15" y="55" class="col-pk">🔑 SoDH (PK, FK)</text>
    <text x="235" y="55" class="col-type">VARCHAR(20)</text>
    <line x1="10" y1="65" x2="240" y2="65" stroke="#f1f5f9" />

    <text x="15" y="85" class="col-pk">🔑 MaHang (PK, FK)</text>
    <text x="235" y="85" class="col-type">VARCHAR(20)</text>
    <line x1="10" y1="95" x2="240" y2="95" stroke="#f1f5f9" />

    <text x="15" y="115" class="col-norm">SoLuongDat</text>
    <text x="235" y="115" class="col-type">INT</text>
  </g>

  <!-- TABLE 8: NOI_GIAO -->
  <g transform="translate(1080, 240)" filter="url(#shadowTbl)">
    <rect width="250" height="100" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 242,0 Q 250,0 250,8 L 250,32 L 0,32 Z" fill="#0369a1" />
    <text x="15" y="21" class="tbl-title">📍 NOI_GIAO</text>
    
    <text x="15" y="55" class="col-pk">🔑 MaSoDDG (PK)</text>
    <text x="235" y="55" class="col-type">VARCHAR(20)</text>
    <line x1="10" y1="65" x2="240" y2="65" stroke="#f1f5f9" />

    <text x="15" y="85" class="col-norm">TenNoiGiao</text>
    <text x="235" y="85" class="col-type">NVARCHAR(200)</text>
  </g>

  <!-- TABLE 9: PHIEU_GIAO_HANG -->
  <g transform="translate(740, 440)" filter="url(#shadowTbl)">
    <rect width="260" height="205" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 252,0 Q 260,0 260,8 L 260,32 L 0,32 Z" fill="#c2410c" />
    <text x="15" y="21" class="tbl-title">📄 PHIEU_GIAO_HANG</text>
    
    <text x="15" y="55" class="col-pk">🔑 SoPG (PK)</text>
    <text x="245" y="55" class="col-type">VARCHAR(20)</text>
    <line x1="10" y1="65" x2="250" y2="65" stroke="#f1f5f9" />

    <text x="15" y="85" class="col-norm">NgayGiao</text>
    <text x="245" y="85" class="col-type">DATE</text>
    <line x1="10" y1="95" x2="250" y2="95" stroke="#f1f5f9" />

    <text x="15" y="115" class="col-fk">🔗 SoDH (FK)</text>
    <text x="245" y="115" class="col-type">VARCHAR(20)</text>
    <line x1="10" y1="125" x2="250" y2="125" stroke="#f1f5f9" />

    <text x="15" y="145" class="col-fk">🔗 MaSoNG (FK)</text>
    <text x="245" y="145" class="col-type">VARCHAR(20)</text>
    <line x1="10" y1="155" x2="250" y2="155" stroke="#f1f5f9" />

    <text x="15" y="175" class="col-fk">🔗 MaSoNN (FK)</text>
    <text x="245" y="175" class="col-type">VARCHAR(20)</text>
    <line x1="10" y1="185" x2="250" y2="185" stroke="#f1f5f9" />

    <text x="15" y="198" class="col-fk">🔗 MaSoDDG (FK)</text>
    <text x="245" y="198" class="col-type">VARCHAR(20)</text>
  </g>

  <!-- TABLE 10: CHI_TIET_GIAO_HANG -->
  <g transform="translate(1080, 440)" filter="url(#shadowTbl)">
    <rect width="270" height="175" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 262,0 Q 270,0 270,8 L 270,32 L 0,32 Z" fill="#c2410c" />
    <text x="15" y="21" class="tbl-title">🧾 CHI_TIET_GIAO_HANG</text>
    
    <text x="15" y="55" class="col-pk">🔑 SoPG (PK, FK)</text>
    <text x="255" y="55" class="col-type">VARCHAR(20)</text>
    <line x1="10" y1="65" x2="260" y2="65" stroke="#f1f5f9" />

    <text x="15" y="85" class="col-pk">🔑 MaHang (PK, FK)</text>
    <text x="255" y="85" class="col-type">VARCHAR(20)</text>
    <line x1="10" y1="95" x2="260" y2="95" stroke="#f1f5f9" />

    <text x="15" y="115" class="col-norm">SoLuongGiao</text>
    <text x="255" y="115" class="col-type">INT</text>
    <line x1="10" y1="125" x2="260" y2="125" stroke="#f1f5f9" />

    <text x="15" y="142" class="col-norm">DonGia</text>
    <text x="255" y="142" class="col-type">DECIMAL(18,2)</text>
    <line x1="10" y1="152" x2="260" y2="152" stroke="#f1f5f9" />

    <text x="15" y="166" class="col-norm">ThanhTien</text>
    <text x="255" y="166" class="col-type">DECIMAL(18,2)</text>
  </g>

  <!-- Connectors between Tables (Visualizing PK-FK Relationships) -->
  <path d="M 310,135 L 355,135 L 355,195 L 400,195" fill="none" stroke="#6366f1" stroke-width="2" />
  <path d="M 310,135 L 355,135 L 355,55 L 710,55 L 710,195 L 740,195" fill="none" stroke="#6366f1" stroke-width="2" />
  <path d="M 525,205 L 525,290" fill="none" stroke="#2563eb" stroke-width="2" />
  <path d="M 525,415 L 525,480" fill="none" stroke="#d97706" stroke-width="2" />
  <path d="M 310,535 L 400,535" fill="none" stroke="#059669" stroke-width="2" />
  <path d="M 650,350 L 695,350 L 695,555 L 740,555" fill="none" stroke="#d97706" stroke-width="2" />
  <path d="M 1000,495 L 1080,495" fill="none" stroke="#ea580c" stroke-width="2" />
  <path d="M 185,630 L 185,690 L 1215,690 L 1215,615" fill="none" stroke="#059669" stroke-width="2" />

  <!-- Summary Card (Perfect formatting & text containment) -->
  <g transform="translate(60, 720)">
    <rect width="1320" height="235" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" />
    <text x="30" y="32" font-size="14.5" font-weight="800" fill="#0f172a">TỔNG HỢP CÁC RÀNG BUỘC TOÀN VẸN &amp; KHÓA NGOẠI (FOREIGN KEYS) CỦA CƠ SỞ DỮ LIỆU:</text>
    
    <text x="30" y="65" font-size="13" font-weight="700" fill="#4338ca">1. Bảng Khách hàng &amp; Nhân sự đại diện:</text>
    <text x="50" y="85" font-size="12" fill="#334155">• NGUOI_DAT (MaDV) và NGUOI_NHAN (MaDV) là khóa ngoại tham chiếu đến DON_VI_KHACH (MaDV). Quan hệ 1 : N.</text>

    <text x="30" y="115" font-size="13" font-weight="700" fill="#b45309">2. Bảng Đơn đặt hàng &amp; Chi tiết đặt:</text>
    <text x="50" y="135" font-size="12" fill="#334155">• DON_DAT_HANG (MaSoND) tham chiếu NGUOI_DAT. CHI_TIET_DAT_HANG có khóa chính phức hợp (SoDH, MaHang) giải quyết quan hệ N : M giữa Đơn đặt hàng và Hàng hóa.</text>

    <text x="30" y="165" font-size="13" font-weight="700" fill="#c2410c">3. Bảng Phiếu giao hàng &amp; Chi tiết giao hàng:</text>
    <text x="50" y="185" font-size="12" fill="#334155">• PHIEU_GIAO_HANG liên kết đa chiều: SoDH (Đơn đặt hàng gốc), MaSoNG (Người giao), MaSoNN (Người nhận), MaSoDDG (Nơi giao).</text>
    <text x="50" y="205" font-size="12" fill="#334155">• CHI_TIET_GIAO_HANG có khóa chính phức hợp (SoPG, MaHang) lưu số lượng giao thực tế, đơn giá và thành tiền theo từng mặt hàng.</text>
  </g>
</svg>
"""

base_dir = r"C:\Users\Admin\.gemini\antigravity-ide\scratch\backend_repo"
assets_dir = os.path.join(base_dir, "assets")

with open(os.path.join(assets_dir, "erd_step4_initial.svg"), "w", encoding="utf-8") as f:
    f.write(svg_step4)

with open(os.path.join(assets_dir, "erd_step5_normalized.svg"), "w", encoding="utf-8") as f:
    f.write(svg_step5)

with open(os.path.join(assets_dir, "relational_schema.svg"), "w", encoding="utf-8") as f:
    f.write(svg_tables)

with open(os.path.join(assets_dir, "step4.html"), "w", encoding="utf-8") as f:
    f.write(create_html_wrapper(svg_step4, "SƠ ĐỒ ERD BƯỚC 4: MÔ HÌNH BAN ĐẦU (CHƯA RÚT GỌN)"))

with open(os.path.join(assets_dir, "step5.html"), "w", encoding="utf-8") as f:
    f.write(create_html_wrapper(svg_step5, "SƠ ĐỒ ERD BƯỚC 5: MÔ HÌNH CHUẨN HÓA, RÚT GỌN"))

with open(os.path.join(assets_dir, "schema.html"), "w", encoding="utf-8") as f:
    f.write(create_html_wrapper(svg_tables, "LƯỢC ĐỒ QUAN HỆ (RELATIONAL SCHEMA)"))

print("Refined SVGs and HTMLs written successfully!")
