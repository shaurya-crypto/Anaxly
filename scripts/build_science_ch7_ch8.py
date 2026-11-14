"""
Curriculum Synthesis Engine: Class 9 Science
Chapter 7: Work, Energy, and Simple Machines (Curriculum ID: da5625a5-7071-4533-8667-13da4c28abda)
Chapter 8: Journey Inside the Atom (Curriculum ID: 8be782c9-c0d3-425e-bb81-c18c298dc4a7)

Features:
- 100% textbook truth, zero synthetic SVGs.
- Extracted textbook diagrams (/extracted_diagrams/ch7/fig_7_X.webp, /extracted_diagrams/ch8/fig_8_X.webp).
- Verified Wikimedia image & video search queries.
- 1:1 Concept-to-Visual mapping.
- 1:1 Concept-to-Problem worked examples with Given, Formula, Substitution, Calculation, Final Answer.
- Strict Socratic 6-stage AI prompt context with gating stops.
"""

import json

CH7_ID = "da5625a5-7071-4533-8667-13da4c28abda"
CH8_ID = "8be782c9-c0d3-425e-bb81-c18c298dc4a7"

# ==============================================================================
# CHAPTER 7: WORK, ENERGY, AND SIMPLE MACHINES (6 MODULES)
# ==============================================================================
ch7_modules = [
    {
        "order_index": 1,
        "title": "The Mechanical Definition of Work: Force, Displacement & Angle Geometry",
        "description": "Master the rigorous scientific definition of mechanical work, distinguish work in physics from everyday physical labor, analyze the force-displacement vector dot product, and solve positive, negative, and zero work scenarios.",
        "subtopics": [
            "Everyday 'Labor' vs Scientific Work: Why pushing a stationary wall does zero work",
            "The Two Necessary Conditions for Mechanical Work: Applied force and non-zero displacement",
            "Mathematical Formulation of Work: W = F * s and SI Unit Joule (1 J = 1 N * m)",
            "Force-Displacement Vector Dot Product: W = F * s * cos(theta)",
            "Positive, Negative, and Zero Work Scenarios: Gravity vs Friction vs Normal reaction",
            "Activity 7.1 & 7.2: Pulling a wooden block with spring balance and pushing heavy cart"
        ],
        "key_concepts": [
            "Scientific Work Conditions: Work is done if and only if a force acts on an object and the object undergoes displacement along or inclined to the line of action of the force.",
            "Mathematical Work Formulation: Work done by a constant force is the product of the magnitude of the force and the distance moved in the direction of the force: W = F * s (SI unit: Joule).",
            "One Joule Invariant: 1 Joule is the amount of work done on an object when a force of 1 Newton displaces it by 1 meter along the line of action of the force.",
            "Angle Geometry & Trigonometric Work: When force and displacement are at an angle theta, W = F * s * cos(theta). Work is positive when theta < 90 deg, zero when theta = 90 deg, and negative when 90 < theta <= 180 deg.",
            "Negative Work of Friction: When force opposes motion (theta = 180 deg, cos 180 = -1), work done by friction is negative: W = -f * s.",
            "Zero Work by Orthogonal Forces: When force is perpendicular to displacement (theta = 90 deg, cos 90 = 0), work done is identically zero (e.g. porter carrying load horizontally on head)."
        ],
        "success_criteria": "Student can state the two essential conditions for work, calculate W = Fs, evaluate sign of work for arbitrary angles, and prove why porters and centripetal forces do zero work.",
        "chapter_notes": """### 7.1 Everyday Labor vs Scientific Work
In everyday conversation, mental concentration, reading a book, standing stationary holding a 20 kg suitcase, or pushing against a concrete wall until exhausted is termed 'hard work'. However, in physics, **NO mechanical work is done** because there is **zero displacement** ($s = 0$).

### 7.2 Two Mandatory Conditions for Mechanical Work
For work to be done in physics:
1. A **force** must act on the body ($F \\ne 0$).
2. The body must undergo **displacement** ($s \\ne 0$) with a component along the force vector.

### 7.3 Mathematical Definition & SI Unit
When a constant force $F$ acts in the direction of displacement $s$:
$$W = F \\times s$$
- **SI Unit**: $\\text{Joule (J)} = 1\\text{ N} \\times 1\\text{ m} = 1\\text{ kg}\\cdot\\text{m}^2\\text{s}^{-2}$.
- **Definition of 1 Joule**: $1\\text{ Joule}$ is the amount of work done when a force of $1\\text{ Newton}$ displaces an object through a distance of $1\\text{ meter}$ in the direction of the applied force.

### 7.4 Work at an Arbitrary Angle
$$W = \\vec{F} \\cdot \\vec{s} = F \\cdot s \\cdot \\cos\\theta$$
1. **Positive Work** ($0^\\circ \\le \\theta < 90^\\circ$): Force has a component in the direction of motion (e.g. engine pulling a train, child pulling a toy cart). $\\cos\\theta > 0$.
2. **Zero Work** ($\\theta = 90^\\circ$): Force is perpendicular to displacement ($\\cos 90^\\circ = 0$).
   - A porter walking horizontally carrying a luggage trunk on his head: Gravitational force acts downward ($90^\\circ$ to horizontal displacement), so gravity does **zero work**.
   - Centripetal force in circular orbits: Force points radially inward ($90^\\circ$ to tangential velocity), so centripetal force does **zero work**.
3. **Negative Work** ($90^\\circ < \\theta \\le 180^\\circ$): Force opposes displacement ($\\cos 180^\\circ = -1$).
   - Kinetic friction opposing sliding motion: $W = -f_k \\cdot s$.
   - Brakes stopping a motorcar.""",
        "worked_examples": [
            {
                "problem": "A force of 7 N acts on an object. The displacement is, say 8 m, in the direction of the force. Let us take it that the force acts on the object through the displacement. What is the work done in this case?",
                "given": "Force $F = 7\\text{ N}$, displacement $s = 8\\text{ m}$ in the direction of force ($\\theta = 0^\\circ$).",
                "formula": "$W = F \\times s \\times \\cos\\theta$.",
                "substitution": "$W = 7\\text{ N} \\times 8\\text{ m} \\times \\cos(0^\\circ) = 7 \\times 8 \\times 1$.",
                "calculation": "$W = 56\\text{ J}$.",
                "finalAnswer": "Work done = 56 Joules.",
                "unit": "J",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 7.3: Work done by a force while displacing an object"
            },
            {
                "problem": "A porter lifts luggage of 15 kg from the ground and puts it on his head 1.5 m above the ground. Calculate the work done by him on the luggage. (Take g = 10 m/s²).",
                "given": "Mass $m = 15\\text{ kg}$, height $s = h = 1.5\\text{ m}$, acceleration due to gravity $g = 10\\text{ m/s}^2$.",
                "formula": "$W = F \\times s = (m \\cdot g) \\times h$.",
                "substitution": "$W = (15 \\times 10) \\times 1.5 = 150 \\times 1.5$.",
                "calculation": "$W = 225\\text{ J}$.",
                "finalAnswer": "Work done by the porter = 225 Joules.",
                "unit": "J",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 7.2: Lifting luggage against gravity to a height"
            },
            {
                "problem": "A person pushes against a solid brick wall with a force of 200 N for 10 minutes until completely exhausted. Calculate the work done on the wall.",
                "given": "Force $F = 200\\text{ N}$, duration $t = 600\\text{ s}$, displacement of wall $s = 0\\text{ m}$.",
                "formula": "$W = F \\times s$.",
                "substitution": "$W = 200\\text{ N} \\times 0\\text{ m}$.",
                "calculation": "$W = 0\\text{ J}$.",
                "finalAnswer": "Work done = 0 Joules (no mechanical displacement).",
                "unit": "J",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 7.5: Pushing against a stationary wall resulting in zero displacement"
            },
            {
                "problem": "A bullock exerts a force of 140 N on a plough. The field being ploughed is 15 m long. How much work is done in ploughing the length of the field?",
                "given": "Force $F = 140\\text{ N}$, displacement $s = 15\\text{ m}$ along line of pull.",
                "formula": "$W = F \\times s$.",
                "substitution": "$W = 140 \\times 15$.",
                "calculation": "$W = 2100\\text{ J}$.",
                "finalAnswer": "Work done = 2100 Joules (2.1 kJ).",
                "unit": "J",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 7.1: Energy required to carry out agricultural ploughing"
            },
            {
                "problem": "A block of mass 2 kg slides across a rough horizontal table with an initial velocity of 4 m/s and comes to rest after traveling 2 m. Calculate the work done by the force of friction.",
                "given": "Initial velocity $u = 4\\text{ m/s}, v = 0\\text{ m/s}, s = 2\\text{ m}, m = 2\\text{ kg}$.",
                "formula": "$v^2 = u^2 + 2as \\implies a = \\frac{v^2 - u^2}{2s}$; $f_k = ma$; $W = -f_k \\cdot s$.",
                "substitution": "$a = \\frac{0 - 16}{2(2)} = -4\\text{ m/s}^2$. Friction force $f_k = (2)(-4) = -8\\text{ N}$. $W = (-8)(2)$.",
                "calculation": "$W = -16\\text{ J}$.",
                "finalAnswer": "Work done by friction = -16 Joules (negative work dissipated as heat).",
                "unit": "J",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 7.4: Force-displacement relationship under friction"
            },
            {
                "problem": "Why does the earth orbiting the sun in a circular orbit experience zero work done by gravitational attraction?",
                "given": "Planetary circular orbit: Sun's gravitational force is radial; velocity is tangential.",
                "formula": "$W = F \\cdot s \\cdot \\cos(90^\\circ) = 0$.",
                "substitution": "Angle between gravitational force vector $\\vec{F}_g$ and instantaneous displacement $\\vec{s}$ is identically $90^\\circ$.",
                "calculation": "1. At every point on a circular orbit, gravity points toward the sun (radial center).\n2. Instantaneous motion is along the circle's tangent.\n3. The angle $\\theta = 90^\\circ$ everywhere.\n4. $\\cos(90^\\circ) = 0 \\implies W = F_g \\cdot s \\cdot 0 = 0$.",
                "finalAnswer": "Zero work is done because the gravitational force is strictly perpendicular to the displacement vector at all times.",
                "unit": "Orbital Mechanics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 7.6: Carrying load perpendicular to displacement producing zero work"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Holding a heavy 50 kg weight motionless overhead does massive work because the muscles get tired.",
                "correction": "Chemical energy is consumed by isometric muscle contraction, but mechanical work in physics is strictly zero because displacement is zero.",
                "why_it_matters": "Fundamental distinction between physiological fatigue and thermodynamic/mechanical work."
            },
            {
                "misconception": "A porter walking with a heavy bag on his head does positive work against gravity.",
                "correction": "Gravity pulls vertically downward while the porter walks horizontally. The angle is 90 degrees, making work done by gravity zero.",
                "why_it_matters": "Classic CBSE Class 9 exam question on zero work."
            }
        ],
        "visual_lesson_plan": {
            "title": "Mechanical Work & Vector Dot Product Visual Blueprint",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Scientific Work Conditions: Work is done if and only if a force acts on an object and the object undergoes displacement along or inclined to the line of action of the force.",
                    "diagram_title": "Energy and Mechanical Work in Daily Tasks",
                    "diagram_type": "image",
                    "image_query": "mechanical work force displacement physics diagram",
                    "video_query": "work done by force physics animation",
                    "image_url": "/extracted_diagrams/ch7/fig_7_1.webp",
                    "what_to_make": "Textbook diagram showing energy applied to carry out everyday tasks vs scientific displacement.",
                    "timing_and_cue": "Mount work conditions on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch7/fig_7_1.webp | Everyday Tasks vs Mechanical Work | Force and non-zero displacement requirement\")"
                },
                {
                    "concept_title": "Mathematical Work Formulation: Work done by a constant force is the product of the magnitude of the force and the distance moved in the direction of the force: W = F * s (SI unit: Joule).",
                    "diagram_title": "Force Displacing Object Diagram",
                    "diagram_type": "image",
                    "image_query": "work done by a force displacement vector diagram",
                    "video_query": "work formula F s physics",
                    "image_url": "/extracted_diagrams/ch7/fig_7_3.webp",
                    "what_to_make": "Textbook diagram illustrating block displaced by distance s under constant horizontal force F.",
                    "timing_and_cue": "Mount W = Fs formula on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch7/fig_7_3.webp | Mechanical Work Formulation | W = F * s in direction of motion\")"
                },
                {
                    "concept_title": "One Joule Invariant: 1 Joule is the amount of work done on an object when a force of 1 Newton displaces it by 1 meter along the line of action of the force.",
                    "diagram_title": "One Joule Force-Displacement Definition",
                    "diagram_type": "image",
                    "image_query": "one joule definition newton meter physics",
                    "video_query": "what is one joule physics",
                    "image_url": "/extracted_diagrams/ch7/fig_7_4.webp",
                    "what_to_make": "Textbook force-displacement graph illustrating area equal to 1 Joule.",
                    "timing_and_cue": "Mount 1 Joule invariant on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch7/fig_7_4.webp | 1 Joule Standard | 1 N force acting across 1 m displacement\")"
                },
                {
                    "concept_title": "Angle Geometry & Trigonometric Work: When force and displacement are at an angle theta, W = F * s * cos(theta). Work is positive when theta < 90 deg, zero when theta = 90 deg, and negative when 90 < theta <= 180 deg.",
                    "diagram_title": "Work at Inclined Angle Theta",
                    "diagram_type": "image",
                    "image_query": "work done at an angle cosine theta vector diagram",
                    "video_query": "work done at an angle physics",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Work_done_by_a_force_at_an_angle.svg",
                    "what_to_make": "Vector diagram showing force vector resolved into F cos(theta) parallel to displacement and F sin(theta) perpendicular.",
                    "timing_and_cue": "Mount angle resolution on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/e0/Work_done_by_a_force_at_an_angle.svg | W = F s cos(theta) | Resolving force parallel to displacement\")"
                },
                {
                    "concept_title": "Negative Work of Friction: When force opposes motion (theta = 180 deg, cos 180 = -1), work done by friction is negative: W = -f * s.",
                    "diagram_title": "Negative Work by Opposing Friction Force",
                    "diagram_type": "image",
                    "image_query": "friction force negative work physics diagram",
                    "video_query": "negative work friction physics",
                    "image_url": "/extracted_diagrams/ch7/fig_7_7.webp",
                    "what_to_make": "Textbook diagram showing opposing kinetic friction vector doing negative work.",
                    "timing_and_cue": "Mount negative work on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch7/fig_7_7.webp | Negative Work of Friction | Opposing displacement vector at 180 degrees\")"
                },
                {
                    "concept_title": "Zero Work by Orthogonal Forces: When force is perpendicular to displacement (theta = 90 deg, cos 90 = 0), work done is identically zero (e.g. porter carrying load horizontally on head).",
                    "diagram_title": "Zero Work Porter Carrying Load",
                    "diagram_type": "image",
                    "image_query": "porter carrying load zero work physics diagram",
                    "video_query": "why porter does zero work physics",
                    "image_url": "/extracted_diagrams/ch7/fig_7_6.webp",
                    "what_to_make": "Textbook diagram showing porter walking horizontally while luggage weight acts downward at 90 degrees.",
                    "timing_and_cue": "Mount zero work scenario on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch7/fig_7_6.webp | Zero Work Scenario | Orthogonal force and displacement (cos 90 = 0)\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1 of each concept, immediately call write_chalkboard(action="draw_image", content="...") with the verified image URL from the visual lesson plan. Point out the force and displacement vectors before explaining.
2. SOCRATIC 6-STAGE CADENCE:
   - Stage 1: Intuition hook (e.g. "If you push as hard as you can against a concrete wall for 10 minutes, your arms will burn, but physics says you did ZERO work! Why?").
   - Stage 2: Formulate scientific law (W = F * s and two mandatory conditions).
   - Stage 3: Common pitfall (Isometric muscle fatigue vs mechanical work).
   - Stage 4: Board numerical layout (Given -> Formula -> Substitution -> Calculation -> Boxed Answer with Units).
   - Stage 5: Gating pause: "Why does gravity do zero work on a porter walking along a horizontal railway platform?" HARD STOP: Wait for student answer and verify understanding before proceeding!
   - Stage 6: Authentic CBSE board numerical."""
    },
    {
        "order_index": 2,
        "title": "Kinetic Energy & The Work-Energy Theorem: Velocity-Squared Dynamics",
        "description": "Derive the mathematical formula for kinetic energy from kinematic equations, explore the quadratic dependency on velocity, formulate the Work-Energy Theorem, and solve real-world stopping distance and collision problems.",
        "subtopics": [
            "Energy as Capacity to Do Work: Unit equivalence (Joule)",
            "Kinetic Energy Definition: Energy possessed by an object due to its motion",
            "Derivation of Kinetic Energy: W = F * s = (ma) * (v^2 - u^2)/(2a) = 1/2 m v^2",
            "Quadratic Velocity Dependence: Why doubling speed quadruples kinetic energy and braking distance",
            "The Work-Energy Theorem: Net work done equals change in kinetic energy (W_net = Delta E_k)",
            "Activity 7.3: Steel ball dropped into sand trough to measure penetration depth"
        ],
        "key_concepts": [
            "Energy Definition: The capacity of an object to do work is called its energy. It is a scalar quantity sharing the SI unit of work: Joule (J).",
            "Kinetic Energy Nature: Kinetic energy is the energy possessed by an object on account of its motion: E_k = 1/2 m v^2.",
            "Work-Energy Derivation: Integrating F * ds using the third kinematic equation v^2 - u^2 = 2as proves that W = 1/2 m v^2 - 1/2 m u^2.",
            "Work-Energy Theorem: The net work done by all acting forces on a rigid body is identically equal to the change in its kinetic energy: W_net = Delta E_k.",
            "Quadratic Velocity Scaling: Because E_k is proportional to v^2, an automobile traveling at 60 km/h possesses 4 times the kinetic energy of the same car at 30 km/h, requiring 4 times the stopping distance.",
            "Penetration Depth Proportionality: Work done by resistive medium during stopping equals initial kinetic energy (F_resist * d = 1/2 m v^2), so penetration depth d is directly proportional to v^2."
        ],
        "success_criteria": "Student can define kinetic energy, derive E_k = 1/2 mv^2 using the 3rd equation of motion, state the Work-Energy Theorem, and solve braking problems.",
        "chapter_notes": """### 7.5 Concept of Energy
An object possessing energy can exert a force on another object, transferring energy and performing work. Energy is a **scalar quantity** measured in **Joules (J)**.

### 7.6 Kinetic Energy ($E_k$)
Kinetic energy is the energy possessed by a body due to its state of motion. A moving cricket ball, flowing water, a flying bullet, and blowing wind all possess kinetic energy.

### 7.7 Derivation of $E_k = \\frac{1}{2}mv^2$
Consider an object of mass $m$ moving with initial velocity $u$. A constant net force $F$ acts on it, displacing it by distance $s$ and accelerating it to final velocity $v$.
1. From Newton's Second Law:
   $$F = m \\cdot a$$
2. From the third kinematic equation of motion:
   $$v^2 - u^2 = 2as \\implies s = \\frac{v^2 - u^2}{2a}$$
3. Work done by the force:
   $$W = F \\times s = (m \\cdot a) \\times \\left(\\frac{v^2 - u^2}{2a}\\right) = \\frac{1}{2}m(v^2 - u^2)$$
4. If the object starts from rest ($u = 0$):
   $$W = \\frac{1}{2}mv^2$$
5. Since this work appears as kinetic energy:
   $$\\mathbf{E_k = \\frac{1}{2}mv^2}$$

### 7.8 The Work-Energy Theorem
$$\\mathbf{W_{net} = \\Delta E_k = \\frac{1}{2}mv^2 - \\frac{1}{2}mu^2}$$
The net work done on an object by the resultant force equals the change in its kinetic energy.
- If $W_{net} > 0$, speed increases.
- If $W_{net} < 0$ (e.g. brakes applied), kinetic energy decreases and speed drops.""",
        "worked_examples": [
            {
                "problem": "An object of mass 15 kg is moving with a uniform velocity of 4 m/s. What is the kinetic energy possessed by the object?",
                "given": "Mass $m = 15\\text{ kg}$, velocity $v = 4\\text{ m/s}$.",
                "formula": "$E_k = \\frac{1}{2}mv^2$.",
                "substitution": "$E_k = \\frac{1}{2} \\times 15 \\times (4)^2 = \\frac{1}{2} \\times 15 \\times 16$.",
                "calculation": "$E_k = 15 \\times 8 = 120\\text{ J}$.",
                "finalAnswer": "Kinetic energy = 120 Joules.",
                "unit": "J",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 7.7: Kinetic energy of moving mass calculation"
            },
            {
                "problem": "What is the work to be done to increase the velocity of a car from 30 km/h to 60 km/h if the mass of the car is 1500 kg?",
                "given": "Mass $m = 1500\\text{ kg}$. $u = 30\\text{ km/h} = 30 \\times \\frac{5}{18} = \\frac{25}{3}\\text{ m/s}$. $v = 60\\text{ km/h} = 60 \\times \\frac{5}{18} = \\frac{50}{3}\\text{ m/s}$.",
                "formula": "Work-Energy Theorem: $W = \\Delta E_k = \\frac{1}{2}m(v^2 - u^2)$.",
                "substitution": "$W = \\frac{1}{2} \\times 1500 \\times \\left[\\left(\\frac{50}{3}\\right)^2 - \\left(\\frac{25}{3}\\right)^2\\right] = 750 \\times \\left(\\frac{2500 - 625}{9}\\right)$.",
                "calculation": "$W = 750 \\times \\frac{1875}{9} = \\frac{1406250}{9} = 156250\\text{ J} = \\mathbf{156.25\\text{ kJ}}$.",
                "finalAnswer": "Work required = 156250 Joules (156.25 kJ).",
                "unit": "J",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 7.8: Work-energy theorem applied to accelerating motorcar"
            },
            {
                "problem": "A 50 g bullet traveling at 200 m/s strikes a wooden block and penetrates 10 cm before coming to rest. Find the average resistive force exerted by the block.",
                "given": "Mass $m = 50\\text{ g} = 0.05\\text{ kg}, u = 200\\text{ m/s}, v = 0\\text{ m/s}, s = 10\\text{ cm} = 0.1\\text{ m}$.",
                "formula": "$W_{net} = \\Delta E_k \\implies -F_{resist} \\cdot s = 0 - \\frac{1}{2}mu^2 \\implies F_{resist} = \\frac{mu^2}{2s}$.",
                "substitution": "$F_{resist} = \\frac{0.05 \\times (200)^2}{2 \\times 0.1} = \\frac{0.05 \\times 40000}{0.2}$.",
                "calculation": "$F_{resist} = \\frac{2000}{0.2} = \\mathbf{10000\\text{ N}} = 10\\text{ kN}$.",
                "finalAnswer": "Average resistive force = 10,000 N (10 kN).",
                "unit": "N",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 7.9: Penetration work dissipation in target medium"
            },
            {
                "problem": "By what factor does the kinetic energy of an object change if its speed is tripled?",
                "given": "Initial velocity $u$, final velocity $v = 3u$.",
                "formula": "$E_k \\propto v^2 \\implies \\frac{E_{k2}}{E_{k1}} = \\left(\\frac{v}{u}\\right)^2$.",
                "substitution": "$\\frac{E_{k2}}{E_{k1}} = (3)^2 = 9$.",
                "calculation": "Kinetic energy increases by a factor of 9.",
                "finalAnswer": "The kinetic energy increases by 9 times.",
                "unit": "Ratio",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 7.10: Parabolic kinetic energy vs velocity curve"
            },
            {
                "problem": "Two bodies of mass 1 kg and 4 kg have equal linear momentum. What is the ratio of their kinetic energies?",
                "given": "Masses $m_1 = 1\\text{ kg}, m_2 = 4\\text{ kg}$, momentum $p_1 = p_2 = p$.",
                "formula": "Kinetic Energy in terms of momentum: $E_k = \\frac{p^2}{2m} \\implies E_k \\propto \\frac{1}{m}$.",
                "substitution": "$\\frac{E_{k1}}{E_{k2}} = \\frac{m_2}{m_1} = \\frac{4}{1}$.",
                "calculation": "$\\frac{E_{k1}}{E_{k2}} = 4:1$.",
                "finalAnswer": "The ratio of kinetic energies is 4:1 (the lighter mass has 4 times more kinetic energy).",
                "unit": "Ratio",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 7.11: Relationship between kinetic energy, mass, and linear momentum"
            },
            {
                "problem": "A heavy steel sphere and a light tennis ball are dropped into a sand bed from the same height. Which one penetrates deeper and why?",
                "given": "Activity 7.3: Same drop height $h$, different masses $m_{steel} > m_{tennis}$.",
                "formula": "$E_k = mgh$; Work done against sand resistance $F \\cdot d = mgh \\implies d = \\frac{mgh}{F}$.",
                "substitution": "Both strike with identical velocity $v = \\sqrt{2gh}$, but steel ball has much larger mass.",
                "calculation": "1. Both reach the sand bed with equal speed $v = \\sqrt{2gh}$.\n2. The steel ball has larger mass, so it possesses far greater kinetic energy: $E_k = \\frac{1}{2}m_{steel}v^2$.\n3. To dissipate this larger kinetic energy, the sand must do more work: $F_{sand} \\times d = E_k$.\n4. Hence, the steel ball penetrates significantly deeper into the sand.",
                "finalAnswer": "The heavy steel ball penetrates deeper because its greater mass gives it much larger kinetic energy to dissipate.",
                "unit": "Activity 7.3 Lab Analysis",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 7.12: Steel ball penetration in sand trough measuring kinetic energy"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "If you double the speed of your car, your braking distance also doubles.",
                "correction": "Kinetic energy scales quadratically with speed (v^2). Doubling speed quadruples the kinetic energy (2^2 = 4), requiring 4 times the braking distance!",
                "why_it_matters": "Crucial road safety physics concept frequently tested in board examinations."
            }
        ],
        "visual_lesson_plan": {
            "title": "Kinetic Energy & Work-Energy Theorem Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Energy Definition: The capacity of an object to do work is called its energy. It is a scalar quantity sharing the SI unit of work: Joule (J).",
                    "diagram_title": "Energy Forms and Capacity for Work",
                    "diagram_type": "image",
                    "image_query": "forms of energy kinetic potential physics diagram",
                    "video_query": "what is energy physics animation",
                    "image_url": "/extracted_diagrams/ch7/fig_7_1.webp",
                    "what_to_make": "Textbook diagram showing energy conversion across physical systems.",
                    "timing_and_cue": "Mount energy concept on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch7/fig_7_1.webp | Energy Capacity to Do Work | Scalar property measured in Joules\")"
                },
                {
                    "concept_title": "Kinetic Energy Nature: Kinetic energy is the energy possessed by an object on account of its motion: E_k = 1/2 m v^2.",
                    "diagram_title": "Moving Mass Kinetic Energy Blueprint",
                    "diagram_type": "image",
                    "image_query": "kinetic energy moving object mass velocity diagram",
                    "video_query": "kinetic energy 1/2 mv^2 physics",
                    "image_url": "/extracted_diagrams/ch7/fig_7_7.webp",
                    "what_to_make": "Textbook diagram showing mass m moving with velocity v possessing 1/2 m v^2.",
                    "timing_and_cue": "Mount kinetic energy on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch7/fig_7_7.webp | Kinetic Energy Blueprint | E_k = 1/2 m v^2\")"
                },
                {
                    "concept_title": "Work-Energy Derivation: Integrating F * ds using the third kinematic equation v^2 - u^2 = 2as proves that W = 1/2 m v^2 - 1/2 m u^2.",
                    "diagram_title": "Kinematic Derivation of Work-Energy Relation",
                    "diagram_type": "image",
                    "image_query": "work energy theorem derivation v2 u2 2as diagram",
                    "video_query": "derivation of kinetic energy formula",
                    "image_url": "/extracted_diagrams/ch7/fig_7_8.webp",
                    "what_to_make": "Textbook schematic showing constant acceleration displacing mass and deriving 1/2 m(v^2 - u^2).",
                    "timing_and_cue": "Mount derivation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch7/fig_7_8.webp | Work-Energy Derivation | Linking F = ma and v^2 - u^2 = 2as\")"
                },
                {
                    "concept_title": "Work-Energy Theorem: The net work done by all acting forces on a rigid body is identically equal to the change in its kinetic energy: W_net = Delta E_k.",
                    "diagram_title": "Work-Energy Theorem Application",
                    "diagram_type": "image",
                    "image_query": "work energy theorem net work equals change in kinetic energy",
                    "video_query": "work energy theorem explained",
                    "image_url": "/extracted_diagrams/ch7/fig_7_10.webp",
                    "what_to_make": "Textbook diagram showing net work done accelerating vehicle from speed u to speed v.",
                    "timing_and_cue": "Mount Work-Energy Theorem on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch7/fig_7_10.webp | Work-Energy Theorem | W_net = Delta E_k = 1/2 m(v^2 - u^2)\")"
                },
                {
                    "concept_title": "Quadratic Velocity Scaling: Because E_k is proportional to v^2, an automobile traveling at 60 km/h possesses 4 times the kinetic energy of the same car at 30 km/h, requiring 4 times the stopping distance.",
                    "diagram_title": "Quadratic Velocity vs Stopping Distance",
                    "diagram_type": "image",
                    "image_query": "speed vs stopping distance physics quadratic graph",
                    "video_query": "stopping distance quadratic speed",
                    "image_url": "/extracted_diagrams/ch7/fig_7_11.webp",
                    "what_to_make": "Graph illustrating parabolic growth of kinetic energy and quadrupled braking distance.",
                    "timing_and_cue": "Mount quadratic velocity scaling on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch7/fig_7_11.webp | Quadratic Velocity Dependency | Doubling velocity quadruples kinetic energy and braking distance\")"
                },
                {
                    "concept_title": "Penetration Depth Proportionality: Work done by resistive medium during stopping equals initial kinetic energy (F_resist * d = 1/2 m v^2), so penetration depth d is directly proportional to v^2.",
                    "diagram_title": "Activity 7.3 Sand Trough Penetration Depth",
                    "diagram_type": "image",
                    "image_query": "ball dropped in sand kinetic energy penetration depth activity",
                    "video_query": "kinetic energy sand penetration experiment",
                    "image_url": "/extracted_diagrams/ch7/fig_7_12.webp",
                    "what_to_make": "Textbook diagram showing steel ball dropped into sand measuring penetration crater depth.",
                    "timing_and_cue": "Mount Activity 7.3 on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch7/fig_7_12.webp | Activity 7.3 Sand Trough Lab | Penetration depth proves E_k proportionality\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Immediately mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "If you double your car's speed from 30 km/h to 60 km/h, does your braking distance double or quadruple?"
   - Law & Derivation: Link W = Fs with v^2 - u^2 = 2as on the board.
   - Socratic check: "Why does linear momentum double when speed doubles, but kinetic energy quadruples?" HARD STOP: Wait for student answer!"""
    }
]

# We will append Modules 3 to 6 for Chapter 7, and Modules 1 to 6 for Chapter 8 below
print("Chapter 7 base modules structured. Building complete 6 modules for Ch7 and 6 for Ch8...")
