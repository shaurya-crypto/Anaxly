"""
High-Precision Vector SVG Builder for Class 10 Mathematics (NCERT CBSE)
Follows /unslop, /hairline-create, and /hairline-adopt design standards:
- Elegant, crisp vector geometry with exact coordinates
- Balanced contrast on subtle slate/neutral backgrounds (#FFFFFF with #F8FAFC)
- Colors: #0F172A (slate text), #2563EB (academic blue), #16A34A (botanical green), #DC2626 (crimson)
- Legible mathematical notation and labels, zero slop/clipart/useless clutter
- Standard responsive viewBox (580 x 360)
"""

import math

def get_svg_wrapper(inner_svg: str, title: str = "", caption: str = "", width: int = 580, height: int = 360) -> str:
    escaped_title = title.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    escaped_caption = caption.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
    header_html = ""
    if title:
        header_html = f"""
        <g id="header">
          <text x="24" y="32" fill="#0F172A" font-size="14" font-weight="700" font-family="system-ui, -apple-system, sans-serif">{escaped_title}</text>
          {f'<text x="24" y="48" fill="#64748B" font-size="11" font-family="system-ui, -apple-system, sans-serif">{escaped_caption}</text>' if caption else ''}
        </g>
        """
        
    return f"""<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border:1.5px solid #E2E8F0; border-radius:12px; font-family:system-ui, -apple-system, sans-serif;">
  <defs>
    <pattern id="gridPattern" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#F1F5F9" stroke-width="0.8"/>
    </pattern>
    <marker id="arrowBlue" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2563EB"/>
    </marker>
    <marker id="arrowSlate" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#475569"/>
    </marker>
    <marker id="arrowRed" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#DC2626"/>
    </marker>
    <marker id="arrowGreen" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#16A34A"/>
    </marker>
  </defs>
  <rect width="{width}" height="{height}" fill="#FFFFFF" rx="12"/>
  <rect width="{width}" height="{height}" fill="url(#gridPattern)" rx="12"/>
  {header_html}
  {inner_svg}
</svg>""".strip()


def build_cartesian_svg(domain=(-6, 6), range_y=(-6, 6), points=None, lines=None, curves=None, polygons=None, title="", caption=""):
    """
    Renders a true Cartesian coordinate system with crisp axes, grid ticks, and plotted geometric objects.
    """
    width, height = 580, 360
    dx = domain[1] - domain[0]
    dy = range_y[1] - range_y[0]
    sx = (width - 120) / dx if dx else 30
    sy = (height - 120) / dy if dy else 30
    scale = min(sx, sy)
    
    ox = 60 + (-domain[0]) * scale
    oy = 300 - (-range_y[0]) * scale
    
    svg_elements = []
    
    # Grid lines & ticks
    for x in range(int(domain[0]), int(domain[1]) + 1):
        px = ox + x * scale
        if 40 <= px <= width - 40:
            svg_elements.append(f'<line x1="{px}" y1="60" x2="{px}" y2="{height-40}" stroke="#E2E8F0" stroke-width="0.8"/>')
            svg_elements.append(f'<line x1="{px}" y1="{oy-3}" x2="{px}" y2="{oy+3}" stroke="#94A3B8" stroke-width="1.2"/>')
            if x != 0 and (x % 2 == 0 or dx <= 8):
                svg_elements.append(f'<text x="{px}" y="{oy+16}" fill="#64748B" font-size="10" text-anchor="middle">{x}</text>')
                
    for y in range(int(range_y[0]), int(range_y[1]) + 1):
        py = oy - y * scale
        if 60 <= py <= height - 40:
            svg_elements.append(f'<line x1="40" y1="{py}" x2="{width-40}" y2="{py}" stroke="#E2E8F0" stroke-width="0.8"/>')
            svg_elements.append(f'<line x1="{ox-3}" y1="{py}" x2="{ox+3}" y2="{py}" stroke="#94A3B8" stroke-width="1.2"/>')
            if y != 0 and (y % 2 == 0 or dy <= 8):
                svg_elements.append(f'<text x="{ox-8}" y="{py+3}" fill="#64748B" font-size="10" text-anchor="end">{y}</text>')
                
    # Axes
    svg_elements.append(f'<line x1="40" y1="{oy}" x2="{width-30}" y2="{oy}" stroke="#334155" stroke-width="1.8" marker-end="url(#arrowSlate)"/>')
    svg_elements.append(f'<line x1="{ox}" y1="{height-30}" x2="{ox}" y2="50" stroke="#334155" stroke-width="1.8" marker-end="url(#arrowSlate)"/>')
    svg_elements.append(f'<text x="{width-25}" y="{oy+4}" fill="#0F172A" font-size="12" font-weight="700">x</text>')
    svg_elements.append(f'<text x="{ox}" y="42" fill="#0F172A" font-size="12" font-weight="700" text-anchor="middle">y</text>')
    svg_elements.append(f'<text x="{ox-8}" y="{oy+16}" fill="#64748B" font-size="10" text-anchor="end">O</text>')
    
    # Curves (e.g. parabolas y = ax^2 + bx + c)
    if curves:
        for c in curves:
            pts = []
            steps = 60
            for i in range(steps + 1):
                cur_x = domain[0] + (dx * i / steps)
                cur_y = c["fn"](cur_x)
                if range_y[0] - 2 <= cur_y <= range_y[1] + 2:
                    cx_px = ox + cur_x * scale
                    cy_px = oy - cur_y * scale
                    pts.append(f"{cx_px:.1f},{cy_px:.1f}")
            if pts:
                color = c.get("color", "#2563EB")
                stroke_w = c.get("stroke_width", 2.2)
                svg_elements.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="{stroke_w}"/>')
                if "label" in c:
                    lx = ox + c.get("label_x", 1) * scale
                    ly = oy - c["fn"](c.get("label_x", 1)) * scale - 12
                    svg_elements.append(f'<text x="{lx}" y="{ly}" fill="{color}" font-size="11" font-weight="600">{c["label"]}</text>')

    # Lines
    if lines:
        for l in lines:
            x1, y1 = l["p1"]
            x2, y2 = l["p2"]
            color = l.get("color", "#2563EB")
            sw = l.get("stroke_width", 2.0)
            dash = f'stroke-dasharray="{l["dash"]}"' if "dash" in l else ""
            px1, py1 = ox + x1 * scale, oy - y1 * scale
            px2, py2 = ox + x2 * scale, oy - y2 * scale
            svg_elements.append(f'<line x1="{px1}" y1="{py1}" x2="{px2}" y2="{py2}" stroke="{color}" stroke-width="{sw}" {dash}/>')
            if "label" in l:
                mid_x, mid_y = (px1 + px2) / 2, (py1 + py2) / 2
                svg_elements.append(f'<text x="{mid_x + 8}" y="{mid_y - 6}" fill="{color}" font-size="11" font-weight="600">{l["label"]}</text>')

    # Points
    if points:
        for p in points:
            px = ox + p["x"] * scale
            py = oy - p["y"] * scale
            color = p.get("color", "#2563EB")
            svg_elements.append(f'<circle cx="{px}" cy="{py}" r="4.5" fill="{color}" stroke="#FFFFFF" stroke-width="1.5"/>')
            if "label" in p:
                svg_elements.append(f'<text x="{px + 7}" y="{py - 6}" fill="{color}" font-size="11" font-weight="700">{p["label"]}</text>')

    return get_svg_wrapper("\n".join(svg_elements), title=title, caption=caption, width=width, height=height)


def build_ap_increments_svg(a=2, d=3, n=5, title="Arithmetic Progression: Staircase of Increments", caption="Showing first term a, common difference d, and nth term an = a + (n-1)d"):
    """
    Renders an Arithmetic Progression step-ladder staircase showing constant difference d increments
    and cumulative sum area block decomposition.
    """
    elements = []
    base_x = 80
    base_y = 280
    step_width = 75
    unit_height = 14
    
    terms = [a + i * d for i in range(n)]
    
    # Draw base line
    elements.append(f'<line x1="60" y1="{base_y}" x2="{base_x + n * step_width + 40}" y2="{base_y}" stroke="#334155" stroke-width="2"/>')
    
    for i, val in enumerate(terms):
        sx = base_x + i * step_width
        sh = val * unit_height
        sy = base_y - sh
        
        # Base rectangle for term
        fill_color = "#EFF6FF" if i % 2 == 0 else "#DBEAFE"
        elements.append(f'<rect x="{sx}" y="{sy}" width="{step_width - 8}" height="{sh}" fill="{fill_color}" stroke="#2563EB" stroke-width="1.8" rx="4"/>')
        
        # Term label at bottom
        elements.append(f'<text x="{sx + (step_width - 8)/2}" y="{base_y + 18}" fill="#0F172A" font-size="11" font-weight="700" text-anchor="middle">a{i+1}</text>')
        # Value label inside column
        elements.append(f'<text x="{sx + (step_width - 8)/2}" y="{sy - 8}" fill="#1D4ED8" font-size="12" font-weight="700" text-anchor="middle">{val}</text>')
        
        # Highlight common difference d between adjacent columns
        if i > 0:
            prev_sy = base_y - terms[i-1] * unit_height
            dh = d * unit_height
            elements.append(f'<line x1="{sx - 8}" y1="{prev_sy}" x2="{sx}" y2="{prev_sy}" stroke="#DC2626" stroke-width="1.2" stroke-dasharray="3,3"/>')
            elements.append(f'<line x1="{sx - 4}" y1="{prev_sy}" x2="{sx - 4}" y2="{sy}" stroke="#DC2626" stroke-width="1.5" marker-end="url(#arrowRed)"/>')
            elements.append(f'<text x="{sx - 14}" y="{(prev_sy + sy)/2 + 4}" fill="#DC2626" font-size="10" font-weight="700">+{d}</text>')

    # Formula HUD Card
    hud = f"""
    <g transform="translate(320, 80)">
      <rect width="220" height="90" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5" rx="8"/>
      <text x="14" y="24" fill="#0F172A" font-size="12" font-weight="700">Governing AP Formulas:</text>
      <text x="14" y="46" fill="#2563EB" font-size="11" font-weight="600">nth Term: an = a + (n - 1)d</text>
      <text x="14" y="66" fill="#16A34A" font-size="11" font-weight="600">Sum: Sn = n/2 [2a + (n - 1)d]</text>
      <text x="14" y="82" fill="#64748B" font-size="10">First term a = {a} | Common diff d = {d}</text>
    </g>
    """
    elements.append(hud)
    return get_svg_wrapper("\n".join(elements), title=title, caption=caption)


