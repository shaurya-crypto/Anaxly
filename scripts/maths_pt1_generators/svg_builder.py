"""
High-Precision Vector SVG Builder for Class 9 Mathematics (Ganita Manjari Grade 9 Part 1)
Follows /unslop and /hairline-create design standards:
- Elegant, crisp vector geometry with exact coordinates
- Balanced contrast on subtle slate/neutral backgrounds
- Legible mathematical notation and labels
- Responsive viewBox (580 x 360 standard)
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
  </defs>
  <rect width="{width}" height="{height}" fill="#FFFFFF" rx="12"/>
  <rect width="{width}" height="{height}" fill="url(#gridPattern)" rx="12"/>
  {header_html}
  {inner_svg}
</svg>""".strip()


def build_cartesian_svg(domain=(-6, 6), range_y=(-6, 6), points=None, lines=None, polygons=None, title="", caption=""):
    """
    Renders a true Cartesian coordinate system with crisp axes, grid ticks, and plotted geometric objects.
    """
    width, height = 580, 360
    
    # Scale calculation
    dx = domain[1] - domain[0]
    dy = range_y[1] - range_y[0]
    sx = (width - 120) / dx if dx else 30
    sy = (height - 120) / dy if dy else 30
    scale = min(sx, sy)
    
    # Adjust origin based on domain and range
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
            svg_elements.append(f'<line x1="{ox-3}" y1="{py}" x2="{ox+3}" stroke="#94A3B8" stroke-width="1.2"/>')
            if y != 0 and (y % 2 == 0 or dy <= 8):
                svg_elements.append(f'<text x="{ox-8}" y="{py+3}" fill="#64748B" font-size="10" text-anchor="end">{y}</text>')

    # Axes
    svg_elements.append(f'<line x1="40" y1="{oy}" x2="{width-40}" y2="{oy}" stroke="#334155" stroke-width="1.8" marker-end="url(#arrowSlate)"/>')
    svg_elements.append(f'<line x1="{ox}" y1="{height-40}" x2="{ox}" y2="60" stroke="#334155" stroke-width="1.8" marker-end="url(#arrowSlate)"/>')
    svg_elements.append(f'<text x="{width-32}" y="{oy+4}" fill="#334155" font-size="12" font-weight="700">X</text>')
    svg_elements.append(f'<text x="{ox-4}" y="52" fill="#334155" font-size="12" font-weight="700" text-anchor="end">Y</text>')
    svg_elements.append(f'<text x="{ox-8}" y="{oy+16}" fill="#64748B" font-size="11" font-weight="600">O</text>')

    # Polygons
    if polygons:
        for poly in polygons:
            pts = poly.get('points', [])
            svg_pts = []
            for pt in pts:
                px = ox + pt[0] * scale
                py = oy - pt[1] * scale
                svg_pts.append(f"{px},{py}")
            fill = poly.get('fill', 'rgba(37, 99, 235, 0.08)')
            stroke = poly.get('stroke', '#2563EB')
            width_s = poly.get('stroke_width', 1.8)
            svg_elements.append(f'<polygon points="{" ".join(svg_pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{width_s}"/>')

    # Lines
    if lines:
        for ln in lines:
            p1, p2 = ln.get('p1'), ln.get('p2')
            x1, y1 = ox + p1[0] * scale, oy - p1[1] * scale
            x2, y2 = ox + p2[0] * scale, oy - p2[1] * scale
            color = ln.get('color', '#2563EB')
            w_line = ln.get('stroke_width', 2)
            dash = f' stroke-dasharray="{ln["dash"]}"' if 'dash' in ln else ""
            svg_elements.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w_line}"{dash}/>')
            if 'label' in ln:
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                svg_elements.append(f'<rect x="{mx-24}" y="{my-16}" width="48" height="14" rx="4" fill="#FFFFFF" opacity="0.9"/>')
                svg_elements.append(f'<text x="{mx}" y="{my-6}" fill="{color}" font-size="10" font-weight="600" text-anchor="middle">{ln["label"]}</text>')

    # Points
    if points:
        for pt in points:
            x, y = pt['x'], pt['y']
            px = ox + x * scale
            py = oy - y * scale
            color = pt.get('color', '#2563EB')
            r = pt.get('r', 4.5)
            svg_elements.append(f'<circle cx="{px}" cy="{py}" r="{r}" fill="{color}" stroke="#FFFFFF" stroke-width="1.5"/>')
            label = pt.get('label', '')
            if label:
                sub = pt.get('sub', f"({x}, {y})")
                dx_l = pt.get('dx', 8)
                dy_l = pt.get('dy', -8)
                anchor = pt.get('anchor', 'start')
                svg_elements.append(f'<text x="{px + dx_l}" y="{py + dy_l}" fill="#0F172A" font-size="11" font-weight="700" text-anchor="{anchor}">{label} <tspan fill="#64748B" font-size="9" font-weight="500">{sub}</tspan></text>')

    return get_svg_wrapper("\n  ".join(svg_elements), title=title, caption=caption, width=width, height=height)


