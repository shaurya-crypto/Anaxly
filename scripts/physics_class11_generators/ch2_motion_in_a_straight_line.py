"""
ch2_motion_in_a_straight_line.py
CBSE Class 11 Physics - Chapter 2: Motion in a Straight Line
Part 1 (Mid-Term Syllabus, Unit II: Kinematics)
Target Pacing: November 17, 2026 to November 21, 2026 (6 Modules, 5 Days)
"""

import sys
import os
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

import svg_builder_physics11 as sb

CURRICULUM_ID = "c11_phy_ch02_straight_line"
CLASS_LEVEL = "Class 11"
BOARD = "CBSE"
SUBJECT = "Physics"

def get_modules():
    modules = []

    # -------------------------------------------------------------
    # MODULE 1: Frame of Reference, Position, Distance & Displacement
    # Date: 2026-11-17
    # -------------------------------------------------------------
    mod1_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 10), range_y=(0, 50),
        lines=[{'p1': (0, 0), 'p2': (10, 50), 'color': '#2563EB', 'label': 'v = 5 m/s (Uniform Motion)'}],
        points=[{'x': 0, 'y': 0, 'label': 'x₀ = 0'}, {'x': 10, 'y': 50, 'label': 'x = 50 m'}],
        x_label="Time t (s)", y_label="Position x (m)",
        title="Position-Time (x-t) Graph: Uniform Linear Motion",
        caption="Constant slope represents constant velocity v = dx/dt = 5 m/s"
    )
    modules.append({
        "order_index": 6,
        "title": "Kinematic Foundations: Frame of Reference, Path Length vs Displacement & Average Velocity",
        "description": "Exploration of the coordinate system as frame of reference, 1D motion, scalar path length versus vector displacement, and rigorous distinctions between average speed and average velocity.",
        "target_completion_date": "2026-11-17",
        "syllabus_pacing": "Day 6 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Mechanics sub-branches: Statics, Kinematics, and Dynamics",
            "Concept of point object / particle approximation in physics",
            "Frame of Reference: Coordinate axes + clock; Inertial vs Non-inertial frames",
            "Motion along a straight line (1D Rectilinear motion)",
            "Path length (Total distance) vs Displacement (Vector change Δx = x₂ - x₁)",
            "Magnitude of displacement vs path length (Displacement ≤ Distance)",
            "Average speed (Total distance / Total time) vs Average velocity (Displacement / Time)",
            "Interpretation of positive, zero, and negative velocity from position-time graphs"
        ],
        "key_concepts": [
            "Frame of Reference & Particle Model",
            "Path Length (Distance) vs Displacement (Δx)",
            "Average Speed vs Average Velocity",
            "Position-Time Graph Slopes (Positive, Negative, Zero)"
        ],
        "success_criteria": [
            "Explain why motion is strictly relative and specify an explicit frame of reference",
            "Prove that magnitude of displacement is always less than or equal to total path length",
            "Calculate average speed and average velocity for round-trips and multi-stage journeys",
            "Interpret direction of motion directly from slope sign in x-t plots"
        ],
        "chapter_notes": """# CHAPTER 2: MOTION IN A STRAIGHT LINE
## MODULE 1: Kinematic Foundations

### 1. Frame of Reference
An object is said to be in **motion** if its position changes with respect to its surroundings in a given time interval. Motion is strictly relative; there is no absolute rest in the universe.
A **Frame of Reference** consists of:
1. A chosen coordinate system (Cartesian axes $X, Y, Z$) fixed to a reference body with an origin $O$.
2. A clock to measure time $t$.
- **Inertial frame**: A frame at rest or moving with constant velocity in which Newton's 1st law holds true.
- **Non-inertial frame**: An accelerated or rotating frame (requires pseudo-forces).

### 2. Path Length vs. Displacement
- **Path Length (Distance)**: The actual length of the path traversed by an object during its motion. It is a scalar, always positive, and path-dependent.
- **Displacement ($\\Delta x$)**: The shortest directed distance from the initial position $x_1$ to final position $x_2$:
$$\\Delta x = x_2 - x_1$$
Displacement is a vector quantity. It can be **positive, zero, or negative**.
*Invariant Relationship*:
$$|\\text{Displacement}| \\le \\text{Path Length}$$
The equality holds if and only if the particle moves strictly in a straight line without reversing direction.

### 3. Average Speed vs. Average Velocity
- **Average Velocity ($\\bar{v}$)**:
$$\\bar{v} = \\frac{\\text{Displacement}}{\\text{Time interval}} = \\frac{x_2 - x_1}{t_2 - t_1} = \\frac{\\Delta x}{\\Delta t}$$
Direction of $\\bar{v}$ is in the direction of displacement $\\Delta x$.
- **Average Speed ($v_{\\text{avg}}$)**:
$$v_{\\text{avg}} = \\frac{\\text{Total path length}}{\\text{Total time interval}}$$
*Key Examination Pitfall*:
$$\\text{Average Speed} \\ge |\\text{Average Velocity}|$$
For a closed round-trip journey (returning to start), displacement is zero $\\implies \\bar{v} = 0$, but average speed is non-zero!
""",
        "worked_examples": [
            {
                "problem": "Textbook Example: A car is moving along a straight line, say OP in Fig. 2.1. It moves from O to P in 18 s and returns from P to Q in 6.0 s. What are the average velocity and average speed of the car in going (a) from O to P ? and (b) from O to P and back to Q? Coordinates: O = 0 m, Q = +240 m, P = +360 m.",
                "given": "Path O to P = 360 m in 18 s; Path P to Q = 120 m in 6.0 s; Net displacement for (b) = +240 m; Total time for (b) = 18 + 6 = 24 s.",
                "formula": "Average velocity = Displacement / Time; Average speed = Path length / Time.",
                "substitution": "(a) O to P: Displacement = +360 m, Path = 360 m, t = 18 s. (b) O to P back to Q: Displacement = +240 m, Path = 360 + 120 = 480 m, t = 24 s.",
                "calculation": "(a) v_avg = 360/18 = 20 m/s; speed_avg = 360/18 = 20 m/s. (b) v_avg = +240/24 = +10 m/s; speed_avg = 480/24 = 20 m/s.",
                "finalAnswer": "(a) Both 20 m/s; (b) Average velocity = +10 m/s, Average speed = 20 m/s",
                "unit": "m/s",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            }
        ],
        "common_misconceptions": [
            "Equating average speed to average of speeds (v1 + v2)/2: Average speed is NEVER (v1 + v2)/2 unless time intervals are strictly equal! For equal distances, v_avg = 2 v1 v2 / (v1 + v2) (Harmonic Mean).",
            "Thinking negative displacement means slowing down: Negative displacement simply means position is to the left of the chosen origin."
        ],
        "visual_lesson_plan": {
            "diagram_type": "graph",
            "svg": mod1_svg,
            "interactive_math_formula": "5*x",
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Path Length (Distance) vs Displacement (Δx)",
                    "diagram_title": "1D Number Line Kinematic Trajectory",
                    "diagram_type": "graph",
                    "svg": mod1_svg,
                    "interactive_math_formula": "5*x",
                    "image_search_query": "distance vs displacement number line physics diagram",
                    "video_search_query": "distance vs displacement difference physics animation",
                    "what_to_make": "Cartesian position-time plot showing forward motion followed by reversal and return",
                    "what_to_explain": "Point out how slope polarity reflects forward (+) and backward (-) velocity",
                    "timing_and_cue": "Step 1 (Intuition)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "Can an object have a constant speed and a varying velocity? Can it have a constant velocity and a varying speed?",
                            "ideal_answer": "Yes, an object in uniform circular motion has constant speed but continuously changing velocity due to direction change. No, if velocity is constant, its magnitude (speed) is strictly constant.",
                            "socratic_hint": "Consider velocity as both magnitude and direction.",
                            "type": "Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 2: Instantaneous Velocity & Acceleration (Calculus)
    # Date: 2026-11-18
    # -------------------------------------------------------------
    mod2_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 6), range_y=(0, 40),
        curves=[{'fn': lambda t: 2.5*t**2, 'label': 'x(t) = 2.5 t²', 'color': '#2563EB'}],
        lines=[{'p1': (1, -2.5), 'p2': (4, 35), 'color': '#DC2626', 'label': 'Tangent at t = 2s: v = 10 m/s'}],
        points=[{'x': 2, 'y': 10, 'label': 'P(2s, 10m)'}],
        x_label="Time t (s)", y_label="Position x (m)",
        title="Instantaneous Velocity via Tangent Slope: v = dx/dt",
        caption="As Δt → 0, chord slope approaches tangent slope: dx/dt = 2bt = 10 m/s at t = 2s"
    )
    modules.append({
        "order_index": 7,
        "title": "Instantaneous Velocity & Acceleration: Differential Calculus in Kinematics",
        "description": "Rigorous derivation of instantaneous velocity as the limiting value of average velocity as Δt approaches zero, geometric interpretation as tangent slope, and acceleration as second time derivative.",
        "target_completion_date": "2026-11-18",
        "syllabus_pacing": "Day 7 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Limiting process: Velocity at an instant as Δt -> 0",
            "Mathematical definition: v = lim_{Δt -> 0} (Δx / Δt) = dx / dt",
            "Geometric meaning: Slope of tangent to the position-time curve",
            "Instantaneous speed as the magnitude of instantaneous velocity",
            "Concept of acceleration: Average acceleration a_avg = Δv / Δt",
            "Instantaneous acceleration: a = lim_{Δt -> 0} (Δv / Δt) = dv / dt = d²x / dt²",
            "Calculus relations between position, velocity, and acceleration via differentiation and integration"
        ],
        "key_concepts": [
            "Instantaneous Velocity v = dx/dt",
            "Tangent Slope Interpretation on x-t Graph",
            "Instantaneous Acceleration a = dv/dt = d²x/dt²",
            "Calculus Differentiation Rules in Kinematics"
        ],
        "success_criteria": [
            "Differentiate position functions x(t) to evaluate velocity and acceleration at specific times",
            "Draw and calculate the slope of tangents to non-linear x-t curves",
            "Recognize when velocity and acceleration have opposing signs (retardation/deceleration)",
            "Integrate acceleration a(t) to obtain velocity and displacement"
        ],
        "chapter_notes": """# CHAPTER 2: MOTION IN A STRAIGHT LINE
## MODULE 2: Instantaneous Velocity & Calculus

### 1. Instantaneous Velocity
Average velocity tells us about the motion over a finite time interval, but reveals nothing about speed at individual instants.
**Instantaneous Velocity** is the velocity of an object at a specific instant of time $t$:
$$v = \\lim_{\\Delta t \\to 0} \\frac{\\Delta x}{\\Delta t} = \\frac{dx}{dt}$$
In the language of calculus, $v$ is the first time derivative of position $x$ with respect to time $t$.
- *Geometric Meaning*: On an $x-t$ curve, the instantaneous velocity at time $t$ is equal to the **slope of the tangent** drawn to the curve at that point.
- *Instantaneous Speed*: The magnitude of instantaneous velocity ($|v| = |dx/dt|$). Instantaneous speed is always equal to the magnitude of instantaneous velocity at that point.

### 2. Instantaneous Acceleration
Acceleration measures the rate at which velocity changes with time:
- **Average Acceleration**: $\\bar{a} = \\frac{\\Delta v}{\\Delta t} = \\frac{v_2 - v_1}{t_2 - t_1}$
- **Instantaneous Acceleration**:
$$a = \\lim_{\\Delta t \\to 0} \\frac{\\Delta v}{\\Delta t} = \\frac{dv}{dt} = \\frac{d}{dt}\\left(\\frac{dx}{dt}\\right) = \\frac{d^2x}{dt^2}$$
Also:
$$a = \\frac{dv}{dt} = \\frac{dv}{dx} \\frac{dx}{dt} = v \\frac{dv}{dx}$$
This chain-rule relation $a = v \\frac{dv}{dx}$ is crucial when acceleration is given as a function of position $x$.

### 3. Sign Conventions for Acceleration
- If $v$ and $a$ have the **same sign** (both positive or both negative), the speed of the object is **increasing** (accelerating).
- If $v$ and $a$ have **opposite signs**, the speed of the object is **decreasing** (retardation / deceleration).
*Note*: A negative acceleration does NOT necessarily mean retardation (e.g. an object moving in negative direction with negative acceleration is speeding up!).
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 2.1: The position of an object moving along x-axis is given by x = a + b t² where a = 8.5 m, b = 2.5 m s⁻² and t is measured in seconds. What is its velocity at t = 0 s and t = 2.0 s? What is the average velocity between t = 2.0 s and t = 4.0 s?",
                "given": "x(t) = a + b t² with a = 8.5 m, b = 2.5 m s⁻².",
                "formula": "v(t) = dx / dt = d/dt (a + b t²) = 2 b t; Average velocity = [x(t₂) - x(t₁)] / (t₂ - t₁).",
                "substitution": "(a) At t = 0: v(0) = 2 × 2.5 × 0 = 0 m/s; At t = 2.0 s: v(2) = 2 × 2.5 × 2.0 = 10 m/s. (b) x(4) = 8.5 + 2.5(16) = 48.5 m; x(2) = 8.5 + 2.5(4) = 18.5 m.",
                "calculation": "v_avg = (48.5 - 18.5) / (4.0 - 2.0) = 30.0 / 2.0 = 15 m/s.",
                "finalAnswer": "Velocity at t=0 is 0 m/s, at t=2.0s is 10 m/s; Average velocity between 2s and 4s is 15 m/s.",
                "unit": "m/s",
                "has_diagram": True,
                "diagram_svg": mod2_svg,
                "is_graph": True,
                "graph_config": {"formula": "2.5*x^2", "domain": [0, 6], "range": [0, 50]}
            }
        ],
        "common_misconceptions": [
            "Equating zero velocity with zero acceleration: At the highest point of a vertically thrown ball, instantaneous velocity is ZERO, but acceleration is 9.8 m/s² downwards!",
            "Assuming deceleration is always negative: Deceleration means speed is decreasing. If a particle moves in the -x direction (v < 0), deceleration requires a POSITIVE acceleration!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "graph",
            "svg": mod2_svg,
            "interactive_math_formula": "2.5*x^2",
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Instantaneous Velocity v = dx/dt",
                    "diagram_title": "Tangent vs Secant Line Limit on Parabolic x-t Curve",
                    "diagram_type": "graph",
                    "svg": mod2_svg,
                    "interactive_math_formula": "2.5*x^2",
                    "image_search_query": "calculus derivative slope tangent instantaneous velocity physics",
                    "video_search_query": "instantaneous velocity calculus derivative physics animation",
                    "what_to_make": "Curve of x = 2.5 t^2 with secant line rotating into tangent line at t = 2s",
                    "what_to_explain": "Demonstrate the mathematical limit lim Δt->0 Δx/Δt as the secant becomes tangent",
                    "timing_and_cue": "Step 2 (Calculus Formulation)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "If x(t) = t³ - 6t² + 9t + 2, at what time(s) does the particle momentarily come to rest?",
                            "ideal_answer": "v(t) = dx/dt = 3t² - 12t + 9 = 3(t² - 4t + 3) = 3(t - 1)(t - 3). Setting v = 0 gives t = 1 s and t = 3 s.",
                            "socratic_hint": "Differentiate x with respect to t and find the roots of the quadratic equation.",
                            "type": "Calculus Numerical"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 3: Kinematic Graphs (x-t, v-t, a-t) & Areas
    # Date: 2026-11-19
    # -------------------------------------------------------------
    mod3_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 10), range_y=(0, 25),
        polygons=[{'points': [(0, 0), (6, 18), (6, 0)], 'fill': 'rgba(37, 99, 235, 0.25)', 'stroke': '#2563EB', 'label': 'Displacement Δx = ½ × 6 × 18 = 54 m'}],
        lines=[{'p1': (0, 0), 'p2': (6, 18), 'color': '#2563EB', 'label': 'Uniform Acceleration a = 3 m/s²'}],
        points=[{'x': 6, 'y': 18, 'label': 'v = 18 m/s at t = 6s'}],
        x_label="Time t (s)", y_label="Velocity v (m/s)",
        title="Velocity-Time (v-t) Graph: Area Equals Displacement",
        caption="Slope gives acceleration (a = dv/dt); Shaded area under v-t curve gives displacement Δx"
    )
    modules.append({
        "order_index": 8,
        "title": "Kinematic Graphs: Systematic Analysis of x-t, v-t & a-t Curves and Integral Areas",
        "description": "Mastery of position-time, velocity-time, and acceleration-time graphs, slope extraction, and mathematical proof that area under v-t curve represents displacement.",
        "target_completion_date": "2026-11-19",
        "syllabus_pacing": "Day 8 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Complete taxonomy of position-time (x-t) curves: Rest, uniform, accelerated, decelerated",
            "Inflection points and concavity of x-t curves (d²x/dt² > 0 concavity upwards)",
            "Velocity-time (v-t) graphs for uniform motion, uniform acceleration, and non-uniform acceleration",
            "Physical meaning of slope of v-t curve: Instantaneous acceleration a = dv / dt",
            "Mathematical proof: Area under v-t curve = Integral v dt = Displacement",
            "Displacement vs Distance from v-t graphs: Algebraic area sum vs Absolute area sum",
            "Acceleration-time (a-t) graphs and area under a-t curve = Change in velocity Δv"
        ],
        "key_concepts": [
            "Slope of x-t Curve = Velocity",
            "Slope of v-t Curve = Acceleration",
            "Area Under v-t Curve = Displacement (Integral v dt)",
            "Area Under a-t Curve = Change in Velocity (Integral a dt)"
        ],
        "success_criteria": [
            "Deduce acceleration and velocity signs directly from the curvature of x-t graphs",
            "Compute exact displacement and distance traveled from segmented polygonal v-t graphs",
            "Convert an x-t graph into a corresponding v-t graph and a-t graph",
            "State why discontinuous jumps in x-t or v-t graphs violate physical laws"
        ],
        "chapter_notes": """# CHAPTER 2: MOTION IN A STRAIGHT LINE
## MODULE 3: Kinematic Graphs & Integral Area Proofs

### 1. Position-Time (x-t) Graphs
1. **Slope of $x-t$ curve**: $\\text{Slope} = \\frac{dx}{dt} = v$ (Velocity).
   - Horizontal line: Slope $= 0 \\implies v = 0$ (Body at rest).
   - Straight line inclined to time axis: Constant slope $\\implies$ Uniform velocity ($a = 0$).
   - Curve bending upwards (concave up, $\\frac{d^2x}{dt^2} > 0$): Slope increasing $\\implies$ Accelerated motion ($a > 0$).
   - Curve bending downwards (concave down, $\\frac{d^2x}{dt^2} < 0$): Slope decreasing $\\implies$ Decelerated motion ($a < 0$).

### 2. Velocity-Time (v-t) Graphs
1. **Slope of $v-t$ curve**: $\\text{Slope} = \\frac{dv}{dt} = a$ (Acceleration).
   - Horizontal line: Slope $= 0 \\implies a = 0$ (Uniform velocity).
   - Straight line with positive slope: Constant positive acceleration.
   - Straight line with negative slope: Constant negative acceleration (retardation).
2. **Area under $v-t$ curve**:
   $$\\text{Area} = \\int_{t_1}^{t_2} v \\, dt = \\int_{x_1}^{x_2} dx = x_2 - x_1 = \\text{Displacement}$$
   *Crucial Board Exam Invariant*:
   - **Displacement**: Area above time-axis is POSITIVE, area below time-axis is NEGATIVE:
     $$\\text{Displacement} = \\text{Area}_1 - \\text{Area}_2$$
   - **Distance Traveled**: Sum of absolute magnitudes of all areas:
     $$\\text{Total Distance} = |\\text{Area}_1| + |\\text{Area}_2|$$

### 3. Acceleration-Time (a-t) Graphs
1. **Area under $a-t$ curve**:
   $$\\text{Area} = \\int_{t_1}^{t_2} a \\, dt = v_2 - v_1 = \\Delta v \\quad (\\text{Change in Velocity})$$
""",
        "worked_examples": [
            {
                "problem": "Board Exam Problem: A particle moves along a straight line such that its velocity-time graph consists of three segments: (1) accelerates uniformly from rest to 10 m/s in 4 s; (2) moves at constant 10 m/s for 6 s; (3) decelerates uniformly to rest in 2 s. Find: (a) acceleration in each phase, (b) total displacement, (c) average velocity.",
                "given": "Phase 1: t=0 to 4s, v=0 to 10 m/s; Phase 2: t=4 to 10s, v=10 m/s; Phase 3: t=10 to 12s, v=10 to 0 m/s.",
                "formula": "a = (v₂ - v₁)/(t₂ - t₁); Displacement = Area of trapezium = ½ (sum of parallel sides) × height.",
                "substitution": "(a) a₁ = (10 - 0)/4 = 2.5 m/s²; a₂ = 0 m/s²; a₃ = (0 - 10)/2 = -5 m/s². (b) Parallel sides are 12 s and 6 s, height = 10 m/s. Area = ½ (12 + 6) × 10 = ½ (18) × 10 = 90 m. (c) v_avg = 90 m / 12 s = 7.5 m/s.",
                "calculation": "Total displacement = 90 m; Average velocity = 7.5 m/s.",
                "finalAnswer": "(a) a₁ = 2.5 m/s², a₂ = 0, a₃ = -5 m/s²; (b) Displacement = 90 m; (c) v_avg = 7.5 m/s",
                "unit": "m, m/s",
                "has_diagram": True,
                "diagram_svg": mod3_svg,
                "is_graph": True,
                "graph_config": {"formula": "3*x", "domain": [0, 10], "range": [0, 25]}
            }
        ],
        "common_misconceptions": [
            "Subtracting area below the time axis when finding total distance: Area below the t-axis is subtracted ONLY for displacement. For distance, all areas are positive scalars!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "graph",
            "svg": mod3_svg,
            "interactive_math_formula": "3*x",
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Area Under v-t Curve = Displacement",
                    "diagram_title": "Integral Area under Trapezoidal v-t Graph",
                    "diagram_type": "graph",
                    "svg": mod3_svg,
                    "interactive_math_formula": "3*x",
                    "image_search_query": "velocity time graph area displacement physics",
                    "video_search_query": "area under velocity time graph displacement derivation",
                    "what_to_make": "Trapezoidal v-t graph showing triangle and rectangle decomposition for area",
                    "what_to_explain": "Show that Riemann sum v_i Δt converges to integral v dt = Δx",
                    "timing_and_cue": "Step 2 (Integral Proof)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "Can the position-time graph of a moving object be a straight line parallel to the time axis? Can it be a vertical line parallel to the position axis?",
                            "ideal_answer": "A line parallel to time axis represents an object at rest (v = 0). A vertical line is physically impossible as it implies infinite velocity and being at multiple positions at the same instant.",
                            "socratic_hint": "Calculate the slope of a vertical line.",
                            "type": "Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 4: Equations of Uniformly Accelerated Motion & Free Fall
    # Date: 2026-11-20
    # -------------------------------------------------------------
    mod4_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 5), range_y=(-50, 25),
        curves=[{'fn': lambda t: 20*t - 5*t**2, 'label': 'y(t) = 20t - 5t²', 'color': '#2563EB'}],
        points=[{'x': 0, 'y': 0, 'label': 'Launch (v₀ = 20 m/s)'}, {'x': 2, 'y': 20, 'label': 'Apex H_max = 20 m (v = 0)'}, {'x': 4, 'y': 0, 'label': 'Ground Hit (t = 4s)'}],
        x_label="Time t (s)", y_label="Vertical Height y (m)",
        title="Free Fall Under Gravity: Ball Thrown Upwards at 20 m/s",
        caption="Symmetric trajectory with constant downward acceleration a = -g = -10 m/s²"
    )
    modules.append({
        "order_index": 9,
        "title": "Kinematic Equations for Constant Acceleration (Calculus & Graphical) & Free Fall",
        "description": "Rigorous derivation of the three fundamental equations of motion using calculus and graphs, motion under gravity, symmetric free-fall properties, and Galileo's law of odd numbers.",
        "target_completion_date": "2026-11-20",
        "syllabus_pacing": "Day 9 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Kinematic equation 1: v = v₀ + a t (Calculus derivation via a = dv/dt)",
            "Kinematic equation 2: x = v₀ t + ½ a t² (Calculus derivation via v = dx/dt)",
            "Kinematic equation 3: v² = v₀² + 2 a x (Calculus derivation via a = v dv/dx)",
            "Displacement in the nth second: D_n = v₀ + a/2 (2n - 1)",
            "Motion under gravity: Taking a = -g = -9.8 m/s² with strict sign conventions",
            "Key free fall formulas: Max height H = v₀² / 2g, Time of ascent t_a = v₀ / g, Total time T = 2v₀ / g",
            "Galileo's Law of Odd Numbers: Ratio of successive distances in equal time intervals is 1:3:5:7..."
        ],
        "key_concepts": [
            "Calculus Derivations of Equations of Motion",
            "Displacement in nth Second D_n = v₀ + a/2(2n - 1)",
            "Vertical Motion Under Gravity (Symmetry of Ascent/Descent)",
            "Galileo's Law of Odd Numbers (1 : 3 : 5 : 7 ...)"
        ],
        "success_criteria": [
            "Perform calculus integrations with limits to derive all 3 kinematic equations",
            "Derive the nth second formula D_n = S_n - S_{n-1} without sign errors",
            "Solve multi-stage ball-throwing problems from buildings and towers",
            "Prove Galileo's law of odd numbers analytically"
        ],
        "chapter_notes": """# CHAPTER 2: MOTION IN A STRAIGHT LINE
## MODULE 4: Equations of Motion & Free Fall

### 1. Calculus Derivations of Equations of Motion
Assume acceleration $a = \\text{constant}$:
1. **Equation 1 ($v = v_0 + at$)**:
   $$a = \\frac{dv}{dt} \\implies dv = a \\, dt$$
   Integrate from $t = 0$ ($v = v_0$) to $t$ ($v = v$):
   $$\\int_{v_0}^v dv = a \\int_0^t dt \\implies [v]_{v_0}^v = a [t]_0^t \\implies v - v_0 = at \\implies v = v_0 + at$$

2. **Equation 2 ($x = x_0 + v_0 t + \\frac{1}{2}at^2$)**:
   $$v = \\frac{dx}{dt} \\implies dx = v \\, dt = (v_0 + at) \\, dt$$
   Integrate from $t = 0$ ($x = x_0$) to $t$ ($x = x$):
   $$\\int_{x_0}^x dx = \\int_0^t (v_0 + at) \\, dt \\implies x - x_0 = v_0 t + \\frac{1}{2} a t^2$$

3. **Equation 3 ($v^2 = v_0^2 + 2 a (x - x_0)$)**:
   $$a = v \\frac{dv}{dx} \\implies a \\, dx = v \\, dv$$
   Integrate:
   $$a \\int_{x_0}^x dx = \\int_{v_0}^v v \\, dv \\implies a (x - x_0) = \\left[\\frac{v^2}{2}\\right]_{v_0}^v = \\frac{v^2 - v_0^2}{2} \\implies v^2 = v_0^2 + 2 a (x - x_0)$$

### 2. Distance Traveled in the nth Second
$$D_n = x(n) - x(n - 1) = \\left[v_0 n + \\frac{1}{2} a n^2\\right] - \\left[v_0(n - 1) + \\frac{1}{2} a (n - 1)^2\\right]$$
$$D_n = v_0 + \\frac{a}{2} (2n - 1)$$

### 3. Motion Under Gravity (Free Fall)
Taking upward as positive ($+y$) and downward as negative ($\\implies a = -g$):
1. $v = v_0 - g t$
2. $y = v_0 t - \\frac{1}{2} g t^2$
3. $v^2 = v_0^2 - 2 g y$
- **At Highest Point ($v = 0$)**:
  $$H_{\\text{max}} = \\frac{v_0^2}{2g}, \\quad t_{\\text{ascent}} = \\frac{v_0}{g}$$
- **Total Time of Flight (return to launch level)**:
  $$T = \\frac{2v_0}{g} = 2 \\, t_{\\text{ascent}}$$
- **Landing Speed**: $v_{\\text{land}} = -v_0$ (symmetric magnitude).

### 4. Galileo's Law of Odd Numbers
For a body released from rest ($v_0 = 0$) under gravity:
$$y(t) = \\frac{1}{2} g t^2$$
For equal successive time intervals $\\tau, 2\\tau, 3\\tau, 4\\tau$:
- Distance in 1st interval $\\tau$: $y_1 = \\frac{1}{2}g\\tau^2 = y_0$
- Distance in 2nd interval $\\tau$: $y_2 = \\frac{1}{2}g(2\\tau)^2 - y_1 = 4y_0 - y_0 = 3 y_0$
- Distance in 3rd interval $\\tau$: $y_3 = \\frac{1}{2}g(3\\tau)^2 - 4y_0 = 9y_0 - 4y_0 = 5 y_0$
- Distance in 4th interval $\\tau$: $y_4 = 16y_0 - 9y_0 = 7 y_0$
$$\\text{Ratio } y_1 : y_2 : y_3 : y_4 \\dots = 1 : 3 : 5 : 7 : \\dots$$
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 2.3: A ball is thrown vertically upwards with a velocity of 20 m s⁻¹ from the top of a multistorey building. The height of the point from where the ball is thrown is 25.0 m from the ground. (a) How high will the ball rise? and (b) how long will it be before the ball hits the ground? Take g = 10 m s⁻².",
                "given": "v₀ = +20 m/s, y₀ = +25.0 m, a = -g = -10 m/s².",
                "formula": "(a) v² = v₀² - 2g(y - y₀) with v = 0 at peak; (b) y - y₀ = v₀ t - ½ g t² with y = 0 at ground.",
                "substitution": "(a) 0 = (20)² - 2(10)(y - 25) => 20(y - 25) = 400 => y - 25 = 20 m => y = 45 m. (b) 0 - 25 = 20 t - ½(10) t² => -25 = 20 t - 5 t² => 5 t² - 20 t - 25 = 0 => t² - 4t - 5 = 0.",
                "calculation": "(t - 5)(t + 1) = 0 => t = 5 s (rejecting negative t = -1 s).",
                "finalAnswer": "(a) Ball rises 20 m above throw point (45 m from ground); (b) Total time to hit ground = 5.0 s.",
                "unit": "m, s",
                "has_diagram": True,
                "diagram_svg": mod4_svg,
                "is_graph": True,
                "graph_config": {"formula": "20*x - 5*x^2", "domain": [0, 5], "range": [-50, 25]}
            }
        ],
        "common_misconceptions": [
            "Changing sign of g when object goes up versus down: Acceleration due to gravity is ALWAYS directed downwards toward Earth center! If upward is chosen as positive, a = -g for the ENTIRE flight (both upward and downward phases)!",
            "Treating displacement as total distance when using y = v₀t - ½gt²: The kinematic equation yields DISPLACEMENT from initial point. When hitting the ground 25 m below, y - y₀ = -25 m, NOT +25 m."
        ],
        "visual_lesson_plan": {
            "diagram_type": "graph",
            "svg": mod4_svg,
            "interactive_math_formula": "20*x - 5*x^2",
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Vertical Motion Under Gravity",
                    "diagram_title": "Parabolic Height-Time Profile under Gravity",
                    "diagram_type": "graph",
                    "svg": mod4_svg,
                    "interactive_math_formula": "20*x - 5*x^2",
                    "image_search_query": "free fall gravity kinematic parabola height time physics",
                    "video_search_query": "ball thrown upwards free fall calculus kinematics physics",
                    "what_to_make": "Cartesian y-t plot with apex at (2s, 20m) and ground landing at t = 5s",
                    "what_to_explain": "Show symmetry of ascent and descent and continuous downward acceleration g",
                    "timing_and_cue": "Step 2 (Calculus Derivation)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "A stone is dropped from a balloon rising upwards with a velocity of 12 m/s when the balloon is at a height of 65 m. What is the initial velocity of the stone?",
                            "ideal_answer": "The stone possesses the inertia of motion of the balloon at the instant of release; therefore, its initial velocity is +12 m/s upwards!",
                            "socratic_hint": "Does an object released from a moving vehicle start from rest or retain the vehicle's speed?",
                            "type": "Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 5: Relative Velocity in 1D, Stopping Distance & Reaction Time
    # Date: 2026-11-21
    # -------------------------------------------------------------
    mod5_svg = sb.build_cartesian_kinematics_svg(
        domain=(0, 8), range_y=(0, 40),
        lines=[
            {'p1': (0, 0), 'p2': (8, 40), 'color': '#2563EB', 'label': 'Car A (v_A = 5 m/s)'},
            {'p1': (0, 10), 'p2': (8, 26), 'color': '#16A34A', 'label': 'Car B (v_B = 2 m/s)'}
        ],
        points=[{'x': 3.33, 'y': 16.67, 'label': 'Overtake Point (t = 3.33 s)'}],
        x_label="Time t (s)", y_label="Position x (m)",
        title="Relative Velocity in 1D: Overtaking Dynamics",
        caption="Relative velocity v_AB = v_A - v_B = 5 - 2 = 3 m/s; Overtake time = separation / v_AB"
    )
    modules.append({
        "order_index": 10,
        "title": "Relative Velocity in One Dimension, Stopping Distance of Vehicles & Human Reaction Time",
        "description": "Formulation of 1D relative velocity (v_AB = v_A - v_B), position-time graphs of two bodies, stopping distance formula (v₀² / 2a), and experimental determination of human reaction time.",
        "target_completion_date": "2026-11-21",
        "syllabus_pacing": "Day 10 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Definition of Relative Velocity: Rate of change of position of object A relative to object B",
            "Formula for Relative Velocity in 1D: v_{AB} = v_A - v_B and v_{BA} = v_B - v_A = -v_{AB}",
            "Special cases: Same direction (v_A - v_B), opposite direction (v_A + v_B)",
            "x-t graphs for relative velocity: Parallel lines (v_A = v_B), intersecting lines (overtake)",
            "Stopping distance of a vehicle under braking: d_s = v₀² / (2a)",
            "Dependence of stopping distance on initial speed squared (d_s ∝ v₀²)",
            "Human reaction time (t_r) and ruler drop experiment: t_r = √(2d / g)",
            "Total stopping distance = Reaction distance (v₀ t_r) + Braking distance (v₀² / 2a)"
        ],
        "key_concepts": [
            "Relative Velocity Formula v_{AB} = v_A - v_B",
            "Stopping Distance d_s = v₀² / (2a)",
            "Human Reaction Time t_r = √(2d / g)",
            "Total Stopping Distance (v₀ t_r + v₀²/2a)"
        ],
        "success_criteria": [
            "Calculate relative velocity for bodies moving in same and opposite directions",
            "Determine the time and location where two vehicles cross or overtake each other",
            "Derive and explain why doubling vehicle speed quadruples the stopping distance",
            "Compute human reaction time from distance fallen by a dropped ruler"
        ],
        "chapter_notes": """# CHAPTER 2: MOTION IN A STRAIGHT LINE
## MODULE 5: Relative Velocity, Stopping Distance & Reaction Time

### 1. Relative Velocity in One Dimension
Let two objects $A$ and $B$ move along the $x$-axis with constant velocities $v_A$ and $v_B$:
$$x_A(t) = x_A(0) + v_A t, \\quad x_B(t) = x_B(0) + v_B t$$
Displacement of $B$ relative to $A$:
$$x_{BA}(t) = x_B(t) - x_A(t) = [x_B(0) - x_A(0)] + (v_B - v_A) t$$
Differentiating with respect to $t$:
$$v_{BA} = \\frac{d}{dt} x_{BA} = v_B - v_A$$
- **Relative velocity of $A$ with respect to $B$**:
  $$v_{AB} = v_A - v_B$$
- **Properties**:
  1. $v_{AB} = -v_{BA}$
  2. If both move in **same direction**: Relative speed is difference $|v_A - v_B|$.
  3. If they move in **opposite directions**: Take $v_B$ as negative $\\implies v_{AB} = v_A - (-v_B) = v_A + v_B$ (Speeds add up!).

### 2. Stopping Distance of Vehicles
When brakes are applied, vehicle undergoes constant retardation $a$:
$$v^2 = v_0^2 - 2 a d_s$$
Setting final velocity $v = 0$:
$$d_s = \\frac{v_0^2}{2a}$$
*Key Road Safety Insight*:
$$d_s \\propto v_0^2$$
If initial speed is doubled ($v_0 \\to 2v_0$), the stopping distance increases by a factor of **4**!

### 3. Human Reaction Time & Total Stopping Distance
- **Reaction Time ($t_r$)**: The time a person takes to observe, think, and initiate action.
- **Ruler Drop Method**: A ruler drops freely under gravity ($v_0 = 0$) distance $d$ before being caught:
  $$d = \\frac{1}{2} g t_r^2 \\implies t_r = \\sqrt{\\frac{2d}{g}}$$
- **Total Stopping Distance**:
  $$D_{\\text{total}} = \\text{Reaction distance} + \\text{Braking distance} = v_0 \\, t_r + \\frac{v_0^2}{2a}$$
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 2.7: Measuring Reaction Time: When a situation demands our immediate action, it takes some time before we really respond. Reaction time is the time a person takes to observe, think and act. For example, if a person is driving and suddenly a boy appears on the road, then the time elapsed before he applies the brakes is the reaction time. Take a ruler and ask your friend to drop it vertically through the gap between your thumb and index finger. As soon as it is dropped, catch it. Suppose the distance slipped by the ruler is measured to be 21.0 cm. Estimate your reaction time. (Take g = 9.8 m/s²).",
                "given": "d = 21.0 cm = 0.21 m, initial velocity v₀ = 0, a = g = 9.8 m/s².",
                "formula": "d = ½ g t_r² => t_r = √(2d / g)",
                "substitution": "t_r = √[ (2 × 0.21 m) / (9.8 m/s²) ] = √(0.42 / 9.8) = √(0.042857)",
                "calculation": "t_r = 0.207 s ≈ 0.21 s.",
                "finalAnswer": "Reaction time t_r ≈ 0.21 s (approx 0.2 s)",
                "unit": "s",
                "has_diagram": True,
                "diagram_svg": mod5_svg
            }
        ],
        "common_misconceptions": [
            "Assuming stopping distance doubles when speed doubles: Stopping distance is proportional to v₀², so doubling speed QUADRUPLES the braking distance!",
            "Neglecting reaction distance in real accident calculations: The car travels at full unreduced speed during the human reaction time (v₀ × t_r) before brakes even engage."
        ],
        "visual_lesson_plan": {
            "diagram_type": "graph",
            "svg": mod5_svg,
            "interactive_math_formula": "5*x; 2*x + 10",
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Relative Velocity Formula v_{AB} = v_A - v_B",
                    "diagram_title": "Linear Overtaking Graph of Two Moving Vehicles",
                    "diagram_type": "graph",
                    "svg": mod5_svg,
                    "interactive_math_formula": "5*x; 2*x + 10",
                    "image_search_query": "relative velocity two cars overtaking physics graph",
                    "video_search_query": "relative velocity in one dimension physics animation",
                    "what_to_make": "Dual lines on x-t plane intersecting at overtake time t = 3.33s",
                    "what_to_explain": "Show how slope difference determines rate of closure between vehicles",
                    "timing_and_cue": "Step 2 (Analytical Formulation)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "Two trains 120 m and 80 m in length are running in opposite directions with velocities 42 km/h and 30 km/h. In what time will they completely pass each other?",
                            "ideal_answer": "Total distance to clear = 120 + 80 = 200 m. Relative velocity = 42 + 30 = 72 km/h = 72 × (5/18) = 20 m/s. Time = Distance / Relative speed = 200 / 20 = 10 s.",
                            "socratic_hint": "Do opposite velocities add or subtract? What is the total length to be cleared?",
                            "type": "Board Exam Numerical"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 6: Complete NCERT Exercise Solver (Ex 2.1 to 2.18)
    # Date: 2026-11-21
    # -------------------------------------------------------------
    modules.append({
        "order_index": 11,
        "title": "Exercise 2.1 to 2.18 Complete Solver: Straight Line Kinematics Mastery",
        "description": "Exhaustive step-by-step solutions to every textbook exercise question (Exercises 2.1 to 2.18) including drunkard random walk, police van firing bullet, and overtaking trains.",
        "target_completion_date": "2026-11-21",
        "syllabus_pacing": "Day 10 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 60,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Exercise 2.1: Point object approximation verification for railway carriage, monkey, cricket ball",
            "Exercise 2.2: Position-time graphs analysis for school children walking home",
            "Exercise 2.3: Woman walking to office and returning in auto-rickshaw x-t plot",
            "Exercise 2.4: Drunkard taking 5 steps forward and 3 steps backward falling into pit",
            "Exercise 2.5: Jet airplane speed and ejected products relative velocity",
            "Exercise 2.6: Car on highway speed 126 km/h stopping distance in 200 m",
            "Exercise 2.7 to 2.12: Two trains on parallel tracks, speed limit, ball dropped from elevator",
            "Exercise 2.13 to 2.18: Look and explain graphs, balls colliding, acceleration sign proofs"
        ],
        "key_concepts": [
            "Point Object Criteria",
            "Drunkard Walk Periodic Pacing",
            "Police Van & Speeding Car Relative Bullet Speed",
            "Complete Exercise Solver (2.1 to 2.18)"
        ],
        "success_criteria": [
            "Solve all 18 textbook exercises with step-by-step layout and boxed answers",
            "Solve the jet plane ejection problem with relative velocity sign rigor",
            "Calculate the exact pit-fall time for periodic step walks",
            "Attain 100% mastery of 1D Kinematics for CBSE Mid-Term Examination"
        ],
        "chapter_notes": """# CHAPTER 2: MOTION IN A STRAIGHT LINE
## MODULE 6: Complete NCERT Exercise Solver

### Summary of Key Exercise Solutions
- **Exercise 2.4 (Drunkard Walk)**:
  - Takes $5\\text{ m}$ forward in $5\\text{ s}$, then $3\\text{ m}$ backward in $3\\text{ s}$.
  - Net progress in one cycle ($8\\text{ s}$) $= 5 - 3 = 2\\text{ m}$.
  - Pit is at $13\\text{ m}$.
  - In $4$ complete cycles ($4 \\times 8 = 32\\text{ s}$), distance covered $= 4 \\times 2 = 8\\text{ m}$.
  - In the next forward step, drunkard moves $5\\text{ m}$ forward: $8 + 5 = 13\\text{ m}$!
  - Time taken for this final $5\\text{ m} = 5\\text{ s}$.
  - **Total time to fall into pit** $= 32 + 5 = 37\\text{ s}$!

- **Exercise 2.5 (Jet Airplane Ejection)**:
  - Jet speed $v_J = 500\\text{ km/h}$ forward.
  - Ejection speed relative to jet $v_{C/J} = -1500\\text{ km/h}$ (backward).
  - Velocity of combustion products relative to ground observer $v_C$:
    $$v_{C/J} = v_C - v_J \\implies v_C = v_{C/J} + v_J = -1500 + 500 = -1000\\text{ km/h}$$
    Magnitude is $1000\\text{ km/h}$ in direction opposite to jet motion.
""",
        "worked_examples": [
            {
                "problem": "NCERT Exercise 2.4: A drunkard walking in a narrow lane takes 5 steps forward and 3 steps backward, followed again by 5 steps forward and 3 steps backward, and so on. Each step is 1 m long and requires 1 s. Determine how long the drunkard takes to fall into a pit 13 m away from the start.",
                "given": "Step length = 1 m, time per step = 1 s; Forward = 5 steps (5 m in 5 s); Backward = 3 steps (3 m in 3 s); Pit location = 13 m.",
                "formula": "Net displacement per 8-second cycle = 5 m - 3 m = 2 m. Notice in the last cycle, reaching 13 m drops him into the pit before stepping backward!",
                "substitution": "Distance before final 5-meter dash = 13 m - 5 m = 8 m. Number of full 2-meter cycles = 8 m / 2 m = 4 cycles. Time for 4 cycles = 4 × 8 s = 32 s. Time for final 5 meters forward = 5 s.",
                "calculation": "Total time = 32 s + 5 s = 37 s.",
                "finalAnswer": "Total time taken to fall into pit = 37 s",
                "unit": "s",
                "has_diagram": True,
                "diagram_svg": mod5_svg
            },
            {
                "problem": "NCERT Exercise 2.5: A jet airplane travelling at the speed of 500 km h⁻¹ ejects its products of combustion at the speed of 1500 km h⁻¹ relative to the jet plane. What is the speed of the latter with respect to an observer on the ground?",
                "given": "Speed of jet v_J = +500 km/h; Speed of combustion products relative to jet v_{C/J} = -1500 km/h.",
                "formula": "v_{C/J} = v_C - v_J => v_C = v_{C/J} + v_J",
                "substitution": "v_C = -1500 km/h + 500 km/h = -1000 km/h",
                "calculation": "|v_C| = 1000 km/h in opposite direction to motion of plane.",
                "finalAnswer": "Speed of combustion products relative to ground observer = 1000 km/h (in direction opposite to plane)",
                "unit": "km/h",
                "has_diagram": True,
                "diagram_svg": mod5_svg
            }
        ],
        "common_misconceptions": [
            "Simply dividing 13 m by 2 m/8s (which gives 52 s): The drunkard falls into the pit on his forward dash at 37 s, so he never takes the subsequent backward steps!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "graph",
            "svg": mod5_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Drunkard Walk Periodic Pacing",
                    "diagram_title": "Sawtooth Position-Time Walk to Pit",
                    "diagram_type": "graph",
                    "svg": mod5_svg,
                    "image_search_query": "drunkard walk physics problem position time graph",
                    "video_search_query": "drunkard walk physics problem ncert solution animation",
                    "what_to_make": "Sawtooth graph showing +5, -3 step intervals terminating at x = 13m and t = 37s",
                    "what_to_explain": "Explain why the final forward dash terminates the motion before backward steps occur",
                    "timing_and_cue": "Step 2 (Solution Walkthrough)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "Can an object have eastward velocity and westward acceleration simultaneously?",
                            "ideal_answer": "Yes. When a car moving eastward applies brakes, its velocity is eastward while its acceleration (retardation) is directed westward.",
                            "socratic_hint": "Think about what acceleration means when speed is decreasing.",
                            "type": "Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    return modules