def build_similar_triangles_bpt_svg(variant="bpt", title="", caption=""):
    """
    Renders Thales Theorem (Basic Proportionality Theorem / BPT) or Similar Triangles with proof lines.
    """
    elements = []
    
    if variant == "bpt":
        # Triangle ABC with DE || BC and altitudes EN perpendicular to AB, DM perpendicular to AC
        A = (290, 80)
        B = (150, 290)
        C = (430, 290)
        D = (220, 185)
        E = (360, 185)
        
        # Main Triangle ABC
        elements.append(f'<polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}" fill="#F8FAFC" stroke="#0F172A" stroke-width="2"/>')
        
        # Parallel line DE
        elements.append(f'<line x1="{D[0]}" y1="{D[1]}" x2="{E[0]}" y2="{E[1]}" stroke="#2563EB" stroke-width="2.2"/>')
        # Arrows indicating parallel DE || BC
        elements.append(f'<path d="M 285 181 L 295 185 L 285 189" fill="none" stroke="#2563EB" stroke-width="1.8"/>')
        elements.append(f'<path d="M 285 286 L 295 290 L 285 294" fill="none" stroke="#0F172A" stroke-width="1.8"/>')
        
        # Construction lines BE and CD (dashed red)
        elements.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{E[0]}" y2="{E[1]}" stroke="#DC2626" stroke-width="1.2" stroke-dasharray="4,4"/>')
        elements.append(f'<line x1="{C[0]}" y1="{C[1]}" x2="{D[0]}" y2="{D[1]}" stroke="#DC2626" stroke-width="1.2" stroke-dasharray="4,4"/>')
        
        # Altitudes EN perp AB and DM perp AC (dashed green)
        elements.append(f'<line x1="{E[0]}" y1="{E[1]}" x2="238" y2="157" stroke="#16A34A" stroke-width="1.2" stroke-dasharray="3,3"/>')
        elements.append(f'<line x1="{D[0]}" y1="{D[1]}" x2="342" y2="157" stroke="#16A34A" stroke-width="1.2" stroke-dasharray="3,3"/>')
        
        # Vertex Labels
        labels = [
            (A[0], A[1] - 10, "A"), (B[0] - 16, B[1] + 6, "B"), (C[0] + 10, C[1] + 6, "C"),
            (D[0] - 16, D[1] - 2, "D"), (E[0] + 8, E[1] - 2, "E")
        ]
        for lx, ly, txt in labels:
            elements.append(f'<text x="{lx}" y="{ly}" fill="#0F172A" font-size="13" font-weight="700">{txt}</text>')
            
        # Thales Theorem Callout
        callout = """
        <g transform="translate(30, 80)">
          <rect width="135" height="74" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.2" rx="6"/>
          <text x="10" y="20" fill="#1E40AF" font-size="11" font-weight="700">Theorem 6.1 (BPT):</text>
          <text x="10" y="38" fill="#0F172A" font-size="11">If DE || BC, then:</text>
          <text x="10" y="58" fill="#2563EB" font-size="12" font-weight="700">AD/DB = AE/EC</text>
        </g>
        """
        elements.append(callout)
        
    return get_svg_wrapper("\n".join(elements), title=title or "Theorem 6.1: Basic Proportionality Theorem (Thales)", caption=caption or "A line drawn parallel to one side of a triangle divides the other two sides in the same ratio")


def build_circle_tangents_svg(variant="external_tangents", title="", caption=""):
    """
    Renders Theorem 10.1 (Radius perp Tangent) or Theorem 10.2 (Lengths of Tangents from External Point).
    """
    elements = []
    
    if variant == "external_tangents":
        # Circle at (320, 200), radius 80. External point P at (100, 200).
        O = (330, 195)
        P = (110, 195)
        r = 85
        
        # Distance OP = 220. Angle = arcsin(r / OP) = arcsin(85 / 220) = 22.7 degrees = 0.396 rad
        d = 220
        ang = math.asin(r / d)
        
        # Tangency points A and B
        Ax = O[0] - r * math.sin(ang)
        Ay = O[1] - r * math.cos(ang)
        Bx = O[0] - r * math.sin(ang)
        By = O[1] + r * math.cos(ang)
        
        # Circle
        elements.append(f'<circle cx="{O[0]}" cy="{O[1]}" r="{r}" fill="#F8FAFC" stroke="#0F172A" stroke-width="2"/>')
        elements.append(f'<circle cx="{O[0]}" cy="{O[1]}" r="3" fill="#0F172A"/>')
        elements.append(f'<text x="{O[0] + 8}" y="{O[1] + 4}" fill="#0F172A" font-size="12" font-weight="700">O</text>')
        
        # Radii OA and OB (green)
        elements.append(f'<line x1="{O[0]}" y1="{O[1]}" x2="{Ax}" y2="{Ay}" stroke="#16A34A" stroke-width="1.8"/>')
        elements.append(f'<line x1="{O[0]}" y1="{O[1]}" x2="{Bx}" y2="{By}" stroke="#16A34A" stroke-width="1.8"/>')
        elements.append(f'<text x="{(O[0]+Ax)/2 + 8}" y="{(O[1]+Ay)/2}" fill="#16A34A" font-size="11" font-weight="600">r</text>')
        elements.append(f'<text x="{(O[0]+Bx)/2 + 8}" y="{(O[1]+By)/2 + 8}" fill="#16A34A" font-size="11" font-weight="600">r</text>')
        
        # Tangents PA and PB (royal blue)
        elements.append(f'<line x1="{P[0]}" y1="{P[1]}" x2="{Ax}" y2="{Ay}" stroke="#2563EB" stroke-width="2.2"/>')
        elements.append(f'<line x1="{P[0]}" y1="{P[1]}" x2="{Bx}" y2="{By}" stroke="#2563EB" stroke-width="2.2"/>')
        
        # Secant line OP (dashed slate)
        elements.append(f'<line x1="{P[0]}" y1="{P[1]}" x2="{O[0]}" y2="{O[1]}" stroke="#64748B" stroke-width="1.4" stroke-dasharray="4,4"/>')
        
        # Right angle boxes at A and B (since radius perp tangent)
        elements.append(f'<circle cx="{Ax}" cy="{Ay}" r="3.5" fill="#2563EB"/>')
        elements.append(f'<circle cx="{Bx}" cy="{By}" r="3.5" fill="#2563EB"/>')
        elements.append(f'<circle cx="{P[0]}" cy="{P[1]}" r="4" fill="#0F172A"/>')
        
        # Labels
        elements.append(f'<text x="{P[0] - 18}" y="{P[1] + 4}" fill="#0F172A" font-size="13" font-weight="700">P</text>')
        elements.append(f'<text x="{Ax - 6}" y="{Ay - 8}" fill="#0F172A" font-size="13" font-weight="700">A</text>')
        elements.append(f'<text x="{Bx - 6}" y="{By + 18}" fill="#0F172A" font-size="13" font-weight="700">B</text>')
        
        # Theorem 10.2 Proof Card
        card = """
        <g transform="translate(30, 60)">
          <rect width="190" height="92" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.2" rx="6"/>
          <text x="10" y="20" fill="#166534" font-size="11" font-weight="700">Theorem 10.2 (Tangent Equality):</text>
          <text x="10" y="38" fill="#0F172A" font-size="11">ΔOPA ≅ ΔOPB (by RHS)</text>
          <text x="10" y="56" fill="#0F172A" font-size="11">Radius ⊥ Tangent: ∠OAP = 90°</text>
          <text x="10" y="78" fill="#16A34A" font-size="13" font-weight="700">PA = PB</text>
        </g>
        """
        elements.append(card)
        
    elif variant == "radius_perp_tangent":
        # Theorem 10.1: Tangent line with radius perpendicular
        O = (290, 160)
        r = 90
        P = (290, 250)
        elements.append(f'<circle cx="{O[0]}" cy="{O[1]}" r="{r}" fill="#F8FAFC" stroke="#0F172A" stroke-width="2"/>')
        elements.append(f'<line x1="120" y1="250" x2="460" y2="250" stroke="#2563EB" stroke-width="2.2"/>')
        elements.append(f'<line x1="{O[0]}" y1="{O[1]}" x2="{P[0]}" y2="{P[1]}" stroke="#16A34A" stroke-width="2"/>')
        elements.append(f'<rect x="290" y="235" width="15" height="15" fill="none" stroke="#DC2626" stroke-width="1.2"/>')
        elements.append(f'<circle cx="{O[0]}" cy="{O[1]}" r="3" fill="#0F172A"/>')
        elements.append(f'<circle cx="{P[0]}" cy="{P[1]}" r="3.5" fill="#2563EB"/>')
        elements.append(f'<text x="{O[0] + 8}" y="{O[1] - 4}" fill="#0F172A" font-size="12" font-weight="700">O</text>')
        elements.append(f'<text x="{P[0] + 6}" y="{P[1] + 18}" fill="#0F172A" font-size="12" font-weight="700">P (Point of Contact)</text>')
        elements.append(f'<text x="450" y="242" fill="#2563EB" font-size="12" font-weight="700">Tangent line</text>')
        
    return get_svg_wrapper("\n".join(elements), title=title or "Circle Tangent Theorem", caption=caption or "Theorem: Tangents drawn from an external point to a circle are equal in length")


