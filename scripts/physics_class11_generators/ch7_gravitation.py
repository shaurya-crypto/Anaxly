"""
ch7_gravitation.py
CBSE Class 11 Physics - Chapter 7: Gravitation
Part 1 (Mid-Term Syllabus, Unit VI: Gravitation)
Target Pacing: December 13, 2026 to December 16, 2026 (6 Modules, 4 Days)
"""

import sys
import os
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

import svg_builder_physics11 as sb

CURRICULUM_ID = "c11_phy_ch07_gravitation"
CLASS_LEVEL = "Class 11"
BOARD = "CBSE"
SUBJECT = "Physics"

def get_modules():
    modules = []

    # -------------------------------------------------------------
    # MODULE 1: Kepler's Laws of Planetary Motion
    # Date: 2026-12-13
    # -------------------------------------------------------------
    mod1_svg = sb.build_gravitation_orbit_svg(
        variant="kepler",
        title="Kepler's Three Laws of Planetary Motion",
        caption="Law of Orbits (Ellipse), Law of Areas (dA/dt = L/2m = const), Law of Periods (T² ∝ a³)"
    )

    modules.append({
        "order_index": 39,
        "title": "Historical Cosmology, Kepler's Three Laws of Planetary Motion & Deduction of Inverse Square Law",
        "description": "Historical transition from geocentric (Ptolemy) to heliocentric (Copernicus) models, Tycho Brahe's precision observational data, Johannes Kepler's three empirical laws of planetary motion, law of areas from angular momentum conservation, and deduction of Newton's inverse-square gravitational force.",
        "target_completion_date": "2026-12-13",
        "syllabus_pacing": "Day 32 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Historical evolution: Geocentric model (Ptolemy) vs Heliocentric model (Copernicus, Galileo)",
            "Tycho Brahe's astronomical observations and Johannes Kepler's mathematical formulation",
            "Kepler's First Law (Law of Orbits): All planets move in elliptical orbits with the Sun at one focus",
            "Geometry of an ellipse: Semi-major axis (a), semi-minor axis (b), eccentricity (e), perihelion, and aphelion",
            "Kepler's Second Law (Law of Areas): The line joining the planet to the Sun sweeps out equal areas in equal intervals of time",
            "Derivation of Areal Velocity: dA/dt = 1/2 r² (dθ/dt) = L / (2m) = constant (conservation of angular momentum under central force)",
            "Consequences of Law of Areas: Planet moves fastest at perihelion (closest to Sun) and slowest at aphelion (farthest)",
            "Kepler's Third Law (Law of Periods): The square of the orbital period T is proportional to the cube of semi-major axis a (T² ∝ a³)",
            "Deduction of Newton's inverse-square law: F = m v² / r = m (2π r / T)² / r = 4π² m r / T² = 4π² m r / (k r³) = (4π² m / k) (1 / r²)"
        ],
        "key_concepts": [
            "Kepler's First Law: Elliptical Orbits with Sun at Focus",
            "Kepler's Second Law: Constant Areal Velocity (dA/dt = L/2m)",
            "Kepler's Third Law: Harmonic Law T² ∝ a³",
            "Deduction of Newton's Inverse-Square Law (F ∝ 1/r²)"
        ],
        "success_criteria": [
            "State all three of Kepler's laws of planetary motion verbatim",
            "Prove analytically that Kepler's second law is a direct consequence of the conservation of angular momentum",
            "Use the harmonic law T₁² / T₂² = a₁³ / a₂³ to compute planetary orbital periods and solar distances",
            "Derive Newton's 1/r² force law using circular orbit approximations and Kepler's third law"
        ],
        "chapter_notes": """# CHAPTER 7: GRAVITATION
## MODULE 1: Kepler's Laws of Planetary Motion

### 1. Historical Background: Geocentric to Heliocentric
- **Geocentric Model**: Proposed by Claudius Ptolemy in the 2nd century A.D. Postulated that the Earth is stationary at the center of the universe, and the Sun, stars, and planets revolve around it in circular orbits with complex epicycles.
- **Heliocentric Model**: Proposed by Nicolaus Copernicus (1543). Postulated that the Sun is at rest at the center of the solar system, and all planets, including Earth, move in circles around it. Supported observationally by Galileo Galilei using his telescope (phases of Venus, moons of Jupiter).
- **Tycho Brahe & Johannes Kepler**: Tycho Brahe recorded continuous, extraordinarily precise naked-eye planetary measurements. Johannes Kepler analyzed this data over 16 years, discovering that planetary orbits are **ellipses, not circles**!

### 2. Kepler's Three Laws of Planetary Motion
1. **Law of Orbits (First Law)**:
   *Statement*: Every planet revolves around the Sun in an **elliptical orbit**, with the Sun situated at one of the two foci of the ellipse.
   - Equation of an ellipse: $\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$, where $a$ is the semi-major axis and $b$ is the semi-minor axis.
   - **Perihelion ($r_p$)**: Point of closest approach to the Sun: $r_p = a(1 - e)$.
   - **Aphelion ($r_a$)**: Point of farthest distance from the Sun: $r_a = a(1 + e)$.
   - Eccentricity $e = \\sqrt{1 - b^2/a^2}$. For Earth, $e \\approx 0.0167$ (nearly circular).

2. **Law of Areas (Second Law)**:
   *Statement*: The radius vector drawn from the Sun to a planet sweeps out **equal areas in equal intervals of time**; that is, the **areal velocity** of the planet is constant.
   $$\\frac{dA}{dt} = \\text{constant}$$
   - **Proof from Conservation of Angular Momentum**:
     In a small time interval $\\Delta t$, the area swept out is approximately a triangle:
     $$\\Delta A = \\frac{1}{2} |\\vec{r} \\times \\Delta \\vec{r}| = \\frac{1}{2} |\\vec{r} \\times \\vec{v} \\Delta t|$$
     $$\\frac{dA}{dt} = \\frac{1}{2} |\\vec{r} \\times \\vec{v}| = \\frac{1}{2m} |\\vec{r} \\times m\\vec{v}| = \\frac{|\\vec{L}|}{2m}$$
     Since gravitational force $\\vec{F}_g = -\\frac{GMm}{r^2}\\hat{r}$ is a **central force** directed toward the Sun, torque $\\vec{\\tau} = \\vec{r} \\times \\vec{F}_g = 0$.
     Therefore, angular momentum $\\vec{L}$ is strictly conserved:
     $$\\vec{\\tau} = 0 \\implies \\vec{L} = \\text{constant} \\implies \\frac{dA}{dt} = \\frac{L}{2m} = \\text{constant}$$
   - **Consequence**: Since $L = m r_p v_p = m r_a v_a = \\text{constant}$:
     $$v_p r_p = v_a r_a \\implies \\frac{v_p}{v_a} = \\frac{r_a}{r_p}$$
     *A planet moves fastest at perihelion and slowest at aphelion!*

3. **Law of Periods (Third Law)**:
   *Statement*: The square of the orbital time period $T$ of a planet is directly proportional to the cube of the semi-major axis $a$ of its elliptical orbit.
   $$T^2 \\propto a^3 \\implies \\frac{T^2}{a^3} = K_s$$
   where $K_s$ is Kepler's constant ($K_s = \\frac{4\\pi^2}{G M_{\\text{sun}}}$), identical for all planets orbiting the Sun!

### 3. Deduction of Newton's Inverse-Square Law from Kepler's Third Law
Consider a planet of mass $m$ revolving in a circular orbit of radius $r$ around the Sun with speed $v$ and period $T$.
- Centripetal force:
  $$F = \\frac{m v^2}{r} = \\frac{m}{r} \\left(\\frac{2\\pi r}{T}\\right)^2 = \\frac{4\\pi^2 m r}{T^2}$$
- By Kepler's third law, $T^2 = k r^3$:
  $$F = \\frac{4\\pi^2 m r}{k r^3} = \\left(\\frac{4\\pi^2 m}{k}\\right) \\frac{1}{r^2} \\implies F \\propto \\frac{1}{r^2}$$
- Since force is mutual (Newton's third law), $F$ must also be proportional to the Sun's mass $M$:
  $$F = G \\frac{M m}{r^2}$$
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 7.1: Let the speed of the planet at the perihelion P in Fig. 7.1 be v_P and the Sun-planet distance SP be r_P. Relate {r_P, v_P} to the corresponding quantities at the aphelion {r_A, v_A}. Will the planet take equal times to traverse BAC and CPB?",
                "given": "Planet with perihelion {r_P, v_P} and aphelion {r_A, v_A}. Sun at focus S.",
                "formula": "Conservation of angular momentum: L = m r_P v_P = m r_A v_A; Kepler's Second Law: dA/dt = constant.",
                "substitution": "Since gravitational torque τ = 0 about the Sun, angular momentum is conserved: m r_P v_P = m r_A v_A ⇒ v_P / v_A = r_A / r_P. Since r_A > r_P, v_P > v_A. For the areas: Area SBAC swept when traveling through BAC is greater than Area SCPB. By Kepler's second law (dA/dt = const), time taken is directly proportional to the area swept.",
                "calculation": "Time t_BAC / t_CPB = Area(SBAC) / Area(SCPB) > 1.",
                "finalAnswer": "The velocity relation is v_P / v_A = r_A / r_P. The planet will NOT take equal times; it takes longer to traverse BAC because Area(SBAC) > Area(SCPB).",
                "unit": "ratios",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            }
        ],
        "common_misconceptions": [
            "Assuming planets move at uniform speed in their orbits: Because orbits are elliptical and angular momentum is conserved, planetary speed varies continuously, peaking at perihelion and reaching a minimum at aphelion!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod1_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Keplerian Elliptical Orbit & Areal Velocity",
                    "diagram_title": "Equal Areas in Equal Times",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "kepler laws elliptical orbit equal areas sun focus physics diagram",
                    "video_search_query": "kepler laws of planetary motion class 11 physics ncert",
                    "what_to_make": "Ellipse with Sun at focus F1 showing triangular sweep sectors A1 and A2",
                    "what_to_explain": "Demonstrate that dA/dt = L/2m = constant arises from zero central torque",
                    "timing_and_cue": "Step 2 (Geometric Proof)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "If the distance of Earth from the Sun were halved, how many days would there be in a year?",
                            "ideal_answer": "Approximately 129 days! By Kepler's third law, T₂ / T₁ = (r₂ / r₁)³/² = (1/2)³/² = 1 / (2√2) ≈ 1 / 2.828. Thus T₂ = 365 / 2.828 ≈ 129 days.",
                            "socratic_hint": "Use the ratio T₂² / T₁² = r₂³ / r₁³ with r₂ = r₁ / 2.",
                            "type": "Board Exam Numerical"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 2: Universal Law of Gravitation & Cavendish Experiment
    # Date: 2026-12-14
    # -------------------------------------------------------------
    grav_forces = [
        {"p1": (2, 5), "p2": (4, 5), "color": "#2563EB", "stroke_width": 2.5, "arrow": True, "label": "F₁₂"},
        {"p1": (8, 5), "p2": (6, 5), "color": "#DC2626", "stroke_width": 2.5, "arrow": True, "label": "F₂₁ = -F₁₂"}
    ]
    grav_points = [
        {"x": 2, "y": 5, "color": "#2563EB", "label": "Mass m₁"},
        {"x": 8, "y": 5, "color": "#DC2626", "label": "Mass m₂"}
    ]
    mod2_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 10), range_y=(0, 10),
        lines=grav_forces, points=grav_points,
        x_label="Separation r (m)", y_label="Force Plane",
        title="Newton's Universal Law of Gravitation: F⃗₁₂ = -G (m₁ m₂ / r²) r̂₁₂",
        caption="Action-reaction pair: F₁₂ = -F₂₁; Universal gravitational constant G = 6.674 × 10⁻¹¹ N m²/kg²"
    )

    modules.append({
        "order_index": 40,
        "title": "Newton's Universal Law of Gravitation, Gravitational Constant G & Cavendish Experiment",
        "description": "Formulation of Newton's Universal Law of Gravitation in scalar and vector notation, properties of gravitational interaction (central, conservative, medium-independent), determination of G via Henry Cavendish's torsion balance experiment, and gravitational superposition.",
        "target_completion_date": "2026-12-14",
        "syllabus_pacing": "Day 33 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Statement of Newton's Universal Law of Gravitation: F = G (m₁ m₂) / r²",
            "Vector form of Universal Gravitation: F⃗₁₂ = -G [m₁ m₂ / r₁₂²] r̂₁₂ satisfying Newton's Third Law F⃗₁₂ = -F⃗₂₁",
            "Properties of Gravitational Force: Always attractive, central force, inverse-square dependence, independent of intervening medium",
            "The Universal Gravitational Constant G: Value G = 6.674 × 10⁻¹¹ N·m²/kg² and dimensions [M⁻¹ L³ T⁻²]",
            "Henry Cavendish's Torsion Balance Experiment (1798): Apparatus, quartz fiber restoring torque, and deflection measurement",
            "Weighing the Earth: Calculating Earth's mass M_E = g R_E² / G ≈ 5.97 × 10²⁴ kg using Cavendish's G",
            "Principle of Superposition for gravitational forces: F⃗_net = Σ F⃗_i",
            "Shell Theorem (Newton's Theorem): (1) Gravitational force exerted by a spherical shell on an external point mass acts as if all shell mass is concentrated at center; (2) Gravitational force on an internal mass inside a hollow shell is identically ZERO"
        ],
        "key_concepts": [
            "Newton's Universal Gravitation Law (Vector Form)",
            "Universal Constant G vs Local Acceleration g",
            "Cavendish Torsion Balance Experiment",
            "Newton's Spherical Shell Theorem (F_inside = 0)",
            "Gravitational Superposition Principle"
        ],
        "success_criteria": [
            "State Newton's Universal Law of Gravitation and write it in vector notation",
            "Describe the principle, working, and formula of the Cavendish torsion balance experiment to measure G",
            "Calculate Earth's mass from the measured values of g, R_E, and G",
            "Apply the shell theorem to calculate gravitational forces for point masses outside and inside hollow spheres"
        ],
        "chapter_notes": """# CHAPTER 7: GRAVITATION
## MODULE 2: Universal Law of Gravitation & Cavendish Experiment

### 1. Newton's Universal Law of Gravitation
- **Statement**: *Every particle in the universe attracts every other particle with a force that is directly proportional to the product of their masses and inversely proportional to the square of the distance between them.*
  $$F = G \\frac{m_1 m_2}{r^2}$$
- **Vector Form**:
  Let $\\vec{r}_1$ and $\\vec{r}_2$ be the position vectors of particles $m_1$ and $m_2$. The force on $m_1$ due to $m_2$ is:
  $$\\vec{F}_{12} = G \\frac{m_1 m_2}{r_{12}^2} \\hat{r}_{21} = -G \\frac{m_1 m_2}{r_{12}^2} \\hat{r}_{12}$$
  - Since $\\hat{r}_{21} = -\\hat{r}_{12}$, we have:
    $$\\vec{F}_{12} = -\\vec{F}_{21}$$
  *Gravitational forces between two particles form an action-reaction pair satisfying Newton's Third Law!*

### 2. Characteristics of Gravitational Force
1. **Always Attractive**: Gravitational force is strictly attractive, never repulsive.
2. **Central Force**: It acts along the line joining the centers of the two interacting bodies.
3. **Conservative Force**: Work done by gravity around a closed loop is zero.
4. **Medium Independence**: Gravitational force is completely unaffected by the presence or chemical nature of any intervening medium.
5. **Universal Range**: Acts across infinite distances, governing everything from falling apples to colliding galaxies.

### 3. The Gravitational Constant $G$ & Cavendish Experiment
- **Dimensions of $G$**:
  $$[G] = \\frac{[F] [r^2]}{[m_1 m_2]} = \\frac{[M L T^{-2}] [L^2]}{[M^2]} = [M^{-1} L^3 T^{-2}]$$
- **Numerical Value**:
  $$G = 6.674 \\times 10^{-11}\\text{ N}\\cdot\\text{m}^2\\text{kg}^{-2} = 6.674 \\times 10^{-8}\\text{ dyne}\\cdot\\text{cm}^2\\text{g}^{-2}$$
- **The Cavendish Torsion Balance (1798)**:
  - Two small lead spheres of mass $m$ attached to ends of a light rod of length $L$ suspended by a fine quartz wire.
  - Two large lead spheres of mass $M$ brought close to the small spheres.
  - Gravitational attraction exerts a deflecting couple: $\\tau_{\\text{grav}} = F \\cdot L = \\left(G \\frac{M m}{d^2}\\right) L$.
  - The quartz wire twists through angle $\\theta$, generating a restoring elastic torque: $\\tau_{\\text{restoring}} = C \\theta$.
  - In equilibrium:
    $$G \\frac{M m}{d^2} L = C \\theta \\implies G = \\frac{C \\theta d^2}{M m L}$$
- **"Weighing the Earth"**:
  Knowing $G = 6.67 \\times 10^{-11}\\text{ N m}^2/\\text{kg}^2$, $g = 9.8\\text{ m/s}^2$, and $R_E = 6.4 \\times 10^6\\text{ m}$:
  $$M_E = \\frac{g R_E^2}{G} = \\frac{(9.8)(6.4 \\times 10^6)^2}{6.67 \\times 10^{-11}} \\approx 5.97 \\times 10^{24}\\text{ kg}$$

### 4. Newton's Spherical Shell Theorems
1. **Theorem 1**: The gravitational force of attraction that a uniform spherical shell of mass $M$ exerts on a point mass $m$ situated **outside** the shell is identical to that of a single point mass $M$ placed at its center:
   $$F = G \\frac{M m}{r^2} \\quad (r \\ge R)$$
2. **Theorem 2**: The gravitational force exerted by a uniform spherical shell on any point mass situated **inside** the shell is identically **zero**!
   $$F = 0 \\quad (r < R)$$
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 7.2: Three equal masses of m kg each are fixed at the vertices of an equilateral triangle of side a. (a) What is the force acting on a mass 2m placed at the centroid G of the triangle? (b) What is the force if the mass at vertex A is doubled?",
                "given": "Equilateral triangle ABC with side a. Vertex masses m_A = m_B = m_C = m. Centroid G has mass 2m. Distance from centroid to any vertex r = a / √3.",
                "formula": "F⃗_net = F⃗_GA + F⃗_GB + F⃗_GC; Gravitational force magnitude F = G (m · 2m) / r² = 2 G m² / (a²/3) = 6 G m² / a².",
                "substitution": "(a) The three forces F⃗_GA, F⃗_GB, F⃗_GC have equal magnitude F = 6 G m² / a² and are oriented symmetrically at 120° to each other in the plane. Vector sum of three equal forces at 120° is identically zero. (b) If mass at A is doubled to 2m, force F'_GA becomes 2F = 12 G m² / a², while F_GB and F_GC remain F. The resultant of F_GB and F_GC is a force of magnitude F directed opposite to F'_GA.",
                "calculation": "Net force F_net = F'_GA - F = 2F - F = F = 6 G m² / a² directed toward vertex A.",
                "finalAnswer": "(a) The net gravitational force on the mass at the centroid is ZERO. (b) If the mass at A is doubled, the net force is 6 G m² / a² directed toward vertex A.",
                "unit": "Newtons (N)",
                "has_diagram": True,
                "diagram_svg": mod2_svg
            }
        ],
        "common_misconceptions": [
            "Confusing G with g: G is a universal physical constant (identical throughout all space and time), whereas g is the local acceleration due to gravity, which varies significantly with altitude, depth, latitude, and planetary mass!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod2_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Cavendish Torsion Balance Apparatus",
                    "diagram_title": "Torsional Deflection for Gravitational Constant G",
                    "diagram_type": "svg",
                    "svg": mod2_svg,
                    "image_search_query": "cavendish experiment torsion balance measuring G physics diagram",
                    "video_search_query": "cavendish experiment measuring gravitational constant class 11",
                    "what_to_make": "Torsion wire with light rod, small masses m and large masses M exerting deflecting couple",
                    "what_to_explain": "Explain how mirror and light scale amplify minuscule angular twists theta to compute G",
                    "timing_and_cue": "Step 2 (Experimental Apparatus)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "What is the gravitational force on an astronaut inside a hollow spherical spaceship orbiting in deep space?",
                            "ideal_answer": "Zero. By Newton's second shell theorem, the gravitational field inside any uniform spherical shell of mass is identically zero everywhere within its cavity!",
                            "socratic_hint": "Recall Newton's shell theorem for interior points.",
                            "type": "Conceptual Reasoning"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 3: Acceleration Due to Gravity (g) & Its Variations
    # Date: 2026-12-15
    # -------------------------------------------------------------
    mod3_svg = sb.build_gravitation_orbit_svg(
        variant="g_variation",
        title="Variation of Acceleration Due to Gravity (g) with Distance r",
        caption="Linear increase inside Earth: g ∝ r; Inverse-square decay outside: g ∝ 1/r²; Peak at surface: g = 9.8 m/s²"
    )

    modules.append({
        "order_index": 41,
        "title": "Acceleration Due to Gravity g & Its Variations with Altitude, Depth, Shape & Rotation",
        "description": "Relation between g, G, mass and radius of Earth, variation of g with altitude above Earth's surface, variation with depth below surface, variation with latitude due to Earth's rotation (centrifugal effect), and oblate spheroidal shape of Earth.",
        "target_completion_date": "2026-12-15",
        "syllabus_pacing": "Day 34 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Relation between g and G: g = GM_E / R_E² = 4/3 π G ρ R_E",
            "Standard value of g at Earth's surface: 9.8 m/s² (average)",
            "Variation of g with Altitude h: g_h = GM_E / (R_E + h)² = g [R_E / (R_E + h)]²",
            "Binomial approximation for small heights (h << R_E): g_h ≈ g (1 - 2h / R_E)",
            "Fractional and percentage decrease in g with altitude: Δg/g = 2h / R_E",
            "Variation of g with Depth d: Mass of active sphere M' = M_E (r/R_E)³; g_d = GM'/r² = g (1 - d / R_E)",
            "Linear variation of g inside Earth: At center of Earth (d = R_E), g = 0",
            "Comparison: g decreases faster with altitude (rate 2/R_E) than with depth (rate 1/R_E) for h << R_E",
            "Variation of g with Latitude λ due to Earth's rotation: Effective gravity g' = g - ω² R_E cos² λ",
            "Values at Poles (λ = 90°): g_pole = g (maximum); At Equator (λ = 0°): g_equator = g - ω² R_E (minimum)",
            "Variation due to Earth's oblate shape: R_equator > R_pole by ~21 km ⇒ g_pole > g_equator"
        ],
        "key_concepts": [
            "Surface Gravity Formula: g = GM_E / R_E²",
            "Altitude Variation: g_h ≈ g (1 - 2h/R_E)",
            "Depth Variation: g_d = g (1 - d/R_E)",
            "Rotational Latitude Variation: g' = g - ω² R_E cos² λ",
            "Peak Gravity Invariant: g is maximal at Earth's surface poles"
        ],
        "success_criteria": [
            "Derive the formulas for variation of g with altitude and depth from Newton's law of gravitation",
            "Prove that the decrease in g at a height h is twice the decrease at depth d (when h = d << R_E)",
            "Calculate effective g at the equator and find the speed of Earth rotation required for weightlessness at the equator",
            "Plot the comprehensive graph of g versus distance r from the center of Earth (r = 0 to r >> R_E)"
        ],
        "chapter_notes": """# CHAPTER 7: GRAVITATION
## MODULE 3: Acceleration Due to Gravity (g) & Variations

### 1. Acceleration Due to Gravity ($g$) at Earth's Surface
- Consider an object of mass $m$ on the surface of Earth (mass $M_E$, radius $R_E$).
- By Newton's second law and universal gravitation:
  $$F = m g = G \\frac{M_E m}{R_E^2} \\implies g = \\frac{G M_E}{R_E^2}$$
- In terms of mean density $\\rho$ of the Earth:
  $$M_E = \\frac{4}{3}\\pi R_E^3 \\rho \\implies g = \\frac{G}{R_E^2}\\left(\\frac{4}{3}\\pi R_E^3 \\rho\\right) = \\frac{4}{3}\\pi G \\rho R_E$$
- **Standard Numerical Value**: $g = 9.8\\text{ m/s}^2 = 980\\text{ cm/s}^2$.

### 2. Variation of $g$ with Altitude ($h$)
- At height $h$ above the Earth's surface:
  $$g_h = \\frac{G M_E}{(R_E + h)^2} = \\frac{G M_E}{R_E^2 \\left(1 + \\frac{h}{R_E}\\right)^2} = g \\left(1 + \\frac{h}{R_E}\\right)^{-2}$$
- For small heights ($h \\ll R_E$), expanding by Binomial Theorem:
  $$g_h \\approx g \\left(1 - \\frac{2h}{R_E}\\right)$$
- **Fractional Decrease**:
  $$\\frac{\\Delta g}{g} = \\frac{g - g_h}{g} = \\frac{2h}{R_E}$$

### 3. Variation of $g$ with Depth ($d$)
- At depth $d$ below the Earth's surface (distance from center $r = R_E - d$):
- By Newton's shell theorem, the outer spherical shell of thickness $d$ exerts zero net gravitational force on the mass. Only the inner sphere of radius $r$ contributes!
- Mass of the inner sphere:
  $$M' = \\frac{4}{3}\\pi (R_E - d)^3 \\rho = M_E \\left(\\frac{R_E - d}{R_E}\\right)^3$$
- Acceleration at depth $d$:
  $$g_d = \\frac{G M'}{(R_E - d)^2} = \\frac{G M_E (R_E - d)^3}{R_E^3 (R_E - d)^2} = \\frac{G M_E}{R_E^2} \\left(\\frac{R_E - d}{R_E}\\right)$$
  $$g_d = g \\left(1 - \\frac{d}{R_E}\\right)$$
- **At the center of the Earth ($d = R_E$)**:
  $$g_{\\text{center}} = g (1 - 1) = 0$$
- **Key Comparison**:
  - For $h \\ll R_E$: $g_h = g(1 - 2h/R_E)$.
  - For depth $d$: $g_d = g(1 - d/R_E)$.
  *To produce the same drop in $g$, the depth must be twice the height ($d = 2h$)!*

### 4. Variation of $g$ with Latitude ($\\lambda$) Due to Earth's Rotation
- As the Earth rotates with angular speed $\\omega$, an object at latitude $\\lambda$ rotates in a circle of radius $r = R_E \\cos \\lambda$.
- Centrifugal force directed outward: $F_{\\text{cf}} = m \\omega^2 r = m \\omega^2 R_E \\cos \\lambda$.
- Resolving along the radial direction:
  $$g' = g - \\omega^2 R_E \\cos^2 \\lambda$$
  1. **At the Equator ($\\lambda = 0^\\circ$)**:
     $$g_{\\text{equator}} = g - \\omega^2 R_E \\quad (\\text{Minimum})$$
  2. **At the Poles ($\\lambda = 90^\\circ$)**:
     $$g_{\\text{pole}} = g \\quad (\\text{Maximum, rotation has zero effect})$$
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 7.3: At what height above the surface of the earth will the acceleration due to gravity be 1% of its value on the surface? (Radius of earth R_E = 6400 km).",
                "given": "g_h = 1% of g = g / 100. R_E = 6400 km.",
                "formula": "g_h = g [R_E / (R_E + h)]² (Do NOT use binomial approximation here because h is not small!).",
                "substitution": "g / 100 = g [R_E / (R_E + h)]² ⇒ 1 / 100 = [R_E / (R_E + h)]² ⇒ 1 / 10 = R_E / (R_E + h).",
                "calculation": "R_E + h = 10 R_E ⇒ h = 9 R_E = 9 × 6400 km = 57,600 km.",
                "finalAnswer": "The acceleration due to gravity drops to 1% of its surface value at a height of 9 R_E = 57,600 km.",
                "unit": "km",
                "has_diagram": True,
                "diagram_svg": mod3_svg
            }
        ],
        "common_misconceptions": [
            "Blindly using the binomial formula g_h = g(1 - 2h/R) for large heights: The formula g(1 - 2h/R) is valid ONLY when h << R (e.g. h < 500 km). For heights comparable to R_E, one MUST use the exact formula g_h = g [R_E / (R_E + h)]²!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod3_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "g versus r Coordinate Profile",
                    "diagram_title": "Linear Rise Inside, Inverse Square Decay Outside",
                    "diagram_type": "svg",
                    "svg": mod3_svg,
                    "image_search_query": "variation of g with distance from center of earth graph physics",
                    "video_search_query": "variation of g with altitude and depth class 11 physics ncert",
                    "what_to_make": "Graph showing straight line g ∝ r from 0 to R_E, peak at R_E, and hyperbolic drop g ∝ 1/r²",
                    "what_to_explain": "Explain why gravity rises linearly from zero at the center of the Earth to 9.8 m/s² at the surface",
                    "timing_and_cue": "Step 2 (Graph Interpretation)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "At what depth below Earth's surface does the acceleration due to gravity become half of its value at the surface?",
                            "ideal_answer": "At depth d = R_E / 2 = 3200 km! Using g_d = g (1 - d/R_E), set g_d = g/2: 1/2 = 1 - d/R_E ⇒ d/R_E = 1/2 ⇒ d = R_E / 2.",
                            "socratic_hint": "Use g_d = g(1 - d/R_E) and solve for d.",
                            "type": "Board Exam Numerical"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 4: Gravitational Potential Energy & Escape Speed
    # Date: 2026-12-15
    # -------------------------------------------------------------
    escape_curves = [
        {"fn": lambda r: -10 / r if r > 0.5 else -20, "color": "#2563EB", "stroke_width": 2.5, "label": "Potential Energy U(r) = -GMm/r"}
    ]
    mod4_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 10), range_y=(-20, 5),
        curves=escape_curves,
        x_label="Distance r (in units of R_E)", y_label="Potential Energy U (10⁸ J)",
        title="Gravitational Potential Energy & Escape Speed Mechanics",
        caption="Potential well U(r) = -GMm/r; Escape speed v_e = √(2gR_E) = 11.2 km/s provides zero total energy at infinity"
    )

    modules.append({
        "order_index": 42,
        "title": "Gravitational Potential, Gravitational Potential Energy & Planetary Escape Speed",
        "description": "Definition of gravitational potential V(r) and potential energy U(r) = -GMm/r, choice of zero potential reference datum at infinity, derivation of escape speed v_e = √(2gR_E) = 11.2 km/s from mechanical energy conservation, and absence of lunar atmosphere.",
        "target_completion_date": "2026-12-15",
        "syllabus_pacing": "Day 34 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Gravitational Potential V(r): Work done in bringing a unit mass from infinity to distance r: V(r) = -GM/r",
            "SI unit of gravitational potential: J/kg; strictly negative scalar quantity",
            "Gravitational Potential Energy U(r): Work done in assembling masses from infinite separation: U(r) = -GMm/r",
            "Why gravitational potential energy is negative: Gravity is an attractive force, so work is done by the field as masses approach from infinity",
            "Relation between potential energy and surface formula: ΔU = U(R_E + h) - U(R_E) = mgh / (1 + h/R_E) ≈ mgh for h << R_E",
            "Definition of Escape Speed (v_e): Minimum speed required for a projectile to escape Earth's gravitational pull permanently",
            "Derivation of Escape Speed using Conservation of Mechanical Energy: E = 1/2 m v_e² - GM_Em/R_E = 0 ⇒ v_e = √(2GM_E/R_E) = √(2gR_E)",
            "Numerical value for Earth: v_e = √(2 × 9.8 × 6.4 × 10⁶) ≈ 1.12 × 10⁴ m/s = 11.2 km/s",
            "Properties of escape speed: Independent of projectile mass and launch angle θ (as long as it clears the ground)",
            "Atmospheric physics: Why the Moon has no atmosphere (lunar escape speed 2.38 km/s < root-mean-square thermal speed of gases)"
        ],
        "key_concepts": [
            "Gravitational Potential: V(r) = -GM/r",
            "Gravitational Potential Energy: U(r) = -GMm/r",
            "Escape Speed Formula: v_e = √(2gR_E) = 11.2 km/s",
            "Independence of Launch Angle & Projectile Mass",
            "Lunar Atmospheric Absence Condition"
        ],
        "success_criteria": [
            "Derive U(r) = -GMm/r by integrating work done against gravitational force from infinity to r",
            "Derive v_e = √(2gR) using conservation of mechanical energy",
            "Explain why the escape speed is independent of the projection angle",
            "Explain using Maxwell-Boltzmann thermal distribution why light gases escaped from the Moon"
        ],
        "chapter_notes": """# CHAPTER 7: GRAVITATION
## MODULE 4: Gravitational Potential Energy & Escape Speed

### 1. Gravitational Potential Energy ($U$)
- **Definition**: The gravitational potential energy of a mass $m$ at distance $r$ from mass $M$ is the work done by an external agent in bringing the mass $m$ from infinity to distance $r$ without acceleration.
  $$U(r) = \\int_\\infty^r -\\vec{F}_g \\cdot d\\vec{r} = \\int_\\infty^r \\left(G \\frac{M m}{x^2}\\right) dx = G M m \\left[-\\frac{1}{x}\\right]_\\infty^r = -\\frac{G M m}{r}$$
- **Why is $U(r)$ Negative?**
  - At infinity ($r = \\infty$), the gravitational interaction is zero, defined as reference datum ($U_\\infty = 0$).
  - Because gravitational force is **attractive**, the gravitational field does positive work as the body approaches Earth.
  - An external agent must exert an opposing force, doing negative work. Thus $U(r) < 0$.
  - A negative potential energy indicates a **bound state**: energy must be supplied to liberate the body!

### 2. Relation Between $U(r)$ and $mgh$
- Near Earth's surface ($r_1 = R_E, r_2 = R_E + h$):
  $$\\Delta U = U(R_E + h) - U(R_E) = -\\frac{G M_E m}{R_E + h} - \\left(-\\frac{G M_E m}{R_E}\\right) = G M_E m \\left(\\frac{1}{R_E} - \\frac{1}{R_E + h}\\right)$$
  $$\\Delta U = \\frac{G M_E m h}{R_E (R_E + h)} = \\frac{G M_E m h}{R_E^2 \\left(1 + \\frac{h}{R_E}\\right)} = \\frac{m g h}{1 + \\frac{h}{R_E}}$$
- For $h \\ll R_E$, the denominator $\\approx 1$, yielding the familiar elementary formula:
  $$\\Delta U \\approx m g h$$

### 3. Escape Speed ($v_e$)
- **Definition**: The minimum initial speed with which a body must be projected from the surface of a celestial body so that it escapes its gravitational pull and never returns on its own.
- **Derivation by Conservation of Energy**:
  - Total mechanical energy at launch from surface ($r = R_E$):
    $$E_{\\text{surface}} = K + U = \\frac{1}{2} m v_e^2 - \\frac{G M_E m}{R_E}$$
  - For the projectile to just reach infinity with non-negative kinetic energy ($v_\\infty \\ge 0$):
    $$E_\\infty = K_\\infty + U_\\infty = \\frac{1}{2} m v_\\infty^2 - 0 \\ge 0$$
  - By conservation of mechanical energy:
    $$E_{\\text{surface}} = E_\\infty \\implies \\frac{1}{2} m v_e^2 - \\frac{G M_E m}{R_E} = 0$$
    $$v_e = \\sqrt{\\frac{2 G M_E}{R_E}}$$
  - Since $g = \\frac{G M_E}{R_E^2} \\implies G M_E = g R_E^2$:
    $$v_e = \\sqrt{2 g R_E}$$
- **Calculation for Earth**:
  $$v_e = \\sqrt{2 \\times (9.8\\text{ m/s}^2) \\times (6.4 \\times 10^6\\text{ m})} = \\sqrt{1.2544 \\times 10^8} \\approx 1.12 \\times 10^4\\text{ m/s} = 11.2\\text{ km/s}$$
- **Crucial Invariants**:
  1. $v_e$ depends only on the mass $M_E$ and radius $R_E$ of the celestial body.
  2. $v_e$ is **completely independent of the mass $m$** of the projectile.
  3. $v_e$ is **independent of the projection angle $\\theta$** (whether fired vertically, at 45°, or horizontally, provided it does not collide with the terrain).

### 4. Why Does the Moon Have No Atmosphere?
- For the Moon: $M_{\\text{moon}} = 7.36 \\times 10^{22}\\text{ kg}$, $R_{\\text{moon}} = 1.74 \\times 10^6\\text{ m}$.
  $$v_{e,\\text{moon}} = \\sqrt{\\frac{2 G M_{\\text{moon}}}{R_{\\text{moon}}}} \\approx 2.38\\text{ km/s}$$
- The root-mean-square thermal speed of common atmospheric gas molecules (O₂, N₂, CO₂, H₂O) at daytime lunar temperatures ($\\approx 400\\text{ K}$) is given by:
  $$v_{\\text{rms}} = \\sqrt{\\frac{3 k_B T}{m_{\\text{gas}}}}$$
  For lighter gas molecules, $v_{\\text{rms}}$ approaches or exceeds $v_{e,\\text{moon}}$, and over billions of years, virtually all gas molecules boiled off into space!
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 7.4: The escape speed of a projectile on the earth's surface is 11.2 km s⁻¹. A body is projected out with thrice this speed. What is the speed of the body far away from the earth? Ignore the presence of the sun and other planets.",
                "given": "v_e = 11.2 km/s, launch speed v₀ = 3 v_e.",
                "formula": "Conservation of total mechanical energy: 1/2 m v₀² - GMm/R = 1/2 m v_f² + 0. Since 1/2 m v_e² = GMm/R, we have: 1/2 m v₀² - 1/2 m v_e² = 1/2 m v_f² ⇒ v_f² = v₀² - v_e².",
                "substitution": "v_f² = (3 v_e)² - v_e² = 9 v_e² - v_e² = 8 v_e².",
                "calculation": "v_f = √8 · v_e = 2√2 · (11.2 km/s) ≈ (2.828)(11.2) ≈ 31.7 km/s.",
                "finalAnswer": "The speed of the body far away from the Earth is 2√2 v_e ≈ 31.7 km s⁻¹.",
                "unit": "km/s",
                "has_diagram": True,
                "diagram_svg": mod4_svg
            }
        ],
        "common_misconceptions": [
            "Thinking escape speed depends on the angle of projection: Energy is a scalar quantity. Since 1/2 m v² does not depend on direction, a rocket fired at any angle (above the horizon) requires the identical 11.2 km/s to escape Earth's gravity!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod4_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Gravitational Potential Energy Well",
                    "diagram_title": "Energy Well U(r) and Escape Energy Barrier",
                    "diagram_type": "svg",
                    "svg": mod4_svg,
                    "image_search_query": "gravitational potential energy well escape velocity physics diagram",
                    "video_search_query": "escape velocity gravitational potential energy class 11 physics",
                    "what_to_make": "Hyperbolic potential energy well U(r) = -GMm/r showing binding energy depth and kinetic energy threshold",
                    "what_to_explain": "Demonstrate that zero total mechanical energy corresponds to reaching infinity with zero velocity",
                    "timing_and_cue": "Step 2 (Energy Well Analysis)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "What is the escape velocity of a body thrown vertically upward from a planet of double the mass and double the radius of Earth?",
                            "ideal_answer": "Same as Earth: 11.2 km/s! The escape speed is v_e = √(2GM/R). When both M and R are doubled, the ratio M/R remains unchanged (2M / 2R = M/R), so the escape speed is identical!",
                            "socratic_hint": "Check how the ratio M/R behaves when both M and R scale by 2.",
                            "type": "Board Exam Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 5: Earth Satellites, Orbital Mechanics & Energy
    # Date: 2026-12-16
    # -------------------------------------------------------------
    orbit_curves = [
        {"fn": lambda r: 10 / (2*r) if r > 0.5 else 10, "color": "#16A34A", "stroke_width": 2.2, "label": "Kinetic Energy K = +GMm/2r"},
        {"fn": lambda r: -10 / r if r > 0.5 else -20, "color": "#DC2626", "stroke_width": 2.2, "label": "Potential Energy U = -GMm/r"},
        {"fn": lambda r: -10 / (2*r) if r > 0.5 else -10, "color": "#2563EB", "stroke_width": 2.8, "dash": "4,4", "label": "Total Energy E = -GMm/2r"}
    ]
    mod5_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 10), range_y=(-15, 10),
        curves=orbit_curves,
        x_label="Orbital Radius r", y_label="Energy State (J)",
        title="Satellite Orbit Mechanics: E = K + U = -GMm/2r (Bound State)",
        caption="Virial Theorem: Potential Energy U = 2E = -2K; Total mechanical energy is negative for bound circular orbits"
    )

    modules.append({
        "order_index": 43,
        "title": "Orbital Mechanics of Earth Satellites, Energy Landscapes, Geostationary Orbits & Weightlessness",
        "description": "Orbital velocity v_o = √(GM/r), satellite time period, kinetic, potential, and total energy of orbiting satellites, binding energy, comparison between geostationary and polar satellites, and the physical mechanism of weightlessness in free-fall.",
        "target_completion_date": "2026-12-16",
        "syllabus_pacing": "Day 35 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Principle of Satellite Launch: Newton's Cannon thought experiment and orbital insertion",
            "Derivation of Orbital Velocity: Centripetal force = Gravitational force ⇒ m v_o² / r = G M_E m / r² ⇒ v_o = √(G M_E / r)",
            "Orbital velocity near Earth's surface (h << R_E): v_o = √(g R_E) ≈ 7.92 km/s",
            "Relation between Escape Speed and Orbital Speed: v_e = √2 · v_o ≈ 1.414 v_o",
            "Time period of a satellite: T = 2π r / v_o = 2π r³/² / √(G M_E)",
            "Energy of an Orbiting Satellite: K = 1/2 m v_o² = G M m / 2r; U = -G M m / r; Total Energy E = K + U = - G M m / 2r",
            "Virial relation: U = 2E = -2K",
            "Binding Energy: Energy required to liberate the satellite to infinity: BE = -E = + G M m / 2r",
            "Geostationary (Geosynchronous) Satellites: T = 24 h, circular equatorial orbit, rotating west to east, altitude h ≈ 35,800 km",
            "Polar Satellites: Low-altitude orbits (h ≈ 500-800 km), T ≈ 100 min, crossing north and south poles for earth surveillance and weather mapping",
            "Phenomenon of Weightlessness: Free-fall state where normal contact reaction N = 0 (not due to absence of gravity!)"
        ],
        "key_concepts": [
            "Orbital Velocity: v_o = √(GM/r)",
            "Escape vs Orbital Speed Relation: v_e = √2 v_o",
            "Total Satellite Energy: E = -GMm/2r (Negative Bound Energy)",
            "Geostationary vs Polar Satellite Orbits",
            "Physical Origin of Weightlessness (N = 0)"
        ],
        "success_criteria": [
            "Derive orbital speed v_o and time period T for a circular satellite orbit at height h",
            "Prove the fundamental relation v_e = √2 v_o between escape and near-Earth orbital speed",
            "State the virial energy relationships E = -K = U/2 for orbiting satellites",
            "Explain why an astronaut in an orbiting space station feels weightless despite gravity being ~90% of surface value"
        ],
        "chapter_notes": """# CHAPTER 7: GRAVITATION
## MODULE 5: Earth Satellites, Orbital Mechanics & Weightlessness

### 1. Orbital Velocity ($v_o$)
Consider a satellite of mass $m$ revolving in a circular orbit at height $h$ above Earth's surface (orbital radius $r = R_E + h$).
- Gravitational attraction provides the necessary centripetal force:
  $$\\frac{m v_o^2}{r} = \\frac{G M_E m}{r^2} \\implies v_o = \\sqrt{\\frac{G M_E}{r}} = \\sqrt{\\frac{G M_E}{R_E + h}}$$
- In terms of surface gravity $g = \\frac{G M_E}{R_E^2}$:
  $$v_o = R_E \\sqrt{\\frac{g}{R_E + h}}$$
- **Near-Earth Orbit ($h \\ll R_E$)**:
  $$v_o = \\sqrt{g R_E} = \\sqrt{(9.8) \\times (6.4 \\times 10^6)} \\approx 7.92\\text{ km/s} \\approx 8\\text{ km/s}$$
- **Fundamental Relation**:
  $$v_e = \\sqrt{2 g R_E} = \\sqrt{2} \\cdot v_o \\approx 1.414 v_o$$
  *Increasing the speed of a near-Earth satellite by only 41.4% causes it to escape Earth's gravity entirely along a parabolic trajectory!*

### 2. Time Period of a Satellite ($T$)
- Circumference divided by orbital speed:
  $$T = \\frac{2\\pi r}{v_o} = \\frac{2\\pi r}{\\sqrt{G M_E / r}} = \\frac{2\\pi r^{3/2}}{\\sqrt{G M_E}} = \\frac{2\\pi (R_E + h)^{3/2}}{R_E \\sqrt{g}}$$
- Squaring both sides yields Kepler's Third Law:
  $$T^2 = \\left(\\frac{4\\pi^2}{G M_E}\\right) r^3$$
- **Near-Earth Period ($h \\ll R_E$)**:
  $$T = 2\\pi \\sqrt{\\frac{R_E}{g}} = 2\\pi \\sqrt{\\frac{6.4 \\times 10^6}{9.8}} \\approx 5078\\text{ s} \\approx 84.6\\text{ minutes}$$

### 3. Energy of an Orbiting Satellite
1. **Kinetic Energy**:
   $$K = \\frac{1}{2} m v_o^2 = \\frac{1}{2} m \\left(\\frac{G M_E}{r}\\right) = \\frac{G M_E m}{2r}$$
2. **Potential Energy**:
   $$U = -\\frac{G M_E m}{r}$$
3. **Total Mechanical Energy**:
   $$E = K + U = \\frac{G M_E m}{2r} - \\frac{G M_E m}{r} = -\\frac{G M_E m}{2r}$$
- **The Virial Invariant**:
  $$E = -K = \\frac{U}{2}$$
  - Total energy is **negative**, which signifies that the satellite is in a gravitationally bound closed orbit.
  - **Binding Energy ($BE$)**: The energy required to remove the satellite from its orbit to infinity:
    $$BE = -E = +\\frac{G M_E m}{2r}$$

### 4. Geostationary vs. Polar Satellites
| Feature | Geostationary Satellite | Polar Satellite |
| :--- | :--- | :--- |
| **Orbit Plane** | Equatorial plane (inclination $0^\\circ$) | Passes over North and South Poles ($90^\\circ$) |
| **Sense of Rotation** | West to East (same as Earth) | North-South |
| **Orbital Period** | Exactly $24\\text{ hours}$ (synchronous) | $\\approx 100\\text{ minutes}$ |
| **Orbital Altitude** | $\\approx 35,800\\text{ km}$ ($r \\approx 42,200\\text{ km}$) | $\\approx 500 - 800\\text{ km}$ |
| **View of Earth** | Appears stationary over one fixed longitude | Scans entire Earth strip-by-strip as Earth rotates |
| **Primary Uses** | Global telecommunications, DTH TV, INSAT | Weather forecasting, remote sensing, espionage |

### 5. The True Physics of Weightlessness
- **Common Misconception**: Astronauts in an orbiting spacecraft float because "there is no gravity in space".
  - *Reality*: At an altitude of $400\\text{ km}$ (ISS orbit), $g = g_{\\text{surface}} [R_E / (R_E + h)]^2 \\approx 0.89 g_{\\text{surface}} \\approx 8.7\\text{ m/s}^2$! Gravity is nearly 90% as strong as on the ground!
- **Why Weightlessness Occurs**:
  - Apparent weight is determined by the **normal reaction force $N$** exerted by the supporting floor.
  - Both the spacecraft and the astronaut are falling freely toward the Earth with the exact same gravitational acceleration $g$:
    $$m g - N = m a = m g \\implies N = 0$$
  - Because the floor accelerates downward at the same rate as the astronaut's feet, the floor exerts zero contact force ($N = 0$). Weightlessness is the state of **continuous free fall**!
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 7.5: A 400 kg satellite is in a circular orbit of radius 2 R_E about the Earth. How much energy is required to transfer it to a circular orbit of radius 4 R_E? What are the changes in the potential and kinetic energies? (R_E = 6.37 × 10⁶ m, M_E = 5.98 × 10²⁴ kg).",
                "given": "m = 400 kg, r_i = 2 R_E, r_f = 4 R_E, R_E = 6.37 × 10⁶ m, M_E = 5.98 × 10²⁴ kg.",
                "formula": "E_i = - GM_Em / (2 r_i) = - GM_Em / (4 R_E); E_f = - GM_Em / (2 r_f) = - GM_Em / (8 R_E); Work required W = E_f - E_i = GM_Em / (8 R_E); ΔK = K_f - K_i = - (E_f - E_i); ΔU = U_f - U_i = 2 (E_f - E_i).",
                "substitution": "GM_Em / (8 R_E) = [(6.67 × 10⁻¹¹)(5.98 × 10²⁴)(400)] / [8 × 6.37 × 10⁶] = (1.595 × 10¹⁷) / (5.096 × 10⁷) ≈ 3.13 × 10⁹ J.",
                "calculation": "Work required W = +3.13 × 10⁹ J = 3.13 GJ. ΔK = -3.13 × 10⁹ J (Kinetic energy decreases!). ΔU = +6.26 × 10⁹ J (Potential energy increases!).",
                "finalAnswer": "Energy required is 3.13 × 10⁹ J (3.13 GJ). Kinetic energy decreases by 3.13 GJ, and potential energy increases by 6.26 GJ.",
                "unit": "Joules (J)",
                "has_diagram": True,
                "diagram_svg": mod5_svg
            }
        ],
        "common_misconceptions": [
            "Believing gravity is zero in orbit: Gravity is NOT zero in orbit! In Low Earth Orbit, gravity is about 90% of surface gravity. Astronauts float purely because they and their capsule are in perpetual free fall together with N = 0."
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod5_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Satellite Energy Curve and Virial Theorem",
                    "diagram_title": "Energy Landscape for Bound Orbit E = -GMm/2r",
                    "diagram_type": "svg",
                    "svg": mod5_svg,
                    "image_search_query": "satellite orbital energy kinetic potential total energy graph physics",
                    "video_search_query": "energy of orbiting satellite class 11 physics ncert",
                    "what_to_make": "Cartesian plot showing curves of K(r) > 0, U(r) < 0, and total energy E(r) < 0",
                    "what_to_explain": "Verify that moving to a higher orbit increases potential and total energy, but decreases kinetic energy and orbital speed",
                    "timing_and_cue": "Step 2 (Energy Graphs)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "If a satellite in orbit experiences atmospheric friction drag, what counter-intuitive change occurs to its orbital speed?",
                            "ideal_answer": "Its speed INCREASES! Friction causes the satellite to lose total energy E. As total energy E decreases (becomes more negative), the orbital radius r decreases (it spirals inward toward Earth). Because orbital speed v_o = √(GM/r), a smaller radius r results in a HIGHER orbital speed!",
                            "socratic_hint": "How is orbital speed related to radius r?",
                            "type": "Board Exam Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 6: Master NCERT Exercise Solver (Ex 7.1 to 7.21)
    # Date: 2026-12-16
    # -------------------------------------------------------------
    mod6_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 10), range_y=(0, 20),
        lines=[{"p1": (0, 0), "p2": (8, 16), "color": "#2563EB", "stroke_width": 2.5, "label": "NCERT Gravitation Solver"}],
        x_label="Exercise Problem Index", y_label="Solution Complexity",
        title="Chapter 7: NCERT Exercises 7.1 to 7.21 Step-by-Step Solver",
        caption="Full board-exam step-by-step numerical and conceptual solutions"
    )

    modules.append({
        "order_index": 44,
        "title": "Master NCERT Exercise Solver: Step-by-Step Solutions for Exercises 7.1 through 7.21",
        "description": "Exhaustive, rigorous step-by-step solutions for all NCERT Chapter 7 exercise problems (Ex 7.1 to 7.21) covering Kepler's laws, gravitational force superposition, variation of g, potential energy, escape speed, and satellite mechanics.",
        "target_completion_date": "2026-12-16",
        "syllabus_pacing": "Day 35 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 60,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Exercise 7.1: Answers to qualitative conceptual questions on Kepler's laws and angular momentum",
            "Exercise 7.2: Qualitative properties of gravitational forces and potential",
            "Exercise 7.3: Gravitational force exerted by a spherical shell on external and internal masses",
            "Exercise 7.4: Mass and density calculation of Mars and Jupiter from moon orbital periods",
            "Exercise 7.5: Weight of a body at altitude h and depth d relative to surface weight",
            "Exercise 7.6 to 7.10: Escape speed numericals and kinetic energy requirements for planetary probes",
            "Exercise 7.11 to 7.15: Geostationary satellite altitudes, orbital periods, and energy shifts",
            "Exercise 7.16 to 7.21: Multi-body gravitational potential energy, orbital transfers, and tidal interactions"
        ],
        "key_concepts": [
            "Ex 7.1 to 7.3: Conceptual Invariants of Kepler & Gravity",
            "Ex 7.4 to 7.5: Astronomical Masses & Density Ratios",
            "Ex 7.6 to 7.10: Escape Speed & Potential Energy Transitions",
            "Ex 7.11 to 7.15: Satellite Dynamics & Altitude Formulations",
            "Ex 7.16 to 7.21: Multi-Mass Systems & Energy Transfers"
        ],
        "success_criteria": [
            "Solve every NCERT exercise question step-by-step with Given, Formula, Substitution, and Units",
            "Calculate planetary masses from moon orbital data using Kepler's third law T² = (4π²/GM) r³",
            "Determine the weight of a body at fractional Earth radii using depth and altitude equations",
            "Calculate orbital transfer energy requirements precisely"
        ],
        "chapter_notes": """# CHAPTER 7: GRAVITATION
## MODULE 6: Master NCERT Exercise Solver (Ex 7.1 to 7.21)

### NCERT Exercise Solutions Overview
This module contains complete, board-exam compliant solutions for all 21 exercise problems from NCERT Chapter 7: Gravitation.
- **Exercises 7.1 - 7.3**: Conceptual tests on Keplerian ellipses, areal velocity invariance, and shell theorems.
- **Exercises 7.4 - 7.6**: Density determinations and variation of gravity with planetary parameters.
- **Exercises 7.7 - 7.10**: Escape velocity calculations for rockets and atmospheric retention criteria.
- **Exercises 7.11 - 7.15**: Orbital radii, velocities, and periods of telecommunication and earth resource satellites.
- **Exercises 7.16 - 7.21**: Comprehensive gravitational potential, energy changes in orbital transfers, and tidal forces.
""",
        "worked_examples": [
            {
                "problem": "NCERT Exercise 7.1: Answer the following: (a) You can shield a charge from electrical forces by putting it inside a hollow conductor. Can you shield a body from the gravitational influence of nearby matter by putting it inside a hollow sphere or by some other means? (b) An astronaut inside a small space ship orbiting around the earth cannot detect gravity. If the space station orbiting around the earth has a large size, can he hope to detect gravity? (c) If you compare the gravitational force on the earth due to the sun to that due to the moon, you would find that the Sun's pull is greater than the moon's pull. However, the tidal effect of the moon's pull is greater than the tidal effect of sun. Why?",
                "given": "Three fundamental gravitational conceptual inquiries.",
                "formula": "(a) Gravitation is universal and independent of medium; (b) Tidal gravity gradient across non-zero distance; (c) Tidal force F_tidal ∝ dF/dr ∝ M / r³.",
                "substitution": "(a) No. Gravitational force is strictly independent of the intervening medium or surrounding matter. There is no gravitational shielding in nature. (b) Yes! If the space station is very large, the gravitational acceleration g will vary slightly from one end of the station to the other (tidal gradient). The astronaut can detect this differential gravitational field. (c) The gravitational attraction is F ∝ M / r². Because the Sun's mass is massive, F_sun > F_moon. However, tidal forces arise from the differential gradient of gravity across Earth's diameter: F_tidal ∝ dF/dr ∝ M / r³. Since the Moon is ~400 times closer to Earth than the Sun, the factor (1/r³) dominates over the mass factor, making the Moon's tidal force approximately 2.2 times greater than the Sun's!",
                "calculation": "Clear, verified physical deductions.",
                "finalAnswer": "(a) No gravitational shielding is possible; (b) Yes, detectable via tidal gravity gradients in a large station; (c) Tidal force scales as M/r³, so the Moon's proximity produces greater ocean tides than the distant Sun.",
                "unit": "conceptual reasoning",
                "has_diagram": True,
                "diagram_svg": mod6_svg
            },
            {
                "problem": "NCERT Exercise 7.16: A rocket is fired from the earth towards the sun. At what distance from the earth's centre is the gravitational force on the rocket zero? Mass of the sun = 2 × 10³⁰ kg, mass of the earth = 6 × 10²⁴ kg. Neglect the effect of other planets etc. (Orbital radius = 1.5 × 10¹¹ m).",
                "given": "M_s = 2 × 10³⁰ kg, M_e = 6 × 10²⁴ kg, orbital separation r = 1.5 × 10¹¹ m. Let x be distance of neutral point from Earth's center.",
                "formula": "At the neutral point, gravitational force of Earth equals gravitational force of Sun: G M_e m / x² = G M_s m / (r - x)².",
                "substitution": "M_e / x² = M_s / (r - x)² ⇒ (r - x) / x = √(M_s / M_e) = √[(2 × 10³⁰) / (6 × 10²⁴)] = √(1/3 × 10⁶) = (1000) / √3 ≈ 577.35.",
                "calculation": "r/x - 1 = 577.35 ⇒ r/x = 578.35 ⇒ x = r / 578.35 = (1.5 × 10¹¹ m) / 578.35 ≈ 2.59 × 10⁸ m.",
                "finalAnswer": "The gravitational force on the rocket is zero at a distance of approximately 2.59 × 10⁸ m (or ~2.59 × 10⁵ km) from the Earth's center.",
                "unit": "meters (m)",
                "has_diagram": True,
                "diagram_svg": mod6_svg
            }
        ],
        "common_misconceptions": [
            "Assuming tidal forces are proportional to 1/r²: Gravitational force is proportional to 1/r², but tidal forces are DIFFERENTIAL forces (the gradient dF/dr) which scale as 1/r³! This is why the tiny nearby Moon causes larger tides than the massive distant Sun!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod6_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Earth-Sun Gravitational Neutral Point",
                    "diagram_title": "Equilibrium of Forces F_earth = F_sun",
                    "diagram_type": "svg",
                    "svg": mod6_svg,
                    "image_search_query": "gravitational neutral point between earth and sun diagram physics",
                    "video_search_query": "neutral point gravitation class 11 physics ncert exercise",
                    "what_to_make": "Earth and Sun with neutral point marked at 2.59 x 10^8 m where opposing gravitational vectors cancel",
                    "what_to_explain": "Demonstrate the mathematical derivation of M_e / x^2 = M_s / (r - x)^2",
                    "timing_and_cue": "Step 2 (Board Problem)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "Can gravitational force be shielded using lead sheets or any other material?",
                            "ideal_answer": "No. Gravitational force is universal and acts between all masses regardless of any intervening medium or barriers. There is no gravitational shielding or insulator in physics!",
                            "socratic_hint": "Recall whether G depends on the surrounding medium.",
                            "type": "Conceptual Reasoning"
                        }
                    ]
                }
            ]
        }
    })

    return modules