def build_circle_geometry_svg(radius=90, center=(290, 200), chords=None, angles=None, points=None, triangles=None, title="", caption=""):
    """
    Renders clean circle geometry with theorems, radii, chords, perpendiculars, and concyclic points.
    """
    cx, cy = center
    svg_elements = []
    
    # Main Circle
    svg_elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="#F8FAFC" stroke="#2563EB" stroke-width="2"/>')
    svg_elements.append(f'<circle cx="{cx}" cy="{cy}" r="3.5" fill="#DC2626"/>')
    svg_elements.append(f'<text x="{cx-12}" y="{cy-8}" fill="#DC2626" font-size="12" font-weight="700">O</text>')
    
    # Triangles inside circle
    if triangles:
        for tri in triangles:
            pts = tri.get('points', [])
            svg_pts = [f"{p[0]},{p[1]}" for p in pts]
            fill = tri.get('fill', 'rgba(37,99,235,0.08)')
            stroke = tri.get('stroke', '#2563EB')
            w = tri.get('stroke_width', 1.8)
            svg_elements.append(f'<polygon points="{" ".join(svg_pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{w}"/>')

    # Chords
    if chords:
        for chord in chords:
            x1, y1 = chord['p1']
            x2, y2 = chord['p2']
            color = chord.get('color', '#0F172A')
            w = chord.get('stroke_width', 2)
            svg_elements.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"/>')
            if 'label' in chord:
                mx, my = (x1 + x2)/2, (y1 + y2)/2
                svg_elements.append(f'<text x="{mx}" y="{my-6}" fill="{color}" font-size="11" font-weight="600" text-anchor="middle">{chord["label"]}</text>')
            if 'midpoint' in chord:
                mx, my = chord['midpoint']
                svg_elements.append(f'<circle cx="{mx}" cy="{my}" r="3" fill="#16A34A"/>')
                svg_elements.append(f'<line x1="{cx}" y1="{cy}" x2="{mx}" y2="{my}" stroke="#16A34A" stroke-width="1.5" stroke-dasharray="4,3"/>')
                svg_elements.append(f'<rect x="{mx-5}" y="{my-5}" width="8" height="8" fill="none" stroke="#16A34A" stroke-width="1"/>')
                svg_elements.append(f'<text x="{mx+8}" y="{my+4}" fill="#16A34A" font-size="10" font-weight="600">{chord.get("midpoint_label", "M")}</text>')

    # Angles / Radii
    if angles:
        for ang in angles:
            if 'points' in ang:
                pts = ang['points']
            elif 'center' in ang and 'p1' in ang and 'p2' in ang:
                pts = [ang['p1'], ang['center'], ang['p2']]
            else:
                continue
            svg_elements.append(f'<line x1="{pts[1][0]}" y1="{pts[1][1]}" x2="{pts[0][0]}" y2="{pts[0][1]}" stroke="#0284C7" stroke-width="1.4" stroke-dasharray="3,3"/>')
            svg_elements.append(f'<line x1="{pts[1][0]}" y1="{pts[1][1]}" x2="{pts[2][0]}" y2="{pts[2][1]}" stroke="#0284C7" stroke-width="1.4" stroke-dasharray="3,3"/>')
            if 'subtended_p' in ang:
                sp = ang['subtended_p']
                svg_elements.append(f'<line x1="{sp[0]}" y1="{sp[1]}" x2="{pts[0][0]}" y2="{pts[0][1]}" stroke="#D97706" stroke-width="1.6"/>')
                svg_elements.append(f'<line x1="{sp[0]}" y1="{sp[1]}" x2="{pts[2][0]}" y2="{pts[2][1]}" stroke="#D97706" stroke-width="1.6"/>')
                svg_elements.append(f'<circle cx="{sp[0]}" cy="{sp[1]}" r="4" fill="#D97706"/>')
                svg_elements.append(f'<text x="{sp[0]}" y="{sp[1]-8}" fill="#D97706" font-size="11" font-weight="700" text-anchor="middle">{ang.get("subtended_label", "P (θ)")}</text>')
                svg_elements.append(f'<text x="{cx+6}" y="{cy+18}" fill="#0284C7" font-size="11" font-weight="700">{ang.get("center_label", "2θ")}</text>')

    # Points on circle
    if points:
        for pt in points:
            if 'pos' in pt:
                px, py = pt['pos']
            elif 'x' in pt and 'y' in pt:
                px, py = pt['x'], pt['y']
            else:
                continue
            color = pt.get('color', '#0F172A')
            svg_elements.append(f'<circle cx="{px}" cy="{py}" r="4" fill="{color}" stroke="#FFFFFF" stroke-width="1.5"/>')
            lbl = pt.get('label', '')
            dx = pt.get('dx', 8)
            dy = pt.get('dy', -6)
            svg_elements.append(f'<text x="{px+dx}" y="{py+dy}" fill="#0F172A" font-size="11" font-weight="700">{lbl}</text>')

    return get_svg_wrapper("\n  ".join(svg_elements), title=title, caption=caption)


def build_cyclic_quad_svg(radius=95, center=(290, 195), vertices=None, opposite_labels=None, title="", caption=""):
    """
    Renders circle with an inscribed cyclic quadrilateral ABCD with opposite angle sums.
    """
    cx, cy = center
    svg_elements = []
    
    # Circle
    svg_elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="#F8FAFC" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="4,3"/>')
    svg_elements.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="#64748B"/>')
    svg_elements.append(f'<text x="{cx+6}" y="{cy+4}" fill="#64748B" font-size="10">O</text>')
    
    # Normalize vertices
    default_labels = ["A", "B", "C", "D"]
    if not vertices:
        angles = [math.radians(130), math.radians(40), math.radians(-35), math.radians(-130)]
        vertices = []
        for i, (a, l) in enumerate(zip(angles, default_labels)):
            vx = cx + radius * math.cos(a)
            vy = cy - radius * math.sin(a)
            vertices.append({"pos": (vx, vy), "label": l})
    else:
        norm_vertices = []
        for i, v in enumerate(vertices):
            if isinstance(v, dict):
                pos = v.get('pos') or (v.get('x'), v.get('y'))
                lbl = v.get('label', default_labels[i % 4])
            elif isinstance(v, (list, tuple)):
                pos = (v[0], v[1])
                lbl = default_labels[i % 4]
            norm_vertices.append({"pos": pos, "label": lbl})
        vertices = norm_vertices
            
    # Polygon quad
    poly_pts = [f"{v['pos'][0]},{v['pos'][1]}" for v in vertices]
    svg_elements.append(f'<polygon points="{" ".join(poly_pts)}" fill="rgba(37,99,235,0.08)" stroke="#2563EB" stroke-width="2"/>')
    
    # Diagonals AC and BD
    if len(vertices) >= 4:
        pA, pB, pC, pD = vertices[0]['pos'], vertices[1]['pos'], vertices[2]['pos'], vertices[3]['pos']
        svg_elements.append(f'<line x1="{pA[0]}" y1="{pA[1]}" x2="{pC[0]}" y2="{pC[1]}" stroke="#94A3B8" stroke-width="1.2" stroke-dasharray="3,3"/>')
        svg_elements.append(f'<line x1="{pB[0]}" y1="{pB[1]}" x2="{pD[0]}" y2="{pD[1]}" stroke="#94A3B8" stroke-width="1.2" stroke-dasharray="3,3"/>')

    # Draw vertices & labels
    for v in vertices:
        vx, vy = v['pos']
        svg_elements.append(f'<circle cx="{vx}" cy="{vy}" r="4" fill="#0F172A" stroke="#FFFFFF" stroke-width="1.5"/>')
        lbl = v.get('label', '')
        dx = (vx - cx) * 0.16
        dy = (vy - cy) * 0.16
        svg_elements.append(f'<text x="{vx + dx}" y="{vy + dy + 4}" fill="#0F172A" font-size="12" font-weight="700" text-anchor="middle">{lbl}</text>')

    # Bottom formula banner
    svg_elements.append(f'<rect x="60" y="305" width="460" height="35" rx="6" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>')
    svg_elements.append(f'<text x="290" y="327" fill="#1E40AF" font-size="12" font-weight="700" text-anchor="middle">Theorem 11 &amp; 12: ∠A + ∠C = 180° &amp; ∠B + ∠D = 180°</text>')

    return get_svg_wrapper("\n  ".join(svg_elements), title=title, caption=caption)