def build_trigonometry_right_triangle_svg(angle_label="θ", opp_label="Opposite (Perpendicular)", adj_label="Adjacent (Base)", hyp_label="Hypotenuse", title="", caption=""):
    """
    Renders standard right-angled triangle with clear trigonometric definitions and HUD.
    """
    elements = []
    
    A = (120, 270)
    B = (340, 270)
    C = (340, 110)
    
    # Triangle ABC
    elements.append(f'<polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}" fill="#EFF6FF" stroke="#0F172A" stroke-width="2"/>')
    
    # Right angle square at B
    elements.append(f'<rect x="{B[0]-16}" y="{B[1]-16}" width="16" height="16" fill="none" stroke="#DC2626" stroke-width="1.5"/>')
    
    # Angle arc at A
    elements.append(f'<path d="M 160 270 A 40 40 0 0 0 152 245" fill="none" stroke="#2563EB" stroke-width="2"/>')
    elements.append(f'<text x="170" y="260" fill="#2563EB" font-size="13" font-weight="700">{angle_label}</text>')
    
    # Side labels
    elements.append(f'<text x="{(A[0]+B[0])/2}" y="{B[1] + 20}" fill="#0F172A" font-size="11" font-weight="600" text-anchor="middle">{adj_label}</text>')
    elements.append(f'<text x="{B[0] + 12}" y="{(B[1]+C[1])/2 + 4}" fill="#0F172A" font-size="11" font-weight="600">{opp_label}</text>')
    elements.append(f'<text x="{(A[0]+C[0])/2 - 18}" y="{(A[1]+C[1])/2 - 10}" fill="#2563EB" font-size="11" font-weight="700">{hyp_label}</text>')
    
    # Vertices
    elements.append(f'<text x="{A[0] - 16}" y="{A[1] + 6}" fill="#0F172A" font-size="13" font-weight="700">A</text>')
    elements.append(f'<text x="{B[0] + 6}" y="{B[1] + 18}" fill="#0F172A" font-size="13" font-weight="700">B (90°)</text>')
    elements.append(f'<text x="{C[0] + 6}" y="{C[1] - 4}" fill="#0F172A" font-size="13" font-weight="700">C</text>')
    
    # Trigonometric Ratios HUD Card
    hud = f"""
    <g transform="translate(390, 80)">
      <rect width="165" height="160" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2" rx="8"/>
      <text x="12" y="22" fill="#0F172A" font-size="11" font-weight="700">Six Trigonometric Ratios:</text>
      <text x="12" y="44" fill="#2563EB" font-size="11">sin {angle_label} = Opp / Hyp</text>
      <text x="12" y="64" fill="#2563EB" font-size="11">cos {angle_label} = Adj / Hyp</text>
      <text x="12" y="84" fill="#2563EB" font-size="11">tan {angle_label} = Opp / Adj</text>
      <line x1="12" y1="94" x2="153" y2="94" stroke="#E2E8F0" stroke-width="1"/>
      <text x="12" y="112" fill="#64748B" font-size="10">cosec {angle_label} = 1 / sin {angle_label}</text>
      <text x="12" y="130" fill="#64748B" font-size="10">sec {angle_label} = 1 / cos {angle_label}</text>
      <text x="12" y="148" fill="#64748B" font-size="10">cot {angle_label} = 1 / tan {angle_label}</text>
    </g>
    """
    elements.append(hud)
    return get_svg_wrapper("\n".join(elements), title=title or "Right-Angled Triangle Trigonometry", caption=caption or "Definition of six trigonometric ratios with respect to reference angle")


def build_heights_and_distances_svg(type_prob="elevation", h_label="h", d_label="d", ang_label="30°", title="", caption=""):
    """
    Renders authentic Application of Trigonometry diagrams (Angle of Elevation & Depression).
    """
    elements = []
    
    # Ground line
    elements.append('<line x1="60" y1="280" x2="520" y2="280" stroke="#334155" stroke-width="2"/>')
    elements.append('<text x="500" y="300" fill="#64748B" font-size="11">Ground</text>')
    
    # Vertical Tower/Building at x=400, base y=280, top y=100
    elements.append('<rect x="390" y="100" width="20" height="180" fill="#E2E8F0" stroke="#334155" stroke-width="1.8"/>')
    elements.append(f'<text x="420" y="190" fill="#0F172A" font-size="12" font-weight="700">Height {h_label}</text>')
    elements.append('<rect x="375" y="265" width="15" height="15" fill="none" stroke="#DC2626" stroke-width="1.2"/>')
    
    # Observer Point at x=140, y=280
    elements.append('<circle cx="140" cy="280" r="4" fill="#2563EB"/>')
    elements.append('<text x="130" y="300" fill="#0F172A" font-size="12" font-weight="700">Observer (O)</text>')
    
    # Line of Sight (Observer to Top of Tower)
    elements.append('<line x1="140" y1="280" x2="390" y2="100" stroke="#2563EB" stroke-width="2.2"/>')
    elements.append('<text x="230" y="180" fill="#2563EB" font-size="11" font-weight="600">Line of Sight</text>')
    
    # Distance line between Observer and Tower
    elements.append(f'<line x1="140" y1="315" x2="390" y2="315" stroke="#475569" stroke-width="1.5" marker-start="url(#arrowSlate)" marker-end="url(#arrowSlate)"/>')
    elements.append(f'<text x="265" y="330" fill="#475569" font-size="12" font-weight="600" text-anchor="middle">Distance {d_label}</text>')
    
    # Angle of Elevation Arc
    elements.append('<path d="M 180 280 A 40 40 0 0 0 175 256" fill="none" stroke="#DC2626" stroke-width="1.8"/>')
    elements.append(f'<text x="190" y="272" fill="#DC2626" font-size="12" font-weight="700">{ang_label}</text>')
    elements.append('<text x="180" y="240" fill="#DC2626" font-size="10">Angle of Elevation</text>')
    
    return get_svg_wrapper("\n".join(elements), title=title or "Trigonometric Heights & Distances", caption=caption or "Visualizing Angle of Elevation from observer to top of vertical tower")


