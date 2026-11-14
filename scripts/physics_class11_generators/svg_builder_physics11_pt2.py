"""
svg_builder_physics11_pt2.py - Dedicated Scientific Vector SVG Builders for Class 11 Physics Part 2 (Final-Term Examination)
Covers Units VII, VIII, IX, and X:
- Mechanical Properties of Solids (Stress-Strain Curve, Moduli)
- Mechanical Properties of Fluids (Pascal's Hydraulic Lift, Capillary Rise, Bernoulli's Venturi)
- Thermal Properties of Matter (Thermal Expansion & Calorimeter)
- Thermodynamics (Carnot Cycle P-V Indicator)
- Kinetic Theory of Gases (Molecular Collision & Pressure in 3D Container)
- Oscillations (SHM Reference Circle, Phasor, Spring-Mass)
- Waves (Standing Waves in Organ Pipes, Acoustic Beats)
"""

try:
    from .svg_builder_physics11 import get_svg_wrapper
except ImportError:
    from svg_builder_physics11 import get_svg_wrapper

def build_stress_strain_curve_svg(material='Structural Steel', title=None, caption=None):
    title = title or f"Stress-Strain Characteristic Curve ({material})"
    caption = caption or "Hooke's linear limit (OA), Yield point (B), Ultimate tensile strength (D), Fracture point (E)"
    inner = """
    <rect width="100%" height="100%" fill="#FFFFFF"/>
    <g transform="translate(80, 270)">
      <!-- Axes -->
      <line x1="0" y1="0" x2="440" y2="0" stroke="#334155" stroke-width="2.5" marker-end="url(#arrow)"/>
      <line x1="0" y1="0" x2="0" y2="-230" stroke="#334155" stroke-width="2.5" marker-end="url(#arrow)"/>
      <text x="450" y="5" fill="#1E293B" font-size="12" font-weight="700">Strain ε</text>
      <text x="-10" y="-240" fill="#1E293B" font-size="12" font-weight="700" text-anchor="end">Stress σ (N/m²)</text>
      <text x="-15" y="15" fill="#64748B" font-size="12" font-weight="600">O</text>

      <!-- Curve OA: Linear Elastic / Proportional Region -->
      <line x1="0" y1="0" x2="90" y2="-140" stroke="#16A34A" stroke-width="3"/>
      <circle cx="90" cy="-140" r="4" fill="#16A34A"/>
      <text x="95" y="-145" fill="#16A34A" font-size="11" font-weight="700">A (Proportional Limit)</text>

      <!-- Curve AB: Elastic Limit / Yield Point -->
      <path d="M 90 -140 Q 120 -170 150 -175" fill="none" stroke="#2563EB" stroke-width="3"/>
      <circle cx="150" cy="-175" r="4" fill="#2563EB"/>
      <text x="145" y="-185" fill="#2563EB" font-size="11" font-weight="700">B (Yield Point σ_y)</text>

      <!-- Curve BC: Plastic Flow & Strain Hardening -->
      <path d="M 150 -175 Q 240 -185 300 -220" fill="none" stroke="#D97706" stroke-width="3"/>
      <circle cx="300" cy="-220" r="5" fill="#D97706"/>
      <text x="305" y="-225" fill="#D97706" font-size="11" font-weight="700">D (Tensile Strength σ_u)</text>

      <!-- Curve DE: Necking & Fracture -->
      <path d="M 300 -220 Q 370 -210 410 -160" fill="none" stroke="#DC2626" stroke-width="3"/>
      <circle cx="410" cy="-160" r="5" fill="#DC2626"/>
      <text x="415" y="-155" fill="#DC2626" font-size="11" font-weight="700">E (Fracture Point)</text>

      <!-- Permanent set dashed line from B -->
      <line x1="150" y1="-175" x2="60" y2="0" stroke="#64748B" stroke-width="1.5" stroke-dasharray="4,3"/>
      <text x="40" y="16" fill="#DC2626" font-size="10" font-weight="600">&lt; 1% Permanent Set</text>

      <!-- Shaded Hooke's Law Region -->
      <rect x="15" y="-115" width="130" height="35" fill="rgba(22, 163, 74, 0.1)" rx="4" stroke="#16A34A" stroke-width="1"/>
      <text x="20" y="-100" fill="#15803D" font-size="10" font-weight="600">Hooke's Law Region</text>
      <text x="20" y="-88" fill="#15803D" font-size="9">Stress = Y × Strain</text>
    </g>
    <g transform="translate(350, 40)">
      <rect width="220" height="80" fill="#F8FAFC" stroke="#CBD5E1" rx="6"/>
      <text x="10" y="18" fill="#0F172A" font-size="11" font-weight="700">Elastic Moduli &amp; Formulas</text>
      <text x="10" y="35" fill="#2563EB" font-size="10">Young's Modulus: Y = (F/A)/(ΔL/L)</text>
      <text x="10" y="51" fill="#D97706" font-size="10">Shear Modulus: G = (F/A)/θ</text>
      <text x="10" y="67" fill="#16A34A" font-size="10">Bulk Modulus: B = -ΔP / (ΔV/V)</text>
    </g>
    """
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=350)


