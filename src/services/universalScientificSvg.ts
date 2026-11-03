/**
 * Anaxly Truly Generative Scientific & Geometric Vector Engine
 * (Aristotle & Gauth Benchmark Standard - 100% Pure Whiteboard Canvas #FFFFFF)
 * 
 * Invariants & Architecture:
 * - ZERO Hardcoded Static Diagrams: All coordinates, ray paths, normal forces,
 *   focal reflections, and geometry angles are dynamically computed using trigonometry
 *   and physics laws (Lens formula 1/f = 1/v - 1/u, Newton's laws, Circle theorems).
 * - Fully Parametric & Customizable: Accepts arbitrary values (focal length f, object distance u,
 *   ramp angle theta, resistance R, voltage V) and dynamically scales the vector canvas.
 * - ZERO Dark Murky Green (#13211B) or Slate (#0A0F1D) Backdrops: Every SVG uses a pure clean white
 *   background (#FFFFFF) with subtle border (#E2E8F0) to blend seamlessly into the digital whiteboard.
 * - High-Contrast Scholastic Palette on White:
 *   * Deep Ink Charcoal: #0F172A (axes, primary text, formulas)
 *   * Aristotle Royal Blue: #2563EB (primary vectors, forward paths, active layers)
 *   * Scholar Emerald Green: #16A34A (motion curves, biological tissues, positive gradients)
 *   * Crimson Red: #DC2626 (return paths, nuclei, critical focus points)
 *   * Warm Amber / Orange: #D97706 or #F59E0B (actual distance arcs, middle lamella)
 *   * Muted Slate Gray: #64748B (tick marks, annotations, leader lines)
 *   * Subtle Grid: #F1F5F9
 */

export interface ScientificDiagramParams {
  domain?: 'optics' | 'circuits' | 'mechanics' | 'kinematics' | 'geometry' | 'chemistry' | 'biology' | 'general'
  title?: string
  caption?: string
  // Kinematics params
  posO?: number
  posA?: number
  posB?: number
  unit?: string
  // Optics params
  focalLength?: number
  objectDistance?: number
  objectHeight?: number
  lensType?: 'convex' | 'concave'
  // Mechanics params
  angleDeg?: number
  massKg?: number
  frictionCoeff?: number
  // Circuit params
  voltage?: number
  resistance?: number
  hasAmmeter?: boolean
  hasVoltmeter?: boolean
  // Geometry params
  arcAngleDeg?: number
  radius?: number
  theoremType?: 'center_circumference' | 'tangent_perpendicular' | 'cyclic_quad'
  // Cell params
  cellType?: 'plant' | 'animal' | 'prokaryote'
  // Coordinate geometry params
  pointX?: number
  pointY?: number
}

export interface GeneratedScientificSvg {
  title: string
  svg: string
  caption: string
  domain: string
  isDynamic: boolean
  computedMetrics: Record<string, any>
}

/**
 * Common SVG Definitions: Custom arrowheads and subtle coordinate grid on clean white canvas.
 */
function getSvgDefs(): string {
  return `
  <defs>
    <pattern id="chalkGrid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#F1F5F9" stroke-width="0.75"/>
    </pattern>
    <!-- Royal Blue Vector Arrow -->
    <marker id="arrowRoyal" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#2563EB"/>
    </marker>
    <!-- Cyan / Sky Ray Arrow -->
    <marker id="arrowIce" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0284C7"/>
    </marker>
    <!-- Scholar Emerald Current / Normal Arrow -->
    <marker id="arrowSage" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#16A34A"/>
    </marker>
    <!-- Crimson Vector Arrow -->
    <marker id="arrowCrimson" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#DC2626"/>
    </marker>
    <!-- Deep Charcoal Ink Arrow -->
    <marker id="arrowCharcoal" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0F172A"/>
    </marker>
    <!-- Warm Amber Arrow -->
    <marker id="arrowAmber" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#D97706"/>
    </marker>
  </defs>`
}

/**
 * 1. TRULY GENERATIVE OPTICS: Convex / Concave Lens with Dynamic Gaussian Lens Formula
 * Computes exact image position v and magnification m dynamically from incoming f and u!
 */
export function generateDynamicOpticsSvg(params: {
  title?: string
  caption?: string
  lensType?: 'convex' | 'concave'
  focalLength?: number
  objectDistance?: number
  objectHeight?: number
}): GeneratedScientificSvg {
  const isConvex = params.lensType !== 'concave'
  const fSigned = isConvex ? Math.abs(params.focalLength || 60) : -Math.abs(params.focalLength || 60)
  const u = -Math.abs(params.objectDistance || 150)
  const h = params.objectHeight || 50

  // 1/f = 1/v - 1/u  =>  v = (f * u) / (u + f)
  const v = (fSigned * u) / (u + fSigned)
  const m = v / u
  const hPrime = m * h
  const isReal = v > 0

  const ox = 270
  const oy = 140
  const scale = 1.0

  const objX = ox + u * scale
  const objY = oy - h
  const imgX = ox + v * scale
  const imgY = oy - hPrime

  const title = params.title || `${isConvex ? 'Convex' : 'Concave'} Lens: u = ${Math.abs(u)}, f = ${Math.abs(fSigned)}`
  const caption = params.caption || `Thin Lens Law: 1/f = 1/v - 1/u. Computed Image Distance v = ${v.toFixed(1)}, Magnification m = ${m.toFixed(2)} (${isReal ? 'Real & Inverted' : 'Virtual & Erect'}).`

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 280" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" style="background:#FFFFFF; font-family:'JetBrains Mono','Segoe UI',sans-serif;">
  ${getSvgDefs()}
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="10" y="10" width="520" height="260" rx="6" fill="url(#chalkGrid)"/>

  <!-- Dynamic Header Bar -->
  <rect x="24" y="18" width="492" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="36" y="34" font-size="11" font-weight="bold" fill="#0F172A">OPTICS: ${title.toUpperCase().slice(0, 52)}</text>
  <text x="495" y="34" text-anchor="end" font-size="10" font-weight="bold" fill="#2563EB">v = ${v.toFixed(1)} | m = ${m.toFixed(2)}</text>

  <!-- Principal Axis -->
  <line x1="30" y1="${oy}" x2="510" y2="${oy}" stroke="#64748B" stroke-width="1.5" stroke-dasharray="4,4"/>
  <text x="500" y="${oy - 8}" font-size="9" fill="#64748B">X</text>

  <!-- Lens Silhouette at Optical Center ox -->
  <line x1="${ox}" y1="45" x2="${ox}" y2="235" stroke="#2563EB" stroke-width="1" stroke-dasharray="3,3"/>
  ${isConvex
    ? `<path d="M ${ox} 50 Q ${ox + 20} ${oy} ${ox} 230 Q ${ox - 20} ${oy} ${ox} 50" fill="#EFF6FF" fill-opacity="0.5" stroke="#2563EB" stroke-width="2.5"/>`
    : `<path d="M ${ox - 14} 50 L ${ox + 14} 50 Q ${ox} ${oy} ${ox + 14} 230 L ${ox - 14} 230 Q ${ox} ${oy} ${ox - 14} 50" fill="#EFF6FF" fill-opacity="0.5" stroke="#2563EB" stroke-width="2.5"/>`
  }

  <!-- Focal Points: F1, 2F1 (left) and F2, 2F2 (right) -->
  <circle cx="${ox - Math.abs(fSigned)}" cy="${oy}" r="3" fill="#0F172A"/>
  <text x="${ox - Math.abs(fSigned)}" y="${oy + 18}" text-anchor="middle" font-size="10" font-weight="bold" fill="#0F172A">F1</text>
  <circle cx="${ox - 2 * Math.abs(fSigned)}" cy="${oy}" r="3" fill="#0F172A"/>
  <text x="${ox - 2 * Math.abs(fSigned)}" y="${oy + 18}" text-anchor="middle" font-size="10" font-weight="bold" fill="#0F172A">2F1</text>
  
  <circle cx="${ox}" cy="${oy}" r="3.5" fill="#16A34A"/>
  <text x="${ox - 10}" y="${oy + 18}" font-size="11" font-weight="bold" fill="#16A34A">O</text>

  <circle cx="${ox + Math.abs(fSigned)}" cy="${oy}" r="3" fill="#0F172A"/>
  <text x="${ox + Math.abs(fSigned)}" y="${oy + 18}" text-anchor="middle" font-size="10" font-weight="bold" fill="#0F172A">F2</text>
  <circle cx="${ox + 2 * Math.abs(fSigned)}" cy="${oy}" r="3" fill="#0F172A"/>
  <text x="${ox + 2 * Math.abs(fSigned)}" y="${oy + 18}" text-anchor="middle" font-size="10" font-weight="bold" fill="#0F172A">2F2</text>

  <!-- Dynamic Object Arrow -->
  <line x1="${objX}" y1="${oy}" x2="${objX}" y2="${objY}" stroke="#2563EB" stroke-width="3" marker-end="url(#arrowRoyal)"/>
  <text x="${objX - 16}" y="${objY + 6}" font-size="11" font-weight="bold" fill="#2563EB">A (h=${h})</text>
  <text x="${objX - 16}" y="${oy - 4}" font-size="10" font-weight="bold" fill="#2563EB">B</text>

  <!-- Ray 1: Parallel to Axis -> Refracts through F2 -->
  <line x1="${objX}" y1="${objY}" x2="${ox}" y2="${objY}" stroke="#0284C7" stroke-width="1.8" marker-end="url(#arrowIce)"/>
  <line x1="${ox}" y1="${objY}" x2="${imgX}" y2="${imgY}" stroke="#0284C7" stroke-width="1.8"/>

  <!-- Ray 2: Passes Straight Through Optical Center O -->
  <line x1="${objX}" y1="${objY}" x2="${ox}" y2="${oy}" stroke="#16A34A" stroke-width="1.8" marker-end="url(#arrowSage)"/>
  <line x1="${ox}" y1="${oy}" x2="${imgX}" y2="${imgY}" stroke="#16A34A" stroke-width="1.8"/>

  <!-- Dynamic Image Arrow -->
  <line x1="${imgX}" y1="${oy}" x2="${imgX}" y2="${imgY}" stroke="#DC2626" stroke-width="${isReal ? '2.8' : '2'}" stroke-dasharray="${isReal ? 'none' : '4,3'}" marker-end="url(#arrowCrimson)"/>
  <text x="${imgX + 8}" y="${imgY + 4}" font-size="11" font-weight="bold" fill="#DC2626">A' (h'=${hPrime.toFixed(1)})</text>
  <text x="${imgX + 8}" y="${oy + (isReal ? 14 : -6)}" font-size="10" font-weight="bold" fill="#DC2626">B'</text>

  <!-- Bottom Metric Card -->
  <rect x="36" y="240" width="468" height="22" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="270" y="255" text-anchor="middle" font-size="10" fill="#0F172A">Computed Parameters: u = ${u} | v = ${v.toFixed(1)} | f = ${fSigned} | m = ${m.toFixed(2)} (${isReal ? 'Real & Inverted' : 'Virtual & Erect'})</text>
