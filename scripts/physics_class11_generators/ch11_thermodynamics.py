"""
Class 11 Physics - Chapter 11: Thermodynamics (Unit VIII)
Syllabus: Final-Term Examination
Module Range: Modules 65 to 70 (6 modules)
Fully aligned with NCERT Physics Part 2 (keph204.pdf) and CBSE 2026-27 Syllabus.
"""

try:
    from .svg_builder_physics11_pt2 import (
        build_thermodynamics_carnot_cycle_svg,
        get_svg_wrapper
    )
except ImportError:
    from svg_builder_physics11_pt2 import (
        build_thermodynamics_carnot_cycle_svg,
        get_svg_wrapper
    )

def get_ch11_curriculum():
    return {
        "chapter_number": 11,
        "title": "Chapter 11: Thermodynamics",
        "description": "Comprehensive study of macroscopic thermal systems, the Zeroth Law, First Law (internal energy, heat, work), specific heat capacities, isothermal, adiabatic, isobaric, and isochoric processes, the Second Law of Thermodynamics, and the Carnot cycle.",
        "term": "Final-Term Examination",
        "unit": "Unit VIII: Thermodynamics",
        "class_level": "Class 11",
        "subject": "Physics",
        "total_modules": 6,
        "start_module": 65,
        "end_module": 70
    }