def build_hydraulic_lift_pascal_svg(f1="F₁", a1="A₁", f2="F₂", a2="A₂", title=None, caption=None):
    title = title or "Pascal's Law & Hydraulic Lift Principle"
    caption = caption or "Pressure transmitted undiminished: P₁ = P₂ => F₂ = F₁ × (A₂ / A₁)"
    inner = f"""
    <rect width="100%" height="100%" fill="#FFFFFF"/>
    <g transform="translate(50, 40)">
      <!-- Hydraulic Fluid reservoir -->
      <path d="M 60 120 L 60 210 Q 60 250 100 250 L 380 250 Q 420 250 420 210 L 420 100 L 260 100 L 260 200 L 160 200 L 160 120 Z" fill="#BFDBFE" stroke="#3B82F6" stroke-width="2"/>

      <!-- Left Cylinder (Narrow A1) -->
      <rect x="55" y="60" width="110" height="140" fill="none" stroke="#334155" stroke-width="4"/>
      <rect x="60" y="110" width="100" height="16" fill="#94A3B8" stroke="#475569" stroke-width="2" rx="2"/>
      <!-- Force F1 vector -->
      <line x1="110" y1="40" x2="110" y2="105" stroke="#DC2626" stroke-width="3" marker-end="url(#arrow)"/>
      <text x="120" y="65" fill="#DC2626" font-size="14" font-weight="700">{f1} (Input)</text>
      <text x="110" y="145" fill="#1E3A8A" font-size="12" font-weight="600" text-anchor="middle">Area {a1}</text>

      <!-- Right Cylinder (Wide A2) -->
      <rect x="255" y="40" width="170" height="170" fill="none" stroke="#334155" stroke-width="4"/>
      <rect x="260" y="90" width="160" height="20" fill="#94A3B8" stroke="#475569" stroke-width="2" rx="2"/>
      <!-- Load (Car) on Right Piston -->
      <rect x="290" y="50" width="100" height="38" fill="#EF4444" stroke="#B91C1C" stroke-width="2" rx="6"/>
      <circle cx="315" cy="88" r="8" fill="#1E293B"/>
      <circle cx="365" cy="88" r="8" fill="#1E293B"/>
      <text x="340" y="72" fill="#FFFFFF" font-size="11" font-weight="700" text-anchor="middle">Heavy Load</text>

      <!-- Upward Force F2 vector -->
      <line x1="340" y1="115" x2="340" y2="160" stroke="#16A34A" stroke-width="3" marker-start="url(#arrow)"/>
      <text x="350" y="140" fill="#16A34A" font-size="14" font-weight="700">{f2} (Output)</text>
      <text x="340" y="180" fill="#1E3A8A" font-size="12" font-weight="600" text-anchor="middle">Area {a2}</text>

      <!-- Pressure equality callout -->
      <rect x="165" y="215" width="150" height="30" fill="#FFFFFF" stroke="#2563EB" rx="4"/>
      <text x="240" y="235" fill="#1D4ED8" font-size="12" font-weight="700" text-anchor="middle">P₁ = P₂ = P</text>
    </g>
    <g transform="translate(320, 270)">
      <rect width="240" height="55" fill="#F8FAFC" stroke="#CBD5E1" rx="6"/>
      <text x="12" y="20" fill="#0F172A" font-size="11" font-weight="700">Mechanical Advantage (M.A.)</text>
      <text x="12" y="40" fill="#2563EB" font-size="12" font-weight="600">F₂ = F₁ × (A₂ / A₁) &gt;&gt; F₁</text>
    </g>
    """
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=350)


