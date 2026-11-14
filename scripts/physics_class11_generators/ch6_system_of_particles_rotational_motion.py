"""
ch6_system_of_particles_rotational_motion.py
CBSE Class 11 Physics - Chapter 6: System of Particles and Rotational Motion
Part 1 (Mid-Term Syllabus, Unit V: Motion of System of Particles and Rigid Body)
Target Pacing: December 08, 2026 to December 12, 2026 (7 Modules, 5 Days)
"""

import sys
import os
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

import svg_builder_physics11 as sb

CURRICULUM_ID = "c11_phy_ch06_rotational_motion"
CLASS_LEVEL = "Class 11"
BOARD = "CBSE"
SUBJECT = "Physics"

def get_modules():
    modules = []

    # -------------------------------------------------------------
    # MODULE 1: Center of Mass of Discrete and Continuous Systems
    # Date: 2026-12-08
    # -------------------------------------------------------------
    com_points = [
        {"x": 2, "y": 3, "color": "#2563EB", "label": "m₁ (x₁, y₁)"},
        {"x": 8, "y": 7, "color": "#16A34A", "label": "m₂ (x₂, y₂)"},
        {"x": 4.4, "y": 4.6, "color": "#DC2626", "label": "COM (R_cm)"}
    ]
    com_lines = [
        {"p1": (2, 3), "p2": (8, 7), "color": "#94A3B8", "stroke_width": 1.5, "dash": "4,4"}
    ]
    mod1_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 10), range_y=(0, 10),
        points=com_points, lines=com_lines,
        x_label="x-coordinate (m)", y_label="y-coordinate (m)",
        title="Center of Mass of a Two-Particle System: R_cm = (m₁ r₁ + m₂ r₂) / (m₁ + m₂)",
        caption="The center of mass lies on the line joining the two particles, dividing it inversely as their masses"
    )

    modules.append({
        "order_index": 32,
        "title": "Center of Mass of Discrete Systems, Continuous Bodies & Rigid Body Foundations",
        "description": "Definition of rigid body, center of mass of a two-particle system, generalization to N-particle system, continuous mass distributions (uniform thin rod, ring, disc, sphere), and symmetry principles for locating the center of mass.",
        "target_completion_date": "2026-12-08",
        "syllabus_pacing": "Day 27 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Definition of rigid body: A body with a perfectly definite and unchanging shape",
            "Translational vs Rotational motion of a rigid body (fixed axis vs precession)",
            "Center of Mass definition: A unique point where the entire mass of the system can be supposed to be concentrated",
            "Center of mass of two particles: X_cm = (m₁ x₁ + m₂ x₂) / (m₁ + m₂)",
            "Inverse mass ratio rule: Distance of COM from masses is inversely proportional to mass (m₁ r₁ = m₂ r₂)",
            "Center of mass of N-particle system: R⃗_cm = (Σ m_i r⃗_i) / M where M = Σ m_i",
            "Center of mass of continuous mass distribution: R⃗_cm = (1/M) ∫ r⃗ dm",
            "Derivation of COM for a uniform thin rod of length L: X_cm = L/2",
            "Center of mass of symmetrical bodies: Geometric center (ring, disc, sphere, cylinder)"
        ],
        "key_concepts": [
            "Rigid Body & Pure Rotation Definition",
            "Two-Particle & N-Particle Center of Mass Formula",
            "Continuous Mass Integration: R⃗_cm = (1/M) ∫ r⃗ dm",
            "Symmetry Principles & Center of Mass Location"
        ],
        "success_criteria": [
            "State the physical definition of center of mass and distinguish it from center of gravity",
            "Calculate COM coordinates for systems of particles arranged in 1D, 2D, and 3D configurations",
            "Derive the center of mass of a uniform rod of length L by setting dm = (M/L) dx",
            "Explain why the center of mass of a hollow ring or hollow cylinder lies in empty space"
        ],
        "chapter_notes": """# CHAPTER 6: SYSTEM OF PARTICLES AND ROTATIONAL MOTION
## MODULE 1: Center of Mass of Discrete and Continuous Systems

### 1. The Rigid Body Concept
- **Rigid Body**: An ideal body whose constituent particles remain at strictly invariant relative distances from each other regardless of applied external forces.
- **Types of Motion**:
  1. **Pure Translation**: Every particle of the body undergoes identical displacement in a given time interval. All particles have the exact same velocity $\\vec{v}$ and acceleration $\\vec{a}$ at every instant.
  2. **Pure Rotation**: The body rotates about a fixed axis; every particle moves in a circle whose center lies on the axis of rotation and whose radius equals the perpendicular distance from the axis.
  3. **General Plane Motion**: Combination of translation and rotation (e.g. a rolling bowling ball or wheel).

### 2. Center of Mass of a Two-Particle System
- Let two particles of masses $m_1$ and $m_2$ be located along the x-axis at positions $x_1$ and $x_2$.
- The center of mass coordinate $X_{\\text{cm}}$ is defined as:
  $$X_{\\text{cm}} = \\frac{m_1 x_1 + m_2 x_2}{m_1 + m_2}$$
- **Key Geometric Invariant**: If the center of mass is taken as the origin ($X_{\\text{cm}} = 0$):
  $$m_1 x_1 + m_2 x_2 = 0 \\implies m_1 r_1 = m_2 r_2 \\implies \\frac{r_1}{r_2} = \\frac{m_2}{m_1}$$
  *The center of mass divides the line segment joining the two masses in the inverse ratio of their masses!* (Closer to the heavier mass).

### 3. Center of Mass of N Particles in 3 Dimensions
- For a system of $n$ particles with masses $m_1, m_2, \\dots, m_n$ and position vectors $\\vec{r}_1, \\vec{r}_2, \\dots, \\vec{r}_n$:
  $$\\vec{R}_{\\text{cm}} = \\frac{\\sum_{i=1}^n m_i \\vec{r}_i}{\\sum_{i=1}^n m_i} = \\frac{1}{M} \\sum_{i=1}^n m_i \\vec{r}_i$$
  where $M = \\sum_{i=1}^n m_i$ is the total mass.
- In Cartesian components:
  $$X_{\\text{cm}} = \\frac{\\sum m_i x_i}{M}, \\quad Y_{\\text{cm}} = \\frac{\\sum m_i y_i}{M}, \\quad Z_{\\text{cm}} = \\frac{\\sum m_i z_i}{M}$$

### 4. Continuous Mass Distribution
- For a continuous body, replace the summation by an integral:
  $$\\vec{R}_{\\text{cm}} = \\frac{1}{M} \\int \\vec{r} dm$$
- **Uniform Thin Rod of Length $L$ and Mass $M$**:
  - Linear mass density $\\lambda = \\frac{M}{L} \\implies dm = \\lambda dx = \\frac{M}{L} dx$.
  - Taking one end at $x = 0$:
    $$X_{\\text{cm}} = \\frac{1}{M} \\int_0^L x \\left(\\frac{M}{L} dx\\right) = \\frac{1}{L} \\left[\\frac{x^2}{2}\\right]_0^L = \\frac{1}{L} \\cdot \\frac{L^2}{2} = \\frac{L}{2}$$
  - The center of mass lies exactly at its geometric midpoint!
- **Important Physical Invariant**: The center of mass need not lie inside the material of the body (e.g. hollow ring, hollow sphere, horseshoe magnet).
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 6.1: Find the centre of mass of three particles at the vertices of an equilateral triangle. The masses of the particles are 100 g, 150 g, and 200 g respectively. Each side of the equilateral triangle is 0.5 m long.",
                "given": "m₁ = 100 g = 0.1 kg at (0, 0); m₂ = 150 g = 0.15 kg at (0.5 m, 0); m₃ = 200 g = 0.2 kg at (0.25 m, 0.5 sin 60° = 0.25√3 m).",
                "formula": "X_cm = (m₁ x₁ + m₂ x₂ + m₃ x₃) / M; Y_cm = (m₁ y₁ + m₂ y₂ + m₃ y₃) / M; M = m₁ + m₂ + m₃.",
                "substitution": "M = 100 + 150 + 200 = 450 g. X_cm = [(100 × 0) + (150 × 0.5) + (200 × 0.25)] / 450 = (0 + 75 + 50) / 450 = 125 / 450 = 5 / 18 ≈ 0.278 m. Y_cm = [(100 × 0) + (150 × 0) + (200 × 0.25√3)] / 450 = (50√3) / 450 = √3 / 9 = 1 / (3√3) ≈ 0.192 m.",
                "calculation": "X_cm = 5/18 m ≈ 0.28 m; Y_cm = √3/9 m ≈ 0.19 m.",
                "finalAnswer": "The center of mass is located at coordinates (5/18 m, √3/9 m) ≈ (0.28 m, 0.19 m).",
                "unit": "meters (m)",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            },
            {
                "problem": "Textbook Example 6.2: Find the centre of mass of a triangular lamina (equilateral or isosceles plate) of uniform mass density.",
                "given": "Uniform triangular lamina ABC.",
                "formula": "By symmetry, divide the triangle into narrow strips parallel to the base BC. The center of mass of each strip lies at its midpoint. The line joining the midpoints is the median from vertex A.",
                "substitution": "Similarly, dividing strips parallel to side AC shows the center of mass must lie along the median from vertex B. Therefore, the center of mass must lie at the intersection of the medians.",
                "calculation": "The intersection of the medians of a triangle is its centroid G.",
                "finalAnswer": "The center of mass of a uniform triangular lamina coincides with its centroid G (which divides each median in the ratio 2:1 from the vertex).",
                "unit": "centroid location",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            }
        ],
        "common_misconceptions": [
            "Assuming center of mass must contain matter: For a hollow ring, doughnut, or hollow cylinder, the center of mass lies at the geometric center where no physical matter exists!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod1_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Center of Mass Coordinate Geometry",
                    "diagram_title": "Equilateral Triangle Mass Configuration",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "center of mass particles triangle coordinate system physics diagram",
                    "video_search_query": "center of mass system of particles class 11 ncert",
                    "what_to_make": "Triangle with masses at vertices and vector arrows to COM",
                    "what_to_explain": "Show how center of mass is biased toward the heaviest mass",
                    "timing_and_cue": "Step 2 (Coordinate Formulation)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "Two bodies of masses 2 kg and 4 kg are separated by 6 m. How far is the center of mass from the 2 kg body?",
                            "ideal_answer": "4 meters. By the inverse mass ratio rule, r₁ / r₂ = m₂ / m₁ = 4 / 2 = 2. Since r₁ + r₂ = 6 m, 2 r₂ + r₂ = 6 ⇒ 3 r₂ = 6 ⇒ r₂ = 2 m. Thus r₁ = 4 m from the 2 kg mass!",
                            "socratic_hint": "Use m₁ r₁ = m₂ r₂ where r₁ + r₂ = total distance.",
                            "type": "Board Exam Numerical"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 2: Motion of Center of Mass & Momentum Conservation
    # Date: 2026-12-09
    # -------------------------------------------------------------
    cm_motion_curves = [
        {"fn": lambda x: 8 - 0.2*(x-5)**2, "color": "#2563EB", "stroke_width": 2.5, "label": "Parabolic CM Path (Exploding Projectile)"}
    ]
    mod2_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 10), range_y=(0, 10),
        curves=cm_motion_curves,
        x_label="Horizontal Distance x (m)", y_label="Vertical Height y (m)",
        title="Center of Mass Motion: M A⃗_cm = F⃗_ext (Internal Forces Cancel)",
        caption="When a projectile explodes in mid-air, internal explosion forces cancel in pairs; the COM continues on its unchanged parabolic trajectory"
    )

    modules.append({
        "order_index": 33,
        "title": "Kinematics & Dynamics of Center of Mass, Newton's Second Law for Systems & Linear Momentum",
        "description": "Velocity and acceleration of the center of mass, Newton's second law for a system of particles M A⃗_cm = F⃗_ext, cancellation of internal forces in action-reaction pairs, and conservation of linear momentum with mid-air projectile explosion physics.",
        "target_completion_date": "2026-12-09",
        "syllabus_pacing": "Day 28 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Velocity of the center of mass: V⃗_cm = dR⃗_cm/dt = (Σ m_i v⃗_i) / M = P⃗_total / M",
            "Total linear momentum of a system of particles equals total mass times velocity of center of mass: P⃗ = M V⃗_cm",
            "Acceleration of center of mass: A⃗_cm = dV⃗_cm/dt = (Σ m_i a⃗_i) / M",
            "Newton's Second Law for a system of particles: M A⃗_cm = Σ F⃗_i = F⃗_ext + F⃗_int",
            "Cancellation of internal forces: Internal mutual interactions cancel in pairs by Newton's Third Law (F⃗_ij = -F⃗_ji ⇒ Σ F⃗_int = 0)",
            "Fundamental equation of system dynamics: M A⃗_cm = F⃗_ext",
            "Law of Conservation of Linear Momentum for a system: If F⃗_ext = 0, P⃗_total = constant ⇒ V⃗_cm = constant",
            "Motion of center of mass under internal explosions: An exploding shell whose fragments scatter in mid-air continues to follow the exact same parabolic trajectory"
        ],
        "key_concepts": [
            "Center of Mass Velocity: V⃗_cm = P⃗_total / M",
            "Newton's Second Law for System: M A⃗_cm = F⃗_ext",
            "Mutual Cancellation of Internal Forces (Σ F⃗_int = 0)",
            "System Linear Momentum Conservation & Projectile Explosion Invariant"
        ],
        "success_criteria": [
            "Derive M A⃗_cm = F⃗_ext from individual particle equations of motion and Newton's third law",
            "Explain why a boat moves backward when a person walks forward inside it on friction-free water",
            "Prove that the center of mass of an exploding firecracker continues along its original parabolic path until landing",
            "Calculate fragment landing locations and velocities using conservation of momentum and center of mass coordinates"
        ],
        "chapter_notes": """# CHAPTER 6: SYSTEM OF PARTICLES AND ROTATIONAL MOTION
## MODULE 2: Motion of Center of Mass & Momentum Conservation

### 1. Velocity and Momentum of Center of Mass
- The position vector of the center of mass is:
  $$\\vec{R}_{\\text{cm}} = \\frac{1}{M} \\sum_{i=1}^n m_i \\vec{r}_i$$
- Differentiating with respect to time $t$:
  $$\\vec{V}_{\\text{cm}} = \\frac{d\\vec{R}_{\\text{cm}}}{dt} = \\frac{1}{M} \\sum_{i=1}^n m_i \\frac{d\\vec{r}_i}{dt} = \\frac{1}{M} \\sum_{i=1}^n m_i \\vec{v}_i$$
- Multiplying by total mass $M$:
  $$M \\vec{V}_{\\text{cm}} = \\sum_{i=1}^n m_i \\vec{v}_i = \\sum_{i=1}^n \\vec{p}_i = \\vec{P}_{\\text{total}}$$
- **Invariant**: *The total linear momentum of a system of particles is equal to the product of the total mass of the system and the velocity of its center of mass.*

### 2. Acceleration of Center of Mass & Newton's Second Law
- Differentiating $\\vec{V}_{\\text{cm}}$ with respect to time $t$:
  $$\\vec{A}_{\\text{cm}} = \\frac{d\\vec{V}_{\\text{cm}}}{dt} = \\frac{1}{M} \\sum_{i=1}^n m_i \\frac{d\\vec{v}_i}{dt} = \\frac{1}{M} \\sum_{i=1}^n m_i \\vec{a}_i$$
  $$M \\vec{A}_{\\text{cm}} = \\sum_{i=1}^n m_i \\vec{a}_i = \\sum_{i=1}^n \\vec{F}_i$$
- The total force on each particle $i$ consists of external forces $\\vec{F}_i^{\\text{ext}}$ and internal forces $\\sum_{j \\ne i} \\vec{F}_{ij}^{\\text{int}}$ exerted by other particles in the system:
  $$\\sum_{i=1}^n \\vec{F}_i = \\sum_{i=1}^n \\vec{F}_i^{\\text{ext}} + \\sum_{i \\ne j} \\vec{F}_{ij}^{\\text{int}}$$
- By Newton's Third Law, $\\vec{F}_{ij}^{\\text{int}} = -\\vec{F}_{ji}^{\\text{int}}$ for every pair, so the internal force sum vanishes identically:
  $$\\sum_{i \\ne j} \\vec{F}_{ij}^{\\text{int}} = 0$$
  $$\\therefore M \\vec{A}_{\\text{cm}} = \\vec{F}_{\\text{ext}}$$
- **Monumental Principle**: *The center of mass of a system of particles moves as if all the mass of the system were concentrated at that point and all external forces were applied directly at that point!* Internal forces cannot accelerate the center of mass!

### 3. Conservation of Linear Momentum of a System
- If the net external force acting on the system is zero ($\\vec{F}_{\\text{ext}} = 0$):
  $$M \\vec{A}_{\\text{cm}} = 0 \\implies \\vec{A}_{\\text{cm}} = \\frac{d\\vec{V}_{\\text{cm}}}{dt} = 0 \\implies \\vec{V}_{\\text{cm}} = \\text{constant}$$
  $$\\vec{P}_{\\text{total}} = M \\vec{V}_{\\text{cm}} = \\text{constant}$$
- **Physical Application: Exploding Projectile**:
  When a shell fired with initial velocity $\\vec{v}_0$ explodes into fragments in mid-air due to internal explosive forces, $\\vec{F}_{\\text{ext}} = M\\vec{g}$ (gravity) is unchanged. Thus $\\vec{A}_{\\text{cm}} = \\vec{g}$. The center of mass of the fragments continues moving on the identical parabolic trajectory as if no explosion had occurred!
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 6.3: A projectile of mass m is fired from the ground with speed v₀ at an angle θ with the horizontal. At the highest point of its trajectory, it explodes into two equal fragments. One fragment comes to rest immediately after the explosion and falls vertically downward. Where does the other fragment land with respect to the launch point?",
                "given": "Total mass m, launch speed v₀, launch angle θ, equal fragments m₁ = m/2, m₂ = m/2. Projectile explodes at peak x = R/2, y = H.",
                "formula": "Range R = (v₀² sin 2θ)/g; Since internal forces do not change the motion of the center of mass, the COM must land at x_cm = R. x_cm = (m₁ x₁ + m₂ x₂) / m.",
                "substitution": "Fragment 1 comes to rest at the peak, so it drops straight down and lands at x₁ = R/2. We have: R = [(m/2)(R/2) + (m/2) x₂] / m = 1/4 R + 1/2 x₂.",
                "calculation": "1/2 x₂ = R - 1/4 R = 3/4 R ⇒ x₂ = (2)(3/4 R) = 3/2 R = 1.5 R.",
                "finalAnswer": "The second fragment lands at a distance of 1.5 R (or 3/2 of the original range) from the launch point.",
                "unit": "meters (m)",
                "has_diagram": True,
                "diagram_svg": mod2_svg
            }
        ],
        "common_misconceptions": [
            "Thinking that an explosion propels the center of mass: Chemical explosion forces are purely internal forces between the fragments. By Newton's 3rd law, they sum to zero and cannot change the acceleration of the center of mass!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod2_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Center of Mass Parabolic Path of Exploding Projectile",
                    "diagram_title": "Fragment Splitting and COM Invariance",
                    "diagram_type": "svg",
                    "svg": mod2_svg,
                    "image_search_query": "projectile explosion center of mass trajectory physics diagram",
                    "video_search_query": "motion of center of mass class 11 physics ncert",
                    "what_to_make": "Parabolic arc with explosion point at apex showing one piece dropping vertically and other landing at 1.5 R",
                    "what_to_explain": "Verify that COM coordinates x_cm = (m1 x1 + m2 x2) / M remain strictly on the theoretical trajectory",
                    "timing_and_cue": "Step 2 (Explosion Invariant)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "A man of mass 60 kg stands on a stationary wooden plank of mass 140 kg floating on a frictionless lake. If the man walks 4 m along the plank, how far does the plank shift relative to the shore?",
                            "ideal_answer": "1.2 m backward. Since net external horizontal force F_ext = 0, the center of mass of the system remains stationary: m_man Δx_man + M_plank Δx_plank = 0. Let plank move backward by x: 60(4 - x) - 140(x) = 0 ⇒ 240 - 60x - 140x = 0 ⇒ 200x = 240 ⇒ x = 1.2 m!",
                            "socratic_hint": "Use the condition that ΔX_cm = 0 when F_ext = 0.",
                            "type": "Board Exam Numerical"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 3: Vector Product & Rotational Kinematics
    # Date: 2026-12-10
    # -------------------------------------------------------------
    mod3_svg = sb.build_rotational_dynamics_svg(
        title="Vector Cross Product & Rotational Kinematics: v⃗ = ω⃗ × r⃗",
        caption="Right-hand rule for cross products, angular velocity vector ω⃗ along axis of rotation"
    )

    modules.append({
        "order_index": 34,
        "title": "Vector Product (Cross Product) of Vectors & Kinematics of Rotational Motion",
        "description": "Definition and geometric interpretation of vector (cross) product, right-hand thumb rule, properties and determinant calculation, linear versus angular velocity vector relation v⃗ = ω⃗ × r⃗, and the kinematic equations of uniform angular acceleration.",
        "target_completion_date": "2026-12-10",
        "syllabus_pacing": "Day 29 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Definition of vector (cross) product: C⃗ = A⃗ × B⃗ = (A B sin θ) n̂ with right-hand rule",
            "Properties of cross product: Non-commutative (A⃗ × B⃗ = - B⃗ × A⃗), distributive",
            "Cross product of unit vectors: î × î = 0, î × ĵ = k̂, ĵ × k̂ = î, k̂ × î = ĵ",
            "Determinant evaluation of cross product in Cartesian coordinates",
            "Geometrical meaning: Magnitude |A⃗ × B⃗| equals the area of the parallelogram formed by A⃗ and B⃗",
            "Angular displacement θ (rad), angular velocity ω = dθ/dt (rad/s), angular acceleration α = dω/dt (rad/s²)",
            "Vector relation between linear and angular velocity: v⃗ = ω⃗ × r⃗",
            "Equations of rotational motion under constant angular acceleration: ω = ω₀ + αt, θ = ω₀t + 1/2 αt², ω² = ω₀² + 2αθ",
            "Comparison table: Linear kinematics (s, u, v, a) versus Rotational kinematics (θ, ω₀, ω, α)"
        ],
        "key_concepts": [
            "Vector Cross Product Formulation & Right-Hand Rule",
            "Determinant Method for A⃗ × B⃗",
            "Linear-Angular Velocity Relation: v⃗ = ω⃗ × r⃗",
            "Rotational Kinematic Equations (Constant α)"
        ],
        "success_criteria": [
            "Compute cross product of two 3D vectors using 3x3 matrix determinant expansion",
            "Find the area of a triangle or parallelogram using cross products: Area = 1/2 |A⃗ × B⃗|",
            "Derive the vector equation v⃗ = ω⃗ × r⃗ and determine the direction of ω⃗ using right-hand screw rule",
            "Solve rotational kinematics problems for angular acceleration, total revolutions, and stopping times"
        ],
        "chapter_notes": """# CHAPTER 6: SYSTEM OF PARTICLES AND ROTATIONAL MOTION
## MODULE 3: Vector Product & Rotational Kinematics

### 1. The Vector (Cross) Product of Two Vectors
- **Definition**: The vector product of two vectors $\\vec{A}$ and $\\vec{B}$ is defined as a vector $\\vec{C} = \\vec{A} \\times \\vec{B}$ whose magnitude is:
  $$|\\vec{A} \\times \\vec{B}| = A B \\sin \\theta$$
  where $0 \\le \\theta \\le \\pi$ is the angle between $\\vec{A}$ and $\\vec{B}$, and its direction $\\hat{n}$ is perpendicular to the plane containing $\\vec{A}$ and $\\vec{B}$ according to the **Right-Hand Thumb Rule**.
  $$\\vec{A} \\times \\vec{B} = (A B \\sin \\theta) \\hat{n}$$
- **Properties**:
  1. **Anti-commutative**: $\\vec{A} \\times \\vec{B} = -(\\vec{B} \\times \\vec{A})$.
  2. **Collinear vectors**: If $\\vec{A} \\parallel \\vec{B}$ ($\\theta = 0$ or $\\pi$), $\\vec{A} \\times \\vec{B} = 0$. In particular, $\\vec{A} \\times \\vec{A} = 0$.
  3. **Unit vectors**:
     $$\\hat{i} \\times \\hat{i} = \\hat{j} \\times \\hat{j} = \\hat{k} \\times \\hat{k} = 0$$
     $$\\hat{i} \\times \\hat{j} = \\hat{k}, \\quad \\hat{j} \\times \\hat{k} = \\hat{i}, \\quad \\hat{k} \\times \\hat{i} = \\hat{j}$$
     $$\\hat{j} \\times \\hat{i} = -\\hat{k}, \\quad \\hat{k} \\times \\hat{j} = -\\hat{i}, \\quad \\hat{i} \\times \\hat{k} = -\\hat{j}$$
  4. **Component Evaluation via Determinant**:
     $$\\vec{A} \\times \\vec{B} = \\begin{vmatrix} \\hat{i} & \\hat{j} & \\hat{k} \\\\ A_x & A_y & A_z \\\\ B_x & B_y & B_z \\end{vmatrix} = \\hat{i}(A_y B_z - A_z B_y) - \\hat{j}(A_x B_z - A_z B_x) + \\hat{k}(A_x B_y - A_y B_x)$$

### 2. Angular Velocity Vector & $\\vec{v} = \\vec{\\omega} \\times \\vec{r}$
- For a rigid body rotating about a fixed axis with angular velocity $\\omega$, the vector $\\vec{\\omega}$ points along the axis of rotation in accordance with the right-hand rule.
- A particle at position $\\vec{r}$ moves in a circle of radius $r_{\\perp} = r \\sin \\theta$.
- Linear velocity magnitude: $v = \\omega r_{\\perp} = \\omega r \\sin \\theta$.
- Since $\\vec{v}$ is perpendicular to both $\\vec{\\omega}$ and $\\vec{r}$:
  $$\\vec{v} = \\vec{\\omega} \\times \\vec{r}$$

### 3. Kinematic Equations for Rotational Motion with Constant Angular Acceleration
| Linear Kinematics (Constant $a$) | Rotational Kinematics (Constant $\\alpha$) |
| :--- | :--- |
| $v = u + a t$ | $\\omega = \\omega_0 + \\alpha t$ |
| $s = u t + \\frac{1}{2} a t^2$ | $\\theta = \\omega_0 t + \\frac{1}{2} \\alpha t^2$ |
| $v^2 = u^2 + 2 a s$ | $\\omega^2 = \\omega_0^2 + 2 \\alpha \\theta$ |
| $s_n = u + \\frac{a}{2}(2n - 1)$ | $\\theta_n = \\omega_0 + \\frac{\\alpha}{2}(2n - 1)$ |
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 6.4: Find the scalar and vector products of two vectors. A⃗ = (3î - 4ĵ + 5k̂) and B⃗ = (-2î + ĵ - 3k̂).",
                "given": "A⃗ = 3î - 4ĵ + 5k̂, B⃗ = -2î + ĵ - 3k̂.",
                "formula": "A⃗ · B⃗ = A_x B_x + A_y B_y + A_z B_z; A⃗ × B⃗ = |î ĵ k̂; A_x A_y A_z; B_x B_y B_z|.",
                "substitution": "Dot product: A⃗ · B⃗ = (3)(-2) + (-4)(1) + (5)(-3) = -6 - 4 - 15 = -25. Cross product: î[(-4)(-3) - (5)(1)] - ĵ[(3)(-3) - (5)(-2)] + k̂[(3)(1) - (-4)(-2)].",
                "calculation": "î[12 - 5] - ĵ[-9 + 10] + k̂[3 - 8] = 7î - ĵ - 5k̂.",
                "finalAnswer": "Scalar product A⃗ · B⃗ = -25; Vector product A⃗ × B⃗ = 7î - ĵ - 5k̂.",
                "unit": "scalar and vector units",
                "has_diagram": True,
                "diagram_svg": mod3_svg
            },
            {
                "problem": "Textbook Example 6.5: The angular speed of a motor wheel is increased from 1200 rpm to 3120 rpm in 16 seconds. (i) What is its angular acceleration, assuming the acceleration to be uniform? (ii) How many revolutions does the engine make during this time?",
                "given": "ω₀ = 1200 rpm, ω = 3120 rpm, t = 16 s.",
                "formula": "ω₀ = 2π × (1200/60) = 40π rad/s; ω = 2π × (3120/60) = 104π rad/s; α = (ω - ω₀) / t; θ = ω₀ t + 1/2 α t²; Revolutions N = θ / (2π).",
                "substitution": "α = (104π - 40π) / 16 = 64π / 16 = 4π rad/s² ≈ 12.57 rad/s². θ = (40π)(16) + 1/2 (4π)(16)² = 640π + 512π = 1152π rad.",
                "calculation": "Revolutions N = 1152π / 2π = 576 revolutions.",
                "finalAnswer": "(i) Angular acceleration α = 4π rad s⁻² ≈ 12.6 rad s⁻²; (ii) The engine makes 576 revolutions.",
                "unit": "rad/s² and revolutions",
                "has_diagram": True,
                "diagram_svg": mod3_svg
            }
        ],
        "common_misconceptions": [
            "Treating angular displacement as a true vector: Finite angular displacements do NOT commute (θ₁ + θ₂ ≠ θ₂ + θ₁), so finite rotations are NOT vectors! However, infinitesimal angular displacements dθ DO commute and are genuine vectors."
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod3_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Right-Hand Rule for Cross Product and Rotation",
                    "diagram_title": "Vector Product Geometry and Direction of Omega",
                    "diagram_type": "svg",
                    "svg": mod3_svg,
                    "image_search_query": "cross product right hand rule angular velocity physics diagram",
                    "video_search_query": "vector product cross product class 11 physics ncert",
                    "what_to_make": "Vector A and B in plane with cross product vector perpendicular and right hand curling",
                    "what_to_explain": "Demonstrate right-hand rule and the anti-commutative nature of cross products",
                    "timing_and_cue": "Step 1 (Definition)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "What is the angle between the linear velocity vector v⃗ and the angular velocity vector ω⃗ for a particle in circular motion?",
                            "ideal_answer": "90° (they are strictly perpendicular). Since v⃗ = ω⃗ × r⃗, the resulting vector v⃗ is perpendicular to both ω⃗ (which lies along the rotation axis) and r⃗ (the position vector)!",
                            "socratic_hint": "Recall the definition of a cross product C⃗ = A⃗ × B⃗.",
                            "type": "Conceptual Reasoning"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 4: Torque & Angular Momentum
    # Date: 2026-12-11
    # -------------------------------------------------------------
    mod4_svg = sb.build_rotational_dynamics_svg(
        title="Torque τ⃗ = r⃗ × F⃗ and Angular Momentum L⃗ = r⃗ × p⃗",
        caption="Rotational analogue of force: τ = r F sin θ; Conservation of angular momentum when τ_ext = 0"
    )

    modules.append({
        "order_index": 35,
        "title": "Torque, Angular Momentum of Particles and Systems & The Law of Conservation of Angular Momentum",
        "description": "Definition of torque τ⃗ = r⃗ × F⃗ as the turning effect of force, moment of a force, angular momentum of a particle L⃗ = r⃗ × p⃗, relation between torque and rate of change of angular momentum dL⃗/dt = τ⃗_ext, and conservation of angular momentum with real-world applications.",
        "target_completion_date": "2026-12-11",
        "syllabus_pacing": "Day 30 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Torque (Moment of Force) definition: τ⃗ = r⃗ × F⃗ with SI unit N·m and dimensions [M L² T⁻²]",
            "Magnitude of torque: τ = r F sin θ = F · (r sin θ) = Force × Perpendicular lever arm distance (d_⊥)",
            "Sign convention of torque: Counter-clockwise torque is positive, clockwise torque is negative",
            "Angular Momentum of a particle: L⃗ = r⃗ × p⃗ with SI unit J·s = kg·m²/s and dimensions [M L² T⁻²]",
            "Relation between Torque and Angular Momentum: dL⃗/dt = d(r⃗ × p⃗)/dt = (dr⃗/dt × p⃗) + (r⃗ × dp⃗/dt) = (v⃗ × mv⃗) + (r⃗ × F⃗) = 0 + τ⃗ = τ⃗",
            "Angular momentum of a system of particles: L⃗_total = Σ L⃗_i; dL⃗_total/dt = τ⃗_ext (internal torques cancel)",
            "Law of Conservation of Angular Momentum: If τ⃗_ext = 0, L⃗ = constant ⇒ I₁ ω₁ = I₂ ω₂",
            "Everyday illustrations: Figure skater/ballet dancer pulling in arms, springboard diver, planetary motion at perihelion/aphelion"
        ],
        "key_concepts": [
            "Torque as Turning Effect: τ⃗ = r⃗ × F⃗",
            "Angular Momentum: L⃗ = r⃗ × p⃗",
            "Rotational Newton's Second Law: τ⃗_ext = dL⃗/dt",
            "Law of Conservation of Angular Momentum: I₁ ω₁ = I₂ ω₂"
        ],
        "success_criteria": [
            "Calculate torque using vector cross product and using perpendicular lever arm distance",
            "Prove the fundamental dynamic relation dL⃗/dt = τ⃗ from the definitions of L⃗ and p⃗",
            "State the conditions for conservation of angular momentum and apply I₁ ω₁ = I₂ ω₂ to solve numericals",
            "Explain why a spinning ballet dancer speeds up when she pulls her arms inward"
        ],
        "chapter_notes": """# CHAPTER 6: SYSTEM OF PARTICLES AND ROTATIONAL MOTION
## MODULE 4: Torque & Angular Momentum

### 1. Torque (Moment of Force)
- **Definition**: The turning or rotational effect of a force about a point or axis is called **torque** or **moment of force**.
  $$\\vec{\\tau} = \\vec{r} \\times \\vec{F}$$
- **Magnitude**:
  $$\\tau = r F \\sin \\theta = F (r \\sin \\theta) = F \\cdot d_{\\perp}$$
  where $d_{\\perp} = r \\sin \\theta$ is the **lever arm** (perpendicular distance from axis/origin to the line of action of force).
  - **SI Unit**: Newton-metre ($\\text{N}\\cdot\\text{m}$).
  - **Dimensions**: $[M L^2 T^{-2}]$ (same dimensions as energy, but torque is a vector!).

### 2. Angular Momentum of a Particle
- **Definition**: The moment of linear momentum of a particle about a reference point is defined as its **angular momentum** $\\vec{L}$:
  $$\\vec{L} = \\vec{r} \\times \\vec{p}$$
- **Magnitude**:
  $$L = r p \\sin \\theta = m v (r \\sin \\theta) = m v r_{\\perp}$$
  - **SI Unit**: Joule-second ($\\text{J}\\cdot\\text{s} = \\text{kg}\\cdot\\text{m}^2\\text{s}^{-1}$).
  - **Dimensions**: $[M L^2 T^{-1}]$.

### 3. Relation Between Torque and Angular Momentum
- Differentiating $\\vec{L} = \\vec{r} \\times \\vec{p}$ with respect to time $t$:
  $$\\frac{d\\vec{L}}{dt} = \\frac{d}{dt}(\\vec{r} \\times \\vec{p}) = \\left(\\frac{d\\vec{r}}{dt} \\times \\vec{p}\\right) + \\left(\\vec{r} \\times \\frac{d\\vec{p}}{dt}\\right)$$
- Since $\\frac{d\\vec{r}}{dt} = \\vec{v}$ and $\\vec{p} = m \\vec{v}$:
  $$\\frac{d\\vec{r}}{dt} \\times \\vec{p} = \\vec{v} \\times (m \\vec{v}) = m (\\vec{v} \\times \\vec{v}) = 0$$
- By Newton's second law, $\\frac{d\\vec{p}}{dt} = \\vec{F}$:
  $$\\vec{r} \\times \\frac{d\\vec{p}}{dt} = \\vec{r} \\times \\vec{F} = \\vec{\\tau}$$
  $$\\therefore \\vec{\\tau} = \\frac{d\\vec{L}}{dt}$$
  *The time rate of change of angular momentum of a particle is equal to the torque acting on it.* (Rotational analogue of $\\vec{F} = \\frac{d\\vec{p}}{dt}$).

### 4. Conservation of Angular Momentum
- For a system of particles, internal torques cancel in pairs ($\\sum \\vec{\\tau}_{\\text{int}} = 0$):
  $$\\frac{d\\vec{L}_{\\text{total}}}{dt} = \\vec{\\tau}_{\\text{ext}}$$
- **Principle of Conservation of Angular Momentum**:
  *If the net external torque acting on a system is zero ($\\vec{\\tau}_{\\text{ext}} = 0$), the total angular momentum of the system remains constant in magnitude and direction.*
  $$\\vec{\\tau}_{\\text{ext}} = 0 \\implies \\vec{L}_{\\text{total}} = \\text{constant}$$
- Since $L = I \\omega$:
  $$I_1 \\omega_1 = I_2 \\omega_2$$
  - When moment of inertia $I$ decreases (e.g. ballerina pulling in arms), angular speed $\\omega$ increases proportionally!
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 6.6: Show that the angular momentum about any point of a single particle moving with constant velocity remains constant throughout the motion.",
                "given": "A particle of mass m moves with constant velocity v⃗ along a straight line. Let O be any fixed origin.",
                "formula": "L⃗ = r⃗ × p⃗ = r⃗ × (m v⃗); Magnitude L = m v (r sin θ) = m v d_⊥.",
                "substitution": "Let d_⊥ be the perpendicular distance from origin O to the straight line of motion. As the particle travels along the line, the distance r and angle θ change, but the perpendicular distance d_⊥ = r sin θ remains strictly constant at all times.",
                "calculation": "Magnitude L = m v d_⊥ = constant. Direction of r⃗ × v⃗ is perpendicular to the plane containing O and the line of motion, which is also constant.",
                "finalAnswer": "Since both magnitude (m v d_⊥) and direction are invariant, the angular momentum of a particle moving with constant velocity is strictly conserved about any chosen point.",
                "unit": "J·s",
                "has_diagram": True,
                "diagram_svg": mod4_svg
            },
            {
                "problem": "Textbook Example 6.7: Find the torque of a force 7î + 3ĵ - 5k̂ about the origin. The force acts on a particle whose position vector is î - ĵ + k̂.",
                "given": "r⃗ = î - ĵ + k̂, F⃗ = 7î + 3ĵ - 5k̂.",
                "formula": "τ⃗ = r⃗ × F⃗ = |î ĵ k̂; x y z; F_x F_y F_z|.",
                "substitution": "τ⃗ = î[(-1)(-5) - (1)(3)] - ĵ[(1)(-5) - (1)(7)] + k̂[(1)(3) - (-1)(7)].",
                "calculation": "τ⃗ = î[5 - 3] - ĵ[-5 - 7] + k̂[3 + 7] = 2î - ĵ(-12) + 10k̂ = 2î + 12ĵ + 10k̂ N·m.",
                "finalAnswer": "The torque about the origin is τ⃗ = 2î + 12ĵ + 10k̂ N m.",
                "unit": "N·m",
                "has_diagram": True,
                "diagram_svg": mod4_svg
            }
        ],
        "common_misconceptions": [
            "Thinking that a straight-line moving body cannot have angular momentum: Angular momentum L = m v r_⊥ is defined about a point. As long as the line of motion does not pass through the reference origin (r_⊥ ≠ 0), a body moving in a straight line has non-zero angular momentum!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod4_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Torque and Perpendicular Lever Arm",
                    "diagram_title": "Line of Action and Lever Arm d_⊥",
                    "diagram_type": "svg",
                    "svg": mod4_svg,
                    "image_search_query": "torque line of action lever arm physics diagram",
                    "video_search_query": "torque and angular momentum class 11 physics ncert",
                    "what_to_make": "Position vector r, force vector F, and lever arm d = r sin theta",
                    "what_to_explain": "Clarify how maximizing lever arm maximizes torque with minimum applied force (e.g. door handle placed at edge)",
                    "timing_and_cue": "Step 2 (Lever Arm Application)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "A person sits on a rotating stool with weights held in outstretched hands. When he suddenly folds his hands, what happens to his angular velocity and kinetic energy?",
                            "ideal_answer": "Angular velocity increases because moment of inertia decreases and angular momentum L is conserved (I₁ ω₁ = I₂ ω₂). Rotational kinetic energy K = L² / (2I) INCREASES because I decreases! The extra kinetic energy comes from the biological internal muscular work done by the person in pulling the weights inward against centrifugal force.",
                            "socratic_hint": "Express kinetic energy in terms of angular momentum L and moment of inertia I.",
                            "type": "Application Reasoning"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 5: Equilibrium of Rigid Bodies & Principle of Moments
    # Date: 2026-12-11
    # -------------------------------------------------------------
    mod5_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 10), range_y=(0, 10),
        lines=[
            {"p1": (1, 5), "p2": (9, 5), "color": "#334155", "stroke_width": 3, "label": "Lever Bar (Length L)"},
            {"p1": (5, 5), "p2": (5, 3), "color": "#D97706", "stroke_width": 2, "label": "Fulcrum F"}
        ],
        points=[
            {"x": 2, "y": 5, "color": "#2563EB", "label": "Load W (Load Arm d₁)"},
            {"x": 8, "y": 5, "color": "#16A34A", "label": "Effort F (Effort Arm d₂)"}
        ],
        x_label="Beam Span x (m)", y_label="Load Position",
        title="Principle of Moments: Load × Load Arm = Effort × Effort Arm",
        caption="Conditions for complete mechanical equilibrium: Translational (Σ F = 0) and Rotational (Σ τ = 0)"
    )

    modules.append({
        "order_index": 36,
        "title": "Equilibrium of Rigid Bodies, Principle of Moments, Center of Gravity & Couples",
        "description": "Conditions for mechanical equilibrium of a rigid body (translational Σ F⃗ = 0 and rotational Σ τ⃗ = 0), principle of moments, mechanical advantage of levers, definition and distinction between Center of Gravity and Center of Mass, and mechanics of couples.",
        "target_completion_date": "2026-12-11",
        "syllabus_pacing": "Day 30 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Conditions for mechanical equilibrium: Complete equilibrium requires both translational and rotational equilibrium",
            "Translational equilibrium: Net external force is zero Σ F⃗_ext = 0 (linear momentum is constant)",
            "Rotational equilibrium: Net external torque about any point is zero Σ τ⃗_ext = 0 (angular momentum is constant)",
            "Partial equilibrium: A system in translational equilibrium but not rotational, or vice versa",
            "Couple: A pair of equal and opposite forces whose lines of action do not coincide",
            "Moment of a couple: τ_couple = Force × Arm of couple (independent of reference point)",
            "Principle of Moments for levers: In equilibrium, Sum of anticlockwise moments = Sum of clockwise moments",
            "Mechanical Advantage (MA) = Load / Effort = Effort arm / Load arm",
            "Center of Gravity (CG): Point through which the resultant gravitational force (weight) acts",
            "Equivalence and distinction between CG and CM (identical only in uniform gravitational fields)"
        ],
        "key_concepts": [
            "Translational Equilibrium: Σ F⃗ = 0",
            "Rotational Equilibrium: Σ τ⃗ = 0",
            "Principle of Moments & Mechanical Advantage",
            "Couple & Independence of Origin",
            "Center of Gravity vs Center of Mass"
        ],
        "success_criteria": [
            "Set up and solve simultaneous equations for both translational and rotational equilibrium",
            "Calculate reaction forces at pivots and supports for loaded beams and inclined ladders",
            "Define a couple and prove mathematically that its moment is independent of the point of calculation",
            "Explain under what condition Center of Gravity fails to coincide with Center of Mass (huge celestial objects)"
        ],
        "chapter_notes": """# CHAPTER 6: SYSTEM OF PARTICLES AND ROTATIONAL MOTION
## MODULE 5: Equilibrium of Rigid Bodies & Principle of Moments

### 1. Conditions for Mechanical Equilibrium
A rigid body is in **complete mechanical equilibrium** if both its linear momentum and angular momentum are constant with time:
1. **Translational Equilibrium**: The vector sum of all external forces acting on the body must be zero:
   $$\\sum_{i=1}^n \\vec{F}_i = 0 \\implies \\sum F_x = 0, \\quad \\sum F_y = 0, \\quad \\sum F_z = 0$$
2. **Rotational Equilibrium**: The vector sum of all external torques acting on the body about any reference point must be zero:
   $$\\sum_{i=1}^n \\vec{\\tau}_i = 0 \\implies \\sum \\tau_x = 0, \\quad \\sum \\tau_y = 0, \\quad \\sum \\tau_z = 0$$

### 2. The Principle of Moments & Levers
- An ideal lever is a light rod pivoted at a point along its length called the **fulcrum** $F$.
- Let a load $W = F_1$ act at distance $d_1$ (load arm) and effort $P = F_2$ act at distance $d_2$ (effort arm) from the fulcrum.
- For rotational equilibrium about the fulcrum:
  $$\\sum \\tau = F_1 d_1 - F_2 d_2 = 0 \\implies F_1 d_1 = F_2 d_2$$
  $$\\text{Load} \\times \\text{Load Arm} = \\text{Effort} \\times \\text{Effort Arm}$$
- **Mechanical Advantage (MA)**:
  $$\\text{MA} = \\frac{\\text{Load}}{\\text{Effort}} = \\frac{F_1}{F_2} = \\frac{d_2}{d_1}$$
  If effort arm $d_2 > d_1$, $\\text{MA} > 1$, and a small effort lifts a large load!

### 3. Couples
- **Couple**: A pair of equal and opposite forces acting along two parallel, non-coinciding lines of action.
- Examples: Turning a water tap, opening a bottle cap, turning a car steering wheel with two hands.
- **Key Theorem**: *The moment of a couple is independent of the reference origin.*
  $$\\vec{\\tau}_{\\text{couple}} = \\vec{r}_1 \\times \\vec{F}_1 + \\vec{r}_2 \\times \\vec{F}_2 = \\vec{r}_1 \\times \\vec{F} + \\vec{r}_2 \\times (-\\vec{F}) = (\\vec{r}_1 - \\vec{r}_2) \\times \\vec{F} = \\vec{r}_{12} \\times \\vec{F}$$
  where $\\vec{r}_{12}$ is the vector connecting the points of application. Magnitude $= F \\times d_{\\perp}$.

### 4. Center of Gravity vs. Center of Mass
- **Center of Mass (CM)**: Point determined solely by the mass distribution of the body ($\\vec{R}_{\\text{cm}} = \\frac{1}{M}\\int \\vec{r} dm$). Independent of gravitational field.
- **Center of Gravity (CG)**: Point at which the total gravitational torque on the body vanishes: $\\sum \\vec{r}_i \\times m_i \\vec{g} = 0$.
- **When they coincide**: In a uniform gravitational field (where $\\vec{g}$ is identical at all points of the body), CG coincides exactly with CM!
- **When they diverge**: For an extremely large body (e.g. a tall mountain or space elevator stretching thousands of kilometers into space where $\\vec{g}$ varies with altitude), CG lies slightly below CM!
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 6.8: A 3 m long ladder weighing 20 kg leans on a frictionless wall. Its feet rest on the floor 1 m from the wall as shown in Fig. 6.8. Find the reaction forces of the wall and the floor.",
                "given": "Length L = 3 m, mass m = 20 kg ⇒ Weight W = mg = 20 × 9.8 = 196 N acting at midpoint of ladder (L/2 = 1.5 m). Distance from wall d = 1 m. Height of wall contact h = √(3² - 1²) = √8 = 2√2 ≈ 2.83 m. Wall is frictionless (normal reaction F₁ horizontal). Floor has friction: reaction F₂ has vertical component N and horizontal component f.",
                "formula": "Translational equilibrium: Σ F_x = 0 ⇒ F₁ = f; Σ F_y = 0 ⇒ N = W. Rotational equilibrium about bottom of ladder A: Σ τ_A = 0 ⇒ F₁ · h - W · (d/2) = 0.",
                "substitution": "N = W = 196 N. F₁ (2.83 m) - (196 N)(0.5 m) = 0 ⇒ 2.83 F₁ = 98 ⇒ F₁ = 98 / 2.83 ≈ 34.6 N. Horizontal friction at floor f = F₁ = 34.6 N.",
                "calculation": "Total reaction force of floor F₂ = √(N² + f²) = √(196² + 34.6²) = √(38416 + 1197) = √39613 ≈ 199 N. Angle with floor: tan θ = N / f = 196 / 34.6 ≈ 5.66 ⇒ θ ≈ 80°.",
                "finalAnswer": "Reaction force of the wall is 34.6 N (horizontal); Reaction force of the floor is 199 N directed at 80° to the horizontal.",
                "unit": "Newtons (N)",
                "has_diagram": True,
                "diagram_svg": mod5_svg
            }
        ],
        "common_misconceptions": [
            "Assuming CG and CM are identical under all circumstances: While practically identical for laboratory scale objects, for massive bodies extending across non-uniform gravity fields, CG is pulled closer to the stronger gravitational field and sits below CM."
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod5_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Ladder Equilibrium and Wall Reaction",
                    "diagram_title": "Ladder Leaning on Frictionless Wall",
                    "diagram_type": "svg",
                    "svg": mod5_svg,
                    "image_search_query": "ladder leaning against wall forces equilibrium physics diagram",
                    "video_search_query": "equilibrium of rigid body ladder problem class 11 physics",
                    "what_to_make": "Ladder leaning on wall showing F_wall, N_floor, f_floor, and weight mg at center",
                    "what_to_explain": "Demonstrate the setup of translational equations Σ F_x = 0, Σ F_y = 0 and rotational equation Σ τ = 0",
                    "timing_and_cue": "Step 2 (Board Problem)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "Can a body be in translational equilibrium without being in rotational equilibrium?",
                            "ideal_answer": "Yes. A couple (two equal and opposite forces with parallel non-coinciding lines of action) has net force Σ F = 0 (translational equilibrium), but net torque Σ τ ≠ 0 (pure rotational acceleration). For example, turning a steering wheel with two hands!",
                            "socratic_hint": "Consider the net force and net torque produced by a couple.",
                            "type": "Conceptual Reasoning"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 6: Moment of Inertia, Theorems & Pure Rolling Motion
    # Date: 2026-12-12
    # -------------------------------------------------------------
    mod6_svg = sb.build_rotational_dynamics_svg(
        title="Moment of Inertia, Radius of Gyration & Rolling Motion",
        caption="Pure rolling: v_cm = ω R; Total KE = ½ M v_cm² (1 + k²/R²)"
    )

    modules.append({
        "order_index": 37,
        "title": "Moment of Inertia, Radius of Gyration, Axis Theorems & Mechanics of Pure Rolling Motion",
        "description": "Moment of inertia as rotational mass I = Σ m_i r_i² = ∫ r² dm, radius of gyration k, parallel and perpendicular axis theorems, standard moments of inertia for regular solids, and dynamics of pure rolling motion without slipping on horizontal and inclined planes.",
        "target_completion_date": "2026-12-12",
        "syllabus_pacing": "Day 31 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Moment of Inertia (Rotational Inertia): Definition I = Σ m_i r_i² with SI unit kg·m² and dimensions [M L² T⁰]",
            "Physical meaning: Resistance of a body to rotational acceleration about a given axis (depends on mass, shape, and axis position)",
            "Radius of Gyration k: Effective distance from axis where entire mass can be concentrated I = M k² ⇒ k = √(I/M)",
            "Perpendicular Axis Theorem (for planar laminae): I_z = I_x + I_y",
            "Parallel Axis Theorem: I = I_cm + M d²",
            "Standard Moments of Inertia: Thin ring (MR²), Circular disc (1/2 MR²), Solid cylinder (1/2 MR²), Hollow cylinder (MR²), Solid sphere (2/5 MR²), Hollow sphere (2/3 MR²), Thin rod (1/12 ML²)",
            "Kinematics of pure rolling without slipping: v_cm = ω R and a_cm = α R",
            "Total kinetic energy in pure rolling: K = K_trans + K_rot = 1/2 M v_cm² + 1/2 I_cm ω² = 1/2 M v_cm² (1 + k²/R²)",
            "Acceleration of rolling body down an inclined plane: a = (g sin θ) / (1 + k²/R²)",
            "Minimum coefficient of friction required for pure rolling: μ_min = [tan θ · (k²/R²)] / [1 + (k²/R²)]"
        ],
        "key_concepts": [
            "Moment of Inertia: I = ∫ r² dm",
            "Radius of Gyration: k = √(I/M)",
            "Parallel Axis Theorem: I = I_cm + M d²",
            "Pure Rolling Kinetic Energy: K = ½ M v_cm² (1 + k²/R²)",
            "Incline Acceleration Hierarchy: Solid Sphere > Disc/Cylinder > Ring/Hollow Cylinder"
        ],
        "success_criteria": [
            "State and apply the parallel and perpendicular axis theorems to calculate moments of inertia about arbitrary axes",
            "Calculate radius of gyration for standard geometric solids",
            "Derive the total kinetic energy equation for rolling without slipping",
            "Rank the acceleration and velocity of rolling bodies (sphere, disc, ring) down an inclined plane"
        ],
        "chapter_notes": """# CHAPTER 6: SYSTEM OF PARTICLES AND ROTATIONAL MOTION
## MODULE 6: Moment of Inertia, Theorems & Pure Rolling

### 1. Moment of Inertia ($I$) & Radius of Gyration ($k$)
- **Moment of Inertia**: The rotational analogue of mass in linear motion. It measures the body's inertia against angular acceleration.
  $$I = \\sum_{i=1}^n m_i r_i^2 = \\int r^2 dm$$
  where $r$ is the perpendicular distance of the mass element $dm$ from the chosen axis of rotation.
  - **SI Unit**: $\\text{kg}\\cdot\\text{m}^2$.
  - **Dimensions**: $[M L^2 T^0]$.
- **Radius of Gyration ($k$)**: The distance from the axis of rotation at which the entire mass $M$ of the body could be concentrated without altering its moment of inertia:
  $$I = M k^2 \\implies k = \\sqrt{\\frac{I}{M}}$$

### 2. Theorems of Moment of Inertia
1. **Perpendicular Axis Theorem** (Applies strictly to planar laminae in the xy-plane):
   $$I_z = I_x + I_y$$
2. **Parallel Axis Theorem** (Applies to any body of arbitrary shape):
   $$I = I_{\\text{cm}} + M d^2$$
   where $I_{\\text{cm}}$ is the moment of inertia about a parallel axis passing through the center of mass, and $d$ is the perpendicular distance between the two axes.

### 3. Standard Moments of Inertia Table
| Body | Axis of Rotation | Moment of Inertia ($I$) | $k^2 / R^2$ |
| :--- | :--- | :--- | :--- |
| **Thin Circular Ring** | Central axis $\\perp$ to plane | $M R^2$ | $1$ |
| **Thin Circular Ring** | Diameter axis | $\\frac{1}{2} M R^2$ | $1/2$ |
| **Circular Disc** | Central axis $\\perp$ to plane | $\\frac{1}{2} M R^2$ | $1/2$ |
| **Circular Disc** | Diameter axis | $\\frac{1}{4} M R^2$ | $1/4$ |
| **Solid Cylinder** | Longitudinal axis | $\\frac{1}{2} M R^2$ | $1/2$ |
| **Hollow Cylinder** | Longitudinal axis | $M R^2$ | $1$ |
| **Solid Sphere** | Any diameter axis | $\\frac{2}{5} M R^2$ | $2/5 = 0.4$ |
| **Hollow Sphere (Shell)** | Any diameter axis | $\\frac{2}{3} M R^2$ | $2/3 \\approx 0.67$ |
| **Thin Rod (Length $L$)** | $\\perp$ to rod at center | $\\frac{1}{12} M L^2$ | $k^2 = L^2/12$ |
| **Thin Rod (Length $L$)** | $\\perp$ to rod at one end | $\\frac{1}{3} M L^2$ | $k^2 = L^2/3$ |

### 4. Mechanics of Pure Rolling Motion (Without Slipping)
- A body of radius $R$ rolling on a stationary surface undergoes simultaneous translation of center of mass and rotation about the center of mass.
  - Condition for rolling without slipping at point of contact: $v_{\\text{contact}} = v_{\\text{cm}} - \\omega R = 0 \\implies v_{\\text{cm}} = \\omega R$.
  - Acceleration relation: $a_{\\text{cm}} = \\alpha R$.
- **Total Kinetic Energy**:
  $$K = K_{\\text{trans}} + K_{\\text{rot}} = \\frac{1}{2} M v_{\\text{cm}}^2 + \\frac{1}{2} I_{\\text{cm}} \\omega^2 = \\frac{1}{2} M v_{\\text{cm}}^2 + \\frac{1}{2} (M k^2) \\left(\\frac{v_{\\text{cm}}}{R}\\right)^2$$
  $$K = \\frac{1}{2} M v_{\\text{cm}}^2 \\left(1 + \\frac{k^2}{R^2}\\right)$$
- **Acceleration Down an Inclined Plane of Angle $\\theta$**:
  $$a = \\frac{g \\sin \\theta}{1 + \\frac{k^2}{R^2}}$$
- **Velocity at Bottom of Incline of Height $h$**:
  $$v = \\sqrt{\\frac{2gh}{1 + \\frac{k^2}{R^2}}}$$
- **The Great Race Down the Incline**:
  Smaller $\\frac{k^2}{R^2}$ means greater acceleration and velocity!
  $$\\text{Solid Sphere } \\left(\\frac{k^2}{R^2} = 0.4\\right) > \\text{Disc } (0.5) > \\text{Hollow Sphere } (0.67) > \\text{Ring } (1.0)$$
  *The solid sphere always wins the race, and the ring arrives last!*
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 6.9: What is the moment of inertia of a disc of mass M and radius R about any of its diameter?",
                "given": "Circular disc of mass M, radius R.",
                "formula": "Perpendicular Axis Theorem: I_z = I_x + I_y. By symmetry, moments of inertia about any two perpendicular diameters in the plane are identical: I_x = I_y = I_d. Known: I_z = 1/2 M R².",
                "substitution": "I_z = I_d + I_d = 2 I_d ⇒ 2 I_d = 1/2 M R².",
                "calculation": "I_d = 1/4 M R².",
                "finalAnswer": "The moment of inertia of a circular disc about any diameter is 1/4 M R².",
                "unit": "kg·m²",
                "has_diagram": True,
                "diagram_svg": mod6_svg
            },
            {
                "problem": "Textbook Example 6.10: What is the moment of inertia of a uniform rod of mass M and length L about an axis perpendicular to the rod and passing through one of its ends?",
                "given": "Uniform rod of mass M, length L. COM is at midpoint (d = L/2). Known: I_cm = 1/12 M L².",
                "formula": "Parallel Axis Theorem: I = I_cm + M d².",
                "substitution": "I = 1/12 M L² + M (L/2)² = 1/12 M L² + 1/4 M L² = (1/12 + 3/12) M L² = 4/12 M L².",
                "calculation": "I = 1/3 M L².",
                "finalAnswer": "The moment of inertia about an end perpendicular axis is 1/3 M L².",
                "unit": "kg·m²",
                "has_diagram": True,
                "diagram_svg": mod6_svg
            }
        ],
        "common_misconceptions": [
            "Assuming rolling friction does work against the kinetic energy of a rolling body: In pure rolling without slipping, the instantaneous contact point is at rest relative to the ground (v_contact = 0). Thus static friction does zero work! It merely enforces the constraint v_cm = ω R."
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod6_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Pure Rolling Velocity Profile",
                    "diagram_title": "Superposition of Translation and Rotation",
                    "diagram_type": "svg",
                    "svg": mod6_svg,
                    "image_search_query": "rolling without slipping velocity vectors contact point physics diagram",
                    "video_search_query": "rolling motion inclined plane class 11 physics ncert",
                    "what_to_make": "Wheel rolling showing v = 2 v_cm at top, v = v_cm at center, and v = 0 at contact point",
                    "what_to_explain": "Demonstrate why the instantaneous point of contact has zero velocity",
                    "timing_and_cue": "Step 2 (Kinematics Formulation)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "A solid cylinder and a hollow cylinder of identical mass and radius are rolled down an inclined plane from rest. Which one reaches the bottom first?",
                            "ideal_answer": "The solid cylinder reaches first! Its moment of inertia is smaller (I = 1/2 M R², k²/R² = 0.5) compared to the hollow cylinder (I = M R², k²/R² = 1.0). Acceleration is a = (g sin θ) / (1 + k²/R²), so the solid cylinder has acceleration a = 2/3 g sin θ while the hollow cylinder has only a = 1/2 g sin θ.",
                            "socratic_hint": "Compare the k²/R² values for solid vs hollow cylinders.",
                            "type": "Board Exam Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 7: Master NCERT Exercise Solver (Ex 6.1 to 6.21)
    # Date: 2026-12-12
    # -------------------------------------------------------------
    mod7_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 10), range_y=(0, 20),
        lines=[{"p1": (0, 0), "p2": (8, 16), "color": "#2563EB", "stroke_width": 2.5, "label": "NCERT Rotational Solver"}],
        x_label="Exercise Problem Index", y_label="Solution Complexity",
        title="Chapter 6: NCERT Exercises 6.1 to 6.21 Step-by-Step Solver",
        caption="Full board-exam step-by-step numerical and conceptual solutions"
    )

    modules.append({
        "order_index": 38,
        "title": "Master NCERT Exercise Solver: Step-by-Step Solutions for Exercises 6.1 through 6.21",
        "description": "Comprehensive, rigorous step-by-step solutions for all NCERT Chapter 6 exercise problems (Ex 6.1 to 6.21) covering center of mass, vector cross products, rotational kinematics, equilibrium of ladders and bars, moments of inertia, and pure rolling mechanics.",
        "target_completion_date": "2026-12-12",
        "syllabus_pacing": "Day 31 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 60,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Exercise 6.1: Location of center of mass of sphere, cylinder, ring, and cubical box",
            "Exercise 6.2: Position of center of mass of HCl molecule given atomic masses and bond length",
            "Exercise 6.3: Velocity of center of mass of a system of particles under external and internal forces",
            "Exercise 6.4: Proof of scalar and vector identities in rotational coordinates",
            "Exercise 6.5: Angular velocity and acceleration of automobile wheels during braking",
            "Exercise 6.6 to 6.11: Levers, torque balance, and reactions at pivot supports",
            "Exercise 6.12 to 6.16: Moments of inertia of composite bodies using axis theorems",
            "Exercise 6.17 to 6.21: Rolling down inclines, kinetic energy partitions, and friction requirements"
        ],
        "key_concepts": [
            "Ex 6.1 to 6.3: Center of Mass Locations & Invariants",
            "Ex 6.4 to 6.7: Vector Operations & Angular Acceleration",
            "Ex 6.8 to 6.11: Equilibrium & Principle of Moments",
            "Ex 6.12 to 6.16: Axis Theorems & MOI Computations",
            "Ex 6.17 to 6.21: Rolling Dynamics & Incline Races"
        ],
        "success_criteria": [
            "Solve every NCERT exercise question step-by-step with Given, Formula, Substitution, and Units",
            "Calculate HCl center of mass offset accurately: x_cm = [m_Cl / (m_H + m_Cl)] d",
            "Apply the parallel axis theorem to compound objects (e.g. discs with holes or off-center pivots)",
            "Determine the fraction of kinetic energy that is rotational vs translational in rolling bodies"
        ],
        "chapter_notes": """# CHAPTER 6: SYSTEM OF PARTICLES AND ROTATIONAL MOTION
## MODULE 7: Master NCERT Exercise Solver (Ex 6.1 to 6.21)

### NCERT Exercise Solutions Overview
This module contains complete, board-exam compliant solutions for all 21 exercise problems from NCERT Chapter 6: System of Particles and Rotational Motion.
- **Exercises 6.1 - 6.3**: Geometric symmetry of center of mass, molecular diatomic centers of mass.
- **Exercises 6.4 - 6.7**: Angular kinematics, RPM to rad/s conversions, vector cross product identities.
- **Exercises 6.8 - 6.11**: Rigid body static equilibrium, levers, weighing scales, and ladder reaction forces.
- **Exercises 6.12 - 6.16**: Moments of inertia using parallel and perpendicular axis theorems.
- **Exercises 6.17 - 6.21**: Pure rolling on horizontal and inclined planes, energy partition ratios.
""",
        "worked_examples": [
            {
                "problem": "NCERT Exercise 6.1: Give the location of the centre of mass of a (i) sphere, (ii) cylinder, (iii) ring, and (iv) cube, each of uniform mass density. Does the centre of mass of a body necessarily lie inside the body?",
                "given": "Four geometric bodies of uniform mass density.",
                "formula": "By symmetry principles, for any body of uniform density with geometric symmetry, the center of mass coincides with its geometric center.",
                "substitution": "(i) Sphere: At the geometric center of the sphere. (ii) Cylinder: At the midpoint of the longitudinal central axis of the cylinder. (iii) Ring: At the geometric center of the ring. (iv) Cube: At the point of intersection of the body diagonals of the cube.",
                "calculation": "No, the center of mass does not necessarily lie inside the body. In the case of a ring, hollow cylinder, hollow sphere, or hollow box, the center of mass lies in empty space where there is no physical material!",
                "finalAnswer": "(i) Geometric center; (ii) Midpoint of axis; (iii) Geometric center; (iv) Center of cube. The COM does NOT necessarily lie inside the material of the body (e.g. ring).",
                "unit": "geometric locations",
                "has_diagram": True,
                "diagram_svg": mod7_svg
            },
            {
                "problem": "NCERT Exercise 6.2: In the HCl molecule, the separation between the nuclei of the two atoms is about 1.27 Å (1 Å = 10⁻¹⁰ m). Find the approximate location of the CM of the molecule, given that a chlorine atom is about 35.5 times as massive as a hydrogen atom and nearly all the mass of an atom is concentrated in its nucleus.",
                "given": "d = 1.27 Å, m_H = 1 unit, m_Cl = 35.5 units.",
                "formula": "Taking hydrogen atom as origin (x_H = 0): X_cm = (m_H x_H + m_Cl x_Cl) / (m_H + m_Cl) = (m_Cl · d) / (m_H + m_Cl).",
                "substitution": "X_cm = (35.5 × 1.27 Å) / (1 + 35.5) = (45.085) / 36.5 ≈ 1.235 Å.",
                "calculation": "X_cm ≈ 1.24 Å from the hydrogen atom.",
                "finalAnswer": "The center of mass of the HCl molecule is located approximately 1.24 Å from the hydrogen nucleus (or 0.035 Å from the chlorine nucleus).",
                "unit": "Ångströms (Å)",
                "has_diagram": True,
                "diagram_svg": mod7_svg
            }
        ],
        "common_misconceptions": [
            "Thinking that center of mass is equidistant between two particles: The center of mass is strictly weighted by mass! In HCl, because chlorine is 35.5 times heavier than hydrogen, the center of mass is situated right next to the chlorine atom (over 97% of the distance toward Cl)!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod7_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "HCl Molecular Center of Mass Offset",
                    "diagram_title": "Diatomic Molecule Center of Mass",
                    "diagram_type": "svg",
                    "svg": mod7_svg,
                    "image_search_query": "hcl molecule center of mass distance chlorine hydrogen diagram",
                    "video_search_query": "center of mass hcl molecule ncert exercise 6.2",
                    "what_to_make": "Small H sphere and massive Cl sphere with COM marked near Cl",
                    "what_to_explain": "Explain the inverse mass ratio principle m1 r1 = m2 r2",
                    "timing_and_cue": "Step 2 (Board Problem)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "What percentage of total kinetic energy is rotational for a uniform solid sphere rolling without slipping on a horizontal floor?",
                            "ideal_answer": "Approximately 28.6% (2/7 of total). For a solid sphere, K_rot = 1/2 I ω² = 1/2 (2/5 M R²) (v/R)² = 1/5 M v². K_trans = 1/2 M v². Total K = 1/2 M v² + 1/5 M v² = 7/10 M v². Fraction rotational = (1/5) / (7/10) = 2/7 ≈ 28.57%!",
                            "socratic_hint": "Find the ratio K_rot / K_total using I = 2/5 M R².",
                            "type": "Board Exam Numerical"
                        }
                    ]
                }
            ]
        }
    })

    return modules