def build_algebraic_dissection_svg(type_ident="a_plus_b_sq", a_val=130, b_val=60, c_val=40, title="", caption=""):
    """
    Renders geometric area dissections of algebraic identities.
    Supports: a_plus_b_sq, a_minus_b_sq, trinomial, algebra_tiles.
    """
    ox, oy = 190, 75
    svg_elements = []
    
    if type_ident == "a_plus_b_sq":
        svg_elements.append(f'<rect x="{ox}" y="{oy}" width="{a_val}" height="{a_val}" fill="#EFF6FF" stroke="#2563EB" stroke-width="2"/>')
        svg_elements.append(f'<text x="{ox + a_val/2}" y="{oy + a_val/2 + 5}" fill="#1D4ED8" font-size="16" font-weight="700" text-anchor="middle">a²</text>')
        
        svg_elements.append(f'<rect x="{ox + a_val}" y="{oy}" width="{b_val}" height="{a_val}" fill="#F0FDF4" stroke="#16A34A" stroke-width="2"/>')
        svg_elements.append(f'<text x="{ox + a_val + b_val/2}" y="{oy + a_val/2 + 5}" fill="#15803D" font-size="14" font-weight="600" text-anchor="middle">ab</text>')
        
        svg_elements.append(f'<rect x="{ox}" y="{oy + a_val}" width="{a_val}" height="{b_val}" fill="#F0FDF4" stroke="#16A34A" stroke-width="2"/>')
        svg_elements.append(f'<text x="{ox + a_val/2}" y="{oy + a_val + b_val/2 + 5}" fill="#15803D" font-size="14" font-weight="600" text-anchor="middle">ab</text>')
        
        svg_elements.append(f'<rect x="{ox + a_val}" y="{oy + a_val}" width="{b_val}" height="{b_val}" fill="#FEF3C7" stroke="#D97706" stroke-width="2"/>')
        svg_elements.append(f'<text x="{ox + a_val + b_val/2}" y="{oy + a_val + b_val/2 + 5}" fill="#B45309" font-size="14" font-weight="700" text-anchor="middle">b²</text>')
        
        svg_elements.append(f'<line x1="{ox}" y1="{oy-10}" x2="{ox+a_val}" y2="{oy-10}" stroke="#64748B" stroke-width="1.2"/>')
        svg_elements.append(f'<text x="{ox+a_val/2}" y="{oy-14}" fill="#64748B" font-size="12" font-weight="600" text-anchor="middle">a</text>')
        svg_elements.append(f'<line x1="{ox+a_val}" y1="{oy-10}" x2="{ox+a_val+b_val}" y2="{oy-10}" stroke="#64748B" stroke-width="1.2"/>')
        svg_elements.append(f'<text x="{ox+a_val+b_val/2}" y="{oy-14}" fill="#64748B" font-size="12" font-weight="600" text-anchor="middle">b</text>')
        
        svg_elements.append(f'<text x="{ox + (a_val+b_val)/2}" y="{oy + a_val + b_val + 32}" fill="#0F172A" font-size="15" font-weight="700" text-anchor="middle">(a + b)² = a² + 2ab + b²</text>')

    elif type_ident == "a_minus_b_sq":
        tot = a_val + b_val
        svg_elements.append(f'<rect x="{ox}" y="{oy}" width="{tot}" height="{tot}" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5" stroke-dasharray="4,3"/>')
        svg_elements.append(f'<rect x="{ox}" y="{oy}" width="{a_val}" height="{a_val}" fill="#EFF6FF" stroke="#2563EB" stroke-width="2"/>')
        svg_elements.append(f'<text x="{ox + a_val/2}" y="{oy + a_val/2 + 5}" fill="#1D4ED8" font-size="15" font-weight="700" text-anchor="middle">(a - b)²</text>')
        svg_elements.append(f'<rect x="{ox + a_val}" y="{oy}" width="{b_val}" height="{a_val}" fill="#FEE2E2" stroke="#DC2626" stroke-width="1.5"/>')
        svg_elements.append(f'<text x="{ox + a_val + b_val/2}" y="{oy + a_val/2 + 5}" fill="#B91C1C" font-size="11" font-weight="600" text-anchor="middle">b(a-b)</text>')
        svg_elements.append(f'<rect x="{ox}" y="{oy + a_val}" width="{tot}" height="{b_val}" fill="#FEE2E2" stroke="#DC2626" stroke-width="1.5"/>')
        svg_elements.append(f'<text x="{ox + tot/2}" y="{oy + a_val + b_val/2 + 5}" fill="#B91C1C" font-size="12" font-weight="600" text-anchor="middle">ab</text>')
        
        svg_elements.append(f'<text x="{ox + tot/2}" y="{oy + tot + 32}" fill="#0F172A" font-size="15" font-weight="700" text-anchor="middle">(a - b)² = a² - 2ab + b²</text>')

    elif type_ident == "trinomial":
        a, b, c = 90, 60, 45
        tx, ty = 190, 65
        colors = [
            ("#EFF6FF", "#2563EB", "a²"), ("#F0FDF4", "#16A34A", "ab"), ("#FEF3C7", "#D97706", "ac"),
            ("#F0FDF4", "#16A34A", "ab"), ("#F5F3FF", "#7C3AED", "b²"), ("#ECFEFF", "#0891B2", "bc"),
            ("#FEF3C7", "#D97706", "ac"), ("#ECFEFF", "#0891B2", "bc"), ("#FDF2F8", "#DB2777", "c²")
        ]
        x_offsets = [0, a, a+b]
        y_offsets = [0, a, a+b]
        widths = [a, b, c]
        heights = [a, b, c]
        
        idx = 0
        for i in range(3):
            for j in range(3):
                bg, border, lbl = colors[idx]
                rx = tx + x_offsets[j]
                ry = ty + y_offsets[i]
                rw = widths[j]
                rh = heights[i]
                svg_elements.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" fill="{bg}" stroke="{border}" stroke-width="1.5"/>')
                svg_elements.append(f'<text x="{rx + rw/2}" y="{ry + rh/2 + 4}" fill="{border}" font-size="12" font-weight="700" text-anchor="middle">{lbl}</text>')
                idx += 1
                
        svg_elements.append(f'<text x="{tx + (a+b+c)/2}" y="{ty + a + b + c + 28}" fill="#0F172A" font-size="13" font-weight="700" text-anchor="middle">(a + b + c)² = a² + b² + c² + 2ab + 2bc + 2ca</text>')

    elif type_ident == "algebra_tiles":
        x_sz, a_sz, b_sz = 120, 60, 40
        ax, ay = 200, 80
        svg_elements.append(f'<rect x="{ax}" y="{ay}" width="{x_sz}" height="{x_sz}" fill="#EFF6FF" stroke="#2563EB" stroke-width="2"/>')
        svg_elements.append(f'<text x="{ax + x_sz/2}" y="{ay + x_sz/2 + 6}" fill="#1D4ED8" font-size="16" font-weight="700" text-anchor="middle">x²</text>')
        svg_elements.append(f'<rect x="{ax + x_sz}" y="{ay}" width="{a_sz}" height="{x_sz}" fill="#F0FDF4" stroke="#16A34A" stroke-width="2"/>')
        svg_elements.append(f'<text x="{ax + x_sz + a_sz/2}" y="{ay + x_sz/2 + 6}" fill="#15803D" font-size="14" font-weight="600" text-anchor="middle">ax</text>')
        svg_elements.append(f'<rect x="{ax}" y="{ay + x_sz}" width="{x_sz}" height="{b_sz}" fill="#F0FDF4" stroke="#16A34A" stroke-width="2"/>')
        svg_elements.append(f'<text x="{ax + x_sz/2}" y="{ay + x_sz + b_sz/2 + 5}" fill="#15803D" font-size="14" font-weight="600" text-anchor="middle">bx</text>')
        svg_elements.append(f'<rect x="{ax + x_sz}" y="{ay + x_sz}" width="{a_sz}" height="{b_sz}" fill="#FEF3C7" stroke="#D97706" stroke-width="2"/>')
        svg_elements.append(f'<text x="{ax + x_sz + a_sz/2}" y="{ay + x_sz + b_sz/2 + 5}" fill="#B45309" font-size="14" font-weight="700" text-anchor="middle">ab</text>')
        
        svg_elements.append(f'<text x="{ax + (x_sz+a_sz)/2}" y="{ay + x_sz + b_sz + 32}" fill="#0F172A" font-size="15" font-weight="700" text-anchor="middle">(x + a)(x + b) = x² + (a + b)x + ab</text>')

    return get_svg_wrapper("\n  ".join(svg_elements), title=title, caption=caption)


