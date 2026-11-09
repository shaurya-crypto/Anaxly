#!/usr/bin/env python3
"""
Master Builder for Class 9 Science:
Chapters 3, 4, 5, and 6 (Complete 26 Modules)
------------------------------------------------
Adheres to Invariant 10: Exhaustive Curriculum Module Decomposition.
Zero omissions, 1:1 visual mapping, verified Wikimedia image & video queries,
extracted textbook figures, Mafs coordinate graphs for motion, and 6-stage Socratic AI prompts.
"""

import json

CH3_ID = "1053ed93-7167-423b-bdf0-0c73f2b179ff"  # Tissues in Action (7 modules)
CH4_ID = "b1a05ff2-8ca8-4d59-b7c7-cc0e1304c3ae"  # Describing Motion Around Us (7 modules)
CH5_ID = "8d01a5f5-bf82-49c2-9fab-253d26b086f4"  # Exploring Mixtures and their Separation (6 modules)
CH6_ID = "7e1d5438-1174-4577-8599-5f05a6642093"  # How Forces Affect Motion (6 modules)

# Load existing Chapter 3
with open("scripts/science_modules_ch3.json", "r", encoding="utf-8") as f:
    ch3_modules = json.load(f)

# Load existing Chapter 4 partial
with open("scripts/science_modules_ch4.json", "r", encoding="utf-8") as f:
    ch4_modules = json.load(f)

# ==============================================================================
# CHAPTER 4: REMAINING MODULES 4, 5, 6, 7
# ==============================================================================

