"""
Class 11 Physics - Chapter 12: Kinetic Theory of Gases (Unit IX)
Syllabus: Final-Term Examination
Module Range: Modules 71 to 76 (6 modules)
Fully aligned with NCERT Physics Part 2 (keph205.pdf) and CBSE 2026-27 Syllabus.
"""

try:
    from .svg_builder_physics11_pt2 import (
        build_kinetic_theory_gas_svg,
        get_svg_wrapper
    )
except ImportError:
    from svg_builder_physics11_pt2 import (
        build_kinetic_theory_gas_svg,
        get_svg_wrapper
    )

def get_ch12_curriculum():
    return {
        "chapter_number": 12,
        "title": "Chapter 12: Kinetic Theory",
        "description": "Microscopic statistical mechanics of ideal gases, derivation of macroscopic pressure from elastic molecular collisions, kinetic interpretation of temperature, Maxwellian speed distribution, degrees of freedom, law of equipartition of energy, molar specific heats, and mean free path.",
        "term": "Final-Term Examination",
        "unit": "Unit IX: Behaviour of Perfect Gases and Kinetic Theory of Gases",
        "class_level": "Class 11",
        "subject": "Physics",
        "total_modules": 6,
        "start_module": 71,
        "end_module": 76
    }

def get_ch12_modules():
    kinetic_svg = build_kinetic_theory_gas_svg()

    return [
        # Module 71
        {
            "order_index": 71,
            "chapter_number": 12,
            "title": "Molecular Nature of Matter, Behaviour of Gases, Gas Laws & Ideal Gas Equation",
            "term": "Final-Term Examination",
            "unit": "Unit IX: Behaviour of Perfect Gases and Kinetic Theory of Gases",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 12: Kinetic Theory
## Module 71: Molecular Nature of Matter, Behaviour of Gases, Gas Laws & Ideal Gas Equation

### 1. Real-Life Intuition: The Microscopic View of a Gas
When you inflate a bicycle tire or a soccer ball with a hand pump, the rubber skin becomes firm and taut. What is pushing outward on the rubber? You are not packing a solid block inside; you are introducing billions upon billions of sub-microscopic molecules darting at supersonic speeds, continuously bombarding the inner walls of the rubber casing.

The **Kinetic Theory of Gases** bridges the gap between the microscopic world of atoms/molecules and the macroscopic thermodynamic quantities we measure in the laboratory: Pressure ($P$), Volume ($V$), and Temperature ($T$).

### 2. Historical Gas Laws
1. **Boyle's Law (Robert Boyle, 1662)**:
   For a given mass of gas at constant temperature $T$:
   $$P \\propto \\frac{1}{V} \\implies P V = \\text{constant} \\quad (T = \\text{constant})$$
2. **Charles's Law (Jacques Charles, 1787)**:
   For a given mass of gas at constant pressure $P$:
   $$V \\propto T \\implies \\frac{V}{T} = \\text{constant} \\quad (P = \\text{constant})$$
   (where $T$ is absolute temperature in Kelvin).
3. **Gay-Lussac's / Amontons's Law**:
   For a given mass of gas at constant volume $V$:
   $$P \\propto T \\implies \\frac{P}{T} = \\text{constant} \\quad (V = \\text{constant})$$
4. **Avogadro's Law (Amedeo Avogadro, 1811)**:
   Equal volumes of all gases under identical conditions of temperature and pressure contain an equal number of molecules:
   $$V \\propto n \\quad (P, T = \\text{constant})$$

### 3. The Ideal Gas Equation of State
Combining Boyle's, Charles's, and Avogadro's laws yields the **Ideal Gas Equation**:
$$P V = n R T$$
where:
- $n = \\frac{m}{M} = \\frac{N}{N_A}$ is the number of moles.
- $R = 8.314 \\text{ J/(mol K)}$ is the Universal Gas Constant.
- $N_A = 6.022 \\times 10^{23} \\text{ molecules/mol}$ is Avogadro's Number.

Alternatively, expressing in terms of the total number of molecules $N$:
$$P V = N k_B T$$
where:
$$k_B = \\frac{R}{N_A} = \\frac{8.314}{6.022 \\times 10^{23}} = 1.381 \\times 10^{-23} \\text{ J/K}$$
is **Boltzmann's Constant**, the fundamental conversion factor between temperature and molecular kinetic energy.

### 4. Real Gases vs Ideal Gases
An **ideal gas** is a theoretical model characterized by:
1. Gas molecules are point masses with negligible finite volume compared to the container volume.
2. Intermolecular attractive and repulsive forces are completely negligible except during instantaneous collisions.

**When does a real gas behave like an ideal gas?**
Real gases (like $O_2, N_2, H_2, He$) approach ideal gas behavior under:
- **Low Pressure ($P \\to 0$)**: Molecules are far apart, making intermolecular forces and molecular volume negligible.
- **High Temperature ($T \\gg T_c$)**: Kinetic energy completely overwhelms intermolecular potential energy.""",
            "svg_code": kinetic_svg,
            
            
            "concept_questions": [
                {
                    "question": "Under what physical conditions does a real gas behave most like an ideal gas?",
                    "options": [
                        "(Recommended) Low pressure and high temperature",
                        "High pressure and low temperature",
                        "High pressure and high temperature",
                        "Low pressure and absolute zero temperature"
                    ],
                    "correct_answer": "(Recommended) Low pressure and high temperature",
                    "explanation": "At low pressure, molecules are spaced far apart so their finite volume is negligible. At high temperature, molecular kinetic energies are large enough to completely overcome intermolecular attraction."
                }
            ]
        },

        # Module 72
        {
            "order_index": 72,
            "chapter_number": 12,
            "title": "Kinetic Theory Postulates & Derivation of Pressure of an Ideal Gas (P = 1/3 ρ v_rms^2)",
            "term": "Final-Term Examination",
            "unit": "Unit IX: Behaviour of Perfect Gases and Kinetic Theory of Gases",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 12: Kinetic Theory
## Module 72: Kinetic Theory Postulates & Derivation of Pressure of an Ideal Gas ($P = \\frac{1}{3} \\rho v_{\\text{rms}}^2$)

### 1. Fundamental Postulates of the Kinetic Theory of Gases
1. A gas consists of an enormous number of identical, tiny, hard, spherical particles called molecules.
2. The actual volume of molecules is negligible compared to the total volume occupied by the gas.
3. Gas molecules are in continuous, random, chaotic motion in all directions with varying speeds.
4. Collisions between molecules and with the container walls are **perfectly elastic** (kinetic energy and momentum are strictly conserved).
5. Gravitational attraction between molecules is negligible compared to their rapid motion.
6. The time duration of a collision is negligible compared to the time interval between successive collisions.

### 2. Rigorous Derivation of Gas Pressure
Consider a cubical container of side $L$ and volume $V = L^3$ containing $N$ identical gas molecules, each of mass $m$.
- Let a molecule have velocity components $(v_x, v_y, v_z)$ such that:
  $$v^2 = v_x^2 + v_y^2 + v_z^2$$

#### Step 1: Collision with Wall Perpendicular to $x$-Axis
Consider the wall $A_1$ located at $x = L$ (area $A = L^2$):
- Before collision, momentum component: $p_{xi} = m v_x$.
- After elastic rebound from the rigid wall: $p_{xf} = -m v_x$.
- Change in momentum of the molecule in one collision:
  $$\\Delta p_x = p_{xf} - p_{xi} = -m v_x - m v_x = -2 m v_x$$
- By Newton's Third Law, momentum transferred to the wall:
  $$\\Delta p_{\\text{wall}} = +2 m v_x$$

#### Step 2: Time Interval Between Collisions
After bouncing off wall $A_1$, the molecule travels across length $L$ to the opposite wall, rebounds, and returns to wall $A_1$, travelling a total distance $2L$:
$$\\Delta t = \\frac{2L}{v_x}$$

#### Step 3: Average Force Exerted by Single Molecule
By Newton's Second Law:
$$F_1 = \\frac{\\Delta p_{\\text{wall}}}{\\Delta t} = \\frac{2 m v_x}{2L / v_x} = \\frac{m v_x^2}{L}$$

#### Step 4: Total Force Exerted by All $N$ Molecules
Summing over all $N$ molecules:
$$F_{\\text{total}} = \\sum_{i=1}^N \\frac{m v_{xi}^2}{L} = \\frac{m}{L} \\sum_{i=1}^N v_{xi}^2 = \\frac{m N}{L} \\overline{v_x^2}$$
where $\\overline{v_x^2}$ is the mean-square velocity in the $x$-direction:
$$\\overline{v_x^2} = \\frac{1}{N} \\sum_{i=1}^N v_{xi}^2$$

#### Step 5: Isotropy of Molecular Velocities
Because molecular motion is completely random and isotropic with no preferred spatial direction:
$$\\overline{v_x^2} = \\overline{v_y^2} = \\overline{v_z^2}$$
Since $\\overline{v^2} = \\overline{v_x^2} + \\overline{v_y^2} + \\overline{v_z^2} = 3 \\overline{v_x^2}$:
$$\\overline{v_x^2} = \\frac{1}{3} \\overline{v^2}$$

#### Step 6: Pressure on the Wall
Pressure is force per unit area:
$$P = \\frac{F_{\\text{total}}}{A} = \\frac{m N \\overline{v_x^2}}{L \\times L^2} = \\frac{m N \\overline{v_x^2}}{L^3} = \\frac{m N}{V} \\left(\\frac{1}{3} \\overline{v^2}\\right)$$
Since total mass of gas is $M = m N$ and density is $\\rho = \\frac{M}{V}$:
$$P = \\frac{1}{3} \\frac{m N}{V} \\overline{v^2} = \\frac{1}{3} \\rho \\overline{v^2} = \\frac{1}{3} \\rho v_{\\text{rms}}^2$$
> **Fundamental Theorem**: The macroscopic pressure of an ideal gas equals one-third of the product of its mass density and its mean-square molecular speed!""",
            "svg_code": kinetic_svg,
            
            
            "concept_questions": [
                {
                    "question": "In the derivation of gas pressure P = 1/3 ρ v_rms^2, where does the factor of 1/3 originate?",
                    "options": [
                        "(Recommended) From the 3-dimensional isotropy of space, where the mean square velocity is equally divided among the x, y, and z axes (v_x^2 = v^2 / 3)",
                        "From the three states of matter (solid, liquid, gas)",
                        "From the triangular cross section of the container",
                        "From Newton's three laws of motion"
                    ],
                    "correct_answer": "(Recommended) From the 3-dimensional isotropy of space, where the mean square velocity is equally divided among the x, y, and z axes (v_x^2 = v^2 / 3)",
                    "explanation": "Because molecular motion is completely random with no preferred direction, the mean-square velocity is split equally across all three spatial dimensions: v_x^2 = v_y^2 = v_z^2 = v^2 / 3."
                }
            ]
        },

        # Module 73
        {
            "order_index": 73,
            "chapter_number": 12,
            "title": "Kinetic Interpretation of Temperature, Average KE & Root-Mean-Square Speed",
            "term": "Final-Term Examination",
            "unit": "Unit IX: Behaviour of Perfect Gases and Kinetic Theory of Gases",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 12: Kinetic Theory
## Module 73: Kinetic Interpretation of Temperature, Average KE & Root-Mean-Square Speed

### 1. Kinetic Interpretation of Temperature
Recall the fundamental pressure relation:
$$P = \\frac{1}{3} \\frac{m N}{V} \\overline{v^2}$$
Multiplying both sides by container volume $V$:
$$P V = \\frac{1}{3} m N \\overline{v^2} = \\frac{2}{3} N \\left(\\frac{1}{2} m \\overline{v^2}\\right)$$
From the ideal gas law:
$$P V = N k_B T$$
Equating the two expressions:
$$\\frac{2}{3} N \\left(\\frac{1}{2} m \\overline{v^2}\\right) = N k_B T$$
Dividing by $N$:
$$\\overline{E_k} = \\frac{1}{2} m \\overline{v^2} = \\frac{3}{2} k_B T$$
> **Profound Physical Conclusion**:
> 1. Absolute temperature $T$ is a direct macroscopic measure of the average translational kinetic energy of the constituent molecules of the gas!
> 2. Average translational kinetic energy depends **solely on absolute temperature $T$**, completely independent of the mass, shape, or chemical identity of the molecule!
> 3. At absolute zero ($T = 0 \\text{ K}$), molecular translational motion ceases completely.

### 2. Total Internal Energy of an Ideal Gas
For $1 \\text{ mole}$ of a monoatomic ideal gas containing $N_A$ molecules:
$$U = N_A \\times \\left(\\frac{3}{2} k_B T\\right) = \\frac{3}{2} (N_A k_B) T = \\frac{3}{2} R T$$
For $n$ moles:
$$U = \\frac{3}{2} n R T$$

### 3. Root-Mean-Square Speed ($v_{\\text{rms}}$)
The root-mean-square speed is defined as the square root of the mean of squares of molecular speeds:
$$v_{\\text{rms}} = \\sqrt{\\overline{v^2}} = \\sqrt{\\frac{3 k_B T}{m}} = \\sqrt{\\frac{3 R T}{M}} = \\sqrt{\\frac{3 P}{\\rho}}$$
where:
- $m$ is the mass of one molecule.
- $M = m N_A$ is the molar mass in $\\text{kg/mol}$.

### 4. Comparison of Characteristic Molecular Speeds
In Maxwell's speed distribution:
1. **Most Probable Speed ($v_{\\text{mp}}$)**:
   $$v_{\\text{mp}} = \\sqrt{\\frac{2 R T}{M}} \\approx 1.414 \\sqrt{\\frac{R T}{M}}$$
2. **Mean / Average Speed ($v_{\\text{av}}$)**:
   $$v_{\\text{av}} = \\sqrt{\\frac{8 R T}{\\pi M}} \\approx 1.596 \\sqrt{\\frac{R T}{M}}$$
3. **Root-Mean-Square Speed ($v_{\\text{rms}}$)**:
   $$v_{\\text{rms}} = \\sqrt{\\frac{3 R T}{M}} \\approx 1.732 \\sqrt{\\frac{R T}{M}}$$
Ratio:
$$v_{\\text{mp}} : v_{\\text{av}} : v_{\\text{rms}} = \\sqrt{2} : \\sqrt{\\frac{8}{\\pi}} : \\sqrt{3} \\approx 1 : 1.128 : 1.225$$

### 5. Worked Board Numerical Problem
**Problem**: Calculate the root-mean-square speed of oxygen molecules ($O_2$) at $27^\\circ\\text{C}$. (Molar mass of $O_2 = 32 \\times 10^{-3} \\text{ kg/mol}$, $R = 8.314 \\text{ J/(mol K)}$).
- **Given**: $T = 27 + 273 = 300 \\text{ K}$, $M = 0.032 \\text{ kg/mol}$.
- **Formula**: $v_{\\text{rms}} = \\sqrt{\\frac{3 R T}{M}}$
- **Calculation**:
  $$v_{\\text{rms}} = \\sqrt{\\frac{3 \\times 8.314 \\times 300}{0.032}} = \\sqrt{\\frac{7482.6}{0.032}} = \\sqrt{233831.25} \\approx 483.6 \\text{ m/s}$$
- **Boxed Answer**: $v_{\\text{rms}} = **484 \\text{ m/s}**$ (faster than the speed of sound in air, $\\approx 343 \\text{ m/s}$!).""",
            "svg_code": kinetic_svg,
            
            
            "concept_questions": [
                {
                    "question": "At the same temperature T, how does the average translational kinetic energy of a heavy uranium hexafluoride molecule compare to that of a light hydrogen molecule?",
                    "options": [
                        "(Recommended) They are exactly identical, because average translational KE = 3/2 k_B T depends solely on temperature, not on molecular mass",
                        "Hydrogen has much greater KE because it travels faster",
                        "Uranium hexafluoride has much greater KE because it is heavier",
                        "Hydrogen has zero kinetic energy"
                    ],
                    "correct_answer": "(Recommended) They are exactly identical, because average translational KE = 3/2 k_B T depends solely on temperature, not on molecular mass",
                    "explanation": "Average translational kinetic energy per molecule is strictly 3/2 k_B T for any gas at temperature T. The lighter hydrogen molecule compensates by having a much larger RMS speed."
                }
            ]
        },

        # Module 74
        {
            "order_index": 74,
            "chapter_number": 12,
            "title": "Law of Equipartition of Energy, Degrees of Freedom & Specific Heats of Gases",
            "term": "Final-Term Examination",
            "unit": "Unit IX: Behaviour of Perfect Gases and Kinetic Theory of Gases",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 12: Kinetic Theory
## Module 74: Law of Equipartition of Energy, Degrees of Freedom & Specific Heats of Gases

### 1. Degrees of Freedom ($f$)
The number of independent coordinates or quadratic energy terms required to completely specify the position, orientation, and configuration of a dynamical system is called its **degrees of freedom** ($f$).

1. **Monoatomic Gas (He, Ne, Ar)**:
   - Point mass free to translate along $x, y, z$ axes.
   - Translational degrees of freedom = $3$.
   - Rotational = $0$ (infinitesimal moment of inertia).
   - Total degrees of freedom:
     $$f = 3$$
2. **Diatomic Gas ($O_2, N_2, H_2$) at Moderate Temperatures**:
   - Rigid dumbbell with fixed bond length.
   - Translational = $3$.
   - Rotational = $2$ (rotation about two axes perpendicular to the internuclear axis; moment of inertia about the bond axis is negligible).
   - Total degrees of freedom:
     $$f = 3 + 2 = 5$$
   *(At high temperatures, vibrational mode activates: adds $1$ kinetic + $1$ potential = $+2$ vibrational modes $\\implies f = 7$)*.
3. **Non-Linear Triatomic / Polyatomic Gas ($H_2O, NH_3, CH_4$)**:
   - Translational = $3$.
   - Rotational = $3$ (can rotate about all three principal axes).
   - Total degrees of freedom:
     $$f = 3 + 3 = 6$$

### 2. The Law of Equipartition of Energy
Formulated by James Clerk Maxwell and Ludwig Boltzmann:
> *In any dynamic system in thermal equilibrium at absolute temperature $T$, the total internal energy is distributed equally among all its degrees of freedom, and the average energy associated with each quadratic degree of freedom per molecule is strictly:*
$$\\epsilon = \\frac{1}{2} k_B T$$

### 3. Prediction of Molar Specific Heat Capacities
For $1 \\text{ mole}$ of a gas with $f$ degrees of freedom:
- Total internal energy:
  $$U = N_A \\times \\left(f \\times \\frac{1}{2} k_B T\\right) = \\frac{f}{2} R T$$
- Molar heat capacity at constant volume:
  $$C_v = \\frac{dU}{dT} = \\frac{f}{2} R$$
- By Mayer's Relation ($C_p = C_v + R$):
  $$C_p = \\left(\\frac{f}{2} + 1\\right) R$$
- Ratio of specific heats (adiabatic index $\\gamma$):
  $$\\gamma = \\frac{C_p}{C_v} = 1 + \\frac{2}{f}$$

#### Comprehensive Summary Table
| Gas Type | $f$ | $C_v$ | $C_p$ | $\\gamma = C_p / C_v$ |
| :--- | :---: | :---: | :---: | :---: |
| **Monoatomic** | 3 | $\\frac{3}{2}R \\approx 12.5 \\text{ J/mol K}$ | $\\frac{5}{2}R \\approx 20.8 \\text{ J/mol K}$ | $\\frac{5}{3} \\approx 1.67$ |
| **Diatomic (rigid)** | 5 | $\\frac{5}{2}R \\approx 20.8 \\text{ J/mol K}$ | $\\frac{7}{2}R \\approx 29.1 \\text{ J/mol K}$ | $\\frac{7}{5} = 1.40$ |
| **Diatomic (vibrating)** | 7 | $\\frac{7}{2}R \\approx 29.1 \\text{ J/mol K}$ | $\\frac{9}{2}R \\approx 37.4 \\text{ J/mol K}$ | $\\frac{9}{7} \\approx 1.29$ |
| **Polyatomic (non-linear)** | 6 | $3R \\approx 24.9 \\text{ J/mol K}$ | $4R \\approx 33.3 \\text{ J/mol K}$ | $\\frac{4}{3} \\approx 1.33$ |

### 4. Specific Heat of Solids (Dulong and Petit's Law)
In a crystalline solid, each of the $N_A$ atoms oscillates in 3 dimensions about its equilibrium lattice site. Each 1D harmonic oscillator has $2$ degrees of freedom ($1$ kinetic energy $\\frac{1}{2}mv^2$ + $1$ potential energy $\\frac{1}{2}kx^2$).
- Average energy per oscillator = $2 \\times \\frac{1}{2}k_B T = k_B T$.
- Total internal energy for $N_A$ atoms oscillating in 3D:
  $$U = 3 N_A k_B T = 3 R T$$
- Molar heat capacity of solids:
  $$C = \\frac{dU}{dT} = 3 R \\approx 3 \\times 8.314 \\approx 24.9 \\text{ J/(mol K)}$$
This is **Dulong and Petit's Law**, experimentally verified for most solids (copper, lead, aluminum) at room temperature!""",
            "svg_code": kinetic_svg,
            
            
            "concept_questions": [
                {
                    "question": "For a rigid diatomic gas molecule like nitrogen at room temperature, what are the values of Cv and γ?",
                    "options": [
                        "(Recommended) Cv = (5/2)R and γ = 1.40",
                        "Cv = (3/2)R and γ = 1.67",
                        "Cv = 3R and γ = 1.33",
                        "Cv = (7/2)R and γ = 1.29"
                    ],
                    "correct_answer": "(Recommended) Cv = (5/2)R and γ = 1.40",
                    "explanation": "A rigid diatomic molecule has 3 translational + 2 rotational = 5 degrees of freedom. Hence Cv = (5/2)R, Cp = (7/2)R, and γ = Cp/Cv = 7/5 = 1.40."
                }
            ]
        },

        # Module 75
        {
            "order_index": 75,
            "chapter_number": 12,
            "title": "Mean Free Path (λ = 1 / (√2 n π d^2)), Molecular Collisions & Brownian Motion",
            "term": "Final-Term Examination",
            "unit": "Unit IX: Behaviour of Perfect Gases and Kinetic Theory of Gases",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 12: Kinetic Theory
## Module 75: Mean Free Path ($\\lambda = \\frac{1}{\\sqrt{2} n \\pi d^2}$), Molecular Collisions & Brownian Motion

### 1. The Paradox of Molecular Speeds vs Diffusion
In Module 73, we saw that gas molecules travel at supersonic speeds ($\approx 484 \\text{ m/s}$ for $O_2$ at room temperature). Yet, if an ammonia bottle or perfume flask is opened across a room, it takes several seconds or minutes for the fragrance to reach your nose. Why?

The molecules do not travel in straight unobstructed paths! In normal air, a gas molecule undergoes roughly $10^9$ to $10^{10}$ collisions per second, tracing a zig-zag random walk. The average straight-line distance a molecule travels between two successive collisions is called the **Mean Free Path** ($\\lambda$).

### 2. Derivation of Mean Free Path ($\\lambda$)
Assume gas molecules are hard spheres of collision diameter $d$.
- A collision occurs whenever the centers of two molecules approach within a center-to-center distance $d$.
- The collision cross-section area is:
  $$\\sigma = \\pi d^2$$

#### Simplified Derivation (Single Moving Molecule):
Imagine one molecule moving at speed $v$ while all other molecules remain stationary:
- In time $\\Delta t$, the molecule sweeps out an imaginary collision cylinder of length $v \\Delta t$ and cross-sectional area $\\pi d^2$.
- Volume of cylinder swept:
  $$V_{\\text{cyl}} = \\pi d^2 v \\, \\Delta t$$
- If the number of molecules per unit volume (number density) is $n = \\frac{N}{V}$:
  $$\\text{Number of collisions in time } \\Delta t = n \\pi d^2 v \\, \\Delta t$$
- Collision frequency (collisions per second):
  $$\\nu = \\frac{\\text{Collisions}}{\\Delta t} = n \\pi d^2 v$$
- Mean free path $\\lambda$ is the distance travelled divided by the number of collisions:
  $$\\lambda_{\\text{approx}} = \\frac{v \\, \\Delta t}{n \\pi d^2 v \\, \\Delta t} = \\frac{1}{n \\pi d^2}$$

#### Accurate Derivation (All Molecules in Motion):
In reality, all molecules are darting simultaneously. The collision frequency depends on the **relative speed** between colliding pairs ($v_{\\text{rel}}$). For a Maxwellian velocity distribution:
$$v_{\\text{rel}} = \\sqrt{2} \\, v_{\\text{av}}$$
Therefore, taking relative molecular motion into account:
$$\\lambda = \\frac{1}{\\sqrt{2} \\, n \\pi d^2}$$

### 3. Dependence of Mean Free Path on $P$ and $T$
From the ideal gas law: $P = n k_B T \\implies n = \\frac{P}{k_B T}$.
Substituting into the mean free path formula:
$$\\lambda = \\frac{k_B T}{\\sqrt{2} \\pi d^2 P}$$
- $\\lambda \\propto T$ (at constant pressure, heating the gas decreases density and increases free path).
- $\\lambda \\propto \\frac{1}{P}$ (at constant temperature, compressing the gas packs molecules closer, reducing free path).

### 4. Brownian Motion
Discovered in 1827 by botanist Robert Brown observing pollen grains suspended in water, and mathematically explained by Albert Einstein in 1905:
- Microscopic pollen grains or smoke particles execute continuous, erratic, jagged zig-zag motions.
- **Cause**: Unbalanced microscopic collisions by surrounding liquid or gas molecules bombarding the microscopic particle from all sides at every millisecond!
- Einstein's mathematical formulation of Brownian motion provided the definitive, incontrovertible proof of the atomic/molecular nature of matter.""",
            "svg_code": kinetic_svg,
            
            
            "concept_questions": [
                {
                    "question": "If the pressure of an ideal gas inside a sealed vessel is doubled at constant temperature, what happens to its mean free path?",
                    "options": [
                        "(Recommended) The mean free path is halved, because λ is inversely proportional to pressure P (or number density n)",
                        "The mean free path is doubled",
                        "The mean free path remains unchanged",
                        "The mean free path increases by a factor of √2"
                    ],
                    "correct_answer": "(Recommended) The mean free path is halved, because λ is inversely proportional to pressure P (or number density n)",
                    "explanation": "λ = k_B T / (√2 π d^2 P). At constant temperature, doubling the pressure doubles the number density n of molecules per unit volume, which cuts the mean free path directly in half."
                }
            ]
        },

        # Module 76
        {
            "order_index": 76,
            "chapter_number": 12,
            "title": "Comprehensive NCERT Exercises 12.1 to 12.14 Detailed Step-by-Step Solver",
            "term": "Final-Term Examination",
            "unit": "Unit IX: Behaviour of Perfect Gases and Kinetic Theory of Gases",
            "cadence_stage": "Stage 5 to 6: Socratic Check & Exam-Topper Numerical Practice",
            "content": """# Chapter 12: Kinetic Theory
## Module 76: Comprehensive NCERT Exercises 12.1 to 12.14 Detailed Step-by-Step Solver

### Exercise 12.1
**Question**: Estimate the fraction of molecular volume to the actual volume occupied by oxygen gas at STP. Take the diameter of an oxygen molecule to be $3 \\text{ \\AA}$.
- **Step 1**: Volume of $1 \\text{ mole}$ of an ideal gas at STP = $22.4 \\text{ litres} = 22.4 \\times 10^{-3} \\text{ m}^3$.
- **Step 2**: Actual volume of $1 \\text{ mole}$ of oxygen molecules:
  Molecular radius $r = \\frac{d}{2} = 1.5 \\text{ \\AA} = 1.5 \\times 10^{-10} \\text{ m}$.
  Volume of 1 molecule $v_0 = \\frac{4}{3} \\pi r^3 = \\frac{4}{3} \\pi (1.5 \\times 10^{-10})^3 \\approx 1.414 \\times 10^{-29} \\text{ m}^3$.
  Total molecular volume for $N_A$ molecules:
  $$V_{\\text{mol}} = N_A v_0 = (6.022 \\times 10^{23}) \\times (1.414 \\times 10^{-29}) \\approx 8.51 \\times 10^{-6} \\text{ m}^3$$
- **Step 3**: Ratio:
  $$\\frac{V_{\\text{mol}}}{V_{\\text{gas}}} = \\frac{8.51 \\times 10^{-6}}{22.4 \\times 10^{-3}} \\approx 3.8 \\times 10^{-4}$$
- **Boxed Answer**: Molecular volume is only **$3.8 \\times 10^{-4}$** (less than $0.04\\%$) of the total gas volume, proving that molecules are separated by enormous empty space!

---

### Exercise 12.2
**Question**: Molar volume is the volume occupied by $1 \\text{ mol}$ of any (ideal) gas at standard temperature and pressure (STP: $1 \\text{ atmospheric pressure}, 0^\\circ\\text{C}$). Show that it is $22.4 \\text{ litres}$.
- **Step 1**: Ideal gas equation: $P V = n R T \\implies V = \\frac{n R T}{P}$.
- **Step 2**: Standard values:
  $n = 1 \\text{ mol}, R = 8.314 \\text{ J/(mol K)}, T = 273.15 \\text{ K}, P = 1.013 \\times 10^5 \\text{ N/m}^2$.
- **Step 3**:
  $$V = \\frac{1 \\times 8.314 \\times 273.15}{1.013 \\times 10^5} = \\frac{2271.07}{1.013 \\times 10^5} \\approx 0.022414 \\text{ m}^3 = 22.414 \\text{ litres}$$
- **Boxed Answer**: Molar volume at STP = **$22.4 \\text{ L}$**.

---

### Exercise 12.3
**Question**: Figure 12.8 shows plot of $P V / T$ versus $P$ for $1.00 \\times 10^{-3} \\text{ kg}$ of oxygen gas at two different temperatures $T_1$ and $T_2$.
1. What does the dotted line signify?
2. Which is true: $T_1 > T_2$ or $T_1 < T_2$?
3. What is the value of $P V / T$ where the curves meet on the y-axis?
- **Answers**:
  1. The dotted horizontal line represents an **ideal gas** for which $P V / T = n R = \\text{constant}$ at all pressures.
  2. $T_1 > T_2$. At higher temperatures, real gases approach ideal gas behavior more closely, so curve $T_1$ is closer to the ideal dotted line than curve $T_2$.
  3. Where the curves meet on the y-axis ($P \\to 0$):
     $$\\frac{P V}{T} = n R = \\frac{m}{M} R = \\frac{1.00 \\times 10^{-3} \\text{ kg}}{32 \\times 10^{-3} \\text{ kg/mol}} \\times 8.314 = \\frac{8.314}{32} \\approx 0.260 \\text{ J/K}$$

---

### Exercise 12.4
**Question**: An oxygen cylinder of volume $30 \\text{ litres}$ has an initial gauge pressure of $15 \\text{ atm}$ and temperature of $27^\\circ\\text{C}$. After some oxygen is withdrawn, the gauge pressure drops to $11 \\text{ atm}$ and temperature drops to $17^\\circ\\text{C}$. Estimate the mass of oxygen taken out of the cylinder. ($R = 8.31 \\text{ J/(mol K)}$, molecular mass of $O_2 = 32$).
- **Step 1**: Initial state:
  $P_1 = 15 \\text{ atm} = 15 \\times 1.013 \\times 10^5 = 1.52 \\times 10^6 \\text{ Pa}$, $V = 30 \\times 10^{-3} \\text{ m}^3$, $T_1 = 300 \\text{ K}$.
  $$n_1 = \\frac{P_1 V}{R T_1} = \\frac{1.52 \\times 10^6 \\times 0.03}{8.314 \\times 300} \\approx 18.28 \\text{ moles}$$
- **Step 2**: Final state:
  $P_2 = 11 \\text{ atm} = 11 \\times 1.013 \\times 10^5 = 1.114 \\times 10^6 \\text{ Pa}$, $T_2 = 290 \\text{ K}$.
  $$n_2 = \\frac{P_2 V}{R T_2} = \\frac{1.114 \\times 10^6 \\times 0.03}{8.314 \\times 290} \\approx 13.86 \\text{ moles}$$
- **Step 3**: Moles withdrawn:
  $$\\Delta n = n_1 - n_2 = 18.28 - 13.86 = 4.42 \\text{ moles}$$
  Mass taken out $\\Delta m = \\Delta n \\times M = 4.42 \\times 32 = 141.44 \\text{ g} = 0.141 \\text{ kg}$.
- **Boxed Answer**: Mass of oxygen withdrawn = **$0.141 \\text{ kg}$** ($141 \\text{ g}$).""",
            "svg_code": kinetic_svg,
            
            
            "concept_questions": [
                {
                    "question": "What is the physical significance of the ratio PV/T at the y-intercept (P -> 0) in the real gas behavior plot?",
                    "options": [
                        "(Recommended) It equals nR, the product of number of moles and the universal gas constant",
                        "It equals zero",
                        "It equals Boltzmann's constant k_B",
                        "It equals the absolute temperature"
                    ],
                    "correct_answer": "(Recommended) It equals nR, the product of number of moles and the universal gas constant",
                    "explanation": "As P -> 0, all real gases strictly obey the ideal gas equation PV = nRT, meaning the limit of PV/T as P -> 0 is universally nR."
                }
            ]
        }
    ]
