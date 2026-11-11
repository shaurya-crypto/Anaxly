"""
Class 11 Physics - Chapter 14: Waves (Unit X)
Syllabus: Final-Term Examination
Module Range: Modules 83 to 88 (6 modules)
Fully aligned with NCERT Physics Part 2 (keph207.pdf) and CBSE 2026-27 Syllabus.
"""

try:
    from .svg_builder_physics11_pt2 import (
        build_standing_waves_organ_pipe_svg,
        build_beats_acoustic_svg,
        get_svg_wrapper
    )
except ImportError:
    from svg_builder_physics11_pt2 import (
        build_standing_waves_organ_pipe_svg,
        build_beats_acoustic_svg,
        get_svg_wrapper
    )

def get_ch14_curriculum():
    return {
        "chapter_number": 14,
        "title": "Chapter 14: Waves",
        "description": "Comprehensive mathematical and physical analysis of wave motion, transverse and longitudinal mechanical waves, wave speed derivations on strings and in gases (Newton-Laplace), superposition principle, boundary reflection, standing waves in strings and organ pipes, and acoustic beats.",
        "term": "Final-Term Examination",
        "unit": "Unit X: Oscillations and Waves",
        "class_level": "Class 11",
        "subject": "Physics",
        "total_modules": 6,
        "start_module": 83,
        "end_module": 88
    }