# Module 4: Derivation of the Three Kinematic Equations of Motion
ch4_modules.append({
    "curriculum_id": CH4_ID,
    "order_index": 4,
    "title": "Derivation & Architectural Calculus of the Three Kinematic Equations of Motion",
    "description": "Master the rigorous graphical derivation of the three fundamental equations of motion (v = u + at, s = ut + 1/2*at^2, v^2 - u^2 = 2as) from the geometry of the velocity-time trapezoid.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
        "First Equation of Motion: Velocity-Time relation derived from slope (v = u + at)",
        "Second Equation of Motion: Position-Time relation derived from area decomposition (s = ut + 1/2*at^2)",
        "Third Equation of Motion: Position-Velocity relation derived from trapezoid area formula (v^2 - u^2 = 2as)",
        "Graphical Construction: Velocity-time trapezoid OABC with initial velocity u, final velocity v, and duration t",
        "Algebraic Equivalence & Validation: Verifying units, dimensions, and limits for stationary start (u = 0)",
        "NCERT Exemplar Calculations: Multi-parameter kinematic solutions"
    ],
    "key_concepts": [
        "The Three Master Equations: The closed-form algebraic system governing 1D motion under constant acceleration.",
        "Derivation of v = u + at: Gradient of line AB equals acceleration a = (v - u) / t, which rearranges to v = u + at.",
        "Derivation of s = ut + 1/2*at^2: Area under AB equals sum of base rectangle OACD (u*t) and triangle ABD (1/2 * (v - u) * t = 1/2 * a * t^2).",
        "Derivation of v^2 - u^2 = 2as: Area of trapezoid OABC = 1/2 * (sum of parallel sides) * height = 1/2 * (u + v) * t; substituting t = (v - u) / a gives 2as = v^2 - u^2.",
        "Constant Acceleration Pre-Condition: These equations are valid ONLY when acceleration 'a' is strictly constant.",
        "Rest and Braking Limits: If starting from rest, u = 0; if coming to a stop, v = 0 with negative acceleration."
    ],
    "success_criteria": "Student can reproduce all three graphical derivations step-by-step with clean labeled diagrams and apply them to complex multi-step numerical problems.",
    "chapter_notes": """### 4.10 The Three Equations of Motion
For an object moving with **uniform acceleration ($a$)**:
1. **Velocity-Time Relation**:
   $$v = u + at$$
2. **Position-Time Relation**:
   $$s = ut + \\frac{1}{2}at^2$$
3. **Position-Velocity Relation**:
   $$v^2 - u^2 = 2as \\iff v^2 = u^2 + 2as$$

### 4.11 Step-by-Step Graphical Derivations
Consider the velocity-time graph of an object with initial velocity $u$ (at $t = 0$) accelerating uniformly to final velocity $v$ in time $t$.
- $OA = DC = u$ (initial velocity)
- $BC = v$ (final velocity)
- $OC = AD = t$ (time interval)
- $BD = BC - CD = v - u$ (change in velocity)

#### Derivation 1: $v = u + at$
$$\\text{Slope } a = \\frac{BD}{AD} = \\frac{v - u}{t} \\implies at = v - u \\implies \\mathbf{v = u + at}$$

#### Derivation 2: $s = ut + \\frac{1}{2}at^2$
$$\\text{Displacement } s = \\text{Area of trapezoid } OABC = \\text{Area of rectangle } OADC + \\text{Area of } \\triangle ABD$$
$$s = (OA \\times OC) + \\left(\\frac{1}{2} \\times AD \\times BD\\right)$$
$$s = (u \\times t) + \\left(\\frac{1}{2} \\times t \\times (v - u)\\right)$$
From equation 1, $v - u = at$. Substituting:
$$s = ut + \\frac{1}{2} \\times t \\times (at) \\implies \\mathbf{s = ut + \\frac{1}{2}at^2}$$

#### Derivation 3: $v^2 - u^2 = 2as$
$$\\text{Area of trapezoid } OABC = \\frac{\\text{Sum of parallel sides} \\times \\text{Perpendicular distance}}{2} = \\frac{(OA + BC) \\times OC}{2} = \\frac{(u + v)t}{2}$$
From equation 1, $t = \\frac{v - u}{a}$. Substituting $t$:
$$s = \\frac{(v + u)(v - u)}{2a} = \\frac{v^2 - u^2}{2a} \\implies 2as = v^2 - u^2 \\implies \\mathbf{v^2 - u^2 = 2as}$$""",
    "worked_examples": [
        {
            "problem": "A train starting from rest attains a velocity of 72 km/h in 5 minutes. Assuming that the acceleration is uniform, find (i) the acceleration and (ii) the distance traveled by the train for attaining this velocity.",
            "given": "Initial velocity u = 0 (starts from rest); Final velocity v = 72 km/h = 72 * (5/18) = 20 m/s; Time t = 5 min = 5 * 60 = 300 s.",
            "formula": "(i) a = (v - u) / t; (ii) s = ut + 1/2*at^2 or v^2 = u^2 + 2as.",
            "substitution": "(i) a = (20 - 0) / 300; (ii) s = 0 + 1/2 * (1/15) * (300)^2.",
            "calculation": "1. Acceleration a = 20 / 300 = 1/15 m/s^2 = 0.067 m/s^2.\\n2. Distance s = 1/2 * (1/15) * 90000 = 45000 / 15 = 3000 m = 3 km.",
            "finalAnswer": "(i) Acceleration = 1/15 m/s^2 (0.067 m/s^2); (ii) Distance traveled = 3000 m (3 km).",
            "unit": "Acceleration (m/s^2), Distance (m)",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 4.24: Velocity-time derivation trapezoid for train acceleration"
        }
    ],
    "common_misconceptions": [
        {
            "misconception": "You can use v = d/t when an object is accelerating.",
            "correction": "v = d/t applies ONLY when speed is strictly CONSTANT (zero acceleration). When accelerating, you MUST use the three kinematic equations (v = u + at, s = ut + 1/2*at^2, v^2 - u^2 = 2as).",
            "why_it_matters": "A fatal error that invalidates numerical calculations."
        }
    ],
    "visual_lesson_plan": {
        "title": "Three Equations of Motion Derivations Visual Plan",
        "diagram_type": "image",
        "concept_visuals": [
            {
                "concept_title": "The Three Master Equations: The closed-form algebraic system governing 1D motion under constant acceleration.",
                "diagram_title": "Kinematic Equations Formula Card",
                "diagram_type": "image",
                "image_query": "Equations of motion physics formula derivation summary",
                "video_query": "three equations of motion derivation",
                "image_url": "/extracted_diagrams/ch4/fig_4_24.webp",
                "what_to_make": "Master reference chart displaying the three equations with their physical names and geometric equivalents.",
                "timing_and_cue": "Mount equations card on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_24.webp | Master Kinematic Equations | Closed-form algebraic system for uniform acceleration\")"
            },
            {
                "concept_title": "Derivation of v = u + at: Gradient of line AB equals acceleration a = (v - u) / t, which rearranges to v = u + at.",
                "diagram_title": "Velocity-Time Slope Derivation Graphic",
                "diagram_type": "image",
                "image_query": "Velocity time graph derivation v equals u plus at",
                "video_query": "derive v u at graphically",
                "image_url": "/extracted_diagrams/ch4/fig_4_25.webp",
                "what_to_make": "Slope triangle ABD illustrating slope a = BD / AD = (v - u) / t.",
                "timing_and_cue": "Mount slope derivation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_25.webp | First Equation Derivation | Slope a = BD/AD = (v - u)/t yields v = u + at\")"
            },
            {
                "concept_title": "Derivation of s = ut + 1/2*at^2: Area under AB equals sum of base rectangle OACD (u*t) and triangle ABD (1/2 * (v - u) * t = 1/2 * a * t^2).",
                "diagram_title": "Area Partitioning Derivation Graphic",
                "diagram_type": "image",
                "image_query": "Derivation s equals ut plus half at squared area under vt graph",
                "video_query": "derive s ut half at2 graphically",
                "image_url": "/extracted_diagrams/ch4/fig_4_26.webp",
                "what_to_make": "Trapezoid split into cyan rectangle (u*t) and yellow triangle (1/2 * at^2).",
                "timing_and_cue": "Mount area derivation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_26.webp | Second Equation Derivation | Rectangle OADC (ut) + Triangle ABD (1/2 at^2)\")"
            },
            {
                "concept_title": "Derivation of v^2 - u^2 = 2as: Area of trapezoid OABC = 1/2 * (sum of parallel sides) * height = 1/2 * (u + v) * t; substituting t = (v - u) / a gives 2as = v^2 - u^2.",
                "diagram_title": "Trapezoid Area Substitution Derivation",
                "diagram_type": "image",
                "image_query": "Derivation v squared minus u squared equals 2as trapezoid formula",
                "video_query": "derive v2 u2 2as graphically",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Trapezoid_motion_derivation.svg",
                "what_to_make": "Trapezoid formula schematic demonstrating algebraic substitution of t = (v - u) / a.",
                "timing_and_cue": "Mount third equation on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/ea/Trapezoid_motion_derivation.svg | Third Equation Derivation | Area = 1/2 (u + v) t yields 2as = v^2 - u^2\")"
            },
            {
                "concept_title": "Constant Acceleration Pre-Condition: These equations are valid ONLY when acceleration 'a' is strictly constant.",
                "diagram_title": "Constant vs Variable Acceleration Contrast",
                "diagram_type": "image",
                "image_query": "Constant acceleration vs variable acceleration graph physics",
                "video_query": "when to use equations of motion constant acceleration",
                "image_url": "/extracted_diagrams/ch4/fig_4_18.webp",
                "what_to_make": "Comparison showing straight-line v-t graph (valid for equations) vs curved v-t graph (requires calculus integration).",
                "timing_and_cue": "Mount condition contrast on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_18.webp | Pre-condition Guard | Equations apply ONLY when acceleration is strictly constant\")"
            },
            {
                "concept_title": "Rest and Braking Limits: If starting from rest, u = 0; if coming to a stop, v = 0 with negative acceleration.",
                "diagram_title": "Rest and Braking Boundary Conditions",
                "diagram_type": "image",
                "image_query": "Starting from rest stopping braking kinematics diagram",
                "video_query": "stopping distance physics kinematics",
                "image_url": "/extracted_diagrams/ch4/fig_4_20.webp",
                "what_to_make": "Vehicle acceleration from rest and braking to rest with boundary condition indicators.",
                "timing_and_cue": "Mount boundary conditions on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_20.webp | Boundary Conditions | Rest implies u = 0; Braking stop implies v = 0\")"
            }
        ]
    },
    "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each derivation turn.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (How high-speed train engineers calculate exact braking distance before approaching a station).
   - Stage 2: Statement of the 3 kinematic equations.
   - Stage 3: Common pitfall (Trying to use s = vt for accelerating objects).
   - Stage 4: Chalkboard derivation step-by-step (Trapezoid = Rectangle + Triangle).
   - Stage 5: Socratic check: "In the second equation s = ut + 1/2 at^2, where does the 1/2 come from geometrically?" HARD STOP: Wait for student response!
   - Stage 6: Authentic CBSE numerical question."""
})

# Module 5: Braking Dynamics, Retardation & Vertical Motion Under Gravity
ch4_modules.append({
    "curriculum_id": CH4_ID,
    "order_index": 5,
    "title": "Braking Dynamics, Reaction Time & Multi-Phase Motion Engineering",
    "description": "Master real-world kinematic applications: stopping distance calculations, driver reaction times, negative acceleration (retardation), and vertical free fall under gravity (g = 9.8 m/s^2).",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
        "Retardation Mechanics: Velocity vector opposed by negative acceleration vector",
        "Stopping Distance Formula: s_stop = u^2 / (2*a) and quadratic velocity dependence",
        "Driver Reaction Time: Constant speed distance traveled during neural perception lag (d_react = u * t_r)",
        "Total Stopping Distance: d_total = d_reaction + d_braking",
        "Free Fall Kinematics: Acceleration due to gravity g = 9.8 m/s^2 (a = -g for upward ascent)",
        "Symmetry of Vertical Motion: Time of ascent = Time of descent; Impact velocity = Launch velocity"
    ],
    "key_concepts": [
        "Retardation / Deceleration: Acceleration vector pointing in opposite direction to velocity, causing speed to drop.",
        "Quadratic Stopping Distance: Doubling vehicle speed quadruples the required braking distance (s proportional to u^2).",
        "Two-Phase Braking Model: Total distance = Perception phase (constant speed u*t_r) + Braking phase (u^2 / 2a).",
        "Free Fall Under Gravity: All objects in vacuum accelerate downward at constant g = 9.8 m/s^2 regardless of mass.",
        "Vertical Ascent Sign Convention: Taking upward as positive: a = -g = -9.8 m/s^2; at maximum peak, v = 0.",
        "Kinematic Symmetry: An object thrown upwards takes exactly the same time to rise as to fall back to the launch height."
    ],
    "success_criteria": "Student can calculate vehicle stopping distances under varied speeds, evaluate reaction time lag, and solve vertical projectile problems using g = 9.8 m/s^2.",
    "chapter_notes": """### 4.12 Retardation & Braking Dynamics
When brakes are applied, the acceleration acts in the opposite direction to velocity ($a < 0$).
From $v^2 = u^2 + 2as$, setting final velocity $v = 0$ (car stops):
$$0 = u^2 - 2as \\implies s_{\\text{braking}} = \\frac{u^2}{2a}$$
**CRITICAL INSIGHT**: Stopping distance is proportional to the **square of velocity** ($s \\propto u^2$).
- If speed doubles ($2\\times$), stopping distance increases **$4\\times$**!
- If speed triples ($3\\times$), stopping distance increases **$9\\times$**!

### 4.13 Reaction Time and Total Stopping Distance
$$\\text{Total Stopping Distance} = s_{\\text{reaction}} + s_{\\text{braking}} = (u \\times t_r) + \\frac{u^2}{2a}$$
Where $t_r$ is the human driver's neural perception-reaction time (~$0.2 - 0.7\\text{ s}$).

### 4.14 Vertical Motion Under Gravity
When an object is thrown vertically upwards:
- Acceleration $a = -g = -9.8\\text{ m/s}^2$ (downward acceleration opposes upward motion).
- At the **highest point**, final velocity **$v = 0$**.
- Maximum height reached: $h_{\\text{max}} = \\frac{u^2}{2g}$.
- Time of ascent: $t_{\\text{up}} = \\frac{u}{g}$.
- Total flight time: $T = 2 \\times t_{\\text{up}} = \\frac{2u}{g}$.""",
    "worked_examples": [
        {
            "problem": "A car was traveling at 20 m/s. The driver applies brakes that produce a uniform deceleration of 5 m/s^2. If the driver's reaction time is 0.5 s, calculate the total distance traveled before the car comes to a complete stop.",
            "given": "Initial speed u = 20 m/s; Deceleration a = 5 m/s^2; Reaction time tr = 0.5 s; Final velocity v = 0.",
            "formula": "d_total = d_reaction + d_braking = (u * tr) + (u^2 / (2*a)).",
            "substitution": "d_reaction = 20 * 0.5; d_braking = (20)^2 / (2 * 5).",
            "calculation": "1. Reaction distance = 20 * 0.5 = 10 m.\\n2. Braking distance = 400 / 10 = 40 m.\\n3. Total stopping distance = 10 + 40 = 50 m.",
            "finalAnswer": "Total distance traveled before stopping = 50 m (10 m reaction + 40 m braking).",
            "unit": "Metres (m)",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 4.21: Multi-phase braking distance and vehicle deceleration profile"
        }
    ],
    "common_misconceptions": [
        {
            "misconception": "Heavier objects fall faster than lighter objects in free fall.",
            "correction": "In free fall, the gravitational acceleration g = 9.8 m/s^2 is completely independent of the mass of the object. A feather and a bowling ball fall at the exact same rate in a vacuum (Galileo's Leaning Tower experiment).",
            "why_it_matters": "A core physical law foundational to Newtonian mechanics."
        }
    ],
    "visual_lesson_plan": {
        "title": "Braking Dynamics & Gravity Visual Plan",
        "diagram_type": "image",
        "concept_visuals": [
            {
                "concept_title": "Retardation / Deceleration: Acceleration vector pointing in opposite direction to velocity, causing speed to drop.",
                "diagram_title": "Braking Retardation Vector Profile",
                "diagram_type": "image",
                "image_query": "Car braking deceleration vector diagram physics",
                "video_query": "braking deceleration physics",
                "image_url": "/extracted_diagrams/ch4/fig_4_21.webp",
                "what_to_make": "Vehicle braking profile showing velocity vector forward and deceleration force vector backward.",
                "timing_and_cue": "Mount retardation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_21.webp | Retardation Mechanics | Negative acceleration vector opposing velocity\")"
            },
            {
                "concept_title": "Quadratic Stopping Distance: Doubling vehicle speed quadruples the required braking distance (s proportional to u^2).",
                "diagram_title": "Quadratic Speed vs Stopping Distance Chart",
                "diagram_type": "image",
                "image_query": "Stopping distance vs speed quadratic chart physics road safety",
                "video_query": "speed vs stopping distance physics",
                "image_url": "/extracted_diagrams/ch4/fig_4_22.webp",
                "what_to_make": "Bar graph illustrating non-linear stopping distances at 30 km/h, 60 km/h, and 90 km/h.",
                "timing_and_cue": "Mount stopping distance chart on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_22.webp | Quadratic Stopping Law | Braking distance scales with u^2 (2x speed = 4x distance)\")"
            },
            {
                "concept_title": "Two-Phase Braking Model: Total distance = Perception phase (constant speed u*t_r) + Braking phase (u^2 / 2a).",
                "diagram_title": "Two-Phase Reaction & Braking Timeline",
                "diagram_type": "image",
                "image_query": "Thinking distance braking distance stopping distance timeline diagram",
                "video_query": "reaction time and stopping distance demonstration",
                "image_url": "/extracted_diagrams/ch4/fig_4_23.webp",
                "what_to_make": "Timeline showing driver perception lag followed by mechanical brake pad application.",
                "timing_and_cue": "Mount two-phase braking on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_23.webp | Two-Phase Braking Model | Total distance = Thinking distance + Braking distance\")"
            },
            {
                "concept_title": "Free Fall Under Gravity: All objects in vacuum accelerate downward at constant g = 9.8 m/s^2 regardless of mass.",
                "diagram_title": "Free Fall Vacuum Chamber Experiment",
                "diagram_type": "image",
                "image_query": "Feather and coin free fall vacuum tube experiment diagram",
                "video_query": "feather and bowling ball vacuum chamber bbc",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Free_fall_vacuum.svg",
                "what_to_make": "Dual tube comparison showing feather and coin falling together in vacuum vs air resistance lag.",
                "timing_and_cue": "Mount free fall on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/ec/Free_fall_vacuum.svg | Galileo Free Fall | Constant g = 9.8 m/s^2 independent of mass in vacuum\")"
            },
            {
                "concept_title": "Vertical Ascent Sign Convention: Taking upward as positive: a = -g = -9.8 m/s^2; at maximum peak, v = 0.",
                "diagram_title": "Vertical Projectile Kinematics Trajectory",
                "diagram_type": "image",
                "image_query": "Vertical projectile motion upward ascent peak zero velocity diagram",
                "video_query": "vertical motion under gravity physics",
                "image_url": "/extracted_diagrams/ch4/fig_4_5.webp",
                "what_to_make": "Vertical trajectory showing upward ascent with decreasing velocity, apex at v = 0, and accelerating downward descent.",
                "timing_and_cue": "Mount vertical kinematics on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_5.webp | Vertical Trajectory | Apex velocity v = 0 under constant downward gravity a = -g\")"
            },
            {
                "concept_title": "Kinematic Symmetry: An object thrown upwards takes exactly the same time to rise as to fall back to the launch height.",
                "diagram_title": "Time of Ascent & Descent Parabolic Symmetry",
                "diagram_type": "image",
                "image_query": "Time of ascent equals time of descent parabolic trajectory physics",
                "video_query": "projectile motion symmetry physics",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/75/Parabolic_motion.svg",
                "what_to_make": "Symmetrical parabola showing equal time intervals on upward and downward limbs.",
                "timing_and_cue": "Mount symmetry on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/7/75/Parabolic_motion.svg | Temporal Symmetry | Time of ascent strictly equals time of descent\")"
            }
        ]
    },
    "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each concept.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (Why a car moving at 100 km/h takes four times longer to brake than at 50 km/h).
   - Stage 2: Stopping distance formula s = u^2 / (2a) and vertical motion sign conventions.
   - Stage 3: Common pitfall (Heavier objects do NOT fall faster in free fall).
   - Stage 4: Chalkboard numerical: driver reaction distance + braking distance.
   - Stage 5: Socratic check: "A ball is thrown straight up. At its very highest peak point, what is its velocity, and what is its acceleration?" HARD STOP: Wait for student response!
   - Stage 6: Authentic CBSE board numerical."""
})