def build_circle_sector_segment_svg(radius=90, theta_deg=60, title="", caption=""):
    """
    Renders Circle Sector and Segment area with clean shaded geometric slices.
    """
    elements = []
    O = (280, 190)
    r = radius
    
    # Angles
    ang_rad = math.radians(theta_deg)
    start_rad = -ang_rad / 2
    end_rad = ang_rad / 2
    
    Ax = O[0] + r * math.cos(start_rad)
    Ay = O[1] + r * math.sin(start_rad)
    Bx = O[0] + r * math.cos(end_rad)
    By = O[1] + r * math.sin(end_rad)
    
    # Full Circle
    elements.append(f'<circle cx="{O[0]}" cy="{O[1]}" r="{r}" fill="#F8FAFC" stroke="#94A3B8" stroke-width="1.5"/>')
    
    # Shaded Minor Sector
    sector_path = f"M {O[0]} {O[1]} L {Ax} {Ay} A {r} {r} 0 0 1 {Bx} {By} Z"
    elements.append(f'<path d="{sector_path}" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>')
    
    # Chord AB creating segment
    elements.append(f'<line x1="{Ax}" y1="{Ay}" x2="{Bx}" y2="{By}" stroke="#DC2626" stroke-width="1.8"/>')
    
    # Central Angle Arc
    elements.append(f'<path d="M {O[0] + 35*math.cos(start_rad)} {O[1] + 35*math.sin(start_rad)} A 35 35 0 0 1 {O[0] + 35*math.cos(end_rad)} {O[1] + 35*math.sin(end_rad)}" fill="none" stroke="#2563EB" stroke-width="1.8"/>')
    elements.append(f'<text x="{O[0] + 45}" y="{O[1] + 4}" fill="#2563EB" font-size="11" font-weight="700">θ = {theta_deg}°</text>')
    
    # Points
    elements.append(f'<circle cx="{O[0]}" cy="{O[1]}" r="3" fill="#0F172A"/>')
    elements.append(f'<circle cx="{Ax}" cy="{Ay}" r="3" fill="#2563EB"/>')
    elements.append(f'<circle cx="{Bx}" cy="{By}" r="3" fill="#2563EB"/>')
    elements.append(f'<text x="{O[0] - 16}" y="{O[1] + 4}" fill="#0F172A" font-size="12" font-weight="700">O</text>')
    elements.append(f'<text x="{Ax + 8}" y="{Ay}" fill="#0F172A" font-size="12" font-weight="700">A</text>')
    elements.append(f'<text x="{Bx + 8}" y="{By + 6}" fill="#0F172A" font-size="12" font-weight="700">B</text>')
    
    # Formula Card
    card = f"""
    <g transform="translate(390, 80)">
      <rect width="165" height="135" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2" rx="8"/>
      <text x="12" y="22" fill="#0F172A" font-size="11" font-weight="700">Sector & Segment Formulas:</text>
      <text x="12" y="44" fill="#2563EB" font-size="11">Arc Length = (θ/360)·2πr</text>
      <text x="12" y="68" fill="#2563EB" font-size="11">Area of Sector = (θ/360)·πr²</text>
      <text x="12" y="92" fill="#DC2626" font-size="11">Area of Segment =</text>
      <text x="12" y="110" fill="#DC2626" font-size="10">Area(Sector) - Area(ΔOAB)</text>
      <text x="12" y="126" fill="#64748B" font-size="9">Radius r = {radius} units</text>
    </g>
    """
    elements.append(card)
    return get_svg_wrapper("\n".join(elements), title=title or "Areas Related to Circles: Sector & Segment", caption=caption or f"Shaded minor sector with central angle θ = {theta_deg}° and minor segment enclosed by chord AB")


def build_surface_areas_volumes_3d_svg(shape_type="cylinder_cone", title="", caption=""):
    """
    Renders 30° axonometric Hairline isometric illustrations for combinations of 3D solids.
    """
    elements = []
    
    if shape_type == "cylinder_cone":
        # Combination: Cylinder surmounted by a Cone (Toy/Circus tent)
        cx = 240
        base_y = 270
        cyl_h = 100
        cone_h = 80
        rx = 80
        ry = 26
        
        # Base of cylinder (ellipse)
        elements.append(f'<ellipse cx="{cx}" cy="{base_y}" rx="{rx}" ry="{ry}" fill="#F1F5F9" stroke="#334155" stroke-width="1.8"/>')
        # Cylinder body
        elements.append(f'<path d="M {cx - rx} {base_y} L {cx - rx} {base_y - cyl_h} A {rx} {ry} 0 0 0 {cx + rx} {base_y - cyl_h} L {cx + rx} {base_y} A {rx} {ry} 0 0 1 {cx - rx} {base_y}" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.8"/>')
        # Cylinder top / Cone base interface (ellipse)
        elements.append(f'<ellipse cx="{cx}" cy="{base_y - cyl_h}" rx="{rx}" ry="{ry}" fill="#DBEAFE" stroke="#2563EB" stroke-width="1.5"/>')
        # Cone top
        apex_y = base_y - cyl_h - cone_h
        elements.append(f'<polygon points="{cx - rx},{base_y - cyl_h} {cx},{apex_y} {cx + rx},{base_y - cyl_h}" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.8"/>')
        
        # Dimension lines
        elements.append(f'<line x1="{cx}" y1="{base_y - cyl_h}" x2="{cx + rx}" y2="{base_y - cyl_h}" stroke="#16A34A" stroke-width="1.5"/>')
        elements.append(f'<text x="{cx + 35}" y="{base_y - cyl_h - 6}" fill="#16A34A" font-size="11" font-weight="700">Radius r</text>')
        
        elements.append(f'<line x1="{cx + rx + 20}" y1="{base_y}" x2="{cx + rx + 20}" y2="{base_y - cyl_h}" stroke="#475569" stroke-width="1.2" marker-start="url(#arrowSlate)" marker-end="url(#arrowSlate)"/>')
        elements.append(f'<text x="{cx + rx + 28}" y="{base_y - cyl_h/2 + 4}" fill="#475569" font-size="11">Cylinder h1</text>')
        
        elements.append(f'<line x1="{cx + rx + 20}" y1="{base_y - cyl_h}" x2="{cx + rx + 20}" y2="{apex_y}" stroke="#475569" stroke-width="1.2" marker-start="url(#arrowSlate)" marker-end="url(#arrowSlate)"/>')
        elements.append(f'<text x="{cx + rx + 28}" y="{apex_y + cone_h/2 + 4}" fill="#475569" font-size="11">Cone h2</text>')
        
        # Formulas Card
        card = """
        <g transform="translate(370, 70)">
          <rect width="185" height="150" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2" rx="8"/>
          <text x="12" y="22" fill="#0F172A" font-size="11" font-weight="700">Combination of Solids:</text>
          <text x="12" y="44" fill="#0284C7" font-size="11">Cone CSA = πrl</text>
          <text x="12" y="60" fill="#64748B" font-size="10">where l = √(r² + h2²)</text>
          <text x="12" y="80" fill="#2563EB" font-size="11">Cylinder CSA = 2πrh1</text>
          <text x="12" y="100" fill="#16A34A" font-size="11">Base Area = πr²</text>
          <line x1="12" y1="110" x2="173" y2="110" stroke="#E2E8F0" stroke-width="1"/>
          <text x="12" y="128" fill="#0F172A" font-size="11" font-weight="700">Total Surface Area =</text>
          <text x="12" y="142" fill="#0F172A" font-size="10">πrl + 2πrh1 + πr²</text>
        </g>
        """
        elements.append(card)
        
    return get_svg_wrapper("\n".join(elements), title=title or "Combination of Solids: Cone on Cylinder", caption=caption or "Calculates total surface area and volume of combined 3D shapes")


def build_real_numbers_factor_tree_svg(number=32760, factors=None, title="", caption=""):
    """
    Renders prime factor tree decomposition showing composite nodes and prime leaves.
    """
    elements = []
    # Standard factor tree for 32760 or any number
    nodes = [
        {"x": 280, "y": 80, "val": 32760, "is_prime": False},
        {"x": 190, "y": 130, "val": 2, "is_prime": True},
        {"x": 370, "y": 130, "val": 16380, "is_prime": False},
        {"x": 300, "y": 180, "val": 2, "is_prime": True},
        {"x": 440, "y": 180, "val": 8190, "is_prime": False},
        {"x": 380, "y": 230, "val": 2, "is_prime": True},
        {"x": 490, "y": 230, "val": 4095, "is_prime": False},
        {"x": 440, "y": 280, "val": 3, "is_prime": True},
        {"x": 520, "y": 280, "val": 1365, "is_prime": False},
    ]
    # Draw branches
    branches = [(0, 1), (0, 2), (2, 3), (2, 4), (4, 5), (4, 6), (6, 7), (6, 8)]
    for p, c in branches:
        n1, n2 = nodes[p], nodes[c]
        elements.append(f'<line x1="{n1["x"]}" y1="{n1["y"]}" x2="{n2["x"]}" y2="{n2["y"]}" stroke="#94A3B8" stroke-width="1.5"/>')
        
    for n in nodes:
        fill = "#EFF6FF" if n["is_prime"] else "#F8FAFC"
        stroke = "#2563EB" if n["is_prime"] else "#475569"
        rx = 22 if n["is_prime"] else 28
        elements.append(f'<ellipse cx="{n["x"]}" cy="{n["y"]}" rx="{rx}" ry="16" fill="{fill}" stroke="{stroke}" stroke-width="1.8"/>')
        elements.append(f'<text x="{n["x"]}" y="{n["y"] + 4}" fill="#0F172A" font-size="11" font-weight="700" text-anchor="middle">{n["val"]}</text>')
        
    # Card
    card = """
    <g transform="translate(30, 80)">
      <rect width="150" height="100" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.2" rx="8"/>
      <text x="10" y="20" fill="#166534" font-size="11" font-weight="700">Fundamental Theorem:</text>
      <text x="10" y="38" fill="#0F172A" font-size="10">Every composite number</text>
      <text x="10" y="52" fill="#0F172A" font-size="10">is uniquely factored into</text>
      <text x="10" y="66" fill="#0F172A" font-size="10">prime powers:</text>
      <text x="10" y="88" fill="#2563EB" font-size="11" font-weight="700">32760 = 2³ × 3² × 5 × 7 × 13</text>
    </g>
    """
    elements.append(card)
    return get_svg_wrapper("\n".join(elements), title=title or "Fundamental Theorem of Arithmetic: Prime Factor Tree", caption=caption or "Unique prime decomposition of composite numbers apart from order")