def build_surface_tension_capillary_svg(title=None, caption=None):
    title = title or "Surface Tension, Meniscus & Capillary Rise"
    caption = caption or "Equilibrium of liquid column: 2πrS cos θ = πr²hρg => h = (2S cos θ) / (rρg)"
    inner = """
    <rect width="100%" height="100%" fill="#FFFFFF"/>
    <g transform="translate(60, 40)">
      <!-- Water Beaker -->
      <rect x="20" y="160" width="220" height="120" fill="#DBEAFE" stroke="#64748B" stroke-width="3" rx="4"/>
      <line x1="20" y1="190" x2="240" y2="190" stroke="#2563EB" stroke-width="2"/>

      <!-- Capillary Tube -->
      <rect x="110" y="50" width="40" height="220" fill="none" stroke="#475569" stroke-width="2.5"/>
      <!-- Liquid column inside capillary -->
      <path d="M 111 190 L 111 100 Q 130 115 149 100 L 149 190 Z" fill="#93C5FD" stroke="#2563EB" stroke-width="1.5"/>

      <!-- Meniscus curvature detail -->
      <line x1="111" y1="100" x2="100" y2="75" stroke="#DC2626" stroke-width="2" marker-end="url(#arrow)"/>
      <line x1="149" y1="100" x2="160" y2="75" stroke="#DC2626" stroke-width="2" marker-end="url(#arrow)"/>
      <text x="95" y="70" fill="#DC2626" font-size="11" font-weight="700">T</text>
      <text x="165" y="70" fill="#DC2626" font-size="11" font-weight="700">T</text>

      <!-- Height h dimension line -->
      <line x1="165" y1="100" x2="165" y2="190" stroke="#D97706" stroke-width="2" stroke-dasharray="3,3"/>
      <line x1="160" y1="100" x2="170" y2="100" stroke="#D97706" stroke-width="2"/>
      <line x1="160" y1="190" x2="170" y2="190" stroke="#D97706" stroke-width="2"/>
      <text x="175" y="150" fill="#D97706" font-size="14" font-weight="700">h (Rise)</text>

      <!-- Radius r annotation -->
      <line x1="111" y1="65" x2="149" y2="65" stroke="#0F172A" stroke-width="1.5"/>
      <text x="130" y="60" fill="#0F172A" font-size="10" font-weight="700" text-anchor="middle">2r</text>
    </g>
    <g transform="translate(330, 70)">
      <rect width="230" height="140" fill="#F8FAFC" stroke="#CBD5E1" rx="8"/>
      <text x="14" y="22" fill="#0F172A" font-size="12" font-weight="700">Capillary &amp; Bubble Formulas</text>
      <text x="14" y="44" fill="#2563EB" font-size="11" font-weight="600">Capillary Rise:</text>
      <text x="14" y="60" fill="#2563EB" font-size="11">h = (2S · cos θ) / (r · ρ · g)</text>
      <text x="14" y="82" fill="#16A34A" font-size="11" font-weight="600">Excess Pressure:</text>
      <text x="14" y="98" fill="#16A34A" font-size="11">Liquid Drop: ΔP = 2S / R</text>
      <text x="14" y="114" fill="#D97706" font-size="11">Soap Bubble (2 surfaces): ΔP = 4S / R</text>
      <text x="14" y="130" fill="#64748B" font-size="10">Angle of contact for pure water &amp; glass: θ ≈ 0°</text>
    </g>
    """
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=350)


