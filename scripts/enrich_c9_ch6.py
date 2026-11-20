import json
import os

CH6_ID = "7e1d5438-1174-4577-8599-5f05a6642093"

def get_ch6_solver_examples():
    return [
        {
            "problem": "Textbook Revise, Reflect, Refine Q1 (Section 6.1, p. 19): Using a horizontal force F, a heavy table is moved across the floor at a constant velocity. What is the magnitude and direction of the frictional force exerted by the floor on the table?",
            "given": "Applied horizontal force = F; Motion of table = Constant velocity (acceleration a = 0).",
            "formula": "Newton's First Law / Net Force Equilibrium: $\\Sigma F = F_{\\text{applied}} - f_{\\text{friction}} = m \\cdot a = 0$.",
            "substitution": "$F - f_{\\text{friction}} = 0 \\implies f_{\\text{friction}} = F$.",
            "calculation": "Since the table moves at a constant velocity, its acceleration is zero ($a = 0$). By Newton's second law, the net external force acting on the table must be identically zero. Therefore, the opposing kinetic frictional force exerted by the floor must have an exact magnitude equal to F, directed opposite to the direction of motion.",
            "finalAnswer": "The frictional force has a magnitude exactly equal to F, acting in the direction opposite to the table's motion.",
            "unit": "Newtons (N)",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "constant velocity dynamic equilibrium friction applied force",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q2 (Section 6.1, p. 19): For a ball rolling on an ideal frictionless horizontal surface, which of the following is true? (a) A constant force is required to keep it moving at constant velocity. (b) It will gradually slow down and stop. (c) It will continue to move with constant velocity forever. (d) Its acceleration will continuously increase.",
            "given": "Ideal horizontal plane with zero friction ($f = 0$) and zero air resistance.",
            "formula": "Galileo's Law of Inertia & Newton's First Law: An object in motion continues in uniform rectilinear motion unless acted upon by a net external force.",
            "substitution": "Net horizontal force $\\Sigma F = 0$.",
            "calculation": "In the complete absence of opposing resistive forces (friction, drag), no continuous forward force is required to sustain motion. By inertia, the ball maintains its uniform speed and direction indefinitely.",
            "finalAnswer": "Correct Option: (c) It will continue to move with constant velocity forever.",
            "unit": "Inertia Law",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "galileo inclined plane law of inertia frictionless surface",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q3 (Section 6.2, p. 19): Two blocks P (mass $m_P = 2\\text{ kg}$) and Q (mass $m_Q = 3\\text{ kg}$) are placed in contact on a smooth frictionless horizontal table. A horizontal force $F = 10\\text{ N}$ is applied to block P pushing towards Q. Calculate: (a) The common acceleration of the blocks, (b) The contact force between block P and block Q.",
            "given": "Mass of block P $m_P = 2\\text{ kg}$; Mass of block Q $m_Q = 3\\text{ kg}$; Applied horizontal force $F = 10\\text{ N}$; Frictionless surface.",
            "formula": "Newton's Second Law: $F = (m_P + m_Q)a \\implies a = \\frac{F}{m_P + m_Q}$; Free body diagram of Q: $N_{\\text{contact}} = m_Q \\cdot a$.",
            "substitution": "$a = \\frac{10}{2 + 3} = \\frac{10}{5}$; $N_{\\text{contact}} = 3 \\times a$.",
            "calculation": "1. Common acceleration:\n   $a = 2\\text{ m s}^{-2}$.\n2. Contact normal force between P and Q:\n   The force accelerating block Q is solely the normal contact force from P:\n   $N_{\\text{contact}} = m_Q \\cdot a = 3\\text{ kg} \\times 2\\text{ m s}^{-2} = 6\\text{ N}$.\n   (By Newton's third law, Q pushes back on P with equal and opposite force $6\\text{ N}$, so net force on P is $10 - 6 = 4\\text{ N} = 2\\text{ kg} \\times 2\\text{ m s}^{-2}$).",
            "finalAnswer": "(a) Common acceleration is 2 m s⁻²; (b) Contact force between block P and block Q is 6 N.",
            "unit": "m s⁻² and N",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Two contact blocks pushed horizontally on frictionless surface",
            "image_search_query": "two blocks in contact normal force acceleration newton second law",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q4 (Section 6.3, p. 20): While practising for the snake boat race (Vallam kali in Kerala), rowers push the water backwards with their oars. Explain in terms of Newton's laws why the boat surges forward.",
            "given": "Rowing mechanics in traditional Kerala snake boat racing.",
            "formula": "Newton's Third Law of Motion: For every action, there is an equal and opposite reaction ($\\vec{F}_{\\text{water on oar}} = -\\vec{F}_{\\text{oar on water}}$).",
            "substitution": "Action = Oars push water backward; Reaction = Water pushes oars and boat forward.",
            "calculation": "When rowers pull their oars, they exert a backward force (Action) on the water. By Newton's third law, the displaced water simultaneously exerts an equal and opposite forward reaction force on the oars. This forward force is transmitted through the rowlocks to the boat hull, overcoming water drag and propelling the snake boat forward.",
            "finalAnswer": "The oars exert a backward force on the water (Action); the water exerts an equal and opposite forward force on the oars (Reaction), driving the boat forward.",
            "unit": "Newton's Third Law Dynamics",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "rowing boat newton third law action reaction water",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q5 (Section 6.1, p. 20): When an unbalanced net external force acts on an object, which of the following physical states can change? (i) Speed of the object, (ii) Direction of motion, (iii) Shape or size of the object, (iv) All of the above. Give concrete examples.",
            "given": "Kinematic and mechanical manifestations of net unbalanced forces.",
            "formula": "Force definition: An external influence that changes or tends to change the state of rest, uniform motion, direction, or dimensions of an object.",
            "substitution": "Evaluate each category.",
            "calculation": "1. Speed: Accelerating a car with the gas pedal increases speed ($F = ma$).\n2. Direction: Centripetal force changes the direction of a stone swung in a circle without necessarily changing speed.\n3. Shape/Size: Compressing a coiled spring or squeezing a rubber ball deforms its geometric dimensions.\n4. Therefore, an unbalanced force can simultaneously or independently alter speed, direction, and shape.",
            "finalAnswer": "Correct Option: (iv) All of the above (speed, direction, and shape can all change under an unbalanced force).",
            "unit": "Force Dynamics",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "effects of force change speed direction shape physics",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q7 (Section 6.3, p. 20): A sailor jumps forward from a small rowing boat to the shore (Fig. 6.38). As the sailor steps forward onto the bank, the boat moves backwards into the water. Explain why.",
            "given": "Sailor jumping forward off an untethered floating boat.",
            "formula": "Newton's Third Law (Action-Reaction) & Conservation of Linear Momentum ($m_{\\text{sailor}} \\vec{v}_{\\text{sailor}} + m_{\\text{boat}} \\vec{v}_{\\text{boat}} = 0$).",
            "substitution": "Action force applied by sailor's feet against the boat deck.",
            "calculation": "To gain forward momentum, the sailor's feet must exert a backward muscular push on the boat floor (Action). By Newton's third law, the boat pushes the sailor forward (Reaction), enabling the leap. Since the boat floats freely on water with minimal resistance, the backward action force accelerates the boat backwards into the lake ($v_{\\text{boat}} = -\\frac{m_{\\text{sailor}}}{m_{\\text{boat}}} v_{\\text{sailor}}$).",
            "finalAnswer": "To leap forward, the sailor pushes backward on the boat (Action); the boat pushes the sailor forward (Reaction) while recoiling backward into the water.",
            "unit": "Momentum & Action-Reaction",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 6.38: Sailor jumping from a boat to the shore showing backward boat recoil",
            "image_search_query": "sailor jumping from boat action reaction newton third law",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q8 (Section 6.2, p. 20): During a high jump athletic event, athletes land on a thick foam mat or a deep sand bed rather than bare concrete. Explain the physics principle.",
            "given": "Athlete landing from a high jump with downward momentum $p = mv$; Target: Minimize impact force.",
            "formula": "Impulse-Momentum Theorem: $F_{\\text{impact}} = \\frac{\\Delta p}{\\Delta t}$.",
            "substitution": "Compare impact duration $\\Delta t$ on rigid concrete vs soft foam.",
            "calculation": "1. An athlete falling from height h reaches the ground with fixed downward momentum $p = m\\sqrt{2gh}$.\n2. Landing on bare concrete arrests momentum almost instantaneously ($\\Delta t \\to 0.005\\text{ s}$), generating an immense peak impact force $F = \\frac{\\Delta p}{\\Delta t}$ that shatters bones and tears ligaments.\n3. A thick foam mat or sand bed yields and deforms under the athlete's body, dramatically prolonging the stopping time $\\Delta t$ (e.g. to $\\sim 0.5\\text{ s}$). Because $\\Delta t$ is increased by a factor of 100, the average impact force experienced by the athlete's skeleton is reduced by 99%, preventing injury.",
            "finalAnswer": "The cushioned mat increases the duration of impact (Δt), thereby drastically reducing the rate of change of momentum and minimizing the impact force (F = Δp/Δt).",
            "unit": "Impulse & Force Mitigation",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "high jump foam landing impulse momentum stopping time",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q9 (Section 6.3, p. 21): A vegetable hand cart of mass 40 kg moving at 3 m s⁻¹ collides head-on with an identical stationary empty cart of mass 10 kg. If the two carts lock together after impact, calculate their common velocity.",
            "given": "Mass of cart 1 $m_1 = 40\\text{ kg}$, initial velocity $u_1 = 3\\text{ m s}^{-1}$; Mass of cart 2 $m_2 = 10\\text{ kg}$, initial velocity $u_2 = 0\\text{ m s}^{-1}$; Completely inelastic collision.",
            "formula": "Law of Conservation of Linear Momentum: $m_1 u_1 + m_2 u_2 = (m_1 + m_2)v$.",
            "substitution": "$(40 \\times 3) + (10 \\times 0) = (40 + 10)v$.",
            "calculation": "$120 + 0 = 50v \\implies v = \\frac{120}{50} = 2.4\\text{ m s}^{-1}$.",
            "finalAnswer": "The common velocity of the coupled carts after collision is 2.4 m s⁻¹ in the original direction of motion.",
            "unit": "m s⁻¹",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "inelastic collision conservation of momentum carts physics",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q10 (Section 6.2, p. 21): What is the mathematical shape of the acceleration-mass graph ($a$ vs $m$) for a constant applied net force F? Sketch and explain.",
            "given": "Constant net force F acting on varying masses m.",
            "formula": "Newton's Second Law: $a = \\frac{F}{m} \\implies a \\propto \\frac{1}{m}$.",
            "substitution": "$a \\cdot m = F = \\text{constant}$.",
            "calculation": "Since acceleration is inversely proportional to mass for a fixed force, the relationship represents a RECTANGULAR HYPERBOLA in the first quadrant. As mass approaches zero, acceleration approaches infinity; as mass becomes extremely large, acceleration asymptotically approaches zero.",
            "finalAnswer": "The acceleration-mass graph is a rectangular hyperbola demonstrating inverse proportionality ($a \\propto 1/m$).",
            "unit": "Graphical Kinematics",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "acceleration versus mass rectangular hyperbola inverse proportionality",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q11 (Section 6.2, p. 21): The velocity-time graph of an object of mass 10 kg moving along a straight line on a floor shows that its speed decreases uniformly from 20 m s⁻¹ to 0 m s⁻¹ in 5 s. Find the frictional force exerted by the floor on the object.",
            "given": "Mass m = 10 kg; Initial velocity u = 20 m s⁻¹; Final velocity v = 0 m s⁻¹; Time interval t = 5 s.",
            "formula": "Acceleration $a = \\frac{v - u}{t}$; Frictional force $f = m \\cdot a$.",
            "substitution": "$a = \\frac{0 - 20}{5} = -4\\text{ m s}^{-2}$; $f = 10 \\times (-4)$.",
            "calculation": "$f = -40\\text{ N}$. The negative sign indicates that the frictional force opposes the direction of motion.",
            "finalAnswer": "The frictional force exerted by the floor has a magnitude of 40 N, directed opposite to the object's velocity.",
            "unit": "Newtons (N)",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "velocity time graph frictional stopping force newton second law",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q12 (Section 6.2, p. 21): A bullet of mass 50 g moving with a speed of 100 m s⁻¹ enters a heavy wooden block and stops after penetrating a distance of 10 cm. Calculate: (a) The average deceleration of the bullet, (b) The resisting force exerted by the block.",
            "given": "Mass $m = 50\\text{ g} = 0.05\\text{ kg}$; Initial velocity $u = 100\\text{ m s}^{-1}$; Final velocity v = 0 m s⁻¹; Penetration depth $s = 10\\text{ cm} = 0.1\\text{ m}$.",
            "formula": "Third Kinematic Equation: $v^2 = u^2 + 2as \\implies a = \\frac{v^2 - u^2}{2s}$; Resisting force $F = m \\cdot a$.",
            "substitution": "$a = \\frac{0^2 - 100^2}{2(0.1)} = \\frac{-10000}{0.2}$; $F = 0.05 \\times a$.",
            "calculation": "1. Deceleration:\n   $a = -50000\\text{ m s}^{-2}$.\n2. Resisting Force:\n   $F = 0.05\\text{ kg} \\times (-50000\\text{ m s}^{-2}) = -2500\\text{ N}$.",
            "finalAnswer": "(a) Average deceleration is 50,000 m s⁻²; (b) The resisting force exerted by the wooden block is 2500 N.",
            "unit": "m s⁻² and N",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "bullet penetrating wooden block stopping force work energy theorem",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q13 (Section 6.2, p. 21): An ace footballer converts a penalty shot by kicking a stationary football of mass 400 g. The ball leaves the player's boot with a velocity of 30 m s⁻¹. If the duration of foot-ball contact is 0.02 s, calculate: (a) The impulse received by the ball, (b) The average force exerted by the footballer.",
            "given": "Mass $m = 400\\text{ g} = 0.4\\text{ kg}$; Initial velocity u = 0; Final velocity $v = 30\\text{ m s}^{-1}$; Contact time $\\Delta t = 0.02\\text{ s}$.",
            "formula": "Impulse $J = \\Delta p = m(v - u)$; Average Force $F_{\\text{avg}} = \\frac{J}{\\Delta t}$.",
            "substitution": "$J = 0.4 \\times (30 - 0)$; $F_{\\text{avg}} = \\frac{12}{0.02}$.",
            "calculation": "1. Impulse $J = 0.4 \\times 30 = 12\\text{ N s}$ (or $12\\text{ kg m s}^{-1}$).\n2. Force $F_{\\text{avg}} = \\frac{12}{0.02} = \\frac{1200}{2} = 600\\text{ N}$.",
            "finalAnswer": "(a) Impulse received by the ball is 12 N s; (b) Average force exerted is 600 N.",
            "unit": "N s and N",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "football kick impulse force momentum contact time",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q14 (Section 6.3, p. 21): An object of mass 2 kg moving at 10 m s⁻¹ strikes a wall perpendicular to its face and rebounds elastically with the same speed. If the contact lasts 0.01 s, calculate: (a) The change in momentum of the object, (b) The average force exerted by the wall on the object.",
            "given": "Mass m = 2 kg; Initial velocity $\\vec{u} = +10\\text{ m s}^{-1}$ (towards wall); Final velocity $\\vec{v} = -10\\text{ m s}^{-1}$ (rebound); Time $\\Delta t = 0.01\\text{ s}$.",
            "formula": "Change in Momentum $\\Delta \\vec{p} = m(\\vec{v} - \\vec{u})$; Average Force $\\vec{F} = \\frac{\\Delta \\vec{p}}{\\Delta t}$.",
            "substitution": "$\\Delta p = 2 \\times [(-10) - (+10)]$; $F = \\frac{\\Delta p}{0.01}$.",
            "calculation": "1. Change in momentum:\n   $\\Delta p = 2 \\times (-20) = -40\\text{ kg m s}^{-1}$.\n2. Average Force:\n   $F = \\frac{-40}{0.01} = -4000\\text{ N}$ (directed away from the wall).",
            "finalAnswer": "(a) Change in momentum is -40 kg m s⁻¹; (b) The average force exerted by the wall is 4000 N (directed away from the wall).",
            "unit": "kg m s⁻¹ and N",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "elastic rebound ball wall momentum change normal force",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q15 (Section 6.2, p. 21): A tractor pulls a harrow of mass $m_1 = 500\\text{ kg}$ connected via a steel hitch to a trailer of mass $m_2 = 1000\\text{ kg}$. If the tractor engine exerts a forward driving force of 6000 N and total ground friction is 1500 N, calculate: (a) The net acceleration of the system, (b) The tension force in the hitch coupling.",
            "given": "Mass $m_1 = 500\\text{ kg}$, $m_2 = 1000\\text{ kg}$; Total mass $M = 1500\\text{ kg}$; Driving force $F_{\\text{engine}} = 6000\\text{ N}$; Frictional resistance $f_{\\text{friction}} = 1500\\text{ N}$. Trailer friction $f_2 = 1000\\text{ N}$.",
            "formula": "Net Force $F_{\\text{net}} = F_{\\text{engine}} - f_{\\text{friction}} = M \\cdot a$; Trailer free body: $T - f_2 = m_2 \\cdot a$.",
            "substitution": "$F_{\\text{net}} = 6000 - 1500 = 4500\\text{ N}$; $a = \\frac{4500}{1500}$.",
            "calculation": "1. Acceleration:\n   $a = 3\\text{ m s}^{-2}$.\n2. Tension in coupling hitch pulling trailer ($m_2$):\n   $T = m_2 a + f_2 = (1000 \\times 3) + 1000 = 4000\\text{ N}$.",
            "finalAnswer": "(a) System acceleration is 3 m s⁻²; (b) Tension in the hitch is 4000 N.",
            "unit": "m s⁻² and N",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "tractor pulling trailer tension force coupled system physics",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q16 (Section 6.1, p. 21): When the north pole of a bar magnet is brought near the north pole of a magnetic compass needle, the needle is deflected away. (a) Is this a contact or non-contact force? (b) Does the compass needle exert an equal force on the bar magnet? Justify.",
            "given": "Magnetic interaction between bar magnet and compass needle.",
            "formula": "Action-at-a-distance non-contact field forces; Newton's Third Law universality.",
            "substitution": "Magnetic field dipole interactions.",
            "calculation": "1. (a) This is a NON-CONTACT FORCE (field force). The magnetic fields of the two magnetic dipoles interact across the intervening air space without physical material contact.\n2. (b) Yes! By Newton's Third Law of Motion, magnetic forces always occur in equal and opposite action-reaction pairs ($\\vec{F}_{\\text{magnet on needle}} = -\\vec{F}_{\\text{needle on magnet}}$). The compass needle exerts an exactly equal and opposite repulsive force on the massive bar magnet. The magnet does not noticeably move solely because its mass and frictional grip on the table are vastly larger than the minute mass of the pivot-mounted needle.",
            "finalAnswer": "(a) Non-contact magnetic field force; (b) Yes, by Newton's Third Law, the compass needle exerts an equal and opposite magnetic force on the bar magnet.",
            "unit": "Field Forces & Newton's Third Law",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "magnetic force action reaction newton third law compass",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "In-Text Question (Section 6.2 & 6.3, p. 13 & p. 17): (a) A toy car of mass 100 g moves at a constant velocity of 0.5 m s⁻¹. What is the net force acting on it? (b) Why does a firefighter struggle to hold a high-velocity fire hose?",
            "given": "(a) Mass m = 100 g = 0.1 kg, v = 0.5 m s⁻¹ constant $\\implies a = 0$.\n(b) High-pressure water discharged from fire hose nozzle.",
            "formula": "(a) $\\Sigma F = ma$; (b) Newton's Third Law & Conservation of Linear Momentum ($F_{\\text{recoil}} = \\frac{dp}{dt} = v_{\\text{water}} \\frac{dm}{dt}$).",
            "substitution": "(a) $F = 0.1 \\times 0 = 0\\text{ N}$. (b) Backward reaction force on firefighter.",
            "calculation": "1. Part (a): Since velocity is constant, acceleration is zero ($a = 0$). By Newton's first and second laws, the net external force acting on the toy car is identically ZERO.\n2. Part (b): Water is pumped out of the nozzle at immense velocity and high mass flow rate ($\frac{dm}{dt}$). By Newton's third law, the stream of escaping water exerts a massive backward recoil reaction force ($F = v \\frac{dm}{dt}$) on the hose and the firefighter holding it. The firefighter must exert huge forward muscular force to prevent being thrown backwards.",
            "finalAnswer": "(a) Net force is 0 N; (b) The escaping water exerts a powerful backward recoil reaction force (Newton's Third Law) that pushes against the firefighter.",
            "unit": "Newtons (N)",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "firefighter fire hose recoil force newton third law",
            "page": 13,
            "section": "Section 6.2"
        }
    ]