def build_geometry_triangle_svg(pA=(290, 80), pB=(150, 260), pC=(430, 260), labels=("A", "B", "C"), side_labels=None, is_right=False, altitude=False, title="", caption=""):
    """
    Renders clean geometry triangles with vertex labels, side annotations, and right angle symbols.
    """
    svg_elements = []
    
    svg_elements.append(f'<polygon points="{pA[0]},{pA[1]} {pB[0]},{pB[1]} {pC[0]},{pC[1]}" fill="rgba(37,99,235,0.08)" stroke="#2563EB" stroke-width="2"/>')
    
    if altitude:
        pD = (pA[0], pB[1])
        svg_elements.append(f'<line x1="{pA[0]}" y1="{pA[1]}" x2="{pD[0]}" y2="{pD[1]}" stroke="#DC2626" stroke-width="1.8" stroke-dasharray="4,3"/>')
        svg_elements.append(f'<circle cx="{pD[0]}" cy="{pD[1]}" r="3" fill="#DC2626"/>')
        svg_elements.append(f'<text x="{pD[0]}" y="{pD[1]+18}" fill="#DC2626" font-size="11" font-weight="700" text-anchor="middle">D (Foot)</text>')
        svg_elements.append(f'<rect x="{pD[0]-8}" y="{pD[1]-8}" width="8" height="8" fill="none" stroke="#DC2626" stroke-width="1.2"/>')
        svg_elements.append(f'<text x="{pD[0]-14}" y="{(pA[1]+pD[1])/2}" fill="#DC2626" font-size="11" font-weight="600" text-anchor="end">h</text>')

    if is_right:
        svg_elements.append(f'<rect x="{pB[0]}" y="{pB[1]-12}" width="12" height="12" fill="none" stroke="#2563EB" stroke-width="1.2"/>')

    for pt, lbl, dy, dx in [(pA, labels[0], -10, 0), (pB, labels[1], 15, -12), (pC, labels[2], 15, 12)]:
        svg_elements.append(f'<circle cx="{pt[0]}" cy="{pt[1]}" r="4" fill="#0F172A" stroke="#FFFFFF" stroke-width="1.5"/>')
        svg_elements.append(f'<text x="{pt[0]+dx}" y="{pt[1]+dy}" fill="#0F172A" font-size="13" font-weight="700" text-anchor="middle">{lbl}</text>')

    if side_labels:
        if len(side_labels) >= 3:
            mAB = ((pA[0]+pB[0])/2 - 14, (pA[1]+pB[1])/2)
            mBC = ((pB[0]+pC[0])/2, pB[1] + 18)
            mAC = ((pA[0]+pC[0])/2 + 14, (pA[1]+pC[1])/2)
            svg_elements.append(f'<text x="{mAB[0]}" y="{mAB[1]}" fill="#16A34A" font-size="12" font-weight="600" text-anchor="end">{side_labels[0]}</text>')
            svg_elements.append(f'<text x="{mBC[0]}" y="{mBC[1]}" fill="#16A34A" font-size="12" font-weight="600" text-anchor="middle">{side_labels[1]}</text>')
            svg_elements.append(f'<text x="{mAC[0]}" y="{mAC[1]}" fill="#16A34A" font-size="12" font-weight="600" text-anchor="start">{side_labels[2]}</text>')

    return get_svg_wrapper("\n  ".join(svg_elements), title=title, caption=caption)