def build_bernoulli_venturi_svg(title=None, caption=None):
    title = title or "Bernoulli's Theorem & Venturi-meter Fluid Dynamics"
    caption = caption or "P + ½ρv² + ρgh = const => High speed constriction has lower static pressure (Venturi effect)"
    inner = """
    <rect width="100%" height="100%" fill="#FFFFFF"/>
    <g transform="translate(50, 40)">
      <!-- Main Horizontal Pipe with Throat -->
      <path d="M 20 100 L 140 100 L 210 130 L 290 130 L 360 100 L 480 100 L 480 180 L 360 180 L 290 150 L 210 150 L 140 180 L 20 180 Z" fill="#EFF6FF" stroke="#334155" stroke-width="3"/>

      <!-- Streamlines -->
      <path d="M 20 120 L 140 120 Q 250 138 360 120 L 480 120" fill="none" stroke="#60A5FA" stroke-width="2"/>
      <path d="M 20 140 L 140 140 L 250 140 L 360 140 L 480 140" fill="none" stroke="#3B82F6" stroke-width="2.5"/>
      <path d="M 20 160 L 140 160 Q 250 142 360 160 L 480 160" fill="none" stroke="#60A5FA" stroke-width="2"/>

      <!-- Velocity Vectors -->
      <line x1="60" y1="140" x2="100" y2="140" stroke="#16A34A" stroke-width="2.5" marker-end="url(#arrow)"/>
      <text x="80" y="132" fill="#16A34A" font-size="11" font-weight="700">v₁ (Lower)</text>
      <text x="80" y="196" fill="#1E3A8A" font-size="11" font-weight="600">Area A₁, Pressure P₁</text>

      <line x1="230" y1="140" x2="280" y2="140" stroke="#DC2626" stroke-width="3" marker-end="url(#arrow)"/>
      <text x="255" y="126" fill="#DC2626" font-size="11" font-weight="700">v₂ (High Speed)</text>
      <text x="250" y="172" fill="#1E3A8A" font-size="10" font-weight="600">Throat A₂ &lt; A₁</text>

      <!-- Vertical Manometer Tubes -->
      <rect x="85" y="20" width="20" height="80" fill="#BFDBFE" stroke="#475569" stroke-width="2"/>
      <rect x="240" y="55" width="20" height="75" fill="#BFDBFE" stroke="#475569" stroke-width="2"/>

      <!-- Pressure height difference h -->
      <line x1="115" y1="20" x2="230" y2="20" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>
      <line x1="115" y1="55" x2="230" y2="55" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>
      <line x1="180" y1="20" x2="180" y2="55" stroke="#D97706" stroke-width="2"/>
      <text x="190" y="42" fill="#D97706" font-size="13" font-weight="700">Δh = P₁ - P₂</text>
    </g>
    <g transform="translate(60, 250)">
      <rect width="480" height="55" fill="#F8FAFC" stroke="#CBD5E1" rx="6"/>
      <text x="16" y="20" fill="#0F172A" font-size="11" font-weight="700">Bernoulli's Equation along Streamline</text>
      <text x="16" y="38" fill="#2563EB" font-size="11">P₁ + ½ρv₁² = P₂ + ½ρv₂² =&gt; Rate of Flow Q = A₁A₂ √(2(P₁ - P₂) / ρ(A₁² - A₂²))</text>
    </g>
    """
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=350)


def build_thermodynamics_carnot_cycle_svg(title=None, caption=None):
    title = title or "Ideal Carnot Engine Cycle (P-V Indicator Diagram)"
    caption = caption or "Efficiency η = 1 - (T₂ / T₁) = W_net / Q₁ (Maximum theoretical efficiency)"
    inner = """
    <rect width="100%" height="100%" fill="#FFFFFF"/>
    <g transform="translate(80, 270)">
      <!-- Axes -->
      <line x1="0" y1="0" x2="440" y2="0" stroke="#334155" stroke-width="2.5" marker-end="url(#arrow)"/>
      <line x1="0" y1="0" x2="0" y2="-230" stroke="#334155" stroke-width="2.5" marker-end="url(#arrow)"/>
      <text x="450" y="5" fill="#1E293B" font-size="12" font-weight="700">Volume V</text>
      <text x="-10" y="-240" fill="#1E293B" font-size="12" font-weight="700" text-anchor="end">Pressure P</text>

      <!-- Carnot Cycle Path: 1 -> 2 -> 3 -> 4 -> 1 -->
      <path d="M 80 -190 Q 140 -160 190 -140 Q 250 -90 310 -60 Q 230 -75 170 -90 Q 115 -140 80 -190 Z" fill="rgba(37, 99, 235, 0.15)" stroke="none"/>

      <!-- Stage 1-2: Isothermal Expansion at T1 -->
      <path d="M 80 -190 Q 140 -160 190 -140" fill="none" stroke="#DC2626" stroke-width="3"/>
      <!-- Stage 2-3: Adiabatic Expansion (steeper) -->
      <path d="M 190 -140 Q 250 -90 310 -60" fill="none" stroke="#2563EB" stroke-width="3"/>
      <!-- Stage 3-4: Isothermal Compression at T2 -->
      <path d="M 310 -60 Q 230 -75 170 -90" fill="none" stroke="#16A34A" stroke-width="3"/>
      <!-- Stage 4-1: Adiabatic Compression -->
      <path d="M 170 -90 Q 115 -140 80 -190" fill="none" stroke="#9333EA" stroke-width="3"/>

      <!-- Vertices -->
      <circle cx="80" cy="-190" r="5" fill="#DC2626"/>
      <text x="60" y="-195" fill="#DC2626" font-size="12" font-weight="700">1 (P₁,V₁,T₁)</text>

      <circle cx="190" cy="-140" r="5" fill="#2563EB"/>
      <text x="200" y="-142" fill="#2563EB" font-size="12" font-weight="700">2 (P₂,V₂,T₁)</text>

      <circle cx="310" cy="-60" r="5" fill="#16A34A"/>
      <text x="320" y="-58" fill="#16A34A" font-size="12" font-weight="700">3 (P₃,V₃,T₂)</text>

      <circle cx="170" cy="-90" r="5" fill="#9333EA"/>
      <text x="130" y="-78" fill="#9333EA" font-size="12" font-weight="700">4 (P₄,V₄,T₂)</text>

      <!-- Heat transfer annotations -->
      <text x="115" y="-180" fill="#DC2626" font-size="11" font-weight="700">Q₁ (Absorbed at T₁)</text>
      <text x="220" y="-62" fill="#16A34A" font-size="11" font-weight="700">Q₂ (Rejected at T₂)</text>
      <text x="165" y="-120" fill="#1E3A8A" font-size="13" font-weight="700">W_net</text>
    </g>
    <g transform="translate(350, 40)">
      <rect width="220" height="80" fill="#F8FAFC" stroke="#CBD5E1" rx="6"/>
      <text x="12" y="18" fill="#0F172A" font-size="11" font-weight="700">Carnot Efficiency &amp; 2nd Law</text>
      <text x="12" y="35" fill="#2563EB" font-size="11" font-weight="600">η = 1 - (T₂ / T₁) = W / Q₁</text>
      <text x="12" y="51" fill="#DC2626" font-size="10">For T₂ &gt; 0 K, η &lt; 1 (No 100% engine)</text>
      <text x="12" y="67" fill="#64748B" font-size="10">Carnot Theorem: Reversible is maximum</text>
    </g>
    """
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=350)