def get_ch11_modules():
    carnot_svg = build_thermodynamics_carnot_cycle_svg()

    return [
        # Module 65
        {
            "order_index": 65,
            "chapter_number": 11,
            "title": "Thermal Equilibrium, Zeroth Law of Thermodynamics, Heat, Work & Internal Energy (First Law)",
            "term": "Final-Term Examination",
            "unit": "Unit VIII: Thermodynamics",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 11: Thermodynamics
## Module 65: Thermal Equilibrium, Zeroth Law of Thermodynamics, Heat, Work & Internal Energy (First Law)

### 1. Real-Life Physical Intuition & The Concept of Thermal Equilibrium
When you pour boiling hot tea into a ceramic cup and leave it on your study table, heat spontaneously flows from the hot liquid to the cooler ceramic cup and the surrounding room. Eventually, the temperature of the tea becomes identical to that of the room. At this point, macroscopic heat transfer ceases; the tea and the room are in **thermal equilibrium**.

Thermodynamics is the macroscopic science of energy transformation between heat and work. Unlike mechanics, which tracks individual particle velocities and forces, thermodynamics characterizes the macroscopic state of a bulk system using macroscopic state variables:
- Pressure ($P$ in $\\text{N/m}^2$ or $\\text{Pa}$)
- Volume ($V$ in $\\text{m}^3$)
- Temperature ($T$ in $\\text{K}$)
- Amount of substance ($n$ in moles or mass $m$ in $\\text{kg}$)

### 2. Zeroth Law of Thermodynamics: The Basis of Thermometry
Consider three thermodynamic systems $A$, $B$, and $C$.
- If system $A$ is in thermal equilibrium with system $C$, then $T_A = T_C$.
- If system $B$ is also in thermal equilibrium with system $C$, then $T_B = T_C$.
- **The Zeroth Law of Thermodynamics States**: *Two systems in thermal equilibrium with a third system separately are in thermal equilibrium with each other.*
Therefore:
$$T_A = T_B$$
This fundamental law justifies the concept of temperature as a measurable physical property that determines whether two systems are in thermal equilibrium. A thermometer is simply system $C$!

### 3. Thermodynamic State Variables & State Functions
A **state variable** depends solely on the current equilibrium state of the system, not on the path or history taken to reach that state.
- **Extensive Variables**: Depend on the size or mass of the system (e.g., Volume $V$, Mass $M$, Internal Energy $U$, Entropy $S$).
- **Intensive Variables**: Independent of system size (e.g., Pressure $P$, Temperature $T$, Density $\\rho$).

### 4. Internal Energy ($U$)
The **Internal Energy** ($U$) of a thermodynamic system is the sum of all microscopic kinetic energies and potential energies of its constituent molecules:
$$U = E_k(\\text{microscopic}) + E_p(\\text{microscopic})$$
For an **ideal gas**, intermolecular forces are zero, meaning microscopic potential energy vanishes ($E_p = 0$). Hence, for an ideal gas:
$$U = U(T)$$
The internal energy of an ideal gas depends solely on its absolute temperature $T$. For a monoatomic ideal gas with $n$ moles:
$$U = \\frac{3}{2} n R T$$

### 5. Heat ($Q$) and Work ($W$)
- **Heat ($Q$)**: Energy transferred across a system boundary solely due to a temperature difference.
  * $Q > 0$: Heat added/absorbed by the system.
  * $Q < 0$: Heat released/rejected by the system.
- **Thermodynamic Work ($W$)**: Energy transferred across system boundaries via macroscopic forces moving through a distance.
  * If a gas expands against an external pressure $P$ by volume change $dV$:
    $$dW = P \\, dV$$
    $$W = \\int_{V_1}^{V_2} P \\, dV$$
  * By standard NCERT/Physics convention:
    * $W > 0$: Work done **by** the system (expansion, $dV > 0$).
    * $W < 0$: Work done **on** the system (compression, $dV < 0$).

### 6. The First Law of Thermodynamics
The First Law of Thermodynamics is the universal law of conservation of energy applied to thermodynamic systems:
$$\\Delta Q = \\Delta U + \\Delta W$$
In differential form:
$$dQ = dU + dW = dU + P \\, dV$$
Rearranging for the change in internal energy:
$$\\Delta U = Q - W$$
> **Fundamental Theorem**: While heat $Q$ and work $W$ are path-dependent quantities (path functions), the difference $\\Delta U = Q - W$ is strictly a state function, independent of the path connecting the initial and final states!

### 7. Worked Example 11.1 (Textbook Derivation)
**Problem**: A gas enclosed in a cylinder is supplied with $110 \\text{ J}$ of heat. The gas expands and performs $40 \\text{ J}$ of external work against the piston. Determine the change in internal energy of the gas.
- **Given**: Heat supplied $\\Delta Q = +110 \\text{ J}$, Work done by gas $\\Delta W = +40 \\text{ J}$.
- **Formula**: $\\Delta U = \\Delta Q - \\Delta W$
- **Calculation**: $\\Delta U = 110 - 40 = 70 \\text{ J}$.
- **Physical Interpretation**: $70 \\text{ J}$ of the absorbed heat went into raising the random kinetic energy of the gas molecules (raising its temperature), while the remaining $40 \\text{ J}$ was converted into mechanical work.""",
            "svg_code": carnot_svg,
            
            
            "concept_questions": [
                {
                    "question": "Can the temperature of a gas increase without adding any heat to it?",
                    "options": [
                        "(Recommended) Yes, if external work is done on the gas during adiabatic compression (ΔW < 0, so ΔU = -ΔW > 0)",
                        "No, temperature change strictly requires heat flow across the boundary",
                        "Yes, but only if the gas is an ideal gas at absolute zero",
                        "No, the First Law of Thermodynamics forbids temperature changes without heat"
                    ],
                    "correct_answer": "(Recommended) Yes, if external work is done on the gas during adiabatic compression (ΔW < 0, so ΔU = -ΔW > 0)",
                    "explanation": "According to the First Law, ΔU = Q - W. If no heat is transferred (Q = 0, adiabatic), compressing the gas (W < 0) yields ΔU = -W > 0, which directly increases the internal energy and temperature."
                },
                {
                    "question": "Why is internal energy (U) a state function while heat (Q) and work (W) are path functions?",
                    "options": [
                        "(Recommended) Because U depends only on the thermodynamic state variables (P, V, T), whereas Q and W depend on the specific path taken on the P-V diagram",
                        "Because U can be measured with a thermometer, whereas Q and W cannot be measured",
                        "Because U is always conserved in every process, whereas Q and W are not conserved",
                        "Because U is an intensive property while Q and W are extensive properties"
                    ],
                    "correct_answer": "(Recommended) Because U depends only on the thermodynamic state variables (P, V, T), whereas Q and W depend on the specific path taken on the P-V diagram",
                    "explanation": "Internal energy is a unique property of the thermodynamic state of the gas. The area under the curve on a P-V indicator diagram represents work W, which visibly varies depending on the trajectory connecting the initial and final states."
                }
            ]
        },

        # Module 66
        {
            "order_index": 66,
            "chapter_number": 11,
            "title": "Specific Heat Capacities of Gases, Mayer's Relation (Cp - Cv = R) & State Variables",
            "term": "Final-Term Examination",
            "unit": "Unit VIII: Thermodynamics",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 11: Thermodynamics
## Module 66: Specific Heat Capacities of Gases, Mayer's Relation ($C_p - C_v = R$) & State Variables

### 1. Why Do Gases Have Multiple Specific Heat Capacities?
When heating a solid or a liquid, the thermal expansion is minute, so virtually all absorbed heat goes into raising temperature. However, when heating a gas, the gas expands significantly against external pressure, performing mechanical work.
- If the gas is held at **constant volume**, all absorbed heat increases internal energy: no work is done ($W = 0$).
- If the gas is kept at **constant pressure**, it expands as it is heated, performing work $P \\, \\Delta V$. Thus, additional heat is required to achieve the same temperature rise!

### 2. Molar Specific Heat Capacities Defined
For $1 \\text{ mole}$ of an ideal gas:
1. **Molar Specific Heat at Constant Volume ($C_v$)**:
   $$C_v = \\left(\\frac{dQ}{dT}\\right)_v = \\left(\\frac{dU}{dT}\\right)_v$$
   Since for an ideal gas $U = U(T)$ regardless of volume:
   $$dU = n C_v \\, dT$$

2. **Molar Specific Heat at Constant Pressure ($C_p$)**:
   $$C_p = \\left(\\frac{dQ}{dT}\\right)_p$$

### 3. Rigorous Derivation of Mayer's Relation ($C_p - C_v = R$)
Consider $1 \\text{ mole}$ of an ideal gas undergoing a temperature rise $dT$:
- **Case 1: Heated at Constant Volume ($dV = 0$)**:
  By the First Law of Thermodynamics:
  $$dQ_v = dU + dW = dU + P(0) = dU$$
  Since $dQ_v = C_v \\, dT$:
  $$dU = C_v \\, dT$$

- **Case 2: Heated at Constant Pressure ($P = \\text{constant}$)**:
  By the First Law:
  $$dQ_p = dU + dW = dU + P \\, dV$$
  Since $dQ_p = C_p \\, dT$ and $dU = C_v \\, dT$:
  $$C_p \\, dT = C_v \\, dT + P \\, dV$$

From the ideal gas equation for $1 \\text{ mole}$ ($P V = R T$):
Differentiating at constant pressure $P$:
$$P \\, dV = R \\, dT$$
Substitute $P \\, dV = R \\, dT$ into the First Law expression:
$$C_p \\, dT = C_v \\, dT + R \\, dT$$
Dividing throughout by $dT$:
$$C_p = C_v + R \\implies C_p - C_v = R$$
This celebrated equation is **Mayer's Relation**.

### 4. Ratio of Specific Heats (Adiabatic Index $\\gamma$)
The dimensionless ratio of specific heats is:
$$\\gamma = \\frac{C_p}{C_v} = 1 + \\frac{R}{C_v}$$
Since $C_p > C_v$, $\\gamma > 1$ for all gases:
- **Monoatomic Gas** (He, Ne, Ar): Degrees of freedom $f = 3$
  $$C_v = \\frac{3}{2}R, \\quad C_p = \\frac{5}{2}R, \\quad \\gamma = \\frac{5}{3} \\approx 1.67$$
- **Diatomic Gas** ($N_2, O_2, H_2$ at room temperature): Degrees of freedom $f = 5$
  $$C_v = \\frac{5}{2}R, \\quad C_p = \\frac{7}{2}R, \\quad \\gamma = \\frac{7}{5} = 1.40$$
- **Triatomic / Polyatomic Non-linear Gas** ($H_2O, NH_3$): Degrees of freedom $f = 6$
  $$C_v = 3R, \\quad C_p = 4R, \\quad \\gamma = \\frac{4}{3} \\approx 1.33$$

### 5. Board Numerical Problem
**Problem**: Calculate the specific heat capacity of diatomic nitrogen gas ($N_2$) at constant volume and constant pressure. Given universal gas constant $R = 8.314 \\text{ J/(mol K)}$ and molar mass $M = 28 \\times 10^{-3} \\text{ kg/mol}$.
- **Step 1: Molar heat capacities**:
  $$C_v = \\frac{5}{2}R = 2.5 \\times 8.314 = 20.785 \\text{ J/(mol K)}$$
  $$C_p = \\frac{7}{2}R = 3.5 \\times 8.314 = 29.099 \\text{ J/(mol K)}$$
- **Step 2: Specific heat capacities per kg ($c_v = C_v / M$)**:
  $$c_v = \\frac{20.785}{28 \\times 10^{-3}} \\approx 742.3 \\text{ J/(kg K)}$$
  $$c_p = \\frac{29.099}{28 \\times 10^{-3}} \\approx 1039.3 \\text{ J/(kg K)}$$""",
            "svg_code": carnot_svg,
            
            
            "concept_questions": [
                {
                    "question": "Why is the molar specific heat at constant pressure (Cp) always greater than that at constant volume (Cv)?",
                    "options": [
                        "(Recommended) At constant pressure, part of the heat energy is expended in doing work against external pressure during expansion (P dV), while at constant volume no work is done",
                        "Because molecules move faster at constant pressure than at constant volume",
                        "Because the gas ionizes when heated at constant pressure",
                        "Because the volume decreases during constant pressure heating"
                    ],
                    "correct_answer": "(Recommended) At constant pressure, part of the heat energy is expended in doing work against external pressure during expansion (P dV), while at constant volume no work is done",
                    "explanation": "At constant volume dV = 0, so dW = 0 and all heat goes into dU. At constant pressure, dQ = dU + P dV, requiring extra heat equivalent to the expansion work done."
                }
            ]
        },

        # Module 67
        {
            "order_index": 67,
            "chapter_number": 11,
            "title": "Thermodynamic Processes: Isothermal, Adiabatic, Isochoric, Isobaric & Indicator Diagrams",
            "term": "Final-Term Examination",
            "unit": "Unit VIII: Thermodynamics",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 11: Thermodynamics
## Module 67: Thermodynamic Processes: Isothermal, Adiabatic, Isochoric, Isobaric & Indicator Diagrams

### 1. Quasi-Static Process
A process executed so infinitesimally slowly that the system remains in thermodynamic equilibrium with its surroundings at every intermediate instant is called a **quasi-static process**. Frictionless, reversible quasi-static processes trace continuous paths on an indicator ($P-V$) diagram.

### 2. Isothermal Process ($T = \\text{constant}$)
A process occurring at constant temperature.
- **Equation of State**:
  $$P V = \\text{constant} \\implies P_1 V_1 = P_2 V_2$$
- **Conditions**: Conducting walls of cylinder, extremely slow compression or expansion allowing heat exchange to maintain constant $T$.
- **Change in Internal Energy**:
  Since $T$ is constant, $\\Delta U = 0$.
- **First Law Formulation**:
  $$Q = W$$
  All heat absorbed is converted directly into external work.
- **Work Done in Isothermal Expansion**:
  $$W_{\\text{iso}} = \\int_{V_1}^{V_2} P \\, dV = \\int_{V_1}^{V_2} \\frac{nRT}{V} \\, dV = nRT [\\ln V]_{V_1}^{V_2}$$
  $$W_{\\text{iso}} = nRT \\ln\\left(\\frac{V_2}{V_1}\\right) = 2.303 \\, nRT \\log_{10}\\left(\\frac{V_2}{V_1}\\right) = 2.303 \\, nRT \\log_{10}\\left(\\frac{P_1}{P_2}\\right)$$

### 3. Adiabatic Process ($Q = 0$)
A process in which no heat enters or leaves the system across its boundaries.
- **Equation of State**:
  $$P V^\\gamma = \\text{constant} = K$$
  In terms of $T$ and $V$:
  $$T V^{\\gamma - 1} = \\text{constant}$$
  In terms of $P$ and $T$:
  $$P^{1 - \\gamma} T^\\gamma = \\text{constant}$$
- **Conditions**: Insulating walls (adiabatic boundary), extremely rapid sudden expansion or compression (e.g., bursting of a tire, propagation of sound waves).
- **First Law Formulation**:
  Since $Q = 0$:
  $$\\Delta U + W = 0 \\implies W = -\\Delta U = -n C_v (T_2 - T_1) = \\frac{nR(T_1 - T_2)}{\\gamma - 1}$$
  In terms of pressures and volumes:
  $$W_{\\text{adia}} = \\frac{P_1 V_1 - P_2 V_2}{\\gamma - 1}$$

### 4. Slopes on the Indicator ($P-V$) Diagram
- **Slope of Isothermal Curve**:
  $$P V = C \\implies P \\, dV + V \\, dP = 0 \\implies \\left(\\frac{dP}{dV}\\right)_{\\text{iso}} = -\\frac{P}{V}$$
- **Slope of Adiabatic Curve**:
  $$P V^\\gamma = C \\implies \\gamma P V^{\\gamma - 1} \\, dV + V^\\gamma \\, dP = 0 \\implies \\left(\\frac{dP}{dV}\\right)_{\\text{adia}} = -\\gamma \\frac{P}{V}$$
- **Key Invariant**:
  $$\\text{Slope of Adiabatic} = \\gamma \\times (\\text{Slope of Isothermal})$$
  Because $\\gamma > 1$, an adiabatic curve is strictly **steeper** than an isothermal curve at any intersection point!

### 5. Isochoric & Isobaric Processes
1. **Isochoric Process ($V = \\text{constant}$)**:
   - $dV = 0 \\implies W = 0$.
   - By First Law: $Q = \\Delta U = n C_v \\Delta T$.
2. **Isobaric Process ($P = \\text{constant}$)**:
   - $W = P(V_2 - V_1) = nR(T_2 - T_1)$.
   - $Q = n C_p \\Delta T$.
   - $\\Delta U = n C_v \\Delta T$.

### 6. Worked Board Problem
**Problem**: An ideal gas at $27^\\circ\\text{C}$ is suddenly compressed to $\\frac{1}{8}\\text{th}$ of its original volume. If $\\gamma = 1.5$, find the final temperature of the gas.
- **Solution**:
  - Given: $T_1 = 27 + 273 = 300 \\text{ K}$, $V_2 = \\frac{1}{8}V_1$, $\\gamma = 1.5$.
  - Formula: $T_1 V_1^{\\gamma - 1} = T_2 V_2^{\\gamma - 1}$
  - Calculation:
    $$T_2 = T_1 \\left(\\frac{V_1}{V_2}\\right)^{\\gamma - 1} = 300 \\times (8)^{1.5 - 1} = 300 \\times 8^{0.5} = 300 \\times \\sqrt{8} = 300 \\times 2.828 \\approx 848.5 \\text{ K}$$
    $$t_2 = 848.5 - 273 = 575.5^\\circ\\text{C}$$
  - The gas heats up drastically during adiabatic compression because work done on the gas increases internal energy.""",
            "svg_code": carnot_svg,
            
            
            "concept_questions": [
                {
                    "question": "Why is an adiabatic curve steeper than an isothermal curve on a P-V diagram?",
                    "options": [
                        "(Recommended) Because the slope of an adiabatic curve is -γ(P/V), which is γ times steeper than the isothermal slope -P/V, with γ > 1",
                        "Because the pressure is zero in an adiabatic process",
                        "Because the volume remains constant in an adiabatic process",
                        "Because heat flows freely into the system during adiabatic expansion"
                    ],
                    "correct_answer": "(Recommended) Because the slope of an adiabatic curve is -γ(P/V), which is γ times steeper than the isothermal slope -P/V, with γ > 1",
                    "explanation": "Differentiating PV = const yields dP/dV = -P/V. Differentiating PV^γ = const yields dP/dV = -γ(P/V). Since γ > 1 (e.g. 1.4 for air), the adiabatic curve has a steeper negative slope."
                }
            ]
        },

        # Module 68
        {
            "order_index": 68,
            "chapter_number": 11,
            "title": "Second Law of Thermodynamics, Heat Engines, Refrigerators & Reversibility",
            "term": "Final-Term Examination",
            "unit": "Unit VIII: Thermodynamics",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 11: Thermodynamics
## Module 68: Second Law of Thermodynamics, Heat Engines, Refrigerators & Reversibility

### 1. Inadequacy of the First Law
The First Law of Thermodynamics guarantees conservation of energy, but does **not** explain the direction of natural processes:
- It does not prevent heat from flowing spontaneously from a cold body to a hotter body.
- It does not forbid a motionless car from spontaneously absorbing thermal energy from the road and accelerating forward!
The **Second Law of Thermodynamics** specifies the natural direction of energy dissipation and the fundamental limits of energy conversion.

### 2. Heat Engine Architecture
A **heat engine** is a cyclical thermodynamic device that absorbs heat from a high-temperature reservoir (source), converts a fraction of it into mechanical work, and rejects the remaining heat to a lower-temperature reservoir (sink).
- Working cycle:
  * Heat absorbed from source at $T_1$: $Q_1$
  * Mechanical work output: $W$
  * Heat rejected to sink at $T_2$: $Q_2$
- Since the engine operates in a closed cycle, $\\Delta U_{\\text{cycle}} = 0$.
  By the First Law:
  $$W = Q_1 - Q_2$$
- **Thermal Efficiency ($\\eta$)**:
  $$\\eta = \\frac{\\text{Work Output}}{\\text{Heat Input}} = \\frac{W}{Q_1} = \\frac{Q_1 - Q_2}{Q_1} = 1 - \\frac{Q_2}{Q_1}$$

### 3. Refrigerator and Heat Pump
A **refrigerator** is a heat engine operating in reverse: it absorbs heat $Q_2$ from a cold body at $T_2$, receives external work $W$ from an electric compressor, and rejects heat $Q_1 = Q_2 + W$ to the warmer surroundings at $T_1$.
- **Coefficient of Performance ($\\beta$ or $\\text{COP}$)**:
  $$\\beta = \\frac{\\text{Desired Output}}{\\text{Work Input}} = \\frac{Q_2}{W} = \\frac{Q_2}{Q_1 - Q_2}$$

### 4. Statements of the Second Law of Thermodynamics
1. **Kelvin-Planck Statement**:
   * *It is impossible to construct an engine operating in a cycle whose sole effect is to extract heat from a reservoir and convert it completely into equivalent work without rejecting any heat.*
   * **Implication**: A 100% efficient heat engine ($\\eta = 1, Q_2 = 0$) is physically impossible!
2. **Clausius Statement**:
   * *It is impossible to construct a cyclic device whose sole effect is the transfer of heat from a cooler body to a hotter body without requiring an external work input.*
   * **Implication**: A refrigerator with infinite COP ($W = 0$) is physically impossible!

> **Equivalence of the Two Statements**: A violation of the Kelvin-Planck statement directly leads to a violation of the Clausius statement, and vice versa.

### 5. Reversible vs Irreversible Processes
- **Reversible Process**: A process that can be reversed such that both the system and the surroundings are restored to their exact initial states without leaving any net change anywhere in the universe. Requirements:
  1. Quasi-static (infinitely slow).
  2. Complete absence of dissipative forces (zero friction, zero viscosity, zero electrical resistance).
- **Irreversible Process**: All natural spontaneous processes in nature (free expansion of gases, friction, heat transfer across finite temperature difference) are irreversible.""",
            "svg_code": carnot_svg,
            
            
            "concept_questions": [
                {
                    "question": "Can a room be cooled by leaving the door of a domestic refrigerator open?",
                    "options": [
                        "(Recommended) No, the room will actually become warmer because the refrigerator rejects more heat to the room (Q1 = Q2 + W) than it absorbs from it (Q2)",
                        "Yes, the cold air from the refrigerator cools the entire room uniformly",
                        "The temperature of the room remains completely unchanged",
                        "The room cools down first and then immediately catches fire"
                    ],
                    "correct_answer": "(Recommended) No, the room will actually become warmer because the refrigerator rejects more heat to the room (Q1 = Q2 + W) than it absorbs from it (Q2)",
                    "explanation": "The room acts as both the source and sink. The refrigerator absorbs Q2 from the room, consumes electrical work W from the mains, and dumps Q1 = Q2 + W into the room. Net heat added to the room is W > 0, so the room heats up."
                }
            ]
        },

        # Module 69
        {
            "order_index": 69,
            "chapter_number": 11,
            "title": "Carnot Engine Cycle, Carnot Efficiency (η = 1 - T2/T1) & Carnot's Theorem",
            "term": "Final-Term Examination",
            "unit": "Unit VIII: Thermodynamics",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 11: Thermodynamics
## Module 69: Carnot Engine Cycle, Carnot Efficiency ($\\eta = 1 - T_2/T_1$) & Carnot's Theorem

### 1. The Ideal Carnot Cycle
In 1824, French engineer Sadi Carnot conceived an idealized, completely reversible thermodynamic cycle operating between two heat reservoirs at temperatures $T_1$ (source) and $T_2$ (sink) ($T_1 > T_2$).

The Carnot cycle consists of four successive reversible strokes:
1. **Stroke 1: Reversible Isothermal Expansion ($A \\to B$)**:
   - The cylinder is placed on the hot source at $T_1$.
   - Gas expands reversibly from $(P_1, V_1)$ to $(P_2, V_2)$ at constant temperature $T_1$.
   - Heat absorbed: $Q_1 = W_1 = nRT_1 \\ln\\left(\\frac{V_2}{V_1}\\right)$.
2. **Stroke 2: Reversible Adiabatic Expansion ($B \\to C$)**:
   - The cylinder is placed on an insulating stand ($Q = 0$).
   - Gas expands from $(P_2, V_2)$ to $(P_3, V_3)$, cooling from $T_1$ to $T_2$.
   - Work done: $W_2 = \\frac{nR(T_1 - T_2)}{\\gamma - 1}$.
3. **Stroke 3: Reversible Isothermal Compression ($C \\to D$)**:
   - The cylinder is placed on the cold sink at $T_2$.
   - Gas is compressed reversibly from $(P_3, V_3)$ to $(P_4, V_4)$ at constant temperature $T_2$.
   - Heat rejected: $Q_2 = -W_3 = nRT_2 \\ln\\left(\\frac{V_3}{V_4}\\right)$.
4. **Stroke 4: Reversible Adiabatic Compression ($D \\to A$)**:
   - The cylinder is placed back on the insulating stand ($Q = 0$).
   - Gas is compressed from $(P_4, V_4)$ back to initial state $(P_1, V_1)$, warming from $T_2$ to $T_1$.
   - Work done: $W_4 = -\\frac{nR(T_1 - T_2)}{\\gamma - 1} = -W_2$.

### 2. Net Work and Carnot Efficiency Derivation
- Net work done in one complete cycle:
  $$W_{\\text{net}} = W_1 + W_2 + W_3 + W_4$$
  Since $W_2 + W_4 = 0$:
  $$W_{\\text{net}} = W_1 + W_3 = nRT_1 \\ln\\left(\\frac{V_2}{V_1}\\right) - nRT_2 \\ln\\left(\\frac{V_3}{V_4}\\right)$$

For the two adiabatic stages ($B \\to C$ and $D \\to A$):
$$T_1 V_2^{\\gamma - 1} = T_2 V_3^{\\gamma - 1} \\quad \\text{and} \\quad T_1 V_1^{\\gamma - 1} = T_2 V_4^{\\gamma - 1}$$
Dividing these equations gives:
$$\\left(\\frac{V_2}{V_1}\\right)^{\\gamma - 1} = \\left(\\frac{V_3}{V_4}\\right)^{\\gamma - 1} \\implies \\frac{V_2}{V_1} = \\frac{V_3}{V_4}$$
Therefore:
$$\\frac{Q_2}{Q_1} = \\frac{T_2 \\ln(V_3/V_4)}{T_1 \\ln(V_2/V_1)} = \\frac{T_2}{T_1}$$
Substituting into the thermal efficiency equation:
$$\\eta_{\\text{carnot}} = 1 - \\frac{Q_2}{Q_1} = 1 - \\frac{T_2}{T_1}$$

### 3. Carnot's Theorem
1. *No heat engine operating between two given constant temperature reservoirs $T_1$ and $T_2$ can be more efficient than a reversible Carnot engine operating between the same two temperatures.*
2. *All reversible engines operating between the same two temperatures have identical efficiencies, irrespective of the nature of the working substance.*
$$\\eta_{\\text{real}} \\le \\eta_{\\text{carnot}} = 1 - \\frac{T_2}{T_1}$$

### 4. Board Numerical Problem
**Problem**: A Carnot engine absorbs $1000 \\text{ J}$ of heat from a heat reservoir at $500 \\text{ K}$ and rejects heat to a sink at $300 \\text{ K}$.
1. Find the efficiency of the engine.
2. Find the mechanical work delivered per cycle.
3. Find the amount of heat rejected to the sink per cycle.
- **Solution**:
  - $T_1 = 500 \\text{ K}, T_2 = 300 \\text{ K}, Q_1 = 1000 \\text{ J}$.
  - Efficiency: $\\eta = 1 - \\frac{300}{500} = 1 - 0.6 = 0.40 = 40\\%$.
  - Work: $W = \\eta \\times Q_1 = 0.40 \\times 1000 = 400 \\text{ J}$.
  - Heat rejected: $Q_2 = Q_1 - W = 1000 - 400 = 600 \\text{ J}$.""",
            "svg_code": carnot_svg,
            
            
            "concept_questions": [
                {
                    "question": "Under what condition would a Carnot engine achieve 100% thermal efficiency?",
                    "options": [
                        "(Recommended) If the sink temperature T2 is at absolute zero (0 K), which is practically unattainable by the Third Law of Thermodynamics",
                        "If the working substance is helium instead of air",
                        "If the cylinder is lubricated with zero friction",
                        "If the source temperature T1 is 100°C"
                    ],
                    "correct_answer": "(Recommended) If the sink temperature T2 is at absolute zero (0 K), which is practically unattainable by the Third Law of Thermodynamics",
                    "explanation": "Efficiency η = 1 - T2/T1. For η = 1, T2 must be 0 K or T1 must be infinity. Since absolute zero cannot be reached in a finite number of steps, 100% efficiency is physically impossible."
                }
            ]
        },

        # Module 70
        {
            "order_index": 70,
            "chapter_number": 11,
            "title": "Comprehensive NCERT Exercises 11.1 to 11.10 Detailed Step-by-Step Solver",
            "term": "Final-Term Examination",
            "unit": "Unit VIII: Thermodynamics",
            "cadence_stage": "Stage 5 to 6: Socratic Check & Exam-Topper Numerical Practice",
            "content": """# Chapter 11: Thermodynamics
## Module 70: Comprehensive NCERT Exercises 11.1 to 11.10 Detailed Step-by-Step Solver

### Exercise 11.1
**Question**: A geyser heats water flowing at the rate of $2.0 \\text{ litres per minute}$ from $27^\\circ\\text{C}$ to $77^\\circ\\text{C}$. If the geyser operates on a gas burner, what is the rate of consumption of the fuel if its heat of combustion is $4.0 \\times 10^4 \\text{ J/g}$?
- **Step 1**: Volume flow rate = $2.0 \\text{ L/min} = \\frac{2.0 \\times 10^{-3} \\text{ m}^3}{60 \\text{ s}}$.
  Mass flow rate $m' = \\frac{2.0 \\text{ kg}}{60 \\text{ s}} = \\frac{1}{30} \\text{ kg/s}$.
- **Step 2**: Temperature increase $\\Delta T = 77 - 27 = 50^\\circ\\text{C} = 50 \\text{ K}$.
  Specific heat capacity of water $c = 4184 \\text{ J/(kg K)}$.
- **Step 3**: Rate of heat required:
  $$\\frac{dQ}{dt} = m' c \\Delta T = \\left(\\frac{1}{30}\\right) \\times 4184 \\times 50 = \\frac{209200}{30} \\approx 6973.3 \\text{ J/s}$$
- **Step 4**: Fuel consumption rate:
  Heat of combustion $H = 4.0 \\times 10^4 \\text{ J/g} = 4.0 \\times 10^7 \\text{ J/kg}$.
  $$\\frac{dm_{\\text{fuel}}}{dt} = \\frac{dQ/dt}{H} = \\frac{6973.3}{4.0 \\times 10^7} \\approx 1.743 \\times 10^{-4} \\text{ kg/s} = 0.174 \\text{ g/s} = 10.46 \\text{ g/min}$$
- **Boxed Answer**: Fuel consumption rate = **$10.5 \\text{ g/min}$**.

---

### Exercise 11.2
**Question**: What amount of heat must be supplied to $2.0 \\times 10^{-2} \\text{ kg}$ of nitrogen (at room temperature) to raise its temperature by $45^\\circ\\text{C}$ at constant pressure? (Molecular mass of $N_2 = 28$, $R = 8.3 \\text{ J/(mol K)}$).
- **Step 1**: Number of moles $n = \\frac{m}{M} = \\frac{20 \\text{ g}}{28 \\text{ g/mol}} = \\frac{5}{7} \\text{ mol}$.
- **Step 2**: Molar heat capacity at constant pressure for diatomic $N_2$:
  $$C_p = \\frac{7}{2}R = 3.5 \\times 8.3 = 29.05 \\text{ J/(mol K)}$$
- **Step 3**: Heat required:
  $$Q = n C_p \\Delta T = \\left(\\frac{5}{7}\\right) \\times 29.05 \\times 45 = 933.75 \\text{ J}$$
- **Boxed Answer**: Heat required = **$934 \\text{ J}$**.

---

### Exercise 11.3
**Question**: Explain why:
1. Two bodies at different temperatures $T_1$ and $T_2$ if brought in thermal contact do not necessarily settle to the mean temperature $(T_1 + T_2)/2$.
2. The coolant in a chemical or nuclear plant should have high specific heat.
3. Air pressure in a car tyre increases during driving.
4. The climate of a harbour town is more temperate than that of a town in a desert at the same latitude.
- **Answers**:
  1. Equilibrium temperature depends on heat capacities ($m_1 c_1$ and $m_2 c_2$). Heat lost = Heat gained: $m_1 c_1 (T_1 - T) = m_2 c_2 (T - T_2)$. Only if $m_1 c_1 = m_2 c_2$ does $T = (T_1 + T_2)/2$.
  2. High specific heat enables the coolant to absorb large amounts of heat with only a small rise in its own temperature, maximizing cooling efficiency.
  3. Friction between the rolling tyre and the road does work on the tyre, heating the trapped air. By Gay-Lussac's Law at constant volume, $P \\propto T$, so pressure increases.
  4. Water has a tremendous specific heat capacity ($4184 \\text{ J/(kg K)}$) compared to land/sand. The sea absorbs heat during hot days and releases it slowly at night, moderating coastal temperature extremes.

---

### Exercise 11.4
**Question**: In changing the state of a gas adiabatically from an equilibrium state $A$ to another equilibrium state $B$, an amount of work equal to $22.3 \\text{ J}$ is done on the system. If the gas is taken from state $A$ to $B$ via a process in which the net heat absorbed by the system is $9.35 \\text{ cal}$, how much is the net work done by the system in the latter case? ($1 \\text{ cal} = 4.19 \\text{ J}$).
- **Step 1**: For adiabatic path ($A \\to B$), $Q = 0$, $W_{\\text{adia}} = -22.3 \\text{ J}$ (work done on system).
  By First Law: $\\Delta U = U_B - U_A = Q - W = 0 - (-22.3) = +22.3 \\text{ J}$.
- **Step 2**: For second path ($A \\to B$):
  Heat absorbed $Q = 9.35 \\text{ cal} = 9.35 \\times 4.19 \\text{ J} = 39.18 \\text{ J}$.
  Since internal energy is a state function, $\\Delta U$ is identical: $\\Delta U = +22.3 \\text{ J}$.
- **Step 3**: Work done by system:
  $$W = Q - \\Delta U = 39.18 - 22.3 = 16.88 \\text{ J}$$
- **Boxed Answer**: Net work done by the system = **$16.9 \\text{ J}$**.

---

### Exercise 11.5
**Question**: A thermodynamic system is taken from an original state to an intermediate state by the linear process shown in Fig. (11.1). Its volume is then reduced to the original value by an isobaric process. Calculate the total work done by the gas from $E$ to $F$ to $G$.
- **Step 1**: Identify indicator diagram: $E \\to F$ is linear expansion from $(P_E, V_E)$ to $(P_F, V_F)$, $F \\to G$ is isobaric compression at $P_F$.
- **Step 2**: Work done in a cyclic or multi-stage path is the area under the trajectory on the $P-V$ diagram.
- **Boxed Answer**: Work done = **Area under the curve on $P-V$ diagram**.

---

### Exercise 11.6 to 11.10 Key Insights
- **Carnot Refrigerator COP**: $\\beta = \\frac{T_2}{T_1 - T_2}$. For freezing water into ice at $0^\\circ\\text{C}$ in a room at $27^\\circ\\text{C}$, $\\beta = \\frac{273}{300 - 273} = \\frac{273}{27} \\approx 10.1$.
- **Steam Engine Efficiency**: Operates between boiler ($T_1$) and condenser ($T_2$). Even ideal Carnot efficiency rarely exceeds $30\\%$ to $40\\%$ for conventional temperature differentials.""",
            "svg_code": carnot_svg,
            
            
            "concept_questions": [
                {
                    "question": "In an adiabatic process from state A to B, 22.3 J of work is done on the system. If taken from A to B via another path absorbing 39.2 J of heat, what is the work done?",
                    "options": [
                        "(Recommended) 16.9 J",
                        "22.3 J",
                        "61.5 J",
                        "-16.9 J"
                    ],
                    "correct_answer": "(Recommended) 16.9 J",
                    "explanation": "ΔU = -W_adia = +22.3 J. For the new path, W = Q - ΔU = 39.2 J - 22.3 J = 16.9 J."
                }
            ]
        }
    ]