def build_heron_triangle_svg(a=13, b=14, c=15, title="", caption=""):
    """
    Renders triangle annotated with Heron's formula semi-perimeter s and sides a, b, c.
    """
    pA = (270, 90)
    pB = (140, 250)
    pC = (440, 250)
    side_labels = (f"c = {c}", f"a = {a}", f"b = {b}")
    return build_geometry_triangle_svg(pA, pB, pC, labels=("A", "B", "C"), side_labels=side_labels, altitude=True, title=title, caption=caption)


def build_number_line_spiral_svg(title="", caption=""):
    """
    Renders the Baudhāyana-Pythagoras Square Root Spiral (Wheel of Theodorus) on a number line.
    """
    width, height = 580, 360
    svg_elements = []
    
    y_nl = 285
    svg_elements.append(f'<line x1="40" y1="{y_nl}" x2="540" y2="{y_nl}" stroke="#334155" stroke-width="2" marker-end="url(#arrowSlate)"/>')
    
    scale = 80
    ox = 100
    for i in range(0, 6):
        px = ox + i * scale
        svg_elements.append(f'<line x1="{px}" y1="{y_nl-5}" x2="{px}" y2="{y_nl+5}" stroke="#475569" stroke-width="1.5"/>')
        svg_elements.append(f'<text x="{px}" y="{y_nl+20}" fill="#334155" font-size="12" font-weight="600" text-anchor="middle">{i}</text>')
        
    p0 = (ox, y_nl)
    p1 = (ox + scale, y_nl)
    p2 = (ox + scale, y_nl - scale)
    
    svg_elements.append(f'<polygon points="{p0[0]},{p0[1]} {p1[0]},{p1[1]} {p2[0]},{p2[1]}" fill="rgba(37,99,235,0.08)" stroke="#2563EB" stroke-width="2"/>')
    svg_elements.append(f'<line x1="{p0[0]}" y1="{p0[1]}" x2="{p2[0]}" y2="{p2[1]}" stroke="#DC2626" stroke-width="2"/>')
    svg_elements.append(f'<rect x="{p1[0]-10}" y="{p1[1]-10}" width="10" height="10" fill="none" stroke="#2563EB" stroke-width="1"/>')
    svg_elements.append(f'<text x="{p0[0] + scale/2}" y="{y_nl-6}" fill="#2563EB" font-size="11" font-weight="600">Base = 1</text>')
    svg_elements.append(f'<text x="{p1[0]+8}" y="{y_nl - scale/2}" fill="#2563EB" font-size="11" font-weight="600">Alt = 1</text>')
    svg_elements.append(f'<text x="{ox + scale/2 - 12}" y="{y_nl - scale/2 - 6}" fill="#DC2626" font-size="12" font-weight="700">√2 ≈ 1.414</text>')
    
    r_sqrt2 = scale * math.sqrt(2)
    p_drop = ox + r_sqrt2
    svg_elements.append(f'<path d="M {p2[0]} {p2[1]} A {r_sqrt2} {r_sqrt2} 0 0 1 {p_drop} {y_nl}" fill="none" stroke="#DC2626" stroke-width="1.8" stroke-dasharray="4,4"/>')
    svg_elements.append(f'<circle cx="{p_drop}" cy="{y_nl}" r="4" fill="#DC2626"/>')
    svg_elements.append(f'<text x="{p_drop}" y="{y_nl+34}" fill="#DC2626" font-size="11" font-weight="700" text-anchor="middle">√2</text>')

    hyp1_angle = math.atan2(scale, scale)
    perp_angle = hyp1_angle + math.pi/2
    p3 = (p2[0] - scale * math.cos(perp_angle), p2[1] + scale * math.sin(perp_angle))
    svg_elements.append(f'<line x1="{p2[0]}" y1="{p2[1]}" x2="{p3[0]}" y2="{p3[1]}" stroke="#16A34A" stroke-width="1.8"/>')
    svg_elements.append(f'<line x1="{p0[0]}" y1="{p0[1]}" x2="{p3[0]}" y2="{p3[1]}" stroke="#7C3AED" stroke-width="2"/>')
    svg_elements.append(f'<text x="{p3[0]-6}" y="{p3[1]-8}" fill="#7C3AED" font-size="12" font-weight="700">√3 ≈ 1.732</text>')
    
    r_sqrt3 = scale * math.sqrt(3)
    p_drop3 = ox + r_sqrt3
    svg_elements.append(f'<path d="M {p3[0]} {p3[1]} A {r_sqrt3} {r_sqrt3} 0 0 1 {p_drop3} {y_nl}" fill="none" stroke="#7C3AED" stroke-width="1.8" stroke-dasharray="4,4"/>')
    svg_elements.append(f'<circle cx="{p_drop3}" cy="{y_nl}" r="4" fill="#7C3AED"/>')
    svg_elements.append(f'<text x="{p_drop3}" y="{y_nl+34}" fill="#7C3AED" font-size="11" font-weight="700" text-anchor="middle">√3</text>')

    return get_svg_wrapper("\n  ".join(svg_elements), title=title, caption=caption)