def build_kinetic_theory_gas_svg(title=None, caption=None):
    title = title or "Kinetic Theory of Gases: Molecular Pressure & RMS Speed"
    caption = caption or "Pressure P = ⅓ρv_rms² => Average translational kinetic energy E = ³/₂k_BT"
    inner = """
    <rect width="100%" height="100%" fill="#FFFFFF"/>
    <g transform="translate(60, 50)">
      <!-- 3D Cubical Container Wireframe -->
      <polygon points="40,40 180,40 180,180 40,180" fill="rgba(241, 245, 249, 0.6)" stroke="#475569" stroke-width="2"/>
      <polygon points="180,40 240,10 240,150 180,180" fill="rgba(226, 232, 240, 0.7)" stroke="#475569" stroke-width="2"/>
      <polygon points="40,40 100,10 240,10 180,40" fill="rgba(248, 250, 252, 0.8)" stroke="#475569" stroke-width="2"/>

      <!-- Gas Molecules in random motion -->
      <circle cx="70" cy="80" r="4" fill="#2563EB"/>
      <line x1="70" y1="80" x2="95" y2="65" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow)"/>

      <circle cx="130" cy="120" r="4" fill="#2563EB"/>
      <line x1="130" y1="120" x2="155" y2="140" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow)"/>

      <circle cx="90" cy="150" r="4" fill="#2563EB"/>
      <line x1="90" y1="150" x2="65" y2="160" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow)"/>

      <!-- Target molecule colliding with wall area A -->
      <circle cx="170" cy="100" r="5" fill="#DC2626"/>
      <line x1="145" y1="100" x2="175" y2="100" stroke="#DC2626" stroke-width="2" marker-end="url(#arrow)"/>
      <text x="185" y="95" fill="#DC2626" font-size="11" font-weight="700">v_x</text>
      <text x="185" y="110" fill="#B91C1C" font-size="10">Δp = 2mv_x</text>

      <!-- Cube side L -->
      <line x1="40" y1="195" x2="180" y2="195" stroke="#0F172A" stroke-width="1.5"/>
      <text x="110" y="210" fill="#0F172A" font-size="11" font-weight="700" text-anchor="middle">Side L (Volume V = L³)</text>
    </g>
    <g transform="translate(320, 50)">
      <rect width="240" height="170" fill="#F8FAFC" stroke="#CBD5E1" rx="8"/>
      <text x="14" y="22" fill="#0F172A" font-size="12" font-weight="700">Kinetic Postulates &amp; Speeds</text>
      <text x="14" y="42" fill="#2563EB" font-size="11" font-weight="600">Pressure of Gas:</text>
      <text x="14" y="58" fill="#2563EB" font-size="11">P = ⅓ ρ v_rms² = ⅓ (Nm/V) v_rms²</text>
      <text x="14" y="80" fill="#D97706" font-size="11" font-weight="600">Kinetic Temperature Law:</text>
      <text x="14" y="96" fill="#D97706" font-size="11">Average K.E. = ³/₂ k_B T (per molecule)</text>
      <text x="14" y="118" fill="#16A34A" font-size="11" font-weight="600">RMS Speed:</text>
      <text x="14" y="134" fill="#16A34A" font-size="11">v_rms = √(3k_BT / m) = √(3RT / M)</text>
      <text x="14" y="154" fill="#64748B" font-size="10">Degrees of Freedom: Mono=3, Dia=5, Poly=6</text>
    </g>
    """
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=330)


