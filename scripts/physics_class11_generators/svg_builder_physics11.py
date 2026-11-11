"""
svg_builder_physics11.py
Comprehensive High-Precision Vector SVG and Cartesian Graph Generator for CBSE Class 11 Physics (Part 1).

Covers:
- Units and Measurements (Vernier/Screw Gauge, Error propagation, Dimensional formulas)
- Kinematics (x-t, v-t, a-t graphs, equations of motion, slopes, areas)
- Motion in a Plane (Vector addition, resolution, projectile motion, circular motion)
- Laws of Motion (FBDs, inclined planes, Atwood pulleys, banked roads, friction)
- Work, Energy & Power (Variable force work F-x area, spring potential energy, collisions)
- Rotational Motion (Center of mass, torque, angular momentum, moment of inertia, rolling)
- Gravitation (Kepler's laws, g variation with altitude & depth, satellite orbits, escape velocity)
"""

import math

def get_svg_wrapper(inner_svg: str, title: str = "", caption: str = "", width: int = 600, height: int = 380) -> str:
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
    <marker id="arrowAmber" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#D97706"/>
    </marker>
  </defs>
  <rect width="{width}" height="{height}" fill="#FFFFFF" rx="12"/>
  <rect width="{width}" height="{height}" fill="url(#gridPattern)" rx="12"/>
  {header_html}
  {inner_svg}
