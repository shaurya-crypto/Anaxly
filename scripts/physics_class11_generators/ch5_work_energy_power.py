"""
ch5_work_energy_power.py
CBSE Class 11 Physics - Chapter 5: Work, Energy and Power
Part 1 (Mid-Term Syllabus, Unit IV: Work, Energy and Power)
Target Pacing: December 03, 2026 to December 07, 2026 (6 Modules, 5 Days)
"""

import sys
import os
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

import svg_builder_physics11 as sb

CURRICULUM_ID = "c11_phy_ch05_work_energy_power"
CLASS_LEVEL = "Class 11"
BOARD = "CBSE"
SUBJECT = "Physics"

def get_modules():
    modules = []

    # -------------------------------------------------------------
    # MODULE 1: Scalar Product of Vectors & Work Done by Constant & Variable Forces
    # Date: 2026-12-03
    # -------------------------------------------------------------
    # SVG: Work as area under F-x curve
    f_x_polygon = [
        {"points": [(0, 0), (2, 0), (2, 10), (0, 0)], "fill": "rgba(37, 99, 235, 0.2)", "stroke": "#2563EB", "label": "Area 1 (Triangle)"},
        {"points": [(2, 0), (6, 0), (6, 10), (2, 10)], "fill": "rgba(22, 163, 74, 0.2)", "stroke": "#16A34A", "label": "Area 2 (Rectangle)"},
        {"points": [(6, 0), (8, 0), (6, 10)], "fill": "rgba(220, 38, 38, 0.2)", "stroke": "#DC2626", "label": "Area 3 (Triangle)"}
    ]
    f_x_lines = [
        {"p1": (0, 0), "p2": (2, 10), "color": "#2563EB", "stroke_width": 2.5},
        {"p1": (2, 10), "p2": (6, 10), "color": "#16A34A", "stroke_width": 2.5},
        {"p1": (6, 10), "p2": (8, 0), "color": "#DC2626", "stroke_width": 2.5}
    ]
    mod1_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 10), range_y=(0, 15),
        polygons=f_x_polygon, lines=f_x_lines,
        x_label="Displacement x (m)", y_label="Force F(x) (N)",
        title="Work Done by a Variable Force: W = ∫ F(x) dx",
        caption="Total work is equal to the algebraic area bounded by the F-x curve and displacement axis"
    )

    modules.append({
        "order_index": 26,
        "title": "Scalar Product of Vectors & Mechanics of Work Done by Constant and Variable Forces",
        "description": "Mathematical definition and properties of scalar (dot) product, physical definition of work W = F⃗ · d⃗ = F d cos θ, positive, negative, and zero work scenarios, and graphical computation of work under variable force curves W = ∫ F dx.",
        "target_completion_date": "2026-12-03",
        "syllabus_pacing": "Day 22 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Definition of scalar (dot) product: A⃗ · B⃗ = A B cos θ with geometrical interpretation",
            "Properties of scalar product: Commutative, distributive, orthogonal unit vectors (î·î = 1, î·ĵ = 0)",
            "Definition of Work in physics: W = F⃗ · d⃗ = F d cos θ with SI unit Joule (J) and dimensions [M L² T⁻²]",
            "Sign convention of work: Positive work (0 ≤ θ < 90°), Negative work (90° < θ ≤ 180°), Zero work (θ = 90° or d = 0)",
            "Zero work examples: Centripetal force in circular motion, coolie carrying luggage horizontally against gravity",
            "Work done by a variable force: Mathematical summation W = lim(Δx→0) Σ F(x)Δx = ∫ F(x) dx",
            "Area under Force-Displacement graph equals work done (incorporating positive and negative areas)"
        ],
        "key_concepts": [
            "Scalar (Dot) Product Properties",
            "Physical Definition of Work: W = F⃗ · d⃗ = F d cos θ",
            "Work Done by Variable Force: Area Under F-x Curve",
            "Conditions for Positive, Negative, and Zero Work"
        ],
        "success_criteria": [
            "Calculate dot product of two vectors in component form: A⃗ · B⃗ = A_x B_x + A_y B_y + A_z B_z",
            "Evaluate work done by pulling, pushing, gravity, and friction forces with proper signs",
            "Prove that centripetal force does zero work on an object undergoing uniform circular motion",
            "Determine work done by integrating variable force functions or calculating geometric areas under F-x plots"
        ],
        "chapter_notes": """# CHAPTER 5: WORK, ENERGY AND POWER
## MODULE 1: Scalar Product & Work Done by Constant and Variable Forces

### 1. The Scalar (Dot) Product of Two Vectors
- **Definition**: The scalar product of two vectors $\\vec{A}$ and $\\vec{B}$, denoted by $\\vec{A} \\cdot \\vec{B}$, is defined as the scalar quantity:
  $$\\vec{A} \\cdot \\vec{B} = A B \\cos \\theta$$
  where $A = |\\vec{A}|$, $B = |\\vec{B}|$, and $\\theta$ is the angle between $\\vec{A}$ and $\\vec{B}$ ($0 \\le \\theta \\le \\pi$).
- **Properties**:
  1. **Commutative**: $\\vec{A} \\cdot \\vec{B} = \\vec{B} \\cdot \\vec{A}$.
  2. **Distributive**: $\\vec{A} \\cdot (\\vec{B} + \\vec{C}) = \\vec{A} \\cdot \\vec{B} + \\vec{A} \\cdot \\vec{C}$.
  3. **Orthogonal unit vectors**:
     $$\\hat{i} \\cdot \\hat{i} = \\hat{j} \\cdot \\hat{j} = \\hat{k} \\cdot \\hat{k} = 1$$
     $$\\hat{i} \\cdot \\hat{j} = \\hat{j} \\cdot \\hat{k} = \\hat{k} \\cdot \\hat{i} = 0$$
  4. **Component form**: If $\\vec{A} = A_x \\hat{i} + A_y \\hat{j} + A_z \\hat{k}$ and $\\vec{B} = B_x \\hat{i} + B_y \\hat{j} + B_z \\hat{k}$:
     $$\\vec{A} \\cdot \\vec{B} = A_x B_x + A_y B_y + A_z B_z$$
  5. **Angle between two vectors**:
     $$\\cos \\theta = \\frac{\\vec{A} \\cdot \\vec{B}}{|\\vec{A}| |\\vec{B}|} = \\frac{A_x B_x + A_y B_y + A_z B_z}{\\sqrt{A_x^2 + A_y^2 + A_z^2} \\sqrt{B_x^2 + B_y^2 + B_z^2}}$$

### 2. Definition & Classification of Work
- **Definition**: Work is said to be done by a force when the point of application of the force undergoes a displacement along or opposite to the line of action of the force.
  $$W = \\vec{F} \\cdot \\vec{d} = F d \\cos \\theta$$
  - **SI Unit**: Joule (J), where $1\\text{ J} = 1\\text{ N}\\cdot\\text{m} = 1\\text{ kg}\\cdot\\text{m}^2\\text{s}^{-2}$.
  - **Dimensions**: $[M L^2 T^{-2}]$.
- **Classification of Work**:
  1. **Positive Work** ($0 \\le \\theta < 90^\\circ$): $\\cos\\theta > 0$. Example: Work done by gravitational force on a freely falling body.
  2. **Negative Work** ($90^\\circ < \\theta \\le 180^\\circ$): $\\cos\\theta < 0$. Example: Work done by friction force on a sliding block ($W = f_k d \\cos 180^\\circ = -f_k d$).
  3. **Zero Work**:
     - When displacement $d = 0$ (e.g. pushing a rigid wall).
     - When force $F = 0$ (e.g. motion in deep space).
     - When $\\theta = 90^\\circ$ ($\\vec{F} \\perp \\vec{d}$): Examples: Centripetal force in circular orbit ($W = \\int \\vec{F}_c \\cdot d\\vec{r} = 0$), coolie carrying a load horizontally on his head against vertical gravity ($W_g = mg d \\cos 90^\\circ = 0$).

### 3. Work Done by a Variable Force
- When force varies with position $F = F(x)$, we divide the displacement into infinitesimal intervals $\\Delta x$:
  $$W = \\lim_{\\Delta x \\to 0} \\sum_{x_i}^{x_f} F(x) \\Delta x = \\int_{x_i}^{x_f} F(x) dx$$
- In 3 dimensions:
  $$W = \\int_{\\vec{r}_i}^{\\vec{r}_f} \\vec{F} \\cdot d\\vec{r} = \\int_{x_i}^{x_f} F_x dx + \\int_{y_i}^{y_f} F_y dy + \\int_{z_i}^{z_f} F_z dz$$
- **Graphical Rule**: The work done by a variable force is geometrically equal to the **area under the $F-x$ curve** bounded by the displacement axis. Areas above the x-axis represent positive work; areas below represent negative work.
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 5.1: Find the angle between force F⃗ = (3î + 4ĵ - 5k̂) unit and displacement d⃗ = (5î + 4ĵ + 3k̂) unit. Also find the projection of F⃗ on d⃗.",
                "given": "F⃗ = 3î + 4ĵ - 5k̂, d⃗ = 5î + 4ĵ + 3k̂.",
                "formula": "F⃗ · d⃗ = F_x d_x + F_y d_y + F_z d_z; cos θ = (F⃗ · d⃗) / (|F⃗| |d⃗|); Projection = F⃗ · d̂ = (F⃗ · d⃗) / |d⃗|.",
                "substitution": "F⃗ · d⃗ = (3)(5) + (4)(4) + (-5)(3) = 15 + 16 - 15 = 16 units. |F⃗| = √(3² + 4² + (-5)²) = √(9 + 16 + 25) = √50 = 5√2. |d⃗| = √(5² + 4² + 3²) = √50 = 5√2.",
                "calculation": "cos θ = 16 / (√50 · √50) = 16 / 50 = 0.32. θ = cos⁻¹(0.32) ≈ 71.3°. Projection of F⃗ on d⃗ = 16 / √50 = 16 / (5√2) = 16√2 / 10 = 2.26 units.",
                "finalAnswer": "The angle between the vectors is cos⁻¹(0.32) ≈ 71.3°, and the projection of F⃗ on d⃗ is 16/√50 ≈ 2.26 units.",
                "unit": "degrees and units",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            },
            {
                "problem": "Textbook Example 5.2: It is well known that a raindrop falls under the influence of the downward gravitational force and the opposing resistive force of the air. The latter is known to be proportional to the speed of the drop but is otherwise undetermined. Consider a drop of mass 1.00 g falling from a height 1.00 km. It hits the ground with a speed of 50.0 m s⁻¹. (a) What is the work done by the gravitational force? (b) What is the work done by the unknown resistive force?",
                "given": "m = 1.00 g = 10⁻³ kg, h = 1.00 km = 1000 m, v_i = 0, v_f = 50.0 m/s, g = 9.8 m/s².",
                "formula": "(a) W_g = mgh; (b) ΔK = 1/2 m v_f² - 1/2 m v_i²; By Work-Energy Theorem: W_net = W_g + W_r = ΔK ⇒ W_r = ΔK - W_g.",
                "substitution": "(a) W_g = (10⁻³ kg)(9.8 m/s²)(1000 m) = 9.8 J. (b) ΔK = 1/2 (10⁻³ kg)(50.0 m/s)² = 0.5 × 10⁻³ × 2500 = 1.25 J.",
                "calculation": "W_r = ΔK - W_g = 1.25 J - 9.80 J = -8.55 J.",
                "finalAnswer": "(a) Work done by gravity is +9.80 J. (b) Work done by the air resistive force is -8.55 J.",
                "unit": "Joules (J)",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            },
            {
                "problem": "Textbook Example 5.3: A cyclist comes to a skidding stop in 10 m. During this process, the force on the cycle due to the road is 200 N and is directly opposed to the motion. (a) How much work does the road do on the cycle? (b) How much work does the cycle do on the road?",
                "given": "F_road = 200 N opposite to motion, d = 10 m.",
                "formula": "W = F d cos θ.",
                "substitution": "(a) For the road on the cycle: θ = 180°. W_road = (200 N)(10 m) cos 180° = -2000 J. (b) For the cycle on the road: By Newton's third law, the cycle exerts an equal and opposite force of 200 N on the road in the direction of motion. However, the road does not undergo any displacement (d_road = 0).",
                "calculation": "(a) W_road = -2000 J = -2 kJ. (b) W_cycle = (200 N)(0 m) = 0 J.",
                "finalAnswer": "(a) The road does -2000 J of work on the cycle (dissipating its kinetic energy into heat). (b) The cycle does zero work on the road because the road is stationary.",
                "unit": "Joules (J)",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            }
        ],
        "common_misconceptions": [
            "Confusing Newton's third law action-reaction pairs with work reciprocity: While the cycle exerts +200 N on the road, the road has zero displacement, so the work done by the cycle on the road is strictly zero, not +2000 J!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod1_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Scalar Product and Geometric Projection",
                    "diagram_title": "Projection of Vector A on Vector B",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "scalar product dot product projection physics diagram",
                    "video_search_query": "dot product scalar product physics class 11 ncert",
                    "what_to_make": "Vector A projected onto vector B showing A cos theta component along B",
                    "what_to_explain": "Demonstrate that dot product is a scalar representing the product of one vector and the component of the second vector along the first",
                    "timing_and_cue": "Step 1 (Definition)"
                },
                {
                    "concept_index": 1,
                    "concept_title": "Work Done as Area Under F-x Curve",
                    "diagram_title": "Area Integration for Variable Force",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "work done variable force area under curve physics graph",
                    "video_search_query": "work done by variable force class 11 physics calculus",
                    "what_to_make": "Cartesian plot showing segmented strips Δx under F(x) summing to the definite integral",
                    "what_to_explain": "Establish that definite integral ∫ F dx is identically equal to the geometric shaded area",
                    "timing_and_cue": "Step 2 (Calculus Formulation)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "A satellite moves in a circular orbit around the Earth. What is the work done by the gravitational force on the satellite in one complete revolution?",
                            "ideal_answer": "Zero. The gravitational force acts radially inward toward the Earth's center, perpendicular to the instantaneous tangential displacement of the satellite at every point along the circular orbit (θ = 90°). Thus dW = F_g · dr = F_g dr cos 90° = 0 at every instant!",
                            "socratic_hint": "What is the angle between the radial gravitational force and the tangential velocity vector?",
                            "type": "Conceptual Reasoning"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 2: Kinetic Energy & The Work-Energy Theorem
    # Date: 2026-12-04
    # -------------------------------------------------------------
    ke_lines = [
        {"p1": (0, 0), "p2": (8, 16), "color": "#2563EB", "stroke_width": 2.5, "label": "v² vs x (Slope = 2a)"}
    ]
    mod2_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 10), range_y=(0, 20),
        lines=ke_lines,
        x_label="Displacement x (m)", y_label="Squared Velocity v² (m²/s²)",
        title="Work-Energy Theorem: ΔK = ∫ F dx = ½ m v_f² - ½ m v_i²",
        caption="Direct mathematical relationship between network done and change in kinetic energy"
    )

    modules.append({
        "order_index": 27,
        "title": "Kinetic Energy Formulation & The Work-Energy Theorem for Constant and Variable Forces",
        "description": "Definition of kinetic energy K = 1/2 m v², rigorous calculus derivation of the Work-Energy Theorem for constant and variable forces, equivalence between net work and change in kinetic energy, and stopping distance mechanics.",
        "target_completion_date": "2026-12-04",
        "syllabus_pacing": "Day 23 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Kinetic Energy definition: Energy possessed by a body by virtue of its motion K = 1/2 m v²",
            "Units and scalar nature of kinetic energy (strictly non-negative K ≥ 0)",
            "Derivation of Work-Energy Theorem for constant force: v² = u² + 2as ⇒ W = F s = 1/2 m v² - 1/2 m u²",
            "Calculus derivation of Work-Energy Theorem for variable force: W = ∫ F dx = ∫ m (v dv/dx) dx = ∫ m v dv = ΔK",
            "Significance of the Work-Energy Theorem: Works in both 1D and 3D vector spaces",
            "Stopping distance and stopping time formulations derived from the Work-Energy Theorem",
            "Work done by multiple forces: W_net = W_gravity + W_normal + W_friction + W_applied = ΔK"
        ],
        "key_concepts": [
            "Kinetic Energy Formulation: K = ½ m v²",
            "Work-Energy Theorem for Constant Force",
            "Work-Energy Theorem for Variable Force (Calculus Proof)",
            "Net Work as Algebraic Sum of Work by All External Forces"
        ],
        "success_criteria": [
            "State the Work-Energy Theorem clearly and write its general vector form W_net = ΔK",
            "Derive W = ∫ m v dv = 1/2 m v_f² - 1/2 m v_i² using chain rule v = dx/dt and a = v dv/dx",
            "Apply the theorem to calculate final velocities or resistive forces in braking and penetration problems",
            "Distinguish between work done by individual forces and the net work done by the resultant force"
        ],
        "chapter_notes": """# CHAPTER 5: WORK, ENERGY AND POWER
## MODULE 2: Kinetic Energy & The Work-Energy Theorem

### 1. Kinetic Energy
- **Definition**: The kinetic energy of an object is a measure of the work an object can do by virtue of its motion.
  $$K = \\frac{1}{2} m v^2 = \\frac{1}{2} m (\\vec{v} \\cdot \\vec{v})$$
  - Since mass $m > 0$ and $v^2 \\ge 0$, kinetic energy is **always a non-negative scalar quantity** ($K \\ge 0$).
  - **Relation with Linear Momentum $p = mv$**:
    $$K = \\frac{p^2}{2m} \\implies p = \\sqrt{2mK}$$

### 2. The Work-Energy Theorem for a Constant Force
- From the third equation of kinematics for rectilinear motion with constant acceleration $a$:
  $$v^2 - u^2 = 2 a s \\implies a s = \\frac{v^2 - u^2}{2}$$
- Multiplying both sides by mass $m$:
  $$m a s = \\frac{1}{2} m v^2 - \\frac{1}{2} m u^2$$
- Since $F = ma$ and $W = F s$:
  $$W = K_f - K_i = \\Delta K$$
- **Statement**: *The work done by the net force acting on a body is equal to the change in its kinetic energy.*

### 3. Proof of the Work-Energy Theorem for a Variable Force (Calculus Method)
- The instantaneous kinetic energy is $K = \\frac{1}{2} m v^2$.
- Differentiating $K$ with respect to time $t$:
  $$\\frac{dK}{dt} = \\frac{d}{dt}\\left(\\frac{1}{2} m v^2\\right) = \\frac{1}{2} m \\left(2 v \\frac{dv}{dt}\\right) = m \\frac{dv}{dt} v$$
- By Newton's second law, $F = m \\frac{dv}{dt} = ma$:
  $$\\frac{dK}{dt} = F v = F \\frac{dx}{dt}$$
- Multiplying both sides by $dt$:
  $$dK = F dx$$
- Integrating both sides from initial state $(x_i, K_i)$ to final state $(x_f, K_f)$:
  $$\\int_{K_i}^{K_f} dK = \\int_{x_i}^{x_f} F dx$$
  $$K_f - K_i = \\int_{x_i}^{x_f} F dx = W$$
  $$\\therefore W_{\\text{net}} = \\Delta K$$
- **Crucial Rule**: The work-energy theorem holds for **all forces** acting on the particle — conservative, non-conservative, internal, and external!
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 5.4: A block of mass m = 1 kg, moving on a horizontal surface with speed v_i = 2 m s⁻¹ enters a rough patch ranging from x = 0.10 m to x = 2.01 m. The retarding force F_r on the block in this range is inversely proportional to x over this range: F_r = -k / x for 0.1 < x < 2.01 m, where k = 0.5 J. What is the final kinetic energy and speed v_f of the block as it crosses this patch?",
                "given": "m = 1 kg, v_i = 2 m/s, x_i = 0.1 m, x_f = 2.01 m, F_r = -k/x with k = 0.5 J.",
                "formula": "Work-Energy Theorem: K_f = K_i + W = 1/2 m v_i² + ∫_{x_i}^{x_f} F_r dx.",
                "substitution": "K_i = 1/2 (1)(2)² = 2 J. W = ∫_{0.1}^{2.01} (-k/x) dx = -k [ln x]_{0.1}^{2.01} = -0.5 [ln(2.01) - ln(0.1)] = -0.5 ln(2.01 / 0.1) = -0.5 ln(20.1). Since ln(20.1) ≈ 3.00, W = -0.5 × 3.00 = -1.5 J.",
                "calculation": "K_f = 2.0 J - 1.5 J = 0.5 J. Since K_f = 1/2 m v_f²: 0.5 = 1/2 (1) v_f² ⇒ v_f² = 1.0 m²/s² ⇒ v_f = 1.0 m/s.",
                "finalAnswer": "The final kinetic energy of the block is 0.5 J and its speed is 1.0 m s⁻¹.",
                "unit": "J and m/s",
                "has_diagram": True,
                "diagram_svg": mod2_svg
            },
            {
                "problem": "Textbook Example 5.5: A bullet of mass 0.012 kg and horizontal speed 70 m s⁻¹ strikes a block of wood of mass 0.4 kg and instantly comes to rest with respect to the block. The block is suspended from the ceiling by thin wire. Calculate the height to which the block rises. Also, estimate the amount of heat produced in the block.",
                "given": "m_1 = 0.012 kg, u_1 = 70 m/s, M = 0.4 kg, u_2 = 0.",
                "formula": "Conservation of linear momentum: m_1 u_1 = (m_1 + M) V; Energy conservation during swing: 1/2 (m_1 + M) V² = (m_1 + M) g h ⇒ h = V² / (2g); Heat produced = Initial KE - Final KE.",
                "substitution": "V = (0.012 × 70) / (0.012 + 0.4) = 0.84 / 0.412 ≈ 2.04 m/s. h = (2.04)² / (2 × 9.8) = 4.16 / 19.6 ≈ 0.212 m = 21.2 cm. Initial KE = 1/2 (0.012)(70)² = 0.006 × 4900 = 29.4 J. KE after impact = 1/2 (0.412)(2.04)² ≈ 0.86 J.",
                "calculation": "Heat produced ΔQ = 29.4 J - 0.86 J = 28.54 J.",
                "finalAnswer": "The block rises to a height of 21.2 cm, and approximately 28.5 J of mechanical energy is dissipated as heat.",
                "unit": "m and J",
                "has_diagram": True,
                "diagram_svg": mod2_svg
            }
        ],
        "common_misconceptions": [
            "Assuming kinetic energy can be negative: Since kinetic energy depends on speed squared v², K is strictly non-negative. However, the *change* in kinetic energy ΔK can be negative if the object slows down."
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod2_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Work-Energy Theorem Integration",
                    "diagram_title": "Derivation of ΔK = ∫ F dx",
                    "diagram_type": "svg",
                    "svg": mod2_svg,
                    "image_search_query": "work energy theorem calculus derivation physics diagram",
                    "video_search_query": "work energy theorem proof class 11 physics ncert",
                    "what_to_make": "Differential element showing dK/dt = F v and integration steps",
                    "what_to_explain": "Highlight how Newton's second law F = ma is integrated over spatial displacement dx to yield work and energy",
                    "timing_and_cue": "Step 2 (Calculus Derivation)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "If the linear momentum of a body is increased by 50%, what is the percentage increase in its kinetic energy?",
                            "ideal_answer": "Let initial momentum be p, initial KE be K = p² / (2m). New momentum p' = 1.5p. New KE K' = (1.5p)² / (2m) = 2.25 [p² / (2m)] = 2.25 K. Percentage increase = [(K' - K)/K] × 100% = (2.25 - 1) × 100% = 125%!",
                            "socratic_hint": "Express kinetic energy as K = p² / 2m and substitute p' = 1.5 p.",
                            "type": "Board Exam Numerical"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 3: Potential Energy, Conservative Forces & Spring Systems
    # Date: 2026-12-05
    # -------------------------------------------------------------
    mod3_svg = sb.build_spring_potential_energy_svg(
        title="Spring-Mass System: Potential Energy U(x) = ½ k x²",
        caption="Parabolic potential well with total mechanical energy conservation E = K + U = constant"
    )

    modules.append({
        "order_index": 28,
        "title": "Potential Energy, Conservative Forces & The Mechanics of Elastic Spring Systems",
        "description": "Concept of potential energy as configuration energy, conservative versus non-conservative forces, mathematical relation F = -dU/dx, conservation of total mechanical energy, and Hooke's law spring potential energy U = 1/2 k x².",
        "target_completion_date": "2026-12-05",
        "syllabus_pacing": "Day 24 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Concept of Potential Energy: Energy stored by virtue of position or configuration",
            "Conservative forces: Definition (work done is path independent and vanishes around a closed loop ∮ F⃗ · dr⃗ = 0)",
            "Non-conservative forces: Friction, viscous drag (work converted into thermal/dissipative energy)",
            "Mathematical formulation: F(x) = -dU/dx (force is negative gradient of potential energy)",
            "Stable, unstable, and neutral equilibrium conditions based on dU/dx = 0 and d²U/dx²",
            "Gravitational potential energy near Earth's surface U(h) = mgh",
            "Hooke's Law for ideal springs: F_s = -kx with spring constant k (N/m)",
            "Derivation of spring potential energy: U(x) = ∫₀ˣ kx dx = 1/2 k x²",
            "Conservation of total mechanical energy in spring oscillations: E = 1/2 m v² + 1/2 k x² = constant"
        ],
        "key_concepts": [
            "Conservative vs Non-Conservative Forces",
            "Force-Potential Energy Relation: F = -dU/dx",
            "Hooke's Law & Elastic Spring Potential Energy: U = ½ k x²",
            "Law of Conservation of Total Mechanical Energy"
        ],
        "success_criteria": [
            "Define conservative force and state the two equivalent criteria (path independence and zero work in closed loop)",
            "Derive F = -dU/dx from the definition of potential energy difference ΔU = -W_c",
            "Derive the formula for elastic potential energy of an extended or compressed spring U = 1/2 k x²",
            "Identify points of stable equilibrium (U is minimum, d²U/dx² > 0) on potential energy curves"
        ],
        "chapter_notes": """# CHAPTER 5: WORK, ENERGY AND POWER
## MODULE 3: Potential Energy & Spring-Mass Systems

### 1. Potential Energy & Conservative Forces
- **Potential Energy ($U$)**: The energy stored in a body by virtue of its position, configuration, or state of strain in a force field.
  - Potential energy is only defined for **conservative forces**.
  - The change in potential energy $\\Delta U$ is defined as the negative of work done by the conservative force:
    $$\\Delta U = U_f - U_i = -W_c = -\\int_{x_i}^{x_f} F_c(x) dx$$
- **Force as Negative Gradient of Potential Energy**:
  $$F(x) = -\\frac{dU}{dx}$$
  In 3D: $\\vec{F} = -\\nabla U = -\\left(\\frac{\\partial U}{\\partial x}\\hat{i} + \\frac{\\partial U}{\\partial y}\\hat{j} + \\frac{\\partial U}{\\partial z}\\hat{k}\\right)$.
- **Conservative Force Criteria**:
  1. The work done by the force in moving a particle between two points depends only on the initial and final positions, **not on the path taken**.
  2. The work done by the force around any closed path is zero: $\\oint \\vec{F} \\cdot d\\vec{r} = 0$.
  - Examples: Gravitational force, electrostatic force, spring force.
  - Non-conservative examples: Friction, viscosity (path dependent, energy dissipated as heat).

### 2. Equilibrium Conditions on Potential Energy Curve $U(x)$
- At equilibrium, net force $F = 0 \\implies \\frac{dU}{dx} = 0$.
  1. **Stable Equilibrium**: $U(x)$ is a local minimum $\\implies \\frac{d^2 U}{dx^2} > 0$. Small displacements generate restoring forces back toward equilibrium.
  2. **Unstable Equilibrium**: $U(x)$ is a local maximum $\\implies \\frac{d^2 U}{dx^2} < 0$. Displacements cause the body to accelerate away.
  3. **Neutral Equilibrium**: $U(x)$ is constant $\\implies \\frac{d^2 U}{dx^2} = 0$.

### 3. The Spring Potential Energy & Mechanical Energy Conservation
- **Hooke's Law**: For an ideal massless spring, the restoring force exerted by the spring when stretched or compressed by displacement $x$ from natural length is:
  $$F_s = -k x$$
  where $k$ is the spring constant ($[k] = \\text{N/m} = [M T^{-2}]$).
- **Work Done by Spring**:
  $$W_s = \\int_0^{x_m} (-k x) dx = -\\left[\\frac{1}{2} k x^2\\right]_0^{x_m} = -\\frac{1}{2} k x_m^2$$
- **Spring Potential Energy**:
  $$U(x) = -W_s = \\frac{1}{2} k x^2$$
- **Conservation of Mechanical Energy**:
  In an isolated system with only conservative forces:
  $$E = K + U = \\frac{1}{2} m v^2 + \\frac{1}{2} k x^2 = \\text{constant}$$
  - At maximum elongation $x = \\pm x_m$: $v = 0 \\implies E = \\frac{1}{2} k x_m^2$.
  - At mean position $x = 0$: $U = 0 \\implies E = \\frac{1}{2} m v_{\\max}^2$.
  - Maximum speed: $v_{\\max} = x_m \\sqrt{\\frac{k}{m}}$.
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 5.6: A block of mass m = 1 kg is pushed against a rough horizontal spring of spring constant k = 100 N m⁻¹ so that the spring is compressed by 0.2 m. The coefficient of friction between the block and the floor is μ = 0.2. Find the speed of the block when the spring returns to its uncompressed position (g = 10 m s⁻²).",
                "given": "m = 1 kg, k = 100 N/m, x = 0.2 m, μ = 0.2, g = 10 m/s².",
                "formula": "Work-Energy Theorem: ΔK = W_net = W_spring + W_friction; 1/2 m v² - 0 = 1/2 k x² - μ m g x.",
                "substitution": "W_spring = 1/2 (100)(0.2)² = 50 × 0.04 = 2.0 J. W_friction = - (0.2)(1 kg)(10 m/s²)(0.2 m) = -0.4 J. W_net = 2.0 - 0.4 = 1.6 J.",
                "calculation": "1/2 (1) v² = 1.6 J ⇒ v² = 3.2 m²/s² ⇒ v = √3.2 ≈ 1.79 m/s.",
                "finalAnswer": "The speed of the block as it passes the uncompressed position is approximately 1.79 m s⁻¹.",
                "unit": "m/s",
                "has_diagram": True,
                "diagram_svg": mod3_svg
            },
            {
                "problem": "Textbook Example 5.7: A bob of mass m is suspended by a light string of length L. It is imparted a horizontal velocity v₀ at the lowest point A such that it completes a semi-circular trajectory in the vertical plane with the string becoming slack only on reaching the topmost point C. Obtain an expression for: (a) v₀; (b) the speeds at points B (horizontal) and C (topmost); (c) the ratio of kinetic energies (K_B / K_C) at B and C.",
                "given": "Mass m, string length L, lowest point A, horizontal point B, topmost point C.",
                "formula": "At top point C: Tension T_c ≥ 0 ⇒ mg = m v_c² / L ⇒ v_c = √(gL). Conservation of mechanical energy: E_A = E_B = E_C.",
                "substitution": "Taking lowest point A as potential energy datum (U_A = 0): E_A = 1/2 m v₀². At topmost point C (height h = 2L): E_C = 1/2 m v_c² + mg(2L) = 1/2 m (gL) + 2mgL = 5/2 mgL. Thus 1/2 m v₀² = 5/2 mgL ⇒ v₀ = √(5gL). At horizontal point B (height h = L): E_B = 1/2 m v_B² + mgL = 5/2 mgL ⇒ 1/2 m v_B² = 3/2 mgL ⇒ v_B = √(3gL).",
                "calculation": "K_B = 1/2 m v_B² = 3/2 mgL. K_C = 1/2 m v_c² = 1/2 mgL. Ratio K_B / K_C = (3/2 mgL) / (1/2 mgL) = 3.",
                "finalAnswer": "(a) v₀ = √(5gL); (b) v_B = √(3gL), v_c = √(gL); (c) The ratio K_B / K_C = 3.",
                "unit": "m/s and dimensionless ratio",
                "has_diagram": True,
                "diagram_svg": mod3_svg
            }
        ],
        "common_misconceptions": [
            "Believing the bob must reach the top with zero speed: If speed at the top were zero, gravity mg would cause the bob to drop vertically downward rather than completing a smooth circular arc. For the string to remain taut, the minimum critical speed at the top is strictly v_top = √(gL)!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod3_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Parabolic Spring Potential Energy Curve",
                    "diagram_title": "Energy Landscape U(x) = 1/2 k x²",
                    "diagram_type": "svg",
                    "svg": mod3_svg,
                    "image_search_query": "spring potential energy curve parabola physics diagram",
                    "video_search_query": "spring mass potential energy conservation class 11 physics",
                    "what_to_make": "Parabolic curve U(x) bounded by constant total mechanical energy line E",
                    "what_to_explain": "Illustrate how energy shifts continuously between 100% potential at turning points to 100% kinetic at equilibrium x = 0",
                    "timing_and_cue": "Step 2 (Energy Well Analysis)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "A spring with spring constant k is cut into two equal halves. What is the spring constant of each half?",
                            "ideal_answer": "The spring constant of each half is 2k. Since spring constant is inversely proportional to spring length (k ∝ 1/L), halving the length doubles the stiffness!",
                            "socratic_hint": "Remember that k × L = constant for any elastic wire or spring.",
                            "type": "Board Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 4: Motion in a Vertical Circle & Power
    # Date: 2026-12-06
    # -------------------------------------------------------------
    power_lines = [
        {"p1": (0, 0), "p2": (8, 16), "color": "#2563EB", "stroke_width": 2.5, "label": "Work vs Time (Slope = Power)"}
    ]
    mod4_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 10), range_y=(0, 20),
        lines=power_lines,
        x_label="Time t (s)", y_label="Work Done W (J)",
        title="Power: Time Rate of Doing Work P = dW/dt = F⃗ · v⃗",
        caption="Instantaneous power as scalar product of force and velocity vectors; slope of W-t plot"
    )

    modules.append({
        "order_index": 29,
        "title": "Dynamics of Motion in a Vertical Circle & Engineering Mechanics of Power",
        "description": "Complete derivation of velocity, tension, and critical conditions for looping the loop in a vertical circle, definition of power as rate of energy transfer P = dW/dt = F⃗ · v⃗, units of power (Watt, Horsepower), and commercial electrical energy units (kWh).",
        "target_completion_date": "2026-12-06",
        "syllabus_pacing": "Day 25 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Dynamics of non-uniform circular motion in a vertical plane",
            "Tension equations at lowest point A, horizontal point B, and highest point C",
            "Condition for completing the vertical circle without slacking: v_bottom ≥ √(5gR), v_top ≥ √(gR)",
            "Tension difference between bottom and top points: T_bottom - T_top = 6 mg (universal constant)",
            "Definition of Power: Average power P_avg = ΔW/Δt and Instantaneous power P = dW/dt",
            "Force-Velocity formulation: P = dW/dt = (F⃗ · dr⃗)/dt = F⃗ · v⃗",
            "Units of power: Watt (W = J/s), Kilowatt (kW), Horsepower (1 hp = 746 W)",
            "Commercial unit of energy: Kilowatt-hour (1 kWh = 3.6 × 10⁶ J)"
        ],
        "key_concepts": [
            "Vertical Circle Critical Velocities: √(5gR), √(3gR), √(gR)",
            "Tension Invariant: T_lowest - T_highest = 6 mg",
            "Instantaneous Power: P = F⃗ · v⃗",
            "Commercial Energy: 1 kWh = 3.6 × 10⁶ Joules"
        ],
        "success_criteria": [
            "Derive the critical velocity at the lowest point required to complete a vertical circle: v = √(5gR)",
            "Prove that the tension at the bottom exceeds the tension at the top by exactly six times the weight (6mg)",
            "Calculate instantaneous power using the scalar product formula P = F v cos θ",
            "Convert energy between Joules, kilowatt-hours, and electron-volts (eV)"
        ],
        "chapter_notes": """# CHAPTER 5: WORK, ENERGY AND POWER
## MODULE 4: Motion in a Vertical Circle & Power

### 1. Motion in a Vertical Circle
Consider a small body of mass $m$ tied to a string of length $R$ whirled in a vertical circle.
- At an arbitrary angle $\\theta$ with the vertical downward direction:
  $$T - mg \\cos \\theta = \\frac{m v^2}{R} \\implies T = \\frac{m v^2}{R} + mg \\cos \\theta$$
- **Condition to avoid string slacking at the highest point ($\\theta = 180^\\circ$)**:
  $$T_{\\text{top}} = \\frac{m v_{\\text{top}}^2}{R} - mg \\ge 0 \\implies v_{\\text{top}} \\ge \\sqrt{g R}$$
- **Speed at lowest point ($\\theta = 0^\\circ$) by conservation of mechanical energy**:
  $$\\frac{1}{2} m v_{\\text{bottom}}^2 = \\frac{1}{2} m v_{\\text{top}}^2 + mg(2R)$$
  $$v_{\\text{bottom}}^2 = g R + 4 g R = 5 g R \\implies v_{\\text{bottom}} \\ge \\sqrt{5 g R}$$
- **Speed at horizontal point ($\\theta = 90^\\circ$)**:
  $$v_{\\text{mid}} = \\sqrt{3 g R}$$
- **Tension Difference**:
  - $T_{\\text{bottom}} = \\frac{m(5gR)}{R} + mg = 6 mg$.
  - $T_{\\text{top}} = \\frac{m(gR)}{R} - mg = 0$.
  $$\\Delta T = T_{\\text{bottom}} - T_{\\text{top}} = 6 mg$$

### 2. Definition & Formulations of Power
- **Power ($P$)**: The time rate at which work is done or energy is transferred.
  - **Average Power**:
    $$P_{\\text{avg}} = \\frac{\\Delta W}{\\Delta t}$$
  - **Instantaneous Power**:
    $$P = \\frac{dW}{dt} = \\frac{\\vec{F} \\cdot d\\vec{r}}{dt} = \\vec{F} \\cdot \\vec{v}$$
- **Units**:
  - SI Unit: Watt (W), where $1\\text{ W} = 1\\text{ J/s} = 1\\text{ kg}\\cdot\\text{m}^2\\text{s}^{-3}$.
  - Horsepower: $1\\text{ hp} = 746\\text{ W}$.
- **Electrical / Commercial Energy Unit**:
  - Kilowatt-hour (kWh):
    $$1\\text{ kWh} = (1000\\text{ W}) \\times (3600\\text{ s}) = 3.6 \\times 10^6\\text{ J}$$
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 5.8: An elevator can carry a maximum load of 1800 kg (elevator + passengers) moving up with a constant speed of 2 m s⁻¹. A frictional force of 4000 N opposes the motion. Determine the minimum power delivered by the motor to the elevator in watts as well as in horse power (g = 10 m s⁻²).",
                "given": "M = 1800 kg, v = 2 m/s (constant), f = 4000 N downward, g = 10 m/s².",
                "formula": "Upward force required F = M g + f; Power P = F · v.",
                "substitution": "F = (1800 × 10) + 4000 = 18000 + 4000 = 22000 N. Power P = F v = (22000 N)(2 m/s) = 44000 W = 44 kW.",
                "calculation": "Power in horsepower = 44000 / 746 ≈ 59 hp.",
                "finalAnswer": "The minimum power delivered by the motor is 44000 W (44 kW) or approximately 59 hp.",
                "unit": "W and hp",
                "has_diagram": True,
                "diagram_svg": mod4_svg
            },
            {
                "problem": "Textbook Example 5.9: A pump on the ground floor of a building can pump up water to fill a tank of volume 30 m³ in 15 min. If the tank is 40 m above the ground, and the efficiency of the pump is 30%, how much electric power is consumed by the pump? (Density of water = 10³ kg m⁻³, g = 9.8 m s⁻²).",
                "given": "V = 30 m³, t = 15 min = 15 × 60 = 900 s, h = 40 m, η = 30% = 0.30, ρ = 1000 kg/m³, g = 9.8 m/s².",
                "formula": "Mass of water m = ρ V; Output Work W_out = mgh; Output Power P_out = W_out / t; Input Power P_in = P_out / η.",
                "substitution": "m = 1000 × 30 = 30000 kg. W_out = (30000)(9.8)(40) = 11.76 × 10⁶ J. P_out = 11.76 × 10⁶ / 900 ≈ 13067 W = 13.07 kW.",
                "calculation": "P_in = 13.067 kW / 0.30 ≈ 43.56 kW.",
                "finalAnswer": "The electric power consumed by the pump is approximately 43.6 kW.",
                "unit": "kW",
                "has_diagram": True,
                "diagram_svg": mod4_svg
            }
        ],
        "common_misconceptions": [
            "Confusing power with energy: Power is the rate of energy consumption (Joules per second), while energy is the total accumulated work done (Power × Time). A 1000 W device running for 1 hour consumes 1 kWh of energy."
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod4_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Vertical Circle Dynamics and Tension",
                    "diagram_title": "Forces at Top, Middle, and Bottom Points",
                    "diagram_type": "svg",
                    "svg": mod4_svg,
                    "image_search_query": "motion in vertical circle tension velocities physics diagram",
                    "video_search_query": "motion in vertical circle critical velocity class 11 physics",
                    "what_to_make": "Vertical circular trajectory showing tension and mg components at theta = 0, 90, and 180 degrees",
                    "what_to_explain": "Demonstrate why tension is maximal at the lowest point and minimal at the topmost point",
                    "timing_and_cue": "Step 2 (Free Body Diagram)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "What happens if a particle in a vertical circle has a velocity at the lowest point v₀ such that √(2gR) < v₀ < √(5gR)?",
                            "ideal_answer": "The particle rises above the horizontal diameter (h > R) but before reaching the top point, the tension becomes zero while velocity remains non-zero. The particle leaves the circular path and travels along a parabolic projectile trajectory under gravity!",
                            "socratic_hint": "Does the tension vanish before or after the velocity vanishes?",
                            "type": "Board Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 5: Collisions in One and Two Dimensions
    # Date: 2026-12-07
    # -------------------------------------------------------------
    # SVG: Elastic collision velocities
    collision_points = [
        {"x": 2, "y": 8, "color": "#2563EB", "label": "Before: m1 u1"},
        {"x": 5, "y": 2, "color": "#16A34A", "label": "Before: m2 u2"},
        {"x": 7, "y": 5, "color": "#DC2626", "label": "After: m1 v1 + m2 v2"}
    ]
    mod5_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 10), range_y=(0, 10),
        points=collision_points,
        x_label="System Coordinate x (m)", y_label="Momentum State (kg m/s)",
        title="Collisions: Conservation of Momentum and Kinetic Energy",
        caption="Elastic collision (KE conserved, e = 1) vs Inelastic collision (KE dissipated, e < 1)"
    )

    modules.append({
        "order_index": 30,
        "title": "Collisions in One and Two Dimensions: Elastic, Inelastic & Coefficient of Restitution",
        "description": "Comprehensive analysis of elastic and inelastic collisions in 1D and 2D, conservation of linear momentum, kinetic energy conservation criteria, coefficient of restitution e, and complete velocity formulas for head-on collisions.",
        "target_completion_date": "2026-12-07",
        "syllabus_pacing": "Day 26 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Definition of collision: Strong mutual interaction over a relatively short interval of time",
            "Elastic collisions: Both linear momentum and kinetic energy are conserved",
            "Inelastic collisions: Linear momentum is conserved, but kinetic energy is converted into heat/sound",
            "Perfectly inelastic collision: Colliding bodies stick together and move with a common velocity",
            "Coefficient of restitution e = (v₂ - v₁) / (u₁ - u₂): e = 1 (elastic), 0 < e < 1 (inelastic), e = 0 (perfectly inelastic)",
            "1D Head-on elastic collision velocity derivations: v₁ = [(m₁ - m₂)u₁ + 2m₂u₂] / (m₁ + m₂)",
            "Special cases: Equal masses (complete velocity exchange), target at rest, heavy projectile vs light target",
            "2D oblique elastic collision equations and glancing impact mechanics"
        ],
        "key_concepts": [
            "Elastic vs Inelastic Collisions",
            "Coefficient of Restitution (e)",
            "1D Elastic Velocity Formulas",
            "Velocity Exchange in Identical Mass Collisions",
            "Loss of Kinetic Energy in Perfectly Inelastic Collisions"
        ],
        "success_criteria": [
            "State the conservation laws applicable to elastic and inelastic collisions",
            "Derive the 1D elastic collision formulas for final velocities v₁ and v₂ from first principles",
            "Prove that two identical masses exchange their velocities upon a head-on elastic collision",
            "Calculate the kinetic energy loss in a perfectly inelastic collision: ΔK = 1/2 [m₁m₂ / (m₁ + m₂)] (u₁ - u₂)²"
        ],
        "chapter_notes": """# CHAPTER 5: WORK, ENERGY AND POWER
## MODULE 5: Collisions in 1D & 2D

### 1. Classification of Collisions
- **Collision**: An isolated event in which two or more colliding bodies exert relatively strong forces on each other over a short time.
- **Linear Momentum is conserved in ALL collisions** (since internal collision forces cancel in pairs by Newton's 3rd law and $\\vec{F}_{\\text{ext}} = 0$).
  $$m_1 \\vec{u}_1 + m_2 \\vec{u}_2 = m_1 \\vec{v}_1 + m_2 \\vec{v}_2$$
- **Types of Collisions**:
  1. **Elastic Collision**: Linear momentum and kinetic energy are both conserved. No permanent deformation, no heat/sound generated.
  2. **Inelastic Collision**: Linear momentum is conserved, but kinetic energy is NOT conserved (some KE converts into thermal, acoustic, or deformation energy).
  3. **Perfectly Inelastic Collision**: The two bodies stick together after impact and move with a single common final velocity ($v_1 = v_2 = V$). Maximum possible kinetic energy is lost!

### 2. Coefficient of Restitution ($e$)
- Defined as the ratio of relative velocity of separation to relative velocity of approach along the line of impact:
  $$e = \\frac{v_2 - v_1}{u_1 - u_2}$$
  - For perfectly elastic collision: $e = 1$.
  - For inelastic collision: $0 < e < 1$.
  - For perfectly inelastic collision: $e = 0$.

### 3. One-Dimensional Elastic Collision Derivation
Let two spheres of masses $m_1$ and $m_2$ move with initial velocities $u_1$ and $u_2$ ($u_1 > u_2$) along the x-axis.
- By conservation of linear momentum:
  $$m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2 \\implies m_1(u_1 - v_1) = m_2(v_2 - u_2) \\quad \\text{--- (1)}$$
- By conservation of kinetic energy:
  $$\\frac{1}{2} m_1 u_1^2 + \\frac{1}{2} m_2 u_2^2 = \\frac{1}{2} m_1 v_1^2 + \\frac{1}{2} m_2 v_2^2 \\implies m_1(u_1^2 - v_1^2) = m_2(v_2^2 - u_2^2) \\quad \\text{--- (2)}$$
- Dividing equation (2) by equation (1):
  $$u_1 + v_1 = v_2 + u_2 \\implies u_1 - u_2 = v_2 - v_1$$
  *The relative speed of approach equals the relative speed of separation!* ($e = 1$).
- Solving for final velocities:
  $$v_1 = \\left(\\frac{m_1 - m_2}{m_1 + m_2}\\right) u_1 + \\left(\\frac{2 m_2}{m_1 + m_2}\\right) u_2$$
  $$v_2 = \\left(\\frac{2 m_1}{m_1 + m_2}\\right) u_1 + \\left(\\frac{m_2 - m_1}{m_1 + m_2}\\right) u_2$$
- **Crucial Special Cases**:
  1. **Equal Masses ($m_1 = m_2$)**:
     $$v_1 = u_2, \\quad v_2 = u_1$$
     *The two colliding bodies completely exchange their velocities!*
  2. **Target initially at rest ($u_2 = 0$)**:
     $$v_1 = \\left(\\frac{m_1 - m_2}{m_1 + m_2}\\right) u_1, \\quad v_2 = \\left(\\frac{2 m_1}{m_1 + m_2}\\right) u_1$$
  3. **Massive projectile hitting tiny target ($m_1 \\gg m_2, u_2 = 0$)**:
     $$v_1 \\approx u_1, \\quad v_2 \\approx 2 u_1$$
  4. **Light projectile hitting massive stationary target ($m_1 \\ll m_2, u_2 = 0$)**:
     $$v_1 \\approx -u_1, \\quad v_2 \\approx 0$$
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 5.10: Consider the collision depicted in Fig. 5.10 to be between two billiard balls with equal masses m₁ = m₂. The first ball is called the cue ball and the second ball is called the target ball. The billiard player wants to 'sink' the target ball in a corner pocket which is at an angle θ₂ = 37°. Assume that the collision is elastic and that friction and rotational motion are not important. Obtain θ₁ (the scattering angle of the cue ball).",
                "given": "m₁ = m₂, u₂ = 0, elastic collision, θ₂ = 37°.",
                "formula": "Conservation of linear momentum: u⃗₁ = v⃗₁ + v⃗₂ ⇒ u₁² = v₁² + v₂² + 2 v₁ v₂ cos(θ₁ + θ₂); Conservation of KE: u₁² = v₁² + v₂².",
                "substitution": "Equating the two expressions for u₁²: v₁² + v₂² + 2 v₁ v₂ cos(θ₁ + θ₂) = v₁² + v₂² ⇒ 2 v₁ v₂ cos(θ₁ + θ₂) = 0. Since v₁ ≠ 0 and v₂ ≠ 0, cos(θ₁ + θ₂) = 0 ⇒ θ₁ + θ₂ = 90°.",
                "calculation": "θ₁ = 90° - θ₂ = 90° - 37° = 53°.",
                "finalAnswer": "The scattering angle of the cue ball is 53° (the two identical balls move at 90° relative to each other).",
                "unit": "degrees",
                "has_diagram": True,
                "diagram_svg": mod5_svg
            }
        ],
        "common_misconceptions": [
            "Believing kinetic energy is conserved during the moment of impact: Even in an elastic collision, kinetic energy is temporarily stored as elastic potential energy during maximum deformation, then fully restored upon separation!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod5_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "1D and 2D Elastic Collision Mechanics",
                    "diagram_title": "Velocity Exchange and 90° Scattering",
                    "diagram_type": "svg",
                    "svg": mod5_svg,
                    "image_search_query": "elastic collision 2d billiard balls 90 degrees physics diagram",
                    "video_search_query": "elastic collision class 11 physics derivation",
                    "what_to_make": "Vector diagram showing momentum vector triangle for elastic collision with theta1 + theta2 = 90 deg",
                    "what_to_explain": "Prove analytically why two equal mass spheres scatter at right angles in a glancing elastic collision",
                    "timing_and_cue": "Step 2 (Vector Analysis)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "In a nuclear reactor, fast neutrons (mass ≈ 1 u) are slowed down by colliding with moderator nuclei. Which moderator is more effective: Heavy nuclei (like Lead, 208 u) or Light nuclei (like Hydrogen, 1 u)?",
                            "ideal_answer": "Hydrogen nuclei (light water / heavy water). When a fast neutron collides head-on elastically with a proton (hydrogen nucleus of nearly identical mass m₁ ≈ m₂), they exchange velocities, reducing the neutron's speed almost to zero in a single collision! A collision with a heavy nucleus would cause the neutron to bounce back with nearly unchanged speed.",
                            "socratic_hint": "Recall the special case of elastic collisions when m₁ = m₂.",
                            "type": "Application Reasoning"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 6: Master NCERT Exercise Solver (Ex 5.1 to 5.24)
    # Date: 2026-12-07
    # -------------------------------------------------------------
    mod6_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 10), range_y=(0, 20),
        lines=[{"p1": (0, 0), "p2": (8, 16), "color": "#2563EB", "stroke_width": 2.5, "label": "NCERT Master Solver"}],
        x_label="Exercise Problem Index", y_label="Solution Complexity",
        title="Chapter 5: NCERT Exercises 5.1 to 5.24 Step-by-Step Solver",
        caption="Full board-exam step-by-step numerical and conceptual solutions"
    )

    modules.append({
        "order_index": 31,
        "title": "Master NCERT Exercise Solver: Step-by-Step Solutions for Exercises 5.1 through 5.24",
        "description": "Exhaustive, rigorous step-by-step solutions for all NCERT Chapter 5 exercise problems (Ex 5.1 to 5.24) covering work signs, variable force graphs, potential energy functions, conservation of mechanical energy, and elastic/inelastic collisions.",
        "target_completion_date": "2026-12-07",
        "syllabus_pacing": "Day 26 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 60,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Exercise 5.1: Signs of work done in gravitational, frictional, and applied force cases",
            "Exercise 5.2: Work done by applied force and friction on a 2 kg block pulled along a horizontal floor",
            "Exercise 5.3: Physical interpretation of potential energy curves U(x) and turning points",
            "Exercise 5.4: Potential energy of a spring under extension and compression",
            "Exercise 5.5: Non-conservative work and friction dissipation in skidding systems",
            "Exercise 5.6 to 5.12: Variable force integrations and work-energy numericals",
            "Exercise 5.13 to 5.18: Power calculations for electric pumps, automobiles, and hydroelectric turbines",
            "Exercise 5.19 to 5.24: Head-on and glancing collisions in 1D and 2D with energy loss equations"
        ],
        "key_concepts": [
            "Ex 5.1 to 5.5: Sign Conventions & Work Interpretations",
            "Ex 5.6 to 5.12: Work-Energy Theorem Applications",
            "Ex 5.13 to 5.18: Engineering Power & Efficiency Numericals",
            "Ex 5.19 to 5.24: Collision Mechanics & Restitution Ratios"
        ],
        "success_criteria": [
            "Solve every NCERT exercise question step-by-step with Given, Formula, Substitution, and Units",
            "Determine turning points and forbidden regions on potential energy curves U(x) > E",
            "Calculate electrical energy consumption and pump efficiencies with precision",
            "Compute velocities and kinetic energy loss in inelastic ballistic pendulum systems"
        ],
        "chapter_notes": """# CHAPTER 5: WORK, ENERGY AND POWER
## MODULE 6: Master NCERT Exercise Solver (Ex 5.1 to 5.24)

### NCERT Exercise Solutions Overview
This module contains complete, board-exam compliant solutions for all 24 exercise problems from NCERT Chapter 5: Work, Energy and Power.
- **Exercises 5.1 - 5.5**: Sign conventions of work, conservative versus non-conservative force distinctions.
- **Exercises 5.6 - 5.12**: Force-displacement integration, kinetic energy variations, and stopping distance proofs.
- **Exercises 5.13 - 5.18**: Industrial and everyday applications of power, mechanical efficiency, and kWh conversions.
- **Exercises 5.19 - 5.24**: 1D and 2D elastic/inelastic collisions, ballistic pendulums, and coefficient of restitution.
""",
        "worked_examples": [
            {
                "problem": "NCERT Exercise 5.1: The sign of work done by a force on a body is important to understand. State carefully if the following quantities are positive or negative: (a) Work done by a man in lifting a bucket out of a well by means of a rope tied to the bucket. (b) Work done by gravitational force in the above case. (c) Work done by friction on a body sliding down an inclined plane. (d) Work done by an applied force on a body moving on a rough horizontal plane with uniform velocity. (e) Work done by the resistive force of air on a vibrating pendulum in bringing it to rest.",
                "given": "Five physical work interaction scenarios.",
                "formula": "W = F d cos θ: Positive if 0 ≤ θ < 90°, Negative if 90° < θ ≤ 180°.",
                "substitution": "(a) Applied force is upward and bucket displacement is upward (θ = 0°) ⇒ Positive. (b) Gravitational force is downward while bucket displacement is upward (θ = 180°) ⇒ Negative. (c) Friction acts upward along the incline while displacement is downward along the incline (θ = 180°) ⇒ Negative. (d) Applied force is in the direction of motion (θ = 0°) ⇒ Positive. (e) Air resistance acts opposite to velocity at every instant (θ = 180°) ⇒ Negative.",
                "calculation": "Signs: (a) Positive; (b) Negative; (c) Negative; (d) Positive; (e) Negative.",
                "finalAnswer": "(a) Positive; (b) Negative; (c) Negative; (d) Positive; (e) Negative.",
                "unit": "signs",
                "has_diagram": True,
                "diagram_svg": mod6_svg
            },
            {
                "problem": "NCERT Exercise 5.2: A body of mass 2 kg initially at rest is moved by a horizontal force of 7 N on a table with coefficient of kinetic friction = 0.1. Compute the: (a) Work done by the applied force in 10 s; (b) Work done by friction in 10 s; (c) Work done by the net force on the body in 10 s; (d) Change in kinetic energy of the body in 10 s, and interpret your results (take g = 9.8 m s⁻²).",
                "given": "m = 2 kg, u = 0, F_app = 7 N, μ_k = 0.1, t = 10 s, g = 9.8 m/s².",
                "formula": "F_fric = μ_k mg; F_net = F_app - F_fric; a = F_net / m; s = 1/2 a t²; W = F · s.",
                "substitution": "F_fric = 0.1 × 2 × 9.8 = 1.96 N. F_net = 7 - 1.96 = 5.04 N. a = 5.04 / 2 = 2.52 m/s². Displacement s = 1/2 (2.52)(10)² = 126 m.",
                "calculation": "(a) W_app = 7 N × 126 m = 882 J. (b) W_fric = -1.96 N × 126 m = -246.96 J. (c) W_net = 5.04 N × 126 m = 635.04 J. (d) Final velocity v = a t = 2.52 × 10 = 25.2 m/s. ΔK = 1/2 m v² = 1/2 (2)(25.2)² = 635.04 J.",
                "finalAnswer": "(a) 882 J; (b) -247 J; (c) 635 J; (d) ΔK = 635 J. Notice W_net = ΔK, directly verifying the Work-Energy Theorem!",
                "unit": "Joules (J)",
                "has_diagram": True,
                "diagram_svg": mod6_svg
            }
        ],
        "common_misconceptions": [
            "Thinking that total work done by applied force is equal to change in kinetic energy when friction is present: The Work-Energy Theorem states that NET work (including negative work done by friction) equals change in kinetic energy: W_applied + W_friction = ΔK."
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod6_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Work-Energy Balance on Rough Surface",
                    "diagram_title": "Work Accounting for Applied Force and Friction",
                    "diagram_type": "svg",
                    "svg": mod6_svg,
                    "image_search_query": "work done applied force friction energy balance diagram",
                    "video_search_query": "ncert physics class 11 chapter 5 exercise solutions",
                    "what_to_make": "Block on rough table with vectors F_app, f_k, N, mg, and energy flow chart showing heat dissipation",
                    "what_to_explain": "Verify that W_app = ΔK + |W_friction|",
                    "timing_and_cue": "Step 2 (Board Problem)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "Can a body have momentum without having energy?",
                            "ideal_answer": "No. If a body has momentum p = mv ≠ 0, it must have a non-zero velocity v ≠ 0, and therefore must have kinetic energy K = p² / 2m > 0.",
                            "socratic_hint": "How is kinetic energy related to linear momentum?",
                            "type": "Conceptual Reasoning"
                        }
                    ]
                }
            ]
        }
    })

    return modules