def build_shm_reference_circle_svg(title=None, caption=None):
    title = title or "Simple Harmonic Motion (SHM) & Reference Circle"
    caption = caption or "x(t) = A cos(ωt + φ) | Velocity v = -ωA sin(ωt + φ) | Acceleration a = -ω²x"
    inner = """
    <rect width="100%" height="100%" fill="#FFFFFF"/>
    <g transform="translate(150, 170)">
      <!-- Reference Circle of Radius A -->
      <circle cx="0" cy="0" r="100" fill="none" stroke="#94A3B8" stroke-width="2" stroke-dasharray="4,3"/>
      <!-- Axes -->
      <line x1="-130" y1="0" x2="130" y2="0" stroke="#334155" stroke-width="2"/>
      <line x1="0" y1="-130" x2="0" y2="130" stroke="#334155" stroke-width="2"/>
      <text x="135" y="5" fill="#1E293B" font-size="12" font-weight="700">+A</text>
      <text x="-155" y="5" fill="#1E293B" font-size="12" font-weight="700">-A</text>

      <!-- Rotating Particle P at angle θ = ωt + φ -->
      <line x1="0" y1="0" x2="70.7" y2="-70.7" stroke="#2563EB" stroke-width="2.5"/>
      <circle cx="70.7" cy="-70.7" r="6" fill="#2563EB"/>
      <text x="80" y="-75" fill="#2563EB" font-size="12" font-weight="700">P (Uniform Circle)</text>

      <!-- Angular speed arrow ω -->
      <path d="M 40 -15 A 40 40 0 0 0 28 -28" fill="none" stroke="#D97706" stroke-width="2" marker-end="url(#arrow)"/>
      <text x="38" y="-32" fill="#D97706" font-size="11" font-weight="700">ωt + φ</text>

      <!-- Projection Particle Q on X-axis -->
      <line x1="70.7" y1="-70.7" x2="70.7" y2="0" stroke="#DC2626" stroke-width="1.8" stroke-dasharray="3,3"/>
      <circle cx="70.7" cy="0" r="6" fill="#DC2626"/>
      <text x="72" y="18" fill="#DC2626" font-size="11" font-weight="700">Q (SHM x)</text>

      <!-- Displacement vector x -->
      <line x1="0" y1="-8" x2="70.7" y2="-8" stroke="#DC2626" stroke-width="2.5" marker-end="url(#arrow)"/>
      <text x="30" y="-12" fill="#DC2626" font-size="11" font-weight="700">x = A cos θ</text>
    </g>
    <g transform="translate(330, 40)">
      <rect width="240" height="170" fill="#F8FAFC" stroke="#CBD5E1" rx="8"/>
      <text x="14" y="22" fill="#0F172A" font-size="12" font-weight="700">Kinematics &amp; Energy in SHM</text>
      <text x="14" y="42" fill="#2563EB" font-size="11">Displacement: x(t) = A cos(ωt + φ)</text>
      <text x="14" y="60" fill="#16A34A" font-size="11">Velocity: v = -ωA sin(ωt + φ) = ±ω√(A² - x²)</text>
      <text x="14" y="78" fill="#DC2626" font-size="11">Acceleration: a = -ω²x (Towards mean)</text>
      <text x="14" y="98" fill="#D97706" font-size="11" font-weight="600">Oscillation Periods:</text>
      <text x="14" y="114" fill="#D97706" font-size="11">Spring-Mass: T = 2π √(m / k)</text>
      <text x="14" y="130" fill="#D97706" font-size="11">Simple Pendulum: T = 2π √(L / g)</text>
      <text x="14" y="150" fill="#475569" font-size="10">Total Energy: E = ½kA² = const</text>
    </g>
    """
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=340)