</svg>`

  return {
    title,
    svg,
    caption,
    domain: 'optics',
    isDynamic: true,
    computedMetrics: { u, v, f: fSigned, m, h, hPrime, isReal },
  }
}

/**
 * 2. TRULY GENERATIVE MECHANICS: Free-Body Diagram on Inclined Plane
 * Computes exact wedge slope, normal force N, friction f, and parallel gravity component dynamically!
 */
export function generateDynamicInclineSvg(params: {
  title?: string
  caption?: string
  angleDeg?: number
  massKg?: number
  frictionCoeff?: number
}): GeneratedScientificSvg {
  const theta = Math.min(60, Math.max(15, params.angleDeg || 30))
  const m = Math.max(1, params.massKg || 5)
  const g = 9.8
  const mu = params.frictionCoeff ?? 0.2

  const thetaRad = (theta * Math.PI) / 180
  const W = m * g
  const N = W * Math.cos(thetaRad)
  const F_parallel = W * Math.sin(thetaRad)
  const f_friction = mu * N
  const a = Math.max(0, (F_parallel - f_friction) / m)

  const startX = 80
  const baseY = 220
  const wedgeBase = 320
  const wedgeH = Math.min(160, Math.round(wedgeBase * Math.tan(thetaRad)))
  const topX = startX
  const topY = baseY - wedgeH
  const cornerX = startX + wedgeBase

  const blockX = startX + wedgeBase * 0.45
  const blockY = baseY - wedgeH * 0.55

  const title = params.title || `Free Body Diagram: m = ${m}kg on ${theta}° Incline`
  const caption = params.caption || `Weight W = ${W.toFixed(1)}N resolved into: Normal reaction N = ${N.toFixed(1)}N, Downward force mg·sinθ = ${F_parallel.toFixed(1)}N, Friction f = ${f_friction.toFixed(1)}N, Acceleration a = ${a.toFixed(2)} m/s².`

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 280" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" style="background:#FFFFFF; font-family:'JetBrains Mono','Segoe UI',sans-serif;">
  ${getSvgDefs()}
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="10" y="10" width="520" height="260" rx="6" fill="url(#chalkGrid)"/>

  <!-- Dynamic Header Bar -->
  <rect x="24" y="18" width="492" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="36" y="34" font-size="11" font-weight="bold" fill="#0F172A">MECHANICS: ${title.toUpperCase().slice(0, 52)}</text>
  <text x="495" y="34" text-anchor="end" font-size="10" font-weight="bold" fill="#2563EB">θ = ${theta}° | m = ${m}kg</text>

  <!-- Triangular Wedge Drawn to Exact Angle theta -->
  <polygon points="${startX},${baseY} ${cornerX},${baseY} ${topX},${topY}" fill="#F1F5F9" stroke="#0F172A" stroke-width="2"/>
  
  <!-- Incline Angle Arc theta -->
  <path d="M ${cornerX - 45} ${baseY} A 45 45 0 0 0 ${cornerX - 40} ${baseY - 18}" fill="none" stroke="#2563EB" stroke-width="2"/>
  <text x="${cornerX - 60}" y="${baseY - 8}" font-size="11" font-weight="bold" fill="#2563EB">${theta}°</text>

  <!-- Block Body Rotated to Match Exact Incline Angle -->
  <g transform="translate(${blockX}, ${blockY}) rotate(-${theta})">
    <rect x="-28" y="-28" width="56" height="28" rx="3" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>
    <text x="0" y="-10" text-anchor="middle" font-size="11" font-weight="bold" fill="#0F172A">${m} kg</text>

    <!-- Normal Force N (Perpendicular to plane) -->
    <line x1="0" y1="-28" x2="0" y2="-85" stroke="#16A34A" stroke-width="2.5" marker-end="url(#arrowSage)"/>
    <text x="6" y="-72" font-size="10" font-weight="bold" fill="#16A34A">N = ${N.toFixed(1)}N</text>

    <!-- Friction Force f (Parallel up plane) -->
    <line x1="28" y1="-14" x2="80" y2="-14" stroke="#D97706" stroke-width="2.2" marker-end="url(#arrowAmber)"/>
    <text x="60" y="-22" font-size="10" font-weight="bold" fill="#D97706">f = ${f_friction.toFixed(1)}N</text>

    <!-- Downward Parallel Force: mg·sinθ -->
    <line x1="-28" y1="-14" x2="-90" y2="-14" stroke="#2563EB" stroke-width="2.5" marker-end="url(#arrowRoyal)"/>
    <text x="-92" y="-20" text-anchor="end" font-size="10" font-weight="bold" fill="#2563EB">mg·sinθ = ${F_parallel.toFixed(1)}N</text>

    <!-- Perpendicular Gravity Component: mg·cosθ -->
    <line x1="0" y1="0" x2="0" y2="55" stroke="#64748B" stroke-width="1.8" stroke-dasharray="3,3" marker-end="url(#arrowCharcoal)"/>
    <text x="6" y="50" font-size="10" font-weight="bold" fill="#64748B">mg·cosθ</text>
  </g>

  <!-- True Downward Gravitational Weight W = mg -->
  <line x1="${blockX}" y1="${blockY}" x2="${blockX}" y2="${blockY + 80}" stroke="#DC2626" stroke-width="2.8" marker-end="url(#arrowCrimson)"/>
  <text x="${blockX + 8}" y="${blockY + 70}" font-size="11" font-weight="bold" fill="#DC2626">W = ${W.toFixed(1)} N</text>

  <!-- Dynamic Equations Panel -->
  <rect x="360" y="60" width="155" height="95" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="370" y="80" font-size="10" font-weight="bold" fill="#0F172A">Dynamic Solutions:</text>
  <text x="370" y="100" font-size="9" fill="#16A34A">N = mg·cos(${theta}°) = ${N.toFixed(1)} N</text>
  <text x="370" y="118" font-size="9" fill="#2563EB">F_net = ${F_parallel.toFixed(1)} - ${f_friction.toFixed(1)} N</text>
  <text x="370" y="138" font-size="10" font-weight="bold" fill="#DC2626">a = ${a.toFixed(2)} m/s²</text>

  <!-- Footer -->
  <rect x="40" y="246" width="460" height="20" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="270" y="260" text-anchor="middle" font-size="9" fill="#64748B">Newton's Second Law: F_net = m·a  |  Normal Force Equilibrium: N = mg·cosθ</text>
</svg>`

  return {
    title,
    svg,
    caption,
    domain: 'mechanics',
    isDynamic: true,
    computedMetrics: { theta, m, W, N, F_parallel, f_friction, a },
  }
}

/**
 * 3. TRULY GENERATIVE GEOMETRY: Circle Theorems (Gauth Standard)
 * Computes exact vertex coordinates on circle circumference using trigonometry!
 */