def build_statistics_chart_svg(chart_type="ogive", title="", caption=""):
    """
    Renders clean statistical charts for Class 10:
    - 'ogive': Less-than and More-than cumulative frequency curves intersecting at Median
    - 'histogram_mode': Grouped frequency distribution highlighting Modal Class and calculation
    """
    elements = []
    width, height = 580, 360
    
    if chart_type == "ogive":
        # Cumulative frequency curves intersecting at median
        # Axes
        ox, oy = 70, 290
        elements.append(f'<line x1="{ox}" y1="{oy}" x2="520" y2="{oy}" stroke="#334155" stroke-width="1.8" marker-end="url(#arrowSlate)"/>')
        elements.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="60" stroke="#334155" stroke-width="1.8" marker-end="url(#arrowSlate)"/>')
        elements.append(f'<text x="525" y="{oy+4}" fill="#0F172A" font-size="11" font-weight="700">Upper/Lower Limits</text>')
        elements.append(f'<text x="{ox}" y="50" fill="#0F172A" font-size="11" font-weight="700" text-anchor="middle">Cumulative Frequency (cf)</text>')
        
        # Grid ticks
        for i in range(1, 6):
            gx = ox + i * 80
            elements.append(f'<line x1="{gx}" y1="{oy}" x2="{gx}" y2="70" stroke="#F1F5F9" stroke-width="1"/>')
            elements.append(f'<text x="{gx}" y="{oy+16}" fill="#64748B" font-size="10" text-anchor="middle">{i*20}</text>')
            gy = oy - i * 40
            elements.append(f'<line x1="{ox}" y1="{gy}" x2="490" y2="{gy}" stroke="#F1F5F9" stroke-width="1"/>')
            elements.append(f'<text x="{ox-8}" y="{gy+4}" fill="#64748B" font-size="10" text-anchor="end">{i*10}</text>')
            
        # Less-than curve (rising S-curve) in blue
        less_pts = [(ox, oy), (ox+80, oy-15), (ox+160, oy-45), (ox+240, oy-100), (ox+320, oy-160), (ox+400, oy-190)]
        d_less = "M " + " ".join([f"{x},{y}" for x, y in less_pts])
        elements.append(f'<path d="{d_less}" fill="none" stroke="#2563EB" stroke-width="2.5"/>')
        for x, y in less_pts:
            elements.append(f'<circle cx="{x}" cy="{y}" r="3.5" fill="#2563EB"/>')
        elements.append(f'<text x="360" y="110" fill="#2563EB" font-size="11" font-weight="700">"Less than" Ogive</text>')
        
        # More-than curve (falling S-curve) in green
        more_pts = [(ox, oy-200), (ox+80, oy-185), (ox+160, oy-150), (ox+240, oy-100), (ox+320, oy-40), (ox+400, oy)]
        d_more = "M " + " ".join([f"{x},{y}" for x, y in more_pts])
        elements.append(f'<path d="{d_more}" fill="none" stroke="#16A34A" stroke-width="2.5"/>')
        for x, y in more_pts:
            elements.append(f'<circle cx="{x}" cy="{y}" r="3.5" fill="#16A34A"/>')
        elements.append(f'<text x="110" y="110" fill="#16A34A" font-size="11" font-weight="700">"More than" Ogive</text>')
        
        # Intersection at Median (N/2 = 25, Median = 60)
        ix, iy = ox + 240, oy - 100
        elements.append(f'<circle cx="{ix}" cy="{iy}" r="6" fill="#DC2626" stroke="#FFFFFF" stroke-width="2"/>')
        elements.append(f'<line x1="{ix}" y1="{iy}" x2="{ix}" y2="{oy}" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="4,4"/>')
        elements.append(f'<line x1="{ix}" y1="{iy}" x2="{ox}" y2="{iy}" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="4,4"/>')
        elements.append(f'<text x="{ix}" y="{oy+18}" fill="#DC2626" font-size="11" font-weight="700" text-anchor="middle">Median ≈ 60</text>')
        elements.append(f'<text x="{ox-8}" y="{iy+4}" fill="#DC2626" font-size="11" font-weight="700" text-anchor="end">N/2 = 25</text>')
        
        # Formula card
        card = """
        <g transform="translate(370, 70)">
          <rect width="180" height="90" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.2" rx="8"/>
          <text x="12" y="22" fill="#0F172A" font-size="11" font-weight="700">Median from Ogives:</text>
          <text x="12" y="40" fill="#334155" font-size="10">• Point of Intersection = (Median, N/2)</text>
          <text x="12" y="58" fill="#334155" font-size="10">• Empirical Formula:</text>
          <text x="12" y="76" fill="#2563EB" font-size="11" font-weight="700">3 Median = Mode + 2 Mean</text>
        </g>
        """
        elements.append(card)
        return get_svg_wrapper("\n".join(elements), title=title or "Statistics: Dual Cumulative Frequency Ogives", caption=caption or "Intersection point of less-than and more-than ogives yields the exact median on the x-axis")
    else:
        # Histogram with modal class
        ox, oy = 60, 290
        elements.append(f'<line x1="{ox}" y1="{oy}" x2="520" y2="{oy}" stroke="#334155" stroke-width="1.8"/>')
        elements.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="60" stroke="#334155" stroke-width="1.8"/>')
        
        bars = [
            {"label": "0-10", "f": 4, "h": 50},
            {"label": "10-20", "f": 8, "h": 100},
            {"label": "20-30", "f": 18, "h": 190, "modal": True},
            {"label": "30-40", "f": 10, "h": 120},
            {"label": "40-50", "f": 5, "h": 65},
        ]
        bw = 65
        for i, b in enumerate(bars):
            bx = ox + 20 + i * bw
            by = oy - b["h"]
            fill = "#DBEAFE" if b.get("modal") else "#F1F5F9"
            stroke = "#2563EB" if b.get("modal") else "#94A3B8"
            elements.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{b["h"]}" fill="{fill}" stroke="{stroke}" stroke-width="1.8"/>')
            elements.append(f'<text x="{bx + bw/2}" y="{by - 6}" fill="{stroke}" font-size="11" font-weight="700" text-anchor="middle">f = {b["f"]}</text>')
            elements.append(f'<text x="{bx + bw/2}" y="{oy + 16}" fill="#64748B" font-size="10" text-anchor="middle">{b["label"]}</text>')
            
        elements.append("""
        <g transform="translate(400, 70)">
          <rect width="160" height="110" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.2" rx="8"/>
          <text x="12" y="22" fill="#1E40AF" font-size="11" font-weight="700">Mode of Grouped Data:</text>
          <text x="12" y="44" fill="#0F172A" font-size="10">Mode = l + [ (f₁ - f₀) / </text>
          <text x="12" y="58" fill="#0F172A" font-size="10">       (2f₁ - f₀ - f₂) ] × h</text>
          <text x="12" y="80" fill="#166534" font-size="10">l = 20, f₁ = 18, f₀ = 8,</text>
          <text x="12" y="96" fill="#166534" font-size="10">f₂ = 10, h = 10</text>
        </g>
        """)
        return get_svg_wrapper("\n".join(elements), title=title or "Statistics: Histogram and Modal Class Identification", caption=caption or "Visual identification of maximum frequency modal class for grouped distribution")