def build_standing_waves_organ_pipe_svg(pipe_type="closed", title=None, caption=None):
    title = title or f"Standing Waves in {'Closed' if pipe_type=='closed' else 'Open'} Organ Pipe"
    caption = caption or "Boundary conditions: Node (N) at rigid/closed boundary, Antinode (A) at open boundary"
    inner = """
    <rect width="100%" height="100%" fill="#FFFFFF"/>
    <g transform="translate(60, 40)">
      <!-- Mode 1: Fundamental Mode -->
      <g transform="translate(0, 0)">
        <text x="0" y="18" fill="#0F172A" font-size="11" font-weight="700">Fundamental (ν₁ = v / 4L)</text>
        <rect x="0" y="25" width="200" height="50" fill="none" stroke="#475569" stroke-width="2"/>
        <line x1="200" y1="25" x2="200" y2="75" stroke="#0F172A" stroke-width="4"/>
        <path d="M 0 32 Q 100 40 200 50" fill="none" stroke="#2563EB" stroke-width="2.5"/>
        <path d="M 0 68 Q 100 60 200 50" fill="none" stroke="#2563EB" stroke-width="2.5" stroke-dasharray="3,3"/>
        <text x="10" y="54" fill="#DC2626" font-size="11" font-weight="700">A</text>
        <text x="185" y="54" fill="#16A34A" font-size="11" font-weight="700">N</text>
        <text x="215" y="53" fill="#64748B" font-size="10">λ₁ = 4L</text>
      </g>

      <!-- Mode 2: 3rd Harmonic (1st Overtone) -->
      <g transform="translate(0, 85)">
        <text x="0" y="18" fill="#0F172A" font-size="11" font-weight="700">1st Overtone (3rd Harmonic ν₃ = 3ν₁)</text>
        <rect x="0" y="25" width="200" height="50" fill="none" stroke="#475569" stroke-width="2"/>
        <line x1="200" y1="25" x2="200" y2="75" stroke="#0F172A" stroke-width="4"/>
        <path d="M 0 30 Q 33 50 67 50 Q 100 50 133 30 Q 167 50 200 50" fill="none" stroke="#D97706" stroke-width="2"/>
        <path d="M 0 70 Q 33 50 67 50 Q 100 50 133 70 Q 167 50 200 50" fill="none" stroke="#D97706" stroke-width="2" stroke-dasharray="3,3"/>
        <text x="62" y="46" fill="#16A34A" font-size="10" font-weight="700">N</text>
        <text x="130" y="26" fill="#DC2626" font-size="10" font-weight="700">A</text>
        <text x="185" y="46" fill="#16A34A" font-size="10" font-weight="700">N</text>
        <text x="215" y="53" fill="#64748B" font-size="10">λ₃ = 4L/3</text>
      </g>

      <!-- Mode 3: 5th Harmonic -->
      <g transform="translate(0, 170)">
        <text x="0" y="18" fill="#0F172A" font-size="11" font-weight="700">2nd Overtone (5th Harmonic ν₅ = 5ν₁)</text>
        <rect x="0" y="25" width="200" height="50" fill="none" stroke="#475569" stroke-width="2"/>
        <line x1="200" y1="25" x2="200" y2="75" stroke="#0F172A" stroke-width="4"/>
        <path d="M 0 30 Q 20 50 40 50 Q 60 50 80 30 Q 100 50 120 50 Q 140 50 160 30 Q 180 50 200 50" fill="none" stroke="#16A34A" stroke-width="2"/>
        <text x="215" y="53" fill="#64748B" font-size="10">λ₅ = 4L/5</text>
      </g>
    </g>
    <g transform="translate(360, 50)">
      <rect width="200" height="160" fill="#F8FAFC" stroke="#CBD5E1" rx="8"/>
      <text x="12" y="22" fill="#0F172A" font-size="11" font-weight="700">Harmonic Frequencies Ratio</text>
      <text x="12" y="44" fill="#DC2626" font-size="11" font-weight="600">Closed Organ Pipe:</text>
      <text x="12" y="60" fill="#DC2626" font-size="11">Odd harmonics only!</text>
      <text x="12" y="76" fill="#2563EB" font-size="11">ν₁ : ν₃ : ν₅ = 1 : 3 : 5</text>
      <text x="12" y="102" fill="#16A34A" font-size="11" font-weight="600">Open Organ Pipe:</text>
      <text x="12" y="118" fill="#16A34A" font-size="11">All harmonics present!</text>
      <text x="12" y="134" fill="#16A34A" font-size="11">ν₁ : ν₂ : ν₃ = 1 : 2 : 3</text>
      <text x="12" y="150" fill="#64748B" font-size="10">Note: Open pipes richer in sound</text>
    </g>
    """
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=320)


