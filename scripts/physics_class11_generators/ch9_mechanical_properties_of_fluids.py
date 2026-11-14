"""
ch9_mechanical_properties_of_fluids.py
CBSE Class 11 Physics - Chapter 9: Mechanical Properties of Fluids
Part 2 (Final-Term Examination Syllabus, Unit VII: Properties of Bulk Matter)
Exhaustive, University-Prep & Board-Exam Topper Curriculum Decomposition
"""

import sys
import os
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

import svg_builder_physics11_pt2 as sb2

CURRICULUM_ID = "c11_phy_ch09_fluids"
CLASS_LEVEL = "Class 11"
BOARD = "CBSE"
SUBJECT = "Physics"
UNIT = "Unit VII: Properties of Bulk Matter"
SYLLABUS_TERM = "Final-Term Examination"

def get_modules():
    modules = []

    # -------------------------------------------------------------
    # MODULE 1: Fluid Pressure, Pascal's Law & Hydraulic Machines
    # Order Index: 51
    # -------------------------------------------------------------
    mod1_svg = sb2.build_hydraulic_lift_pascal_svg(
        f1="F₁", a1="A₁", f2="F₂", a2="A₂",
        title="Pascal's Principle & Hydraulic Lift Mechanism",
        caption="Pressure transmitted undiminished throughout enclosed fluid: P₁ = P₂ => F₂ = F₁ × (A₂ / A₁)"
    )

    modules.append({
        "order_index": 51,
        "title": "Fluid Statics, Hydrostatic Pressure, Pascal's Law & Principle of Hydraulic Machines",
        "description": "Foundations of fluid statics: definition of fluid, isotropic nature of fluid pressure, variation of pressure with depth (P = P_a + ρgh), atmospheric pressure measurement with Torricelli barometer, gauge pressure vs absolute pressure, Pascal's law of equal transmission of pressure, and mechanical advantage in hydraulic lifts and hydraulic brakes.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Definition of Fluids: Liquids and gases capable of continuous flowing under shear stress",
            "Hydrostatic Pressure: Normal compressive force exerted per unit area by fluid at rest (P = dF_perp / dA, SI: Pa)",
            "Isotropic nature of static pressure: At any given point in a fluid at rest, pressure is equal in all directions",
            "Derivation of Pressure with Depth: Free-body equilibrium of an imaginary fluid cylinder (P₂ A - P₁ A - m g = 0 => P₂ - P₁ = ρ g h)",
            "Absolute Pressure vs Gauge Pressure: P = P_atm + ρ g h, Gauge Pressure P_gauge = P - P_atm = ρ g h",
            "Atmospheric Pressure Measurement: Evangelista Torricelli's mercury barometer (P_atm = ρ_Hg g h = 1.013 × 10⁵ Pa = 1 atm = 760 mm of Hg = 760 torr)",
            "Open-tube U-tube Manometer for measuring gas container pressure",
            "Blaise Pascal's Law (1652): Pressure applied to an enclosed in-compressible fluid is transmitted undiminished to every portion of the fluid and walls of containing vessel",
            "Hydraulic Lift Design: Two interconnected cylinders with cross-sectional areas A₁ and A₂ (P = F₁ / A₁ = F₂ / A₂ => F₂ = F₁ (A₂ / A₁))",
            "Hydraulic Brakes in automobiles: Master cylinder to slave cylinders transmission",
            "Hydrostatic Paradox: Liquid pressure depends purely on vertical height h and density ρ, completely independent of the shape, volume, or base area of the container"
        ],
        "key_concepts": [
            "Hydrostatic Pressure Equation P = P_a + ρgh",
            "Absolute Pressure vs Gauge Pressure Distinction",
            "Torricelli Mercury Barometer (1 atm = 1.013 × 10⁵ Pa)",
            "Pascal's Law & Mechanical Advantage F₂ = F₁ (A₂ / A₁)",
            "Hydrostatic Paradox (Pressure Depends Only on Height h)"
        ],
        "success_criteria": [
            "Derive the hydrostatic pressure formula P = P_a + ρgh using an imaginary vertical fluid cylinder",
            "Differentiate clearly between absolute pressure and gauge pressure with numerical conversions",
            "Calculate output lifting force and piston displacement in hydraulic lifts using Pascal's principle",
            "Explain the physical basis of the hydrostatic paradox"
        ],
        "chapter_notes": """# Fluid Statics: Hydrostatic Pressure & Pascal's Law
## 1. Hydrostatic Pressure & Depth Variation
Consider an imaginary cylindrical fluid element of cross-sectional area $A$ and height $h$ in a liquid of uniform density $\\rho$ at rest:
$$\\sum F_y = 0 \\implies P_2 A - P_1 A - m g = 0$$
Since mass $m = \\rho V = \\rho A h$:
$$P_2 A - P_1 A = \\rho A h g \\implies P_2 - P_1 = \\rho g h$$
If the top surface is exposed to the atmosphere at pressure $P_a$:
$$P = P_a + \\rho g h \\quad (\\text{Absolute Pressure})$$
The excess pressure over atmospheric pressure is the **Gauge Pressure**:
$$P_{\\text{gauge}} = P - P_a = \\rho g h$$

## 2. Atmospheric Pressure Measurement
Torricelli inverted a $1\\text{ m}$ mercury tube into a trough of mercury:
$$P_a = \\rho_{\\text{Hg}} g h = (13.6 \\times 10^3\\text{ kg/m}^3)(9.8\\text{ m/s}^2)(0.76\\text{ m}) = 1.013 \\times 10^5\\text{ Pa} = 1\\text{ atm}$$
- $1\\text{ torr} = 1\\text{ mm of Hg} \\approx 133.32\\text{ Pa}$
- $1\\text{ bar} = 10^5\\text{ Pa}$

## 3. Pascal's Law & Hydraulic Machines
Pressure applied to an enclosed in-compressible fluid is transmitted equally and undiminished in all directions:
$$P_1 = P_2 \\implies \\frac{F_1}{A_1} = \\frac{F_2}{A_2} \\implies F_2 = F_1 \\left(\\frac{A_2}{A_1}\\right)$$
If $A_2 \\gg A_1$, a small input force $F_1$ produces a giant output lifting force $F_2$.
By conservation of energy, the liquid volume moved is conserved:
$$V = A_1 x_1 = A_2 x_2 \\implies x_2 = x_1 \\left(\\frac{A_1}{A_2}\\right)$$
Work done at input equals work done at output: $W = F_1 x_1 = F_2 x_2$.
""",
        "worked_examples": [
            {
                "problem": "In a car lift, compressed air exerts a force on a small piston having a radius of 5.0 cm. This pressure is transmitted through liquid to a second piston of radius 15 cm. What is the force which the compressed air must exert to lift a car of mass 1350 kg? Take g = 9.8 m/s². (NCERT Example 9.2)",
                "given": "Input piston radius r₁ = 5.0 cm = 0.05 m, Output piston radius r₂ = 15 cm = 0.15 m, Car mass m = 1350 kg, Output force F₂ = m · g = 1350 × 9.8 = 13,230 N",
                "formula": "Pascal's Law: F₁ / A₁ = F₂ / A₂ => F₁ = F₂ · (A₁ / A₂) = F₂ · (π r₁² / π r₂²) = F₂ · (r₁ / r₂)²",
                "substitution": "F₁ = 13,230 N × (0.05 m / 0.15 m)² = 13,230 N × (1 / 3)² = 13,230 / 9",
                "calculation": "F₁ = 1470 N. The corresponding air pressure is P = F₁ / (π r₁²) = 1470 / (π × 0.0025) = 1.87 × 10⁵ Pa ≈ 1.9 atm",
                "finalAnswer": "Required input air force F₁ = 1470 N (Air pressure P = 1.87 × 10⁵ Pa)",
                "unit": "Newtons (N)"
            }
        ],
        "common_misconceptions": [
            "Misconception: A hydraulic lift creates free energy because a small force lifts a massive car. Reality: Work done is strictly conserved ($F_1 x_1 = F_2 x_2$). The output piston moves up by a tiny distance $x_2 = x_1 (A_1 / A_2)$ for a large stroke $x_1$ of the input piston."
        ],
        "concept_questions": [
            {
                "question": "Three vessels of different geometric shapes (one cylindrical, one conical, and one stepped) have identical flat base areas A. They are filled with water to the exact same vertical depth h. Which vessel experiences the greatest hydrostatic force on its base?",
                "options": [
                    "All three vessels experience the exact same hydrostatic force on their base",
                    "The cylindrical vessel because it holds the most water",
                    "The conical vessel because of inward sloping wall reactions",
                    "The stepped vessel because of atmospheric concentration"
                ],
                "correctAnswer": "All three vessels experience the exact same hydrostatic force on their base",
                "explanation": "Hydrostatic pressure at the base depends strictly on vertical depth h: P = P_a + ρgh. Since base area A and depth h are identical for all three vessels, the force on the bottom F = P · A is strictly identical, regardless of the total volume or shape of water contained (Hydrostatic Paradox).",
                "hint": "Recall the hydrostatic paradox: does base pressure depend on the container shape or only on vertical height h?",
                "blooms_level": "Understand"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "Pascal's Principle & Hydraulic Multiplication",
                "diagram_type": "image",
                "diagram_title": "Hydraulic Lift Force Multiplication Schematic",
                "why_needed": "Visual proof of pressure transmission and mechanical advantage",
                "timing_and_cue": "Stage 1 when introducing Pascal's principle",
                "what_to_explain": "How pressure is equal at both pistons and force scales with area ratio A2/A1",
                "image_search_query": "hydraulic lift pascal law principle diagram physics",
                
                "svg": mod1_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Hydraulic Lift",
                    "diagram_type": "image",
                    "image_search_query": "hydraulic lift pascal principle diagram",
                    "svg": mod1_svg
                }
            ]
        },
        "ai_system_prompt_context": "TEACHING MOMENTUM: Emphasize that pressure in fluid statics has no direction—it is a scalar pushing equally against any oriented surface. Lay out NCERT Example 9.2 clearly on the board."
    })

    # -------------------------------------------------------------
    # MODULE 2: Streamline Flow, Equation of Continuity & Reynolds Number
    # Order Index: 52
    # -------------------------------------------------------------
    mod2_svg = sb2.build_bernoulli_venturi_svg(
        title="Streamline Flow & Equation of Continuity",
        caption="A₁v₁ = A₂v₂ = Constant (Conservation of mass in steady in-compressible flow)"
    )

    modules.append({
        "order_index": 52,
        "title": "Streamline Flow, Tube of Flow, Equation of Continuity & Critical Reynolds Number",
        "description": "Transition to fluid dynamics: laminar vs turbulent flow, streamlines, pathlines, streaklines, tube of flow properties, rigorous mathematical derivation of the Equation of Continuity (A₁v₁ = A₂v₂ = const) from mass conservation in in-compressible flow, laminar velocity profiles, and Reynolds number criteria for turbulence.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Steady / Streamline / Laminar Flow: Velocity of fluid particles passing any fixed point remains constant in magnitude and direction over time",
            "Streamline definition: Curve whose tangent at any point gives the instantaneous direction of fluid velocity",
            "Invariance of streamlines: Two streamlines can never cross each other (would imply two distinct velocity directions at intersection)",
            "Tube of Flow: Bundle of streamlines forming a tubular boundary across which no fluid passes laterally",
            "Derivation of Equation of Continuity from Mass Conservation:",
            "Mass entering section 1 in time Δt: Δm₁ = ρ₁ A₁ v₁ Δt",
            "Mass leaving section 2 in time Δt: Δm₂ = ρ₂ A₂ v₂ Δt",
            "For steady flow: Δm₁ = Δm₂ => ρ₁ A₁ v₁ = ρ₂ A₂ v₂",
            "For in-compressible fluids (ρ₁ = ρ₂ = ρ): A₁ v₁ = A₂ v₂ = Constant (Volume flow rate Q = dV/dt)",
            "Physical consequence: Fluid speed is inversely proportional to cross-sectional area (v ∝ 1/A); fluid accelerates when passing through a narrowing",
            "Turbulent Flow: Irregular, chaotic, unsteady flow characterized by eddies, vortices, and rapid mixing occurring beyond critical velocity",
            "Reynolds Number (R_e): Dimensionless number governing flow regime: R_e = (ρ v d) / η (inertial force / viscous force)",
            "Regimes: R_e < 1000 => Steady laminar flow; 1000 < R_e < 2000 => Unsteady transition; R_e > 2000 => Fully turbulent flow"
        ],
        "key_concepts": [
            "Streamlines Never Cross (Unique Velocity Vector)",
            "Mass Conservation & Equation of Continuity A₁v₁ = A₂v₂",
            "Volume Flow Rate Q = A · v (m³/s)",
            "Reynolds Number R_e = (ρ v d) / η & Critical Turbulence Threshold"
        ],
        "success_criteria": [
            "Derive the equation of continuity A₁v₁ = A₂v₂ from conservation of mass",
            "Explain why water issuing from a tap narrows into a slender stream as it accelerates downwards",
            "Calculate fluid speed in arterial constrictions using continuity",
            "Predict laminar vs turbulent flow regime using Reynolds number R_e"
        ],
        "chapter_notes": """# Fluid Dynamics: Streamlines, Continuity & Reynolds Number
## 1. Streamline Flow & Properties
Flow is said to be **steady** or **streamline** if each particle passing a given point follows the exact same path with the exact same velocity as previous particles.
- **Properties of Streamlines**:
  1. The tangent to a streamline gives the direction of fluid velocity at that point.
  2. **Two streamlines can never intersect**. If they did, a particle at the junction would have two different velocities simultaneously, which is physically impossible.
  3. Streamlines crowd closer together in regions of higher speed ($v \\propto \\frac{1}{\\text{spacing}}$).

## 2. Derivation: Equation of Continuity
Consider steady flow of an in-compressible fluid through a pipe of varying cross-section:
- At inlet (area $A_1$, speed $v_1$): In time $\\Delta t$, fluid moves distance $\\Delta x_1 = v_1 \\Delta t$.
  $$\\text{Mass entered: } \\Delta m_1 = \\rho_1 A_1 v_1 \\Delta t$$
- At outlet (area $A_2$, speed $v_2$):
  $$\\text{Mass exited: } \\Delta m_2 = \\rho_2 A_2 v_2 \\Delta t$$
By **Conservation of Mass**, mass accumulated inside the pipe is zero:
$$\\Delta m_1 = \\Delta m_2 \\implies \\rho_1 A_1 v_1 = \\rho_2 A_2 v_2$$
For in-compressible liquids ($\\rho_1 = \\rho_2$):
$$A_1 v_1 = A_2 v_2 = \\text{Constant} \\quad (\\text{Equation of Continuity})$$
The product $A v = Q = \\frac{dV}{dt}$ is the **Volume Flow Rate** (SI: $\\text{m}^3/\\text{s}$).

### Everyday Phenomenon:
Why does the water stream from a tap taper as it falls?
As water falls under gravity, its speed increases ($v^2 = u^2 + 2gh$). By continuity ($A v = \\text{const}$), as $v$ increases, cross-sectional area $A$ must contract, forming a narrow neck!

## 3. Reynolds Number ($R_e$) & Turbulence
$$R_e = \\frac{\\text{Inertial Force}}{\\text{Viscous Force}} = \\frac{\\rho v d}{\\eta}$$
where $\\rho$ is fluid density, $v$ is average speed, $d$ is pipe diameter, and $\\eta$ is dynamic viscosity.
- $R_e < 1000$: **Laminar / Streamline Flow**
- $1000 \\le R_e \\le 2000$: **Unstable / Transition Flow**
- $R_e > 2000$: **Turbulent Flow**
""",
        "worked_examples": [
            {
                "problem": "A horizontal pipeline of diameter 20 cm carries water at a speed of 2.0 m/s. It connects to a smaller pipe of diameter 10 cm. Find the flow speed in the smaller pipe and the volume flow rate Q in liters per second.",
                "given": "Diameter d₁ = 20 cm = 0.20 m, Radius r₁ = 0.10 m, Speed v₁ = 2.0 m/s, Diameter d₂ = 10 cm = 0.10 m, Radius r₂ = 0.05 m",
                "formula": "A₁ v₁ = A₂ v₂ => v₂ = v₁ · (A₁ / A₂) = v₁ · (d₁ / d₂)²; Q = A₁ · v₁",
                "substitution": "v₂ = 2.0 m/s × (20 cm / 10 cm)² = 2.0 × 2² = 2.0 × 4; Q = π × (0.10)² × 2.0",
                "calculation": "v₂ = 8.0 m/s; Q = 3.1416 × 0.01 × 2.0 = 0.06283 m³/s = 62.83 L/s (since 1 m³ = 1000 L)",
                "finalAnswer": "Speed in smaller pipe v₂ = 8.0 m/s; Volume flow rate Q = 62.8 L/s",
                "unit": "m/s and L/s"
            }
        ],
        "common_misconceptions": [
            "Misconception: When water speeds up in a narrow pipe, the pressure must increase because the particles are crammed together. Reality: By Bernoulli's principle, when water speeds up into a constriction, internal static pressure actually DROPS! Static pressure is lower at the constriction."
        ],
        "concept_questions": [
            {
                "question": "A gardener holds a hosepipe of cross-sectional area A from which water flows out with speed v. She covers half the opening of the pipe with her thumb (new area A/2). What is the new speed of the water jet?",
                "options": [
                    "Speed doubles to 2v",
                    "Speed quadruples to 4v",
                    "Speed halves to v/2",
                    "Speed remains unchanged"
                ],
                "correctAnswer": "Speed doubles to 2v",
                "explanation": "From the equation of continuity A₁ v₁ = A₂ v₂, if the exit area is halved to A/2, the exit speed must double to 2v to conserve volume flow rate.",
                "hint": "Check the inverse proportionality between area and speed: v ∝ 1/A.",
                "blooms_level": "Understand"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "Equation of Continuity & Flow Convergence",
                "diagram_type": "image",
                "diagram_title": "Streamline Crowding & Velocity Acceleration in Constricted Pipe",
                "why_needed": "Visualizes mass conservation and tap water tapering",
                "timing_and_cue": "Stage 2 during continuity derivation",
                "what_to_explain": "Why streamline spacing decreases where fluid accelerates",
                "image_search_query": "equation of continuity streamline fluid pipe tapering diagram",
                "svg": mod2_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Continuity Equation",
                    "diagram_type": "image",
                    "image_search_query": "streamlines pipe constriction fluid dynamics diagram",
                    "svg": mod2_svg
                }
            ]
        },
        "ai_system_prompt_context": "SOCRATIC TIP: Introduce the tap water tapering hook in Stage 1: 'Have you ever noticed why the stream of water falling from your kitchen tap gets narrower and narrower as it approaches the sink?'"
    })

    # -------------------------------------------------------------
    # MODULE 3: Bernoulli's Principle, Venturi-meter & Dynamic Lift
    # Order Index: 53
    # -------------------------------------------------------------
    mod3_svg = sb2.build_bernoulli_venturi_svg(
        title="Bernoulli's Principle, Venturi-meter & Dynamic Lift",
        caption="P + ½ρv² + ρgh = Constant (Work-Energy theorem applied to streamline fluid flow)"
    )

    modules.append({
        "order_index": 53,
        "title": "Bernoulli's Principle, Energy Conservation in Fluids, Venturi-meter & Aerodynamic Lift",
        "description": "Rigorous work-energy theorem derivation of Daniel Bernoulli's equation for steady, streamline, non-viscous, in-compressible flow: P + 1/2 ρv² + ρgh = constant. Analysis of static pressure head, velocity head, and elevation head. Applications to the Venturi-meter flow gauge, atomizers/carburetors, dynamic aerodynamic lift on airplane wings, and the Magnus effect on spinning balls.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Assumptions of Bernoulli's Theorem: Streamline flow, in-compressible fluid (ρ = const), non-viscous / zero friction (η = 0), and irrotational",
            "Derivation from Work-Energy Theorem on a fluid element:",
            "Work done by pressure forces: W_p = (P₁ - P₂) ΔV",
            "Change in gravitational potential energy: ΔU = ρ ΔV g (h₂ - h₁)",
            "Change in kinetic energy: ΔK = 1/2 ρ ΔV (v₂² - v₁²)",
            "Equating Net Work to ΔK + ΔU: P₁ + 1/2 ρ v₁² + ρ g h₁ = P₂ + 1/2 ρ v₂² + ρ g h₂ = Constant",
            "Alternative head formulation: P / (ρ g) + v² / (2g) + h = Constant (Pressure head + Velocity head + Elevation head)",
            "Horizontal Flow: h₁ = h₂ => P + 1/2 ρ v² = Constant (High speed implies low static pressure)",
            "Venturi-meter: Instrument for measuring fluid discharge in pipelines using differential manometer",
            "Derivation of flow speed in Venturi-meter: v₁ = √[ 2(P₁ - P₂) / (ρ (A₁²/A₂² - 1)) ] = √[ 2 ρ_m g h / (ρ (A₁²/A₂² - 1)) ]",
            "Sprayer / Atomizer & Paint Guns: High-speed air jet over vertical suction tube drops pressure, lifting liquid into a fine mist",
            "Aerodynamic Lift on Aerofoil (Airplane Wing): Curved cambered upper surface forces streamlines closer, creating higher speed and lower pressure above wing than below (ΔP = P_bottom - P_top > 0, producing upward lift)",
            "Magnus Effect: Dynamic lift on spinning ball in air due to asymmetry in streamline speeds on top vs bottom surfaces"
        ],
        "key_concepts": [
            "Bernoulli's Equation P + ½ρv² + ρgh = Constant",
            "Trade-off Between Static Pressure and Kinetic Energy",
            "Venturi-meter Discharge Formula Q = A₁A₂ √[2ΔP / ρ(A₁² - A₂²)]",
            "Aerofoil Camber & Upward Aerodynamic Lift Force",
            "Magnus Effect on Spinning Cricket/Baseball Balls"
        ],
        "success_criteria": [
            "Derive Bernoulli's equation from the work-energy theorem with clear boundary pressure terms",
            "Explain why static pressure is lowest at the narrowest throat of a horizontal pipe",
            "Calculate volume flow rate Q using Venturi-meter manometer deflection height h",
            "Explain aerodynamic lift on aircraft wings and curved trajectory in Magnus effect with streamline diagrams"
        ],
        "chapter_notes": """# Bernoulli's Principle & Applications
## 1. Derivation of Bernoulli's Equation
Consider a fluid flowing through a non-uniform pipe from height $h_1$ to height $h_2$:
1. **Work done by pressure forces**:
   At inlet: $W_1 = P_1 A_1 \\Delta x_1 = P_1 \\Delta V$
   At outlet: $W_2 = - P_2 A_2 \\Delta x_2 = - P_2 \\Delta V$
   $$\\text{Net pressure work: } W_{\\text{net}} = (P_1 - P_2) \\Delta V$$
2. **Work done by gravity**:
   $$W_g = - \\Delta U = - m g (h_2 - h_1) = - \\rho \\Delta V g (h_2 - h_1)$$
3. **Change in Kinetic Energy**:
   $$\\Delta K = \\frac{1}{2} m (v_2^2 - v_1^2) = \\frac{1}{2} \\rho \\Delta V (v_2^2 - v_1^2)$$
By the **Work-Energy Theorem** ($W_{\\text{net}} + W_g = \\Delta K$):
$$(P_1 - P_2) \\Delta V - \\rho \\Delta V g (h_2 - h_1) = \\frac{1}{2} \\rho \\Delta V (v_2^2 - v_1^2)$$
Dividing by $\\Delta V$ and rearranging:
$$P_1 + \\frac{1}{2} \\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2} \\rho v_2^2 + \\rho g h_2$$
$$\\boxed{P + \\frac{1}{2}\\rho v^2 + \\rho g h = \\text{Constant}}$$

## 2. Venturi-meter (Flow Rate Measurement)
For a horizontal pipe ($h_1 = h_2$):
$$P_1 - P_2 = \\frac{1}{2} \\rho (v_2^2 - v_1^2)$$
From continuity: $v_2 = v_1 \\left(\\frac{A_1}{A_2}\\right)$:
$$P_1 - P_2 = \\frac{1}{2} \\rho v_1^2 \\left[ \\left(\\frac{A_1}{A_2}\\right)^2 - 1 \\right]$$
Using differential manometer height $h$ (fluid density $\\rho_m$): $P_1 - P_2 = \\rho_m g h$:
$$v_1 = \\sqrt{\\frac{2 \\rho_m g h}{\\rho \\left[ (A_1 / A_2)^2 - 1 \\right]}}$$
$$Q = A_1 v_1 = A_1 A_2 \\sqrt{\\frac{2 \\Delta P}{\\rho (A_1^2 - A_2^2)}}$$

## 3. Dynamic Lift & Magnus Effect
- **Aerofoil Wing**: Upper surface is cambered (curved) while lower surface is flatter. Air flows faster over top ($v_{\\text{top}} > v_{\\text{bottom}}$), creating lower pressure above ($P_{\\text{top}} < P_{\\text{bottom}}$). The resulting upward force is **Dynamic Lift**:
  $$F_{\\text{lift}} = (P_{\\text{bottom}} - P_{\\text{top}}) A$$
- **Magnus Effect**: When a cylinder or ball spins in a fluid stream, friction drags air faster on one side and slows it down on the opposite side, producing a lateral pressure imbalance that bends the trajectory.
""",
        "worked_examples": [
            {
                "problem": "A fully loaded Boeing aircraft has a mass of 3.3 × 10⁵ kg. Its total wing area is 500 m². It is in level flight with a speed of 960 km/h (267 m/s). (a) Estimate the pressure difference between the lower and upper surfaces of the wings. (b) Estimate the fractional increase in the speed of the air on the upper surface compared to the lower surface. The density of air is ρ = 1.2 kg/m³. Take g = 9.8 m/s². (NCERT Example 9.3)",
                "given": "Aircraft mass m = 3.3 × 10⁵ kg, Wing area A = 500 m², Flight speed v_avg = 960 km/h = 267 m/s, Air density ρ = 1.2 kg/m³",
                "formula": "Level flight: Upward lift = Weight of aircraft => ΔP · A = m · g => ΔP = (m · g) / A; Bernoulli: ΔP = 1/2 ρ (v₂² - v₁²) = ρ v_avg (v₂ - v₁) => (v₂ - v₁) / v_avg = ΔP / (ρ v_avg²)",
                "substitution": "ΔP = (3.3 × 10⁵ kg × 9.8 m/s²) / 500 m² = 3.234 × 10⁶ / 500 = 6468 N/m²; Fractional speed difference = 6468 / (1.2 × (267)²)",
                "calculation": "6468 / (1.2 × 71289) = 6468 / 85547 = 0.0756 ≈ 7.6% = 0.08",
                "finalAnswer": "Pressure difference ΔP = 6.5 × 10³ N/m²; Air on upper surface is ~8% faster than on lower surface",
                "unit": "N/m² and percentage"
            }
        ],
        "common_misconceptions": [
            "Misconception: Air molecules must take the exact same time to traverse the top and bottom of an aerofoil (equal transit time theory). Reality: The equal transit time theory is physically false. Air over the top surface travels significantly FASTER than required by equal transit time, as proven in wind tunnels."
        ],
        "concept_questions": [
            {
                "question": "Why does a tin roof or thatched roof blow OFF upwards during a high-speed hurricane or cyclone rather than collapsing downwards?",
                "options": [
                    "High-speed wind blowing across the top of the roof reduces pressure above it (P_top << P_atm), while still air inside the house remains at high atmospheric pressure, generating an enormous net upward lifting force",
                    "The wind pushes the roof upward from underneath the floorboards",
                    "Warm air inside the room pushes the roof",
                    "Gravitational force reverses during cyclones"
                ],
                "correctAnswer": "High-speed wind blowing across the top of the roof reduces pressure above it (P_top << P_atm), while still air inside the house remains at high atmospheric pressure, generating an enormous net upward lifting force",
                "explanation": "By Bernoulli's principle, wind speed over the roof is very large (P_out = P_atm - 1/2 ρ v²), while air inside the closed room is stagnant (P_in = P_atm). The huge upward pressure difference ΔP = 1/2 ρ v² lifts the roof off.",
                "hint": "Think about Bernoulli's trade-off: high speed air outside means what for outside static pressure?",
                "blooms_level": "Understand"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "Bernoulli's Theorem & Venturi Effect",
                "diagram_type": "image",
                "diagram_title": "Venturi Tube Manometer & Aerofoil Streamline Flow",
                "why_needed": "Visualizes static pressure dip at high-speed constriction and aerofoil lift",
                "timing_and_cue": "Stage 2 during Bernoulli formulation",
                "what_to_explain": "Why manometer height dips at the throat and streamlines compress above the aerofoil",
                "image_search_query": "venturi tube bernoulli equation aerofoil lift diagram physics",
                "svg": mod3_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Bernoulli Dynamics",
                    "diagram_type": "image",
                    "image_search_query": "aerofoil streamline dynamic lift pressure diagram",
                    "svg": mod3_svg
                }
            ]
        },
        "ai_system_prompt_context": "BOARD TOPPER TIP: Solve NCERT Example 9.3 (Boeing aircraft lift) line by line using the Trio Combo. Highlight the conversion from km/h to m/s in [ROUGH_WORK]."
    })

    # -------------------------------------------------------------
    # MODULE 4: Torricelli's Law of Efflux & Orifice Dynamics
    # Order Index: 54
    # -------------------------------------------------------------
    mod4_svg = sb2.build_bernoulli_venturi_svg(
        title="Torricelli's Law of Efflux & Water Jet Trajectory",
        caption="Speed of efflux v = √(2gh) (Identical to the speed of free fall from depth h)"
    )

    modules.append({
        "order_index": 54,
        "title": "Torricelli's Law of Efflux, Velocity of Exit, Range of Fluid Jets & Tank Emptying Time",
        "description": "Application of Bernoulli's principle to fluids discharging through a small orifice in a large container: Torricelli's Law of Efflux (v = √(2gh)), closed pressurized tanks vs open tanks, maximum horizontal range of fluid jets on the ground, vena contracta contraction, and differential calculus integration for total time required to drain a tank.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Evangelista Torricelli's experiment (1643) on liquid efflux through an orifice",
            "Derivation from Bernoulli's equation applied between top free surface (1) and orifice (2):",
            "P_top + 1/2 ρ v₁² + ρ g y₁ = P_atm + 1/2 ρ v₂² + ρ g y₂",
            "Continuity constraint: A₁ v₁ = A₂ v₂ => v₁ = (A₂ / A₁) v₂ << v₂ since tank area A₁ >> orifice area A₂ (v₁ ≈ 0)",
            "For open tank (P_top = P_atm): 1/2 ρ v₂² = ρ g (y₁ - y₂) = ρ g h => v₂ = √(2 g h)",
            "Physical interpretation: Speed of efflux is identical to the velocity acquired by a body falling freely from rest through height h",
            "Closed pressurized tank with gauge pressure P: v₂ = √[ 2(P - P_atm)/ρ + 2gh ]",
            "Vena Contracta: Cross-section of fluid jet contracts slightly beyond orifice due to converging streamlines",
            "Horizontal range of liquid jet: Jet exits horizontally at height y above ground from an orifice at depth h below top surface (H = h + y)",
            "Time of flight: t = √(2y / g); Range R = v₂ · t = √(2gh) · √(2y/g) = 2 √(h y)",
            "Maximum Range Condition: R is maximum when h = y = H/2 (orifice at midpoint of water column), giving R_max = H",
            "Equal range for complementary depths: Orifices at depths h and (H - h) produce identical horizontal landing points",
            "Time to completely empty a tank of cross-section A through orifice a: -A (dh/dt) = a √(2gh) => t_empty = (A/a) √(2H/g)"
        ],
        "key_concepts": [
            "Torricelli's Speed of Efflux v = √(2gh)",
            "Free Fall Equivalence Principle",
            "Horizontal Range Formula R = 2 √(h y)",
            "Maximum Range Condition h = y = H/2 => R_max = H",
            "Tank Emptying Integration t = (A/a) √(2H/g)"
        ],
        "success_criteria": [
            "Derive Torricelli's law of efflux from Bernoulli's equation stating all approximations",
            "Prove that the horizontal range of a fluid jet is R = 2 √(h y)",
            "Determine the orifice position required to achieve maximum horizontal water spray",
            "Calculate the speed of efflux from closed containers under high internal air pressure"
        ],
        "chapter_notes": """# Torricelli's Law of Efflux & Projectile Kinematics of Fluid Jets
## 1. Derivation of Torricelli's Law
Consider a large open tank containing liquid of density $\\rho$ to height $H$. An orifice of small area $A_2$ is located at depth $h$ below the liquid surface ($y_1 - y_2 = h$):
- Surface (1): Pressure $P_1 = P_a$, height $y_1$, speed $v_1$.
- Orifice (2): Pressure $P_2 = P_a$ (open to atmosphere), height $y_2$, speed $v_2$.

By the **Equation of Continuity**:
$$A_1 v_1 = A_2 v_2 \\implies v_1 = \\left(\\frac{A_2}{A_1}\\right) v_2$$
Since $A_1 \\gg A_2$, $\\frac{A_2}{A_1} \\approx 0 \\implies v_1 \\approx 0$.

Applying Bernoulli's Theorem:
$$P_a + \\frac{1}{2}\\rho v_1^2 + \\rho g y_1 = P_a + \\frac{1}{2}\\rho v_2^2 + \\rho g y_2$$
$$\\rho g (y_1 - y_2) = \\frac{1}{2}\\rho v_2^2 \\implies \\rho g h = \\frac{1}{2}\\rho v_2^2$$
$$\\boxed{v_2 = \\sqrt{2 g h}}$$
**Torricelli's Law**: The speed of efflux of a liquid through an orifice at depth $h$ is equal to the speed acquired by a body falling freely from rest through height $h$.

## 2. Horizontal Range of the Liquid Jet
The jet leaves horizontally ($u_x = \\sqrt{2gh}$, $u_y = 0$) from height $y = H - h$ above the ground.
1. **Time of flight** to hit the floor:
   $$y = \\frac{1}{2} g t^2 \\implies t = \\sqrt{\\frac{2y}{g}}$$
2. **Horizontal Range**:
   $$R = u_x \\cdot t = \\sqrt{2gh} \\cdot \\sqrt{\\frac{2y}{g}} = 2\\sqrt{h y} = 2\\sqrt{h(H - h)}$$

### Maximizing Horizontal Range:
To maximize $R$, maximize $f(h) = h(H - h) = H h - h^2$:
$$\\frac{df}{dh} = H - 2h = 0 \\implies h = \\frac{H}{2}$$
When the orifice is drilled exactly at the midpoint of the liquid column ($h = y = H/2$):
$$R_{\\text{max}} = 2\\sqrt{\\left(\\frac{H}{2}\\right)\\left(\\frac{H}{2}\\right)} = H$$
The maximum range equals the total liquid height $H$!
Furthermore, depths $h$ and $H - h$ have identical ranges: $R(h) = R(H - h)$.

## 3. Total Time to Drain a Tank
$$- A \\frac{dh}{dt} = a \\sqrt{2gh} \\implies dt = -\\frac{A}{a\\sqrt{2g}} h^{-1/2} dh$$
$$t_{\\text{empty}} = \\int_0^{t_{\\text{empty}}} dt = -\\frac{A}{a\\sqrt{2g}} \\int_H^0 h^{-1/2} dh = \\frac{A}{a} \\sqrt{\\frac{2H}{g}}$$
""",
        "worked_examples": [
            {
                "problem": "A cylindrical water tank of height 4.0 m is completely filled with water. A small circular hole of radius 2.0 mm is punctured at a depth of 1.0 m below the top surface. Find (a) the velocity of efflux of the water jet, (b) the horizontal distance from the base of the tank where the jet strikes the ground, and (c) the volume flow rate Q. Take g = 9.8 m/s².",
                "given": "Total height H = 4.0 m, Depth of orifice h = 1.0 m, Height above ground y = H - h = 3.0 m, Hole radius r = 2.0 mm = 2.0 × 10⁻³ m, g = 9.8 m/s²",
                "formula": "v = √(2 g h); Range R = 2 √(h · y); Orifice Area a = π r²; Flow rate Q = a · v",
                "substitution": "v = √(2 × 9.8 × 1.0) = √19.6; R = 2 × √(1.0 × 3.0) = 2 × √3; a = π × (2.0 × 10⁻³)² = 1.257 × 10⁻⁵ m²; Q = a · v",
                "calculation": "v = 4.427 m/s; R = 2 × 1.732 = 3.464 m; Q = 1.257 × 10⁻⁵ m² × 4.427 m/s = 5.565 × 10⁻⁵ m³/s = 0.0557 L/s",
                "finalAnswer": "Efflux speed v = 4.43 m/s, Range R = 3.46 m, Flow rate Q = 0.056 L/s",
                "unit": "m/s, meters, and L/s"
            }
        ],
        "common_misconceptions": [
            "Misconception: Drilling a hole near the bottom always gives the greatest range because the water comes out fastest. Reality: While water exits fastest near the bottom (v = √(2gh)), it has negligible fall time (t = √(2y/g) ≈ 0) to travel horizontally! The range is maximum at the middle height h = H/2."
        ],
        "concept_questions": [
            {
                "question": "A cylindrical tank filled with liquid to height H has two small holes: Hole A at depth H/4 and Hole B at depth 3H/4. Which hole's jet lands farther horizontally on the ground?",
                "options": [
                    "Both jets land at the exact same horizontal distance from the tank base",
                    "Hole A because it has greater fall time",
                    "Hole B because it has higher exit speed",
                    "Neither jet lands outside the tank base"
                ],
                "correctAnswer": "Both jets land at the exact same horizontal distance from the tank base",
                "explanation": "From the range formula R = 2 √(h · y), for Hole A: h = H/4, y = 3H/4 => R_A = 2 √((H/4)(3H/4)) = (√3 / 2) H. For Hole B: h = 3H/4, y = H/4 => R_B = 2 √((3H/4)(H/4)) = (√3 / 2) H. The ranges are mathematically identical for complementary depths!",
                "hint": "Check the symmetry in R = 2 √(h (H - h)).",
                "blooms_level": "Understand"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "Torricelli Efflux & Range Symmetry",
                "diagram_type": "image",
                "diagram_title": "Water Jets at Different Depths & Complementary Range Parabola",
                "why_needed": "Visualizes why midpoint jet achieves maximum range and complementary depths match",
                "timing_and_cue": "Stage 4 when analyzing jet trajectory",
                "what_to_explain": "Speed of efflux v = √(2gh), time of flight, and range curves R = 2√(hy)",
                "image_search_query": "torricelli law of efflux trajectory horizontal range water jets diagram",
                "svg": mod4_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Torricelli Efflux",
                    "diagram_type": "image",
                    "image_search_query": "torricelli efflux velocity water jet tank diagram",
                    "svg": mod4_svg
                }
            ]
        },
        "ai_system_prompt_context": "TEACHING TIP: Prompt the student to deduce why R_max occurs at h = H/2 using symmetry before presenting the derivative proof."
    })

    # -------------------------------------------------------------
    # MODULE 5: Viscosity, Stokes' Law & Terminal Velocity
    # Order Index: 55
    # -------------------------------------------------------------
    mod5_svg = sb2.build_bernoulli_venturi_svg(
        title="Viscous Drag, Stokes' Law & Terminal Velocity",
        caption="Viscous Drag F_v = 6πηrv | Terminal Velocity v_t = 2r²(ρ - σ)g / 9η (Forces balance: W = F_b + F_v)"
    )

    modules.append({
        "order_index": 55,
        "title": "Viscosity, Newton's Law of Viscous Force, Stokes' Law & Terminal Velocity Dynamics",
        "description": "Internal friction in fluids: Newton's formula for viscous force (F = -η A dv/dx), coefficient of dynamic viscosity η (Poise / Poiseuille), temperature dependence in liquids vs gases, Sir George Stokes' drag law on spherical bodies (F = 6πηrv), equilibrium of falling spherical bodies under gravity, buoyancy, and viscous drag, derivation of Terminal Velocity (v_t = 2r²(ρ - σ)g / 9η), and applications to raindrops and Millikan's oil drop experiment.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Concept of Viscosity: Internal friction between adjacent fluid layers moving with relative velocity",
            "Velocity Gradient: Change in fluid velocity per unit perpendicular distance (dv/dx, SI unit: s⁻¹)",
            "Sir Isaac Newton's Law of Viscosity: F = - η A (dv/dx) (negative sign indicates drag opposes relative motion)",
            "Coefficient of Dynamic Viscosity (η): Shear stress per unit velocity gradient (SI Unit: Pa·s or N·s/m² = Poiseuille (Pl); CGS: Poise, 1 Pa·s = 10 Poise)",
            "Temperature dependence: Viscosity of liquids decreases with temperature (intermolecular bonds break); viscosity of gases increases with temperature (molecular collisions increase)",
            "Sir George Stokes' Law (1851): Drag force on a rigid sphere of radius r moving with low velocity v through an infinite viscous medium: F_drag = 6 π η r v",
            "Dimensional derivation of Stokes' law using Buckingham π / dimensional analysis (F ∝ η^a r^b v^c => a=1, b=1, c=1)",
            "Forces acting on a falling spherical body of density ρ in fluid of density σ:",
            "1. Downward Weight: W = m g = 4/3 π r³ ρ g",
            "2. Upward Buoyant Force (Archimedes): F_b = 4/3 π r³ σ g",
            "3. Upward Viscous Drag: F_v = 6 π η r v",
            "Derivation of Terminal Velocity (v_t): At terminal speed, net acceleration a = 0 => W = F_b + F_v",
            "Equilibrium equation: 4/3 π r³ ρ g = 4/3 π r³ σ g + 6 π η r v_t",
            "Master Terminal Velocity Formula: v_t = [ 2 r² (ρ - σ) g ] / [ 9 η ]",
            "Dependence: v_t ∝ r² (larger raindrops fall significantly faster than tiny mist droplets); v_t ∝ 1/η",
            "Sign analysis: If ρ > σ, v_t > 0 (sinks downward); if ρ < σ, v_t < 0 (bubbles rise upward at terminal speed)"
        ],
        "key_concepts": [
            "Newton's Viscosity Law F = -η A (dv/dx)",
            "Stokes' Drag Law F = 6πηrv for Spheres",
            "Force Equilibrium at Terminal Velocity (W = F_b + F_v)",
            "Terminal Velocity Formula v_t = 2r²(ρ - σ)g / 9η (v_t ∝ r²)",
            "Why Clouds Float (Tiny Water Droplets Have Extremely Small v_t)"
        ],
        "success_criteria": [
            "State Newton's law of viscosity and define the coefficient of viscosity η with SI and CGS units",
            "Derive Stokes' law F = 6πηrv using dimensional analysis",
            "Derive the complete expression for terminal velocity v_t showing all three forces on FBD",
            "Explain why raindrops do not kill humans despite falling from clouds 3 km high"
        ],
        "chapter_notes": """# Viscosity, Stokes' Law & Terminal Velocity
## 1. Newton's Law of Viscosity
When a fluid flows over a solid surface, layers exhibit a velocity gradient $\\frac{dv}{dx}$. The viscous drag force $F$ between layers is:
$$F = - \\eta A \\frac{dv}{dx}$$
- $\\eta$ is the **Coefficient of Viscosity**.
- **SI Unit**: $\\text{Pa}\\cdot\\text{s} = \\text{N}\\cdot\\text{s}\\cdot\\text{m}^{-2} = \\text{kg}\\cdot\\text{m}^{-1}\\cdot\\text{s}^{-1}$ (also called Poiseuille, $\\text{Pl}$).
- **CGS Unit**: $\\text{Poise}$ ($1\\text{ Pa}\\cdot\\text{s} = 10\\text{ Poise}$).
- **Effect of Temperature**:
  - Liquids: $\\eta$ drops exponentially with temperature (e.g., motor oil thins when hot).
  - Gases: $\\eta \\propto \\sqrt{T}$, viscosity increases with temperature.

## 2. Stokes' Law (Viscous Drag on Spheres)
For a sphere of radius $r$ moving at low speed $v$ through an extensive fluid of viscosity $\\eta$:
$$F_{\\text{viscous}} = 6 \\pi \\eta r v$$

## 3. Derivation: Terminal Velocity ($v_t$)
Consider a sphere of density $\\rho$ and radius $r$ falling in a fluid of density $\\sigma$ and viscosity $\\eta$:
Three vertical forces act:
1. **Downward Gravity**: $W = V \\rho g = \\frac{4}{3}\\pi r^3 \\rho g$
2. **Upward Archimedes Buoyancy**: $F_b = V \\sigma g = \\frac{4}{3}\\pi r^3 \\sigma g$
3. **Upward Viscous Drag**: $F_v = 6\\pi \\eta r v$

As speed $v$ increases, viscous drag $F_v$ increases until net force becomes zero ($a = 0$). The constant steady speed achieved is the **Terminal Velocity** $v_t$:
$$W = F_b + F_v$$
$$\\frac{4}{3}\\pi r^3 \\rho g = \\frac{4}{3}\\pi r^3 \\sigma g + 6\\pi \\eta r v_t$$
$$6\\pi \\eta r v_t = \\frac{4}{3}\\pi r^3 (\\rho - \\sigma) g$$
$$\\boxed{v_t = \\frac{2 r^2 (\\rho - \\sigma) g}{9 \\eta}}$$

### Critical Physical Insights:
- $v_t \\propto r^2$: A raindrop of radius $1\\text{ mm}$ falls $100$ times faster than a cloud droplet of radius $0.1\\text{ mm}$. Tiny mist droplets ($r \\sim 10^{-5}\\text{ m}$) have $v_t \\sim 1\\text{ cm/s}$, appearing to float suspended in air as clouds!
- Terminal speed is inversely proportional to viscosity: $v_t \\propto 1/\\eta$.
""",
        "worked_examples": [
            {
                "problem": "A terminal velocity of a copper ball of radius 2.0 mm falling through a tank of oil at 20°C is 6.5 cm/s. Compute the viscosity of the oil at 20°C. Density of copper is 8.9 × 10³ kg/m³ and density of oil is 1.5 × 10³ kg/m³. Take g = 9.8 m/s². (NCERT Example 9.4)",
                "given": "Radius r = 2.0 mm = 2.0 × 10⁻³ m, Terminal speed v_t = 6.5 cm/s = 0.065 m/s, Density of copper ρ = 8.9 × 10³ kg/m³, Density of oil σ = 1.5 × 10³ kg/m³, g = 9.8 m/s²",
                "formula": "Terminal Velocity v_t = [ 2 r² (ρ - σ) g ] / [ 9 η ] => Viscosity η = [ 2 r² (ρ - σ) g ] / [ 9 v_t ]",
                "substitution": "η = [ 2 × (2.0 × 10⁻³)² × (8.9 × 10³ - 1.5 × 10³) × 9.8 ] / [ 9 × 0.065 ]",
                "calculation": "Numerator = 2 × (4.0 × 10⁻⁶) × (7.4 × 10³) × 9.8 = 8.0 × 10⁻⁶ × 72520 = 0.58016; Denominator = 9 × 0.065 = 0.585; η = 0.58016 / 0.585 = 0.9917 Pa·s ≈ 0.99 Pa·s",
                "finalAnswer": "Viscosity of the oil η = 0.99 Pa·s = 9.9 Poise",
                "unit": "Pa·s (Poiseuille)"
            }
        ],
        "common_misconceptions": [
            "Misconception: Raindrops accelerate continuously all the way down from the clouds and hit the earth at bullet speeds. Reality: Within the first few meters of fall, the viscous drag of air balances gravity minus buoyancy, and the raindrop reaches a modest terminal speed of only 5 to 9 m/s!"
        ],
        "concept_questions": [
            {
                "question": "Two spherical raindrops of radii r and 2r fall through still air under gravity. What is the ratio of their terminal velocities v₁ : v₂?",
                "options": [
                    "1 : 4 (The larger drop falls 4 times faster)",
                    "1 : 2",
                    "1 : 8",
                    "1 : 1 (Equal terminal velocities)"
                ],
                "correctAnswer": "1 : 4 (The larger drop falls 4 times faster)",
                "explanation": "Terminal velocity is directly proportional to the square of the radius: v_t ∝ r². Therefore, v₁ / v₂ = (r / 2r)² = 1 / 4. The larger raindrop falls 4 times faster.",
                "hint": "Recall the r-dependence in v_t = 2r²(ρ - σ)g / 9η.",
                "blooms_level": "Apply"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "Stokes' Drag & Terminal Velocity Equilibrium",
                "diagram_type": "image",
                "diagram_title": "Free Body Diagram of Falling Sphere & Velocity vs Time Curve",
                "why_needed": "Visualizes force balance W = Fb + Fv and asymptotic approach to vt",
                "timing_and_cue": "Stage 4 during terminal velocity derivation",
                "what_to_explain": "How buoyant force and viscous drag rise to cancel weight exactly",
                "image_search_query": "terminal velocity falling sphere stokes law forces diagram",
                "svg": mod5_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Terminal Velocity",
                    "diagram_type": "image",
                    "image_search_query": "terminal velocity raindrop stokes law diagram",
                    "svg": mod5_svg
                }
            ]
        },
        "ai_system_prompt_context": "SOCRATIC HOOK: Start with: 'A cloud can weigh over 500,000 kilograms of liquid water. Why doesn't it instantly crash down onto our heads like a gigantic waterfall?' Connect directly to terminal velocity r² dependence."
    })

    # -------------------------------------------------------------
    # MODULE 6: Surface Energy, Surface Tension & Capillary Action
    # Order Index: 56
    # -------------------------------------------------------------
    mod6_svg = sb2.build_surface_tension_capillary_svg(
        title="Surface Tension, Angle of Contact & Capillary Meniscus",
        caption="Capillary Rise: h = (2S cos θ) / (r ρ g) | Excess Pressure: Drop ΔP = 2S/R, Soap Bubble ΔP = 4S/R"
    )

    modules.append({
        "order_index": 56,
        "title": "Surface Energy, Surface Tension, Angle of Contact, Excess Pressure & Capillary Rise",
        "description": "Molecular physics of liquid surfaces: sphere of molecular influence, unbalanced cohesive forces on surface molecules, formal definition of surface tension (S = F/L) and surface energy (W = S · ΔA), angle of contact θ (wetting vs non-wetting liquids), derivation of excess pressure across curved interfaces (liquid drop ΔP = 2S/R, soap bubble ΔP = 4S/R), capillary rise derivation (h = 2S cos θ / rρg), and detergents/surfactants action.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Molecular Theory of Surface Tension: Cohesive forces (like molecules) vs adhesive forces (unlike molecules)",
            "Sphere of molecular influence (~10⁻⁹ m): Molecule inside bulk experiences zero net force; molecule at surface experiences net inward cohesive pull",
            "Surface Energy: Extra potential energy possessed by surface molecules due to work done against inward attraction in bringing them to the surface",
            "Surface Tension (S or T): Force per unit length acting perpendicular to an imaginary line drawn on the liquid surface (S = F / L, SI: N/m or J/m²)",
            "Work done in increasing surface area: W = S · ΔA (Work = Surface Tension × Increase in Area)",
            "Angle of Contact (θ): Angle between the tangent to liquid surface at the point of contact and solid surface inside the liquid",
            "Wetting liquids (e.g., pure water on clean glass): Adhesive force > Cohesive force => Concave meniscus, θ < 90° (acute), θ ≈ 0° for pure water",
            "Non-wetting liquids (e.g., mercury on glass): Cohesive force > Adhesive force => Convex meniscus, θ > 90° (obtuse, θ ≈ 138° for mercury)",
            "Curved Liquid Interfaces: Pressure on the concave side is always greater than pressure on the convex side (P_concave - P_convex = ΔP)",
            "Derivation of Excess Pressure inside Liquid Drop (1 surface): W = ΔP · 4π R² ΔR = S · ΔA = S (8π R ΔR) => ΔP = 2S / R",
            "Derivation of Excess Pressure inside Soap Bubble (2 surfaces: inner and outer): W = ΔP · 4π R² ΔR = S (16π R ΔR) => ΔP = 4S / R",
            "Derivation of Capillary Rise (Jurin's Law): Equilibrium of upward surface tension force around circumference and weight of liquid column",
            "Equilibrium: 2 π r S cos θ = m g = π r² h ρ g => h = (2 S cos θ) / (r ρ g)",
            "Capillary depression: For mercury (θ > 90°, cos θ < 0), liquid depresses downward (h < 0)",
            "Effect of detergents and temperature: Surfactants lower surface tension, reducing contact angle and facilitating penetration into fabric pores"
        ],
        "key_concepts": [
            "Molecular Inward Pull & Surface Energy W = S · ΔA",
            "Angle of Contact θ (Wetting θ < 90° vs Non-Wetting θ > 90°)",
            "Excess Pressure: Drop ΔP = 2S/R vs Soap Bubble ΔP = 4S/R",
            "Capillary Rise Formula h = (2S cos θ) / (r ρ g)",
            "Why Raindrops and Soap Bubbles are Naturally Spherical (Minimal Surface Area)"
        ],
        "success_criteria": [
            "Explain the microscopic origin of surface tension using cohesive molecular spheres of influence",
            "Derive the excess pressure formulas for a liquid drop (2S/R) and a soap bubble (4S/R) using virtual work",
            "Derive the capillary ascent formula h = 2S cos θ / (r ρ g) from vertical force equilibrium",
            "Explain how detergents reduce surface tension to clean grease from clothing fibers"
        ],
        "chapter_notes": """# Surface Tension, Excess Pressure & Capillary Rise
## 1. Molecular Origin & Surface Energy
A molecule in the interior of a liquid is attracted equally in all directions by surrounding molecules (net force $= 0$). A molecule at the surface has neighbors only below it, experiencing a **net inward cohesive force**.
To bring a molecule from the interior to the surface requires positive work against this inward pull, stored as **Surface Energy**.
$$\\text{Surface Tension } S = \\frac{F}{L} = \\frac{W}{\\Delta A} \\quad (\\text{SI Unit: } \\text{N/m} \\text{ or } \\text{J/m}^2)$$

## 2. Angle of Contact ($\\theta$)
The angle between the tangent to the liquid surface at the point of contact and the solid surface inside the liquid:
- **Acute Angle ($\\theta < 90^\\circ$)**: Adhesive forces dominate. Liquid wets solid, meniscus is **concave**, capillary **rises** (e.g., Water on Glass, $\\theta \\approx 0^\\circ$).
- **Obtuse Angle ($\\theta > 90^\\circ$)**: Cohesive forces dominate. Liquid does not wet solid, meniscus is **convex**, capillary **depresses** (e.g., Mercury on Glass, $\\theta \\approx 138^\\circ$).

## 3. Derivation: Excess Pressure Inside Curved Interfaces
Pressure on the concave side is always higher than on the convex side.
1. **Liquid Drop (1 surface)**:
   Work done in expanding drop radius from $R$ to $R + \\Delta R$:
   $$W = (\\Delta P) \\cdot (4\\pi R^2 \\Delta R)$$
   Increase in surface area: $\\Delta A = 4\\pi (R + \\Delta R)^2 - 4\\pi R^2 \\approx 8\\pi R \\Delta R$.
   $$W = S \\cdot \\Delta A = S (8\\pi R \\Delta R)$$
   $$(\\Delta P)(4\\pi R^2 \\Delta R) = S (8\\pi R \\Delta R) \\implies \\boxed{\\Delta P_{\\text{drop}} = \\frac{2S}{R}}$$

2. **Soap Bubble in Air (2 surfaces: inner and outer)**:
   Since there are two liquid-air interfaces, $\\Delta A = 2 \\times (8\\pi R \\Delta R) = 16\\pi R \\Delta R$:
   $$\\boxed{\\Delta P_{\\text{bubble}} = \\frac{4S}{R}}$$

## 4. Derivation: Capillary Rise (Jurin's Law)
In a narrow glass tube of radius $r$, the liquid forms a concave meniscus with angle of contact $\\theta$.
The upward vertical component of surface tension force around the circular perimeter ($2\\pi r$) supports the weight of the cylindrical liquid column of height $h$:
$$F_{\\text{upward}} = (S \\cos \\theta) \\cdot (2\\pi r)$$
$$W_{\\text{column}} = m g = (\\pi r^2 h \\rho) g$$
Equating forces:
$$2\\pi r S \\cos \\theta = \\pi r^2 h \\rho g$$
$$\\boxed{h = \\frac{2 S \\cos \\theta}{r \\rho g}}$$
- Since $h \\propto 1/r$, the narrower the capillary bore, the higher the liquid climbs.
- For mercury ($\\theta \\approx 138^\\circ$, $\\cos \\theta < 0$), $h < 0$, giving a capillary **depression**.
""",
        "worked_examples": [
            {
                "problem": "What is the excess pressure inside a bubble of soap solution of radius 5.00 mm, given that the surface tension of soap solution at 20°C is 2.50 × 10⁻² N/m? If an air bubble of the same dimension were formed at a depth of 40.0 cm in a container containing a soap solution of relative density 1.20, what would be the total absolute pressure inside the bubble? Take g = 9.8 m/s² and P_atm = 1.01 × 10⁵ Pa. (NCERT Example 9.6)",
                "given": "Bubble radius R = 5.00 mm = 5.0 × 10⁻³ m, Soap surface tension S = 2.50 × 10⁻² N/m, Depth h = 40.0 cm = 0.40 m, Density of solution ρ = 1.20 × 1000 = 1200 kg/m³, P_atm = 1.01 × 10⁵ Pa",
                "formula": "(a) Soap bubble in air (2 surfaces): ΔP = 4S / R; (b) Air bubble inside liquid (1 surface): ΔP_air = 2S / R; P_liquid = P_atm + ρ g h; P_inside = P_liquid + ΔP_air",
                "substitution": "ΔP = (4 × 2.50 × 10⁻² N/m) / (5.0 × 10⁻³ m); ΔP_air = (2 × 2.50 × 10⁻²) / (5.0 × 10⁻³); P_liquid = 1.01 × 10⁵ + (1200 × 9.8 × 0.40)",
                "calculation": "ΔP = 1.0 × 10⁻¹ / 5.0 × 10⁻³ = 20 Pa; ΔP_air = 10 Pa; P_liquid = 1.01 × 10⁵ + 4704 = 101,000 + 4704 = 105,704 Pa; P_inside = 105,704 + 10 = 105,714 Pa = 1.06 × 10⁵ Pa",
                "finalAnswer": "Excess pressure in soap bubble = 20 Pa; Absolute pressure in air bubble at 40 cm depth = 1.06 × 10⁵ Pa",
                "unit": "Pascals (Pa)"
            }
        ],
        "common_misconceptions": [
            "Misconception: An air bubble submerged inside water has two surfaces like a soap bubble. Reality: An air bubble inside water has only ONE interface (liquid-gas boundary). A soap bubble in air has TWO interfaces (inner air-film boundary and outer film-air boundary). Hence ΔP = 4S/R for soap bubbles in air, but ΔP = 2S/R for air bubbles inside liquid!"
        ],
        "concept_questions": [
            {
                "question": "Two soap bubbles of unequal radii r₁ and r₂ (with r₁ > r₂) are connected by a narrow hollow tube with an open tap. What happens to the two bubbles?",
                "options": [
                    "Air flows from the smaller bubble into the larger bubble; the smaller bubble shrinks and the larger bubble expands",
                    "Air flows from the larger bubble into the smaller bubble until both have equal radii",
                    "No air flows because both bubbles are made of the same soap solution",
                    "Both bubbles pop simultaneously"
                ],
                "correctAnswer": "Air flows from the smaller bubble into the larger bubble; the smaller bubble shrinks and the larger bubble expands",
                "explanation": "Excess pressure inside a bubble is inversely proportional to its radius: ΔP = 4S/r. Therefore, the smaller bubble (r₂) has HIGHER internal pressure than the larger bubble (r₁). Air flows naturally from high pressure to low pressure (from smaller to larger bubble), causing the small bubble to collapse into the large one!",
                "hint": "Calculate which bubble has higher internal pressure using ΔP = 4S/r.",
                "blooms_level": "Understand"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "Surface Tension, Bubble Pressure & Capillary Rise",
                "diagram_type": "image",
                "diagram_title": "Capillary Ascent Meniscus & Soap Bubble Interface Anatomy",
                "why_needed": "Visualizes why 2 interfaces double excess pressure and why acute contact angle lifts water",
                "timing_and_cue": "Stage 2 during capillary derivation",
                "what_to_explain": "Circumferential tension forces pulling liquid column upward against gravity",
                "image_search_query": "capillary rise meniscus contact angle surface tension jurin law diagram",
                "svg": mod6_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Capillary Action & Surface Tension",
                    "diagram_type": "image",
                    "image_search_query": "capillary tube water mercury meniscus diagram",
                    "svg": mod6_svg
                }
            ]
        },
        "ai_system_prompt_context": "SOCRATIC EXAM HOOK: The two connected bubbles puzzle (small bubble blowing into big bubble) is an iconic CBSE board exam question! Challenge the student's intuition gently and prove it via ΔP = 4S/r."
    })

    # -------------------------------------------------------------
    # MODULE 7: Comprehensive NCERT Textbook Exercises 9.1 to 9.25 Solver
    # Order Index: 57
    # -------------------------------------------------------------
    mod7_svg = sb2.build_bernoulli_venturi_svg(
        title="NCERT Chapter 9 Exercises 9.1 to 9.25 Full Solutions Suite",
        caption="Step-by-step solutions for Fluid Pressure, Bernoulli, Viscosity, and Capillary Action"
    )

    modules.append({
        "order_index": 57,
        "title": "Comprehensive NCERT Textbook Exercises 9.1 to 9.25 Detailed Numerical Solutions Suite",
        "description": "Exhaustive step-by-step solutions to all end-of-chapter NCERT exercise questions (9.1 to 9.25) on Mechanical Properties of Fluids, covering heel pressure on floors, U-tube manometers with immiscible liquids (oil and water), hydraulic car lifts, blood flow speed through aorta, Torricelli tanks, terminal velocity of raindrops in air, and capillary rise in narrow bores.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 60,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "NCERT Exercise 9.1: Pressure exerted by a 50 kg woman wearing high-heeled shoes on a flat floor",
            "NCERT Exercise 9.2: Torricelli mercury barometer filled with French wine (density 984 kg/m³)",
            "NCERT Exercise 9.3: Vertical glass window of a submarine at deep ocean trench",
            "NCERT Exercise 9.4: Car lift operated by compressed air on input piston",
            "NCERT Exercise 9.5: U-tube manometer with water and methylated spirit separated by mercury",
            "NCERT Exercise 9.6: In the previous problem, if 15 cm of water and spirit are added, find the mercury level difference",
            "NCERT Exercise 9.7: Can Bernoulli's equation be used to describe the flow of blood in a rapid artery?",
            "NCERT Exercise 9.8: A plane in a wind tunnel has air speed of 70 m/s on lower surface and 63 m/s on upper surface",
            "NCERT Exercise 9.9: Venturi-meter tube with water discharge calculation",
            "NCERT Exercise 9.10: Rate of flow through a horizontal pipe connected to an open water tank",
            "NCERT Exercises 9.11 to 9.25: Terminal speed of rain drops, soap bubbles, capillary tubes, and detergent action"
        ],
        "key_concepts": [
            "U-Tube Manometer Immiscible Liquid Equilibrium (P_left = P_right at common level)",
            "High-Heel Puncture Pressure vs Elephant Foot Pressure",
            "Bernoulli Head Losses & Real Fluid Limitations",
            "Systematic Board Exam Layout: Given -> Formula -> Substitution -> Calculation -> Boxed Answer"
        ],
        "success_criteria": [
            "Solve multi-fluid U-tube manometer equilibrium problems using reference level isobaric lines",
            "Calculate pressure exerted by stiletto heels compared to flat elephant feet",
            "Solve Bernoulli equation problems accounting for pressure difference across aerofoils",
            "Master every authentic numerical pattern appearing in CBSE Class 11 final-term physics examination"
        ],
        "chapter_notes": """# NCERT Chapter 9: Complete Exercise Solutions Master Notes
## Summary of Master Equations:
1. **Hydrostatic Pressure**: $P = P_a + \\rho g h$
2. **Pascal's Principle**: $\\frac{F_1}{A_1} = \\frac{F_2}{A_2}$
3. **Equation of Continuity**: $A_1 v_1 = A_2 v_2$
4. **Bernoulli's Theorem**: $P + \\frac{1}{2}\\rho v^2 + \\rho g h = \\text{const}$
5. **Torricelli's Efflux**: $v = \\sqrt{2gh}$, Range $R = 2\\sqrt{hy}$
6. **Viscous Force**: $F = -\\eta A \\frac{dv}{dx}$
7. **Stokes' Law**: $F = 6\\pi \\eta r v$
8. **Terminal Velocity**: $v_t = \\frac{2 r^2 (\\rho - \\sigma) g}{9 \\eta}$
9. **Surface Energy**: $W = S \\cdot \\Delta A$
10. **Excess Pressure**: Drop $\\Delta P = \\frac{2S}{R}$, Soap bubble $\\Delta P = \\frac{4S}{R}$
11. **Capillary Ascent**: $h = \\frac{2 S \\cos \\theta}{r \\rho g}$
""",
        "worked_examples": [
            {
                "problem": "A 50 kg girl wearing high heel shoes balances on a single heel. The heel is circular with a diameter of 1.0 cm. What is the pressure exerted by the heel on the horizontal floor? (NCERT Exercise 9.1)",
                "given": "Girl mass m = 50 kg, Weight W = m · g = 50 × 9.8 = 490 N, Heel diameter d = 1.0 cm = 0.01 m, Radius r = 0.5 cm = 0.005 m",
                "formula": "Area A = π r²; Pressure P = W / A",
                "substitution": "A = π × (0.005 m)² = 3.1416 × 2.5 × 10⁻⁵ m² = 7.854 × 10⁻⁵ m²; P = 490 N / (7.854 × 10⁻⁵ m²)",
                "calculation": "P = 490 / 7.854 × 10⁻⁵ = 6.239 × 10⁶ N/m² = 6.24 × 10⁶ Pa ≈ 62 atmospheres!",
                "finalAnswer": "Pressure exerted by the heel = 6.24 × 10⁶ Pa (approx. 62 atm)",
                "unit": "Pascals (Pa)"
            },
            {
                "problem": "Torricelli's barometer used mercury. Pascal duplicated it using French wine of density 984 kg/m³. Determine the height of the wine column for normal atmospheric pressure (1.013 × 10⁵ Pa). (NCERT Exercise 9.2)",
                "given": "Atmospheric pressure P_a = 1.013 × 10⁵ Pa, Density of wine ρ = 984 kg/m³, g = 9.8 m/s²",
                "formula": "P_a = ρ · g · h => Height of column h = P_a / (ρ · g)",
                "substitution": "h = (1.013 × 10⁵ N/m²) / (984 kg/m³ × 9.8 m/s²)",
                "calculation": "Denominator = 984 × 9.8 = 9643.2; h = 101,300 / 9643.2 = 10.505 m",
                "finalAnswer": "Height of the wine barometer column = 10.5 m (approx. 34.5 feet tall!)",
                "unit": "meters"
            }
        ],
        "common_misconceptions": [
            "Misconception: A barometer column's height is always 76 cm regardless of liquid. Reality: 76 cm is strictly for dense mercury (ρ = 13,600 kg/m³). For water or wine (ρ ≈ 1000 kg/m³), the required barometer tube must be over 10.5 meters (3 stories tall)!"
        ],
        "concept_questions": [
            {
                "question": "Why is mercury used as the standard liquid in barometers instead of water?",
                "options": [
                    "Mercury's high density (13.6 times water) keeps the tube height manageable at 76 cm, and its vapor pressure at room temperature is negligible",
                    "Mercury is lighter than water",
                    "Mercury boils at 0°C",
                    "Water cannot exert hydrostatic pressure"
                ],
                "correctAnswer": "Mercury's high density (13.6 times water) keeps the tube height manageable at 76 cm, and its vapor pressure at room temperature is negligible",
                "explanation": "Because mercury is 13.6 times denser than water, atmospheric pressure balances 0.76 m of mercury versus 10.3 m of water. Furthermore, mercury does not stick to glass (cohesion > adhesion) and has virtually zero vapor pressure above the meniscus.",
                "hint": "Think about how tall a water barometer tube would have to be compared to mercury.",
                "blooms_level": "Understand"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "NCERT 9 Exercise Problem Solving Suite",
                "diagram_type": "image",
                "diagram_title": "High Heel Pressure vs Torricelli Barometer Schematics",
                "why_needed": "Visualizes end-of-chapter numerical problem setups on chalkboard",
                "timing_and_cue": "Stage 4 when solving Exercises 9.1, 9.2, and 9.4",
                "what_to_explain": "Free body diagrams, reference level pressure balances, and unit conversions",
                "image_search_query": "torricelli wine barometer mercury comparison diagram physics",
                "svg": mod7_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "NCERT 9 Exercises",
                    "diagram_type": "image",
                    "image_search_query": "hydraulic car lift problem diagram physics ncert",
                    "svg": mod7_svg
                }
            ]
        },
        "ai_system_prompt_context": "CHALKBOARD MANDATE: Strictly follow the Trio Combo for all NCERT Chapter 9 exercise numericals. Highlight the huge pressure of high heels (62 atm) to amaze the student!"
    })

    return {
        "curriculum_id": CURRICULUM_ID,
        "title": "Chapter 9: Mechanical Properties of Fluids",
        "description": "Comprehensive CBSE Class 11 Physics Part 2 curriculum covering Fluid Pressure, Pascal's Law, Hydraulic Lift, Streamline Flow, Equation of Continuity, Bernoulli's Principle, Torricelli's Law of Efflux, Viscosity, Stokes' Law, Terminal Velocity, Surface Tension, and Capillary Rise.",
        "category": "Physics",
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "difficulty_level": "advanced",
        "order_index": 9,
        "syllabus_term": SYLLABUS_TERM,
        "unit_name": UNIT,
        "weightage_marks": "Part of Unit VII-IX Group (20 Marks)",
        "notes_source_filename": "keph202.pdf",
        "modules": modules
    }