def build_number_line_points_svg(points=None, domain=(-3, 3), title="", caption=""):
    """
    Renders number line with plotted rational points and intervals.
    """
    width, height = 580, 360
    y_nl = 190
    svg_elements = []
    
    svg_elements.append(f'<line x1="50" y1="{y_nl}" x2="530" y2="{y_nl}" stroke="#334155" stroke-width="2.5" marker-end="url(#arrowSlate)"/>')
    
    d_min, d_max = domain
    scale = 420 / (d_max - d_min)
    ox = 80 - d_min * scale
    
    # Integer ticks
    for i in range(int(math.floor(d_min)), int(math.ceil(d_max)) + 1):
        px = ox + i * scale
        if 50 <= px <= 530:
            svg_elements.append(f'<line x1="{px}" y1="{y_nl-6}" x2="{px}" y2="{y_nl+6}" stroke="#475569" stroke-width="1.5"/>')
            svg_elements.append(f'<text x="{px}" y="{y_nl+24}" fill="#334155" font-size="12" font-weight="600" text-anchor="middle">{i}</text>')

    # Plotted points
    if points:
        for pt in points:
            val = pt['val']
            px = ox + val * scale
            col = pt.get('color', '#DC2626')
            lbl = pt.get('label', str(val))
            svg_elements.append(f'<circle cx="{px}" cy="{y_nl}" r="5" fill="{col}" stroke="#FFFFFF" stroke-width="2"/>')
            svg_elements.append(f'<line x1="{px}" y1="{y_nl-8}" x2="{px}" y2="{y_nl-30}" stroke="{col}" stroke-width="1.5"/>')
            svg_elements.append(f'<text x="{px}" y="{y_nl-36}" fill="{col}" font-size="12" font-weight="700" text-anchor="middle">{lbl}</text>')

    return get_svg_wrapper("\n  ".join(svg_elements), title=title, caption=caption)


def build_running_track_svg(title="", caption=""):
    """
    Renders 400m athletics track with straightaways, semicircles, and lane stagger geometry.
    """
    width, height = 580, 360
    svg_elements = []
    
    cx1, cx2 = 210, 370
    cy = 190
    r1 = 60
    w_lane = 18
    r2 = r1 + w_lane
    
    path_inner = f"""
    M {cx1} {cy-r1} L {cx2} {cy-r1} 
    A {r1} {r1} 0 0 1 {cx2} {cy+r1} 
    L {cx1} {cy+r1} 
    A {r1} {r1} 0 0 1 {cx1} {cy-r1} Z
    """
    path_outer = f"""
    M {cx1} {cy-r2} L {cx2} {cy-r2} 
    A {r2} {r2} 0 0 1 {cx2} {cy+r2} 
    L {cx1} {cy+r2} 
    A {r2} {r2} 0 0 1 {cx1} {cy-r2} Z
    """
    svg_elements.append(f'<path d="{path_outer}" fill="#FEF3C7" stroke="#D97706" stroke-width="2"/>')
    svg_elements.append(f'<path d="{path_inner}" fill="#FFFFFF" stroke="#2563EB" stroke-width="2"/>')
    
    svg_elements.append(f'<rect x="{cx1}" y="{cy-r1+6}" width="{cx2-cx1}" height="{2*r1-12}" fill="#F0FDF4" rx="4"/>')
    svg_elements.append(f'<text x="{(cx1+cx2)/2}" y="{cy}" fill="#16A34A" font-size="12" font-weight="600" text-anchor="middle">Infield Grass</text>')
    
    svg_elements.append(f'<line x1="{cx1}" y1="{cy-r1}" x2="{cx2}" y2="{cy-r1}" stroke="#1E293B" stroke-width="2"/>')
    svg_elements.append(f'<text x="{(cx1+cx2)/2}" y="{cy-r1-8}" fill="#1E293B" font-size="11" font-weight="700" text-anchor="middle">Straightaway = 84.39 m</text>')
    
    svg_elements.append(f'<line x1="{cx1}" y1="{cy}" x2="{cx1}" y2="{cy-r1}" stroke="#2563EB" stroke-width="1.5" stroke-dasharray="3,3"/>')
    svg_elements.append(f'<text x="{cx1-8}" y="{cy - r1/2}" fill="#2563EB" font-size="10" font-weight="600" text-anchor="end">R₁ = 36.5 m</text>')
    
    svg_elements.append(f'<rect x="40" y="275" width="500" height="50" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>')
    svg_elements.append(f'<text x="50" y="295" fill="#0F172A" font-size="11" font-weight="700">Lane Stagger Formula: Δ = 2π × w = 2 × (22/7) × 1.22 m = 7.67 m</text>')
    svg_elements.append(f'<text x="50" y="312" fill="#64748B" font-size="10">Runner in lane 2 starts 7.67 m ahead of runner in lane 1 to equalize total distance to 400 m.</text>')

    return get_svg_wrapper("\n  ".join(svg_elements), title=title, caption=caption)