</svg>""".strip()


def build_cartesian_kinematics_svg(
    domain=(0, 10), range_y=(0, 20),
    points=None, lines=None, curves=None, polygons=None,
    x_label="Time t (s)", y_label="Velocity v (m/s)",
    title="", caption=""
):
    """
    Renders a physics coordinate system for x-t, v-t, a-t, F-x plots.
    """
    width, height = 600, 380
    dx = domain[1] - domain[0]
    dy = range_y[1] - range_y[0]
    scale_x = (width - 140) / dx if dx else 40
    scale_y = (height - 130) / dy if dy else 15
    
    ox = 70 + (-domain[0]) * scale_x
    oy = 320 - (-range_y[0]) * scale_y
    
    svg_elements = []
    
    # Grid lines & ticks
    step_x = max(1, int(dx / 8))
    for x in range(int(domain[0]), int(domain[1]) + 1, step_x):
        px = ox + x * scale_x
        if 50 <= px <= width - 40:
            svg_elements.append(f'<line x1="{px}" y1="65" x2="{px}" y2="{height-45}" stroke="#E2E8F0" stroke-width="0.8"/>')
            svg_elements.append(f'<line x1="{px}" y1="{oy-3}" x2="{px}" y2="{oy+3}" stroke="#94A3B8" stroke-width="1.2"/>')
            svg_elements.append(f'<text x="{px}" y="{oy+16}" fill="#64748B" font-size="10" text-anchor="middle">{x}</text>')
                
    step_y = max(1, int(dy / 8))
    for y in range(int(range_y[0]), int(range_y[1]) + 1, step_y):
        py = oy - y * scale_y
        if 65 <= py <= height - 45:
            svg_elements.append(f'<line x1="50" y1="{py}" x2="{width-40}" y2="{py}" stroke="#E2E8F0" stroke-width="0.8"/>')
            svg_elements.append(f'<line x1="{ox-3}" y1="{py}" x2="{ox+3}" y2="{py}" stroke="#94A3B8" stroke-width="1.2"/>')
            if y != 0:
                svg_elements.append(f'<text x="{ox-8}" y="{py+3}" fill="#64748B" font-size="10" text-anchor="end">{y}</text>')
                
    # Axes
    svg_elements.append(f'<line x1="50" y1="{oy}" x2="{width-30}" y2="{oy}" stroke="#334155" stroke-width="1.8" marker-end="url(#arrowSlate)"/>')
    svg_elements.append(f'<line x1="{ox}" y1="{height-35}" x2="{ox}" y2="55" stroke="#334155" stroke-width="1.8" marker-end="url(#arrowSlate)"/>')
    svg_elements.append(f'<text x="{width-25}" y="{oy+4}" fill="#0F172A" font-size="11" font-weight="700">{x_label}</text>')
    svg_elements.append(f'<text x="{ox}" y="45" fill="#0F172A" font-size="11" font-weight="700" text-anchor="middle">{y_label}</text>')
    svg_elements.append(f'<text x="{ox-8}" y="{oy+16}" fill="#64748B" font-size="10" text-anchor="end">O</text>')
    
    # Polygons (shaded area = displacement / work)
    if polygons:
        for p in polygons:
            pts_str = " ".join([f"{ox + pt[0]*scale_x:.1f},{oy - pt[1]*scale_y:.1f}" for pt in p["points"]])
            fill = p.get("fill", "rgba(37, 99, 235, 0.15)")
            stroke = p.get("stroke", "#2563EB")
            svg_elements.append(f'<polygon points="{pts_str}" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
            if "label" in p:
                mid_x = sum(pt[0] for pt in p["points"]) / len(p["points"])
                mid_y = sum(pt[1] for pt in p["points"]) / len(p["points"])
                lx, ly = ox + mid_x * scale_x, oy - mid_y * scale_y
                svg_elements.append(f'<text x="{lx}" y="{ly}" fill="{stroke}" font-size="11" font-weight="600" text-anchor="middle">{p["label"]}</text>')

    # Curves (e.g. parabolas, exponential, harmonic)
    if curves:
        for c in curves:
            pts = []
            steps = 80
            for i in range(steps + 1):
                cur_x = domain[0] + (dx * i / steps)
                try:
                    cur_y = c["fn"](cur_x)
                    if range_y[0] - 2 <= cur_y <= range_y[1] + 2:
                        cx_px = ox + cur_x * scale_x
                        cy_px = oy - cur_y * scale_y
                        pts.append(f"{cx_px:.1f},{cy_px:.1f}")
                except Exception:
                    continue
            if pts:
                color = c.get("color", "#2563EB")
                stroke_w = c.get("stroke_width", 2.2)
                dash = f'stroke-dasharray="{c["dash"]}"' if "dash" in c else ""
                svg_elements.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="{stroke_w}" {dash}/>')
                if "label" in c:
                    lx = ox + c.get("label_x", domain[1]*0.6) * scale_x
                    ly = oy - c["fn"](c.get("label_x", domain[1]*0.6)) * scale_y - 12
                    svg_elements.append(f'<text x="{lx}" y="{ly}" fill="{color}" font-size="11" font-weight="600">{c["label"]}</text>')

    # Lines
    if lines:
        for l in lines:
            x1, y1 = l["p1"]
            x2, y2 = l["p2"]
            color = l.get("color", "#2563EB")
            sw = l.get("stroke_width", 2.0)
            dash = f'stroke-dasharray="{l["dash"]}"' if "dash" in l else ""
            px1, py1 = ox + x1 * scale_x, oy - y1 * scale_y
            px2, py2 = ox + x2 * scale_x, oy - y2 * scale_y
            marker = 'marker-end="url(#arrowBlue)"' if l.get("arrow") else ""
            svg_elements.append(f'<line x1="{px1:.1f}" y1="{py1:.1f}" x2="{px2:.1f}" y2="{py2:.1f}" stroke="{color}" stroke-width="{sw}" {dash} {marker}/>')
            if "label" in l:
                mx, my = (px1 + px2) / 2, (py1 + py2) / 2 - 8
                svg_elements.append(f'<text x="{mx:.1f}" y="{my:.1f}" fill="{color}" font-size="11" font-weight="600">{l["label"]}</text>')

    # Points
    if points:
        for pt in points:
            px = ox + pt["x"] * scale_x
            py = oy - pt["y"] * scale_y
            color = pt.get("color", "#DC2626")
            svg_elements.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4.5" fill="{color}" stroke="#FFFFFF" stroke-width="1.5"/>')
            if "label" in pt:
                svg_elements.append(f'<text x="{px + 6:.1f}" y="{py - 6:.1f}" fill="#0F172A" font-size="10" font-weight="600">{pt["label"]}</text>')

    inner_svg = "\n  ".join(svg_elements)
    return get_svg_wrapper(inner_svg, title=title, caption=caption, width=width, height=height)


# =========================================================================
# 1. UNITS & MEASUREMENTS (Vernier, Screw Gauge, Error Propagation)
# =========================================================================

def build_measurement_apparatus_svg(apparatus="vernier", title="Vernier Callipers Measurement", caption="Least Count = 1 MSD - 1 VSD = 0.1 mm"):
    if apparatus == "screw_gauge":
        inner = """
        <g id="screw_gauge" transform="translate(60, 110)">
          <!-- U Frame -->
          <path d="M 40 40 C 0 40 0 160 40 160 L 100 160 C 130 160 130 40 100 40 Z" fill="none" stroke="#334155" stroke-width="14" stroke-linejoin="round"/>
          <text x="65" y="105" fill="#64748B" font-size="11" font-weight="700" text-anchor="middle">SCREW GAUGE</text>
          <!-- Anvil and Spindle -->
          <rect x="80" y="85" width="20" height="30" fill="#94A3B8" stroke="#475569" stroke-width="1.5"/>
          <text x="90" y="75" fill="#475569" font-size="10" text-anchor="middle">Anvil</text>
          <rect x="130" y="85" width="50" height="30" fill="#CBD5E1" stroke="#475569" stroke-width="1.5"/>
          <text x="155" y="75" fill="#475569" font-size="10" text-anchor="middle">Spindle</text>
          <!-- Stud / Specimen -->
          <circle cx="115" cy="100" r="14" fill="#F87171" stroke="#DC2626" stroke-width="1.5"/>
          <text x="115" y="104" fill="#FFFFFF" font-size="9" font-weight="700" text-anchor="middle">Wire</text>
          <!-- Main Scale Barrel -->
          <rect x="180" y="80" width="100" height="40" fill="#F1F5F9" stroke="#334155" stroke-width="1.5"/>
          <line x1="180" y1="100" x2="280" y2="100" stroke="#0F172A" stroke-width="1.2"/>
          <text x="185" y="94" fill="#0F172A" font-size="9">0</text>
          <text x="210" y="94" fill="#0F172A" font-size="9">5</text>
          <text x="235" y="94" fill="#0F172A" font-size="9">10 mm</text>
          <!-- Circular Scale Thimble -->
          <rect x="280" y="70" width="70" height="60" rx="4" fill="#E2E8F0" stroke="#2563EB" stroke-width="2"/>
          <line x1="280" y1="85" x2="295" y2="85" stroke="#2563EB" stroke-width="1.2"/>
          <line x1="280" y1="100" x2="305" y2="100" stroke="#DC2626" stroke-width="1.8"/>
          <line x1="280" y1="115" x2="295" y2="115" stroke="#2563EB" stroke-width="1.2"/>
          <text x="312" y="103" fill="#DC2626" font-size="10" font-weight="700">45</text>
          <text x="315" y="80" fill="#2563EB" font-size="10">Thimble</text>
          <!-- Ratchet -->
          <rect x="350" y="82" width="30" height="36" rx="2" fill="#64748B" stroke="#334155" stroke-width="1.5"/>
          <text x="365" y="74" fill="#64748B" font-size="10" text-anchor="middle">Ratchet</text>
        </g>
        <g id="readings" transform="translate(140, 310)">
          <rect width="320" height="42" fill="#F8FAFC" stroke="#CBD5E1" rx="6"/>
          <text x="160" y="18" fill="#0F172A" font-size="11" font-weight="700" text-anchor="middle">Total Reading = Pitch Scale (PSR) + (HSR × LC)</text>
          <text x="160" y="34" fill="#2563EB" font-size="11" text-anchor="middle">Least Count (LC) = Pitch / Total Divisions = 1 mm / 100 = 0.01 mm</text>
        </g>
        """
    else:
        # Vernier Callipers
        inner = """
        <g id="vernier_callipers" transform="translate(50, 100)">
          <!-- Main Beam -->
          <rect x="50" y="60" width="380" height="40" fill="#F1F5F9" stroke="#334155" stroke-width="1.5"/>
          <!-- Fixed Jaw -->
          <path d="M 50 60 L 50 170 C 50 180 35 180 35 170 L 35 30 L 70 30 L 70 60 Z" fill="#E2E8F0" stroke="#334155" stroke-width="1.5"/>
          <text x="25" y="130" fill="#475569" font-size="10" font-weight="600" transform="rotate(-90 25 130)">Fixed Jaw</text>
          <!-- Main Scale Markings -->
          <line x1="80" y1="100" x2="420" y2="100" stroke="#334155" stroke-width="1"/>
          <g fill="#0F172A" font-size="9" text-anchor="middle">
            <text x="90" y="92">0</text><line x1="90" y1="94" x2="90" y2="100" stroke="#334155"/>
            <text x="130" y="92">1</text><line x1="130" y1="94" x2="130" y2="100" stroke="#334155"/>
            <text x="170" y="92">2</text><line x1="170" y1="94" x2="170" y2="100" stroke="#334155"/>
            <text x="210" y="92">3</text><line x1="210" y1="94" x2="210" y2="100" stroke="#334155"/>
            <text x="250" y="92">4</text><line x1="250" y1="94" x2="250" y2="100" stroke="#334155"/>
            <text x="290" y="92">5 cm</text><line x1="290" y1="94" x2="290" y2="100" stroke="#334155"/>
          </g>
          <!-- Sliding Vernier Jaw -->
          <path d="M 190 50 L 270 50 L 270 110 L 210 110 L 210 170 C 210 180 195 180 195 170 L 195 50 Z" fill="#E0E7FF" stroke="#2563EB" stroke-width="1.8"/>
          <text x="235" y="75" fill="#2563EB" font-size="10" font-weight="700">VERNIER</text>
          <!-- Vernier divisions -->
          <g stroke="#2563EB" stroke-width="1">
            <line x1="195" y1="100" x2="195" y2="108"/>
            <line x1="203" y1="100" x2="203" y2="106"/>
            <line x1="211" y1="100" x2="211" y2="106"/>
            <line x1="219" y1="100" x2="219" y2="108"/>
            <line x1="227" y1="100" x2="227" y2="106"/>
            <line x1="235" y1="100" x2="235" y2="108"/>
          </g>
          <!-- Cylinder Measured -->
          <rect x="50" y="125" width="145" height="35" rx="3" fill="#FED7AA" stroke="#D97706" stroke-width="1.5"/>
          <text x="122" y="146" fill="#9A3412" font-size="11" font-weight="700" text-anchor="middle">Measured Object</text>
        </g>
        <g id="vernier_formula" transform="translate(130, 310)">
          <rect width="340" height="42" fill="#F8FAFC" stroke="#CBD5E1" rx="6"/>
          <text x="170" y="18" fill="#0F172A" font-size="11" font-weight="700" text-anchor="middle">Reading = MSR + (VSR × LC) - (Zero Error)</text>
          <text x="170" y="34" fill="#2563EB" font-size="11" text-anchor="middle">LC = 1 MSD - 1 VSD = 1 mm - 0.9 mm = 0.1 mm = 0.01 cm</text>
        </g>
        """
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=380)


# =========================================================================
# 2. MOTION IN A PLANE (Vectors, Projectile Trajectory, Centripetal Motion)
# =========================================================================

def build_vector_addition_resolution_svg(variant="addition", title="", caption=""):
    if variant == "resolution":
        inner = """
        <g transform="translate(90, 260)">
          <!-- Axes -->
          <line x1="-20" y1="0" x2="360" y2="0" stroke="#64748B" stroke-width="1.5" marker-end="url(#arrowSlate)"/>
          <line x1="0" y1="20" x2="0" y2="-200" stroke="#64748B" stroke-width="1.5" marker-end="url(#arrowSlate)"/>
          <text x="350" y="18" fill="#0F172A" font-size="12" font-weight="700">X</text>
          <text x="-15" y="-190" fill="#0F172A" font-size="12" font-weight="700">Y</text>
          <text x="-12" y="14" fill="#64748B" font-size="10">O</text>
          <!-- Vector A -->
          <line x1="0" y1="0" x2="240" y2="-140" stroke="#2563EB" stroke-width="3" marker-end="url(#arrowBlue)"/>
          <text x="110" y="-85" fill="#2563EB" font-size="14" font-weight="700">A⃗</text>
          <!-- Projections -->
          <line x1="240" y1="0" x2="240" y2="-140" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="4,4"/>
          <line x1="0" y1="-140" x2="240" y2="-140" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="4,4"/>
          <!-- Components -->
          <line x1="0" y1="0" x2="240" y2="0" stroke="#16A34A" stroke-width="3" marker-end="url(#arrowGreen)"/>
          <text x="110" y="18" fill="#16A34A" font-size="12" font-weight="700">A_x = A cos θ</text>
          <line x1="0" y1="0" x2="0" y2="-140" stroke="#DC2626" stroke-width="3" marker-end="url(#arrowRed)"/>
          <text x="-90" y="-70" fill="#DC2626" font-size="12" font-weight="700">A_y = A sin θ</text>
          <!-- Angle arc -->
          <path d="M 50 0 A 50 50 0 0 0 42 -27" fill="none" stroke="#D97706" stroke-width="2"/>
          <text x="56" y="-12" fill="#D97706" font-size="12" font-weight="700">θ</text>
        </g>
        <g id="hud" transform="translate(370, 90)">
          <rect width="190" height="90" fill="#F8FAFC" stroke="#CBD5E1" rx="8"/>
          <text x="15" y="24" fill="#0F172A" font-size="11" font-weight="700">Orthogonal Components</text>
          <text x="15" y="44" fill="#2563EB" font-size="11">|A⃗| = √(A_x² + A_y²)</text>
          <text x="15" y="64" fill="#D97706" font-size="11">tan θ = A_y / A_x</text>
          <text x="15" y="80" fill="#475569" font-size="10">A⃗ = A_x î + A_y ĵ</text>
        </g>
        """
        title = title or "Vector Resolution in Rectangular Components"
        caption = caption or "Decomposition into orthogonal horizontal and vertical components"
    else:
        # Vector addition: Parallelogram Law
        inner = """
        <g transform="translate(80, 260)">
          <!-- Vector A -->
          <line x1="0" y1="0" x2="200" y2="0" stroke="#2563EB" stroke-width="3" marker-end="url(#arrowBlue)"/>
          <text x="95" y="20" fill="#2563EB" font-size="13" font-weight="700">A⃗ (P)</text>
          <!-- Vector B -->
          <line x1="0" y1="0" x2="110" y2="-120" stroke="#16A34A" stroke-width="3" marker-end="url(#arrowGreen)"/>
          <text x="40" y="-70" fill="#16A34A" font-size="13" font-weight="700">B⃗ (Q)</text>
          <!-- Parallelogram dash lines -->
          <line x1="200" y1="0" x2="310" y2="-120" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="4,4"/>
          <line x1="110" y1="-120" x2="310" y2="-120" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="4,4"/>
          <!-- Resultant R -->
          <line x1="0" y1="0" x2="310" y2="-120" stroke="#DC2626" stroke-width="3.2" marker-end="url(#arrowRed)"/>
          <text x="160" y="-75" fill="#DC2626" font-size="14" font-weight="700">R⃗ = A⃗ + B⃗</text>
          <!-- Angle theta -->
          <path d="M 40 0 A 40 40 0 0 0 26 -28" fill="none" stroke="#D97706" stroke-width="1.8"/>
          <text x="45" y="-12" fill="#D97706" font-size="11" font-weight="700">θ</text>
          <!-- Angle alpha -->
          <path d="M 65 0 A 65 65 0 0 0 58 -22" fill="none" stroke="#DC2626" stroke-width="1.8"/>
          <text x="72" y="-6" fill="#DC2626" font-size="11" font-weight="700">α</text>
        </g>
        <g id="hud" transform="translate(360, 90)">
          <rect width="210" height="95" fill="#F8FAFC" stroke="#CBD5E1" rx="8"/>
          <text x="15" y="22" fill="#0F172A" font-size="11" font-weight="700">Parallelogram Law of Vectors</text>
          <text x="15" y="42" fill="#DC2626" font-size="11">R = √(A² + B² + 2AB cos θ)</text>
          <text x="15" y="62" fill="#D97706" font-size="11">tan α = (B sin θ) / (A + B cos θ)</text>
          <text x="15" y="82" fill="#475569" font-size="10">Special: θ = 90° ⇒ R = √(A² + B²)</text>
        </g>
        """
        title = title or "Parallelogram Law of Vector Addition"
        caption = caption or "Analytical magnitude and direction of the resultant vector"
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=380)


def build_projectile_motion_svg(title="Projectile Motion Trajectory", caption="Parabolic path under gravity with independent horizontal & vertical motions"):
    inner = """
    <g transform="translate(70, 270)">
      <!-- Axes -->
      <line x1="-15" y1="0" x2="480" y2="0" stroke="#64748B" stroke-width="1.5" marker-end="url(#arrowSlate)"/>
      <line x1="0" y1="15" x2="0" y2="-190" stroke="#64748B" stroke-width="1.5" marker-end="url(#arrowSlate)"/>
      <text x="470" y="16" fill="#0F172A" font-size="11" font-weight="700">x (Range)</text>
      <text x="-12" y="-180" fill="#0F172A" font-size="11" font-weight="700">y</text>
      <text x="-10" y="14" fill="#64748B" font-size="10">O</text>
      <!-- Parabolic Curve y = x * tan(theta) - (g * x^2)/(2 v0^2 cos^2 theta) -->
      <!-- Peak at x = 210, y = -140 -->
      <path d="M 0 0 Q 210 -280 420 0" fill="none" stroke="#2563EB" stroke-width="2.8"/>
      <!-- Initial Launch Velocity Vector -->
      <line x1="0" y1="0" x2="65" y2="-75" stroke="#DC2626" stroke-width="2.5" marker-end="url(#arrowRed)"/>
      <text x="35" y="-82" fill="#DC2626" font-size="12" font-weight="700">v₀</text>
      <line x1="0" y1="0" x2="55" y2="0" stroke="#16A34A" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="25" y="14" fill="#16A34A" font-size="10">v₀ cos θ</text>
      <line x1="0" y1="0" x2="0" y2="-65" stroke="#DC2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="-50" y="-35" fill="#DC2626" font-size="10">v₀ sin θ</text>
      <path d="M 30 0 A 30 30 0 0 0 22 -22" fill="none" stroke="#D97706" stroke-width="1.8"/>
      <text x="32" y="-10" fill="#D97706" font-size="11" font-weight="700">θ₀</text>
      <!-- Apex Point -->
      <circle cx="210" cy="-140" r="4.5" fill="#DC2626"/>
      <line x1="210" y1="-140" x2="265" y2="-140" stroke="#16A34A" stroke-width="2.2" marker-end="url(#arrowGreen)"/>
      <text x="270" y="-136" fill="#16A34A" font-size="10" font-weight="600">v_x = v₀ cos θ (v_y = 0)</text>
      <!-- Maximum Height H -->
      <line x1="210" y1="0" x2="210" y2="-140" stroke="#94A3B8" stroke-width="1.2" stroke-dasharray="3,3"/>
      <text x="180" y="-70" fill="#2563EB" font-size="11" font-weight="700">H_max</text>
      <!-- Range R -->
      <line x1="0" y1="28" x2="420" y2="28" stroke="#334155" stroke-width="1.2" marker-end="url(#arrowSlate)" marker-start="url(#arrowSlate)"/>
      <text x="210" y="42" fill="#0F172A" font-size="11" font-weight="700" text-anchor="middle">Horizontal Range R = (v₀² sin 2θ) / g</text>
    </g>
    <g id="hud" transform="translate(340, 65)">
      <rect width="230" height="90" fill="#F8FAFC" stroke="#CBD5E1" rx="8"/>
      <text x="14" y="20" fill="#0F172A" font-size="11" font-weight="700">Core Projectile Formulas</text>
      <text x="14" y="38" fill="#2563EB" font-size="11">Time of Flight: T = (2 v₀ sin θ) / g</text>
      <text x="14" y="56" fill="#DC2626" font-size="11">Max Height: H = (v₀² sin² θ) / 2g</text>
      <text x="14" y="74" fill="#16A34A" font-size="11">Max Range at θ = 45°: R_max = v₀² / g</text>
    </g>
    """
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=380)


# =========================================================================
# 3. LAWS OF MOTION (FBD, Inclined Plane, Banked Road, Atwood Pulley)
# =========================================================================

def build_inclined_plane_fbd_svg(theta_deg=30, title="Free Body Diagram: Block on Inclined Plane", caption="Forces resolved parallel and perpendicular to inclined surface"):
    inner = """
    <g transform="translate(70, 270)">
      <!-- Wedge -->
      <polygon points="0,0 360,0 360,-180" fill="#F1F5F9" stroke="#334155" stroke-width="2"/>
      <path d="M 60 0 A 60 60 0 0 0 54 -28" fill="none" stroke="#D97706" stroke-width="2"/>
      <text x="68" y="-10" fill="#D97706" font-size="12" font-weight="700">θ</text>
      <!-- Block on incline -->
      <!-- Incline angle ~26.5 deg (slope 0.5) -->
      <g transform="translate(200, -100) rotate(-26.56)">
        <rect x="-35" y="-35" width="70" height="35" rx="3" fill="#E0E7FF" stroke="#2563EB" stroke-width="2"/>
        <text x="0" y="-14" fill="#2563EB" font-size="11" font-weight="700" text-anchor="middle">m</text>
        <!-- Normal Force N -->
        <line x1="0" y1="-35" x2="0" y2="-95" stroke="#16A34A" stroke-width="2.5" marker-end="url(#arrowGreen)"/>
        <text x="8" y="-85" fill="#16A34A" font-size="11" font-weight="700">N</text>
        <!-- Friction force up incline -->
        <line x1="-35" y1="0" x2="-85" y2="0" stroke="#D97706" stroke-width="2.2" marker-end="url(#arrowAmber)"/>
        <text x="-80" y="-8" fill="#D97706" font-size="10" font-weight="700">f_s (or f_k)</text>
        <!-- mg sin theta down incline -->
        <line x1="35" y1="0" x2="95" y2="0" stroke="#DC2626" stroke-width="2.2" marker-end="url(#arrowRed)"/>
        <text x="50" y="16" fill="#DC2626" font-size="10" font-weight="700">mg sin θ</text>
        <!-- mg cos theta opposite N -->
        <line x1="0" y1="0" x2="0" y2="60" stroke="#64748B" stroke-width="2" stroke-dasharray="3,3" marker-end="url(#arrowSlate)"/>
        <text x="8" y="55" fill="#64748B" font-size="10">mg cos θ</text>
      </g>
      <!-- True Gravity vector vertically down -->
      <g transform="translate(200, -100)">
        <line x1="0" y1="0" x2="0" y2="80" stroke="#DC2626" stroke-width="2.5" marker-end="url(#arrowRed)"/>
        <text x="8" y="70" fill="#DC2626" font-size="11" font-weight="700">mg</text>
      </g>
    </g>
    <g id="hud" transform="translate(370, 70)">
      <rect width="200" height="95" fill="#F8FAFC" stroke="#CBD5E1" rx="8"/>
      <text x="14" y="20" fill="#0F172A" font-size="11" font-weight="700">Equations of Equilibrium</text>
      <text x="14" y="38" fill="#16A34A" font-size="11">Perpendicular: N = mg cos θ</text>
      <text x="14" y="56" fill="#D97706" font-size="11">Max Static Friction: f_s ≤ μ_s N</text>
      <text x="14" y="74" fill="#DC2626" font-size="11">Sliding condition: tan θ &gt; μ_s</text>
      <text x="14" y="90" fill="#2563EB" font-size="10">Acceleration a = g(sin θ - μ_k cos θ)</text>
    </g>
    """
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=380)


def build_banked_road_svg(title="Dynamics of Circular Motion: Banked Road", caption="Optimum speed without friction vs maximum speed with friction"):
    inner = """
    <g transform="translate(80, 270)">
      <!-- Banked Surface -->
      <polygon points="0,0 340,0 340,-130" fill="#F1F5F9" stroke="#334155" stroke-width="2"/>
      <path d="M 60 0 A 60 60 0 0 0 56 -21" fill="none" stroke="#D97706" stroke-width="2"/>
      <text x="68" y="-8" fill="#D97706" font-size="12" font-weight="700">θ</text>
      <!-- Vehicle on banked road -->
      <!-- Incline ~21 deg -->
      <g transform="translate(190, -72) rotate(-20.9)">
        <rect x="-35" y="-25" width="70" height="25" rx="4" fill="#3B82F6" stroke="#1D4ED8" stroke-width="2"/>
        <circle cx="-20" cy="0" r="5" fill="#0F172A"/>
        <circle cx="20" cy="0" r="5" fill="#0F172A"/>
        <text x="0" y="-8" fill="#FFFFFF" font-size="10" font-weight="700" text-anchor="middle">Car</text>
        <!-- Normal Force N -->
        <line x1="0" y1="-25" x2="0" y2="-90" stroke="#16A34A" stroke-width="2.5" marker-end="url(#arrowGreen)"/>
        <text x="8" y="-80" fill="#16A34A" font-size="11" font-weight="700">N</text>
      </g>
      <!-- Vertical and Horizontal Components of N -->
      <g transform="translate(190, -72)">
        <!-- Vertical: N cos theta -->
        <line x1="0" y1="0" x2="0" y2="-75" stroke="#16A34A" stroke-width="2" stroke-dasharray="3,3" marker-end="url(#arrowGreen)"/>
        <text x="8" y="-60" fill="#16A34A" font-size="10" font-weight="600">N cos θ = mg</text>
        <!-- Horizontal: N sin theta = mv^2 / R -->
        <line x1="0" y1="0" x2="-80" y2="0" stroke="#DC2626" stroke-width="2.5" marker-end="url(#arrowRed)"/>
        <text x="-125" y="-8" fill="#DC2626" font-size="10" font-weight="700">N sin θ = mv²/r</text>
        <!-- mg downwards -->
        <line x1="0" y1="0" x2="0" y2="70" stroke="#0F172A" stroke-width="2.2" marker-end="url(#arrowSlate)"/>
        <text x="8" y="60" fill="#0F172A" font-size="11" font-weight="700">mg</text>
      </g>
    </g>
    <g id="hud" transform="translate(360, 65)">
      <rect width="210" height="95" fill="#F8FAFC" stroke="#CBD5E1" rx="8"/>
      <text x="14" y="20" fill="#0F172A" font-size="11" font-weight="700">Banked Curve Mechanics</text>
      <text x="14" y="38" fill="#2563EB" font-size="11">Optimum Speed (Zero Wear):</text>
      <text x="24" y="54" fill="#2563EB" font-size="12" font-weight="700">v₀ = √(r g tan θ)</text>
      <text x="14" y="74" fill="#DC2626" font-size="11">Max Safe Speed with friction μ:</text>
      <text x="14" y="90" fill="#DC2626" font-size="10">v_max = √[r g (μ + tan θ) / (1 - μ tan θ)]</text>
    </g>
    """
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=380)


# =========================================================================
# 4. WORK, ENERGY & POWER (Spring PE, Collisions in 1D & 2D)
# =========================================================================

def build_spring_potential_energy_svg(title="Spring-Mass System & Potential Energy", caption="Restoring Force F = -kx and Elastic Potential Energy U(x) = 1/2 k x²"):
    inner = """
    <g transform="translate(60, 90)">
      <!-- Physical Spring Mass Setup -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="10" height="80" fill="#64748B"/>
        <!-- Wall hatching -->
        <line x1="-5" y1="10" x2="0" y2="20" stroke="#475569" stroke-width="1.5"/>
        <line x1="-5" y1="30" x2="0" y2="40" stroke="#475569" stroke-width="1.5"/>
        <line x1="-5" y1="50" x2="0" y2="60" stroke="#475569" stroke-width="1.5"/>
        <!-- Floor -->
        <line x1="0" y1="80" x2="220" y2="80" stroke="#334155" stroke-width="2"/>
        <!-- Spring zig-zag -->
        <path d="M 10 40 L 25 30 L 40 50 L 55 30 L 70 50 L 85 30 L 100 50 L 115 30 L 130 50 L 140 40" fill="none" stroke="#2563EB" stroke-width="2.2"/>
        <!-- Mass m -->
        <rect x="140" y="20" width="45" height="60" rx="3" fill="#FED7AA" stroke="#D97706" stroke-width="2"/>
        <text x="162" y="55" fill="#9A3412" font-size="12" font-weight="700" text-anchor="middle">m</text>
        <!-- Displacement x -->
        <line x1="110" y1="95" x2="110" y2="15" stroke="#94A3B8" stroke-dasharray="3,3"/>
        <text x="110" y="108" fill="#64748B" font-size="9" text-anchor="middle">x = 0</text>
        <line x1="110" y1="95" x2="162" y2="95" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrowBlue)"/>
        <text x="136" y="108" fill="#2563EB" font-size="10" font-weight="600" text-anchor="middle">+x_m</text>
        <!-- Restoring force arrow -->
        <line x1="140" y1="50" x2="90" y2="50" stroke="#DC2626" stroke-width="2.5" marker-end="url(#arrowRed)"/>
        <text x="100" y="42" fill="#DC2626" font-size="10" font-weight="700">F = -kx</text>
      </g>
      <!-- Parabolic Potential Energy Curve U(x) = 1/2 k x^2 -->
      <g transform="translate(300, 160)">
        <line x1="-90" y1="0" x2="90" y2="0" stroke="#64748B" stroke-width="1.5" marker-end="url(#arrowSlate)"/>
        <line x1="0" y1="10" x2="0" y2="-120" stroke="#64748B" stroke-width="1.5" marker-end="url(#arrowSlate)"/>
        <text x="85" y="14" fill="#0F172A" font-size="10" font-weight="700">x</text>
        <text x="-8" y="-115" fill="#0F172A" font-size="10" font-weight="700">E, U</text>
        <!-- Total Mechanical Energy line E -->
        <line x1="-70" y1="-80" x2="70" y2="-80" stroke="#DC2626" stroke-width="2" stroke-dasharray="4,4"/>
        <text x="75" y="-76" fill="#DC2626" font-size="10" font-weight="700">Total E</text>
        <!-- U(x) parabola -->
        <path d="M -70 -80 Q 0 0 70 -80" fill="rgba(37, 99, 235, 0.15)" stroke="#2563EB" stroke-width="2.5"/>
        <text x="35" y="-35" fill="#2563EB" font-size="10" font-weight="600">U(x) = ½kx²</text>
        <!-- Kinetic energy label -->
        <text x="0" y="-55" fill="#16A34A" font-size="10" font-weight="600" text-anchor="middle">K = E - U(x)</text>
      </g>
    </g>
    <g id="hud" transform="translate(100, 290)">
      <rect width="400" height="42" fill="#F8FAFC" stroke="#CBD5E1" rx="6"/>
      <text x="200" y="18" fill="#0F172A" font-size="11" font-weight="700" text-anchor="middle">Conservation of Mechanical Energy: E = K + U = ½mv² + ½kx² = constant</text>
      <text x="200" y="34" fill="#2563EB" font-size="11" text-anchor="middle">At extreme x = ±x_m: K = 0, E = ½kx_m² | At mean x = 0: U = 0, v_max = x_m √(k/m)</text>
    </g>
    """
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=380)


# =========================================================================
# 5. ROTATIONAL MOTION (Center of Mass, Torque, Rolling)
# =========================================================================

def build_rotational_dynamics_svg(title="Torque and Angular Momentum", caption="Torque τ⃗ = r⃗ × F⃗ and Conservation of Angular Momentum L⃗ = I ω⃗"):
    inner = """
    <g transform="translate(120, 240)">
      <!-- Axis of Rotation -->
      <line x1="0" y1="40" x2="0" y2="-170" stroke="#334155" stroke-width="2.5" stroke-dasharray="6,4"/>
      <text x="-8" y="-160" fill="#334155" font-size="11" font-weight="700" text-anchor="end">Axis of Rotation</text>
      <circle cx="0" cy="0" r="5" fill="#0F172A"/>
      <text x="-12" y="15" fill="#64748B" font-size="10">O</text>
      <!-- Position Vector r -->
      <line x1="0" y1="0" x2="160" y2="-60" stroke="#2563EB" stroke-width="2.5" marker-end="url(#arrowBlue)"/>
      <text x="75" y="-40" fill="#2563EB" font-size="12" font-weight="700">r⃗</text>
      <!-- Force Vector F at point P -->
      <circle cx="160" cy="-60" r="5" fill="#DC2626"/>
      <text x="168" y="-70" fill="#0F172A" font-size="11" font-weight="700">P (Particle m)</text>
      <line x1="160" y1="-60" x2="250" y2="-120" stroke="#DC2626" stroke-width="3" marker-end="url(#arrowRed)"/>
      <text x="255" y="-115" fill="#DC2626" font-size="13" font-weight="700">F⃗</text>
      <!-- Angle theta between r and F -->
      <line x1="160" y1="-60" x2="240" y2="-90" stroke="#94A3B8" stroke-width="1.2" stroke-dasharray="3,3"/>
      <path d="M 190 -71 A 30 30 0 0 0 185 -84" fill="none" stroke="#D97706" stroke-width="1.8"/>
      <text x="200" y="-80" fill="#D97706" font-size="11" font-weight="700">θ</text>
      <!-- Lever Arm (Perpendicular Distance) -->
      <line x1="0" y1="0" x2="105" y2="45" stroke="#16A34A" stroke-width="2" stroke-dasharray="3,3"/>
      <text x="40" y="35" fill="#16A34A" font-size="11" font-weight="700">d = r sin θ</text>
      <!-- Torque Vector τ pointing along z-axis (upwards) -->
      <line x1="0" y1="0" x2="0" y2="-110" stroke="#8B5CF6" stroke-width="3.5" marker-end="url(#arrowSlate)"/>
      <text x="10" y="-95" fill="#8B5CF6" font-size="13" font-weight="700">τ⃗ = r⃗ × F⃗</text>
      <!-- Circular arrow showing direction of rotation -->
      <path d="M 35 15 A 40 25 0 1 0 35 -15" fill="none" stroke="#8B5CF6" stroke-width="2" marker-end="url(#arrowSlate)"/>
      <text x="48" y="5" fill="#8B5CF6" font-size="11" font-weight="600">ω⃗</text>
    </g>
    <g id="hud" transform="translate(370, 75)">
      <rect width="200" height="95" fill="#F8FAFC" stroke="#CBD5E1" rx="8"/>
      <text x="14" y="20" fill="#0F172A" font-size="11" font-weight="700">Rotational Kinematics &amp; Dynamics</text>
      <text x="14" y="38" fill="#8B5CF6" font-size="11">Torque: |τ⃗| = r F sin θ = I α</text>
      <text x="14" y="56" fill="#2563EB" font-size="11">Angular Momentum: L = I ω</text>
      <text x="14" y="74" fill="#16A34A" font-size="11">Rotational KE = ½ I ω²</text>
      <text x="14" y="90" fill="#DC2626" font-size="10">Rolling KE = ½ M v² + ½ I ω²</text>
    </g>
    """
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=380)


# =========================================================================
# 6. GRAVITATION (Kepler's Ellipse, Variation of g, Orbital Satellite)
# =========================================================================

def build_gravitation_orbit_svg(variant="kepler", title="", caption=""):
    if variant == "g_variation":
        inner = """
        <g transform="translate(80, 260)">
          <!-- Axes: g vs r -->
          <line x1="-15" y1="0" x2="360" y2="0" stroke="#64748B" stroke-width="1.5" marker-end="url(#arrowSlate)"/>
          <line x1="0" y1="15" x2="0" y2="-190" stroke="#64748B" stroke-width="1.5" marker-end="url(#arrowSlate)"/>
          <text x="350" y="16" fill="#0F172A" font-size="11" font-weight="700">Distance r</text>
          <text x="-12" y="-180" fill="#0F172A" font-size="11" font-weight="700">g(r)</text>
          <text x="-12" y="14" fill="#64748B" font-size="10">O</text>
          <!-- Inside Earth: r < R (Linear g = g_s * r / R) -->
          <line x1="0" y1="0" x2="140" y2="-140" stroke="#2563EB" stroke-width="2.8"/>
          <text x="50" y="-85" fill="#2563EB" font-size="11" font-weight="700">g ∝ r (Inside)</text>
          <!-- Surface Peak at r = R -->
          <line x1="140" y1="0" x2="140" y2="-140" stroke="#94A3B8" stroke-width="1.2" stroke-dasharray="3,3"/>
          <line x1="0" y1="-140" x2="140" y2="-140" stroke="#94A3B8" stroke-width="1.2" stroke-dasharray="3,3"/>
          <circle cx="140" cy="-140" r="5" fill="#DC2626"/>
          <text x="135" y="16" fill="#0F172A" font-size="11" font-weight="700">r = R_E</text>
          <text x="-50" y="-136" fill="#DC2626" font-size="11" font-weight="700">g = 9.8 m/s²</text>
          <!-- Outside Earth: r > R (Inverse Square g = GM / r^2) -->
          <!-- Hyperbolic decay -->
          <path d="M 140 -140 Q 180 -55 330 -15" fill="none" stroke="#16A34A" stroke-width="2.8"/>
          <text x="210" y="-60" fill="#16A34A" font-size="11" font-weight="700">g ∝ 1/r² (Outside)</text>
        </g>
        <g id="hud" transform="translate(360, 60)">
          <rect width="210" height="95" fill="#F8FAFC" stroke="#CBD5E1" rx="8"/>
          <text x="14" y="20" fill="#0F172A" font-size="11" font-weight="700">Variation of g Formulas</text>
          <text x="14" y="38" fill="#16A34A" font-size="11">Altitude h: g_h ≈ g (1 - 2h/R)</text>
          <text x="14" y="56" fill="#2563EB" font-size="11">Depth d: g_d = g (1 - d/R)</text>
          <text x="14" y="74" fill="#DC2626" font-size="11">At Earth Center (d=R): g = 0</text>
          <text x="14" y="90" fill="#D97706" font-size="10">Latitude λ: g' = g - ω² R cos² λ</text>
        </g>
        """
        title = title or "Variation of Acceleration Due to Gravity (g) with Distance"
        caption = caption or "Linear increase inside the Earth and inverse-square decay outside"
    else:
        # Kepler's Planetary Motion & Satellite Orbit
        inner = """
        <g transform="translate(180, 200)">
          <!-- Elliptical Orbit -->
          <ellipse cx="0" cy="0" rx="140" ry="90" fill="none" stroke="#2563EB" stroke-width="2"/>
          <!-- Sun at Focus F1 (-70, 0) -->
          <circle cx="-65" cy="0" r="16" fill="#F59E0B" stroke="#D97706" stroke-width="2"/>
          <text x="-65" y="4" fill="#FFFFFF" font-size="10" font-weight="700" text-anchor="middle">Sun</text>
          <text x="-65" y="26" fill="#D97706" font-size="10" font-weight="600" text-anchor="middle">Focus S</text>
          <!-- Perihelion (closest) -->
          <circle cx="-140" cy="0" r="8" fill="#3B82F6"/>
          <text x="-140" y="-12" fill="#3B82F6" font-size="10" font-weight="700" text-anchor="middle">Perihelion (v_max)</text>
          <line x1="-140" y1="0" x2="-140" y2="-40" stroke="#DC2626" stroke-width="2" marker-end="url(#arrowRed)"/>
          <!-- Aphelion (farthest) -->
          <circle cx="140" cy="0" r="8" fill="#3B82F6"/>
          <text x="140" y="-12" fill="#3B82F6" font-size="10" font-weight="700" text-anchor="middle">Aphelion (v_min)</text>
          <line x1="140" y1="0" x2="140" y2="-25" stroke="#DC2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
          <!-- Areal velocity sweep sectors: Area A1 and Area A2 -->
          <path d="M -65 0 L -140 0 A 140 90 0 0 1 -125 -42 Z" fill="rgba(245, 158, 11, 0.25)" stroke="#D97706" stroke-width="1.2"/>
          <text x="-115" y="-15" fill="#D97706" font-size="10" font-weight="700">Area 1</text>
          <path d="M -65 0 L 140 0 A 140 90 0 0 0 130 35 Z" fill="rgba(37, 99, 235, 0.25)" stroke="#2563EB" stroke-width="1.2"/>
          <text x="100" y="18" fill="#2563EB" font-size="10" font-weight="700">Area 2</text>
        </g>
        <g id="hud" transform="translate(360, 60)">
          <rect width="210" height="95" fill="#F8FAFC" stroke="#CBD5E1" rx="8"/>
          <text x="14" y="20" fill="#0F172A" font-size="11" font-weight="700">Kepler's Laws of Planetary Motion</text>
          <text x="14" y="38" fill="#2563EB" font-size="11">1. Law of Orbits: Ellipse with Sun at focus</text>
          <text x="14" y="56" fill="#D97706" font-size="11">2. Law of Areas: dA/dt = L / 2m = const</text>
          <text x="14" y="74" fill="#16A34A" font-size="11">3. Law of Periods: T² ∝ a³</text>
          <text x="14" y="90" fill="#DC2626" font-size="10">Escape Speed: v_e = √(2GM/R) = 11.2 km/s</text>
        </g>
        """
        title = title or "Kepler's Laws of Planetary Motion & Elliptical Orbits"
        caption = caption or "Equal areas swept in equal time intervals due to conservation of angular momentum"
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=380)
