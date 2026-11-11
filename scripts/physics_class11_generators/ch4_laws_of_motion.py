"""
ch4_laws_of_motion.py
CBSE Class 11 Physics - Chapter 4: Laws of Motion
Part 1 (Mid-Term Syllabus, Unit III: Laws of Motion)
Target Pacing: November 28, 2026 to December 02, 2026 (7 Modules, 5 Days)
"""

import sys
import os
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

import svg_builder_physics11 as sb

CURRICULUM_ID = "c11_phy_ch04_laws_of_motion"
CLASS_LEVEL = "Class 11"
BOARD = "CBSE"
SUBJECT = "Physics"

def get_modules():
    modules = []

    # -------------------------------------------------------------
    # MODULE 1: Concept of Force, Inertia & Newton's First Law
    # Date: 2026-11-28
    # -------------------------------------------------------------
    mod1_svg = sb.build_inclined_plane_fbd_svg(theta_deg=30, title="Free Body Diagram: Block on Inclined Plane", caption="Equilibrium of forces: Normal N = mg cos θ; Friction f_s = mg sin θ")
    modules.append({
        "order_index": 19,
        "title": "Classical Dynamics Foundations: Aristotle's Fallacy, Galileo's Inertia & Newton's First Law",
        "description": "Historical evolution of dynamics, Aristotle's fallacy of sustained motion, Galileo's double inclined plane experiments, Newton's first law of motion, and inertia of rest, motion, and direction.",
        "target_completion_date": "2026-11-28",
        "syllabus_pacing": "Day 17 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Aristotle's fallacy: An external force is required to keep a body in uniform motion (Disproven)",
            "Galileo's thought experiments: Double inclined planes and perpetual motion on friction-free horizontal plane",
            "Concept of Inertia: Natural resistance of an object to change its state of rest or uniform motion",
            "Types of inertia: Inertia of Rest, Inertia of Motion, and Inertia of Direction with everyday examples",
            "Newton's First Law of Motion (Law of Inertia): Definitive statement and physical consequences",
            "Concept of Force defined qualitatively as the agency that changes or tends to change state of rest/motion",
            "Inertial frames of reference vs non-inertial accelerating frames (fictitious pseudo-forces)"
        ],
        "key_concepts": [
            "Aristotle's Fallacy vs Galileo's Incline Experiment",
            "Inertia of Rest, Motion & Direction",
            "Newton's First Law of Motion",
            "Qualitative Definition of Force"
        ],
        "success_criteria": [
            "Refute Aristotle's flawed dynamics citing friction as the opposing resistive force",
            "Explain everyday inertial phenomena (dusting a rug, jumping from a moving bus, banking curves)",
            "Formulate Newton's first law and identify inertial reference frames",
            "Draw Galileo's double inclined plane showing height conservation"
        ],
        "chapter_notes": """# CHAPTER 4: LAWS OF MOTION
## MODULE 1: Force & Newton's First Law

### 1. Aristotle's Fallacy vs. Galileo's Insight
- **Aristotelian View (Flawed)**: *"An external force is required to keep a body in uniform motion."*
  *Why it is wrong*: In everyday experience, a sliding cart comes to rest because of opposing **frictional forces** exerted by the ground and air. The applied force is merely needed to *counterbalance* friction!
- **Galileo's Incline Plane Experiments**:
  1. A ball rolling down an inclined plane speeds up ($a > 0$).
  2. A ball rolling up an inclined plane slows down ($a < 0$).
  3. On a smooth horizontal plane (zero incline), there is neither acceleration nor retardation: the ball will continue to move **indefinitely with constant velocity**!
  4. On a double inclined plane, a ball released from height $h$ on one slope reaches the same height $h$ on the opposite slope regardless of slope angle. As the opposite slope approaches horizontal, the ball must travel an infinite distance!

### 2. Concept of Inertia & Newton's First Law
- **Inertia**: The inherent property of all material bodies by virtue of which they resist any change in their state of rest or of uniform motion in a straight line.
  - **Mass is the quantitative measure of inertia**: A larger mass has greater inertia.
  - *Inertia of Rest*: A passenger falls backward when a bus abruptly starts.
  - *Inertia of Motion*: A passenger falls forward when brakes are suddenly applied.
  - *Inertia of Direction*: Mud flies off tangentially from rotating bicycle tires.
- **Newton's First Law of Motion**:
  *Statement*: Every body continues in its state of rest, or of uniform motion in a straight line, unless it is compelled to change that state by an external force impressed upon it.
  $$\\text{If } \\vec{F}_{\\text{net}} = 0, \\quad \\vec{a} = 0 \\implies \\vec{v} = \\text{constant}$$
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 4.1: An astronaut accidentally gets separated out of his small spaceship accelerating in inter stellar space at a constant rate of 100 m s⁻². What is the acceleration of the astronaut the instant after he is outside the spaceship? (Assume that there are no nearby stars to exert gravitational force on him.)",
                "given": "Spaceship acceleration = 100 m/s², no gravitational forces in deep interstellar space.",
                "formula": "Newton's First Law: a = F_net / m.",
                "substitution": "The moment the astronaut is outside the spaceship, there is no physical contact with the ship and no external forces acting on him. Thus net external force F_net = 0.",
                "calculation": "a = 0 / m = 0 m/s².",
                "finalAnswer": "The acceleration of the astronaut the instant after leaving the spaceship is zero.",
                "unit": "m/s²",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            }
        ],
        "common_misconceptions": [
            "Believing an object keeps accelerating after leaving the spaceship: Once outside, the driving rocket force ceases on the astronaut. By Newton's 1st law, he moves with constant velocity (a = 0)!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod1_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Aristotle's Fallacy vs Galileo's Incline Experiment",
                    "diagram_title": "Galileo's Double Inclined Plane Thought Experiment",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "galileo double inclined plane inertia thought experiment diagram",
                    "video_search_query": "galileo inclined plane thought experiment inertia animation",
                    "what_to_make": "Double incline showing conservation of height h as the second ramp angle flattens to horizontal",
                    "what_to_explain": "Contrast Aristotle's friction-clouded observation with Galileo's frictionless thought experiment",
                    "timing_and_cue": "Step 1 (Intuition)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "A stone of mass 0.1 kg is thrown vertically upwards. What is the magnitude and direction of the net force acting on the stone during its upward motion and at the highest point?",
                            "ideal_answer": "In both cases, neglecting air resistance, the only force acting is gravity. Net force F = mg = 0.1 × 9.8 = 0.98 N vertically downwards.",
                            "socratic_hint": "Does gravity turn off when the stone reaches the highest point?",
                            "type": "Checkpoint"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 2: Momentum, Newton's Second Law & Impulse
    # Date: 2026-11-29
    # -------------------------------------------------------------
    modules.append({
        "order_index": 20,
        "title": "Newton's Second Law of Motion: Linear Momentum, F = dp/dt & Impulse-Momentum Theorem",
        "description": "Mathematical formulation of linear momentum, derivation of F = ma for constant mass, impulse as force-time integral, and practical applications in catching balls and seatbelts.",
        "target_completion_date": "2026-11-29",
        "syllabus_pacing": "Day 18 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Linear momentum p⃗ = m v⃗ (vector quantity with direction of velocity)",
            "Newton's Second Law: Rate of change of momentum is proportional to impressed force",
            "Mathematical derivation: F⃗ = d(m v⃗) / dt = m (dv⃗ / dt) = m a⃗ (for constant mass)",
            "Vector component equations: F_x = m a_x, F_y = m a_y, F_z = m a_z",
            "SI unit of force: Definition of 1 Newton (1 N = 1 kg m s⁻²)",
            "Impulse J⃗ = ∫ F⃗ dt = F_avg Δt: Measure of total effect of a large force over short time",
            "Impulse-Momentum Theorem: Impulse equals change in linear momentum (J⃗ = Δp⃗)",
            "Practical cushioning: Why a cricketer draws hands back while catching a cricket ball"
        ],
        "key_concepts": [
            "Linear Momentum p⃗ = m v⃗",
            "Newton's Second Law F⃗ = dp⃗/dt = m a⃗",
            "Impulse J⃗ = F_avg Δt = Δp⃗",
            "Cushioning Mechanism (Increasing Impact Time Δt Reduces Impact Force F)"
        ],
        "success_criteria": [
            "Derive F = ma from F ∝ dp/dt setting proportionality constant k = 1 via definition of 1 Newton",
            "Prove the Impulse-Momentum theorem analytically",
            "Explain mathematically why increasing impact duration Δt reduces impulsive force F",
            "Solve variable force and 2D momentum change problems (e.g. ball rebounding from wall)"
        ],
        "chapter_notes": """# CHAPTER 3: LAWS OF MOTION
## MODULE 2: Momentum & Newton's Second Law

### 1. Linear Momentum
The **linear momentum** of a body is defined as the product of its mass $m$ and velocity $\\vec{v}$:
$$\\vec{p} = m \\vec{v}$$
- Dimension: $[M L T^{-1}]$; SI Unit: $\\text{kg m s}^{-1}$ or $\\text{N s}$.
- It is a vector pointing in the direction of velocity.

### 2. Newton's Second Law of Motion
*Statement*: The rate of change of momentum of a body is directly proportional to the applied force and takes place in the direction in which the force acts.
$$\\vec{F} \\propto \\frac{d\\vec{p}}{dt} \\implies \\vec{F} = k \\frac{d\\vec{p}}{dt}$$
For constant mass $m$:
$$\\frac{d\\vec{p}}{dt} = \\frac{d}{dt}(m\\vec{v}) = m \\frac{d\\vec{v}}{dt} = m \\vec{a}$$
In SI units, $1\\text{ N}$ is defined as the force that produces an acceleration of $1\\text{ m/s}^2$ in a mass of $1\\text{ kg} \\implies k = 1$:
$$\\vec{F} = m \\vec{a}$$

### 3. Component Form of Second Law
$$\\vec{F} = F_x \\hat{i} + F_y \\hat{j} + F_z \\hat{k} = m(a_x \\hat{i} + a_y \\hat{j} + a_z \\hat{k})$$
$$F_x = m a_x = m \\frac{d^2x}{dt^2}, \\quad F_y = m a_y = m \\frac{d^2y}{dt^2}, \\quad F_z = m a_z = m \\frac{d^2z}{dt^2}$$
*Crucial Consequence*: Acceleration at an instant is determined by the force acting at THAT instant, independent of the past history of the body!

### 4. Impulse and the Impulse-Momentum Theorem
A large force acting for a very short duration is called an **impulsive force** (e.g. bat hitting ball).
**Impulse** $\\vec{J}$ is defined as:
$$\\vec{J} = \\int_{t_1}^{t_2} \\vec{F} \\, dt = \\vec{F}_{\\text{avg}} \\Delta t$$
Since $\\vec{F} = \\frac{d\\vec{p}}{dt} \\implies \\vec{F} dt = d\\vec{p}$:
$$\\vec{J} = \\int_{\\vec{p}_1}^{\\vec{p}_2} d\\vec{p} = \\vec{p}_2 - \\vec{p}_1 = \\Delta \\vec{p}$$
**Impulse-Momentum Theorem**: The impulse of a force is equal to the change in momentum produced by it.
$$F_{\\text{avg}} = \\frac{\\Delta p}{\\Delta t}$$
- *Cricketer catching ball*: By pulling hands backward, $\\Delta t$ increases $\\implies$ Average force $F$ on hands is reduced dramatically, preventing injury!
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 4.2: A bullet of mass 0.04 kg moving with a speed of 90 m s⁻¹ enters a heavy wooden block and is stopped after a distance of 60 cm. What is the average resistive force exerted by the block on the bullet?",
                "given": "m = 0.04 kg, u = 90 m/s, v = 0, s = 60 cm = 0.60 m.",
                "formula": "v² = u² + 2as => a = -u² / 2s; F = m a.",
                "substitution": "a = - (90)² / (2 × 0.60) = - 8100 / 1.2 = - 6750 m/s². F = 0.04 kg × (-6750 m/s²).",
                "calculation": "F = - 270 N.",
                "finalAnswer": "The average resistive force exerted by the wooden block is 270 N (directed opposite to bullet motion).",
                "unit": "N",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            },
            {
                "problem": "Textbook Example 4.4: A batsman hits back a ball straight in the direction of the bowler without changing its initial speed of 12 m s⁻¹. If the mass of the ball is 0.15 kg, determine the impulse imparted to the ball. (Assume linear motion of the ball).",
                "given": "m = 0.15 kg, initial velocity u = +12 m/s, final velocity v = -12 m/s (rebounded straight back).",
                "formula": "Impulse J = Δp = m (v - u).",
                "substitution": "J = 0.15 kg × [(-12 m/s) - (+12 m/s)] = 0.15 × (-24 m/s)",
                "calculation": "J = - 3.6 N s (directed towards the bowler).",
                "finalAnswer": "Impulse imparted = 3.6 N s in the direction from the batsman to the bowler.",
                "unit": "N s",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            }
        ],
        "common_misconceptions": [
            "Forgetting vector signs in momentum change: If a ball bounces back with equal speed v, the momentum change is NOT zero! Δp = m(-v) - mv = -2mv!",
            "Confusing force with impulse: Force is the instantaneous rate of momentum change; impulse is the total accumulated momentum change over a time interval."
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod1_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Impulse J⃗ = F_avg Δt = Δp⃗",
                    "diagram_title": "Force-Time Impulsive Spike vs Averaged Force Curve",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "impulse momentum theorem force time graph physics",
                    "video_search_query": "impulse momentum theorem physics catching ball animation",
                    "what_to_make": "F-t graph showing narrow high peak for hard surface vs wide low curve for cushioned surface",
                    "what_to_explain": "Demonstrate that the area under both curves is identical (same momentum change), but peak force is vastly reduced",
                    "timing_and_cue": "Step 2 (Formulation)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "Why does a glass plate break when dropped on a concrete floor but remains intact when dropped on a carpet from the same height?",
                            "ideal_answer": "In both cases, the change in momentum Δp is identical. The concrete floor stops the plate in a very small time Δt, producing a huge impulsive force F = Δp/Δt that shatters the glass. The carpet yields, increasing Δt and dramatically reducing the impact force below the fracture limit.",
                            "socratic_hint": "Compare the stopping times Δt on concrete vs carpet.",
                            "type": "Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 3: Newton's Third Law & Conservation of Momentum
    # Date: 2026-11-30
    # -------------------------------------------------------------
    modules.append({
        "order_index": 21,
        "title": "Newton's Third Law of Motion, Action-Reaction Pairs & Law of Conservation of Linear Momentum",
        "description": "Rigorous treatment of Newton's third law (F_AB = -F_BA), simultaneous nature of forces acting on two different bodies, isolation of systems, conservation of linear momentum, and recoil mechanics.",
        "target_completion_date": "2026-11-30",
        "syllabus_pacing": "Day 19 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Newton's Third Law: To every action, there is always an equal and opposite reaction",
            "Critical invariant: Action and reaction act on TWO DIFFERENT bodies, never on the same body",
            "Why action and reaction never cancel each other out",
            "Simultaneous occurrence: No cause-effect delay between action and reaction",
            "Derivation of Law of Conservation of Linear Momentum from 2nd and 3rd laws",
            "Isolated system: When net external force is zero (F_ext = 0 => P_total = constant)",
            "Recoil of a gun: Analytical formula for recoil velocity v_r = - (m_b / M_g) v_b",
            "Rocket propulsion principle: Variable mass thrust force F = v_rel (dm/dt)"
        ],
        "key_concepts": [
            "Newton's Third Law (F_AB = -F_BA)",
            "Action-Reaction Act on Different Bodies",
            "Law of Conservation of Linear Momentum",
            "Recoil Velocity of Gun v_r = - (m/M) v"
        ],
        "success_criteria": [
            "State Newton's third law and identify action-reaction pairs for book on table and walking on ground",
            "Explain why action and reaction forces can never produce equilibrium or cancel out",
            "Derive the law of conservation of linear momentum using Newton's second and third laws",
            "Calculate recoil velocity of firearms and thrust of rocket engines"
        ],
        "chapter_notes": """# CHAPTER 4: LAWS OF MOTION
## MODULE 3: Third Law & Momentum Conservation

### 1. Newton's Third Law of Motion
*Statement*: To every action, there is always an equal and opposite reaction.
$$\\vec{F}_{AB} = - \\vec{F}_{BA}$$
where $\\vec{F}_{AB}$ is the force on body $A$ exerted by body $B$, and $\\vec{F}_{BA}$ is the force on body $B$ exerted by body $A$.
*Three Cardinal Invariants*:
1. **Forces always occur in pairs**: There is no such thing as an isolated single force in nature.
2. **Action and reaction act on DIFFERENT bodies**: Therefore, they **never cancel each other out**! To find the acceleration of body $A$, we consider ONLY the forces acting ON body $A$.
3. **No cause-effect delay**: Action and reaction are completely simultaneous.

### 2. Derivation of Conservation of Linear Momentum
Consider an isolated two-body system consisting of bodies $A$ and $B$.
During a collision of duration $\\Delta t$:
- Force on $A$ by $B$: $\\vec{F}_{AB} = \\frac{\\Delta \\vec{p}_A}{\\Delta t}$
- Force on $B$ by $A$: $\\vec{F}_{BA} = \\frac{\\Delta \\vec{p}_B}{\\Delta t}$
By Newton's Third Law:
$$\\vec{F}_{AB} = - \\vec{F}_{BA} \\implies \\frac{\\Delta \\vec{p}_A}{\\Delta t} = - \\frac{\\Delta \\vec{p}_B}{\\Delta t}$$
$$\\Delta \\vec{p}_A + \\Delta \\vec{p}_B = \\vec{0} \\implies \\Delta(\\vec{p}_A + \\vec{p}_B) = \\vec{0}$$
$$\\vec{p}_A + \\vec{p}_B = \\text{constant}$$
*Law of Conservation of Linear Momentum*: In an isolated system (where net external force is zero), the total linear momentum of the system remains conserved.

### 3. Recoil of a Gun
Let a bullet of mass $m$ be fired with muzzle velocity $\\vec{v}$ from a gun of mass $M$.
Initially at rest: $\\vec{P}_{\\text{initial}} = \\vec{0}$.
By momentum conservation:
$$\\vec{P}_{\\text{final}} = M \\vec{V}_{\\text{gun}} + m \\vec{v} = \\vec{0}$$
$$\\vec{V}_{\\text{gun}} = -\\left(\\frac{m}{M}\\right) \\vec{v}$$
The negative sign confirms the gun recoils backward. Since $M \\gg m$, the recoil velocity is much smaller than the bullet velocity.
""",
        "worked_examples": [
            {
                "problem": "Board Exam Problem: A bullet of mass 10 g is fired horizontally with a velocity of 300 m/s from a pistol of mass 1.5 kg. Calculate the recoil velocity of the pistol.",
                "given": "Mass of bullet m = 10 g = 0.01 kg, velocity of bullet v = +300 m/s; Mass of pistol M = 1.5 kg.",
                "formula": "V_recoil = - (m / M) v",
                "substitution": "V_recoil = - (0.01 kg / 1.5 kg) × 300 m/s = - (3 / 1.5) m/s",
                "calculation": "V_recoil = - 2.0 m/s.",
                "finalAnswer": "Recoil velocity of pistol = 2.0 m/s in backward direction.",
                "unit": "m/s",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            }
        ],
        "common_misconceptions": [
            "Claiming normal reaction and gravity on a book on table are action-reaction pairs: NO! Weight mg is exerted by Earth on book; normal force N is exerted by table on book. Both act on the SAME body! The true reaction to Earth pulling book is book pulling Earth upwards!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod1_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Action-Reaction Act on Different Bodies",
                    "diagram_title": "Book on Table Force Analysis: Interaction Pairs Separation",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "newton third law action reaction pair book table earth physics",
                    "video_search_query": "newton third law action reaction misconceptions physics",
                    "what_to_make": "Split diagram isolating table, book, and Earth showing the two distinct pairs",
                    "what_to_explain": "Prove that normal reaction and gravity are not action-reaction pairs because they act on the same body",
                    "timing_and_cue": "Step 2 (Invariant Formulation)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "A horse pulls a cart. By Newton's 3rd law, the cart pulls the horse with an equal and opposite force. Why then does the cart move forward?",
                            "ideal_answer": "To determine the motion of the cart, consider ONLY forces acting on the cart (forward tension/pull by horse and opposing wheel friction). To determine the horse's motion, consider the horse pushing backward on the ground; the ground pushes the horse forward with an equal reaction force. Since ground reaction exceeds backward cart pull, the horse moves forward, accelerating the cart!",
                            "socratic_hint": "Identify the external force exerted on the horse by the ground.",
                            "type": "Conceptual Classic"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 4: Equilibrium of Concurrent Forces & Free Body Diagrams (FBD)
    # Date: 2026-12-01
    # -------------------------------------------------------------
    modules.append({
        "order_index": 22,
        "title": "Equilibrium of Concurrent Forces & Free Body Diagrams: Pulleys, Strings & Atwood Machine",
        "description": "Condition of equilibrium for concurrent forces (Σ F⃗ = 0), Lami's theorem, systematic step-by-step Free Body Diagram (FBD) methodology, tension in strings, and Atwood machine dynamics.",
        "target_completion_date": "2026-12-01",
        "syllabus_pacing": "Day 20 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Definition of Concurrent Forces: Forces whose lines of action pass through a common point",
            "Equilibrium condition: Vector sum of concurrent forces is zero (Σ F⃗ = 0)",
            "Resolution into components: Σ F_x = 0, Σ F_y = 0, Σ F_z = 0",
            "Lami's Theorem for three coplanar concurrent forces in equilibrium: P/sin α = Q/sin β = R/sin γ",
            "Systematic protocol for drawing Free Body Diagrams (FBD): Isolating bodies, identifying contact/field forces",
            "Ideal strings and pulleys: Light (massless), inextensible, frictionless (uniform tension T)",
            "Atwood Machine analysis: Acceleration a = (m₁ - m₂)g / (m₁ + m₂) and Tension T = 2 m₁ m₂ g / (m₁ + m₂)"
        ],
        "key_concepts": [
            "Equilibrium of Concurrent Forces (Σ F⃗ = 0)",
            "Lami's Theorem",
            "Free Body Diagram (FBD) Isolation Protocol",
            "Atwood Machine Acceleration and Tension Formulas"
        ],
        "success_criteria": [
            "Isolate any component in a mechanical system and draw its complete, accurate FBD",
            "Apply Lami's theorem to solve three-force equilibrium hanging rope problems",
            "Derive acceleration and string tension for connected blocks and pulley systems",
            "Resolve concurrent forces along mutually perpendicular axes to set up equilibrium equations"
        ],
        "chapter_notes": """# CHAPTER 4: LAWS OF MOTION
## MODULE 4: Equilibrium & Free Body Diagrams

### 1. Equilibrium of Concurrent Forces
Forces are said to be **concurrent** if their lines of action intersect at a common point.
A particle is in **equilibrium** under concurrent forces if the vector sum of all forces is zero:
$$\\sum \\vec{F} = \\vec{F}_1 + \\vec{F}_2 + \\dots + \\vec{F}_n = \\vec{0}$$
In Cartesian components:
$$\\sum F_x = 0, \\quad \\sum F_y = 0, \\quad \\sum F_z = 0$$

### 2. Lami's Theorem
For three concurrent coplanar forces $\\vec{P}, \\vec{Q}, \\vec{R}$ in equilibrium:
$$\\frac{P}{\\sin \\alpha} = \\frac{Q}{\\sin \\beta} = \\frac{R}{\\sin \\gamma}$$
where $\\alpha$ is the angle between $\\vec{Q}$ and $\\vec{R}$, $\\beta$ is the angle between $\\vec{P}$ and $\\vec{R}$, and $\\gamma$ is the angle between $\\vec{P}$ and $\\vec{Q}$.

### 3. Atwood Machine (Two Masses Connected over a Pulley)
Two masses $m_1 > m_2$ connected by a light inextensible string over a frictionless pulley:
- For mass $m_1$ moving downwards:
  $$m_1 g - T = m_1 a \\quad \\text{--- (1)}$$
- For mass $m_2$ moving upwards:
  $$T - m_2 g = m_2 a \\quad \\text{--- (2)}$$
Adding (1) and (2):
$$(m_1 - m_2) g = (m_1 + m_2) a \\implies a = \\left(\\frac{m_1 - m_2}{m_1 + m_2}\\right) g$$
Substituting $a$ into (2):
$$T = \\left(\\frac{2 m_1 m_2}{m_1 + m_2}\\right) g$$
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 4.6: See Fig. 4.8. A mass of 6 kg is suspended by a rope of length 2 m from the ceiling. A force of 50 N in the horizontal direction is applied at the mid-point P of the rope, as shown. What is the angle the rope makes with the vertical in equilibrium? (Take g = 10 m s⁻²). Neglect the mass of the rope.",
                "given": "m = 6 kg, F = 50 N horizontal, g = 10 m/s², rope length = 2 m.",
                "formula": "T₁ cos θ = W = mg; T₁ sin θ = F = 50 N.",
                "substitution": "T₁ cos θ = 6 kg × 10 m/s² = 60 N; T₁ sin θ = 50 N. Dividing: tan θ = (T₁ sin θ)/(T₁ cos θ) = 50 / 60 = 5/6.",
                "calculation": "tan θ = 0.8333 => θ = tan⁻¹(0.8333) ≈ 40°.",
                "finalAnswer": "The angle made by the rope with the vertical is approximately 40°.",
                "unit": "degrees",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            }
        ],
        "common_misconceptions": [
            "Assuming string tension is equal to the hanging mass weight (T = mg) during acceleration: Tension equals mg ONLY when a = 0 (at rest). When accelerating, T = m(g - a) or T = m(g + a)!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod1_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Free Body Diagram (FBD) Isolation Protocol",
                    "diagram_title": "Midpoint Rope Deflection FBD",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "free body diagram equilibrium concurrent forces physics",
                    "video_search_query": "free body diagrams how to draw physics atwood pulley",
                    "what_to_make": "FBD of point P showing horizontal 50N force, downward 60N tension, and angled tension T1",
                    "what_to_explain": "Demonstrate how component balancing yields tan θ = 5/6",
                    "timing_and_cue": "Step 2 (FBD Construction)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "Two masses of 5 kg and 3 kg are tied to the ends of a light string passing over a frictionless pulley. Find the acceleration of the system.",
                            "ideal_answer": "a = (m₁ - m₂)g / (m₁ + m₂) = (5 - 3)(9.8) / (5 + 3) = 2(9.8) / 8 = 19.6 / 8 = 2.45 m/s².",
                            "socratic_hint": "Use the Atwood machine acceleration formula.",
                            "type": "Numerical"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 5: Friction: Static, Kinetic & Rolling Friction
    # Date: 2026-12-01
    # -------------------------------------------------------------
    modules.append({
        "order_index": 23,
        "title": "Friction Mechanics: Static, Kinetic & Rolling Friction, Laws of Friction & Angle of Repose",
        "description": "Microscopic origins of friction, self-adjusting static friction, limiting friction, kinetic friction, laws of friction, angle of friction, angle of repose, and motion on rough inclined planes.",
        "target_completion_date": "2026-12-01",
        "syllabus_pacing": "Day 20 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Origin of friction: Microscopic interlocking of asperities and cold welds",
            "Static Friction (f_s): A self-adjusting opposing force (0 <= f_s <= f_s,max)",
            "Limiting Friction: Maximum static friction f_s,max = μ_s N",
            "Kinetic (Dynamic) Friction: Friction during relative sliding f_k = μ_k N (μ_k < μ_s)",
            "Graph of friction force vs applied force showing linear static phase, peak, and kinetic plateau",
            "Laws of Friction: Independence of apparent contact area; proportionality to normal force",
            "Angle of Friction (θ_f): Angle between resultant contact force and normal force (tan θ_f = μ_s)",
            "Angle of Repose (α): Minimum tilt angle of inclined plane at which a body begins to slide (tan α = μ_s)",
            "Rolling Friction: Origins (surface deformation) and why μ_r << μ_k (advantages of ball bearings)"
        ],
        "key_concepts": [
            "Static Friction as Self-Adjusting Force",
            "Limiting Friction f_s,max = μ_s N",
            "Kinetic Friction f_k = μ_k N (μ_k < μ_s)",
            "Angle of Repose Identity (tan α = μ_s)",
            "Rolling Friction Mechanism"
        ],
        "success_criteria": [
            "Sketch the friction vs applied force curve and identify static, limiting, and kinetic regimes",
            "Prove that the angle of repose is equal to the angle of friction",
            "Calculate acceleration of a block sliding down a rough inclined plane: a = g(sin θ - μ_k cos θ)",
            "Explain why pushing a lawnmower is harder than pulling it using FBDs"
        ],
        "chapter_notes": """# CHAPTER 4: LAWS OF MOTION
## MODULE 5: Friction Mechanics

### 1. Nature of Friction
Friction is the contact force parallel to the interface that opposes relative sliding between two surfaces.
- **Static Friction ($f_s$)**: Opposes the impending motion. It is **self-adjusting** in both magnitude and direction:
  $$f_s = F_{\\text{applied}} \\quad (\\text{as long as body remains at rest})$$
  Maximum static friction is the **limiting friction**:
  $$f_{s,\\text{max}} = \\mu_s N$$
  where $\\mu_s$ is the coefficient of static friction and $N$ is normal force.
- **Kinetic Friction ($f_k$)**: Opposes actual relative sliding:
  $$f_k = \\mu_k N$$
  Since fewer cold welds form during motion:
  $$\\mu_k < \\mu_s$$

### 2. Angle of Repose ($\\alpha$)
The minimum angle of an inclined plane at which a body placed on it just begins to slide down by gravity:
Along the incline:
$$mg \\sin \\alpha = f_{s,\\text{max}} = \\mu_s N$$
Perpendicular to incline:
$$N = mg \\cos \\alpha$$
Dividing:
$$\\frac{mg \\sin \\alpha}{mg \\cos \\alpha} = \\frac{\\mu_s N}{N} \\implies \\tan \\alpha = \\mu_s$$
*Theorem*: Angle of repose is equal to the angle of friction!

### 3. Pushing vs. Pulling a Lawnmower
- **Pushing**: Applied force has a downward vertical component $\\implies N = mg + F\\sin\\theta \\implies$ Friction increases ($f_k = \\mu_k(mg + F\\sin\\theta)$).
- **Pulling**: Applied force has an upward vertical component $\\implies N = mg - F\\sin\\theta \\implies$ Friction decreases ($f_k = \\mu_k(mg - F\\sin\\theta)$).
*Conclusion*: **Pulling is always easier than pushing!**
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 4.8: See Fig. 4.11. A mass of 4 kg rests on a horizontal plane. The plane is gradually inclined until at an angle θ = 15° with the horizontal, the mass just begins to slide. What is the coefficient of static friction between the block and the surface?",
                "given": "m = 4 kg, angle of repose θ = 15°.",
                "formula": "μ_s = tan θ",
                "substitution": "μ_s = tan 15° = tan(45° - 30°) = (1 - 1/√3) / (1 + 1/√3) = (√3 - 1) / (√3 + 1)",
                "calculation": "μ_s = (1.732 - 1) / (1.732 + 1) = 0.732 / 2.732 ≈ 0.268.",
                "finalAnswer": "Coefficient of static friction μ_s = 0.27",
                "unit": "dimensionless",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            }
        ],
        "common_misconceptions": [
            "Thinking static friction is always equal to μ_s N: μ_s N is the MAXIMUM possible static friction! If you push a 10 kg box with 5 N and it doesn't move, static friction is exactly 5 N, NOT μ_s N!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod1_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Angle of Repose Identity (tan α = μ_s)",
                    "diagram_title": "Inclined Plane at Limiting Equilibrium Angle of Repose",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "angle of repose inclined plane friction physics diagram",
                    "video_search_query": "angle of repose friction inclined plane experiment physics",
                    "what_to_make": "Wedge inclined at 15 degrees with FBD showing N balancing mg cos θ and fs balancing mg sin θ",
                    "what_to_explain": "Demonstrate the derivation of tan α = μ_s step-by-step",
                    "timing_and_cue": "Step 2 (Proof)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "Why is it easier to pull a heavy roller than to push it?",
                            "ideal_answer": "When pulling, the vertical component of the pulling force acts upwards, reducing the normal force (N = mg - F sin θ), which reduces friction. When pushing, the vertical component acts downwards, increasing normal force (N = mg + F sin θ) and increasing friction.",
                            "socratic_hint": "Draw the FBD for pushing vs pulling and compare the normal force.",
                            "type": "Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 6: Circular Motion Dynamics: Level & Banked Roads
    # Date: 2026-12-02
    # -------------------------------------------------------------
    mod6_svg = sb.build_banked_road_svg(title="Dynamics of Circular Motion: Banked Road", caption="Optimum speed without friction v₀ = √(rg tan θ); Maximum safe speed with friction")
    modules.append({
        "order_index": 24,
        "title": "Dynamics of Circular Motion: Centripetal Force, Level Roads & Banked Highway Engineering",
        "description": "Derivation of centripetal force F = mv²/r, maximum safe speed of a vehicle on a flat level circular road, physics of banking of roads and railway tracks, and optimum speed derivation.",
        "target_completion_date": "2026-12-02",
        "syllabus_pacing": "Day 21 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Centripetal Force: Definition F_c = m a_c = m v² / r (Required inward force)",
            "Motion of a car on a level circular road: Friction provides centripetal force (f_s = m v² / r)",
            "Maximum safe speed on level road: v_max = √(μ_s r g)",
            "Need for banking: Eliminating reliance on friction to prevent skidding and tire wear",
            "Angle of Banking (θ): Outer edge raised above inner edge",
            "Optimum speed on banked road (zero friction condition): v₀ = √(r g tan θ)",
            "Maximum safe speed on banked road with friction: v_max = √[r g (μ_s + tan θ) / (1 - μ_s tan θ)]",
            "Bending of a cyclist on a curve: tan θ = v² / (r g)"
        ],
        "key_concepts": [
            "Centripetal Force F_c = m v² / r",
            "Max Speed on Level Road v_max = √(μ_s r g)",
            "Optimum Banking Speed v₀ = √(r g tan θ)",
            "Max Speed on Banked Road with Friction",
            "Bending of a Cyclist"
        ],
        "success_criteria": [
            "Derive v_max = √(μ_s r g) for a level circular track",
            "Draw the complete FBD of a car on a banked road showing N cos θ, N sin θ, f cos θ, f sin θ",
            "Derive the optimum speed v₀ = √(rg tan θ) and maximum safe speed formula",
            "Calculate banking angle for highway turns and railway curvature"
        ],
        "chapter_notes": """# CHAPTER 4: LAWS OF MOTION
## MODULE 6: Dynamics of Circular Motion

### 1. Centripetal Force
Any motion along a curved circular path of radius $r$ requires an inward centripetal acceleration $a_c = v^2/r$. By Newton's second law, this requires a net inward **centripetal force**:
$$F_c = m a_c = \\frac{m v^2}{r} = m \\omega^2 r$$
Centripetal force is not an independent physical force; it must be provided by actual physical forces (tension in a string, gravity for satellite, friction for car).

### 2. Motion of a Car on a Level Road
On a flat horizontal circular road:
- Vertical: $N = mg$
- Horizontal: Static friction between tires and road provides centripetal force:
  $$f_s = \\frac{m v^2}{r} \\le f_{s,\\text{max}} = \\mu_s N = \\mu_s mg$$
$$\\frac{m v^2}{r} \\le \\mu_s mg \\implies v \\le \\sqrt{\\mu_s r g}$$
$$\\mathbf{v_{\\text{max}} = \\sqrt{\\mu_s r g}}$$
If $v > v_{\\text{max}}$, friction is insufficient and the car skids outward!

### 3. Banking of Roads
To avoid skidding on wet roads and reduce tire wear, the road is tilted inward at an angle $\\theta$ (**banking**).
- **Optimum Speed (Zero Friction Condition)**:
  Tires experience no sideways frictional force. The horizontal component of normal reaction $N$ alone provides centripetal force:
  $$N \\sin \\theta = \\frac{m v_0^2}{r}$$
  $$N \\cos \\theta = mg$$
  Dividing equations:
  $$\\tan \\theta = \\frac{v_0^2}{r g} \\implies \\mathbf{v_0 = \\sqrt{r g \\tan \\theta}}$$
- **Maximum Safe Speed with Friction ($\\mu_s$)**:
  When driving faster than $v_0$, impending skid is outward $\\implies$ friction $f_s$ acts down the incline:
  $$N \\cos \\theta - f_s \\sin \\theta = mg$$
  $$N \\sin \\theta + f_s \\cos \\theta = \\frac{m v_{\\text{max}}^2}{r}$$
  Setting $f_s = \\mu_s N$ and solving:
  $$\\mathbf{v_{\\text{max}} = \\sqrt{r g \\left(\\frac{\\mu_s + \\tan \\theta}{1 - \\mu_s \\tan \\theta}\\right)}}$$
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 4.10: A cyclist speeding at 18 km/h on a level road takes a sharp circular turn of radius 3 m without reducing the speed. The co-efficient of static friction between the tyres and the road is 0.1. Will the cyclist slip while taking the turn?",
                "given": "v = 18 km/h = 18 × (5/18) = 5 m/s, r = 3 m, μ_s = 0.1, g = 9.8 m/s².",
                "formula": "v_max = √(μ_s r g)",
                "substitution": "v_max = √[ 0.1 × 3 m × 9.8 m/s² ] = √[ 2.94 ] ≈ 1.71 m/s.",
                "calculation": "The actual speed of cyclist is v = 5 m/s, which is much greater than v_max = 1.71 m/s.",
                "finalAnswer": "Since v > v_max, the cyclist will definitely slip while taking the turn.",
                "unit": "m/s",
                "has_diagram": True,
                "diagram_svg": mod6_svg
            },
            {
                "problem": "Textbook Example 4.11: A circular racetrack of radius 300 m is banked at an angle of 15°. If the coefficient of friction between the wheels of a race-car and the road is 0.2, find (a) the optimum speed of the race-car to avoid wear and tear on its tyres, and (b) maximum permissible speed to avoid slipping. (Take g = 9.8 m s⁻²).",
                "given": "r = 300 m, θ = 15°, μ_s = 0.2, g = 9.8 m/s²; tan 15° = 0.2679.",
                "formula": "(a) v₀ = √(rg tan θ); (b) v_max = √[ rg (μ_s + tan θ) / (1 - μ_s tan θ) ].",
                "substitution": "(a) v₀ = √[ 300 × 9.8 × 0.2679 ] = √[ 787.6 ] = 28.1 m/s ≈ 28 m/s. (b) v_max = √[ 300 × 9.8 × (0.2 + 0.2679) / (1 - 0.2 × 0.2679) ] = √[ 2940 × 0.4679 / (1 - 0.05358) ] = √[ 1375.6 / 0.9464 ] = √1453.5 ≈ 38.1 m/s.",
                "calculation": "(a) v₀ = 28 m/s (= 101 km/h); (b) v_max = 38 m/s (= 137 km/h).",
                "finalAnswer": "(a) Optimum speed v₀ = 28.1 m/s; (b) Maximum safe speed v_max = 38.1 m/s.",
                "unit": "m/s",
                "has_diagram": True,
                "diagram_svg": mod6_svg
            }
        ],
        "common_misconceptions": [
            "Thinking banking eliminates friction entirely: Banking provides an OPTIMUM speed v₀ at which friction is zero. At speeds higher or lower than v₀, friction acts to prevent skidding!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod6_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Optimum Banking Speed v₀ = √(r g tan θ)",
                    "diagram_title": "Banked Road Cross-Section with Normal Force Components",
                    "diagram_type": "svg",
                    "svg": mod6_svg,
                    "image_search_query": "banked road circular motion normal force friction physics diagram",
                    "video_search_query": "banking of roads physics derivation circular motion animation",
                    "what_to_make": "Cross-section of car on banked incline with normal force vector resolved into vertical and horizontal components",
                    "what_to_explain": "Demonstrate why N sin θ provides the centripetal force without relying on tire friction",
                    "timing_and_cue": "Step 2 (Derivation)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "Why are railway tracks banked on curved rails?",
                            "ideal_answer": "By raising the outer rail above the inner rail, the normal reaction from the rails is tilted inward. Its horizontal component provides the required centripetal force for the turn, preventing derailment and reducing wear on the wheel flanges.",
                            "socratic_hint": "What provides the centripetal force if the tracks are flat?",
                            "type": "Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 7: Complete NCERT Exercise Solver (Ex 4.1 to 4.24)
    # Date: 2026-12-02
    # -------------------------------------------------------------
    modules.append({
        "order_index": 25,
        "title": "Exercise 4.1 to 4.24 Complete Solver: Laws of Motion, Friction & Dynamics Mastery",
        "description": "Exhaustive step-by-step solutions to every textbook exercise question (Exercises 4.1 through 4.24) including helicopter lift, rocket acceleration, connected carts, and banking turns.",
        "target_completion_date": "2026-12-02",
        "syllabus_pacing": "Day 21 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 60,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Exercise 4.1 to 4.4: Force magnitude and direction on dropped pebbles, flying kites, accelerating cars",
            "Exercise 4.5 to 4.8: Constant force accelerating masses, connected bodies, momentum change",
            "Exercise 4.9 to 4.12: Rocket thrust with mass ejection rate, friction on floor, truck carrying box",
            "Exercise 4.13 to 4.17: Helicopter reaction on air, man in elevator apparent weight",
            "Exercise 4.18 to 4.24: Connected blocks on double inclines, monkey climbing rope, banking turns"
        ],
        "key_concepts": [
            "Apparent Weight in Accelerating Elevator (N = m(g ± a))",
            "Helicopter Force on Surrounding Air",
            "Monkey Climbing Rope Tension Limits",
            "Complete Exercise Solver (4.1 to 4.24)"
        ],
        "success_criteria": [
            "Solve all 24 textbook exercises with rigorous FBDs and boxed answers",
            "Calculate apparent weight during upward and downward acceleration in an elevator",
            "Determine maximum climbing acceleration of a monkey without snapping the rope",
            "Attain 100% mastery of Unit III for CBSE Mid-Term Examination"
        ],
        "chapter_notes": """# CHAPTER 4: LAWS OF MOTION
## MODULE 7: Complete NCERT Exercise Solver

### Summary of Classical Problems
- **Apparent Weight of Man in Elevator of Mass $m$ (Exercise 4.14)**:
  - (a) Moving upward with uniform speed $v$: $a = 0 \\implies N = mg$ (True weight).
  - (b) Accelerating downward with $a$: $mg - N = ma \\implies N = m(g - a)$ (Weight decreases).
  - (c) Accelerating upward with $a$: $N - mg = ma \\implies N = m(g + a)$ (Weight increases).
  - (d) Cable snaps (Free fall, $a = g$): $N = m(g - g) = 0$ (**Weightlessness**).

- **Helicopter Forces (Exercise 4.16)**:
  Mass of helicopter $M = 2000\\text{ kg}$, crew/passengers $m = 500\\text{ kg}$, upward acceleration $a = 15\\text{ m/s}^2$:
  - (a) Force on floor by crew: $N = m(g + a) = 500(10 + 15) = 12,500\\text{ N}$ downwards.
  - (b) Action of rotor on surrounding air: $F = (M + m)(g + a) = 2500(25) = 62,500\\text{ N}$ downwards.
  - (c) Force on helicopter by surrounding air: Reaction to rotor force $= 62,500\\text{ N}$ upwards.
""",
        "worked_examples": [
            {
                "problem": "NCERT Exercise 4.14: A man of mass 70 kg stands on a weighing scale in a lift which is moving (a) upwards with a uniform speed of 10 m s⁻¹, (b) downwards with a uniform acceleration of 5 m s⁻², (c) upwards with a uniform acceleration of 5 m s⁻². What would be the readings on the scale in each case? (Take g = 10 m s⁻²). (d) What would be the reading if the lift mechanism failed and it hurtled down freely under gravity?",
                "given": "m = 70 kg, g = 10 m/s².",
                "formula": "(a) a = 0 => N = mg; (b) a = 5 m/s² down => N = m(g - a); (c) a = 5 m/s² up => N = m(g + a); (d) Free fall a = g => N = m(g - g) = 0.",
                "substitution": "(a) N = 70 × 10 = 700 N (Reading = 70 kg); (b) N = 70 × (10 - 5) = 350 N (Reading = 35 kg); (c) N = 70 × (10 + 5) = 1050 N (Reading = 105 kg); (d) N = 0 N (Reading = 0 kg).",
                "calculation": "Reading on scale = N / g.",
                "finalAnswer": "(a) 70 kg; (b) 35 kg; (c) 105 kg; (d) 0 kg (State of weightlessness).",
                "unit": "kg",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            }
        ],
        "common_misconceptions": [
            "Thinking weighing scale measures mass: A weighing scale measures the NORMAL CONTACT FORCE N exerted on it, which varies with frame acceleration!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod1_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Apparent Weight in Accelerating Elevator",
                    "diagram_title": "Elevator FBD: Normal Reaction vs Real Weight",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "apparent weight elevator acceleration physics diagram",
                    "video_search_query": "apparent weight in elevator physics free body diagram",
                    "what_to_make": "Person on weighing scale inside elevator showing normal force N and gravity mg under different accelerations",
                    "what_to_explain": "Show why upward acceleration increases apparent weight and free fall yields zero normal force",
                    "timing_and_cue": "Step 2 (FBD Application)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "What is the reading of a spring balance if the elevator cable breaks and the elevator falls freely?",
                            "ideal_answer": "Zero. Under free fall (a = g downwards), both the body and the spring balance fall with acceleration g; thus no restoring force develops in the spring and apparent weight is zero (weightlessness).",
                            "socratic_hint": "What is N when a = g in N = m(g - a)?",
                            "type": "Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    return modules