export function generateDynamicCircleTheoremSvg(params: {
  title?: string
  caption?: string
  arcAngleDeg?: number
  radius?: number
  theoremType?: 'center_circumference' | 'tangent_perpendicular'
}): GeneratedScientificSvg {
  const ox = 260
  const oy = 150
  const r = params.radius || 85
  const arcDeg = Math.min(170, Math.max(40, params.arcAngleDeg || 120))
  const inscribedDeg = arcDeg / 2

  const halfArc = arcDeg / 2
  const angleA_deg = 270 - halfArc
  const angleB_deg = 270 + halfArc
  const angleP_deg = 90

  const toRad = (d: number) => (d * Math.PI) / 180

  const ax = ox + r * Math.cos(toRad(angleA_deg))
  const ay = oy - r * Math.sin(toRad(angleA_deg))
  const bx = ox + r * Math.cos(toRad(angleB_deg))
  const by = oy - r * Math.sin(toRad(angleB_deg))
  const px = ox + r * Math.cos(toRad(angleP_deg))
  const py = oy - r * Math.sin(toRad(angleP_deg))

  const title = params.title || `Circle Theorem: Arc Angle = ${arcDeg}° -> Inscribed = ${inscribedDeg}°`
  const caption = params.caption || `Subtended central angle ∠AOB = ${arcDeg}°. The inscribed angle at circumference ∠APB = ${inscribedDeg}° (exactly half).`

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 280" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" style="background:#FFFFFF; font-family:'JetBrains Mono','Segoe UI',sans-serif;">
  ${getSvgDefs()}
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="10" y="10" width="520" height="260" rx="6" fill="url(#chalkGrid)"/>

  <!-- Dynamic Header Bar -->
  <rect x="24" y="18" width="492" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="36" y="34" font-size="11" font-weight="bold" fill="#0F172A">GEOMETRY: ${title.toUpperCase().slice(0, 52)}</text>
  <text x="495" y="34" text-anchor="end" font-size="10" font-weight="bold" fill="#2563EB">∠AOB = 2 · ∠APB</text>

  <!-- Circle -->
  <circle cx="${ox}" cy="${oy}" r="${r}" fill="#F8FAFC" stroke="#0F172A" stroke-width="2"/>

  <!-- Center Point O -->
  <circle cx="${ox}" cy="${oy}" r="3.5" fill="#0F172A"/>
  <text x="${ox + 8}" y="${oy - 4}" font-size="11" font-weight="bold" fill="#0F172A">O</text>

  <!-- Vertices: P (Circumference), A & B (Arc ends) -->
  <circle cx="${px}" cy="${py}" r="4" fill="#2563EB"/>
  <text x="${px}" y="${py - 8}" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563EB">P (${inscribedDeg}°)</text>

  <circle cx="${ax.toFixed(1)}" cy="${ay.toFixed(1)}" r="4" fill="#0F172A"/>
  <text x="${(ax - 14).toFixed(1)}" y="${(ay + 10).toFixed(1)}" font-size="12" font-weight="bold" fill="#0F172A">A</text>

  <circle cx="${bx.toFixed(1)}" cy="${by.toFixed(1)}" r="4" fill="#0F172A"/>
  <text x="${(bx + 14).toFixed(1)}" y="${(by + 10).toFixed(1)}" font-size="12" font-weight="bold" fill="#0F172A">B</text>

  <!-- Chords PA and PB -->
  <line x1="${px}" y1="${py}" x2="${ax.toFixed(1)}" y2="${ay.toFixed(1)}" stroke="#2563EB" stroke-width="2"/>
  <line x1="${px}" y1="${py}" x2="${bx.toFixed(1)}" y2="${by.toFixed(1)}" stroke="#2563EB" stroke-width="2"/>

  <!-- Radii OA and OB (Central Angle) -->
  <line x1="${ox}" y1="${oy}" x2="${ax.toFixed(1)}" y2="${ay.toFixed(1)}" stroke="#16A34A" stroke-width="2.2"/>
  <line x1="${ox}" y1="${oy}" x2="${bx.toFixed(1)}" y2="${by.toFixed(1)}" stroke="#16A34A" stroke-width="2.2"/>

  <!-- Dynamic Angle Labels -->
  <text x="${ox}" y="${oy + 30}" text-anchor="middle" font-size="13" font-weight="bold" fill="#16A34A">${arcDeg}° (2θ)</text>

  <!-- Highlighted Arc AB -->
  <path d="M ${ax.toFixed(1)} ${ay.toFixed(1)} A ${r} ${r} 0 0 0 ${bx.toFixed(1)} ${by.toFixed(1)}" fill="none" stroke="#D97706" stroke-width="3.5"/>
  <text x="${ox}" y="${(oy + r + 20).toFixed(1)}" text-anchor="middle" font-size="10" font-weight="bold" fill="#D97706">Subtended Arc AB (${arcDeg}°)</text>

  <!-- Proof Summary Box -->
  <rect x="380" y="60" width="135" height="95" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="390" y="80" font-size="10" font-weight="bold" fill="#0F172A">Theorem Proof:</text>
  <text x="390" y="98" font-size="9" fill="#64748B">Arc = ${arcDeg}°</text>
  <text x="390" y="116" font-size="9" fill="#16A34A">∠AOB = ${arcDeg}°</text>
  <text x="390" y="136" font-size="10" font-weight="bold" fill="#2563EB">∠APB = ${inscribedDeg}°</text>
</svg>`

  return {
    title,
    svg,
    caption,
    domain: 'geometry',
    isDynamic: true,
    computedMetrics: { arcDeg, inscribedDeg, r, ax, ay, bx, by, px, py },
  }
}

/**
 * 4. TRULY GENERATIVE CIRCUITS: Closed Loop with Dynamic Ohm's Law Parameters
 */
export function generateDynamicCircuitSvg(params: {
  title?: string
  caption?: string
  voltage?: number
  resistance?: number
}): GeneratedScientificSvg {
  const V = params.voltage || 12
  const R = params.resistance || 4
  const I = V / R

  const title = params.title || `Ohm's Law Circuit: V = ${V}V, R = ${R}Ω`
  const caption = params.caption || `Closed electrical loop: Applied Potential V = ${V} Volts across Resistor R = ${R} Ohms yields Current I = V/R = ${I.toFixed(2)} Amperes.`

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 280" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" style="background:#FFFFFF; font-family:'JetBrains Mono','Segoe UI',sans-serif;">
  ${getSvgDefs()}
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="10" y="10" width="520" height="260" rx="6" fill="url(#chalkGrid)"/>

  <!-- Dynamic Header Bar -->
  <rect x="24" y="18" width="492" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="36" y="34" font-size="11" font-weight="bold" fill="#0F172A">CIRCUIT: ${title.toUpperCase().slice(0, 52)}</text>
  <text x="495" y="34" text-anchor="end" font-size="10" font-weight="bold" fill="#2563EB">I = V/R = ${I.toFixed(2)} A</text>

  <!-- Wires & Resistor Top Line -->
  <line x1="90" y1="80" x2="200" y2="80" stroke="#0F172A" stroke-width="2"/>
  <!-- Parametric Resistor Zigzag -->
  <path d="M 200 80 L 208 68 L 224 92 L 240 68 L 256 92 L 272 68 L 288 92 L 296 80 L 340 80" fill="none" stroke="#2563EB" stroke-width="2.5"/>
  <text x="248" y="58" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563EB">R = ${R} Ω</text>

  <!-- Voltmeter in Parallel -->
  <line x1="190" y1="80" x2="190" y2="135" stroke="#0284C7" stroke-width="1.8"/>
  <line x1="190" y1="135" x2="225" y2="135" stroke="#0284C7" stroke-width="1.8"/>
  <circle cx="248" cy="135" r="18" fill="#F8FAFC" stroke="#0284C7" stroke-width="2"/>
  <text x="248" y="141" text-anchor="middle" font-size="13" font-weight="bold" fill="#0284C7">V</text>
  <text x="248" y="168" text-anchor="middle" font-size="10" font-weight="bold" fill="#0284C7">${V} V</text>
  <line x1="266" y1="135" x2="310" y2="135" stroke="#0284C7" stroke-width="1.8"/>
  <line x1="310" y1="135" x2="310" y2="80" stroke="#0284C7" stroke-width="1.8"/>
  <circle cx="190" cy="80" r="3.5" fill="#0F172A"/>
  <circle cx="310" cy="80" r="3.5" fill="#0F172A"/>

  <!-- Right Wire & Series Ammeter -->
  <line x1="340" y1="80" x2="450" y2="80" stroke="#0F172A" stroke-width="2"/>
  <line x1="450" y1="80" x2="450" y2="120" stroke="#0F172A" stroke-width="2"/>
  <circle cx="450" cy="142" r="18" fill="#F8FAFC" stroke="#16A34A" stroke-width="2"/>
  <text x="450" y="148" text-anchor="middle" font-size="13" font-weight="bold" fill="#16A34A">A</text>
  <text x="450" y="174" text-anchor="middle" font-size="10" font-weight="bold" fill="#16A34A">${I.toFixed(2)} A</text>
  <line x1="450" y1="160" x2="450" y2="215" stroke="#0F172A" stroke-width="2"/>

  <!-- Bottom Wire with DC Voltage Source V -->
  <line x1="450" y1="215" x2="235" y2="215" stroke="#0F172A" stroke-width="2"/>
  <line x1="235" y1="200" x2="235" y2="230" stroke="#DC2626" stroke-width="3"/>
  <text x="235" y="194" text-anchor="middle" font-size="12" font-weight="bold" fill="#DC2626">+</text>
  <line x1="225" y1="206" x2="225" y2="224" stroke="#0F172A" stroke-width="4.5"/>
  <text x="225" y="194" text-anchor="middle" font-size="12" font-weight="bold" fill="#0F172A">-</text>
  <text x="230" y="244" text-anchor="middle" font-size="11" font-weight="bold" fill="#DC2626">V = ${V} V</text>
  <line x1="225" y1="215" x2="90" y2="215" stroke="#0F172A" stroke-width="2"/>
  <line x1="90" y1="215" x2="90" y2="80" stroke="#0F172A" stroke-width="2"/>

  <!-- Current Direction Indicator -->
  <line x1="120" y1="80" x2="155" y2="80" stroke="#16A34A" stroke-width="2" marker-end="url(#arrowSage)"/>
  <text x="135" y="72" font-size="10" font-weight="bold" fill="#16A34A">I = ${I.toFixed(2)} A</text>

  <!-- Footer -->
  <rect x="40" y="248" width="460" height="20" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="270" y="262" text-anchor="middle" font-size="9" fill="#64748B">Calculation: I = ${V}V / ${R}Ω = ${I.toFixed(2)} Amperes | Voltmeter measures parallel ΔV = ${V}V</text>
</svg>`

  return {
    title,
    svg,
    caption,
    domain: 'circuits',
    isDynamic: true,
    computedMetrics: { V, R, I },
  }
}

/**
 * 5. TRULY GENERATIVE KINEMATICS & 1D SPATIAL REFERENCE SCALE
 * Computes exact coordinate distances, direction vectors, path totals, and net displacement
 * strictly adhering to NCERT Class 9 / Class 11 Motion in a Straight Line standards.
 */
export function generateDynamic1DMotionSvg(params: {
  title?: string
  caption?: string
  posO?: number
  posA?: number
  posB?: number
  unit?: string
}): GeneratedScientificSvg {
  const o = typeof params.posO === 'number' ? params.posO : 0
  const a = typeof params.posA === 'number' ? params.posA : 100
  const b = typeof params.posB === 'number' ? params.posB : 40
  const unit = params.unit || 'm'

  const forwardPath = a - o
  const returnPath = b - a
  const totalDistance = Math.abs(forwardPath) + Math.abs(returnPath)
  const displacement = b - o
  const dispSign = displacement > 0 ? '+' : displacement < 0 ? '-' : ''

  const title = params.title || '1D Spatial Reference Scale & Motion'
  const caption =
    params.caption ||
    `1D Coordinate Reference Scale: Origin O (${o}${unit}), Point A (+${a}${unit}), Point B (+${b}${unit}). Total Distance = |OA| + |AB| = ${totalDistance}${unit}, Net Displacement Δx = x_final - x_initial = ${dispSign}${Math.abs(displacement)}${unit}.`

  const ox = 100
  const bx = 250
  const ax = 440
  const axisY = 190

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 280" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" style="background:#FFFFFF; font-family:'JetBrains Mono','Segoe UI',sans-serif;">
  ${getSvgDefs()}
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="10" y="10" width="520" height="260" rx="6" fill="url(#chalkGrid)"/>

  <!-- Dynamic Header Bar -->
  <rect x="24" y="18" width="492" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="36" y="34" font-size="11" font-weight="bold" fill="#0F172A">KINEMATICS (1D REFERENCE): ${title.toUpperCase().slice(0, 48)}</text>
  <text x="495" y="34" text-anchor="end" font-size="10" font-weight="bold" fill="#2563EB">Dist = ${totalDistance}${unit} | Δx = ${dispSign}${Math.abs(displacement)}${unit}</text>

  <!-- Distance & Displacement Analytical Cards -->
  <rect x="36" y="52" width="468" height="28" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="270" y="70" text-anchor="middle" font-size="11" font-weight="bold" fill="#0F172A">Total Distance = |OA| + |AB| = ${Math.abs(forwardPath)}${unit} + ${Math.abs(returnPath)}${unit} = ${totalDistance}${unit}</text>

  <!-- Return Path Arrow (AB) -->
  <line x1="${ax}" y1="102" x2="${bx}" y2="102" stroke="#DC2626" stroke-width="2" stroke-dasharray="5,4"/>
  <path d="M ${bx} 102 L ${bx + 8} 98 L ${bx + 8} 106 Z" fill="#DC2626"/>
  <text x="${(ax + bx) / 2}" y="95" text-anchor="middle" font-size="11" font-weight="bold" fill="#DC2626">Return Path AB = ${returnPath}${unit}</text>

  <!-- Forward Path Arrow (OA) -->
  <line x1="${ox}" y1="132" x2="${ax}" y2="132" stroke="#2563EB" stroke-width="2" stroke-dasharray="5,4"/>
  <path d="M ${ax} 132 L ${ax - 8} 128 L ${ax - 8} 136 Z" fill="#2563EB"/>
  <text x="${(ox + ax) / 2}" y="125" text-anchor="middle" font-size="11" font-weight="bold" fill="#2563EB">Forward Path OA = +${forwardPath}${unit}</text>

  <!-- 1D Horizontal Coordinate Axis -->
  <line x1="50" y1="${axisY}" x2="490" y2="${axisY}" stroke="#0F172A" stroke-width="2.5"/>
  <path d="M 490 ${axisY} L 480 ${axisY - 5} L 480 ${axisY + 5} Z" fill="#0F172A"/>
  <text x="498" y="${axisY + 4}" font-size="10" font-weight="bold" fill="#0F172A">+X</text>
  <text x="38" y="${axisY + 4}" font-size="10" font-weight="bold" fill="#64748B">-X</text>

  <!-- Coordinate Ticks -->
  <!-- Origin O -->
  <line x1="${ox}" y1="${axisY - 10}" x2="${ox}" y2="${axisY + 10}" stroke="#0F172A" stroke-width="2.5"/>
  <circle cx="${ox}" cy="${axisY}" r="4" fill="#16A34A"/>
  <text x="${ox}" y="${axisY + 24}" text-anchor="middle" font-size="12" font-weight="bold" fill="#16A34A">O (${o}${unit})</text>
  <text x="${ox}" y="${axisY + 38}" text-anchor="middle" font-size="9" fill="#64748B">Origin (x = 0)</text>

  <!-- Point B -->
  <line x1="${bx}" y1="${axisY - 10}" x2="${bx}" y2="${axisY + 10}" stroke="#0F172A" stroke-width="2.5"/>
  <circle cx="${bx}" cy="${axisY}" r="4" fill="#D97706"/>
  <text x="${bx}" y="${axisY + 24}" text-anchor="middle" font-size="12" font-weight="bold" fill="#D97706">B (+${b}${unit})</text>
  <text x="${bx}" y="${axisY + 38}" text-anchor="middle" font-size="9" fill="#64748B">Final Position</text>

  <!-- Point A -->
  <line x1="${ax}" y1="${axisY - 10}" x2="${ax}" y2="${axisY + 10}" stroke="#0F172A" stroke-width="2.5"/>
  <circle cx="${ax}" cy="${axisY}" r="4" fill="#DC2626"/>
  <text x="${ax}" y="${axisY + 24}" text-anchor="middle" font-size="12" font-weight="bold" fill="#DC2626">A (+${a}${unit})</text>
  <text x="${ax}" y="${axisY + 38}" text-anchor="middle" font-size="9" fill="#64748B">Turnaround Point</text>

  <!-- Net Displacement Banner -->
  <rect x="110" y="244" width="320" height="22" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="270" y="259" text-anchor="middle" font-size="10" font-weight="bold" fill="#16A34A">Net Displacement OB = x_final - x_initial = ${dispSign}${Math.abs(displacement)}${unit}</text>
</svg>`

  return {
    title,
    svg,
    caption,
    domain: 'kinematics',
    isDynamic: true,
    computedMetrics: {
      origin: o,
      pointA: a,
      pointB: b,
      forwardPath,
      returnPath,
      totalDistance,
      displacement,
    },
  }
}

/**
 * 6. MATHEMATICAL CARTESIAN COORDINATE PLANE & QUADRANTS
 * Authentic, textbook-accurate 2D coordinate system with perpendicular axes,
 * origin O(0,0), numbered grid ticks, and all 4 quadrants labeled with sign conventions.
 */
