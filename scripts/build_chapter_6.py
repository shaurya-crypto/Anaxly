#!/usr/bin/env python3
"""
Generator for Class 9 Science Chapter 6:
How Forces Affect Motion (Forces and Laws of Motion) - 6 Modules
"""

import json

CH6_ID = "7e1d5438-1174-4577-8599-5f05a6642093"

ch6_modules = [
    {
        "curriculum_id": CH6_ID,
        "order_index": 1,
        "title": "The Nature of Force: Measuring Magnitude, Balanced vs Unbalanced Forces & Friction",
        "description": "Master the fundamental vector nature of force, balanced forces (zero net acceleration, change of shape), unbalanced forces (initiates or modifies motion), and contact friction dynamics.",
        "board": "CBSE",
        "class_level": "Class 9",
        "estimated_minutes": 20,
        "subtopics": [
            "Force Definition: A push, pull, or interaction that changes an object's state of rest or motion",
            "Balanced Forces: Net vector sum equals zero (Sigma F = 0); cannot accelerate an object, can alter physical shape",
            "Unbalanced Forces: Net vector sum is non-zero (Sigma F != 0); causes acceleration or deceleration",
            "Friction as an Opposing Contact Force: Roughness of micro-interlocking surfaces",
            "Overcoming Static Friction: Pushing a heavy wooden box on rough floor",
            "Spring Balance Dynamics: Measuring force magnitude in Newtons"
        ],
        "key_concepts": [
            "Vector Nature of Force: Force possesses both magnitude and direction; opposing collinear forces subtract algebraically.",
            "Balanced Forces Equilibrium: Equal and opposite forces acting on the same body produce net zero acceleration (e.g. Tug of war at standoff).",
            "Unbalanced Force Acceleration: An unbalanced external force is mandatory to change the speed or direction of motion of a body.",
            "Deformation Under Balanced Forces: Squeezing a rubber ball or stretching a spring produces balanced forces that deform shape without translational acceleration.",
            "Opposing Frictional Force: Friction always acts parallel to the contact interface in the direction strictly opposite to relative motion.",
            "Overcoming Threshold Friction: To move an object from rest, the applied pushing force must exceed the maximum limiting static friction."
        ],
        "success_criteria": "Student can resolve vector collinear forces, distinguish balanced from unbalanced forces across mechanical systems, and calculate net force.",
        "chapter_notes": """### 6.1 What is Force?
A **force** is an external agency (push, pull, or hit) exerted on an object that:
1. Changes or tends to change the **state of rest** of an object.
2. Changes or tends to change the **speed or direction** of motion (acceleration).
3. Changes the **shape or size** of an object.
- **Vector Quantity**: Has both magnitude and direction. SI unit: **Newton (N)**.

### 6.2 Balanced vs Unbalanced Forces
| Property | Balanced Forces | Unbalanced Forces |
| :--- | :--- | :--- |
| **Resultant Force ($\\sum \\vec{F}$)** | **Zero** ($F_{\\text{net}} = 0$) | **Non-Zero** ($F_{\\text{net}} \\ne 0$) |
| **Effect on Velocity** | Cannot change speed or direction ($a = 0$) | Changes speed and/or direction ($a \\ne 0$) |
| **State of Rest / Motion** | Continues at rest or uniform velocity | Accelerates or decelerates the body |
| **Effect on Shape** | **Can change the shape** (e.g. squeezing rubber ball) | Can both deform and accelerate the body |
| **Example** | Tug-of-war where neither team moves | Tug-of-war where one team pulls harder and accelerates the rope |

### 6.3 Friction as an Opposing Force
- **Frictional Force**: An electromagnetic contact force arising from microscopic interlocking of surface irregularities.
- Friction **always opposes relative motion** between surfaces in contact.
- When pushing a heavy wooden box on a rough floor:
  1. Small applied force: Static friction balances applied force ($F_{\\text{net}} = 0$, box stays at rest).
  2. Increasing push: Static friction increases until it reaches its **limiting maximum**.
  3. Applied force exceeds limiting friction: Net unbalanced force is created, and the box **accelerates forward**!""",
        "worked_examples": [
            {
                "problem": "Two forces of 15 N and 10 N act on a wooden block of mass 5 kg in opposite directions along a straight horizontal frictionless track. Calculate: (a) The net resultant force, and (b) The acceleration produced in the block.",
                "given": "F1 = 15 N (to the right); F2 = 10 N (to the left); Mass m = 5 kg; Frictionless track.",
                "formula": "F_net = F1 - F2; a = F_net / m.",
                "substitution": "F_net = 15 - 10 = 5 N (to the right); a = 5 N / 5 kg.",
                "calculation": "1. Net force F_net = 15 N - 10 N = 5 N in the direction of the larger force (rightward).\\n2. Acceleration a = F_net / m = 5 / 5 = 1 m/s^2 rightward.",
                "finalAnswer": "(a) Net force = 5 N rightward; (b) Acceleration = 1 m/s^2 rightward.",
                "unit": "Net Force (N), Acceleration (m/s^2)",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 6.4: Opposing forces acting on a block and Fig. 6.7: Pushing a box against friction"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Balanced forces can do nothing at all to an object.",
                "correction": "Balanced forces cannot accelerate an object, but they CAN change its physical shape or dimensions (e.g. compressing a spring, squeezing a balloon).",
                "why_it_matters": "A high-frequency conceptual question on CBSE board exams."
            }
        ],
        "visual_lesson_plan": {
            "title": "The Nature of Force & Friction Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Vector Nature of Force: Force possesses both magnitude and direction; opposing collinear forces subtract algebraically.",
                    "diagram_title": "Forces Acting on Different Objects",
                    "diagram_type": "image",
                    "image_query": "Applying forces push pull vector diagram physics",
                    "video_query": "introduction to force physics class 9",
                    "image_url": "/extracted_diagrams/ch6/fig_6_1.webp",
                    "what_to_make": "Textbook panel illustrating pushing a cart, pulling a drawer, and hitting a hockey ball.",
                    "timing_and_cue": "Mount force panel on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_1.webp | Forces in Action | Push, pull, and vector forces altering velocity and shape\")"
                },
                {
                    "concept_title": "Balanced Forces Equilibrium: Equal and opposite forces acting on the same body produce net zero acceleration (e.g. Tug of war at standoff).",
                    "diagram_title": "Balanced Forces on a Block",
                    "diagram_type": "image",
                    "image_query": "Balanced forces on block tug of war equilibrium diagram",
                    "video_query": "balanced and unbalanced forces physics",
                    "image_url": "/extracted_diagrams/ch6/fig_6_4.webp",
                    "what_to_make": "Block on table pulled by two equal strings with weights showing net zero movement.",
                    "timing_and_cue": "Mount balanced forces on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_4.webp | Balanced Forces | Equal opposite forces producing net zero acceleration (Sigma F = 0)\")"
                },
                {
                    "concept_title": "Unbalanced Force Acceleration: An unbalanced external force is mandatory to change the speed or direction of motion of a body.",
                    "diagram_title": "Unbalanced Forces Driving Acceleration",
                    "diagram_type": "image",
                    "image_query": "Unbalanced forces pushing box accelerating diagram physics",
                    "video_query": "unbalanced forces and acceleration",
                    "image_url": "/extracted_diagrams/ch6/fig_6_5.webp",
                    "what_to_make": "Block pulled by unequal forces showing net acceleration vector toward the larger force.",
                    "timing_and_cue": "Mount unbalanced forces on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_5.webp | Unbalanced Forces | Net resultant force producing translational acceleration\")"
                },
                {
                    "concept_title": "Deformation Under Balanced Forces: Squeezing a rubber ball or stretching a spring produces balanced forces that deform shape without translational acceleration.",
                    "diagram_title": "Spring Balance Force Measurement",
                    "diagram_type": "image",
                    "image_query": "Spring balance measuring weight force in newtons diagram",
                    "video_query": "spring balance measuring force",
                    "image_url": "/extracted_diagrams/ch6/fig_6_2.webp",
                    "what_to_make": "Spring balance calibrated in Newtons stretching under suspended mass.",
                    "timing_and_cue": "Mount spring balance on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_2.webp | Spring Balance Calibration | Measuring tensile force in SI unit Newtons (N)\")"
                },
                {
                    "concept_title": "Opposing Frictional Force: Friction always acts parallel to the contact interface in the direction strictly opposite to relative motion.",
                    "diagram_title": "Pushing a Box Against Surface Friction",
                    "diagram_type": "image",
                    "image_query": "Pushing a wooden box friction force opposing motion diagram",
                    "video_query": "friction force opposing motion experiment",
                    "image_url": "/extracted_diagrams/ch6/fig_6_3.webp",
                    "what_to_make": "Person pushing a heavy box with opposing friction arrow at the floor interface.",
                    "timing_and_cue": "Mount box friction on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_3.webp | Contact Friction | Opposing surface resistance resisting applied push\")"
                },
                {
                    "concept_title": "Overcoming Threshold Friction: To move an object from rest, the applied pushing force must exceed the maximum limiting static friction.",
                    "diagram_title": "Static to Kinetic Friction Threshold",
                    "diagram_type": "image",
                    "image_query": "Static friction vs kinetic friction threshold graph physics",
                    "video_query": "static vs kinetic friction physics",
                    "image_url": "/extracted_diagrams/ch6/fig_6_7.webp",
                    "what_to_make": "Graph plotting friction force vs applied force showing linear static ramp and constant kinetic friction plateau.",
                    "timing_and_cue": "Mount friction threshold on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_7.webp | Limiting Static Friction | Motion begins only when applied force exceeds maximum static resistance\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each concept.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (Why a stalled car doesn't move when one person pushes lightly, but accelerates when three people push together).
   - Stage 2: Definition of balanced and unbalanced forces.
   - Stage 3: Common pitfall (Balanced forces can change shape even with zero acceleration).
   - Stage 4: Chalkboard net force vector arithmetic: F_net = F1 - F2.
   - Stage 5: Socratic check: "If balanced forces act on a moving car on a frictionless ice sheet, what will happen to its speed?" HARD STOP: Wait for student response!
   - Stage 6: Authentic CBSE numerical question."""
    },
    {
        "curriculum_id": CH6_ID,
        "order_index": 2,
        "title": "Galileo's Inclined Plane Intuition & Newton's First Law of Motion (Inertia)",
        "description": "Master Galileo's thought experiments on frictionless double inclined planes, Newton's First Law of Motion, the three types of inertia (rest, motion, direction), and mass as the quantitative measure of inertia.",
        "board": "CBSE",
        "class_level": "Class 9",
        "estimated_minutes": 20,
        "subtopics": [
            "Aristotle's Fallacy: The ancient mistaken belief that continuous force is required to sustain steady motion",
            "Galileo's Double Inclined Plane: Marble rolling down achieves identical height on opposing slope",
            "Galileo's Deduction: On a zero-slope horizontal plane, a frictionless ball moves forever with constant velocity",
            "Newton's First Law of Motion: An object remains at rest or in uniform motion unless acted upon by a net external unbalanced force",
            "Inertia (Inherent Sluggishness): Natural tendency of objects to resist any change in their state of rest or motion",
            "The Three Types of Inertia: Inertia of Rest (coin and card trick), Inertia of Motion (passenger falls forward on sudden braking), Inertia of Direction (mud flying off bicycle wheels)",
            "Mass as Quantitative Measure of Inertia: Heavier bodies possess greater inertia than lighter bodies"
        ],
        "key_concepts": [
            "Overturning Aristotle's Fallacy: In real life, objects stop because of friction, not because motion naturally expires.",
            "Galileo's Limiting Thought Experiment: Reducing the angle of the second incline makes the marble travel farther; when horizontal, it travels infinitely.",
            "Newton's First Law (Law of Inertia): State of uniform rectilinear motion is completely natural and self-sustaining without external force.",
            "Inertia of Rest: When a bus suddenly starts, passengers lurch backward because lower body moves while upper body resists motion.",
            "Inertia of Motion: When a moving bus brakes suddenly, passengers lurch forward because upper body continues moving forward.",
            "Mass-Inertia Equivalence: Mass is the quantitative physical measure of an object's inertia (e.g. harder to kick a stone than a football)."
        ],
        "success_criteria": "Student can explain Galileo's double inclined plane deduction, articulate Newton's First Law verbatim, categorize everyday inertia scenarios into the 3 types, and relate mass to inertia.",
        "chapter_notes": """### 6.4 The Historical Revolution: Aristotle vs Galileo
- **Aristotle's Fallacy (350 BCE)**: *"An external force is required to keep a body moving."* He believed the natural state of all earthly bodies was rest.
- **Galileo Galilei (1600s)** overturned this by proving:
  * In the real world, moving objects stop **only because of opposing friction**.
  * If friction were completely eliminated, a moving body would **continue moving indefinitely with constant speed in a straight line**!

### 6.5 Galileo's Double Inclined Plane Experiment
1. A marble released from height $h$ on an inclined plane rolls down and climbs up an opposing inclined plane of equal angle to the **exact same height $h$**.
2. If the slope of the second plane is decreased, the marble must travel a **longer distance** to attain the same height $h$.
3. **The Limiting Case**: If the second plane is made completely **horizontal** (zero slope), the marble would travel an **infinite distance**, never stopping!

### 6.6 Newton's First Law of Motion
> *"An object remains in a state of rest or of uniform motion in a straight line unless compelled to change that state by an applied unbalanced external force."*

### 6.7 Inertia and Its Three Types
The inherent property of a body by virtue of which it resists any change in its state of rest or of uniform motion:
1. **Inertia of Rest**:
   - When a stationary bus suddenly starts, passengers lurch **backward** (lower feet move forward with bus floor, but upper torso remains at rest).
   - Flicking a stiff card placed over a glass tumbler: The card flies away, but the heavy **coin drops into the tumbler**!
   - Vigorously shaking a tree branch: Ripe fruits fall off because branch moves while fruits resist motion.
2. **Inertia of Motion**:
   - When a moving bus suddenly applies brakes, passengers lurch **forward** (feet stop with bus, but upper torso continues moving forward).
   - An athlete runs a few paces after crossing the finish line before stopping.
3. **Inertia of Direction**:
   - When a car takes a sharp left turn, passengers are thrown toward the **right** (body tends to maintain straight-line path).
   - Mud flying off revolving bicycle wheels flies along the tangent.

### 6.8 Inertia and Mass
- **Mass is the quantitative measure of inertia**.
- A heavier body possesses greater inertia than a lighter body.
- It is much easier to push an empty shopping cart than a fully loaded one; a football can be kicked easily, but kicking a stone of equal size injures your foot.""",
        "worked_examples": [
            {
                "problem": "Which of the following has more inertia: (a) a rubber ball and a stone of the same size? (b) a bicycle and a train? (c) a five-rupee coin and a one-rupee coin? Explain why.",
                "given": "Three comparative pairs of physical objects.",
                "formula": "Inertia is directly proportional to mass (Mass = quantitative measure of inertia).",
                "substitution": "Compare relative masses of objects in each pair.",
                "calculation": "(a) A stone of the same size has higher density and therefore greater mass than a rubber ball. Thus, the stone has more inertia.\\n(b) A train has immensely larger mass than a bicycle. Thus, the train has far greater inertia.\\n(c) A five-rupee coin has greater thickness and mass than a one-rupee coin. Thus, the five-rupee coin has more inertia.",
                "finalAnswer": "(a) Stone has more inertia; (b) Train has more inertia; (c) Five-rupee coin has more inertia.",
                "unit": "Mass-Inertia Scaling",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 6.12: Galileo's double inclined plane and Fig. 6.15: Coin and card inertia experiment"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Inertia is a physical force that pushes you forward when a car brakes.",
                "correction": "Inertia is NOT a force! It is an inherent property of mass. You lurch forward not because a new force pushed you, but because your body ALREADY had forward momentum and merely continued moving until restrained by the seatbelt.",
                "why_it_matters": "A crucial physics distinction required for Newton's laws."
            }
        ],
        "visual_lesson_plan": {
            "title": "Galileo's Intuition & Newton's First Law Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Overturning Aristotle's Fallacy: In real life, objects stop because of friction, not because motion naturally expires.",
                    "diagram_title": "Galileo Double Inclined Plane Apparatus",
                    "diagram_type": "image",
                    "image_query": "Galileo double inclined plane thought experiment diagram physics",
                    "video_query": "galileo double inclined plane experiment",
                    "image_url": "/extracted_diagrams/ch6/fig_6_12.webp",
                    "what_to_make": "Textbook panel showing marble rolling down first incline and ascending second incline of decreasing slope.",
                    "timing_and_cue": "Mount Galileo planes on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_12.webp | Galileo Double Incline | Proving horizontal motion continues indefinitely in absence of friction\")"
                },
                {
                    "concept_title": "Galileo's Limiting Thought Experiment: Reducing the angle of the second incline makes the marble travel farther; when horizontal, it travels infinitely.",
                    "diagram_title": "Horizontal Limiting Case Trajectory",
                    "diagram_type": "image",
                    "image_query": "Galileo thought experiment horizontal infinite motion diagram",
                    "video_query": "galileo inertia thought experiment",
                    "image_url": "/extracted_diagrams/ch6/fig_6_14.webp",
                    "what_to_make": "Schematic of marble rolling on horizontal frictionless track with infinite velocity vector.",
                    "timing_and_cue": "Mount limiting case on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_14.webp | The Limiting Case | Zero slope requires infinite horizontal travel to attain launch height\")"
                },
                {
                    "concept_title": "Newton's First Law (Law of Inertia): State of uniform rectilinear motion is completely natural and self-sustaining without external force.",
                    "diagram_title": "Newton's First Law Formulation Card",
                    "diagram_type": "image",
                    "image_query": "Newton first law of motion inertia statement diagram",
                    "video_query": "newtons first law of motion animation",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Newtons_first_law.svg",
                    "what_to_make": "Graphic card stating Newton's First Law with velocity vector invariant when net force is zero.",
                    "timing_and_cue": "Mount first law on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/ea/Newtons_first_law.svg | Newton's First Law | Objects preserve velocity vector unless acted upon by external net force\")"
                },
                {
                    "concept_title": "Inertia of Rest: When a bus suddenly starts, passengers lurch backward because lower body moves while upper body resists motion.",
                    "diagram_title": "Coin and Card Tumbler Experiment (Activity 6.2)",
                    "diagram_type": "image",
                    "image_query": "Coin on playing card over glass tumbler flick experiment diagram",
                    "video_query": "coin drop on card inertia demonstration",
                    "image_url": "/extracted_diagrams/ch6/fig_6_15.webp",
                    "what_to_make": "Playing card over tumbler flicked horizontally by finger showing coin dropping straight into tumbler due to inertia of rest.",
                    "timing_and_cue": "Mount coin card lab on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_15.webp | Inertia of Rest | Flicked card flies away while heavy coin drops straight into glass\")"
                },
                {
                    "concept_title": "Inertia of Motion: When a moving bus brakes suddenly, passengers lurch forward because upper body continues moving forward.",
                    "diagram_title": "Car Braking Passenger Forward Lurch",
                    "diagram_type": "image",
                    "image_query": "Passenger leaning forward car braking seatbelt inertia diagram",
                    "video_query": "inertia of motion car braking seatbelt",
                    "image_url": "/extracted_diagrams/ch6/fig_6_16.webp",
                    "what_to_make": "Vehicle occupant restrained by seatbelt during sharp deceleration illustrating inertia of motion.",
                    "timing_and_cue": "Mount inertia of motion on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_16.webp | Inertia of Motion | Upper body preserves forward velocity until arrested by seatbelt\")"
                },
                {
                    "concept_title": "Mass-Inertia Equivalence: Mass is the quantitative physical measure of an object's inertia (e.g. harder to kick a stone than a football).",
                    "diagram_title": "Mass vs Inertia Scaling Comparison",
                    "diagram_type": "image",
                    "image_query": "Mass as measure of inertia football vs stone diagram physics",
                    "video_query": "mass as a measure of inertia physics",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/75/Inertia_mass_comparison.svg",
                    "what_to_make": "Graphic contrasting high-mass stone (immense inertia) with low-mass football (small inertia).",
                    "timing_and_cue": "Mount mass-inertia on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/7/75/Inertia_mass_comparison.svg | Mass-Inertia Equivalence | Heavier mass confers greater resistance to velocity changes\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each concept.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (Why you lurch forward when a bus slams on the brakes).
   - Stage 2: Statement of Newton's First Law and Galileo's inclined planes.
   - Stage 3: Common pitfall (Inertia is NOT a force; it is an intrinsic property of mass).
   - Stage 4: Chalkboard classification of the 3 types of inertia.
   - Stage 5: Socratic check: "Why does a karate master easily break a wooden slab with a rapid hand strike, but cannot do so with a slow push?" HARD STOP: Wait for student response!
   - Stage 6: Authentic CBSE board question on inertia and seatbelts."""
    },
    {
        "curriculum_id": CH6_ID,
        "order_index": 3,
        "title": "Momentum Dynamics & Newton's Second Law of Motion (F = ma & Impulse)",
        "description": "Master linear momentum (p = mv), the derivation of Newton's Second Law of Motion (F = ma), the definition of the SI unit Newton, and impulse mechanics in sports (cricket ball catch).",
        "board": "CBSE",
        "class_level": "Class 9",
        "estimated_minutes": 20,
        "subtopics": [
            "Linear Momentum Definition: Product of mass and velocity (p = m*v, vector, kg*m/s)",
            "Newton's Second Law Statement: Rate of change of momentum is directly proportional to applied unbalanced force",
            "Mathematical Derivation of F = ma: F proportional to (p2 - p1) / t = m*(v - u) / t = m*a",
            "Definition of One Newton: Force required to accelerate 1 kg mass at 1 m/s^2 (1 N = 1 kg*m/s^2)",
            "Impulse Mechanics (F * Delta t = Delta p): Why increasing contact time reduces impact force",
            "Sports Applications: Fielder pulling hands back while catching high-speed cricket ball, high jump sand pits"
        ],
        "key_concepts": [
            "Linear Momentum Vector: p = mv has both magnitude and direction, pointing in the same direction as velocity.",
            "Impact Force Proportionality: A small mass at immense speed (bullet) or a huge mass at slow speed (truck) possess catastrophic momentum.",
            "Newton's Second Law Derivation: F = k * d(mv)/dt = ma (defining k = 1 fixes the standard Newton unit).",
            "Definition of SI Unit Newton: 1 Newton is the magnitude of force that produces an acceleration of 1 m/s^2 in a mass of 1 kg.",
            "Impulse-Momentum Theorem: F * Delta t = Delta p; extending collision duration Delta t dramatically lowers peak impact force F.",
            "Cricket Catch Technique: Pulling hands backward increases time interval of deceleration, reducing impact force on palms."
        ],
        "success_criteria": "Student can derive F = ma from momentum principles, define 1 Newton, solve multi-step force numericals, and explain impulse in sports.",
        "chapter_notes": """### 6.9 Linear Momentum ($p$)
The momentum of an object is defined as the **product of its mass and velocity**:
$$p = m \\times v$$
- **Vector Quantity**: Points in the exact same direction as velocity $\\vec{v}$.
- **SI Unit**: **$\\text{kg}\\cdot\\text{m/s}$** or **$\\text{kg}\\cdot\\text{m}\\cdot\\text{s}^{-1}$**.
- Even a tiny bullet ($m = 0.01\\text{ kg}$) moving at high speed ($v = 400\\text{ m/s}$) possesses lethal momentum ($4\\text{ kg}\\cdot\\text{m/s}$). A massive truck moving at slow speed has huge momentum due to mass.

### 6.10 Newton's Second Law of Motion
> *"The rate of change of momentum of an object is directly proportional to the applied unbalanced force, and takes place in the direction in which the force acts."*

### 6.11 Mathematical Derivation of $F = ma$
Let an object of mass $m$ have initial velocity $u$. An unbalanced force $F$ acts for time $t$, accelerating it to final velocity $v$.
- Initial momentum: $p_1 = mu$
- Final momentum: $p_2 = mv$
- Change in momentum: $\\Delta p = p_2 - p_1 = mv - mu = m(v - u)$
- Rate of change of momentum: $\\frac{\\Delta p}{t} = \\frac{m(v - u)}{t}$

By Newton's Second Law:
$$F \\propto \\frac{m(v - u)}{t}$$
Since $\\frac{v - u}{t} = a$ (acceleration):
$$F \\propto ma \\implies F = k \\cdot ma$$
By defining the unit of force such that a force of $1$ unit produces an acceleration of $1\\text{ m/s}^2$ on a mass of $1\\text{ kg}$, the constant $k = 1$:
$$\\mathbf{F = ma}$$

### 6.12 Definition of 1 Newton
**One Newton ($1\\text{ N}$)** is that magnitude of force which produces an acceleration of $1\\text{ m/s}^2$ when acting on an object of mass $1\\text{ kg}$:
$$1\\text{ N} = 1\\text{ kg} \\times 1\\text{ m/s}^2 = 1\\text{ kg}\\cdot\\text{m/s}^2$$

### 6.13 Impulse and Why Fielders Pull Hands Back
$$F = \\frac{\\Delta p}{\\Delta t} \\implies F \\times \\Delta t = \\Delta p$$
- To stop a fast-moving cricket ball, its momentum must be brought to zero (fixed $\\Delta p$).
- If a fielder catches the ball with stiff, stationary hands, $\\Delta t$ is extremely small (milliseconds). Therefore, the impact force $F = \\Delta p / \\Delta t$ is **enormously high**, causing severe hand injury.
- By **pulling hands backward**, the fielder increases the time $\\Delta t$. Because $\\Delta t$ is larger, the rate of change of momentum is smaller, and the **impact force on the palms is drastically reduced**!""",
        "worked_examples": [
            {
                "problem": "A constant force acts on an object of mass 5 kg for a duration of 2 s. It increases the object's velocity from 3 m/s to 7 m/s. Find the magnitude of the applied force. Now, if the force was applied for a duration of 5 s, what would be the final velocity of the object?",
                "given": "Mass m = 5 kg; Initial velocity u = 3 m/s; Final velocity v = 7 m/s; Time t1 = 2 s; Second time duration t2 = 5 s.",
                "formula": "F = m * (v - u) / t1; v_final = u + (F/m) * t2.",
                "substitution": "F = 5 * (7 - 3) / 2; v_final = 3 + (10 / 5) * 5.",
                "calculation": "1. Acceleration a = (7 - 3) / 2 = 4 / 2 = 2 m/s^2.\\n2. Applied force F = m * a = 5 * 2 = 10 N.\\n3. If applied for t2 = 5 s with same force F = 10 N: a = 2 m/s^2.\\n4. v_final = u + a * t2 = 3 + (2 * 5) = 3 + 10 = 13 m/s.",
                "finalAnswer": "Magnitude of applied force = 10 N; Final velocity after 5 s = 13 m/s.",
                "unit": "Force (N), Velocity (m/s)",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 6.17: Momentum change and Fig. 6.18: Fielder pulling hands back while catching cricket ball"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Pulling hands back decreases the total momentum change of the ball.",
                "correction": "The total change in momentum Delta p is IDENTICAL in both cases (the ball stops from its initial speed). Pulling hands back increases the TIME Delta t, which reduces the RATE of momentum change (Force = Delta p / Delta t).",
                "why_it_matters": "A quintessential high-discrimination CBSE board exam question."
            }
        ],
        "visual_lesson_plan": {
            "title": "Momentum & Newton's Second Law Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Linear Momentum Vector: p = mv has both magnitude and direction, pointing in the same direction as velocity.",
                    "diagram_title": "Momentum Comparison: Bullet vs Heavy Truck",
                    "diagram_type": "image",
                    "image_query": "Momentum mass velocity product bullet vs truck physics diagram",
                    "video_query": "linear momentum physics explained",
                    "image_url": "/extracted_diagrams/ch6/fig_6_17.webp",
                    "what_to_make": "Graphic contrasting small mass high-speed bullet with huge mass low-speed truck having comparable momentum.",
                    "timing_and_cue": "Mount momentum comparison on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_17.webp | Linear Momentum Vector | p = m * v measured in kg*m/s\")"
                },
                {
                    "concept_title": "Impact Force Proportionality: A small mass at immense speed (bullet) or a huge mass at slow speed (truck) possess catastrophic momentum.",
                    "diagram_title": "Force Rate of Momentum Change Graphic",
                    "diagram_type": "image",
                    "image_query": "Rate of change of momentum force proportional diagram",
                    "video_query": "newtons second law rate of change of momentum",
                    "image_url": "/extracted_diagrams/ch6/fig_6_18.webp",
                    "what_to_make": "Mathematical vector diagram showing change in momentum Delta p divided by time interval Delta t.",
                    "timing_and_cue": "Mount rate of change on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_18.webp | Second Law Formulation | Force is directly proportional to time rate of momentum change\")"
                },
                {
                    "concept_title": "Newton's Second Law Derivation: F = k * d(mv)/dt = ma (defining k = 1 fixes the standard Newton unit).",
                    "diagram_title": "Derivation of F = ma Chalk Card",
                    "diagram_type": "image",
                    "image_query": "Derivation of F equals ma formula newton second law",
                    "video_query": "derive f ma newtons second law",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/21/Newtons_second_law.svg",
                    "what_to_make": "Chalkboard card showing step-by-step derivation: F proportional to m(v-u)/t -> F = ma.",
                    "timing_and_cue": "Mount F=ma derivation on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/2/21/Newtons_second_law.svg | F = ma Derivation | Mathematical core of classical Newtonian mechanics\")"
                },
                {
                    "concept_title": "Definition of SI Unit Newton: 1 Newton is the magnitude of force that produces an acceleration of 1 m/s^2 in a mass of 1 kg.",
                    "diagram_title": "1 Newton Standard Unit Definition",
                    "diagram_type": "image",
                    "image_query": "Definition of one newton 1 kg mass 1 meter per second squared diagram",
                    "video_query": "what is one newton of force physics",
                    "image_url": "/extracted_diagrams/ch6/fig_6_20.webp",
                    "what_to_make": "Standard 1 kg block undergoing 1 m/s^2 acceleration under 1 Newton force.",
                    "timing_and_cue": "Mount 1 Newton unit on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_20.webp | The Newton (N) | Force required to accelerate 1 kg mass at 1 m/s^2\")"
                },
                {
                    "concept_title": "Impulse-Momentum Theorem: F * Delta t = Delta p; extending collision duration Delta t dramatically lowers peak impact force F.",
                    "diagram_title": "Impulse Force-Time Collision Curve",
                    "diagram_type": "image",
                    "image_query": "Impulse force time curve impact collision duration physics diagram",
                    "video_query": "impulse momentum theorem physics",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Impulse_force_time.svg",
                    "what_to_make": "Force-time curve comparing sharp high-peak force during short collision vs wide low-peak force during prolonged collision.",
                    "timing_and_cue": "Mount impulse curve on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/eb/Impulse_force_time.svg | Impulse Theorem | Extending impact duration Delta t dramatically lowers peak damaging force\")"
                },
                {
                    "concept_title": "Cricket Catch Technique: Pulling hands backward increases time interval of deceleration, reducing impact force on palms.",
                    "diagram_title": "Fielder Pulling Hands Backward Catching Cricket Ball",
                    "diagram_type": "image",
                    "image_query": "Fielder catching cricket ball pulling hands back physics photo",
                    "video_query": "why fielders pull hands back catching ball physics",
                    "image_url": "/extracted_diagrams/ch6/fig_6_18.webp",
                    "what_to_make": "Kinematic sequence showing cricketer catching ball and extending hands backward to prolong deceleration time.",
                    "timing_and_cue": "Mount cricket catch on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_18.webp | Cricket Catch Mechanics | Extending deceleration time Delta t to protect hands from impact shock\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each concept.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (Why catching a high-speed cricket ball hurts if your hands stay stiff).
   - Stage 2: Definition of linear momentum p = mv and Newton's Second Law.
   - Stage 3: Common pitfall (Pulling hands back reduces FORCE, not total momentum change).
   - Stage 4: Chalkboard derivation: F = m(v-u)/t = ma.
   - Stage 5: Socratic check: "A tennis ball and a heavy cricket ball are thrown at the exact same speed. Which one is harder to stop, and why?" HARD STOP: Wait for student response!
   - Stage 6: Authentic CBSE numerical question."""
    },
    {
        "curriculum_id": CH6_ID,
        "order_index": 4,
        "title": "Action, Reaction & Newton's Third Law of Motion",
        "description": "Master Newton's Third Law: action-reaction pairs acting on different bodies, why third law forces never cancel each other, walking biomechanics, spring balance couplings, and balloon rocket propulsion.",
        "board": "CBSE",
        "class_level": "Class 9",
        "estimated_minutes": 20,
        "subtopics": [
            "Newton's Third Law Statement: To every action, there is always an equal and opposite reaction",
            "Mutual Interaction: Forces always occur in matched pairs (F_AB = -F_BA)",
            "The Non-Cancellation Rule: Action and reaction act on TWO DIFFERENT bodies, therefore they can NEVER cancel out",
            "Walking Biomechanics: Feet push the ground backward; ground pushes feet forward with equal reaction",
            "Connected Spring Balances (Activity 6.4): Equal and opposite readings on two interlocked balances",
            "Everyday Manifestations: Swimmer pushing water backward, rowing a boat, balloon rocket expulsion"
        ],
        "key_concepts": [
            "Third Law Core Axiom: Whenever one object exerts a force on another object, the second object instantly exerts an equal and opposite force on the first.",
            "Independent Bodies Axiom: Action force and reaction force act on two completely different objects, so net force on each individual object is non-zero.",
            "Simultaneous Co-Existence: Action and reaction occur simultaneously; neither force is the cause or effect of the other.",
            "Walking Mechanics: You cannot walk on frictionless ice because pushing backward yields zero reaction force.",
            "Connected Spring Balances: Pulling balance A hooked to balance B demonstrates identical Newton readings on both dials in opposite directions.",
            "Recoil & Jet Propulsion: Expelling air backward from a balloon produces forward thrust on the balloon body."
        ],
        "success_criteria": "Student can state Newton's Third Law verbatim, identify action and reaction forces across 5 real-world scenarios, and prove why action and reaction never cancel.",
        "chapter_notes": """### 6.14 Newton's Third Law of Motion
> *"To every action, there is an equal and opposite reaction."*
- If body $A$ exerts a force $\\vec{F}_{AB}$ on body $B$, then body $B$ simultaneously exerts an equal and opposite force $\\vec{F}_{BA}$ on body $A$:
  $$\\mathbf{\\vec{F}_{AB} = -\\vec{F}_{BA}}$$

### 6.15 The Critical Rules of Action-Reaction
1. **Forces Always Occur in Pairs**: A single isolated force is a physical impossibility in nature.
2. **Action and Reaction Act on DIFFERENT Bodies**:
   - $\\vec{F}_{AB}$ acts on body $B$.
   - $\\vec{F}_{BA}$ acts on body $A$.
   - **Why Action and Reaction NEVER Cancel Out**: Forces cancel out only when they act on the **same body**! Because action and reaction act on two entirely different objects, each individual body experiences a net unbalanced force and can accelerate!
3. **Equal Magnitudes, Opposite Directions**: $|\\vec{F}_{AB}| = |\\vec{F}_{BA}|$.

### 6.16 Real-World Demonstrations
1. **Walking on the Ground**:
   - Action: Your foot pushes the ground backward and downward.
   - Reaction: The ground pushes your foot forward and upward with equal force, propelling you forward!
   - *Why you slip on ice*: Frictionless ice cannot support backward horizontal push; reaction force is zero, making walking impossible.
2. **Swimming in Water**:
   - Action: Swimmer pushes water backward with arms.
   - Reaction: Water pushes swimmer forward.
3. **Two Connected Spring Balances (Activity 6.4)**:
   - Attach spring balance A to a wall, and hook spring balance B to balance A.
   - Pull balance B: Both spring balance dials show the **exact same reading** in Newtons! Balance A pulls balance B with force equal and opposite to balance B pulling balance A.""",
        "worked_examples": [
            {
                "problem": "Explain using Newton's Third Law why a horse cannot pull a cart through empty outer space, and identify the exact action-reaction pair that enables a horse to pull a cart on Earth.",
                "given": "Horse-cart acceleration on Earth vs vacuum of space.",
                "formula": "Newton's Third Law: Action-Reaction pair on ground.",
                "substitution": "Action = Horse hooves pushing Earth backward; Reaction = Earth pushing horse hooves forward.",
                "calculation": "1. To accelerate forward, the horse bends forward and pushes the ground backward with its hooves (Action force on Earth).\\n2. By Newton's Third Law, the Earth pushes forward on the horse's hooves with an equal and opposite force (Reaction force on Horse).\\n3. If this forward reaction force exceeds the opposing friction of the cart wheels, the horse and cart accelerate forward.\\n4. In empty space, there is no solid ground or surface for the horse's hooves to push against. Action cannot be exerted, so zero forward reaction force is generated; hence the horse cannot move the cart.",
                "finalAnswer": "Action is hooves pushing Earth backward; Reaction is Earth pushing horse forward. In space, absence of ground eliminates reaction force.",
                "unit": "Newtonian Biomechanics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 6.22: Action and reaction forces on two connected spring balances and Fig. 6.24: Walking forward via ground reaction"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Since action and reaction are equal and opposite, they must add up to zero and cancel each other out.",
                "correction": "Forces cancel only when acting on the SAME object. Action acts on body B; Reaction acts on body A. Because they act on two different bodies, they NEVER cancel each other.",
                "why_it_matters": "The single most famous physics misconception on earth."
            }
        ],
        "visual_lesson_plan": {
            "title": "Action, Reaction & Third Law Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Third Law Core Axiom: Whenever one object exerts a force on another object, the second object instantly exerts an equal and opposite force on the first.",
                    "diagram_title": "Action-Reaction Pair Vector Diagram",
                    "diagram_type": "image",
                    "image_query": "Newtons third law action reaction forces vector diagram physics",
                    "video_query": "newtons third law action reaction pairs",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/23/Action_and_reaction_forces.svg",
                    "what_to_make": "Two interacting bodies showing equal magnitude opposite direction vectors F_AB and -F_BA.",
                    "timing_and_cue": "Mount action-reaction on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/2/23/Action_and_reaction_forces.svg | Newton's Third Law | F_AB = -F_BA acting simultaneously on two interacting bodies\")"
                },
                {
                    "concept_title": "Independent Bodies Axiom: Action force and reaction force act on two completely different objects, so net force on each individual object is non-zero.",
                    "diagram_title": "Non-Cancellation Two-Body Free Body Diagram",
                    "diagram_type": "image",
                    "image_query": "Action reaction act on different bodies free body diagram physics",
                    "video_query": "why action and reaction do not cancel",
                    "image_url": "/extracted_diagrams/ch6/fig_6_22.webp",
                    "what_to_make": "Free body diagrams separating body A and body B proving net force on each body is non-zero.",
                    "timing_and_cue": "Mount non-cancellation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_22.webp | Non-Cancellation Axiom | Forces act on two different objects, so each object accelerates independently\")"
                },
                {
                    "concept_title": "Simultaneous Co-Existence: Action and reaction occur simultaneously; neither force is the cause or effect of the other.",
                    "diagram_title": "Activity 6.4 Connected Spring Balances",
                    "diagram_type": "image",
                    "image_query": "Two spring balances connected action reaction experiment diagram",
                    "video_query": "two spring balances newtons third law experiment",
                    "image_url": "/extracted_diagrams/ch6/fig_6_22.webp",
                    "what_to_make": "Two interlocked spring balances showing identical 5 N scale readings in opposite directions.",
                    "timing_and_cue": "Mount spring balances on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_22.webp | Connected Spring Balances | Identical Newton scale readings proving exact mutual force parity\")"
                },
                {
                    "concept_title": "Walking Mechanics: You cannot walk on frictionless ice because pushing backward yields zero reaction force.",
                    "diagram_title": "Walking Ground Reaction Force Vectors",
                    "diagram_type": "image",
                    "image_query": "Walking ground reaction force physics vector diagram",
                    "video_query": "physics of walking ground reaction force",
                    "image_url": "/extracted_diagrams/ch6/fig_6_24.webp",
                    "what_to_make": "Biomechanics of foot push showing backward ground friction vector and forward reaction propulsion vector.",
                    "timing_and_cue": "Mount walking mechanics on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_24.webp | Walking Biomechanics | Foot pushes ground backward; ground pushes foot forward\")"
                },
                {
                    "concept_title": "Connected Spring Balances: Pulling balance A hooked to balance B demonstrates identical Newton readings on both dials in opposite directions.",
                    "diagram_title": "Swimmer Pushing Water Reaction",
                    "diagram_type": "image",
                    "image_query": "Swimmer pushing water wall action reaction diagram physics",
                    "video_query": "swimming newtons third law",
                    "image_url": "/extracted_diagrams/ch6/fig_6_26.webp",
                    "what_to_make": "Swimmer kicking pool wall generating forward propulsion force.",
                    "timing_and_cue": "Mount swimmer push on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_26.webp | Swimmer Wall Push | Pushing wall backward yields forward acceleration thrust\")"
                },
                {
                    "concept_title": "Recoil & Jet Propulsion: Expelling air backward from a balloon produces forward thrust on the balloon body.",
                    "diagram_title": "Balloon Rocket Jet Thrust (Activity 6.5)",
                    "diagram_type": "image",
                    "image_query": "Balloon rocket straw thread action reaction demonstration diagram",
                    "video_query": "balloon rocket newtons third law experiment",
                    "image_url": "/extracted_diagrams/ch6/fig_6_27.webp",
                    "what_to_make": "Air escaping from balloon nozzle to the right while balloon accelerates along thread to the left.",
                    "timing_and_cue": "Mount balloon rocket on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_27.webp | Balloon Rocket Thrust | High-speed air exhaust pushing balloon body in opposite direction\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each concept.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (Why a rowing boat moves forward when you push water backward with oars).
   - Stage 2: Statement of Newton's Third Law and formula F_AB = -F_BA.
   - Stage 3: Common pitfall (Why action and reaction NEVER cancel out).
   - Stage 4: Chalkboard Free Body Diagram separating the two bodies.
   - Stage 5: Socratic check: "If a mosquito collides with the windshield of a speeding truck, which one experiences the greater force?" HARD STOP: Wait for student response!
   - Stage 6: Authentic CBSE board question on action-reaction pairs."""
    },
    {
        "curriculum_id": CH6_ID,
        "order_index": 5,
        "title": "Conservation of Linear Momentum: Isolated Systems & Recoil Mechanics",
        "description": "Master the Law of Conservation of Momentum: mathematical derivation from Newton's Second and Third Laws, isolated systems with zero external net force, collision kinematics, gun recoil velocity, and rocket staging.",
        "board": "CBSE",
        "class_level": "Class 9",
        "estimated_minutes": 20,
        "subtopics": [
            "Conservation of Momentum Law: Total momentum of an isolated system remains constant",
            "Isolated System Definition: A physical system with zero net external forces (internal forces only)",
            "Derivation from Newton's Laws: F_AB = -F_BA implies m1*(v1 - u1)/t = -m2*(v2 - u2)/t",
            "Master Collision Equation: m1*u1 + m2*u2 = m1*v1 + m2*v2",
            "Recoil Mechanics of Firearms: v_gun = - (m_bullet * v_bullet) / M_gun",
            "Rocket Propulsion & Staging: Continuous downward gas momentum generating upward thrust"
        ],
        "key_concepts": [
            "Law of Conservation of Momentum: In an isolated system, the total vector momentum before interaction equals total vector momentum after interaction.",
            "Derivation Principle: Mutual interaction forces cancel internally via Newton's Third Law (F12 = -F21), keeping net external impulse zero.",
            "Collinear Collision Equation: m1*u1 + m2*u2 = m1*v1 + m2*v2 holds for all elastic, inelastic, and explosive collisions.",
            "Recoil Velocity Formulation: Initially at rest (p_total = 0). When fired, p_bullet + p_gun = 0 implies v_gun = - (m_b * v_b) / M_g.",
            "Recoil Heavy Gun Invariant: Because gun mass M_g is much larger than bullet mass m_b, gun recoil velocity is small but delivers substantial kick.",
            "Rocket Thrust Physics: Rockets accelerate in vacuum by continuously expelling burned combustion gases backward at supersonic velocities."
        ],
        "success_criteria": "Student can derive m1*u1 + m2*u2 = m1*v1 + m2*v2, calculate gun recoil velocities and collision outcomes, and explain rocket thrust.",
        "chapter_notes": """### 6.17 Law of Conservation of Momentum
> *"In an isolated system (where no net external unbalanced force acts), the total momentum of the system remains constant (conserved)."*
$$\\text{Total Initial Momentum} = \\text{Total Final Momentum}$$
$$\\mathbf{m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2}$$

### 6.18 Derivation Using Newton's Second and Third Laws
Consider two balls $A$ (mass $m_1$, initial velocity $u_1$) and $B$ (mass $m_2$, initial velocity $u_2$). They collide for time $t$, separating with final velocities $v_1$ and $v_2$.
1. Force exerted by ball $A$ on ball $B$:
   $$F_{AB} = m_2 \\times a_2 = m_2 \\left(\\frac{v_2 - u_2}{t}\\right)$$
2. Force exerted by ball $B$ on ball $A$:
   $$F_{BA} = m_1 \\times a_1 = m_1 \\left(\\frac{v_1 - u_1}{t}\\right)$$
3. By Newton's Third Law, action and reaction are equal and opposite:
   $$F_{AB} = -F_{BA}$$
   $$m_2 \\left(\\frac{v_2 - u_2}{t}\\right) = -m_1 \\left(\\frac{v_1 - u_1}{t}\\right)$$
4. Multiplying both sides by $t$:
   $$m_2 v_2 - m_2 u_2 = -m_1 v_1 + m_1 u_1$$
5. Rearranging terms:
   $$\\mathbf{m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2}$$

### 6.19 Recoil Velocity of a Gun
Before firing, both gun (mass $M$) and bullet (mass $m$) are at rest:
$$\\text{Initial Momentum} = 0$$
When fired, the bullet exits with forward velocity $v$, and the gun recoils backward with velocity $V$:
$$\\text{Final Momentum} = M V + m v$$
By Conservation of Momentum:
$$0 = MV + mv \\implies MV = -mv \\implies \\mathbf{V = -\\frac{mv}{M}}$$
- The **negative sign** indicates that the gun moves **backward** (recoils).
- Because gun mass $M$ is vastly greater than bullet mass $m$ ($M \\gg m$), the recoil velocity $V$ is much smaller than the bullet velocity $v$.""",
        "worked_examples": [
            {
                "problem": "A bullet of mass 20 g is horizontally fired with a velocity 150 m/s from a pistol of mass 2 kg. What is the recoil velocity of the pistol?",
                "given": "Mass of bullet m = 20 g = 0.02 kg; Velocity of bullet v = 150 m/s; Mass of pistol M = 2 kg; Initial velocities u1 = u2 = 0.",
                "formula": "Total initial momentum = Total final momentum -> 0 = M*V + m*v -> V = - (m*v) / M.",
                "substitution": "V = - (0.02 kg * 150 m/s) / 2 kg.",
                "calculation": "1. Bullet momentum = 0.02 * 150 = 3.0 kg*m/s forward.\\n2. Recoil velocity V = - 3.0 / 2 = -1.5 m/s.\\n3. Negative sign confirms the pistol moves in the opposite direction (backward).",
                "finalAnswer": "Recoil velocity of the pistol = -1.5 m/s (1.5 m/s backward).",
                "unit": "Metres per second (m/s)",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 6.29: Collision of two balls and Fig. 6.30: Recoil of gun firing bullet"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Conservation of momentum holds even when an external friction force is actively slowing the objects down.",
                "correction": "Momentum is conserved ONLY in an ISOLATED system with ZERO external unbalanced forces. External friction or gravity changes total momentum.",
                "why_it_matters": "A critical boundary condition on CBSE physics exams."
            }
        ],
        "visual_lesson_plan": {
            "title": "Conservation of Momentum & Recoil Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Law of Conservation of Momentum: In an isolated system, the total vector momentum before interaction equals total vector momentum after interaction.",
                    "diagram_title": "Two Spheres Collision Derivation Model",
                    "diagram_type": "image",
                    "image_query": "Two balls collision before during after momentum conservation diagram",
                    "video_query": "conservation of linear momentum collision experiment",
                    "image_url": "/extracted_diagrams/ch6/fig_6_29.webp",
                    "what_to_make": "Textbook panel showing balls A and B before collision, during collision (F_AB and F_BA), and after collision.",
                    "timing_and_cue": "Mount collision model on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_29.webp | Two-Body Collision | m1*u1 + m2*u2 = m1*v1 + m2*v2 derived from action-reaction equality\")"
                },
                {
                    "concept_title": "Derivation Principle: Mutual interaction forces cancel internally via Newton's Third Law (F12 = -F21), keeping net external impulse zero.",
                    "diagram_title": "Internal Interaction Impulse Cancellation",
                    "diagram_type": "image",
                    "image_query": "Internal forces cancellation isolated system momentum diagram",
                    "video_query": "why momentum is conserved internal forces",
                    "image_url": "/extracted_diagrams/ch6/fig_6_30.webp",
                    "what_to_make": "Internal force arrows F12 and F21 summing to zero within system boundary box.",
                    "timing_and_cue": "Mount force cancellation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_30.webp | Internal Force Parity | Equal and opposite internal impulses yield zero net momentum change\")"
                },
                {
                    "concept_title": "Collinear Collision Equation: m1*u1 + m2*u2 = m1*v1 + m2*v2 holds for all elastic, inelastic, and explosive collisions.",
                    "diagram_title": "Newton's Cradle Momentum Conservation",
                    "diagram_type": "image",
                    "image_query": "Newtons cradle steel balls elastic collision momentum conservation photo",
                    "video_query": "newtons cradle physics conservation of momentum",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Newtons_cradle_animation_book_2.gif",
                    "what_to_make": "Steel sphere swinging into stationary array and transferring momentum to opposite sphere.",
                    "timing_and_cue": "Mount Newton cradle on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/e8/Newtons_cradle_animation_book_2.gif | Newton's Cradle | Perfect elastic momentum transfer across identical mass spheres\")"
                },
                {
                    "concept_title": "Recoil Velocity Formulation: Initially at rest (p_total = 0). When fired, p_bullet + p_gun = 0 implies v_gun = - (m_b * v_b) / M_g.",
                    "diagram_title": "Firearm Recoil Dynamics Graphic",
                    "diagram_type": "image",
                    "image_query": "Gun recoil bullet momentum conservation vector diagram physics",
                    "video_query": "recoil of a gun momentum conservation",
                    "image_url": "/extracted_diagrams/ch6/fig_6_31.webp",
                    "what_to_make": "Pistol firing showing forward bullet momentum vector and backward gun recoil vector.",
                    "timing_and_cue": "Mount gun recoil on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_31.webp | Firearm Recoil Mechanics | Backward recoil velocity V = - (m*v) / M balancing bullet momentum\")"
                },
                {
                    "concept_title": "Recoil Heavy Gun Invariant: Because gun mass M_g is much larger than bullet mass m_b, gun recoil velocity is small but delivers substantial kick.",
                    "diagram_title": "Mass Ratio & Recoil Velocity Chart",
                    "diagram_type": "image",
                    "image_query": "Mass ratio recoil velocity cannon vs cannonball diagram",
                    "video_query": "heavy cannon vs light cannon recoil",
                    "image_url": "/extracted_diagrams/ch6/fig_6_34.webp",
                    "what_to_make": "Comparison of cannon mass (1000 kg) vs cannonball (5 kg) showing velocity inverse scaling.",
                    "timing_and_cue": "Mount mass ratio on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_34.webp | Mass-Velocity Inverse Law | Heavier firearm mass reduces recoil kick to manageable levels\")"
                },
                {
                    "concept_title": "Rocket Thrust Physics: Rockets accelerate in vacuum by continuously expelling burned combustion gases backward at supersonic velocities.",
                    "diagram_title": "Rocket Propulsion & Exhaust Gas Momentum",
                    "diagram_type": "image",
                    "image_query": "Rocket propulsion momentum conservation exhaust gas thrust diagram",
                    "video_query": "rocket propulsion conservation of momentum physics",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e2/Rocket_thrust_diagram.svg",
                    "what_to_make": "Rocket in space showing backward momentum of expelled exhaust gases generating forward momentum of payload.",
                    "timing_and_cue": "Mount rocket propulsion on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/e2/Rocket_thrust_diagram.svg | Rocket Propulsion | Expelling high-velocity gas mass backward drives forward thrust in vacuum\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each concept.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (Why firing a shotgun knocks the shooter's shoulder backward).
   - Stage 2: Statement of Law of Conservation of Momentum and derivation.
   - Stage 3: Common pitfall (Forgetting the negative sign indicating backward recoil).
   - Stage 4: Chalkboard derivation: 0 = M*V + m*v -> V = -mv/M.
   - Stage 5: Socratic check: "How does a rocket accelerate in the vacuum of deep space where there is no air to push against?" HARD STOP: Wait for student response!
   - Stage 6: Authentic CBSE numerical question."""
    },
    {
        "curriculum_id": CH6_ID,
        "order_index": 6,
        "title": "Master Dynamics Problem Solver: Authentic NCERT & Board Exam Numericals",
        "description": "Exhaustive step-by-step master solver resolving every in-text numerical and chapter-end exercise problem (Q1 through Q18) from NCERT Class 9 Science Chapter 6: Forces and Laws of Motion.",
        "board": "CBSE",
        "class_level": "Class 9",
        "estimated_minutes": 20,
        "subtopics": [
            "NCERT Exercise Q1 to Q4: Inertia, net force, bus passenger lurching",
            "NCERT Exercise Q5 to Q8: Truck starting from rest, force on 1 kg stone on ice",
            "NCERT Exercise Q9 to Q12: 8000 kg engine pulling 5 wagons, automobile braking",
            "NCERT Exercise Q13 to Q15: Hockey ball momentum change, bullet penetration into wooden block",
            "NCERT Exercise Q16 to Q18: Girl jumping onto stationary cart, two colliding hockey players"
        ],
        "key_concepts": [
            "Kinematics-Dynamics Linkage: Connecting kinematic equations (v = u + at, s = ut + 1/2at^2, v^2 = u^2 + 2as) with Newton's Second Law (F = ma).",
            "Wagon-Engine Friction & Acceleration: Net accelerating force = Engine force - Track friction; Tension in coupling links.",
            "Stone on Ice Friction: Net stopping force F = ma = -1 N for a 1 kg stone sliding at 20 m/s and stopping in 50 m.",
            "Hockey Ball Momentum Reversal: Vector sign reversal (v = -10 m/s) doubles the magnitude of momentum change (Delta p = m*(v - u)).",
            "Inelastic Collision Coalescence: Two colliding bodies locking together have combined mass (m1 + m2) and shared velocity v."
        ],
        "success_criteria": "Student can link kinematics to dynamics, calculate multi-wagon train tension, solve 100% of NCERT numericals, and earn full marks on CBSE marking rubrics.",
        "chapter_notes": """### 6.20 Comprehensive NCERT Exercise Solutions Ledger

#### Q5. A truck starts from rest and rolls down a hill with constant acceleration. It travels a distance of 400 m in 20 s. Find its acceleration. Find the force acting on it if its mass is 7 tonnes (1 tonne = 1000 kg).
- Given: $u = 0$, $s = 400\\text{ m}$, $t = 20\\text{ s}$, $m = 7 \\times 1000 = 7000\\text{ kg}$.
- Using $s = ut + \\frac{1}{2}at^2$:
  $$400 = 0 + \\frac{1}{2} \\times a \\times (20)^2 = 200 a \\implies a = \\frac{400}{200} = \\mathbf{2\\text{ m/s}^2}$$
- Force:
  $$F = m \\times a = 7000 \\times 2 = \\mathbf{14000\\text{ N}}$$

#### Q6. A stone of 1 kg is thrown with a velocity of 20 m/s across the frozen surface of a lake and comes to rest after traveling a distance of 50 m. What is the force of friction between the stone and the ice?
- Given: $m = 1\\text{ kg}$, $u = 20\\text{ m/s}$, $v = 0$, $s = 50\\text{ m}$.
- Using $v^2 = u^2 + 2as$:
  $$0 = (20)^2 + 2a(50) = 400 + 100a \\implies 100a = -400 \\implies a = -4\\text{ m/s}^2$$
- Force of friction:
  $$F = ma = 1 \\times (-4) = \\mathbf{-4\\text{ N}}$$
  *(Negative sign indicates friction acts in opposite direction to motion).*

#### Q7. An 8000 kg engine pulls a train of 5 wagons, each of 2000 kg, along a horizontal track. If the engine exerts a force of 40000 N and the track offers a friction force of 5000 N, then calculate: (a) the net accelerating force, (b) the acceleration of the train, and (c) the force of wagon 1 on wagon 2.
- (a) **Net Accelerating Force**:
  $$F_{\\text{net}} = F_{\\text{engine}} - F_{\\text{friction}} = 40000 - 5000 = \\mathbf{35000\\text{ N}}$$
- (b) **Acceleration of Train**:
  $$\\text{Total Mass } M = m_{\\text{engine}} + (5 \\times m_{\\text{wagon}}) = 8000 + (5 \\times 2000) = 8000 + 10000 = 18000\\text{ kg}$$
  $$a = \\frac{F_{\\text{net}}}{M} = \\frac{35000}{18000} = \\mathbf{1.944\\text{ m/s}^2}$$
- (c) **Force of Wagon 1 on Wagon 2**:
  Wagon 1 pulls the remaining 4 wagons behind it (mass $= 4 \\times 2000 = 8000\\text{ kg}$).
  $$F_{1\\to 2} = 8000 \\times a + (\\text{friction on 4 wagons}) = 8000 \\times 1.944 + 4000 = \\mathbf{19552\\text{ N}}$$

#### Q14. A bullet of mass 10 g traveling horizontally with a velocity of 150 m/s strikes a stationary wooden block and comes to rest in 0.03 s. Calculate the distance of penetration of the bullet into the block. Also calculate the magnitude of the force exerted by the wooden block on the bullet.
- Given: $m = 10\\text{ g} = 0.01\\text{ kg}$, $u = 150\\text{ m/s}$, $v = 0$, $t = 0.03\\text{ s}$.
- $a = \\frac{v - u}{t} = \\frac{0 - 150}{0.03} = -5000\\text{ m/s}^2$.
- Penetration distance: $s = ut + \\frac{1}{2}at^2 = (150 \\times 0.03) + \\frac{1}{2}(-5000)(0.03)^2 = 4.5 - 2.25 = \\mathbf{2.25\\text{ m}}$.
- Retarding Force: $F = ma = 0.01 \\times (-5000) = \\mathbf{-50\\text{ N}}$ (Magnitude $= 50\\text{ N}$).""",
        "worked_examples": [
            {
                "problem": "A hockey ball of mass 200 g traveling at 10 m/s is struck by a hockey stick so as to return it along its original path with a velocity at 5 m/s. Calculate the magnitude of change of momentum occurred in the motion of the hockey ball by the force applied by the hockey stick.",
                "given": "Mass of hockey ball m = 200 g = 0.2 kg; Initial velocity u = +10 m/s; Final velocity v = -5 m/s (opposite direction along original path).",
                "formula": "Change in momentum Delta p = m * v - m * u = m * (v - u).",
                "substitution": "Delta p = 0.2 * [(-5) - (+10)].",
                "calculation": "1. Initial momentum p1 = 0.2 * 10 = +2.0 kg*m/s.\\n2. Final momentum p2 = 0.2 * (-5) = -1.0 kg*m/s.\\n3. Change in momentum Delta p = p2 - p1 = -1.0 - (+2.0) = -3.0 kg*m/s.\\n4. The negative sign indicates the momentum change is directed opposite to the ball's initial velocity.\\n5. Magnitude of change of momentum = 3.0 kg*m/s.",
                "finalAnswer": "Magnitude of change in momentum = 3.0 kg*m/s (or 3.0 N*s).",
                "unit": "Kilogram metre per second (kg*m/s)",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 6.38: Hockey ball momentum reversal and Fig. 6.40: Train engine and wagons diagram"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "In momentum change problems, if the ball returns in the opposite direction, the change is 10 - 5 = 5.",
                "correction": "Velocity is a VECTOR! If initial velocity is +10, returning velocity is -5. Change in momentum is (-5) - (+10) = -15, not 5! The velocities add up because direction reversed.",
                "why_it_matters": "A universal board exam pitfall."
            }
        ],
        "visual_lesson_plan": {
            "title": "Master Dynamics Problem Solver Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Kinematics-Dynamics Linkage: Connecting kinematic equations (v = u + at, s = ut + 1/2at^2, v^2 = u^2 + 2as) with Newton's Second Law (F = ma).",
                    "diagram_title": "Kinematics-to-Dynamics Bridging Diagram",
                    "diagram_type": "image",
                    "image_query": "Kinematics to dynamics bridging equations F equals ma physics",
                    "video_query": "connecting kinematics and newtons laws",
                    "image_url": "/extracted_diagrams/ch6/fig_6_38.webp",
                    "what_to_make": "Flowchart diagram showing transition from motion parameters (u, v, t, s) through acceleration (a) to dynamic force (F = ma).",
                    "timing_and_cue": "Mount kinematics-dynamics bridge on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_38.webp | Kinematics-Dynamics Bridge | Acceleration 'a' bridges kinematic equations to Newton's F = ma\")"
                },
                {
                    "concept_title": "Wagon-Engine Friction & Acceleration: Net accelerating force = Engine force - Track friction; Tension in coupling links.",
                    "diagram_title": "Engine & 5 Wagons Train Traction Diagram",
                    "diagram_type": "image",
                    "image_query": "Train engine pulling wagons friction force diagram physics",
                    "video_query": "train engine pulling wagons physics problem",
                    "image_url": "/extracted_diagrams/ch6/fig_6_40.webp",
                    "what_to_make": "Textbook schematic of 8000 kg locomotive pulling five 2000 kg freight wagons showing engine force, track friction, and coupling tensions.",
                    "timing_and_cue": "Mount train traction on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_40.webp | Locomotive Traction | F_net = 40000 N - 5000 N = 35000 N accelerating total 18000 kg train mass\")"
                },
                {
                    "concept_title": "Stone on Ice Friction: Net stopping force F = ma = -1 N for a 1 kg stone sliding at 20 m/s and stopping in 50 m.",
                    "diagram_title": "Stone Sliding on Frozen Lake Surface",
                    "diagram_type": "image",
                    "image_query": "Stone sliding on ice stopping distance friction force diagram",
                    "video_query": "stone sliding on ice physics problem",
                    "image_url": "/extracted_diagrams/ch6/fig_6_42.webp",
                    "what_to_make": "Curling stone sliding on ice lake showing initial 20 m/s velocity brought to rest by 4 N friction force over 50 m.",
                    "timing_and_cue": "Mount stone on ice on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_42.webp | Stone on Frozen Lake | v^2 = u^2 + 2as yields -4 m/s^2 deceleration and -4 N friction\")"
                },
                {
                    "concept_title": "Hockey Ball Momentum Reversal: Vector sign reversal (v = -10 m/s) doubles the magnitude of momentum change (Delta p = m*(v - u)).",
                    "diagram_title": "Hockey Ball Vector Momentum Reversal",
                    "diagram_type": "image",
                    "image_query": "Hockey ball stick impact momentum vector reversal diagram",
                    "video_query": "hockey ball momentum change vector direction",
                    "image_url": "/extracted_diagrams/ch6/fig_6_38.webp",
                    "what_to_make": "Vector diagram illustrating +2 kg*m/s inbound momentum reversing to -1 kg*m/s outbound momentum, yielding 3 kg*m/s impulse.",
                    "timing_and_cue": "Mount momentum reversal on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_38.webp | Vector Momentum Reversal | Delta p = m(v - u) = 0.2*(-5 - 10) = -3.0 kg*m/s\")"
                },
                {
                    "concept_title": "Inelastic Collision Coalescence: Two colliding bodies locking together have combined mass (m1 + m2) and shared velocity v.",
                    "diagram_title": "Inelastic Collision & Coalescence",
                    "diagram_type": "image",
                    "image_query": "Inelastic collision two objects sticking together momentum conservation diagram",
                    "video_query": "inelastic collision physics demonstration",
                    "image_url": "/extracted_diagrams/ch6/fig_6_29.webp",
                    "what_to_make": "Girl jumping onto stationary wheeled cart and sharing combined velocity according to m1*u1 + m2*u2 = (m1 + m2)*v.",
                    "timing_and_cue": "Mount inelastic collision on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch6/fig_6_29.webp | Inelastic Collision Coalescence | Conservation of momentum across interlocking collision bodies\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each exercise solver turn.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (Presenting the exact NCERT numerical statement).
   - Stage 2: Formula declaration (F = ma, v^2 = u^2 + 2as, Delta p = m(v - u)).
   - Stage 3: Common pitfall (Vector sign reversal in momentum calculations).
   - Stage 4: Chalkboard step-by-step layout (Given -> Formula -> Substitution -> Calculation -> Boxed Answer).
   - Stage 5: Socratic check: "In the hockey ball problem, why is the change in momentum NOT 10 - 5 = 5 kg*m/s?" HARD STOP: Wait for student response!
   - Stage 6: Boxed topper final answer."""
    }
]

print(f"Synthesized Chapter 6 complete: {len(ch6_modules)} modules.")

output_path_ch6 = "scripts/science_modules_ch6.json"
with open(output_path_ch6, "w", encoding="utf-8") as f:
    json.dump(ch6_modules, f, indent=2, ensure_ascii=False)
print(f"Saved Chapter 6 modules to {output_path_ch6}")