def build_probability_scale_tree_svg(type_prob="scale", title="", caption=""):
    """
    Renders probability scales, tree diagrams, or geometric target areas.
    """
    width, height = 580, 360
    svg_elements = []
    
    if type_prob == "scale":
        y_sc = 180
        svg_elements.append(f'<line x1="80" y1="{y_sc}" x2="500" y2="{y_sc}" stroke="#334155" stroke-width="4"/>')
        
        benchmarks = [
            (80, "0", "Impossible", "#DC2626"),
            (185, "0.25", "Unlikely", "#EA580C"),
            (290, "0.50", "Even Chance (50-50)", "#2563EB"),
            (395, "0.75", "Likely", "#0D9488"),
            (500, "1.0", "Certain", "#16A34A")
        ]
        for bx, val, desc, col in benchmarks:
            svg_elements.append(f'<circle cx="{bx}" cy="{y_sc}" r="6" fill="{col}" stroke="#FFFFFF" stroke-width="2"/>')
            svg_elements.append(f'<text x="{bx}" y="{y_sc - 18}" fill="{col}" font-size="13" font-weight="700" text-anchor="middle">{val}</text>')
            svg_elements.append(f'<text x="{bx}" y="{y_sc + 26}" fill="#0F172A" font-size="11" font-weight="600" text-anchor="middle">{desc}</text>')
            
        svg_elements.append(f'<rect x="80" y="240" width="420" height="45" rx="8" fill="#F1F5F9"/>')
        svg_elements.append(f'<text x="290" y="268" fill="#334155" font-size="12" font-weight="600" text-anchor="middle">Invariant: For any event E, 0 ≤ P(E) ≤ 1 and P(E) + P(not E) = 1</text>')

    elif type_prob == "tree":
        ox = 80
        oy = 180
        svg_elements.append(f'<circle cx="{ox}" cy="{oy}" r="6" fill="#334155"/>')
        svg_elements.append(f'<text x="{ox-10}" y="{oy+4}" fill="#334155" font-size="11" font-weight="700" text-anchor="end">Start</text>')
        
        t1_x = 220
        svg_elements.append(f'<line x1="{ox}" y1="{oy}" x2="{t1_x}" y2="{oy-60}" stroke="#2563EB" stroke-width="2"/>')
        svg_elements.append(f'<line x1="{ox}" y1="{oy}" x2="{t1_x}" y2="{oy+60}" stroke="#2563EB" stroke-width="2"/>')
        svg_elements.append(f'<text x="140" y="{oy-40}" fill="#2563EB" font-size="11" font-weight="600">H (1/2)</text>')
        svg_elements.append(f'<text x="140" y="{oy+48}" fill="#2563EB" font-size="11" font-weight="600">T (1/2)</text>')
        
        t2_x = 380
        svg_elements.append(f'<line x1="{t1_x}" y1="{oy-60}" x2="{t2_x}" y2="{oy-90}" stroke="#16A34A" stroke-width="1.8"/>')
        svg_elements.append(f'<line x1="{t1_x}" y1="{oy-60}" x2="{t2_x}" y2="{oy-30}" stroke="#16A34A" stroke-width="1.8"/>')
        svg_elements.append(f'<text x="300" y="{oy-84}" fill="#16A34A" font-size="10">H (1/2)</text>')
        svg_elements.append(f'<text x="300" y="{oy-36}" fill="#16A34A" font-size="10">T (1/2)</text>')
        
        svg_elements.append(f'<line x1="{t1_x}" y1="{oy+60}" x2="{t2_x}" y2="{oy+30}" stroke="#16A34A" stroke-width="1.8"/>')
        svg_elements.append(f'<line x1="{t1_x}" y1="{oy+60}" x2="{t2_x}" y2="{oy+90}" stroke="#16A34A" stroke-width="1.8"/>')
        svg_elements.append(f'<text x="300" y="{oy+36}" fill="#16A34A" font-size="10">H (1/2)</text>')
        svg_elements.append(f'<text x="300" y="{oy+84}" fill="#16A34A" font-size="10">T (1/2)</text>')
        
        outcomes = [
            (t2_x, oy-90, "HH", "1/4 = 0.25"),
            (t2_x, oy-30, "HT", "1/4 = 0.25"),
            (t2_x, oy+30, "TH", "1/4 = 0.25"),
            (t2_x, oy+90, "TT", "1/4 = 0.25")
        ]
        for ox2, oy2, code, prob in outcomes:
            svg_elements.append(f'<circle cx="{ox2}" cy="{oy2}" r="4" fill="#0F172A"/>')
            svg_elements.append(f'<text x="{ox2+12}" y="{oy2+4}" fill="#0F172A" font-size="12" font-weight="700">{code} <tspan fill="#64748B" font-size="10" font-weight="500">→ P = {prob}</tspan></text>')

    elif type_prob == "target":
        tx, ty = 290, 190
        radii = [(100, "#EFF6FF", "#3B82F6", "Outer Target (r = 10)"), (60, "#FEF3C7", "#F59E0B", "Middle Ring (r = 6)"), (25, "#FEE2E2", "#EF4444", "Bullseye (r = 2.5)")]
        for r, bg, border, lbl in radii:
            svg_elements.append(f'<circle cx="{tx}" cy="{ty}" r="{r}" fill="{bg}" stroke="{border}" stroke-width="2"/>')
        svg_elements.append(f'<circle cx="{tx}" cy="{ty}" r="3" fill="#DC2626"/>')
        svg_elements.append(f'<rect x="80" y="305" width="420" height="35" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>')
        svg_elements.append(f'<text x="290" y="327" fill="#0F172A" font-size="11" font-weight="700" text-anchor="middle">Geometric Probability: P(Hit Target Region) = Area(Region) / Total Area</text>')

    return get_svg_wrapper("\n  ".join(svg_elements), title=title, caption=caption)