def build_beats_acoustic_svg(f1="256 Hz", f2="252 Hz", title=None, caption=None):
    title = title or f"Acoustic Beats Waveform ({f1} &amp; {f2})"
    caption = caption or "Beat frequency ν_beat = |ν₁ - ν₂| = 4 Hz (Periodic variation in sound intensity)"
    inner = """
    <rect width="100%" height="100%" fill="#FFFFFF"/>
    <g transform="translate(60, 40)">
      <!-- Constituent Wave 1 -->
      <g transform="translate(0, 0)">
        <text x="0" y="15" fill="#2563EB" font-size="11" font-weight="700">Wave 1 (y₁ = A sin 2πf₁t, 256 Hz)</text>
        <line x1="0" y1="35" x2="480" y2="35" stroke="#94A3B8" stroke-width="1"/>
        <path d="M 0 35 Q 12 15 24 35 Q 36 55 48 35 Q 60 15 72 35 Q 84 55 96 35 Q 108 15 120 35 Q 132 55 144 35 Q 156 15 168 35 Q 180 55 192 35 Q 204 15 216 35 Q 228 55 240 35 Q 252 15 264 35 Q 276 55 288 35 Q 300 15 312 35 Q 324 55 336 35 Q 348 15 360 35 Q 372 55 384 35 Q 396 15 408 35 Q 420 55 432 35 Q 444 15 456 35 Q 468 55 480 35" fill="none" stroke="#2563EB" stroke-width="1.8"/>
      </g>

      <!-- Constituent Wave 2 -->
      <g transform="translate(0, 65)">
        <text x="0" y="15" fill="#D97706" font-size="11" font-weight="700">Wave 2 (y₂ = A sin 2πf₂t, 252 Hz)</text>
        <line x1="0" y1="35" x2="480" y2="35" stroke="#94A3B8" stroke-width="1"/>
        <path d="M 0 35 Q 13 15 26 35 Q 39 55 52 35 Q 65 15 78 35 Q 91 55 104 35 Q 117 15 130 35 Q 143 55 156 35 Q 169 15 182 35 Q 195 55 208 35 Q 221 15 234 35 Q 247 55 260 35 Q 273 15 286 35 Q 299 55 312 35 Q 325 15 338 35 Q 351 55 364 35 Q 377 15 390 35 Q 403 55 416 35 Q 429 15 442 35 Q 455 55 468 35 L 480 35" fill="none" stroke="#D97706" stroke-width="1.8"/>
      </g>

      <!-- Resultant Beat Waveform with Modulated Envelope -->
      <g transform="translate(0, 145)">
        <text x="0" y="15" fill="#DC2626" font-size="12" font-weight="700">Superposition: Beats Waveform (Waxing &amp; Waning of Loudness)</text>
        <line x1="0" y1="55" x2="480" y2="55" stroke="#334155" stroke-width="1.5"/>
        <!-- Envelope Top -->
        <path d="M 0 25 Q 120 55 240 25 Q 360 55 480 25" fill="none" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>
        <!-- Envelope Bottom -->
        <path d="M 0 85 Q 120 55 240 85 Q 360 55 480 85" fill="none" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>

        <!-- Rapid oscillations inside envelope -->
        <path d="M 0 55 Q 6 30 12 55 Q 18 80 24 55 Q 30 35 36 55 Q 42 75 48 55 Q 54 40 60 55 Q 66 70 72 55 Q 78 45 84 55 Q 90 65 96 55 Q 102 50 108 55 Q 114 60 120 55 Q 126 50 132 55 Q 138 60 144 55 Q 150 45 156 55 Q 162 65 168 55 Q 174 40 180 55 Q 186 70 192 55 Q 198 35 204 55 Q 210 75 216 55 Q 222 30 228 55 Q 234 80 240 55 Q 246 30 252 55 Q 258 80 264 55 Q 270 35 276 55 Q 282 75 288 55 Q 294 40 300 55 Q 306 70 312 55 Q 318 45 324 55 Q 330 65 336 55 Q 342 50 348 55 Q 354 60 360 55 Q 366 50 372 55 Q 378 60 384 55 Q 390 45 396 55 Q 402 65 408 55 Q 414 40 420 55 Q 426 70 432 55 Q 438 35 444 55 Q 450 75 456 55 Q 462 30 468 55 Q 474 80 480 55" fill="none" stroke="#DC2626" stroke-width="2"/>

        <!-- Beat Period Annotation -->
        <line x1="0" y1="95" x2="240" y2="95" stroke="#16A34A" stroke-width="2"/>
        <text x="120" y="110" fill="#16A34A" font-size="11" font-weight="700" text-anchor="middle">Beat Period T_beat = 1 / (f₁ - f₂) = 0.25 s</text>
      </g>
    </g>
    """
    return get_svg_wrapper(inner, title=title, caption=caption, width=600, height=330)