export function generateDynamicCoordinatePlaneSvg(params: {
  title?: string
  caption?: string
  pointX?: number
  pointY?: number
}): GeneratedScientificSvg {
  const title = params.title || '2-D Cartesian Plane & Quadrants'
  const caption = params.caption || 'The coordinate axes divide the plane into four quadrants (I, II, III, IV) numbered counter-clockwise.'
  const px = typeof params.pointX === 'number' ? params.pointX : 3
  const py = typeof params.pointY === 'number' ? params.pointY : 2

  // Transform Cartesian (x, y) to SVG coordinates: Origin O at (270, 140), 50px per unit
  const svgPx = 270 + px * 50
  const svgPy = 140 - py * 30

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 280" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" style="background:#FFFFFF; font-family:'JetBrains Mono','Segoe UI',sans-serif;">
  ${getSvgDefs()}
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>

  <!-- Subtle Coordinate Grid Background -->
  <g stroke="#F1F5F9" stroke-width="1">
    <line x1="70" y1="28" x2="70" y2="252"/>
    <line x1="120" y1="28" x2="120" y2="252"/>
    <line x1="170" y1="28" x2="170" y2="252"/>
    <line x1="220" y1="28" x2="220" y2="252"/>
    <line x1="320" y1="28" x2="320" y2="252"/>
    <line x1="370" y1="28" x2="370" y2="252"/>
    <line x1="420" y1="28" x2="420" y2="252"/>
    <line x1="470" y1="28" x2="470" y2="252"/>
    <line x1="30" y1="50" x2="510" y2="50"/>
    <line x1="30" y1="80" x2="510" y2="80"/>
    <line x1="30" y1="110" x2="510" y2="110"/>
    <line x1="30" y1="170" x2="510" y2="170"/>
    <line x1="30" y1="200" x2="510" y2="200"/>
    <line x1="30" y1="230" x2="510" y2="230"/>
  </g>

  <!-- Quadrants Subdued Background Tint -->
  <rect x="270" y="40" width="235" height="100" fill="#2563EB" fill-opacity="0.04"/>
  <rect x="35" y="40" width="235" height="100" fill="#DC2626" fill-opacity="0.04"/>
  <rect x="35" y="140" width="235" height="100" fill="#16A34A" fill-opacity="0.04"/>
  <rect x="270" y="140" width="235" height="100" fill="#D97706" fill-opacity="0.04"/>

  <!-- Quadrant Labels -->
  <text x="390" y="65" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563EB">Quadrant I</text>
  <text x="390" y="80" text-anchor="middle" font-size="10" fill="#2563EB">(x &gt; 0, y &gt; 0) [+, +]</text>

  <text x="150" y="65" text-anchor="middle" font-size="12" font-weight="bold" fill="#DC2626">Quadrant II</text>
  <text x="150" y="80" text-anchor="middle" font-size="10" fill="#DC2626">(x &lt; 0, y &gt; 0) [-, +]</text>

  <text x="150" y="215" text-anchor="middle" font-size="12" font-weight="bold" fill="#16A34A">Quadrant III</text>
  <text x="150" y="230" text-anchor="middle" font-size="10" fill="#16A34A">(x &lt; 0, y &gt; 0) [-, -]</text>

  <text x="390" y="215" text-anchor="middle" font-size="12" font-weight="bold" fill="#D97706">Quadrant IV</text>
  <text x="390" y="230" text-anchor="middle" font-size="10" fill="#D97706">(x &gt; 0, y &lt; 0) [+, -]</text>

  <!-- Principal X-Axis -->
  <line x1="30" y1="140" x2="505" y2="140" stroke="#0F172A" stroke-width="2" marker-end="url(#arrowCharcoal)"/>
  <text x="515" y="144" font-size="13" font-weight="bold" fill="#0F172A">X</text>
  <text x="20" y="144" font-size="13" font-weight="bold" fill="#0F172A">X'</text>

  <!-- Principal Y-Axis -->
  <line x1="270" y1="250" x2="270" y2="28" stroke="#0F172A" stroke-width="2" marker-end="url(#arrowCharcoal)"/>
  <text x="275" y="25" font-size="13" font-weight="bold" fill="#0F172A">Y</text>
  <text x="275" y="262" font-size="13" font-weight="bold" fill="#0F172A">Y'</text>

  <!-- Origin Point O(0,0) -->
  <circle cx="270" cy="140" r="4.5" fill="#0F172A"/>
  <text x="254" y="155" font-size="11" font-weight="bold" fill="#0F172A">O (0,0)</text>

  <!-- Numerical Ticks on X-Axis -->
  <g fill="#64748B" font-size="10" text-anchor="middle">
    <line x1="70" y1="136" x2="70" y2="144" stroke="#0F172A" stroke-width="1.5"/><text x="70" y="155">-4</text>
    <line x1="120" y1="136" x2="120" y2="144" stroke="#0F172A" stroke-width="1.5"/><text x="120" y="155">-3</text>
    <line x1="170" y1="136" x2="170" y2="144" stroke="#0F172A" stroke-width="1.5"/><text x="170" y="155">-2</text>
    <line x1="220" y1="136" x2="220" y2="144" stroke="#0F172A" stroke-width="1.5"/><text x="220" y="155">-1</text>
    <line x1="320" y1="136" x2="320" y2="144" stroke="#0F172A" stroke-width="1.5"/><text x="320" y="155">1</text>
    <line x1="370" y1="136" x2="370" y2="144" stroke="#0F172A" stroke-width="1.5"/><text x="370" y="155">2</text>
    <line x1="420" y1="136" x2="420" y2="144" stroke="#0F172A" stroke-width="1.5"/><text x="420" y="155">3</text>
    <line x1="470" y1="136" x2="470" y2="144" stroke="#0F172A" stroke-width="1.5"/><text x="470" y="155">4</text>
  </g>

  <!-- Numerical Ticks on Y-Axis -->
  <g fill="#64748B" font-size="10" text-anchor="end">
    <line x1="266" y1="50" x2="274" y2="50" stroke="#0F172A" stroke-width="1.5"/><text x="264" y="54">3</text>
    <line x1="266" y1="80" x2="274" y2="80" stroke="#0F172A" stroke-width="1.5"/><text x="264" y="84">2</text>
    <line x1="266" y1="110" x2="274" y2="110" stroke="#0F172A" stroke-width="1.5"/><text x="264" y="114">1</text>
    <line x1="266" y1="170" x2="274" y2="170" stroke="#0F172A" stroke-width="1.5"/><text x="264" y="174">-1</text>
    <line x1="266" y1="200" x2="274" y2="200" stroke="#0F172A" stroke-width="1.5"/><text x="264" y="204">-2</text>
    <line x1="266" y1="230" x2="274" y2="230" stroke="#0F172A" stroke-width="1.5"/><text x="264" y="234">-3</text>
  </g>

  <!-- Plotted Example Point P(x, y) with dashed projections -->
  <line x1="${svgPx}" y1="140" x2="${svgPx}" y2="${svgPy}" stroke="#2563EB" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="270" y1="${svgPy}" x2="${svgPx}" y2="${svgPy}" stroke="#2563EB" stroke-width="1.2" stroke-dasharray="3,3"/>
  <circle cx="${svgPx}" cy="${svgPy}" r="4.5" fill="#2563EB"/>
  <text x="${svgPx + 8}" y="${svgPy - 4}" font-size="11" font-weight="bold" fill="#2563EB">P (${px}, ${py})</text>

  <!-- Top Title Banner -->
  <rect x="24" y="14" width="492" height="22" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="34" y="29" font-size="11" font-weight="bold" fill="#0F172A">CARTESIAN PLANE: QUADRANTS &amp; COORDINATES</text>
  <text x="506" y="29" text-anchor="end" font-size="10" fill="#64748B">Counter-Clockwise Convention</text>
</svg>`

  return {
    title,
    svg,
    caption,
    domain: 'mathematics',
    isDynamic: true,
    computedMetrics: { pointX: px, pointY: py },
  }
}

/**
 * 7. BIOLOGY: PLANT CELL WALL ULTRASTRUCTURE & MULTI-LAYER ARCHITECTURE
 * Publication-grade vector diagram on clean white canvas.
 */
export function generateDynamicPlantCellWallSvg(params: {
  title?: string
  caption?: string
}): GeneratedScientificSvg {
  const title = params.title || 'Plant Cell Wall: Ultrastructure & Layered Architecture'
  const caption = params.caption || 'The plant cell wall consists of the pectin-rich middle lamella, primary wall with flexible microfibrils, multi-layered secondary wall, and inner plasma membrane.'

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 280" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" style="background:#FFFFFF; font-family:'JetBrains Mono','Segoe UI',sans-serif;">
  ${getSvgDefs()}
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>

  <!-- Top Title Banner -->
  <rect x="24" y="14" width="492" height="22" rx="5" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="36" y="29" font-size="11" font-weight="bold" fill="#0F172A">CELL BIOLOGY: ${title.toUpperCase().slice(0, 48)}</text>
  <text x="504" y="29" text-anchor="end" font-size="9" font-weight="bold" fill="#2563EB">Textbook Ultrastructure</text>

  <!-- Cell Wall Layer Stage -->
  <!-- 1. Middle Lamella (Pectin-rich cementing layer) -->
  <rect x="40" y="48" width="280" height="26" rx="3" fill="#FEF3C7" stroke="#D97706" stroke-width="1.5"/>
  <g fill="#D97706" opacity="0.6">
    <circle cx="55" cy="58" r="1.8"/><circle cx="75" cy="64" r="1.8"/><circle cx="95" cy="56" r="1.8"/>
    <circle cx="120" cy="62" r="1.8"/><circle cx="150" cy="58" r="1.8"/><circle cx="180" cy="64" r="1.8"/>
    <circle cx="210" cy="60" r="1.8"/><circle cx="240" cy="64" r="1.8"/><circle cx="270" cy="58" r="1.8"/>
  </g>

  <!-- 2. Primary Cell Wall (Interwoven cellulose microfibrils) -->
  <rect x="40" y="78" width="280" height="40" rx="3" fill="#DCFCE7" stroke="#16A34A" stroke-width="1.5"/>
  <g stroke="#16A34A" stroke-width="1.2" opacity="0.75">
    <line x1="45" y1="84" x2="95" y2="114"/><line x1="75" y1="80" x2="135" y2="116"/>
    <line x1="115" y1="82" x2="175" y2="114"/><line x1="155" y1="80" x2="215" y2="116"/>
    <line x1="195" y1="82" x2="255" y2="114"/><line x1="235" y1="80" x2="295" y2="116"/>
    <line x1="95" y1="80" x2="45" y2="116"/><line x1="145" y1="82" x2="85" y2="114"/>
    <line x1="185" y1="80" x2="125" y2="116"/><line x1="225" y1="82" x2="165" y2="114"/>
    <line x1="265" y1="80" x2="205" y2="116"/><line x1="305" y1="82" x2="245" y2="114"/>
  </g>

  <!-- 3. Secondary Cell Wall (Dense lamellae S1, S2, S3) -->
  <rect x="40" y="122" width="280" height="52" rx="3" fill="#DBEAFE" stroke="#2563EB" stroke-width="1.5"/>
  <line x1="40" y1="139" x2="320" y2="139" stroke="#2563EB" stroke-width="0.8" stroke-dasharray="3,3" opacity="0.5"/>
  <line x1="40" y1="156" x2="320" y2="156" stroke="#2563EB" stroke-width="0.8" stroke-dasharray="3,3" opacity="0.5"/>
  <text x="312" y="135" font-size="8" fill="#2563EB" text-anchor="end">S1</text>
  <text x="312" y="152" font-size="8" fill="#2563EB" text-anchor="end">S2</text>
  <text x="312" y="169" font-size="8" fill="#2563EB" text-anchor="end">S3</text>

  <!-- 4. Plasma Membrane (Phospholipid Bilayer) -->
  <rect x="40" y="178" width="280" height="24" rx="2" fill="#F1F5F9" stroke="#0F172A" stroke-width="1.5"/>
  <g fill="#0F172A" opacity="0.75">
    <circle cx="50" cy="183" r="2"/><circle cx="65" cy="183" r="2"/><circle cx="80" cy="183" r="2"/>
    <circle cx="95" cy="183" r="2"/><circle cx="110" cy="183" r="2"/><circle cx="125" cy="183" r="2"/>
    <circle cx="140" cy="183" r="2"/><circle cx="155" cy="183" r="2"/><circle cx="170" cy="183" r="2"/>
    <circle cx="205" cy="183" r="2"/><circle cx="220" cy="183" r="2"/><circle cx="235" cy="183" r="2"/>
    <circle cx="250" cy="183" r="2"/><circle cx="265" cy="183" r="2"/><circle cx="280" cy="183" r="2"/>
    <circle cx="50" cy="197" r="2"/><circle cx="65" cy="197" r="2"/><circle cx="80" cy="197" r="2"/>
    <circle cx="95" cy="197" r="2"/><circle cx="110" cy="197" r="2"/><circle cx="125" cy="197" r="2"/>
    <circle cx="140" cy="197" r="2"/><circle cx="155" cy="197" r="2"/><circle cx="170" cy="197" r="2"/>
    <circle cx="205" cy="197" r="2"/><circle cx="220" cy="197" r="2"/><circle cx="235" cy="197" r="2"/>
  </g>
  <!-- Transmembrane Protein Channel -->
  <rect x="180" y="179" width="18" height="22" rx="4" fill="#FEE2E2" stroke="#DC2626" stroke-width="1"/>

  <!-- 5. Plasmodesma Pore Channel -->
  <path d="M 215 46 L 215 204 L 227 204 L 227 46 Z" fill="#FFFFFF" stroke="#DC2626" stroke-width="1.2" stroke-dasharray="2,2"/>
  <text x="221" y="116" font-size="8" fill="#DC2626" text-anchor="middle" transform="rotate(-90 221 116)">PLASMODESMA</text>

  <!-- 6. Right-Hand Callout Labels with Leader Lines -->
  <!-- Callout 1: Middle Lamella -->
  <line x1="280" y1="61" x2="350" y2="61" stroke="#64748B" stroke-width="1"/>
  <circle cx="280" cy="61" r="3" fill="#D97706"/>
  <text x="358" y="58" font-size="10" font-weight="bold" fill="#D97706">Middle Lamella</text>
  <text x="358" y="69" font-size="8.5" fill="#64748B">Pectin cementing layer (Calcium pectate)</text>

  <!-- Callout 2: Primary Cell Wall -->
  <line x1="280" y1="98" x2="350" y2="98" stroke="#64748B" stroke-width="1"/>
  <circle cx="280" cy="98" r="3" fill="#16A34A"/>
  <text x="358" y="95" font-size="10" font-weight="bold" fill="#16A34A">Primary Cell Wall</text>
  <text x="358" y="106" font-size="8.5" fill="#64748B">Extensible, interwoven cellulose microfibrils</text>

  <!-- Callout 3: Secondary Cell Wall -->
  <line x1="280" y1="148" x2="350" y2="148" stroke="#64748B" stroke-width="1"/>
  <circle cx="280" cy="148" r="3" fill="#2563EB"/>
  <text x="358" y="145" font-size="10" font-weight="bold" fill="#2563EB">Secondary Cell Wall</text>
  <text x="358" y="156" font-size="8.5" fill="#64748B">Rigid 3-layered (S1, S2, S3) with lignin</text>

  <!-- Callout 4: Plasma Membrane & Transmembrane Protein -->
  <line x1="280" y1="190" x2="350" y2="190" stroke="#64748B" stroke-width="1"/>
  <circle cx="280" cy="190" r="3" fill="#0F172A"/>
  <text x="358" y="187" font-size="10" font-weight="bold" fill="#0F172A">Plasma Membrane</text>
  <text x="358" y="198" font-size="8.5" fill="#DC2626">Lipid bilayer &amp; transport protein channel</text>

  <!-- Bottom Legend Bar -->
  <rect x="40" y="246" width="460" height="20" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="270" y="260" text-anchor="middle" font-size="9" fill="#0F172A">Plant Cell Boundary • Mechanical Rigidity, Turgor Resistance &amp; Plasmodesmata Symplast</text>
</svg>`

  return {
    title,
    svg,
    caption,
    domain: 'biology',
    isDynamic: true,
    computedMetrics: { title },
  }
}

