"""
ch3_motion_in_a_plane.py
CBSE Class 11 Physics - Chapter 3: Motion in a Plane
Part 1 (Mid-Term Syllabus, Unit II: Kinematics)
Target Pacing: November 22, 2026 to November 27, 2026 (7 Modules, 6 Days)
"""

import sys
import os
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

import svg_builder_physics11 as sb

CURRICULUM_ID = "c11_phy_ch03_motion_in_a_plane"
CLASS_LEVEL = "Class 11"
BOARD = "CBSE"
SUBJECT = "Physics"

def get_modules():
    modules = []

    # -------------------------------------------------------------
    # MODULE 1: Scalars, Vectors, Vector Algebra & Parallelogram Law
    # Date: 2026-11-22
    # -------------------------------------------------------------
    mod1_svg = sb.build_vector_addition_resolution_svg(variant="addition", title="Vector Addition: Parallelogram Law", caption="Resultant R = √(A² + B² + 2AB cos θ); tan α = (B sin θ)/(A + B cos θ)")
    modules.append({
        "order_index": 12,
        "title": "Vector Foundations: Scalars vs Vectors, Triangle & Parallelogram Laws of Addition",
        "description": "Distinction between scalar and vector quantities, geometric representation, null vector, vector equality, triangle law, and analytical derivation of parallelogram law of vector addition.",
        "target_completion_date": "2026-11-22",
        "syllabus_pacing": "Day 11 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Definition of scalars (magnitude only) and vectors (magnitude, direction, obeys vector addition laws)",
            "Why physical quantities with direction (like electric current, pressure) are NOT vectors",
            "Position vector r⃗ and displacement vector Δr⃗ in a 2D Cartesian plane",
            "Equality of vectors, negative of a vector, and multiplication of a vector by a real number",
            "The Zero (Null) vector: Definition, physical significance, and mathematical properties",
            "Triangle Law of Vector Addition (head-to-tail graphical rule)",
            "Parallelogram Law of Vector Addition: Analytical derivation of magnitude and direction of resultant",
            "Special cases: Vectors in same direction (θ=0°), opposite direction (θ=180°), perpendicular (θ=90°)"
        ],
        "key_concepts": [
            "Scalars vs Vectors Criteria",
            "Position & Displacement Vectors in 2D",
            "Parallelogram Law Analytical Derivation",
            "Null Vector Properties (A⃗ + 0⃗ = A⃗, λ 0⃗ = 0⃗)"
        ],
        "success_criteria": [
            "State why electric current is a scalar despite possessing a directional flow",
            "Derive R = √(A² + B² + 2AB cos θ) and tan α = (B sin θ)/(A + B cos θ) from geometric constructions",
            "Calculate the resultant of two forces or velocities acting at arbitrary angles",
            "Demonstrate commutative and associative laws of vector addition"
        ],
        "chapter_notes": """# CHAPTER 3: MOTION IN A PLANE
## MODULE 1: Vectors & Vector Addition

### 1. Scalars vs. Vectors
- **Scalar**: A physical quantity specified completely by its magnitude and unit (Mass, Time, Speed, Work, Electric Current).
- **Vector**: A physical quantity that has both magnitude and direction AND obeys the laws of vector addition (Displacement, Velocity, Force, Linear Momentum).
*Why is Electric Current a scalar?* Electric current has a specified direction of flow, but current at a junction obeys algebraic Kirchhoff's law ($I = I_1 + I_2$), NOT the vector parallelogram law!

### 2. Analytical Treatment of Parallelogram Law
Let two vectors $\\vec{A}$ and $\\vec{B}$ be represented in magnitude and direction by two adjacent sides $OP$ and $OQ$ of parallelogram $OPRQ$, with angle $\\theta$ between them.
Drop perpendicular $RN$ from $R$ to the extension of line $OP$:
- In right $\\triangle RNP$:
  $$PN = B \\cos \\theta, \\quad RN = B \\sin \\theta$$
- In right $\\triangle ONR$:
  $$OR^2 = ON^2 + NR^2 = (OP + PN)^2 + NR^2$$
  $$R^2 = (A + B \\cos \\theta)^2 + (B \\sin \\theta)^2 = A^2 + 2AB \\cos \\theta + B^2 (\\cos^2 \\theta + \\sin^2 \\theta)$$
$$R = \\sqrt{A^2 + B^2 + 2 A B \\cos \\theta}$$

- **Direction of Resultant (Angle $\\alpha$ with vector $\\vec{A}$)**:
  $$\\tan \\alpha = \\frac{RN}{ON} = \\frac{B \\sin \\theta}{A + B \\cos \\theta}$$

### 3. Special Cases
1. **Parallel Vectors ($\\theta = 0^\\circ$)**: $\\cos 0^\\circ = 1 \\implies R_{\\text{max}} = A + B$.
2. **Anti-parallel Vectors ($\\theta = 180^\\circ$)**: $\\cos 180^\\circ = -1 \\implies R_{\\text{min}} = |A - B|$.
3. **Perpendicular Vectors ($\\theta = 90^\\circ$)**: $\\cos 90^\\circ = 0 \\implies R = \\sqrt{A^2 + B^2}$, $\\tan \\alpha = B/A$.
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 3.1: Rain is falling vertically with a speed of 35 m s⁻¹. Winds starts blowing after sometime with a speed of 12 m s⁻¹ in east to west direction. In which direction should a boy waiting at a bus stop hold his umbrella?",
                "given": "Velocity of rain v_r = 35 m/s vertically downwards; Velocity of wind v_w = 12 m/s east to west.",
                "formula": "Relative velocity of rain with respect to stationary boy is v = v_r + v_w. tan θ = v_w / v_r.",
                "substitution": "tan θ = (12 m/s) / (35 m/s) = 0.3429 => θ = tan⁻¹(0.3429) ≈ 19°.",
                "calculation": "Magnitude v = √[(35)² + (12)²] = √[1225 + 144] = √1369 = 37 m/s. Direction θ = 19° with the vertical towards the west.",
                "finalAnswer": "The boy should hold his umbrella at an angle of about 19° with the vertical towards the direction from which wind is blowing (towards the west).",
                "unit": "degrees",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            }
        ],
        "common_misconceptions": [
            "Adding vectors algebraically like numbers: |A⃗ + B⃗| is NOT |A⃗| + |B⃗| unless the angle between them is strictly zero!",
            "Confusing angle with A versus angle with B: tan α = (B sin θ)/(A + B cos θ) gives the angle relative to vector A. The vector in the denominator without the trig function is the reference vector."
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod1_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Parallelogram Law Analytical Derivation",
                    "diagram_title": "Geometric Right Triangle Construction for Resultant Vector R",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "parallelogram law of vector addition derivation diagram",
                    "video_search_query": "parallelogram law of vectors analytical derivation class 11",
                    "what_to_make": "Parallelogram OPRQ with perpendicular RN and angle alpha annotations",
                    "what_to_explain": "Walk through Pythagoras theorem on triangle ONR step-by-step",
                    "timing_and_cue": "Step 2 (Analytical Proof)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "Two vectors of equal magnitude P act at an angle θ. What must be the angle θ so that their resultant also has magnitude P?",
                            "ideal_answer": "R² = P² + P² + 2P² cos θ => P² = 2P²(1 + cos θ) => 1 = 2(1 + cos θ) => 1 + cos θ = 1/2 => cos θ = -1/2 => θ = 120°.",
                            "socratic_hint": "Substitute R = P and A = B = P into the parallelogram formula.",
                            "type": "Board Numerical"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 2: Resolution of Vectors & Unit Vectors
    # Date: 2026-11-23
    # -------------------------------------------------------------
    mod2_svg = sb.build_vector_addition_resolution_svg(variant="resolution", title="Orthogonal Resolution of a Vector", caption="A⃗ = A_x î + A_y ĵ; A_x = A cos θ, A_y = A sin θ")
    modules.append({
        "order_index": 13,
        "title": "Resolution of Vectors in a Plane: Unit Vectors, Rectangular Components & 3D Generalization",
        "description": "Decomposition of vectors into mutually perpendicular rectangular components, unit vectors î, ĵ, k̂, vector magnitude formula, direction cosines, and algebraic vector addition by components.",
        "target_completion_date": "2026-11-23",
        "syllabus_pacing": "Day 12 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Need for resolution: Splitting a single force or velocity into independent orthogonal effects",
            "Concept and definition of a Unit Vector (n̂ = A⃗ / |A⃗|)",
            "Cartesian base unit vectors î, ĵ, k̂ along X, Y, Z axes",
            "Rectangular components in a plane: A_x = A cos θ and A_y = A sin θ",
            "Reconstruction of vector from components: |A⃗| = √(A_x² + A_y²) and tan θ = A_y / A_x",
            "3D Vector representation: A⃗ = A_x î + A_y ĵ + A_z k̂ and magnitude √(A_x² + A_y² + A_z²)",
            "Direction cosines (cos α, cos β, cos γ) and the identity cos² α + cos² β + cos² γ = 1",
            "Adding multiple vectors analytically using components: R_x = Σ A_xi, R_y = Σ A_yi"
        ],
        "key_concepts": [
            "Unit Vectors (î, ĵ, k̂)",
            "Orthogonal Rectangular Components (A_x, A_y)",
            "Direction Cosines Identity cos²α + cos²β + cos²γ = 1",
            "Component Method of Vector Addition"
        ],
        "success_criteria": [
            "Resolve any vector inclined at angle θ into horizontal and vertical components",
            "Write vectors in terms of unit vectors î, ĵ, k̂",
            "Prove that the sum of the squares of direction cosines equals 1",
            "Add three or more coplanar forces by resolving each along X and Y axes"
        ],
        "chapter_notes": """# CHAPTER 3: MOTION IN A PLANE
## MODULE 2: Vector Resolution & Component Algebra

### 1. Unit Vectors
A **unit vector** is a vector of unit magnitude drawn in the direction of a given vector $\\vec{A}$:
$$\\hat{n} = \\frac{\\vec{A}}{|\\vec{A}|} \\implies \\vec{A} = |\\vec{A}| \\hat{n}$$
Unit vectors are dimensionless and carry no physical units.
In standard 3D Cartesian coordinates:
- $\\hat{i}$ is the unit vector along $+X$-axis.
- $\\hat{j}$ is the unit vector along $+Y$-axis.
- $\\hat{k}$ is the unit vector along $+Z$-axis.

### 2. Resolution into Rectangular Components
Let vector $\\vec{A}$ make angle $\\theta$ with the $X$-axis in the $X-Y$ plane:
- **Horizontal component**: $A_x = A \\cos \\theta$
- **Vertical component**: $A_y = A \\sin \\theta$
- **Vector Form**:
  $$\\vec{A} = A_x \\hat{i} + A_y \\hat{j}$$
- **Magnitude**:
  $$|\\vec{A}| = \\sqrt{A_x^2 + A_y^2}$$
- **Direction Angle**:
  $$\\tan \\theta = \\frac{A_y}{A_x} \\implies \\theta = \\tan^{-1}\\left(\\frac{A_y}{A_x}\\right)$$

### 3. Generalization to Three Dimensions
$$\\vec{A} = A_x \\hat{i} + A_y \\hat{j} + A_z \\hat{k}$$
$$|\\vec{A}| = \\sqrt{A_x^2 + A_y^2 + A_z^2}$$
If $\\vec{A}$ makes angles $\\alpha, \\beta, \\gamma$ with $X, Y, Z$ axes respectively:
$$\\cos \\alpha = \\frac{A_x}{|\\vec{A}|}, \\quad \\cos \\beta = \\frac{A_y}{|\\vec{A}|}, \\quad \\cos \\gamma = \\frac{A_z}{|\\vec{A}|}$$
*Fundamental Identity*:
$$\\cos^2 \\alpha + \\cos^2 \\beta + \\cos^2 \\gamma = \\frac{A_x^2 + A_y^2 + A_z^2}{|\\vec{A}|^2} = 1$$
Also: $\\sin^2 \\alpha + \\sin^2 \\beta + \\sin^2 \\gamma = 2$.
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 3.4: The position of a particle is given by r⃗ = 3.0 t î + 2.0 t² ĵ + 5.0 k̂ where t is in seconds and the coefficients have the proper units for r to be in metres. (a) Find v⃗(t) and a⃗(t) of the particle. (b) Find the magnitude and direction of v⃗(t) at t = 1.0 s.",
                "given": "r⃗(t) = 3.0 t î + 2.0 t² ĵ + 5.0 k̂.",
                "formula": "v⃗ = dr⃗/dt; a⃗ = dv⃗/dt; |v⃗| = √(v_x² + v_y² + v_z²); θ = tan⁻¹(v_y / v_x).",
                "substitution": "(a) v⃗(t) = d/dt (3.0 t î + 2.0 t² ĵ + 5.0 k̂) = 3.0 î + 4.0 t ĵ; a⃗(t) = d/dt (3.0 î + 4.0 t ĵ) = 4.0 ĵ. (b) At t = 1.0 s: v⃗(1.0) = 3.0 î + 4.0 ĵ m/s.",
                "calculation": "Magnitude |v⃗| = √[(3.0)² + (4.0)²] = √[9 + 16] = √25 = 5.0 m/s. Direction θ = tan⁻¹(4.0 / 3.0) = tan⁻¹(1.333) ≈ 53° with x-axis.",
                "finalAnswer": "(a) v⃗(t) = 3.0 î + 4.0 t ĵ, a⃗(t) = 4.0 ĵ m/s²; (b) At t = 1.0s, speed = 5.0 m/s at 53° with x-axis.",
                "unit": "m/s, m/s²",
                "has_diagram": True,
                "diagram_svg": mod2_svg
            }
        ],
        "common_misconceptions": [
            "Assuming A_x is always A cos θ: A_x is A cos θ ONLY when θ is measured relative to the X-axis! If θ is measured relative to the Y-axis, A_y = A cos θ and A_x = A sin θ!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod2_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Orthogonal Rectangular Components (A_x, A_y)",
                    "diagram_title": "Vector Projection onto Cartesian Axes",
                    "diagram_type": "svg",
                    "svg": mod2_svg,
                    "image_search_query": "vector components resolution cartesian plane physics",
                    "video_search_query": "resolving vectors into components physics animation",
                    "what_to_make": "Vector A on coordinate plane with green horizontal component and red vertical component",
                    "what_to_explain": "Demonstrate the right-triangle trigonometry leading to Ax = A cos θ and Ay = A sin θ",
                    "timing_and_cue": "Step 2 (Formulation)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "Can a vector have zero magnitude if one of its rectangular components is non-zero?",
                            "ideal_answer": "No. Since |A⃗| = √(A_x² + A_y² + A_z²), if any single component is non-zero, its square is positive, making the magnitude strictly greater than zero.",
                            "socratic_hint": "Look at the square root sum of squares formula.",
                            "type": "Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 3: Vector Products (Scalar Dot Product & Vector Cross Product)
    # Date: 2026-11-24
    # -------------------------------------------------------------
    modules.append({
        "order_index": 14,
        "title": "Vector Multiplication: Scalar (Dot) Product, Vector (Cross) Product & Physical Meaning",
        "description": "Deep mathematical and physical exploration of the dot product (work, power) and cross product (torque, angular momentum), algebraic component rules, and right-hand screw rule.",
        "target_completion_date": "2026-11-24",
        "syllabus_pacing": "Day 13 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Scalar (Dot) Product: Definition A⃗ · B⃗ = A B cos θ (Projection of B along A)",
            "Properties of Dot Product: Commutative (A⃗ · B⃗ = B⃗ · A⃗), distributive",
            "Orthogonal unit vector dot products: î · î = ĵ · ĵ = k̂ · k̂ = 1 and î · ĵ = ĵ · k̂ = k̂ · î = 0",
            "Dot product in component form: A⃗ · B⃗ = A_x B_x + A_y B_y + A_z B_z",
            "Condition for perpendicular vectors: A⃗ · B⃗ = 0 (Orthogonality test)",
            "Vector (Cross) Product: Definition A⃗ × B⃗ = (A B sin θ) n̂ (Area of parallelogram)",
            "Right-hand thumb rule / screw rule for direction of cross product",
            "Anti-commutative property: A⃗ × B⃗ = - (B⃗ × A⃗) and self-cross product A⃗ × A⃗ = 0",
            "Cross product in determinant form using Cartesian unit vectors"
        ],
        "key_concepts": [
            "Scalar Product A⃗ · B⃗ = AB cos θ",
            "Orthogonality Condition (A⃗ · B⃗ = 0)",
            "Vector Product A⃗ × B⃗ = (AB sin θ) n̂",
            "Determinant Method for Cross Product"
        ],
        "success_criteria": [
            "Calculate work done using W = F⃗ · d⃗",
            "Determine the angle between any two vectors using cos θ = (A⃗ · B⃗) / (|A⃗||B⃗|)",
            "Evaluate cross products using 3×3 determinants for torque and angular momentum",
            "Calculate the area of a triangle or parallelogram formed by two vectors"
        ],
        "chapter_notes": """# CHAPTER 3: MOTION IN A PLANE
## MODULE 3: Vector Multiplication

### 1. Scalar (Dot) Product
$$\\vec{A} \\cdot \\vec{B} = |\\vec{A}| |\\vec{B}| \\cos \\theta$$
- **Geometric Meaning**: Magnitude of $\\vec{A}$ multiplied by the projection of $\\vec{B}$ onto $\\vec{A}$.
- **Unit vectors**:
  $$\\hat{i} \\cdot \\hat{i} = \\hat{j} \\cdot \\hat{j} = \\hat{k} \\cdot \\hat{k} = 1$$
  $$\\hat{i} \\cdot \\hat{j} = \\hat{j} \\cdot \\hat{k} = \\hat{k} \\cdot \\hat{i} = 0$$
- **Component form**:
  $$\\vec{A} \\cdot \\vec{B} = A_x B_x + A_y B_y + A_z B_z$$
- **Angle between vectors**:
  $$\\cos \\theta = \\frac{\\vec{A} \\cdot \\vec{B}}{|\\vec{A}| |\\vec{B}|} = \\frac{A_x B_x + A_y B_y + A_z B_z}{\\sqrt{A_x^2 + A_y^2 + A_z^2} \\sqrt{B_x^2 + B_y^2 + B_z^2}}$$

### 2. Vector (Cross) Product
$$\\vec{A} \\times \\vec{B} = (|\\vec{A}| |\\vec{B}| \\sin \\theta) \\, \\hat{n}$$
where $\\hat{n}$ is a unit vector perpendicular to the plane containing $\\vec{A}$ and $\\vec{B}$, given by the **Right-Hand Rule**.
- **Properties**:
  1. Anti-commutative: $\\vec{A} \\times \\vec{B} = -(\\vec{B} \\times \\vec{A})$
  2. Collinear/Parallel vectors ($\\theta = 0^\\circ$ or $180^\\circ$): $\\vec{A} \\times \\vec{B} = \\vec{0}$
  3. Self cross product: $\\hat{i} \\times \\hat{i} = \\hat{j} \\times \\hat{j} = \\hat{k} \\times \\hat{k} = \\vec{0}$
  4. Cyclic cross products:
     $$\\hat{i} \\times \\hat{j} = \\hat{k}, \\quad \\hat{j} \\times \\hat{k} = \\hat{i}, \\quad \\hat{k} \\times \\hat{i} = \\hat{j}$$
- **Determinant Form**:
  $$\\vec{A} \\times \\vec{B} = \\begin{vmatrix} \\hat{i} & \\hat{j} & \\hat{k} \\\\ A_x & A_y & A_z \\\\ B_x & B_y & B_z \\end{vmatrix} = \\hat{i}(A_y B_z - A_z B_y) - \\hat{j}(A_x B_z - A_z B_x) + \\hat{k}(A_x B_y - A_y B_x)$$
- **Geometric Meaning**: Magnitude $|\\vec{A} \\times \\vec{B}|$ equals the **area of the parallelogram** formed by $\\vec{A}$ and $\\vec{B}$.
""",
        "worked_examples": [
            {
                "problem": "Board Exam Problem: Find the angle between force vector F⃗ = (3 î + 4 ĵ - 5 k̂) N and displacement vector d⃗ = (5 î + 4 ĵ + 3 k̂) m. Also find the work done.",
                "given": "F⃗ = 3 î + 4 ĵ - 5 k̂, d⃗ = 5 î + 4 ĵ + 3 k̂.",
                "formula": "Work W = F⃗ · d⃗; cos θ = (F⃗ · d⃗) / (|F⃗||d⃗|).",
                "substitution": "F⃗ · d⃗ = (3)(5) + (4)(4) + (-5)(3) = 15 + 16 - 15 = 16 J. |F⃗| = √[3² + 4² + (-5)²] = √[9 + 16 + 25] = √50 = 5√2. |d⃗| = √[5² + 4² + 3²] = √50 = 5√2.",
                "calculation": "cos θ = 16 / (5√2 × 5√2) = 16 / 50 = 0.32 => θ = cos⁻¹(0.32) ≈ 71.3°.",
                "finalAnswer": "Work done = 16 J; Angle between vectors = 71.3°",
                "unit": "J, degrees",
                "has_diagram": True,
                "diagram_svg": mod2_svg
            }
        ],
        "common_misconceptions": [
            "Assuming cross product is commutative: A⃗ × B⃗ is equal to - (B⃗ × A⃗). Reversing order reverses the vector direction by 180°!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod2_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Vector Product A⃗ × B⃗ = (AB sin θ) n̂",
                    "diagram_title": "Right-Hand Rule for Vector Cross Product",
                    "diagram_type": "svg",
                    "svg": mod2_svg,
                    "image_search_query": "cross product right hand rule physics diagram",
                    "video_search_query": "vector cross product right hand rule 3d animation",
                    "what_to_make": "Right-hand rule diagram showing curl from A to B and thumb pointing along normal n",
                    "what_to_explain": "Explain why cross product produces a vector normal to the plane of A and B",
                    "timing_and_cue": "Step 2 (Geometric Meaning)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "What is the condition for two vectors A⃗ and B⃗ to be parallel? What is the condition for them to be perpendicular?",
                            "ideal_answer": "Two non-zero vectors are parallel if their cross product is zero (A⃗ × B⃗ = 0⃗). They are perpendicular if their dot product is zero (A⃗ · B⃗ = 0).",
                            "socratic_hint": "Recall when sin θ = 0 and when cos θ = 0.",
                            "type": "Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 4: Projectile Motion Trajectory & Kinematics
    # Date: 2026-11-25
    # -------------------------------------------------------------
    mod4_svg = sb.build_projectile_motion_svg(title="Projectile Motion Trajectory Analysis", caption="Parabolic trajectory: y = x tan θ - (g x²)/(2 v₀² cos² θ)")
    modules.append({
        "order_index": 15,
        "title": "Projectile Motion: Two-Dimensional Kinematics, Parabolic Trajectory & Range Mastery",
        "description": "Comprehensive analytical derivation of projectile motion under gravity: path equation (parabola), time of flight, maximum height, horizontal range, and proof of equal ranges for complementary angles.",
        "target_completion_date": "2026-11-25",
        "syllabus_pacing": "Day 14 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Principle of independence of vertical and horizontal motions (Galileo's principle)",
            "Horizontal motion with zero acceleration: x(t) = (v₀ cos θ₀) t",
            "Vertical motion under constant downward acceleration: y(t) = (v₀ sin θ₀) t - ½ g t²",
            "Equation of trajectory: Deriving y = x tan θ₀ - [g / (2 v₀² cos² θ₀)] x² (Proof of parabola)",
            "Time to reach maximum height: t_m = (v₀ sin θ₀) / g",
            "Total time of flight: T = (2 v₀ sin θ₀) / g",
            "Maximum height attained: H = (v₀² sin² θ₀) / (2g)",
            "Horizontal Range: R = (v₀² sin 2θ₀) / g",
            "Maximum range condition: θ₀ = 45° giving R_max = v₀² / g",
            "Galileo's theorem: Equal horizontal ranges for complementary angles (θ and 90° - θ)"
        ],
        "key_concepts": [
            "Parabolic Equation of Trajectory",
            "Time of Flight T = (2 v₀ sin θ) / g",
            "Maximum Height H = (v₀² sin² θ) / 2g",
            "Horizontal Range R = (v₀² sin 2θ) / g & Max at 45°",
            "Equal Ranges for Complementary Angles (45° ± α)"
        ],
        "success_criteria": [
            "Derive the parabolic trajectory equation eliminating time t between x and y",
            "Derive formulas for T, H, and R with explicit algebraic steps",
            "Prove analytically that R(45° + α) = R(45° - α)",
            "Calculate velocity vector components and direction at any instant of flight"
        ],
        "chapter_notes": """# CHAPTER 3: MOTION IN A PLANE
## MODULE 4: Projectile Motion

### 1. Independence of Motions
A projectile is an object thrown into space that moves under the sole influence of gravity.
- **Horizontal Direction**: $a_x = 0 \\implies v_x = v_0 \\cos \\theta_0 = \\text{constant}$
  $$x = (v_0 \\cos \\theta_0) t \\implies t = \\frac{x}{v_0 \\cos \\theta_0}$$
- **Vertical Direction**: $a_y = -g \\implies v_y = v_0 \\sin \\theta_0 - gt$
  $$y = (v_0 \\sin \\theta_0) t - \\frac{1}{2} g t^2$$

### 2. Equation of the Path (Trajectory)
Substitute $t = \\frac{x}{v_0 \\cos \\theta_0}$ into the vertical equation:
$$y = (v_0 \\sin \\theta_0)\\left(\\frac{x}{v_0 \\cos \\theta_0}\\right) - \\frac{1}{2} g \\left(\\frac{x}{v_0 \\cos \\theta_0}\\right)^2$$
$$y = x \\tan \\theta_0 - \\left[\\frac{g}{2 v_0^2 \\cos^2 \\theta_0}\\right] x^2$$
This has the form $y = ax - bx^2$, where $a$ and $b$ are constants. This is the standard equation of a **parabola**!

### 3. Core Trajectory Parameters
1. **Time of Flight ($T$)**: Setting $y = 0$:
   $$0 = T \\left(v_0 \\sin \\theta_0 - \\frac{1}{2} g T\\right) \\implies T = \\frac{2 v_0 \\sin \\theta_0}{g}$$
2. **Maximum Height ($H$)**: At peak, $v_y = 0 \\implies 0 = (v_0 \\sin \\theta_0)^2 - 2gH$:
   $$H = \\frac{v_0^2 \\sin^2 \\theta_0}{2g}$$
3. **Horizontal Range ($R$)**: Range $= v_x \\times T = (v_0 \\cos \\theta_0) \\left(\\frac{2 v_0 \\sin \\theta_0}{g}\\right)$:
   $$R = \\frac{v_0^2 (2 \\sin \\theta_0 \\cos \\theta_0)}{g} = \\frac{v_0^2 \\sin 2\\theta_0}{g}$$

### 4. Maximum Range & Complementary Angles
- **Maximum Range**: $\\sin 2\\theta_0$ is maximum when $2\\theta_0 = 90^\\circ \\implies \\theta_0 = 45^\\circ$:
  $$R_{\\text{max}} = \\frac{v_0^2}{g}$$
- **Equal Range for Complementary Angles**:
  For launch angle $\\theta_1 = 45^\\circ + \\alpha$ and $\\theta_2 = 45^\\circ - \\alpha$:
  $$\\sin 2\\theta_1 = \\sin(90^\\circ + 2\\alpha) = \\cos 2\\alpha$$
  $$\\sin 2\\theta_2 = \\sin(90^\\circ - 2\\alpha) = \\cos 2\\alpha$$
  Therefore, $R(\\theta_1) = R(\\theta_2)$!
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 3.8: A cricket ball is thrown at a speed of 28 m s⁻¹ in a direction 30° above the horizontal. Calculate (a) the maximum height, (b) the time taken by the ball to return to the same level, and (c) the distance from the thrower to the point where the ball returns to the same level. (Take g = 9.8 m s⁻²).",
                "given": "v₀ = 28 m/s, θ₀ = 30°, g = 9.8 m/s².",
                "formula": "(a) H = (v₀² sin² θ) / 2g; (b) T = (2 v₀ sin θ) / g; (c) R = (v₀² sin 2θ) / g.",
                "substitution": "(a) H = [(28)² × (sin 30°)²] / [2 × 9.8] = [784 × (0.5)²] / 19.6 = [784 × 0.25] / 19.6 = 196 / 19.6 = 10 m. (b) T = [2 × 28 × 0.5] / 9.8 = 28 / 9.8 = 2.86 s. (c) R = [(28)² × sin 60°] / 9.8 = [784 × (√3/2)] / 9.8 = [784 × 0.866] / 9.8 = 678.9 / 9.8 = 69.28 m ≈ 69 m.",
                "calculation": "H = 10 m, T = 2.9 s, R = 69 m.",
                "finalAnswer": "(a) Maximum height H = 10 m; (b) Time of flight T = 2.9 s; (c) Horizontal range R = 69 m.",
                "unit": "m, s",
                "has_diagram": True,
                "diagram_svg": mod4_svg,
                "is_graph": True,
                "graph_config": {"formula": "x*tan(pi/6) - (9.8*x^2)/(2*(28^2)*(cos(pi/6))^2)", "domain": [0, 80], "range": [0, 15]}
            }
        ],
        "common_misconceptions": [
            "Assuming acceleration at the highest point of projectile is zero: Horizontal acceleration is zero throughout, but vertical acceleration is ALWAYS 9.8 m/s² downwards!",
            "Assuming velocity at peak is zero: Vertical component v_y is zero, but horizontal component v_x = v₀ cos θ is non-zero, so the projectile NEVER comes to rest at the top!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "graph",
            "svg": mod4_svg,
            "interactive_math_formula": "x*tan(pi/6) - (9.8*x^2)/(2*(28^2)*(cos(pi/6))^2)",
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Parabolic Equation of Trajectory",
                    "diagram_title": "Parabolic Trajectory Coordinates with Velocity Vectors",
                    "diagram_type": "graph",
                    "svg": mod4_svg,
                    "interactive_math_formula": "x*tan(pi/6) - (9.8*x^2)/(2*(28^2)*(cos(pi/6))^2)",
                    "image_search_query": "projectile motion parabolic trajectory physics diagram",
                    "video_search_query": "projectile motion derivation time height range physics",
                    "what_to_make": "Parabolic arc with apex at (34.6m, 10m) and landing at 69m with velocity vector components",
                    "what_to_explain": "Explain why horizontal velocity remains strictly constant while vertical velocity varies linearly",
                    "timing_and_cue": "Step 2 (Derivation)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "What is the angle between velocity and acceleration at the highest point of a projectile path?",
                            "ideal_answer": "At the apex, the velocity is purely horizontal (v_x) and the acceleration is purely vertical (g downwards). Therefore, the angle between them is exactly 90°.",
                            "socratic_hint": "What is the direction of velocity at the peak? What is the direction of gravity?",
                            "type": "Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 5: Horizontal Projection from a Cliff / Height
    # Date: 2026-11-26
    # -------------------------------------------------------------
    mod5_svg = sb.build_projectile_motion_svg(title="Horizontal Projection from a Height", caption="Initial vertical velocity v_y0 = 0; Time of flight T = √(2h/g) independent of launch speed!")
    modules.append({
        "order_index": 16,
        "title": "Horizontal Projection from an Elevated Height: Time of Flight & Impact Mechanics",
        "description": "Analysis of objects projected horizontally from cliffs, towers, and aircraft: independence of horizontal speed on falling time, trajectory derivation, and final impact velocity vector.",
        "target_completion_date": "2026-11-26",
        "syllabus_pacing": "Day 15 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 50,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Initial conditions for horizontal launch: v_{x0} = u, v_{y0} = 0",
            "Time of flight: h = ½ g t² => t = √(2h / g) (Strictly independent of launch velocity u!)",
            "Horizontal range: R = u t = u √(2h / g)",
            "Velocity at any instant t: v_x = u, v_y = gt => v = √(u² + g² t²)",
            "Impact angle with ground: tan β = v_y / v_x = gt / u",
            "Dropping emergency aid packets from moving aircraft: Forward lead distance required"
        ],
        "key_concepts": [
            "Independence of Time of Flight on Horizontal Speed (t = √(2h/g))",
            "Horizontal Range R = u √(2h/g)",
            "Impact Speed v = √(u² + 2gh)",
            "Aircraft Bomb/Packet Release Kinematics"
        ],
        "success_criteria": [
            "Prove that a horizontally fired bullet and a dropped bullet hit level ground at the exact same instant",
            "Calculate horizontal range and landing velocity for cliff launch scenarios",
            "Determine the release lead angle when dropping supplies from an airplane"
        ],
        "chapter_notes": """# CHAPTER 3: MOTION IN A PLANE
## MODULE 5: Horizontal Projection from Height

### 1. Kinematics of Horizontal Projection
Let an object be thrown horizontally with velocity $u$ from height $h$:
- **Horizontal**: $x = u t \\implies t = \\frac{x}{u}$
- **Vertical**: $y = \\frac{1}{2} g t^2 = \\frac{1}{2} g \\left(\\frac{x}{u}\\right)^2 = \\frac{g}{2 u^2} x^2$ (Parabola with vertex at origin).

### 2. Time of Flight & Range
- **Time of flight ($T$)**:
  $$h = \\frac{1}{2} g T^2 \\implies T = \\sqrt{\\frac{2h}{g}}$$
  *Remarkable Physical Fact*: $T$ depends **only on height $h$ and gravity $g$**. It does NOT depend on launch velocity $u$. A bullet fired horizontally from a rifle and another bullet dropped simultaneously from the same height will strike the flat ground at the **exact same instant**!
- **Horizontal Range ($R$)**:
  $$R = u T = u \\sqrt{\\frac{2h}{g}}$$

### 3. Velocity at Landing
At the moment of hitting ground ($t = T$):
$$v_x = u, \\quad v_y = g T = \\sqrt{2gh}$$
$$v = \\sqrt{v_x^2 + v_y^2} = \\sqrt{u^2 + 2gh}$$
Direction with ground: $\\tan \\beta = \\frac{v_y}{v_x} = \\frac{\\sqrt{2gh}}{u}$.
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 3.7: A hiker stands on the edge of a cliff 490 m above the ground and throws a stone horizontally with an initial speed of 15 m s⁻¹. Neglecting air resistance, find the time taken by the stone to reach the ground, and the speed with which it hits the ground. (Take g = 9.8 m s⁻²).",
                "given": "h = 490 m, v_{x0} = 15 m/s, v_{y0} = 0, g = 9.8 m/s².",
                "formula": "T = √(2h / g); v = √(v_x² + v_y²) where v_x = 15 m/s, v_y = gt.",
                "substitution": "T = √[(2 × 490 m) / (9.8 m/s²)] = √(980 / 9.8) = √100 = 10 s. v_x = 15 m/s; v_y = 9.8 × 10 = 98 m/s.",
                "calculation": "Impact speed v = √[(15)² + (98)²] = √[225 + 9604] = √9829 ≈ 99.1 m/s.",
                "finalAnswer": "Time to reach ground = 10 s; Impact speed = 99 m/s",
                "unit": "s, m/s",
                "has_diagram": True,
                "diagram_svg": mod5_svg
            }
        ],
        "common_misconceptions": [
            "Believing the faster projectile stays in the air longer: Both horizontally fired and dropped objects fall vertically with identical acceleration g. Their time of flight is identical!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod5_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Independence of Time of Flight on Horizontal Speed",
                    "diagram_title": "Stroboscopic Comparison: Dropped Ball vs Horizontally Fired Ball",
                    "diagram_type": "svg",
                    "svg": mod5_svg,
                    "image_search_query": "horizontal projectile motion simultaneous drop physics diagram",
                    "video_search_query": "bullet fired vs bullet dropped mythbusters physics",
                    "what_to_make": "Dual trajectories showing identical vertical heights at every horizontal flash interval",
                    "what_to_explain": "Explain that gravity operates exclusively on the vertical coordinate",
                    "timing_and_cue": "Step 1 (Intuition Demonstration)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "An airplane flying horizontally at altitude h with speed v drops a food packet. How far ahead of the target must the pilot release the packet?",
                            "ideal_answer": "The packet takes time T = √(2h/g) to fall. During this time it moves forward distance d = v √(2h/g). The pilot must release it at horizontal distance d ahead of target.",
                            "socratic_hint": "What is the initial horizontal velocity of the packet at release?",
                            "type": "Board Numerical"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 6: Uniform Circular Motion & Centripetal Acceleration
    # Date: 2026-11-27
    # -------------------------------------------------------------
    modules.append({
        "order_index": 17,
        "title": "Uniform Circular Motion: Angular Variables & Centripetal Acceleration Derivation",
        "description": "Rigorous vector calculus derivation of centripetal acceleration a_c = v²/r directed radially inward, angular velocity ω, relationship v = ω r, and frequency/period relations.",
        "target_completion_date": "2026-11-27",
        "syllabus_pacing": "Day 16 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Definition of Uniform Circular Motion (UCM): Constant speed, continuously changing direction",
            "Angular displacement θ (in radians) and Angular velocity ω = dθ / dt = 2π / T = 2π ν",
            "Linear velocity relation: v = ω r (directed tangentially)",
            "Vector geometric derivation of Centripetal Acceleration: a_c = lim (Δv / Δt) = v² / r",
            "Vector direction: Centripetal acceleration is strictly directed radially inward toward circle center",
            "Alternative formulas for centripetal acceleration: a_c = v² / r = ω² r = 4π² ν² r",
            "Non-uniform circular motion: Tangential acceleration a_t = dv/dt and total acceleration a = √(a_c² + a_t²)"
        ],
        "key_concepts": [
            "Uniform Circular Motion Kinematics",
            "Angular Velocity ω = 2π / T = 2π ν",
            "Centripetal Acceleration Vector Derivation a_c = v²/r (-r̂)",
            "Total Acceleration in Non-Uniform Circular Motion"
        ],
        "success_criteria": [
            "Derive a_c = v²/r using similar velocity triangles or unit vector differentiation",
            "Explain why UCM is an accelerated motion despite constant speed",
            "Convert revolutions per minute (rpm) to radians per second (rad/s)",
            "Calculate total acceleration when a particle speeds up in a circular path"
        ],
        "chapter_notes": """# CHAPTER 3: MOTION IN A PLANE
## MODULE 6: Uniform Circular Motion

### 1. Definition of UCM
When an object follows a circular path at a **constant speed**, its motion is called **Uniform Circular Motion (UCM)**.
Even though speed is constant, the velocity vector $\\vec{v}$ continuously changes direction, pointing tangentially at every instant. Since velocity changes, the object is continuously **accelerating**!

### 2. Angular Variables
- **Angular Displacement ($\\Delta \\theta$)**: Angle subtended at the center in radians: $\\Delta \\theta = \\frac{\\Delta s}{r}$.
- **Time Period ($T$)**: Time taken to complete one revolution.
- **Frequency ($\\nu$)**: Number of revolutions per unit second: $\\nu = 1 / T$ (in Hz or s$^{-1}$).
- **Angular Velocity ($\\omega$)**:
  $$\\omega = \\frac{d\\theta}{dt} = \\frac{2\\pi}{T} = 2\\pi \\nu$$
- **Linear Velocity ($v$)**: Distance in one revolution / period:
  $$v = \\frac{2\\pi r}{T} = \\omega r$$

### 3. Derivation of Centripetal Acceleration
Let position vectors at $t$ and $t + \\Delta t$ be $\\vec{r}$ and $\\vec{r}'$, with $|\vec{r}| = |\\vec{r}'| = R$.
The velocity vectors $\\vec{v}$ and $\\vec{v}'$ are perpendicular to $\\vec{r}$ and $\\vec{r}'$ with $|\\vec{v}| = |\\vec{v}'| = v$.
The angle between $\\vec{v}$ and $\\vec{v}'$ is $\\Delta \\theta$.
Forming the velocity vector triangle:
$$\\frac{|\\Delta \\vec{v}|}{v} \\approx \\frac{\\Delta r}{R} \\implies |\\Delta \\vec{v}| = \\frac{v}{R} \\Delta r$$
Dividing by $\\Delta t$ as $\\Delta t \\to 0$:
$$a_c = \\lim_{\\Delta t \\to 0} \\frac{|\\Delta \\vec{v}|}{\\Delta t} = \\frac{v}{R} \\left(\\lim_{\\Delta t \\to 0} \\frac{\\Delta r}{\\Delta t}\\right) = \\frac{v}{R} \\times v = \\frac{v^2}{R}$$
Using $v = \\omega R$:
$$a_c = \\frac{v^2}{R} = \\omega^2 R = 4\\pi^2 \\nu^2 R$$
- **Direction**: As $\\Delta t \\to 0$, the vector $\\Delta \\vec{v}$ becomes perpendicular to $\\vec{v}$ and points **radially inwards towards the center**. Hence called **centripetal** (center-seeking) acceleration:
  $$\\vec{a}_c = -\\left(\\frac{v^2}{R}\\right) \\hat{r}$$
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 3.9: An insect trapped in a circular groove of radius 12 cm moves along the groove steadily and completes 7 revolutions in 100 s. (a) What is the angular speed, and the linear speed of the motion? (b) Is the acceleration vector a constant vector? What is its magnitude?",
                "given": "r = 12 cm = 0.12 m; n = 7 revolutions in t = 100 s => ν = 7 / 100 s⁻¹ = 0.07 Hz.",
                "formula": "(a) ω = 2π ν; v = ω r; (b) a_c = ω² r.",
                "substitution": "(a) ω = 2 × (22/7) × (7/100) = 44 / 100 = 0.44 rad/s. v = 0.44 rad/s × 12 cm = 5.28 cm/s = 0.053 m/s. (b) a_c = (0.44)² × 12 cm = 0.1936 × 12 = 2.32 cm/s² = 2.3 × 10⁻² m/s².",
                "calculation": "Acceleration magnitude is constant (2.3 cm/s²), but its direction points continuously toward the center (changing direction continuously); thus the acceleration vector is NOT a constant vector!",
                "finalAnswer": "(a) ω = 0.44 rad/s, v = 5.3 cm/s; (b) Acceleration magnitude = 2.3 cm/s² (direction is not constant).",
                "unit": "rad/s, cm/s, cm/s²",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            }
        ],
        "common_misconceptions": [
            "Claiming acceleration in UCM is constant: The MAGNITUDE of centripetal acceleration is constant (v²/r), but its DIRECTION rotates continuously; therefore, the acceleration vector is NOT constant!",
            "Confusing centripetal force with a new physical force: Centripetal force is not an extra force; it is simply the net required inward force provided by real physical interactions (friction, tension, gravity, normal reaction)."
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod1_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Centripetal Acceleration Vector Derivation a_c = v²/r (-r̂)",
                    "diagram_title": "Position and Velocity Triangle Geometry in UCM",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "centripetal acceleration vector derivation velocity triangle ucm",
                    "video_search_query": "centripetal acceleration derivation physics similar triangles",
                    "what_to_make": "Circular path with radius vectors and corresponding velocity vector subtraction triangle",
                    "what_to_explain": "Demonstrate why Δv points strictly inward toward the circle center as Δt approaches 0",
                    "timing_and_cue": "Step 2 (Analytical Derivation)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "What is the direction of the velocity vector and acceleration vector for a particle in uniform circular motion?",
                            "ideal_answer": "Velocity is directed tangentially to the circle in the direction of motion; acceleration is directed radially inward toward the center. They are strictly perpendicular (90°) at every point.",
                            "socratic_hint": "Think about tangent and radius lines on a circle.",
                            "type": "Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 7: Complete NCERT Exercise Solver (Ex 3.1 to 3.22)
    # Date: 2026-11-27
    # -------------------------------------------------------------
    modules.append({
        "order_index": 18,
        "title": "Exercise 3.1 to 3.22 Complete Solver: Vectors, Projectiles & Circular Motion Mastery",
        "description": "Exhaustive step-by-step solutions to every textbook exercise question (Exercises 3.1 through 3.22) including aircraft wind compensation, river swimmer, rotating grooves, and ceiling collisions.",
        "target_completion_date": "2026-11-27",
        "syllabus_pacing": "Day 16 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 60,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Exercise 3.1 to 3.3: Scalar vs Vector classifications and algebraic relationships",
            "Exercise 3.4 to 3.6: Geometric proofs of vector inequalities |a + b| <= |a| + |b|",
            "Exercise 3.7 to 3.10: Steamboat in river, swimmer aiming across flow, wind-aircraft triangle",
            "Exercise 3.11 to 3.15: Projectile ceiling clearance, maximum range, rifle shooting at target",
            "Exercise 3.16 to 3.18: Fighter jet releasing bomb, rotating turntable centripetal limits",
            "Exercise 3.19 to 3.22: String tension in circular motion and relative velocities"
        ],
        "key_concepts": [
            "Vector Triangle Inequalities (|A + B| ≤ |A| + |B|)",
            "River Swimmer Crossing: Shortest Path vs Shortest Time",
            "Ceiling Clearance Projectile Problem (Ex 3.13)",
            "Complete Exercise Solver (3.1 to 3.22)"
        ],
        "success_criteria": [
            "Solve every question of Exercise 3.1 to 3.22 with full step-by-step layout",
            "Solve the river-swimmer minimum time (aim perpendicular) and zero drift (aim upstream)",
            "Determine the maximum horizontal range when a ceiling restricts vertical height to h",
            "Attain 100% mastery of 2D Kinematics for CBSE Mid-Term Examination"
        ],
        "chapter_notes": """# CHAPTER 3: MOTION IN A PLANE
## MODULE 7: Complete NCERT Exercise Solver

### Summary of Classical Problems
- **Exercise 3.13 (Ceiling Clearance)**:
  - Ceiling height $H = 25\\text{ m}$, launch speed $v_0 = 40\\text{ m/s}$.
  - To avoid hitting ceiling: $H_{\\text{max}} = \\frac{v_0^2 \\sin^2 \\theta}{2g} \\le 25\\text{ m}$.
  - $\\sin^2 \\theta = \\frac{25 \\times 2 \\times 9.8}{(40)^2} = \\frac{490}{1600} = 0.30625 \\implies \\sin \\theta = 0.5534 \\implies \\theta = 33.6^\\circ$.
  - Maximum range at this restricted angle:
    $$R = \\frac{v_0^2 \\sin 2\\theta}{g} = \\frac{1600 \\times \\sin(67.2^\\circ)}{9.8} = \\frac{1600 \\times 0.9219}{9.8} = 150.5\\text{ m}$$

- **Exercise 3.14 (River Swimmer)**:
  - River width $d = 1\\text{ km}$, speed of river $v_r = 3\\text{ km/h}$, swimmer speed in still water $v_s = 4\\text{ km/h}$.
  - (a) To reach directly opposite bank (zero drift):
    $$\\sin \\theta = \\frac{v_r}{v_s} = \\frac{3}{4} = 0.75 \\implies \\theta = 48.6^\\circ \\text{ upstream from normal (or } 138.6^\\circ \\text{ with flow)}.$$
  - (b) Time to cross:
    $$v_{\\text{eff}} = \\sqrt{v_s^2 - v_r^2} = \\sqrt{16 - 9} = \\sqrt{7} = 2.65\\text{ km/h}$$
    $$t = \\frac{1\\text{ km}}{2.65\\text{ km/h}} = 0.378\\text{ h} = 22.7\\text{ min}.$$
""",
        "worked_examples": [
            {
                "problem": "NCERT Exercise 3.13: A boy can jump to a maximum horizontal distance of 1.5 m. How high can he jump? (Also: The ceiling of a long hall is 25 m high. What is the maximum horizontal distance that a ball thrown with a speed of 40 m s⁻¹ can go without hitting the ceiling of the hall?)",
                "given": "Ceiling height H = 25 m, launch speed v₀ = 40 m/s, g = 9.8 m/s².",
                "formula": "H_max = (v₀² sin² θ) / 2g <= 25 m; R = (v₀² sin 2θ) / g.",
                "substitution": "sin² θ = (2 × 9.8 × 25) / (40)² = 490 / 1600 = 0.30625 => sin θ = 0.5534 => θ = 33.6°. 2θ = 67.2°. R = [(40)² × sin(67.2°)] / 9.8 = [1600 × 0.9219] / 9.8 = 1475 / 9.8",
                "calculation": "R = 150.5 m ≈ 151 m.",
                "finalAnswer": "Maximum horizontal distance without hitting ceiling = 150.5 m (≈ 151 m)",
                "unit": "m",
                "has_diagram": True,
                "diagram_svg": mod4_svg
            }
        ],
        "common_misconceptions": [
            "Using θ = 45° when ceiling height is restricted: Launching at 45° would achieve max height H = (40² × 0.5) / (19.6) = 40.8 m, which would collide with the 25 m ceiling!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "graph",
            "svg": mod4_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Ceiling Clearance Projectile Problem",
                    "diagram_title": "Horizontal Ceiling Constraint on Trajectory",
                    "diagram_type": "graph",
                    "svg": mod4_svg,
                    "image_search_query": "projectile motion ceiling hall height physics diagram",
                    "video_search_query": "projectile ceiling problem ncert physics solution",
                    "what_to_make": "Parabolic curve grazing horizontal ceiling line at y = 25m",
                    "what_to_explain": "Show how ceiling restricts maximum vertical component of velocity",
                    "timing_and_cue": "Step 2 (Constrained Optimization)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "A boat crosses a river of width d with speed v relative to water. What direction should the boat head to cross in the MINIMUM possible time?",
                            "ideal_answer": "To cross in minimum time, the boat must head directly perpendicular to the bank (straight across). Time = d / v, although it will experience drift downstream.",
                            "socratic_hint": "Which component of velocity is responsible for crossing the river width?",
                            "type": "Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    return modules