def get_ch14_modules():
    organ_svg = build_standing_waves_organ_pipe_svg()
    beats_svg = build_beats_acoustic_svg()

    return [
        # Module 83
        {
            "order_index": 83,
            "chapter_number": 14,
            "title": "Transverse & Longitudinal Waves, Progressive Wave Equation, Amplitude & Phase",
            "term": "Final-Term Examination",
            "unit": "Unit X: Oscillations and Waves",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 14: Waves
## Module 83: Transverse & Longitudinal Waves, Progressive Wave Equation, Amplitude & Phase

### 1. Intuition: Energy Propagation Without Bulk Mass Transfer
When you toss a pebble into a calm pond, concentric ripples expand outward across the surface. A dry leaf floating on the water merely bobs up and down; it does not travel with the expanding wave crests.
> **Definition of a Wave**: A wave is a self-sustaining disturbance that propagates through a medium (or vacuum for electromagnetic waves), transporting **energy and momentum** from one point to another without the bodily transport of matter.

### 2. Transverse vs Longitudinal Waves
1. **Transverse Waves**:
   - The constituent particles of the medium oscillate **perpendicular** to the direction of wave propagation.
   - Propagates as alternating **crests** (elevations) and **troughs** (depressions).
   - Requires shear elasticity (modulus of rigidity) to propagate $\\implies$ *can propagate only in solids and on liquid surfaces, never in the bulk of liquids or gases*.
   - Examples: Waves on a plucked guitar string, ripples on water.
2. **Longitudinal Waves**:
   - The particles of the medium oscillate **parallel** (back and forth) along the direction of wave propagation.
   - Propagates as alternating **compressions** (high density and pressure) and **rarefactions** (low density and pressure).
   - Requires volume elasticity (bulk modulus) $\\implies$ *can propagate through solids, liquids, and gases alike*.
   - Example: Sound waves in air.

### 3. The Harmonic Progressive Wave Equation
Consider a harmonic wave travelling in the positive $x$-direction:
$$y(x, t) = A \\sin(k x - \\omega t + \\phi)$$
or equivalently:
$$y(x, t) = A \\sin(\\omega t - k x + \\phi')$$
where:
- $y(x, t)$: Transverse displacement of particle at position $x$ at time $t$.
- $A$: **Amplitude**, the maximum displacement from equilibrium.
- $\\omega = 2\\pi \\nu = \\frac{2\\pi}{T}$: **Angular Frequency** ($\\text{rad/s}$).
- $k = \\frac{2\\pi}{\\lambda}$: **Propagation Constant / Angular Wave Number** ($\\text{rad/m}$).
- $\\lambda$: **Wavelength**, the spatial period between two consecutive points in the same phase.
- $\\phi$: Initial phase angle.

#### Wave Speed Relation:
The speed with which the wave profile travels through space is:
$$v = \\frac{\\omega}{k} = \\frac{2\\pi \\nu}{2\\pi / \\lambda} = \\nu \\lambda = \\frac{\\lambda}{T}$$

### 4. Direction of Wave Propagation
- If the argument is $(k x - \\omega t)$ or $(k x + \\omega t)$:
  * $(k x - \\omega t)$: Wave travelling in the **$+x$ direction** (to the right).
  * $(k x + \\omega t)$: Wave travelling in the **$-x$ direction** (to the left).

### 5. Particle Velocity vs Wave Speed
- **Wave Speed ($v$)**: The constant speed of energy propagation determined solely by medium properties:
  $$v = \\frac{\\omega}{k}$$
- **Particle Velocity ($v_p$)**: The instantaneous velocity of a specific medium particle executing SHM:
  $$v_p(x, t) = \\frac{\\partial y}{\\partial t} = -\\omega A \\cos(k x - \\omega t + \\phi)$$
- **Slope of Wave Profile**:
  $$\\frac{\\partial y}{\\partial x} = k A \\cos(k x - \\omega t + \\phi)$$
- **Fundamental Invariant**:
  $$v_p = -v \\left(\\frac{\\partial y}{\\partial x}\\right) = -(\\text{Wave Speed}) \\times (\\text{Slope of Wave})$$""",
            "svg_code": organ_svg,
            
            
            "concept_questions": [
                {
                    "question": "What is the relationship between particle velocity (v_p), wave speed (v), and the slope of the wave profile (∂y/∂x)?",
                    "options": [
                        "(Recommended) v_p = - v (∂y/∂x)",
                        "v_p = + v (∂y/∂x)",
                        "v_p = v / (∂y/∂x)",
                        "v_p = - (∂y/∂x) / v"
                    ],
                    "correct_answer": "(Recommended) v_p = - v (∂y/∂x)",
                    "explanation": "Differentiating y = A sin(kx - ωt) with respect to t gives v_p = -ω A cos(kx - ωt). Differentiating with respect to x gives ∂y/∂x = k A cos(kx - ωt). Dividing yields v_p = -(ω/k)(∂y/∂x) = -v(∂y/∂x)."
                }
            ]
        },

        # Module 84
        {
            "order_index": 84,
            "chapter_number": 14,
            "title": "Speed of Travelling Waves: Stretched Strings & Newton-Laplace Sound Equation",
            "term": "Final-Term Examination",
            "unit": "Unit X: Oscillations and Waves",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 14: Waves
## Module 84: Speed of Travelling Waves: Stretched Strings & Newton-Laplace Sound Equation

### 1. Speed of Transverse Wave on a Stretched String
The speed of a transverse pulse propagating along a taut elastic string depends on:
1. **Elastic property**: Tension $T$ in the string ($\\text{N}$).
2. **Inertial property**: Linear mass density $\\mu = \\frac{m}{L}$ (mass per unit length in $\\text{kg/m}$).

By dimensional analysis and dynamic equilibrium of a small circular arc element of the string:
$$v = \\sqrt{\\frac{T}{\\mu}}$$
- Increasing string tension $T$ makes the wave travel faster (tightening guitar tuning pegs raises pitch!).
- Heavier, thicker strings (larger $\\mu$) carry waves slower (thick bass strings produce lower frequencies).

### 2. Speed of Longitudinal (Sound) Waves in an Elastic Fluid
For any fluid medium with Bulk Modulus $B$ and density $\\rho$:
$$v = \\sqrt{\\frac{B}{\\rho}}$$

### 3. Newton's Formula for Speed of Sound in Air
Sir Isaac Newton assumed that when sound propagates through air, compressions and rarefactions occur so slowly that heat generated during compression escapes to surroundings, and cooling during rarefaction is compensated. Hence, he assumed sound propagation is an **isothermal process**.
- For an isothermal process:
  $$P V = \\text{constant} \\implies P \\, dV + V \\, dP = 0 \\implies B_{\\text{iso}} = -V \\frac{dP}{dV} = P$$
- Newton's formula:
  $$v = \\sqrt{\\frac{P}{\\rho}}$$
- Calculation at STP ($P = 1.013 \\times 10^5 \\text{ N/m}^2$, $\\rho = 1.293 \\text{ kg/m}^3$):
  $$v = \\sqrt{\\frac{1.013 \\times 10^5}{1.293}} \\approx 280 \\text{ m/s}$$
- **Discrepancy**: The experimental speed of sound in air at STP is **$331 \\text{ m/s}$**. Newton's formula was off by nearly $16\\%$!

### 4. Laplace's Adiabatic Correction (Pierre-Simon Laplace, 1816)
Laplace pointed out Newton's fundamental flaw:
1. Air is a very poor conductor of heat.
2. Compressions and rarefactions occur with immense rapidity (hundreds to thousands of times per second).
3. Therefore, no heat exchange takes place between compression zones and rarefaction zones: sound propagation is strictly an **adiabatic process** ($P V^\\gamma = \\text{constant}$)!

- For an adiabatic process:
  $$P V^\\gamma = C \\implies \\gamma P V^{\\gamma - 1} dV + V^\\gamma dP = 0 \\implies B_{\\text{adia}} = -V \\frac{dP}{dV} = \\gamma P$$
- **The Newton-Laplace Formula**:
  $$v = \\sqrt{\\frac{\\gamma P}{\\rho}}$$
- Calculation for air (diatomic gas, $\\gamma = 1.40$):
  $$v = \\sqrt{\\frac{1.40 \\times 1.013 \\times 10^5}{1.293}} = \\sqrt{109675} \\approx 331.2 \\text{ m/s}$$
This agrees with experimental measurements!

### 5. Factors Affecting the Speed of Sound in Gases
Using $P V = n R T \\implies \\frac{P}{\\rho} = \\frac{R T}{M}$:
$$v = \\sqrt{\\frac{\\gamma R T}{M}}$$
1. **Effect of Temperature**: $v \\propto \\sqrt{T}$. Speed increases as air warms up.
2. **Effect of Pressure**: At constant temperature, $\\frac{P}{\\rho} = \\text{constant}$, so sound speed is **independent of pressure**!
3. **Effect of Humidity**: Water vapor is lighter than dry air ($M_{\\text{vapor}} = 18 \\text{ g/mol}$ vs $M_{\\text{air}} \\approx 29 \\text{ g/mol}$). Humid air has lower density, hence sound travels faster in humid air.""",
            "svg_code": organ_svg,
            
            
            "concept_questions": [
                {
                    "question": "Why did Newton's original formula for the speed of sound in air fail, and how did Laplace correct it?",
                    "options": [
                        "(Recommended) Newton assumed isothermal propagation (B = P), whereas Laplace proved compressions and rarefactions occur too rapidly for heat transfer, making it adiabatic (B = γP)",
                        "Newton assumed air is a solid, while Laplace treated it as a liquid",
                        "Newton forgot to include the mass of the Earth in the equation",
                        "Newton used Fahrenheit instead of Kelvin"
                    ],
                    "correct_answer": "(Recommended) Newton assumed isothermal propagation (B = P), whereas Laplace proved compressions and rarefactions occur too rapidly for heat transfer, making it adiabatic (B = γP)",
                    "explanation": "Because air is an insulator and sound oscillations occur rapidly, no heat flows across wave zones. The adiabatic bulk modulus B_adia = γP yields the accurate theoretical speed v = √(γP/ρ) ≈ 331 m/s."
                }
            ]
        },

        # Module 85
        {
            "order_index": 85,
            "chapter_number": 14,
            "title": "Superposition Principle & Reflection of Waves at Rigid and Open Boundaries",
            "term": "Final-Term Examination",
            "unit": "Unit X: Oscillations and Waves",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 14: Waves
## Module 85: Superposition Principle & Reflection of Waves at Rigid and Open Boundaries

### 1. Principle of Superposition of Waves
When two or more wave trains travel through the same medium simultaneously, each wave propagates independently as if the other waves were not present.
> **The Principle of Superposition States**:
> *The resultant displacement of any medium particle at any given instant is the vector sum of the individual displacements produced by each constituent wave:*
$$y(x, t) = y_1(x, t) + y_2(x, t) + \\dots + y_n(x, t)$$

This linear superposition leads to three profound phenomena in acoustics:
1. **Interference**: Superposition of two waves of equal frequency travelling in the same direction.
2. **Standing / Stationary Waves**: Superposition of two identical waves travelling in **opposite directions**.
3. **Beats**: Superposition of two waves of slightly differing frequencies travelling in the same direction.

### 2. Reflection of Waves at Boundaries
When a wave travelling in a medium strikes a boundary, it is reflected back into the original medium.

#### 1. Reflection at a Rigid / Fixed Boundary (Denser Medium):
Imagine a string securely tied to a rigid steel post:
- When a crest hits the rigid wall, it exerts an upward force on the support.
- By Newton's Third Law, the rigid support exerts an equal and opposite downward reaction force on the string.
- The reflected pulse returns as an **inverted trough**:
  $$y_i = A \\sin(k x - \\omega t)$$
  $$y_r = -A \\sin(-k x - \\omega t) = A \\sin(k x + \\omega t + \\pi)$$
- **Key Invariant**: Reflection at a rigid boundary introduces a **phase change of $\\pi$ radians ($180^\\circ$)**!

#### 2. Reflection at an Open / Free Boundary (Rarer Medium):
Imagine a string attached to a frictionless light ring that slides freely along a vertical rod:
- The ring is unrestrained and moves to twice the incident amplitude at the boundary.
- No downward restoring reaction force is exerted.
- The reflected pulse returns as an **upright crest** (zero phase change):
  $$y_r = A \\sin(k x + \\omega t)$$
- **Key Invariant**: Reflection at a free boundary occurs with **zero phase change**!""",
            "svg_code": organ_svg,
            
            
            "concept_questions": [
                {
                    "question": "What is the phase difference between an incident wave pulse and its reflected wave pulse at a rigid boundary?",
                    "options": [
                        "(Recommended) π radians (180° phase flip)",
                        "Zero radians (in phase)",
                        "π / 2 radians (90°)",
                        "2π radians"
                    ],
                    "correct_answer": "(Recommended) π radians (180° phase flip)",
                    "explanation": "At a rigid boundary, the net displacement must remain zero (node). Newton's Third Law reaction exerts an opposite restoring force that flips crests into troughs, imparting a phase change of π."
                }
            ]
        },

        # Module 86
        {
            "order_index": 86,
            "chapter_number": 14,
            "title": "Standing Waves & Normal Modes: Stretched Strings and Organ Pipes",
            "term": "Final-Term Examination",
            "unit": "Unit X: Oscillations and Waves",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 14: Waves
## Module 86: Standing Waves & Normal Modes: Stretched Strings and Organ Pipes

### 1. Mathematical Formation of Standing Waves
Consider two identical harmonic waves of equal amplitude $A$ and angular frequency $\\omega$ travelling in opposite directions along a string:
$$y_1(x, t) = A \\sin(kx - \\omega t)$$
$$y_2(x, t) = -A \\sin(kx + \\omega t) \\quad (\\text{reflected from rigid boundary at } x = 0)$$

By the Principle of Superposition:
$$y(x, t) = y_1 + y_2 = A [\\sin(kx - \\omega t) - \\sin(kx + \\omega t)]$$
Using the identity $\\sin C - \\sin D = 2 \\cos\\left(\\frac{C+D}{2}\\right) \\sin\\left(\\frac{C-D}{2}\\right)$:
$$y(x, t) = -[2A \\sin(kx)] \\cos(\\omega t)$$
- **Key Features of Standing Waves**:
  * The wave does **not** travel: it is stationary in space!
  * Every particle executes SHM with the same frequency $\\omega$, but the amplitude is spatially dependent:
    $$A_{\\text{standing}}(x) = 2A \\sin(kx)$$
  * **Nodes ($N$)**: Points of permanently zero amplitude ($A_{\\text{standing}} = 0$):
    $$\\sin(kx) = 0 \\implies kx = n\\pi \\implies x = n \\frac{\\lambda}{2} \\quad (n = 0, 1, 2, \\dots)$$
  * **Antinodes ($A$)**: Points of maximum oscillation amplitude ($2A$):
    $$\\sin(kx) = \\pm 1 \\implies kx = \\left(n + \\frac{1}{2}\\right)\\pi \\implies x = \\left(n + \\frac{1}{2}\\right) \\frac{\\lambda}{2}$$
  * Distance between consecutive nodes = distance between consecutive antinodes = $\\frac{\\lambda}{2}$.
  * Distance between adjacent node and antinode = $\\frac{\\lambda}{4}$.

### 2. Normal Modes of a Stretched String (Fixed at Both Ends)
For a string of length $L$ fixed at $x = 0$ and $x = L$, nodes must occur at both boundaries:
$$L = n \\frac{\\lambda_n}{2} \\implies \\lambda_n = \\frac{2L}{n} \\quad (n = 1, 2, 3, \\dots)$$
Frequencies of normal modes:
$$\\nu_n = \\frac{v}{\\lambda_n} = n \\left(\\frac{v}{2L}\\right) = \\frac{n}{2L} \\sqrt{\\frac{T}{\\mu}}$$
- **Fundamental / First Harmonic ($n = 1$)**: $\\nu_1 = \\frac{v}{2L}$.
- **Second Harmonic / First Overtone ($n = 2$)**: $\\nu_2 = 2 \\nu_1$.
- **Harmonics Ratio**: $\\nu_1 : \\nu_2 : \\nu_3 = 1 : 2 : 3 : 4 \\dots$ (All harmonics are present!).

### 3. Normal Modes of Organ Pipes
1. **Closed Organ Pipe (Closed at one end, Open at the other)**:
   - Closed end = Node (air molecules cannot move).
   - Open end = Antinode (pressure equals atmospheric, displacement is free).
   - Length condition:
     $$L = (2n - 1) \\frac{\\lambda_n}{4} \\implies \\lambda_n = \\frac{4L}{2n - 1} \\quad (n = 1, 2, 3, \\dots)$$
   - Frequencies:
     $$\\nu_n = (2n - 1) \\frac{v}{4L}$$
   - **Harmonics Ratio**: $\\nu_1 : \\nu_2 : \\nu_3 = 1 : 3 : 5 : 7 \\dots$
   - **Crucial Rule**: *A closed organ pipe produces ONLY odd harmonics!*
2. **Open Organ Pipe (Open at both ends)**:
   - Antinodes occur at both open ends.
   - Length condition:
     $$L = n \\frac{\\lambda_n}{2} \\implies \\lambda_n = \\frac{2L}{n}$$
   - Frequencies:
     $$\\nu_n = n \\frac{v}{2L} \\quad (n = 1, 2, 3, \\dots)$$
   - **Harmonics Ratio**: $\\nu_1 : \\nu_2 : \\nu_3 = 1 : 2 : 3 : 4 \\dots$
   - *An open organ pipe produces both even and odd harmonics, making its musical tone richer than a closed pipe!*""",
            "svg_code": organ_svg,
            
            
            "concept_questions": [
                {
                    "question": "Why does an open organ pipe produce a richer and more melodious sound than a closed organ pipe of the same fundamental frequency?",
                    "options": [
                        "(Recommended) Because an open organ pipe produces both even and odd harmonics (1:2:3:4...), whereas a closed pipe produces only odd harmonics (1:3:5...)",
                        "Because an open pipe is made of wood rather than metal",
                        "Because an open pipe has a higher wave speed",
                        "Because no nodes exist anywhere inside an open pipe"
                    ],
                    "correct_answer": "(Recommended) Because an open organ pipe produces both even and odd harmonics (1:2:3:4...), whereas a closed pipe produces only odd harmonics (1:3:5...)",
                    "explanation": "Open organ pipes possess antinodes at both ends, allowing all integer multiples (n = 1, 2, 3, 4...) of the fundamental frequency to resonate, creating a richer acoustic spectrum with all overtones."
                }
            ]
        },

        # Module 87
        {
            "order_index": 87,
            "chapter_number": 14,
            "title": "Acoustic Beats: Analytical Derivation, Beat Frequency & Tuning Applications",
            "term": "Final-Term Examination",
            "unit": "Unit X: Oscillations and Waves",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 14: Waves
## Module 87: Acoustic Beats: Analytical Derivation, Beat Frequency & Tuning Applications

### 1. Real-Life Intuition: The Pulsing Hum of Two Guitars
When two guitarists tune their strings to the same note, as their frequencies come very close (say $440 \\text{ Hz}$ and $442 \\text{ Hz}$), they hear a distinct periodic swelling and fading in loudness—a throbbing "wah-wah-wah" sound twice per second. As they adjust the pegs and the frequencies become exactly identical, the throbbing vanishes!
> **Definition of Beats**: The periodic waxings (constructive interference) and wanings (destructive interference) in the intensity of sound heard when two sound waves of slightly differing frequencies travel simultaneously in the same direction.

### 2. Rigorous Analytical Derivation
Consider two sound waves of equal amplitude $A$ and slightly different angular frequencies $\\omega_1$ and $\\omega_2$ arriving at the observer's ear ($x = 0$):
$$s_1(t) = A \\cos(\\omega_1 t)$$
$$s_2(t) = A \\cos(\\omega_2 t)$$
where $\\omega_1 = 2\\pi \\nu_1$ and $\\omega_2 = 2\\pi \\nu_2$.

By the Superposition Principle:
$$s(t) = s_1(t) + s_2(t) = A [\\cos(\\omega_1 t) + \\cos(\\omega_2 t)]$$
Using the trigonometric identity $\\cos C + \\cos D = 2 \\cos\\left(\\frac{C - D}{2}\\right) \\cos\\left(\\frac{C + D}{2}\\right)$:
$$s(t) = 2A \\cos\\left[\\frac{(\\omega_1 - \\omega_2)}{2} t\\right] \\cos\\left[\\frac{(\\omega_1 + \\omega_2)}{2} t\\right]$$
Let:
- Effective modulated amplitude:
  $$A_{\\text{mod}}(t) = 2A \\cos\\left[\\pi (\\nu_1 - \\nu_2) t\\right]$$
- Average carrier frequency:
  $$\\nu_{\\text{av}} = \\frac{\\nu_1 + \\nu_2}{2}$$
Thus:
$$s(t) = A_{\\text{mod}}(t) \\cos(2\\pi \\nu_{\\text{av}} t)$$

### 3. Beat Frequency Formulation
Intensity $I$ is proportional to the square of amplitude:
$$I \\propto A_{\\text{mod}}^2 = 4A^2 \\cos^2\\left[\\pi (\\nu_1 - \\nu_2) t\\right]$$

1. **Maximal Intensity (Waxing)**:
   Occurs when $\\cos[\\pi (\\nu_1 - \\nu_2) t] = \\pm 1$:
   $$\\pi (\\nu_1 - \\nu_2) t = n\\pi \\implies t = \\frac{n}{\\nu_1 - \\nu_2} \\quad (n = 0, 1, 2, \\dots)$$
   Time interval between consecutive waxings:
   $$T_b = \\frac{1}{\\nu_1 - \\nu_2}$$
2. **Minimal Intensity (Waning)**:
   Occurs when $\\cos[\\pi (\\nu_1 - \\nu_2) t] = 0$:
   $$t = \\frac{(2n + 1)}{2(\\nu_1 - \\nu_2)}$$
3. **The Beat Frequency ($\\nu_b$)**:
   $$\\nu_b = \\frac{1}{T_b} = |\\nu_1 - \\nu_2|$$
   > **Fundamental Theorem**: *The number of beats heard per second equals the absolute difference between the frequencies of the two interfering sound sources!*

### 4. Human Auditory Limit
The persistence of hearing in human ears is roughly $0.1 \\text{ second}$.
Therefore, for distinct beats to be perceived individually by the human ear, the beat period must exceed $0.1 \\text{ s}$:
$$\\nu_b \\le 10 \\text{ beats/second}$$
If $\\nu_b > 10 \\text{ Hz}$, the beats blur into a continuous discordant sensation (acoustic roughness).

### 5. Practical Applications
1. **Tuning Musical Instruments**: Musicians sound a reference tuning fork alongside their instrument until the beat rate slows down to zero.
2. **Detection of Poisonous Mine Gases**: An open pipe blown with pure air is sounded alongside a pipe containing mine gas. If toxic methane is present, the change in sound speed creates noticeable beats.""",
            "svg_code": beats_svg,
            
            
            "concept_questions": [
                {
                    "question": "What is the maximum beat frequency that can be distinctly perceived as individual throbs by the human ear?",
                    "options": [
                        "(Recommended) 10 beats per second (due to the 0.1 s persistence of human hearing)",
                        "20,000 beats per second",
                        "2 beats per second",
                        "100 beats per second"
                    ],
                    "correct_answer": "(Recommended) 10 beats per second (due to the 0.1 s persistence of human hearing)",
                    "explanation": "Because human hearing retains acoustic sensations for approximately 0.1 seconds, beat frequencies greater than 10 Hz fuse into a continuous tone rather than distinct periodic waxings and wanings."
                }
            ]
        },

        # Module 88
        {
            "order_index": 88,
            "chapter_number": 14,
            "title": "Comprehensive NCERT Exercises 14.1 to 14.22 Detailed Step-by-Step Solver",
            "term": "Final-Term Examination",
            "unit": "Unit X: Oscillations and Waves",
            "cadence_stage": "Stage 5 to 6: Socratic Check & Exam-Topper Numerical Practice",
            "content": """# Chapter 14: Waves
## Module 88: Comprehensive NCERT Exercises 14.1 to 14.22 Detailed Step-by-Step Solver

### Exercise 14.1
**Question**: A string of mass $2.50 \\text{ kg}$ is under a tension of $200 \\text{ N}$. The length of the stretched string is $20.0 \\text{ m}$. If the transverse jerk is struck at one end of the string, how long does the disturbance take to reach the other end?
- **Step 1**: Linear mass density $\\mu = \\frac{M}{L} = \\frac{2.50 \\text{ kg}}{20.0 \\text{ m}} = 0.125 \\text{ kg/m}$.
- **Step 2**: Speed of transverse wave:
  $$v = \\sqrt{\\frac{T}{\\mu}} = \\sqrt{\\frac{200}{0.125}} = \\sqrt{1600} = 40.0 \\text{ m/s}$$
- **Step 3**: Time to traverse length $L$:
  $$t = \\frac{L}{v} = \\frac{20.0 \\text{ m}}{40.0 \\text{ m/s}} = 0.50 \\text{ s}$$
- **Boxed Answer**: Time taken = **$0.50 \\text{ seconds}$**.

---

### Exercise 14.2
**Question**: A stone dropped from the top of a tower of height $300 \\text{ m}$ high splashes into the water of a pond near the base of the tower. When is the splash heard at the top? Given that the speed of sound in air is $340 \\text{ m/s}$ ($g = 9.8 \\text{ m/s}^2$).
- **Step 1**: Time for stone to fall distance $h = 300 \\text{ m}$:
  $$h = \\frac{1}{2} g t_1^2 \\implies t_1 = \\sqrt{\\frac{2h}{g}} = \\sqrt{\\frac{2 \\times 300}{9.8}} = \\sqrt{61.22} \\approx 7.824 \\text{ s}$$
- **Step 2**: Time for sound wave of splash to travel up $300 \\text{ m}$:
  $$t_2 = \\frac{h}{v} = \\frac{300}{340} \\approx 0.882 \\text{ s}$$
- **Step 3**: Total time elapsed:
  $$t_{\\text{total}} = t_1 + t_2 = 7.824 + 0.882 = 8.706 \\text{ s}$$
- **Boxed Answer**: Splash is heard after **$8.71 \\text{ seconds}$**.

---

### Exercise 14.3
**Question**: A steel wire has a length of $12.0 \\text{ m}$ and a mass of $2.10 \\text{ kg}$. What should be the tension in the wire so that speed of a transverse wave on the wire equals the speed of sound in dry air at $20^\\circ\\text{C}$ ($= 343 \\text{ m/s}$)?
- **Step 1**: Linear mass density $\\mu = \\frac{2.10}{12.0} = 0.175 \\text{ kg/m}$.
- **Step 2**: Formula $v = \\sqrt{\\frac{T}{\\mu}} \\implies T = \\mu v^2$.
- **Step 3**:
  $$T = 0.175 \\times (343)^2 = 0.175 \\times 117649 \\approx 20588.6 \\text{ N} = 2.06 \\times 10^4 \\text{ N}$$
- **Boxed Answer**: Tension required = **$2.06 \\times 10^4 \\text{ N}$**.

---

### Exercise 14.4
**Question**: Use the formula $v = \\sqrt{\\frac{\\gamma P}{\\rho}}$ to explain why the speed of sound in air:
1. Is independent of pressure.
2. Increases with temperature.
3. Increases with humidity.
- **Answers**:
  1. From ideal gas equation $\\frac{P}{\\rho} = \\frac{RT}{M}$. Thus $v = \\sqrt{\\frac{\\gamma RT}{M}}$, which depends only on temperature $T$ and molar mass $M$, completely independent of pressure $P$ at constant temperature.
  2. $v \\propto \\sqrt{T}$, so as absolute temperature rises, speed of sound increases.
  3. Water vapor has molar mass $18 \\text{ g/mol}$, which is significantly lighter than dry air ($\approx 29 \\text{ g/mol}$). Moist air has lower density $\\rho$, so $v = \\sqrt{\\frac{\\gamma P}{\\rho}}$ increases.

---

### Exercise 14.5
**Question**: You have learnt that a travelling wave in one dimension is represented by a function $y = f(x, t)$ where $x$ and $t$ must appear in the combination $x - vt$ or $x + vt$.
Which of the following functions can represent a travelling wave?
1. $(x - vt)^2$
2. $\\ln[(x + vt)/x_0]$
3. $\\frac{1}{x + vt}$
4. $\\exp[-(x - vt)^2]$
- **Answer**:
  A function represents a physical wave only if it remains **finite and bounded** for all values of $x$ and $t$.
  1. $(x - vt)^2 \\to \\infty$ as $x \\to \\infty$ (unphysical).
  2. $\\ln[(x + vt)/x_0] \\to -\\infty$ at $x = -vt$ and $\\to \\infty$ as $x \\to \\infty$ (unphysical).
  3. $\\frac{1}{x + vt} \\to \\infty$ at $x = -vt$ (unphysical singular pole).
  4. $\\exp[-(x - vt)^2]$ is bounded between $0$ and $1$ everywhere $\\implies$ **Represents a physical Gaussian wave pulse!**""",
            "svg_code": beats_svg,
            
            
            "concept_questions": [
                {
                    "question": "Why does the function exp[-(x - vt)^2] represent a valid travelling wave pulse whereas (x - vt)^2 does not?",
                    "options": [
                        "(Recommended) Because exp[-(x - vt)^2] remains bounded and finite everywhere between 0 and 1, whereas (x - vt)^2 blows up to infinity as x -> infinity",
                        "Because exponential functions can only move forwards in time",
                        "Because (x - vt)^2 has no velocity term",
                        "Because Gaussian functions are strictly periodic"
                    ],
                    "correct_answer": "(Recommended) Because exp[-(x - vt)^2] remains bounded and finite everywhere between 0 and 1, whereas (x - vt)^2 blows up to infinity as x -> infinity",
                    "explanation": "A physical wave displacement must be finite and physically realizable for all values of position and time. (x - vt)^2 diverges to infinity, making it non-physical, whereas the Gaussian pulse is smooth and bounded everywhere."
                }
            ]
        }
    ]