def build_probability_svg(variant="dice_grid", title="", caption=""):
    """
    Renders clean probability visual structures:
    - 'dice_grid': 6x6 outcomes table (36 pairs) with diagonal sum highlights
    - 'cards_deck': 52 playing cards breakdown (Suits, Colors, Face cards)
    - 'coin_tree': 3-coin toss binary decision tree with 8 outcomes
    """
    elements = []
    width, height = 580, 360
    
    if variant == "dice_grid":
        # 6x6 matrix of dice rolls (Die 1 vs Die 2)
        ox, oy = 80, 80
        cell_size = 38
        
        elements.append(f'<text x="{ox - 30}" y="{oy + 115}" fill="#2563EB" font-size="12" font-weight="700" transform="rotate(-90 {ox-30},{oy+115})" text-anchor="middle">Die 1 (Red)</text>')
        elements.append(f'<text x="{ox + 114}" y="{oy - 25}" fill="#16A34A" font-size="12" font-weight="700" text-anchor="middle">Die 2 (Green)</text>')
        
        for r in range(1, 7):
            for c in range(1, 7):
                cx = ox + (c - 1) * cell_size
                cy = oy + (r - 1) * cell_size
                val_sum = r + c
                # Highlight diagonal sum = 7 in soft blue, sum = 8 in soft green, doubles in amber
                is_sum_7 = (val_sum == 7)
                is_double = (r == c)
                fill = "#EFF6FF" if is_sum_7 else "#FEF3C7" if is_double else "#FFFFFF"
                stroke = "#2563EB" if is_sum_7 else "#D97706" if is_double else "#E2E8F0"
                elements.append(f'<rect x="{cx}" y="{cy}" width="{cell_size}" height="{cell_size}" fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
                elements.append(f'<text x="{cx + cell_size/2}" y="{cy + 24}" fill="#0F172A" font-size="10" font-weight="600" text-anchor="middle">({r},{c})</text>')
                
        # Legend card
        card = """
        <g transform="translate(330, 80)">
          <rect width="220" height="210" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.2" rx="8"/>
          <text x="14" y="24" fill="#0F172A" font-size="12" font-weight="700">Pair of Dice: n(S) = 36</text>
          
          <rect x="14" y="38" width="14" height="14" fill="#EFF6FF" stroke="#2563EB" rx="3"/>
          <text x="36" y="50" fill="#1E40AF" font-size="10" font-weight="600">Sum = 7 (6 outcomes): P = 6/36 = 1/6</text>
          
          <rect x="14" y="62" width="14" height="14" fill="#FEF3C7" stroke="#D97706" rx="3"/>
          <text x="36" y="74" fill="#92400E" font-size="10" font-weight="600">Doubles (6 outcomes): P = 6/36 = 1/6</text>
          
          <text x="14" y="104" fill="#334155" font-size="10">• Sum ranges from 2 (min) to 12 (max)</text>
          <text x="14" y="122" fill="#334155" font-size="10">• P(Sum = 2) = 1/36 = P(Sum = 12)</text>
          <text x="14" y="140" fill="#334155" font-size="10">• P(Sum is prime) = 15/36 = 5/12</text>
          <text x="14" y="158" fill="#334155" font-size="10">• P(Neither 9 nor 11) = 30/36 = 5/6</text>
          
          <rect x="14" y="172" width="192" height="28" fill="#F0FDF4" stroke="#86EFAC" rx="4"/>
          <text x="22" y="190" fill="#166534" font-size="10" font-weight="700">P(E) = Number of favourable / 36</text>
        </g>
        """
        elements.append(card)
        return get_svg_wrapper("\n".join(elements), title=title or "Probability: Pair of Dice 36-Outcome Sample Space", caption=caption or "Complete two-dice coordinate grid showing diagonal sum clusters and doublets")
    else:
        # Standard 52 Playing Cards distribution breakdown
        ox, oy = 40, 80
        elements.append("""
        <g transform="translate(40, 70)">
          <!-- Total Deck -->
          <rect x="180" y="0" width="140" height="36" fill="#0F172A" rx="6"/>
          <text x="250" y="23" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">Full Deck: 52 Cards</text>
          
          <!-- Red / Black branches -->
          <line x1="220" y1="36" x2="110" y2="70" stroke="#94A3B8" stroke-width="1.5"/>
          <line x1="280" y1="36" x2="390" y2="70" stroke="#94A3B8" stroke-width="1.5"/>
          
          <!-- Red Cards -->
          <rect x="40" y="70" width="140" height="32" fill="#FEF2F2" stroke="#DC2626" stroke-width="1.5" rx="6"/>
          <text x="110" y="91" fill="#DC2626" font-size="11" font-weight="700" text-anchor="middle">26 Red Cards</text>
          
          <!-- Black Cards -->
          <rect x="320" y="70" width="140" height="32" fill="#F8FAFC" stroke="#0F172A" stroke-width="1.5" rx="6"/>
          <text x="390" y="91" fill="#0F172A" font-size="11" font-weight="700" text-anchor="middle">26 Black Cards</text>
          
          <!-- 4 Suits -->
          <g transform="translate(10, 130)">
            <!-- Hearts -->
            <rect x="0" y="0" width="115" height="50" fill="#FFFFFF" stroke="#FECACA" rx="6"/>
            <text x="57" y="20" fill="#DC2626" font-size="12" font-weight="700" text-anchor="middle">♥ Hearts (13)</text>
            <text x="57" y="38" fill="#64748B" font-size="9" text-anchor="middle">3 Face (K, Q, J) + 1 Ace</text>
            
            <!-- Diamonds -->
            <rect x="125" y="0" width="115" height="50" fill="#FFFFFF" stroke="#FECACA" rx="6"/>
            <text x="182" y="20" fill="#DC2626" font-size="12" font-weight="700" text-anchor="middle">♦ Diamonds (13)</text>
            <text x="182" y="38" fill="#64748B" font-size="9" text-anchor="middle">3 Face (K, Q, J) + 1 Ace</text>
            
            <!-- Spades -->
            <rect x="250" y="0" width="115" height="50" fill="#FFFFFF" stroke="#CBD5E1" rx="6"/>
            <text x="307" y="20" fill="#0F172A" font-size="12" font-weight="700" text-anchor="middle">♠ Spades (13)</text>
            <text x="307" y="38" fill="#64748B" font-size="9" text-anchor="middle">3 Face (K, Q, J) + 1 Ace</text>
            
            <!-- Clubs -->
            <rect x="375" y="0" width="115" height="50" fill="#FFFFFF" stroke="#CBD5E1" rx="6"/>
            <text x="432" y="20" fill="#0F172A" font-size="12" font-weight="700" text-anchor="middle">♣ Clubs (13)</text>
            <text x="432" y="38" fill="#64748B" font-size="9" text-anchor="middle">3 Face (K, Q, J) + 1 Ace</text>
          </g>
          
          <!-- Summary HUD -->
          <g transform="translate(10, 200)">
            <rect width="480" height="56" fill="#F0FDF4" stroke="#86EFAC" rx="6"/>
            <text x="16" y="22" fill="#166534" font-size="11" font-weight="700">Total Face Cards = 12 (4 Kings, 4 Queens, 4 Jacks) | Total Aces = 4</text>
            <text x="16" y="42" fill="#15803D" font-size="10">P(Red Face Card) = 6/52 = 3/26 | P(Spade) = 13/52 = 1/4 | P(Ace of Hearts) = 1/52</text>
          </g>
        </g>
        """)
        return get_svg_wrapper("\n".join(elements), title=title or "Probability: 52-Card Deck Hierarchical Classification", caption=caption or "Systematic taxonomy of suits, honors, colors, and face cards for board exam probability")


def build_polynomial_ex2_1_grid_svg():
    """
    Renders the complete 6-graph Cartesian atlas for NCERT Exercise 2.1 (Fig 2.10).
    Displays a 3x2 grid of mini Cartesian coordinate systems showing polynomial curves
    with 0, 1, 3, 2, 4, and 3 zeroes.
    """
    panels = []
    width, height = 580, 360
    box_w, box_h = 160, 120
    
    # Grid coordinates for 3 columns, 2 rows
    grid_pos = [
        (30, 65, "(i) No zero (0)"),
        (210, 65, "(ii) 1 zero"),
        (390, 65, "(iii) 3 zeroes"),
        (30, 205, "(iv) 2 zeroes"),
        (210, 205, "(v) 4 zeroes"),
        (390, 205, "(vi) 3 zeroes")
    ]
    
    for idx, (bx, by, label) in enumerate(grid_pos):
        cx, cy = bx + box_w / 2, by + box_h / 2
        # Card background
        panels.append(f'<rect x="{bx}" y="{by}" width="{box_w}" height="{box_h}" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2" rx="6"/>')
        # Subtitle
        panels.append(f'<text x="{bx + 8}" y="{by + 16}" fill="#0F172A" font-size="10" font-weight="700">{label}</text>')
        # Mini Cartesian Axes
        panels.append(f'<line x1="{bx + 15}" y1="{cy}" x2="{bx + box_w - 15}" y2="{cy}" stroke="#64748B" stroke-width="1.2" marker-end="url(#arrowSlate)"/>')
        panels.append(f'<line x1="{cx}" y1="{by + box_h - 12}" x2="{cx}" y2="{by + 20}" stroke="#64748B" stroke-width="1.2" marker-end="url(#arrowSlate)"/>')
        panels.append(f'<text x="{bx + box_w - 12}" y="{cy + 10}" fill="#64748B" font-size="8">x</text>')
        panels.append(f'<text x="{cx + 6}" y="{by + 22}" fill="#64748B" font-size="8">y</text>')
        panels.append(f'<text x="{cx - 6}" y="{cy + 10}" fill="#94A3B8" font-size="7">O</text>')
        
        # Plotted Curves & Intercept Dots
        if idx == 0:
            # (i) Horizontal line parallel to x-axis
            panels.append(f'<line x1="{bx + 20}" y1="{cy - 22}" x2="{bx + box_w - 20}" y2="{cy - 22}" stroke="#2563EB" stroke-width="2"/>')
            panels.append(f'<text x="{cx}" y="{by + box_h - 6}" fill="#DC2626" font-size="9" font-weight="600" text-anchor="middle">0 points on x-axis</text>')
        elif idx == 1:
            # (ii) S-curve intersecting x-axis at 1 point
            panels.append(f'<path d="M {cx - 45} {cy + 30} Q {cx - 20} {cy + 15} {cx + 20} {cy} T {cx + 50} {cy - 35}" fill="none" stroke="#2563EB" stroke-width="2"/>')
            panels.append(f'<circle cx="{cx + 20}" cy="{cy}" r="3.5" fill="#DC2626"/>')
            panels.append(f'<text x="{cx}" y="{by + box_h - 6}" fill="#16A34A" font-size="9" font-weight="600" text-anchor="middle">1 point on x-axis</text>')
        elif idx == 2:
            # (iii) Cubic curve intersecting x-axis at 3 points
            panels.append(f'<path d="M {cx - 50} {cy + 30} Q {cx - 35} {cy - 25} {cx - 15} {cy} Q {cx + 10} {cy + 30} {cx + 35} {cy} T {cx + 50} {cy - 35}" fill="none" stroke="#2563EB" stroke-width="2"/>')
            panels.append(f'<circle cx="{cx - 38}" cy="{cy}" r="3.5" fill="#DC2626"/>')
            panels.append(f'<circle cx="{cx - 15}" cy="{cy}" r="3.5" fill="#DC2626"/>')
            panels.append(f'<circle cx="{cx + 35}" cy="{cy}" r="3.5" fill="#DC2626"/>')
            panels.append(f'<text x="{cx}" y="{by + box_h - 6}" fill="#16A34A" font-size="9" font-weight="600" text-anchor="middle">3 points on x-axis</text>')
        elif idx == 3:
            # (iv) Parabola opening upward intersecting at 2 points
            panels.append(f'<path d="M {cx - 40} {cy - 25} Q {cx} {cy + 35} {cx + 40} {cy - 25}" fill="none" stroke="#2563EB" stroke-width="2"/>')
            panels.append(f'<circle cx="{cx - 26}" cy="{cy}" r="3.5" fill="#DC2626"/>')
            panels.append(f'<circle cx="{cx + 26}" cy="{cy}" r="3.5" fill="#DC2626"/>')
            panels.append(f'<text x="{cx}" y="{by + box_h - 6}" fill="#16A34A" font-size="9" font-weight="600" text-anchor="middle">2 points on x-axis</text>')
        elif idx == 4:
            # (v) Curve with 4 zeroes
            panels.append(f'<path d="M {cx - 55} {cy - 25} Q {cx - 42} {cy + 30} {cx - 28} {cy} Q {cx - 14} {cy - 25} {cx} {cy} Q {cx + 14} {cy + 25} {cx + 28} {cy} T {cx + 55} {cy - 25}" fill="none" stroke="#2563EB" stroke-width="2"/>')
            panels.append(f'<circle cx="{cx - 46}" cy="{cy}" r="3" fill="#DC2626"/>')
            panels.append(f'<circle cx="{cx - 28}" cy="{cy}" r="3" fill="#DC2626"/>')
            panels.append(f'<circle cx="{cx + 10}" cy="{cy}" r="3" fill="#DC2626"/>')
            panels.append(f'<circle cx="{cx + 38}" cy="{cy}" r="3" fill="#DC2626"/>')
            panels.append(f'<text x="{cx}" y="{by + box_h - 6}" fill="#16A34A" font-size="9" font-weight="600" text-anchor="middle">4 points on x-axis</text>')
        elif idx == 5:
            # (vi) Curve touching at 2 points and crossing at 1 point (3 zeroes)
            panels.append(f'<path d="M {cx - 50} {cy - 30} Q {cx - 30} {cy} {cx - 15} {cy - 20} Q {cx} {cy - 30} {cx + 15} {cy} Q {cx + 30} {cy + 25} {cx + 45} {cy}" fill="none" stroke="#2563EB" stroke-width="2"/>')
            panels.append(f'<circle cx="{cx - 30}" cy="{cy}" r="3.5" fill="#DC2626"/>')
            panels.append(f'<circle cx="{cx + 15}" cy="{cy}" r="3.5" fill="#DC2626"/>')
            panels.append(f'<circle cx="{cx + 45}" cy="{cy}" r="3.5" fill="#DC2626"/>')
            panels.append(f'<text x="{cx}" y="{by + box_h - 6}" fill="#16A34A" font-size="9" font-weight="600" text-anchor="middle">3 points on x-axis</text>')

    return get_svg_wrapper("\n".join(panels), title="Exercise 2.1 Complete Cartesian Zero Atlas (Q1 parts i to vi)", caption="Number of zeroes equals the number of times the curve y = p(x) intersects or touches the x-axis")


def build_linear_equations_comparison_svg():
    """
    Renders the 3-panel geometric comparison of pair of linear equations in two variables:
    Panel 1: Intersecting Lines (Unique Solution, Consistent)
    Panel 2: Coincident Lines (Infinitely Many Solutions, Consistent & Dependent)
    Panel 3: Parallel Lines (No Solution, Inconsistent)
    """
    panels = []
    box_w, box_h = 165, 230
    grid_pos = [
        (25, 75, "1. Intersecting", "a₁/a₂ ≠ b₁/b₂", "Unique Solution (1)", "#EFF6FF", "#2563EB"),
        (205, 75, "2. Coincident", "a₁/a₂ = b₁/b₂ = c₁/c₂", "Infinite Solutions", "#F0FDF4", "#16A34A"),
        (385, 75, "3. Parallel", "a₁/a₂ = b₁/b₂ ≠ c₁/c₂", "No Solution (0)", "#FEF2F2", "#DC2626")
    ]
    
    for idx, (bx, by, title_text, ratio_text, sol_text, bg_color, accent_color) in enumerate(grid_pos):
        cx, cy = bx + box_w / 2, by + 90
        # Container Card
        panels.append(f'<rect x="{bx}" y="{by}" width="{box_w}" height="{box_h}" fill="{bg_color}" stroke="{accent_color}" stroke-width="1.5" rx="8"/>')
        # Title and Ratios
        panels.append(f'<text x="{bx + 12}" y="{by + 22}" fill="#0F172A" font-size="12" font-weight="700">{title_text}</text>')
        panels.append(f'<text x="{bx + 12}" y="{by + 38}" fill="{accent_color}" font-size="11" font-weight="700">{ratio_text}</text>')
        
        # Mini Cartesian Axes
        panels.append(f'<line x1="{bx + 15}" y1="{cy}" x2="{bx + box_w - 15}" y2="{cy}" stroke="#94A3B8" stroke-width="1"/>')
        panels.append(f'<line x1="{cx}" y1="{by + 160}" x2="{cx}" y2="{by + 50}" stroke="#94A3B8" stroke-width="1"/>')
        
        if idx == 0:
            # Intersecting Lines
            panels.append(f'<line x1="{bx + 20}" y1="{cy + 40}" x2="{bx + box_w - 20}" y2="{cy - 40}" stroke="#2563EB" stroke-width="2"/>')
            panels.append(f'<line x1="{bx + 20}" y1="{cy - 35}" x2="{bx + box_w - 20}" y2="{cy + 35}" stroke="#16A34A" stroke-width="2"/>')
            panels.append(f'<circle cx="{cx}" cy="{cy}" r="4.5" fill="#DC2626"/>')
            panels.append(f'<text x="{cx + 8}" y="{cy - 6}" fill="#DC2626" font-size="10" font-weight="700">P(x, y)</text>')
        elif idx == 1:
            # Coincident Lines (thick overlapping)
            panels.append(f'<line x1="{bx + 20}" y1="{cy + 35}" x2="{bx + box_w - 20}" y2="{cy - 35}" stroke="#2563EB" stroke-width="3.5"/>')
            panels.append(f'<line x1="{bx + 20}" y1="{cy + 35}" x2="{bx + box_w - 20}" y2="{cy - 35}" stroke="#16A34A" stroke-width="1.8" stroke-dasharray="4,4"/>')
            panels.append(f'<text x="{cx}" y="{cy - 20}" fill="#166534" font-size="9" font-weight="600" text-anchor="middle">Every point is a solution</text>')
        elif idx == 2:
            # Parallel Lines
            panels.append(f'<line x1="{bx + 20}" y1="{cy + 20}" x2="{bx + box_w - 20}" y2="{cy - 40}" stroke="#2563EB" stroke-width="2"/>')
            panels.append(f'<line x1="{bx + 20}" y1="{cy + 50}" x2="{bx + box_w - 20}" y2="{cy - 10}" stroke="#DC2626" stroke-width="2"/>')
            panels.append(f'<text x="{cx}" y="{cy + 15}" fill="#991B1B" font-size="9" font-weight="600" text-anchor="middle">Lines never intersect</text>')
            
        # Solution footer badge
        panels.append(f'<rect x="{bx + 12}" y="{by + box_h - 40}" width="{box_w - 24}" height="28" fill="#FFFFFF" stroke="{accent_color}" rx="4"/>')
        panels.append(f'<text x="{bx + box_w/2}" y="{by + box_h - 22}" fill="{accent_color}" font-size="11" font-weight="700" text-anchor="middle">{sol_text}</text>')

    return get_svg_wrapper("\n".join(panels), title="Pair of Linear Equations: Complete Geometric Classification Atlas", caption="Comparing Intersecting, Coincident, and Parallel systems based on coefficient ratios a1/a2, b1/b2, and c1/c2")


def build_trapezium_diagonals_svg():
    """
    Renders Trapezium ABCD with AB || DC and diagonals AC and BD intersecting at O.
    Construction line EO || AB drawn to prove AO/BO = CO/DO via BPT.
    """
    elements = []
    # Vertices
    A = (160, 110)
    B = (420, 110)
    C = (490, 270)
    D = (90, 270)
    O = (290, 190)
    E = (125, 190)
    
    # Trapezium outline
    elements.append(f'<polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]} {D[0]},{D[1]}" fill="#F8FAFC" stroke="#0F172A" stroke-width="2"/>')
    # Parallel indicators on AB and DC
    elements.append('<path d="M 285 106 L 295 110 L 285 114" fill="none" stroke="#2563EB" stroke-width="1.8"/>')
    elements.append('<path d="M 285 266 L 295 270 L 285 274" fill="none" stroke="#2563EB" stroke-width="1.8"/>')
    
    # Diagonals AC and BD
    elements.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="#2563EB" stroke-width="1.8"/>')
    elements.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{D[0]}" y2="{D[1]}" stroke="#2563EB" stroke-width="1.8"/>')
    
    # Construction line EO (dashed green)
    elements.append(f'<line x1="{E[0]}" y1="{E[1]}" x2="{O[0]}" y2="{O[1]}" stroke="#16A34A" stroke-width="1.8" stroke-dasharray="4,4"/>')
    
    # Vertex dots and labels
    pts = [(A, "A", -12, -8), (B, "B", 8, -8), (C, "C", 8, 14), (D, "D", -16, 14), (O, "O", 4, -8), (E, "E", -16, 4)]
    for pt, txt, dx, dy in pts:
        elements.append(f'<circle cx="{pt[0]}" cy="{pt[1]}" r="3.5" fill="#0F172A"/>')
        elements.append(f'<text x="{pt[0] + dx}" y="{pt[1] + dy}" fill="#0F172A" font-size="12" font-weight="700">{txt}</text>')
        
    # Proof callout card
    card = """
    <g transform="translate(30, 60)">
      <rect width="125" height="75" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.2" rx="6"/>
      <text x="10" y="20" fill="#1E40AF" font-size="10" font-weight="700">Trapezium Diagonals:</text>
      <text x="10" y="38" fill="#0F172A" font-size="10">Draw EO || AB || DC</text>
      <text x="10" y="54" fill="#0F172A" font-size="10">Apply BPT in ΔADC &amp; ΔABD:</text>
      <text x="10" y="70" fill="#2563EB" font-size="11" font-weight="700">AO/BO = CO/DO</text>
    </g>
    """
    elements.append(card)
    return get_svg_wrapper("\n".join(elements), title="Trapezium Diagonals & BPT Proportionality", caption="Diagonals of a trapezium with parallel sides AB || DC divide each other proportionally")


def build_lamp_post_shadow_svg():
    """
    Renders the classic shadow similarity problem:
    Lamp-post AB (3.6m), girl CD (0.9m) walking away, cast shadow DE.
    """
    elements = []
    # Ground
    elements.append('<line x1="50" y1="280" x2="530" y2="280" stroke="#334155" stroke-width="2"/>')
    # Lamp-post AB at x=100
    elements.append('<line x1="100" y1="280" x2="100" y2="80" stroke="#0F172A" stroke-width="3"/>')
    elements.append('<text x="80" y="75" fill="#0F172A" font-size="12" font-weight="700">A (Lamp 3.6m)</text>')
    elements.append('<text x="85" y="300" fill="#0F172A" font-size="12" font-weight="700">B</text>')
    
    # Girl CD at x=320, height 50px (representing 0.9m)
    elements.append('<line x1="320" y1="280" x2="320" y2="230" stroke="#2563EB" stroke-width="2.5"/>')
    elements.append('<text x="310" y="222" fill="#2563EB" font-size="11" font-weight="700">C (Girl 0.9m)</text>')
    elements.append('<text x="315" y="300" fill="#2563EB" font-size="12" font-weight="700">D</text>')
    
    # Light ray line from A through C to ground E at x=440
    elements.append('<line x1="100" y1="80" x2="440" y2="280" stroke="#EAB308" stroke-width="2" stroke-dasharray="4,4"/>')
    elements.append('<circle cx="440" cy="280" r="3.5" fill="#DC2626"/>')
    elements.append('<text x="445" y="295" fill="#DC2626" font-size="12" font-weight="700">E (Tip of shadow)</text>')
    
    # Distance BD = 4.8 m (walking 1.2 m/s for 4 s)
    elements.append('<line x1="100" y1="315" x2="320" y2="315" stroke="#475569" stroke-width="1.2" marker-start="url(#arrowSlate)" marker-end="url(#arrowSlate)"/>')
    elements.append('<text x="210" y="330" fill="#475569" font-size="11" font-weight="600" text-anchor="middle">BD = 4.8 m (walked in 4s)</text>')
    
    # Shadow length DE = x
    elements.append('<line x1="320" y1="315" x2="440" y2="315" stroke="#DC2626" stroke-width="1.2" marker-start="url(#arrowRed)" marker-end="url(#arrowRed)"/>')
    elements.append('<text x="380" y="330" fill="#DC2626" font-size="11" font-weight="700" text-anchor="middle">Shadow DE = 1.6 m</text>')
    
    # Similarity Callout Card
    card = """
    <g transform="translate(180, 80)">
      <rect width="210" height="85" fill="#FEFCE8" stroke="#FDE047" stroke-width="1.2" rx="8"/>
      <text x="12" y="22" fill="#854D0E" font-size="11" font-weight="700">AA Similarity: ΔABE ~ ΔCDE</text>
      <text x="12" y="42" fill="#0F172A" font-size="10">AB / CD = BE / DE</text>
      <text x="12" y="58" fill="#0F172A" font-size="10">3.6 / 0.9 = (4.8 + x) / x</text>
      <text x="12" y="76" fill="#16A34A" font-size="11" font-weight="700">4 = (4.8 + x)/x ⇒ 4x = 4.8 + x ⇒ x = 1.6 m</text>
    </g>
    """
    elements.append(card)
    return get_svg_wrapper("\n".join(elements), title="Similar Triangles: Lamp-Post Shadow Problem", caption="Using AA similarity between large triangle ABE and small triangle CDE to determine shadow length")


def build_concentric_circles_chord_svg():
    """
    Renders two concentric circles with radii 5cm and 3cm.
    Chord AB of larger circle touches smaller circle at point P.
    """
    elements = []
    O = (280, 195)
    R = 100  # 5 cm scale
    r = 60   # 3 cm scale
    
    # Concentric Circles
    elements.append(f'<circle cx="{O[0]}" cy="{O[1]}" r="{R}" fill="#F8FAFC" stroke="#0F172A" stroke-width="2"/>')
    elements.append(f'<circle cx="{O[0]}" cy="{O[1]}" r="{r}" fill="#EFF6FF" stroke="#2563EB" stroke-width="2"/>')
    
    # Tangent Chord AB touching inner circle at P (top point of inner circle: x=280, y=195 - 60 = 135)
    Py = O[1] - r
    half_chord = math.sqrt(R**2 - r**2)  # 80 px (4 cm scale)
    Ax = O[0] - half_chord
    Bx = O[0] + half_chord
    
    # Chord AB
    elements.append(f'<line x1="{Ax}" y1="{Py}" x2="{Bx}" y2="{Py}" stroke="#DC2626" stroke-width="2.2"/>')
    # Radius OP (inner)
    elements.append(f'<line x1="{O[0]}" y1="{O[1]}" x2="{O[0]}" y2="{Py}" stroke="#16A34A" stroke-width="2"/>')
    # Radius OB (outer)
    elements.append(f'<line x1="{O[0]}" y1="{O[1]}" x2="{Bx}" y2="{Py}" stroke="#2563EB" stroke-width="2"/>')
    
    # Right angle box at P
    elements.append(f'<rect x="{O[0]}" y="{Py}" width="12" height="12" fill="none" stroke="#DC2626" stroke-width="1.2"/>')
    
    # Points and labels
    elements.append(f'<circle cx="{O[0]}" cy="{O[1]}" r="3.5" fill="#0F172A"/>')
    elements.append(f'<text x="{O[0] + 6}" y="{O[1] + 16}" fill="#0F172A" font-size="12" font-weight="700">O</text>')
    elements.append(f'<text x="{O[0] - 22}" y="{Py + 20}" fill="#16A34A" font-size="11" font-weight="700">r = 3</text>')
    elements.append(f'<text x="{O[0] + half_chord/2 + 6}" y="{O[1] - r/2 + 6}" fill="#2563EB" font-size="11" font-weight="700">R = 5</text>')
    elements.append(f'<text x="{Ax - 18}" y="{Py + 4}" fill="#DC2626" font-size="12" font-weight="700">A</text>')
    elements.append(f'<text x="{Bx + 8}" y="{Py + 4}" fill="#DC2626" font-size="12" font-weight="700">B</text>')
    elements.append(f'<text x="{O[0]}" y="{Py - 8}" fill="#0F172A" font-size="12" font-weight="700" text-anchor="middle">P (Point of Contact)</text>')
    
    # Computation HUD Card
    card = """
    <g transform="translate(30, 60)">
      <rect width="180" height="95" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.2" rx="8"/>
      <text x="12" y="22" fill="#166534" font-size="11" font-weight="700">Concentric Circle Chord Theorem:</text>
      <text x="12" y="40" fill="#0F172A" font-size="10">OP ⊥ AB ⇒ P bisects chord AB</text>
      <text x="12" y="58" fill="#0F172A" font-size="10">In right ΔOPB: PB = √(5² - 3²) = 4 cm</text>
      <text x="12" y="76" fill="#DC2626" font-size="12" font-weight="700">Total Chord AB = 2 × 4 = 8 cm</text>
    </g>
    """
    elements.append(card)
    return get_svg_wrapper("\n".join(elements), title="Concentric Circles: Chord of Larger Circle Touching Smaller Circle", caption="Radius through point of contact is perpendicular to the tangent chord and bisects it into two equal halves")