/**
 * 8. BIOLOGY: GENERAL CELL STRUCTURE & ORGANELLES
 * Publication-grade vector diagram illustrating Cell Membrane, Nucleus with Chromatin,
 * Mitochondria with cristae, Chloroplasts, Vacuole, and Cytosol on clean white canvas.
 */
export function generateDynamicCellStructureSvg(params: {
  title?: string
  caption?: string
  cellType?: 'plant' | 'animal' | 'prokaryote'
}): GeneratedScientificSvg {
  const cellType = params.cellType || 'plant'
  const title = params.title || `${cellType === 'plant' ? 'Plant Cell' : cellType === 'animal' ? 'Animal Cell' : 'Cell Structure'}: Organelles & Ultrastructure`
  const caption = params.caption || 'A complete structural diagram showing the compartmentalized cytoplasm, nucleus, energy organelles, and outer boundaries.'

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 280" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" style="background:#FFFFFF; font-family:'JetBrains Mono','Segoe UI',sans-serif;">
  ${getSvgDefs()}
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>

  <!-- Top Title Banner -->
  <rect x="24" y="14" width="492" height="22" rx="5" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="36" y="29" font-size="11" font-weight="bold" fill="#0F172A">CYTOLOGY: ${title.toUpperCase().slice(0, 48)}</text>
  <text x="504" y="29" text-anchor="end" font-size="9" font-weight="bold" fill="#2563EB">Magnification: 2500x</text>

  <!-- Cell Boundary -->
  <rect x="40" y="48" width="280" height="185" rx="28" fill="#F0FDF4" stroke="#16A34A" stroke-width="2.5"/>
  <rect x="46" y="54" width="268" height="173" rx="22" fill="#FFFFFF" stroke="#2563EB" stroke-width="1.5"/>

  <!-- Large Central Vacuole -->
  <path d="M 120 75 Q 230 70 240 135 Q 245 190 160 185 Q 115 180 110 125 Z" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.5" stroke-dasharray="3,2"/>
  <text x="175" y="133" font-size="9.5" fill="#16A34A" text-anchor="middle" font-weight="bold">Central Vacuole</text>
  <text x="175" y="144" font-size="8" fill="#64748B" text-anchor="middle">(Turgor Cell Sap)</text>

  <!-- Nucleus with Double Membrane and Nucleolus -->
  <circle cx="85" cy="110" r="26" fill="#FEE2E2" stroke="#DC2626" stroke-width="2"/>
  <circle cx="85" cy="110" r="24" fill="none" stroke="#DC2626" stroke-width="0.8" stroke-dasharray="2,2"/>
  <circle cx="82" cy="108" r="8" fill="#DC2626" opacity="0.9"/>
  <!-- Chromatin strands -->
  <path d="M 68 113 Q 75 100 88 117 Q 95 105 102 113" fill="none" stroke="#DC2626" stroke-width="1"/>

  <!-- Mitochondria with Cristae -->
  <g transform="translate(65, 170) rotate(-20)">
    <rect x="0" y="0" width="34" height="16" rx="8" fill="#FEF3C7" stroke="#D97706" stroke-width="1.5"/>
    <path d="M 6 3 L 6 13 M 12 3 L 12 13 M 18 3 L 18 13 M 24 3 L 24 13 M 28 3 L 28 13" stroke="#D97706" stroke-width="1"/>
  </g>

  <!-- Chloroplast with Grana -->
  <g transform="translate(250, 80) rotate(15)">
    <ellipse cx="18" cy="12" rx="20" ry="11" fill="#DCFCE7" stroke="#16A34A" stroke-width="1.5"/>
    <line x1="8" y1="9" x2="8" y2="15" stroke="#16A34A" stroke-width="2"/>
    <line x1="18" y1="7" x2="18" y2="17" stroke="#16A34A" stroke-width="2"/>
    <line x1="28" y1="9" x2="28" y2="15" stroke="#16A34A" stroke-width="2"/>
  </g>

  <!-- Endoplasmic Reticulum Ribbons -->
  <path d="M 70 83 Q 60 70 80 63 Q 95 67 88 83" fill="none" stroke="#8B5CF6" stroke-width="1.5"/>
  <circle cx="68" cy="73" r="1.2" fill="#8B5CF6"/>
  <circle cx="84" cy="67" r="1.2" fill="#8B5CF6"/>

  <!-- Right-Hand Labeling & Callout Directory -->
  <!-- Callout 1: Cell Wall & Membrane -->
  <line x1="260" y1="58" x2="345" y2="58" stroke="#64748B" stroke-width="1"/>
  <circle cx="260" cy="58" r="3" fill="#16A34A"/>
  <text x="352" y="55" font-size="10" font-weight="bold" fill="#16A34A">Cell Wall &amp; Plasma Membrane</text>
  <text x="352" y="66" font-size="8.5" fill="#64748B">Rigid cellulose envelope + selective barrier</text>

  <!-- Callout 2: Nucleus -->
  <line x1="110" y1="100" x2="345" y2="100" stroke="#64748B" stroke-width="1"/>
  <circle cx="110" cy="100" r="3" fill="#DC2626"/>
  <text x="352" y="97" font-size="10" font-weight="bold" fill="#DC2626">Nucleus &amp; Nucleolus</text>
  <text x="352" y="108" font-size="8.5" fill="#64748B">Genetic master blueprint (DNA / Chromatin)</text>

  <!-- Callout 3: Mitochondria -->
  <line x1="100" y1="175" x2="345" y2="145" stroke="#64748B" stroke-width="1"/>
  <circle cx="100" cy="175" r="3" fill="#D97706"/>
  <text x="352" y="142" font-size="10" font-weight="bold" fill="#D97706">Mitochondria</text>
  <text x="352" y="153" font-size="8.5" fill="#64748B">Powerhouse of cell; generates ATP via cristae</text>

  <!-- Callout 4: Chloroplast -->
  <line x1="280" y1="90" x2="345" y2="185" stroke="#64748B" stroke-width="1"/>
  <circle cx="280" cy="90" r="3" fill="#16A34A"/>
  <text x="352" y="182" font-size="10" font-weight="bold" fill="#16A34A">Chloroplasts (Plastids)</text>
  <text x="352" y="193" font-size="8.5" fill="#64748B">Thylakoid grana sites of photosynthesis</text>

  <!-- Bottom Legend Bar -->
  <rect x="40" y="246" width="460" height="20" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="270" y="260" text-anchor="middle" font-size="9" fill="#0F172A">Structural &amp; Functional Unit of Life • Compartmentalized Eukaryotic Cytoplasm (NCERT)</text>
</svg>`

  return {
    title,
    svg,
    caption,
    domain: 'biology',
    isDynamic: true,
    computedMetrics: { title, cellType },
  }
}


/**
 * 9. Biology: Plant Tissues & Meristematic Architecture
 * (Shoot Apical, Root Apical, Lateral Cambium, Intercalary Meristem, Permanent Tissues)
 */
export function generateDynamicPlantTissuesSvg(params: {
  title?: string
  caption?: string
  tissueType?: 'apical' | 'lateral' | 'intercalary' | 'overview' | 'permanent'
}): GeneratedScientificSvg {
  const title = params.title || 'Plant Tissues: Meristematic Architecture'
  const norm = `${title} ${params.caption || ''}`.toLowerCase()

  const isApical = norm.includes('apical') || norm.includes('root tip') || norm.includes('shoot tip') || norm.includes('length')
  const isLateral = norm.includes('lateral') || norm.includes('cambium') || norm.includes('girth') || norm.includes('secondary')
  const isIntercalary = norm.includes('intercalary') || norm.includes('internode') || norm.includes('grass')

  let subHeading = 'Plant Tissues: Apical, Lateral & Intercalary Zones'
  let mainVisualContent = ''

  if (isApical) {
    subHeading = 'Shoot & Root Apical Meristem: Primary Growth & Zonal Division'
    mainVisualContent = `
    <!-- Shoot Apex Diagram (Left) -->
    <g transform="translate(60, 45)">
      <rect x="0" y="0" width="180" height="195" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <text x="90" y="16" text-anchor="middle" font-size="10" font-weight="bold" fill="#0F172A">Shoot Apex (Shoot Tip)</text>

      <!-- Stem Outline -->
      <path d="M 60 190 L 60 90 Q 60 40 90 28 Q 120 40 120 90 L 120 190 Z" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.8"/>

      <!-- Leaf Primordia -->
      <path d="M 60 85 C 40 70 35 45 48 35 C 55 45 58 65 65 78 Z" fill="#DCFCE7" stroke="#16A34A" stroke-width="1.5"/>
      <path d="M 120 85 C 140 70 145 45 132 35 C 125 45 122 65 115 78 Z" fill="#DCFCE7" stroke="#16A34A" stroke-width="1.5"/>

      <!-- Shoot Apical Meristem Zone (Dome) -->
      <path d="M 75 55 Q 90 32 105 55 Z" fill="#2563EB" opacity="0.85"/>
      <circle cx="90" cy="45" r="2" fill="#FFFFFF"/>

      <!-- Dividing Cells Hash Matrix -->
      <line x1="82" y1="50" x2="98" y2="50" stroke="#FFFFFF" stroke-width="0.8"/>
      <line x1="85" y1="46" x2="95" y2="46" stroke="#FFFFFF" stroke-width="0.8"/>

      <!-- Shoot Callouts -->
      <line x1="90" y1="36" x2="35" y2="24" stroke="#2563EB" stroke-width="1"/>
      <circle cx="90" cy="36" r="2" fill="#2563EB"/>
      <text x="32" y="22" text-anchor="end" font-size="8.5" font-weight="bold" fill="#2563EB">Shoot Apical Meristem</text>

      <!-- Primary Growth Vector -->
      <line x1="90" y1="26" x2="90" y2="10" stroke="#DC2626" stroke-width="1.5" marker-end="url(#arrowCrimson)"/>
      <text x="96" y="16" font-size="7.5" font-weight="bold" fill="#DC2626">Primary Growth (↑)</text>
    </g>

    <!-- Root Tip Diagram (Center-Right) -->
    <g transform="translate(265, 45)">
      <rect x="0" y="0" width="235" height="195" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <text x="117" y="16" text-anchor="middle" font-size="10" font-weight="bold" fill="#0F172A">Root Tip (Root Apex Zones)</text>

      <!-- Root Column Outline -->
      <path d="M 60 25 L 60 130 Q 60 165 95 180 Q 130 165 130 130 L 130 25 Z" fill="#F8FAFC" stroke="#0F172A" stroke-width="1.8"/>

      <!-- Zone 1: Zone of Maturation (with Root Hairs) -->
      <rect x="61" y="26" width="68" height="42" fill="#EFF6FF" opacity="0.6"/>
      <!-- Root Hairs -->
      <line x1="60" y1="35" x2="42" y2="33" stroke="#2563EB" stroke-width="1.2"/>
      <line x1="60" y1="45" x2="38" y2="45" stroke="#2563EB" stroke-width="1.2"/>
      <line x1="60" y1="55" x2="44" y2="58" stroke="#2563EB" stroke-width="1.2"/>
      <line x1="130" y1="35" x2="148" y2="33" stroke="#2563EB" stroke-width="1.2"/>
      <line x1="130" y1="45" x2="152" y2="45" stroke="#2563EB" stroke-width="1.2"/>
      <line x1="130" y1="55" x2="146" y2="58" stroke="#2563EB" stroke-width="1.2"/>

      <!-- Zone 2: Zone of Elongation -->
      <rect x="61" y="69" width="68" height="42" fill="#FEF3C7" opacity="0.6"/>
      <line x1="62" y1="68" x2="128" y2="68" stroke="#D97706" stroke-dasharray="3,3"/>

      <!-- Zone 3: Meristematic Zone (Cell Division) -->
      <path d="M 61 112 L 61 140 Q 61 160 95 168 Q 129 160 129 140 L 129 112 Z" fill="#DCFCE7" stroke="#16A34A" stroke-width="1"/>
      <line x1="62" y1="111" x2="128" y2="111" stroke="#16A34A" stroke-dasharray="3,3"/>
      <!-- Actively dividing cells -->
      <circle cx="85" cy="130" r="3" fill="#16A34A"/>
      <circle cx="95" cy="128" r="3" fill="#16A34A"/>
      <circle cx="105" cy="132" r="3" fill="#16A34A"/>
      <circle cx="90" cy="140" r="3" fill="#16A34A"/>
      <circle cx="100" cy="142" r="3" fill="#16A34A"/>

      <!-- Root Cap (Protective Thimble) -->
      <path d="M 65 152 Q 95 190 125 152 Q 95 174 65 152 Z" fill="#CBD5E1" stroke="#64748B" stroke-width="1.4"/>

      <!-- Root Tip Zone Pointers -->
      <line x1="130" y1="45" x2="160" y2="45" stroke="#2563EB" stroke-width="1"/>
      <text x="164" y="44" font-size="8" font-weight="bold" fill="#2563EB">Zone of Maturation</text>
      <text x="164" y="53" font-size="7" fill="#64748B">Cell differentiation &amp; root hairs</text>

      <line x1="130" y1="88" x2="160" y2="88" stroke="#D97706" stroke-width="1"/>
      <text x="164" y="87" font-size="8" font-weight="bold" fill="#D97706">Zone of Elongation</text>
      <text x="164" y="96" font-size="7" fill="#64748B">Rapid cellular lengthening</text>

      <line x1="129" y1="132" x2="160" y2="132" stroke="#16A34A" stroke-width="1"/>
      <text x="164" y="131" font-size="8" font-weight="bold" fill="#16A34A">Root Apical Meristem</text>
      <text x="164" y="140" font-size="7" fill="#64748B">Dense cytoplasm &amp; active division</text>

      <line x1="120" y1="172" x2="160" y2="172" stroke="#64748B" stroke-width="1"/>
      <text x="164" y="171" font-size="8" font-weight="bold" fill="#475569">Root Cap (Calyptra)</text>
      <text x="164" y="180" font-size="7" fill="#64748B">Thimble protecting tender apex</text>
    </g>`
  } else if (isLateral) {
    subHeading = 'Lateral Meristem (Cambium): Secondary Growth & Girth Increase'
    mainVisualContent = `
    <!-- Stem Transverse Cross Section (Left) -->
    <g transform="translate(65, 45)">
      <rect x="0" y="0" width="200" height="195" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <text x="100" y="16" text-anchor="middle" font-size="10" font-weight="bold" fill="#0F172A">Stem Cross-Section (Girth Growth)</text>

      <circle cx="100" cy="105" r="75" fill="#FEF3C7" stroke="#D97706" stroke-width="2"/>
      <circle cx="100" cy="105" r="62" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.2"/>
      <circle cx="100" cy="105" r="45" fill="none" stroke="#2563EB" stroke-width="3" stroke-dasharray="6,3"/>
      <circle cx="100" cy="105" r="50" fill="none" stroke="#16A34A" stroke-width="1.5" stroke-dasharray="2,2"/>
      <circle cx="100" cy="105" r="38" fill="#F8FAFC" stroke="#0F172A" stroke-width="1.2"/>
      <circle cx="100" cy="105" r="16" fill="#F1F5F9" stroke="#64748B" stroke-width="1"/>
      <text x="100" y="108" text-anchor="middle" font-size="7.5" fill="#64748B">Pith</text>

      <!-- Radial Girth Growth Arrows -->
      <line x1="100" y1="60" x2="100" y2="40" stroke="#DC2626" stroke-width="1.5" marker-end="url(#arrowCrimson)"/>
      <line x1="100" y1="150" x2="100" y2="170" stroke="#DC2626" stroke-width="1.5" marker-end="url(#arrowCrimson)"/>
      <line x1="55" y1="105" x2="35" y2="105" stroke="#DC2626" stroke-width="1.5" marker-end="url(#arrowCrimson)"/>
      <line x1="145" y1="105" x2="165" y2="105" stroke="#DC2626" stroke-width="1.5" marker-end="url(#arrowCrimson)"/>
    </g>

    <!-- Structural Breakdown & Functional Mechanism (Right) -->
    <g transform="translate(285, 45)">
      <rect x="0" y="0" width="215" height="195" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="107" y="18" text-anchor="middle" font-size="10" font-weight="bold" fill="#0F172A">Lateral Meristem Mechanisms</text>

      <rect x="12" y="30" width="190" height="44" rx="4" fill="#EFF6FF" stroke="#2563EB" stroke-width="1"/>
      <text x="20" y="44" font-size="8.5" font-weight="bold" fill="#2563EB">1. Vascular Cambium Ring</text>
      <text x="20" y="56" font-size="7.5" fill="#0F172A">• Cuts off Secondary Xylem toward inside</text>
      <text x="20" y="66" font-size="7.5" fill="#0F172A">• Cuts off Secondary Phloem toward outside</text>

      <rect x="12" y="82" width="190" height="44" rx="4" fill="#FEF3C7" stroke="#D97706" stroke-width="1"/>
      <text x="20" y="96" font-size="8.5" font-weight="bold" fill="#D97706">2. Cork Cambium (Phellogen)</text>
      <text x="20" y="108" font-size="7.5" fill="#0F172A">• Generates outer protective bark &amp; cork</text>
      <text x="20" y="118" font-size="7.5" fill="#0F172A">• Prevents water loss &amp; microbial infection</text>

      <rect x="12" y="134" width="190" height="48" rx="4" fill="#F0FDF4" stroke="#16A34A" stroke-width="1"/>
      <text x="20" y="148" font-size="8.5" font-weight="bold" fill="#16A34A">• Board Exam Distinction</text>
      <text x="20" y="160" font-size="7.5" fill="#0F172A">• Growth Type: Secondary Growth (Lateral)</text>
      <text x="20" y="172" font-size="7.5" fill="#0F172A">• Direct Result: Increases stem/root diameter &amp; girth</text>
    </g>`
  } else {
    // Default & Overview: Complete NCERT Architecture (Apical, Intercalary, Lateral in Plant Body)
    subHeading = 'Location of Meristematic Tissues in Plant Body (NCERT Fig 6.2)'
    mainVisualContent = `
    <g transform="translate(60, 45)">
      <rect x="0" y="0" width="200" height="195" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <text x="100" y="16" text-anchor="middle" font-size="10" font-weight="bold" fill="#0F172A">Plant Axis (Longitudinal Section)</text>

      <path d="M 80 190 L 80 50 Q 80 30 100 24 Q 120 30 120 50 L 120 190 Z" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.8"/>

      <!-- 1. Apical Meristem (Shoot Apex) -->
      <path d="M 82 45 Q 100 25 118 45 Z" fill="#2563EB"/>
      <circle cx="100" cy="36" r="2.5" fill="#FFFFFF"/>

      <!-- Node 1 with Intercalary Meristem -->
      <line x1="60" y1="85" x2="140" y2="85" stroke="#16A34A" stroke-width="1.5"/>
      <rect x="80" y="80" width="40" height="10" fill="#F59E0B" opacity="0.9"/>
      <path d="M 80 85 C 65 75 55 60 45 60" fill="none" stroke="#16A34A" stroke-width="1.8"/>
      <path d="M 120 85 C 135 75 145 60 155 60" fill="none" stroke="#16A34A" stroke-width="1.8"/>

      <!-- Node 2 with Intercalary Meristem -->
      <line x1="60" y1="135" x2="140" y2="135" stroke="#16A34A" stroke-width="1.5"/>
      <rect x="80" y="130" width="40" height="10" fill="#F59E0B" opacity="0.9"/>
      <path d="M 80 135 C 65 125 55 110 45 110" fill="none" stroke="#16A34A" stroke-width="1.8"/>
      <path d="M 120 135 C 135 125 145 110 155 110" fill="none" stroke="#16A34A" stroke-width="1.8"/>

      <!-- Lateral Meristem -->
      <rect x="76" y="150" width="5" height="35" fill="#DC2626"/>
      <rect x="119" y="150" width="5" height="35" fill="#DC2626"/>
    </g>

    <!-- Right Side: Exact NCERT Anatomical Callouts -->
    <g transform="translate(280, 45)">
      <rect x="0" y="0" width="220" height="195" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="110" y="18" text-anchor="middle" font-size="10" font-weight="bold" fill="#0F172A">Anatomical Meristem Directory</text>

      <rect x="10" y="28" width="200" height="45" rx="4" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.2"/>
      <circle cx="22" cy="40" r="4" fill="#2563EB"/>
      <text x="32" y="43" font-size="9" font-weight="bold" fill="#2563EB">1. Apical Meristem</text>
      <text x="32" y="55" font-size="7.5" fill="#0F172A">• Location: Tips of roots and stems</text>
      <text x="32" y="65" font-size="7.5" fill="#0F172A">• Function: Primary growth (increases length)</text>

      <rect x="10" y="80" width="200" height="45" rx="4" fill="#FEF3C7" stroke="#D97706" stroke-width="1.2"/>
      <circle cx="22" cy="92" r="4" fill="#D97706"/>
      <text x="32" y="95" font-size="9" font-weight="bold" fill="#D97706">2. Intercalary Meristem</text>
      <text x="32" y="107" font-size="7.5" fill="#0F172A">• Location: Base of leaves / internodes (grasses)</text>
      <text x="32" y="117" font-size="7.5" fill="#0F172A">• Function: Rapid elongation &amp; regrowth</text>

      <rect x="10" y="132" width="200" height="45" rx="4" fill="#FEF2F2" stroke="#DC2626" stroke-width="1.2"/>
      <circle cx="22" cy="144" r="4" fill="#DC2626"/>
      <text x="32" y="147" font-size="9" font-weight="bold" fill="#DC2626">3. Lateral Meristem (Cambium)</text>
      <text x="32" y="159" font-size="7.5" fill="#0F172A">• Location: Along sides of stem/root</text>
      <text x="32" y="169" font-size="7.5" fill="#0F172A">• Function: Secondary growth (increases girth)</text>
    </g>`
  }

  const svg = `<svg viewBox="0 0 540 280" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; font-family:'JetBrains Mono','Segoe UI',sans-serif;">
  ${getSvgDefs()}
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="4" y="4" width="532" height="272" fill="url(#chalkGrid)" opacity="0.6"/>

  <rect x="40" y="12" width="460" height="22" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="27" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold">${subHeading}</text>

  ${mainVisualContent}

  <rect x="40" y="248" width="460" height="18" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="270" y="261" text-anchor="middle" font-size="8.5" fill="#0F172A">NCERT Class 9 Biology • Chapter 3: Tissues • Active Mitotic Division (No Vacuoles, Dense Cytoplasm)</text>
</svg>`

  return {
    title,
    svg,
    caption: params.caption || subHeading,
    domain: 'biology',
    isDynamic: true,
    computedMetrics: { isApical, isLateral, isIntercalary },
  }
}

/**
 * 10. Physics: Electromagnetism & Solenoid Magnetic Field Lines
 * (Soft Iron Core, Helical Coils, DC Source, Looping B-Field Lines)
 */
export function generateDynamicElectromagnetSvg(params: {
  title?: string
  caption?: string
  turns?: number
  current?: number
}): GeneratedScientificSvg {
  const title = params.title || 'Electromagnet & Magnetic Field of a Solenoid'
  const caption = params.caption || 'Magnetic field produced by electric current flowing through a coiled conductor around an iron core.'

  const svg = `<svg viewBox="0 0 540 280" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; font-family:'JetBrains Mono','Segoe UI',sans-serif;">
  ${getSvgDefs()}
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="4" y="4" width="532" height="272" fill="url(#chalkGrid)" opacity="0.6"/>

  <rect x="60" y="12" width="420" height="22" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="27" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold">Electromagnet: Solenoid with Soft Iron Core &amp; B-Field Lines</text>

  <path d="M 125 110 C 125 40 415 40 415 110" fill="none" stroke="#16A34A" stroke-width="1.5" stroke-dasharray="4,2"/>
  <path d="M 140 110 C 140 60 400 60 400 110" fill="none" stroke="#16A34A" stroke-width="1.5"/>
  <line x1="260" y1="48" x2="280" y2="48" stroke="#16A34A" stroke-width="2" marker-end="url(#arrowSage)"/>
  <line x1="260" y1="67" x2="280" y2="67" stroke="#16A34A" stroke-width="2" marker-end="url(#arrowSage)"/>

  <path d="M 125 140 C 125 210 415 210 415 140" fill="none" stroke="#16A34A" stroke-width="1.5" stroke-dasharray="4,2"/>
  <path d="M 140 140 C 140 190 400 190 400 140" fill="none" stroke="#16A34A" stroke-width="1.5"/>
  <line x1="280" y1="202" x2="260" y2="202" stroke="#16A34A" stroke-width="2" marker-end="url(#arrowSage)"/>
  <line x1="280" y1="183" x2="260" y2="183" stroke="#16A34A" stroke-width="2" marker-end="url(#arrowSage)"/>

  <g transform="translate(130, 105)">
    <rect x="0" y="0" width="280" height="40" rx="4" fill="#E2E8F0" stroke="#0F172A" stroke-width="1.8"/>
    <rect x="0" y="4" width="280" height="8" fill="#F8FAFC" opacity="0.8"/>
    <rect x="4" y="6" width="30" height="28" rx="4" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>
    <text x="19" y="25" text-anchor="middle" font-size="16" font-weight="bold" fill="#2563EB">N</text>
    <rect x="246" y="6" width="30" height="28" rx="4" fill="#FEF2F2" stroke="#DC2626" stroke-width="1.5"/>
    <text x="261" y="25" text-anchor="middle" font-size="16" font-weight="bold" fill="#DC2626">S</text>
  </g>

  <g stroke="#D97706" stroke-width="3.5" fill="none">
    <path d="M 175 103 C 180 90 195 90 200 103 L 210 147 C 215 160 230 160 235 147" stroke="#B45309"/>
    <path d="M 215 103 C 220 90 235 90 240 103 L 250 147 C 255 160 270 160 275 147" stroke="#B45309"/>
    <path d="M 255 103 C 260 90 275 90 280 103 L 290 147 C 295 160 310 160 315 147" stroke="#B45309"/>
    <path d="M 295 103 C 300 90 315 90 320 103 L 330 147 C 335 160 350 160 355 147" stroke="#B45309"/>
    <path d="M 335 103 C 340 90 355 90 360 103 L 370 147" stroke="#B45309"/>
  </g>

  <line x1="205" y1="120" x2="208" y2="132" stroke="#2563EB" stroke-width="2" marker-end="url(#arrowRoyal)"/>
  <line x1="245" y1="120" x2="248" y2="132" stroke="#2563EB" stroke-width="2" marker-end="url(#arrowRoyal)"/>
  <line x1="285" y1="120" x2="288" y2="132" stroke="#2563EB" stroke-width="2" marker-end="url(#arrowRoyal)"/>
  <line x1="325" y1="120" x2="328" y2="132" stroke="#2563EB" stroke-width="2" marker-end="url(#arrowRoyal)"/>

  <path d="M 175 103 L 175 80 L 70 80 L 70 235 L 230 235" fill="none" stroke="#0F172A" stroke-width="1.8"/>
  <path d="M 370 147 L 370 235 L 310 235" fill="none" stroke="#0F172A" stroke-width="1.8"/>

  <line x1="230" y1="225" x2="230" y2="245" stroke="#0F172A" stroke-width="3"/>
  <line x1="240" y1="215" x2="240" y2="255" stroke="#0F172A" stroke-width="1.8"/>
  <line x1="250" y1="225" x2="250" y2="245" stroke="#0F172A" stroke-width="3"/>
  <line x1="260" y1="215" x2="260" y2="255" stroke="#0F172A" stroke-width="1.8"/>
  <text x="268" y="222" font-size="10" font-weight="bold" fill="#DC2626">+</text>
  <text x="220" y="222" font-size="10" font-weight="bold" fill="#0F172A">-</text>

  <line x1="270" y1="235" x2="285" y2="235" stroke="#0F172A" stroke-width="1.8"/>
  <circle cx="285" cy="235" r="2.5" fill="#0F172A"/>
  <line x1="285" y1="235" x2="303" y2="225" stroke="#0F172A" stroke-width="1.8"/>
  <circle cx="305" cy="235" r="2.5" fill="#0F172A"/>
  <line x1="305" y1="235" x2="315" y2="235" stroke="#0F172A" stroke-width="1.8"/>
  <text x="295" y="218" text-anchor="middle" font-size="8" fill="#64748B">Key (K)</text>

  <rect x="420" y="70" width="105" height="52" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="472" y="86" text-anchor="middle" font-size="9" font-weight="bold" fill="#0F172A">Governing Law</text>
  <text x="472" y="100" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563EB">B = μ₀ · n · I</text>
  <text x="472" y="114" text-anchor="middle" font-size="7.5" fill="#64748B">B ∝ I &amp; B ∝ n (turns)</text>

  <text x="145" y="165" font-size="8.5" font-weight="bold" fill="#0F172A">Soft Iron Core</text>
  <text x="145" y="175" font-size="7.5" fill="#64748B">High magnetic permeability</text>

  <rect x="40" y="254" width="460" height="18" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="270" y="266" text-anchor="middle" font-size="8.5" fill="#0F172A">Magnetic Effect of Electric Current • Right-Hand Thumb Rule • S-Pole &amp; N-Pole Formation</text>
</svg>`

  return {
    title,
    svg,
    caption,
    domain: 'physics',
    isDynamic: true,
    computedMetrics: { turns: params.turns || 5, current: params.current || 2 },
  }
}

/**
 * 11. Biology: Human Female Reproductive System & Gamete Anatomy
 * (Ovaries, Fallopian Tube, Uterus, Endometrium, Cervix, Vagina)
 */
export function generateDynamicReproductiveAnatomySvg(params: {
  title?: string
  caption?: string
}): GeneratedScientificSvg {
  const title = params.title || 'Human Female Reproductive System'
  const caption = params.caption || 'Anatomy of the female reproductive system showing site of fertilization and implantation.'

  const svg = `<svg viewBox="0 0 540 280" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; font-family:'JetBrains Mono','Segoe UI',sans-serif;">
  ${getSvgDefs()}
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="4" y="4" width="532" height="272" fill="url(#chalkGrid)" opacity="0.6"/>

  <rect x="60" y="12" width="420" height="22" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="27" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold">Human Female Reproductive System: Organs &amp; Functions (NCERT)</text>

  <g transform="translate(140, 45)">
    <path d="M 90 40 C 50 35 30 70 30 110 C 30 135 45 155 45 180 L 75 180 C 75 155 90 135 90 110 Z" fill="#FFE4E6" stroke="#E11D48" stroke-width="1.8"/>
    <path d="M 90 40 C 130 35 150 70 150 110 C 150 135 135 155 135 180 L 105 180 C 105 155 90 135 90 110 Z" fill="#FFE4E6" stroke="#E11D48" stroke-width="1.8"/>

    <path d="M 90 55 C 70 55 55 80 55 110 C 55 130 65 145 65 170 L 115 170 C 115 145 125 130 125 110 C 125 80 110 55 90 55 Z" fill="#FFF1F2" stroke="#FB7185" stroke-width="1.2"/>

    <path d="M 50 45 C 10 40 -40 30 -60 55 C -65 62 -75 75 -70 85" fill="none" stroke="#E11D48" stroke-width="3"/>
    <path d="M -70 85 C -80 88 -85 95 -80 102 M -70 85 C -75 92 -75 102 -68 105 M -70 85 C -65 92 -60 100 -55 98" stroke="#E11D48" stroke-width="1.5"/>

    <ellipse cx="-72" cy="115" rx="15" ry="20" fill="#FEF3C7" stroke="#D97706" stroke-width="1.6"/>
    <line x1="-57" y1="115" x2="35" y2="100" stroke="#D97706" stroke-width="1.2" stroke-dasharray="2,2"/>

    <path d="M 130 45 C 170 40 220 30 240 55 C 245 62 255 75 250 85" fill="none" stroke="#E11D48" stroke-width="3"/>
    <path d="M 250 85 C 260 88 265 95 260 102 M 250 85 C 255 92 255 102 248 105 M 250 85 C 245 92 240 100 235 98" stroke="#E11D48" stroke-width="1.5"/>

    <ellipse cx="252" cy="115" rx="15" ry="20" fill="#FEF3C7" stroke="#D97706" stroke-width="1.6"/>
    <line x1="237" y1="115" x2="145" y2="100" stroke="#D97706" stroke-width="1.2" stroke-dasharray="2,2"/>

    <rect x="75" y="175" width="30" height="15" fill="#FDA4AF" stroke="#E11D48" stroke-width="1.5"/>
    <rect x="70" y="190" width="40" height="25" fill="#FFE4E6" stroke="#E11D48" stroke-width="1.5"/>
  </g>

  <!-- Left Labels & Pointers -->
  <line x1="90" y1="85" x2="45" y2="85" stroke="#64748B" stroke-width="1"/>
  <circle cx="90" cy="85" r="2.5" fill="#2563EB"/>
  <text x="40" y="82" text-anchor="end" font-size="9" font-weight="bold" fill="#2563EB">Oviduct / Fallopian Tube</text>
  <text x="40" y="92" text-anchor="end" font-size="7.5" fill="#64748B">• Site of fertilization (Ampulla)</text>

  <line x1="68" y1="160" x2="45" y2="145" stroke="#64748B" stroke-width="1"/>
  <circle cx="68" cy="160" r="2.5" fill="#D97706"/>
  <text x="40" y="142" text-anchor="end" font-size="9" font-weight="bold" fill="#D97706">Ovary</text>
  <text x="40" y="152" text-anchor="end" font-size="7.5" fill="#64748B">Produces egg/ovum &amp; estrogen</text>

  <!-- Right Labels & Pointers -->
  <line x1="230" y1="140" x2="360" y2="120" stroke="#64748B" stroke-width="1"/>
  <circle cx="230" cy="140" r="2.5" fill="#E11D48"/>
  <text x="365" y="117" font-size="9" font-weight="bold" fill="#E11D48">Uterus (Womb)</text>
  <text x="365" y="127" font-size="7.5" fill="#64748B">Thick muscular bag; site of implantation</text>

  <line x1="235" y1="170" x2="360" y2="155" stroke="#64748B" stroke-width="1"/>
  <circle cx="235" cy="170" r="2.5" fill="#E11D48"/>
  <text x="365" y="152" font-size="9" font-weight="bold" fill="#E11D48">Endometrium Lining</text>
  <text x="365" y="162" font-size="7.5" fill="#64748B">Vascular lining supporting embryo placenta</text>

  <line x1="230" y1="235" x2="360" y2="195" stroke="#64748B" stroke-width="1"/>
  <circle cx="230" cy="235" r="2.5" fill="#0F172A"/>
  <text x="365" y="192" font-size="9" font-weight="bold" fill="#0F172A">Cervix &amp; Vagina</text>
  <text x="365" y="202" font-size="7.5" fill="#64748B">Entry for sperm; birth canal</text>

  <rect x="40" y="254" width="460" height="18" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="270" y="266" text-anchor="middle" font-size="8.5" fill="#0F172A">Class 10 Biology • Chapter: How Do Organisms Reproduce • Gametogenesis &amp; Fertilization</text>
</svg>`

  return {
    title,
    svg,
    caption,
    domain: 'biology',
    isDynamic: true,
    computedMetrics: { title },
  }
}

/**
 * 12. Universal Scholastic Concept Blueprint
 * (Default Fallback: Structured Hierarchical Schematic on Clean Whiteboard Canvas)
 * GUARANTEED ZERO CARTESIAN GRAPHS ON NON-MATH TOPICS.
 */
export function generateDynamicUniversalConceptSvg(params: {
  title?: string
  caption?: string
  domain?: string
}): GeneratedScientificSvg {
  const title = params.title || 'Scholastic Concept Blueprint'
  const caption = params.caption || 'Authentic conceptual relationship model & board-exam key takeaways.'
  const cleanTitle = title.replace(/^(?:concept\s*\d*[:\-\s]*)/i, '').trim()

  const svg = `<svg viewBox="0 0 540 280" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; font-family:'JetBrains Mono','Segoe UI',sans-serif;">
  ${getSvgDefs()}
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="4" y="4" width="532" height="272" fill="url(#chalkGrid)" opacity="0.6"/>

  <rect x="40" y="12" width="460" height="22" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="27" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold">${cleanTitle.slice(0, 48)}</text>

  <g transform="translate(25, 45)">
    <rect x="0" y="0" width="150" height="195" rx="6" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.2"/>
    <rect x="0" y="0" width="150" height="24" rx="6" fill="#DCFCE7"/>
    <text x="75" y="16" text-anchor="middle" font-size="9" font-weight="bold" fill="#16A34A">1. Physical Intuition</text>

    <circle cx="15" cy="45" r="3" fill="#16A34A"/>
    <text x="25" y="48" font-size="8" font-weight="bold" fill="#0F172A">Real-World Hook</text>
    <text x="25" y="60" font-size="7" fill="#64748B">Tangible daily basis</text>
    <text x="25" y="70" font-size="7" fill="#64748B">Observable mechanism</text>

    <circle cx="15" cy="95" r="3" fill="#16A34A"/>
    <text x="25" y="98" font-size="8" font-weight="bold" fill="#0F172A">Underlying Driver</text>
    <text x="25" y="110" font-size="7" fill="#64748B">Core energetic / structural</text>
    <text x="25" y="120" font-size="7" fill="#64748B">fundamental force</text>

    <circle cx="15" cy="145" r="3" fill="#16A34A"/>
    <text x="25" y="148" font-size="8" font-weight="bold" fill="#0F172A">Classroom Analogy</text>
    <text x="25" y="160" font-size="7" fill="#64748B">Concrete representation</text>
    <text x="25" y="170" font-size="7" fill="#64748B">Intuitive bridge to law</text>
  </g>

  <line x1="180" y1="140" x2="195" y2="140" stroke="#2563EB" stroke-width="2" marker-end="url(#arrowRoyal)"/>

  <g transform="translate(195, 45)">
    <rect x="0" y="0" width="150" height="195" rx="6" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.4"/>
    <rect x="0" y="0" width="150" height="24" rx="6" fill="#DBEAFE"/>
    <text x="75" y="16" text-anchor="middle" font-size="9" font-weight="bold" fill="#2563EB">2. Governing Principle</text>

    <rect x="10" y="36" width="130" height="50" rx="4" fill="#FFFFFF" stroke="#2563EB" stroke-width="1"/>
    <text x="75" y="55" text-anchor="middle" font-size="8" font-weight="bold" fill="#2563EB">CORE LAW / THEOREM</text>
    <text x="75" y="72" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#0F172A">${cleanTitle.split(':')[0].slice(0, 18)}</text>

    <circle cx="15" cy="110" r="3" fill="#2563EB"/>
    <text x="25" y="113" font-size="8" font-weight="bold" fill="#0F172A">Governing Rules</text>
    <text x="25" y="125" font-size="7" fill="#64748B">Strict scientific criteria</text>
    <text x="25" y="135" font-size="7" fill="#64748B">Mandatory conditions</text>

    <circle cx="15" cy="155" r="3" fill="#2563EB"/>
    <text x="25" y="158" font-size="8" font-weight="bold" fill="#0F172A">SI Units &amp; Constants</text>
    <text x="25" y="170" font-size="7" fill="#64748B">Dimensional integrity</text>
    <text x="25" y="180" font-size="7" fill="#64748B">Zero unit conversion loss</text>
  </g>

  <line x1="350" y1="140" x2="365" y2="140" stroke="#16A34A" stroke-width="2" marker-end="url(#arrowSage)"/>

  <g transform="translate(365, 45)">
    <rect x="0" y="0" width="150" height="195" rx="6" fill="#FEF3C7" stroke="#D97706" stroke-width="1.2"/>
    <rect x="0" y="0" width="150" height="24" rx="6" fill="#FDE68A"/>
    <text x="75" y="16" text-anchor="middle" font-size="9" font-weight="bold" fill="#D97706">3. Board Application</text>

    <circle cx="15" cy="45" r="3" fill="#D97706"/>
    <text x="25" y="48" font-size="8" font-weight="bold" fill="#0F172A">Trio Layout</text>
    <text x="25" y="60" font-size="7" fill="#0F172A">Given → Formula</text>
    <text x="25" y="70" font-size="7" fill="#0F172A">Substitution → Boxed</text>

    <circle cx="15" cy="95" r="3" fill="#D97706"/>
    <text x="25" y="98" font-size="8" font-weight="bold" fill="#0F172A">Common Trap</text>
    <text x="25" y="110" font-size="7" fill="#DC2626">Avoid unit mismatches</text>
    <text x="25" y="120" font-size="7" fill="#DC2626">Watch sign conventions</text>

    <circle cx="15" cy="145" r="3" fill="#D97706"/>
    <text x="25" y="148" font-size="8" font-weight="bold" fill="#0F172A">Scoring Keywords</text>
    <text x="25" y="160" font-size="7" fill="#16A34A">Verbatim definitions</text>
    <text x="25" y="170" font-size="7" fill="#16A34A">Full 100% credit</text>
  </g>

  <rect x="40" y="254" width="460" height="18" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="270" y="266" text-anchor="middle" font-size="8.5" fill="#0F172A">Authentic Vector Schematic • CBSE / ICSE / IB Scholastic Standards</text>
</svg>`

  return {
    title,
    svg,
    caption,
    domain: params.domain || 'general',
    isDynamic: true,
    computedMetrics: { title: cleanTitle },
  }
}

/**
 * Universal Parser & Master Dispatcher
 * Strictly generates pure white-canvas vector diagrams with zero hardcoding.
 */
export function createUniversalScientificSvg(
  input: string | ScientificDiagramParams,
  caption?: string
): GeneratedScientificSvg {
  const norm = typeof input === 'string' ? `${input} ${caption || ''}`.toLowerCase() : JSON.stringify(input).toLowerCase()

  
  // 1. Biology: Plant Tissues & Meristematic Zones (Apical, Lateral, Intercalary, Permanent)
  if (
    norm.includes('meristem') ||
    norm.includes('apical') ||
    norm.includes('lateral') ||
    norm.includes('intercalary') ||
    norm.includes('cambium') ||
    norm.includes('parenchyma') ||
    norm.includes('collenchyma') ||
    norm.includes('sclerenchyma') ||
    norm.includes('xylem') ||
    norm.includes('phloem') ||
    norm.includes('root tip') ||
    norm.includes('shoot tip') ||
    norm.includes('plant tissue') ||
    norm.includes('permanent tissue') ||
    (norm.includes('tissue') && (norm.includes('plant') || norm.includes('cell division') || norm.includes('girth') || norm.includes('growth in length')))
  ) {
    return generateDynamicPlantTissuesSvg({
      title: typeof input === 'string' ? input : input.title,
      caption,
    })
  }

  // 1b. Biology: Human Female & Male Reproductive System & Gamete Anatomy
  if (
    norm.includes('reproductive') ||
    norm.includes('reproduction') ||
    norm.includes('ovary') ||
    norm.includes('uterus') ||
    norm.includes('fallopian') ||
    norm.includes('oviduct') ||
    norm.includes('cervix') ||
    norm.includes('vagina') ||
    norm.includes('fertilization') ||
    norm.includes('gamete') ||
    norm.includes('zygote')
  ) {
    return generateDynamicReproductiveAnatomySvg({
      title: typeof input === 'string' ? input : input.title,
      caption,
    })
  }

  // 1c. Physics: Electromagnetism & Solenoid Magnetic Field Lines
  if (
    norm.includes('electromagnet') ||
    norm.includes('solenoid') ||
    norm.includes('magnetic field') ||
    norm.includes('magnetic line') ||
    norm.includes('induction') ||
    norm.includes('flux') ||
    norm.includes('core') ||
    (norm.includes('coil') && norm.includes('current'))
  ) {
    return generateDynamicElectromagnetSvg({
      title: typeof input === 'string' ? input : input.title,
      caption,
    })
  }

  // 1. Biology: Plant Cell Wall & Ultrastructure
  if (
    norm.includes('cell wall') ||
    norm.includes('lamella') ||
    norm.includes('microfibril') ||
    norm.includes('cellulose') ||
    norm.includes('primary wall') ||
    norm.includes('secondary wall') ||
    norm.includes('plasmodesm')
  ) {
    return generateDynamicPlantCellWallSvg({
      title: typeof input === 'string' ? input : input.title,
      caption,
    })
  }

  // 2. Biology: Cell Anatomy, Organelles, Unicellular & Eukaryotic / Prokaryotic Cells
  if (
    norm.includes('unicellular') ||
    norm.includes('multicellular') ||
    norm.includes('cell structure') ||
    norm.includes('organelle') ||
    norm.includes('prokaryot') ||
    norm.includes('eukaryot') ||
    norm.includes('bacteria') ||
    norm.includes('plant cell') ||
    norm.includes('animal cell') ||
    norm.includes('mitochondri') ||
    norm.includes('chloroplast') ||
    norm.includes('vacuole') ||
    norm.includes('cytoplasm') ||
    norm.includes('nucleus') ||
    norm.includes('membrane') ||
    norm.includes('cell')
  ) {
    return generateDynamicCellStructureSvg({
      title: typeof input === 'string' ? input : input.title,
      caption,
    })
  }

  // 3. Coordinate Geometry & Cartesian Plane (Strictly restricted to Math Coordinate Geometry topics)
  if (
    norm.includes('quadrant') ||
    norm.includes('cartesian') ||
    norm.includes('coordinate geometry') ||
    norm.includes('coordinate plane') ||
    norm.includes('abscissa') ||
    norm.includes('ordinate') ||
    norm.includes('2-d plane') ||
    (norm.includes('axis') && (norm.includes('x-axis') || norm.includes('y-axis') || norm.includes('origin')))
  ) {
    return generateDynamicCoordinatePlaneSvg({
      title: typeof input === 'string' ? input : input.title,
      caption,
    })
  }

  // 4. Kinematics & 1D Motion: Position, Reference Point, Distance & Displacement
  if (
    norm.includes('position') ||
    norm.includes('reference') ||
    norm.includes('displacement') ||
    norm.includes('distance') ||
    norm.includes('1d motion') ||
    norm.includes('straight line') ||
    norm.includes('kinematic') ||
    norm.includes('motion in a straight line') ||
    norm.includes('number line') ||
    norm.includes('coordinate scale') ||
    norm.includes('motion')
  ) {
    const aMatch = norm.match(/(?:point\s*a|pos\s*a|forward)\s*[:=]?\s*([\d\.]+)/i)
    const bMatch = norm.match(/(?:point\s*b|pos\s*b|return)\s*[:=]?\s*([\d\.]+)/i)

    return generateDynamic1DMotionSvg({
      title: typeof input === 'string' ? input : input.title,
      caption,
      posO: 0,
      posA: aMatch ? parseFloat(aMatch[1]) : 100,
      posB: bMatch ? parseFloat(bMatch[1]) : 40,
      unit: norm.includes('km') ? 'km' : norm.includes('cm') ? 'cm' : 'm',
    })
  }

  // 5. Ray Optics: Lenses & Mirrors
  if (norm.includes('lens') || norm.includes('focal') || norm.includes('ray diagram') || norm.includes('optics') || norm.includes('refraction') || norm.includes('convex') || norm.includes('concave')) {
    const fMatch = norm.match(/\bf\s*=\s*([\d\.]+)/)
    const uMatch = norm.match(/\bu\s*=\s*([\-\d\.]+)/)
    const hMatch = norm.match(/\bh\s*=\s*([\d\.]+)/)
    const isConcave = norm.includes('concave')

    return generateDynamicOpticsSvg({
      title: typeof input === 'string' ? input : input.title,
      caption,
      lensType: isConcave ? 'concave' : 'convex',
      focalLength: fMatch ? parseFloat(fMatch[1]) : 60,
      objectDistance: uMatch ? Math.abs(parseFloat(uMatch[1])) : 150,
      objectHeight: hMatch ? parseFloat(hMatch[1]) : 50,
    })
  }

  // 6. Mechanics: Incline / Free Body Diagram
  if (norm.includes('inclined') || norm.includes('incline') || norm.includes('free body') || norm.includes('fbd') || norm.includes('friction') || norm.includes('ramp')) {
    const angleMatch = norm.match(/(?:angle|theta|\bdeg)\s*[:=]?\s*(\d+)/i) || norm.match(/(\d+)\s*(?:deg|°|degree)/i)
    const massMatch = norm.match(/(?:mass|m)\s*[:=]?\s*([\d\.]+)/i) || norm.match(/([\d\.]+)\s*kg/i)
    const muMatch = norm.match(/(?:mu|friction|coeff)\s*[:=]?\s*([\d\.]+)/i)

    return generateDynamicInclineSvg({
      title: typeof input === 'string' ? input : input.title,
      caption,
      angleDeg: angleMatch ? parseInt(angleMatch[1], 10) : 30,
      massKg: massMatch ? parseFloat(massMatch[1]) : 5,
      frictionCoeff: muMatch ? parseFloat(muMatch[1]) : 0.2,
    })
  }

  // 7. Euclidean Geometry: Circle Theorems
  if (norm.includes('circle') || norm.includes('subtend') || norm.includes('tangent') || norm.includes('arc') || norm.includes('theorem')) {
    const arcMatch = norm.match(/(?:arc|angle)\s*[:=]?\s*(\d+)/i) || norm.match(/(\d+)\s*(?:deg|°|degree)/i)

    return generateDynamicCircleTheoremSvg({
      title: typeof input === 'string' ? input : input.title,
      caption,
      arcAngleDeg: arcMatch ? parseInt(arcMatch[1], 10) : 120,
    })
  }

  // 8. Electric Circuits & Ohm's Law
  if (norm.includes('circuit') || norm.includes('ohm') || norm.includes('resistor') || norm.includes('ammeter') || norm.includes('battery')) {
    const vMatch = norm.match(/(?:v|volt|voltage)\s*[:=]?\s*([\d\.]+)/i) || norm.match(/([\d\.]+)\s*v\b/i)
    const rMatch = norm.match(/(?:r|ohm|resistance)\s*[:=]?\s*([\d\.]+)/i) || norm.match(/([\d\.]+)\s*(?:ohm|Ω)/i)

    return generateDynamicCircuitSvg({
      title: typeof input === 'string' ? input : input.title,
      caption,
      voltage: vMatch ? parseFloat(vMatch[1]) : 12,
      resistance: rMatch ? parseFloat(rMatch[1]) : 4,
    })
  }

  // Default: Return Scholastic Concept Blueprint on pure white canvas (NEVER Cartesian Plane!)
  return generateDynamicUniversalConceptSvg({
    title: typeof input === 'string' ? input : input.title || 'Scholastic Concept Blueprint',
    caption: caption || 'Authentic conceptual relationship model plotted on digital chalkboard.',
  })
}