def build_sierpinski_triangle_svg(title="", caption=""):
    """
    Renders the Sierpiński Triangle fractal showing recursive geometric progression (1, 3, 9, 27).
    """
    width, height = 580, 360
    svg_elements = []
    
    stages = [
        ("Stage 0 (1)", 110, 180, 70, 0),
        ("Stage 1 (3)", 250, 180, 70, 1),
        ("Stage 2 (9)", 390, 180, 70, 2),
    ]
    
    for lbl, cx, cy, sz, d in stages:
        svg_elements.append(f'<text x="{cx}" y="110" fill="#0F172A" font-size="12" font-weight="700" text-anchor="middle">{lbl}</text>')
        h = sz * (math.sqrt(3)/2)
        p1 = (cx, cy - h/2)
        p2 = (cx - sz/2, cy + h/2)
        p3 = (cx + sz/2, cy + h/2)
        svg_elements.append(f'<polygon points="{p1[0]},{p1[1]} {p2[0]},{p2[1]} {p3[0]},{p3[1]}" fill="#2563EB" stroke="#1D4ED8" stroke-width="1.2"/>')
        if d >= 1:
            m12 = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
            m23 = ((p2[0] + p3[0])/2, (p2[1] + p3[1])/2)
            m31 = ((p3[0] + p1[0])/2, (p3[1] + p1[1])/2)
            svg_elements.append(f'<polygon points="{m12[0]},{m12[1]} {m23[0]},{m23[1]} {m31[0]},{m31[1]}" fill="#FFFFFF" stroke="#1D4ED8" stroke-width="1"/>')
        if d >= 2:
            sub_tris = [
                (p1, m12, m31),
                (m12, p2, m23),
                (m31, m23, p3)
            ]
            for a, b, c in sub_tris:
                sm12 = ((a[0] + b[0])/2, (a[1] + b[1])/2)
                sm23 = ((b[0] + c[0])/2, (b[1] + c[1])/2)
                sm31 = ((c[0] + a[0])/2, (c[1] + a[1])/2)
                svg_elements.append(f'<polygon points="{sm12[0]},{sm12[1]} {sm23[0]},{sm23[1]} {sm31[0]},{sm31[1]}" fill="#FFFFFF" stroke="#1D4ED8" stroke-width="0.8"/>')
                
    svg_elements.append(f'<rect x="80" y="270" width="420" height="45" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>')
    svg_elements.append(f'<text x="290" y="290" fill="#0F172A" font-size="11" font-weight="700" text-anchor="middle">GP Formulation: Number of shaded triangles = 3ⁿ (1, 3, 9, 27, ...)</text>')
    svg_elements.append(f'<text x="290" y="306" fill="#64748B" font-size="10" text-anchor="middle">Total shaded area decays by common ratio r = 3/4: Area(n) = (3/4)ⁿ × A₀</text>')

    return get_svg_wrapper("\n  ".join(svg_elements), title=title, caption=caption)


def build_triangular_numbers_dot_svg(title="", caption=""):
    """
    Renders triangular numbers T_1=1, T_2=3, T_3=6, T_4=10 dot arrays with formula n(n+1)/2.
    """
    width, height = 580, 360
    svg_elements = []
    
    configs = [
        ("T₁ = 1", 100, 200, 1),
        ("T₂ = 3", 210, 200, 2),
        ("T₃ = 6", 330, 200, 3),
        ("T₄ = 10", 460, 200, 4),
    ]
    
    spacing = 18
    for lbl, base_x, base_y, n in configs:
        svg_elements.append(f'<text x="{base_x}" y="110" fill="#0F172A" font-size="13" font-weight="700" text-anchor="middle">{lbl}</text>')
        for row in range(1, n + 1):
            row_y = base_y - (n - row) * spacing
            start_x = base_x - (row - 1) * spacing / 2
            for col in range(row):
                dot_x = start_x + col * spacing
                svg_elements.append(f'<circle cx="{dot_x}" cy="{row_y}" r="4.5" fill="#2563EB" stroke="#FFFFFF" stroke-width="1"/>')
                
    svg_elements.append(f'<rect x="80" y="275" width="420" height="40" rx="8" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>')
    svg_elements.append(f'<text x="290" y="299" fill="#1E40AF" font-size="13" font-weight="700" text-anchor="middle">Gauss Triangular Formula: Tₙ = 1 + 2 + ... + n = n(n + 1) / 2</text>')

    return get_svg_wrapper("\n  ".join(svg_elements), title=title, caption=caption)


def build_bouncing_ball_decay_svg(title="", caption=""):
    """
    Renders bouncing ball height decay curves demonstrating geometric progression h_n = h_0 * r^n.
    """
    width, height = 580, 360
    svg_elements = []
    
    y_ground = 260
    svg_elements.append(f'<line x1="40" y1="{y_ground}" x2="540" y2="{y_ground}" stroke="#334155" stroke-width="2.5"/>')
    svg_elements.append(f'<text x="535" y="{y_ground+18}" fill="#64748B" font-size="10" text-anchor="end">Ground</text>')
    
    bounces = [
        {"x_start": 70, "x_end": 180, "peak_h": 110, "label": "h₁ = 60m"},
        {"x_start": 180, "x_end": 280, "peak_h": 66, "label": "h₂ = 36m"},
        {"x_start": 280, "x_end": 370, "peak_h": 40, "label": "h₃ = 21.6m"},
        {"x_start": 370, "x_end": 445, "peak_h": 24, "label": "h₄ = 13m"},
    ]
    
    svg_elements.append(f'<line x1="70" y1="80" x2="70" y2="{y_ground}" stroke="#DC2626" stroke-width="2" stroke-dasharray="3,3"/>')
    svg_elements.append(f'<circle cx="70" cy="80" r="6" fill="#DC2626"/>')
    svg_elements.append(f'<text x="70" y="70" fill="#DC2626" font-size="12" font-weight="700" text-anchor="middle">h₀ = 100 m</text>')
    
    for b in bounces:
        xs = b["x_start"]
        xe = b["x_end"]
        xm = (xs + xe) / 2
        pk = y_ground - b["peak_h"]
        svg_elements.append(f'<path d="M {xs} {y_ground} Q {xm} {pk - b["peak_h"]*0.8} {xe} {y_ground}" fill="none" stroke="#2563EB" stroke-width="2"/>')
        svg_elements.append(f'<circle cx="{xm}" cy="{pk}" r="4.5" fill="#2563EB"/>')
        svg_elements.append(f'<text x="{xm}" y="{pk-8}" fill="#2563EB" font-size="10" font-weight="600" text-anchor="middle">{b["label"]}</text>')

    svg_elements.append(f'<rect x="70" y="285" width="440" height="35" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>')
    svg_elements.append(f'<text x="290" y="307" fill="#0F172A" font-size="11" font-weight="700" text-anchor="middle">Geometric Progression: hₙ = h₀ × rⁿ with common damping ratio r = 0.60</text>')

    return get_svg_wrapper("\n  ".join(svg_elements), title=title, caption=caption)