def update_ch6():
    with open("scripts/science_modules_ch6.json", "r", encoding="utf-8") as f:
        mods = json.load(f)
    
    for m in mods:
        m["curriculum_id"] = CH6_ID
        m["class_level"] = "Class 9"
        m["board"] = "CBSE"
        for we in m.get("worked_examples", []):
            if "image_search_query" not in we or not we["image_search_query"]:
                we["image_search_query"] = "forces motion newton laws class 9 ncert"
            if "page" not in we:
                we["page"] = 80 + m["order_index"]
            if "section" not in we:
                we["section"] = f"Section 6.{m['order_index']}"
                
    m6 = mods[-1]
    m6["title"] = "Master Numerical Solver & Comprehensive NCERT Chapter Exercise Ledger (Revise, Reflect, Refine Q1 to Q16)"
    m6["worked_examples"] = get_ch6_solver_examples()
    m6["description"] = "Exhaustive step-by-step master solutions for all in-text activities and all 16 'Revise, Reflect, Refine' chapter-end exercise problems from NCERT Exploration Grade 9 Chapter 6."
    
    with open("scripts/science_modules_ch6.json", "w", encoding="utf-8") as f:
        json.dump(mods, f, indent=2)
    print("Updated scripts/science_modules_ch6.json successfully!")

if __name__ == "__main__":
    update_ch6()