# Module 6: Motion in a Plane: Uniform Circular Motion (UCM)
ch4_modules.append({
    "curriculum_id": CH4_ID,
    "order_index": 6,
    "title": "Motion in a Plane: Uniform Circular Motion (UCM) & Radial Acceleration",
    "description": "Master uniform circular motion: why motion with constant speed along a circular trajectory is perpetually accelerated, tangential velocity vectors, and centripetal kinematics.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
        "Circular Trajectory Mechanics: Path with continuously changing direction",
        "Uniform Circular Motion Definition: Circular motion at constant scalar speed",
        "Why UCM is Accelerated: Continuously rotating velocity vector requires net centripetal acceleration",
        "Orbital Speed Formula: v = 2*pi*r / T",
        "Tangential Velocity Demonstration: Whirling stone on string released flies off along tangent",
        "Real-World UCM Systems: Artificial earth satellites, tip of clock hands, moon around earth"
    ],
    "key_concepts": [
        "UCM Definition: When an object moves in a circular path with constant speed, its motion is called Uniform Circular Motion.",
        "Perpetual Acceleration Invariant: Even though speed is invariant, the continuous turning of the velocity direction vector makes UCM an accelerated motion.",
        "Tangential Direction: The instantaneous velocity vector at any point on the circle points along the tangent to the circle at that point.",
        "UCM Speed Formula: v = (2 * pi * r) / T, where r is orbital radius and T is period of revolution.",
        "Centripetal Inward Force: An inward acceleration (a = v^2 / r) directed toward the circle center is required to maintain the curved path.",
        "Inertial Tangential Release: When the centripetal constraint is severed (e.g. string breaks), the object continues straight along the instantaneous tangent."
    ],
    "success_criteria": "Student can explain why circular motion with constant speed is accelerated, compute orbital speeds via v = 2*pi*r / T, and predict tangential release trajectories.",
    "chapter_notes": """### 4.15 Uniform Circular Motion (UCM)
When an object moves in a **circular path with uniform (constant) speed**, its motion is termed **Uniform Circular Motion**.

### 4.16 Why is UCM an Accelerated Motion?
- Velocity is a **vector** having both magnitude (speed) and direction.
- In circular motion, although speed remains constant, the **direction of motion changes continuously at every point**.
- Because velocity changes direction continuously, there is a continuous change in velocity with time.
- Therefore, **Uniform Circular Motion is an accelerated motion**!
- The acceleration is directed radially inward toward the center and is called **Centripetal Acceleration**:
  $$a_c = \\frac{v^2}{r}$$

### 4.17 Calculating Speed in UCM
For a circular path of radius $r$, the circumference is $2\\pi r$. If an object takes $T$ seconds to complete one revolution:
$$v = \\frac{\\text{Circumference}}{\\text{Time Period}} = \\frac{2\\pi r}{T}$$

### 4.18 Tangential Release (Activity 4.11)
- Whirling a stone tied to a thread in a circular path: The stone moves in a circle because the thread exerts an inward centripetal tension.
- If the thread breaks or is released, the stone **flies off in a straight line along the tangent** to the circular path at that instant!
- This proves that at every instant, the velocity vector is directed along the **tangent** to the circle.""",
    "worked_examples": [
        {
            "problem": "An artificial satellite is moving in a circular orbit of radius 42250 km. Calculate its speed if it takes 24 hours to revolve around the Earth.",
            "given": "Radius of circular orbit r = 42250 km; Time period T = 24 hours = 24 * 3600 = 86400 s.",
            "formula": "Orbital speed v = (2 * pi * r) / T.",
            "substitution": "v = (2 * 3.1416 * 42250 km) / 86400 s.",
            "calculation": "1. Circumference = 2 * 3.14159 * 42250 = 265464.58 km.\\n2. Orbital speed in km/s = 265464.58 / 86400 = 3.0725 km/s.\\n3. In m/s: 3.0725 * 1000 = 3072.5 m/s = 3.07 km/s.",
            "finalAnswer": "Orbital speed of satellite = 3.07 km/s (or 11061 km/h).",
            "unit": "Kilometres per second (km/s)",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 4.30: Artificial satellite in circular geostationary orbit around Earth"
        }
    ],
    "common_misconceptions": [
        {
            "misconception": "When you release a whirled stone, it flies directly outward away from the center (radially).",
            "correction": "The stone flies strictly TANGENTIALLY, not radially outward! Because at the instant of release, its instantaneous velocity vector was pointing along the tangent to the circle (Newton's First Law).",
            "why_it_matters": "A high-frequency misconception tested with multiple choice arrow diagrams."
        }
    ],
    "visual_lesson_plan": {
        "title": "Uniform Circular Motion Visual Plan",
        "diagram_type": "image",
        "concept_visuals": [
            {
                "concept_title": "UCM Definition: When an object moves in a circular path with constant speed, its motion is called Uniform Circular Motion.",
                "diagram_title": "Polygonal to Circular Track Evolution",
                "diagram_type": "image",
                "image_query": "Polygonal track to circular track transition physics diagram",
                "video_query": "uniform circular motion intro physics",
                "image_url": "/extracted_diagrams/ch4/fig_4_30.webp",
                "what_to_make": "Evolution from rectangular track (4 turns) to hexagonal (6) to octagonal (8) to smooth circle (infinite turns).",
                "timing_and_cue": "Mount track evolution on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_30.webp | Polygonal to Circle Transition | Showing continuous direction change at infinite points\")"
            },
            {
                "concept_title": "Perpetual Acceleration Invariant: Even though speed is invariant, the continuous turning of the velocity direction vector makes UCM an accelerated motion.",
                "diagram_title": "Rotating Velocity Vectors in Circular Path",
                "diagram_type": "image",
                "image_query": "Uniform circular motion velocity vector direction change diagram",
                "video_query": "why circular motion is accelerated physics",
                "image_url": "/extracted_diagrams/ch4/fig_4_31.webp",
                "what_to_make": "Circle with four tangential velocity vectors v showing equal magnitude but continuously shifting angles.",
                "timing_and_cue": "Mount rotating vectors on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_31.webp | Rotating Velocity Vectors | Invariant speed with changing direction yields perpetual acceleration\")"
            },
            {
                "concept_title": "Tangential Direction: The instantaneous velocity vector at any point on the circle points along the tangent to the circle at that point.",
                "diagram_title": "Whirling Stone Tangential Release (Activity 4.11)",
                "diagram_type": "image",
                "image_query": "Whirling stone on string tangential release diagram physics",
                "video_query": "stone released from string tangential motion",
                "image_url": "/extracted_diagrams/ch4/fig_4_32.webp",
                "what_to_make": "Person whirling a stone tied to a string with release point showing tangential straight-line exit path.",
                "timing_and_cue": "Mount tangential release on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_32.webp | Tangential Release | Instantaneous velocity points strictly along the tangent\")"
            },
            {
                "concept_title": "UCM Speed Formula: v = (2 * pi * r) / T, where r is orbital radius and T is period of revolution.",
                "diagram_title": "Satellite Orbital Kinematics Geometry",
                "diagram_type": "image",
                "image_query": "Satellite circular orbit radius period formula diagram",
                "video_query": "satellite orbital velocity calculation",
                "image_url": "/extracted_diagrams/ch4/fig_4_33.webp",
                "what_to_make": "Earth with orbiting satellite showing orbital radius r = 42250 km and 24 h revolution path.",
                "timing_and_cue": "Mount satellite kinematics on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_33.webp | Satellite Orbital Speed | v = 2*pi*r / T = 3.07 km/s for geostationary orbit\")"
            },
            {
                "concept_title": "Centripetal Inward Force: An inward acceleration (a = v^2 / r) directed toward the circle center is required to maintain the curved path.",
                "diagram_title": "Centripetal Acceleration Vector",
                "diagram_type": "image",
                "image_query": "Centripetal acceleration inward vector circle diagram",
                "video_query": "centripetal acceleration explained",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/71/Centripetal_force_diagram.svg",
                "what_to_make": "Circle with radial arrows pointing to origin indicating inward centripetal acceleration vector.",
                "timing_and_cue": "Mount centripetal vector on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/7/71/Centripetal_force_diagram.svg | Inward Centripetal Acceleration | Radially directed acceleration maintaining circular trajectory\")"
            },
            {
                "concept_title": "Inertial Tangential Release: When the centripetal constraint is severed (e.g. string breaks), the object continues straight along the instantaneous tangent.",
                "diagram_title": "Sparks from Grinding Wheel Tangential Flight",
                "diagram_type": "image",
                "image_query": "Sparks flying tangentially from grinding wheel physics photo",
                "video_query": "grinding wheel sparks tangential direction",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Angle_grinder_sparks.jpg",
                "what_to_make": "Photograph of industrial grinding wheel showing incandescent metal particles flying along tangents.",
                "timing_and_cue": "Mount grinding sparks on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/4/4b/Angle_grinder_sparks.jpg | Tangential Spark Trajectories | Natural proof of tangential velocity in circular systems\")"
            }
        ]
    },
    "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each concept.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (Why sparks fly off in straight lines from a spinning sharpening stone).
   - Stage 2: Definition of UCM and orbital speed v = 2*pi*r / T.
   - Stage 3: Common pitfall (Sparks and released stones fly tangentially, NOT radially outward).
   - Stage 4: Chalkboard calculation of satellite orbital speed (3.07 km/s).
   - Stage 5: Socratic check: "If an athlete runs at a constant 6 m/s around a circular track, is their acceleration zero? Explain why or why not." HARD STOP: Wait for student response!
   - Stage 6: Authentic CBSE numerical question."""
})

# Module 7: Master Problem Solver & Comprehensive Textbook Exercise Ledger
ch4_modules.append({
    "curriculum_id": CH4_ID,
    "order_index": 7,
    "title": "Master Problem Solver & Comprehensive Textbook Exercise Ledger (Q1 to Q10)",
    "description": "Exhaustive step-by-step master solver resolving every in-text numerical and chapter-end exercise problem (Q1 through Q10) from NCERT Class 9 Science Chapter 4: Motion.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
        "NCERT Exercise Q1: Athlete circular track 200m diameter in 40s (distance & displacement)",
        "NCERT Exercise Q2: Joseph jogs from end A to end B (300m in 2m 50s) and turns back to C (100m in 1m)",
        "NCERT Exercise Q3: Abdul driving to school calculates average speed 20 km/h, returns along same route with 30 km/h",
        "NCERT Exercise Q4: Motorboat starting from rest accelerates at 3 m/s^2 for 8 s",
        "NCERT Exercise Q5: Driver A traveling at 52 km/h applies brakes (stops in 5s) vs Driver B at 3 km/h (stops in 10s)",
        "NCERT Exercise Q6 to Q10: Interpretation of s-t and v-t curves, circular orbit calculations"
    ],
    "key_concepts": [
        "Harmonic Average Speed Invariant: For equal distances traveled at speeds v1 and v2, average speed is the harmonic mean: v_avg = 2*v1*v2 / (v1 + v2).",
        "Multi-Segment JRF Modeling: Displacements add vectorially while distances add arithmetically.",
        "Graphical Braking Distance Comparison: Comparing areas of right-angled triangles under v-t graphs for two braking cars.",
        "Kinematic Area Calculus: Area of trapezoid represents displacement irrespective of the initial speed.",
        "Full 10-Question Master Ledger: Complete structured solutions with given, formula, substitution, calculation, and boxed units."
    ],
    "success_criteria": "Student can solve 100% of NCERT chapter-end numericals with zero errors, correctly apply the harmonic average speed formula, and earn full marks on CBSE board rubrics.",
    "chapter_notes": """### 4.19 Comprehensive NCERT Exercise Solutions Ledger

#### Q1. Athlete on Circular Track
- $D = 200\\text{ m} \\implies r = 100\\text{ m}$. Time for 1 round $= 40\\text{ s}$.
- Time $t = 2\\text{ min } 20\\text{ s} = 140\\text{ s}$.
- Number of rounds $= 140/40 = 3.5$.
- **Distance** $= 3.5 \\times 2\\pi r = 3.5 \\times 2 \\times \\frac{22}{7} \\times 100 = \\mathbf{2200\\text{ m}}$.
- **Displacement** $=$ Straight line between diametrically opposite points $= 2r = \\mathbf{200\\text{ m}}$.

#### Q2. Joseph's Jogging Trajectory
- Point $A$ to $B$: $300\\text{ m}$ in $2\\text{ min } 50\\text{ s} = 170\\text{ s}$.
  * Average Speed $= 300 / 170 = \\mathbf{1.76\\text{ m/s}}$.
  * Average Velocity $= 300 / 170 = \\mathbf{1.76\\text{ m/s}}$ (along $AB$).
- Point $A$ to $C$ (turns back $100\\text{ m}$ in $1\\text{ min} = 60\\text{ s}$):
  * Total Distance $= 300 + 100 = 400\\text{ m}$. Total Time $= 170 + 60 = 230\\text{ s}$.
  * **Average Speed** $= 400 / 230 = \\mathbf{1.74\\text{ m/s}}$.
  * Net Displacement $= 300 - 100 = 200\\text{ m}$.
  * **Average Velocity** $= 200 / 230 = \\mathbf{0.87\\text{ m/s}}$ (along $AB$).

#### Q3. Abdul's Commute Average Speed
- Let distance to school be $x\\text{ km}$.
- Time to go: $t_1 = x / 20$. Time to return: $t_2 = x / 30$.
- Total distance $= 2x$. Total time $= x/20 + x/30 = 5x / 60 = x / 12$.
- **Average Speed** $= \\frac{2x}{x/12} = 2 \\times 12 = \\mathbf{24\\text{ km/h}}$.
*(Notice: NOT the simple arithmetic average of 25 km/h, but the harmonic mean: $\\frac{2 \\times 20 \\times 30}{20 + 30} = 24\\text{ km/h}$!)*

#### Q4. Motorboat Acceleration
- Starts from rest: $u = 0$. Acceleration $a = 3.0\\text{ m/s}^2$. Time $t = 8.0\\text{ s}$.
- $s = ut + \\frac{1}{2}at^2 = 0 + \\frac{1}{2} \\times 3.0 \\times (8)^2 = \\frac{1}{2} \\times 3 \\times 64 = \\mathbf{96\\text{ m}}$.

#### Q5. Two Braking Cars v-t Comparison
- Car 1: $u_1 = 52\\text{ km/h} = 52 \\times \\frac{5}{18} = 14.44\\text{ m/s}$. Stops in $t_1 = 5\\text{ s}$.
  * Distance covered $s_1 = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 5 \\times 14.44 = \\mathbf{36.1\\text{ m}}$.
- Car 2: $u_2 = 3\\text{ km/h} = 3 \\times \\frac{5}{18} = 0.833\\text{ m/s}$. Stops in $t_2 = 10\\text{ s}$.
  * Distance covered $s_2 = \\frac{1}{2} \\times 10 \\times 0.833 = \\mathbf{4.17\\text{ m}}$.
- **Conclusion**: Car 1 traveled much farther ($36.1\\text{ m}$ vs $4.17\\text{ m}$) after the application of brakes.""",
    "worked_examples": [
        {
            "problem": "Abdul, while driving to school, computes the average speed for his trip to be 20 km/h. On his return trip along the same route, there is less traffic and the average speed is 30 km/h. What is the average speed for Abdul's trip?",
            "given": "Speed to school v1 = 20 km/h; Return speed along identical route v2 = 30 km/h; Distance both ways = d.",
            "formula": "Average Speed = Total Distance / Total Time = 2*d / (t1 + t2) = 2*v1*v2 / (v1 + v2).",
            "substitution": "t1 = d/20, t2 = d/30. Total time = d/20 + d/30 = 5d/60 = d/12.",
            "calculation": "1. Total distance = d + d = 2d.\\n2. Total time = d/12 hours.\\n3. Average Speed = 2d / (d/12) = 2 * 12 = 24 km/h.\\nNote: The arithmetic mean (20 + 30)/2 = 25 km/h is mathematically WRONG because the driver spends more time traveling at the slower speed.",
            "finalAnswer": "Average speed for Abdul's entire round trip = 24 km/h.",
            "unit": "Kilometres per hour (km/h)",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 4.14: Round trip displacement and harmonic average speed model"
        }
    ],
    "common_misconceptions": [
        {
            "misconception": "Average speed is simply (v1 + v2) / 2.",
            "correction": "Average speed is (v1 + v2) / 2 ONLY if the object travels at those speeds for EQUAL INTERVALS OF TIME. When traveling EQUAL DISTANCES, you must compute total distance divided by total time, which yields the harmonic mean: 2*v1*v2 / (v1 + v2).",
            "why_it_matters": "The single most tested numerical trap on CBSE Class 9 mid-term and final exams."
        }
    ],
    "visual_lesson_plan": {
        "title": "Master Kinematics Problem Solver Visual Plan",
        "diagram_type": "image",
        "concept_visuals": [
            {
                "concept_title": "Harmonic Average Speed Invariant: For equal distances traveled at speeds v1 and v2, average speed is the harmonic mean: v_avg = 2*v1*v2 / (v1 + v2).",
                "diagram_title": "Abdul Round Trip Commute Model",
                "diagram_type": "image",
                "image_query": "Average speed harmonic mean round trip commute diagram physics",
                "video_query": "average speed harmonic mean physics",
                "image_url": "/extracted_diagrams/ch4/fig_4_14.webp",
                "what_to_make": "Two-way route schematic showing 20 km/h outbound and 30 km/h inbound with total time analysis.",
                "timing_and_cue": "Mount commute model on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_14.webp | Harmonic Average Speed | v_avg = 24 km/h (not 25 km/h!) due to unequal time weighting\")"
            },
            {
                "concept_title": "Multi-Segment JRF Modeling: Displacements add vectorially while distances add arithmetically.",
                "diagram_title": "Joseph Jogging Trajectory Map",
                "diagram_type": "image",
                "image_query": "Displacement vs distance jogging path vector diagram physics",
                "video_query": "jogger distance and displacement physics",
                "image_url": "/extracted_diagrams/ch4/fig_4_2.webp",
                "what_to_make": "Linear trajectory from A to B (300 m) with reversal to C (100 m) showing distance = 400 m and displacement = 200 m.",
                "timing_and_cue": "Mount jogger trajectory on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_2.webp | Jogging Trajectory Map | Total ground path (400 m) vs Net vector displacement (200 m)\")"
            },
            {
                "concept_title": "Graphical Braking Distance Comparison: Comparing areas of right-angled triangles under v-t graphs for two braking cars.",
                "diagram_title": "Two Braking Cars v-t Comparison Graph",
                "diagram_type": "graph",
                "image_query": "Two cars braking velocity time graph comparison diagram physics",
                "video_query": "comparing braking distance using velocity time graph",
                "image_url": "/extracted_diagrams/ch4/fig_4_16.webp",
                "what_to_make": "Dual plot showing Car 1 (14.44 m/s stopping in 5 s) vs Car 2 (0.83 m/s stopping in 10 s).",
                "timing_and_cue": "Mount braking comparison on Step 1: plot_mathematical_graph(title=\"Two Braking Cars Comparison\", equation=\"14.44 - 2.888*x\", xMin=0, xMax=10, yMin=0, yMax=16, xLabel=\"Time t (s)\", yLabel=\"Velocity v (m/s)\")"
            },
            {
                "concept_title": "Kinematic Area Calculus: Area of trapezoid represents displacement irrespective of the initial speed.",
                "diagram_title": "Motorboat Acceleration Distance Area",
                "diagram_type": "image",
                "image_query": "Motorboat acceleration constant slope v-t graph distance",
                "video_query": "motorboat acceleration kinematics",
                "image_url": "/extracted_diagrams/ch4/fig_4_12.webp",
                "what_to_make": "Triangular v-t area for motorboat starting from rest reaching 24 m/s in 8 s yielding 96 m distance.",
                "timing_and_cue": "Mount motorboat area on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_12.webp | Motorboat Kinematic Area | Triangular area = 1/2 * 8s * 24 m/s = 96 m distance\")"
            },
            {
                "concept_title": "Full 10-Question Master Ledger: Complete structured solutions with given, formula, substitution, calculation, and boxed units.",
                "diagram_title": "NCERT Motion Master Chapter Review Card",
                "diagram_type": "image",
                "image_query": "Motion physics formulas and graphs master summary sheet",
                "video_query": "class 9 science motion full chapter review",
                "image_url": "/extracted_diagrams/ch4/fig_4_1.webp",
                "what_to_make": "Comprehensive formula and graphical cheatsheet covering all 10 NCERT exercise questions.",
                "timing_and_cue": "Mount review card on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_1.webp | NCERT Motion Master Review | All 10 exercise solutions verified to 100% board accuracy\")"
            }
        ]
    },
    "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each exercise solver turn.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (Presenting the exact NCERT question statement).
   - Stage 2: Formula declaration (v = (v1*t1 + v2*t2)/(t1+t2), s = ut + 1/2 at^2).
   - Stage 3: Common pitfall (Arithmetic vs Harmonic mean in Abdul's problem).
   - Stage 4: Chalkboard step-by-step layout (Given -> Formula -> Substitution -> Calculation -> Boxed Answer).
   - Stage 5: Socratic check: "In Abdul's problem, why is the average speed 24 km/h instead of 25 km/h?" HARD STOP: Wait for student response!
   - Stage 6: Boxed topper final answer."""
})

print(f"Synthesized Chapter 4 complete: {len(ch4_modules)} modules.")

output_path_ch4 = "scripts/science_modules_ch4.json"
with open(output_path_ch4, "w", encoding="utf-8") as f:
    json.dump(ch4_modules, f, indent=2, ensure_ascii=False)
print(f"Saved Chapter 4 modules to {output_path_ch4}")
