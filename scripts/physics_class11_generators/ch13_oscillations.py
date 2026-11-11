"""
Class 11 Physics - Chapter 13: Oscillations (Unit X)
Syllabus: Final-Term Examination
Module Range: Modules 77 to 82 (6 modules)
Fully aligned with NCERT Physics Part 2 (keph206.pdf) and CBSE 2026-27 Syllabus.
"""

try:
    from .svg_builder_physics11_pt2 import (
        build_shm_reference_circle_svg,
        get_svg_wrapper
    )
except ImportError:
    from svg_builder_physics11_pt2 import (
        build_shm_reference_circle_svg,
        get_svg_wrapper
    )

def get_ch13_curriculum():
    return {
        "chapter_number": 13,
        "title": "Chapter 13: Oscillations",
        "description": "Rigorous kinematics and dynamics of periodic and oscillatory motions, Simple Harmonic Motion (SHM), reference circle projection, velocity and acceleration differential equations, potential and kinetic energy conservation, spring-mass systems, and the simple pendulum.",
        "term": "Final-Term Examination",
        "unit": "Unit X: Oscillations and Waves",
        "class_level": "Class 11",
        "subject": "Physics",
        "total_modules": 6,
        "start_module": 77,
        "end_module": 82
    }

def get_ch13_modules():
    shm_svg = build_shm_reference_circle_svg()

    return [
        # Module 77
        {
            "order_index": 77,
            "chapter_number": 13,
            "title": "Periodic and Oscillatory Motions, Period, Frequency & Simple Harmonic Motion (SHM)",
            "term": "Final-Term Examination",
            "unit": "Unit X: Oscillations and Waves",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 13: Oscillations
## Module 77: Periodic and Oscillatory Motions, Period, Frequency & Simple Harmonic Motion (SHM)

### 1. Real-Life Intuition: The World of Vibrations
Look around you: a grandfather clock's swinging pendulum, the rhythmic heartbeat thumping in your chest, the plucked string of a guitar singing at 440 Hz, or the quartz crystal resonating in your wristwatch. All these motions exhibit a universal characteristic: they repeat themselves periodically over regular intervals of time.

### 2. Periodic vs Oscillatory Motion
- **Periodic Motion**: Any motion that repeats itself at regular intervals of time $T$ (e.g., the Earth orbiting the Sun, hands of a clock).
- **Oscillatory / Vibratory Motion**: A specific type of periodic motion in which an object moves back and forth (**to and fro**) about a stable central equilibrium position (mean position).
  * **Key Distinction**: *Every oscillatory motion is periodic, but every periodic motion is NOT oscillatory!* (The planetary orbit of Earth is periodic, but not to-and-fro).

### 3. Fundamental Kinematic Parameters
1. **Time Period ($T$)**: The smallest time interval after which the motion repeats itself. SI unit: second ($\\text{s}$).
2. **Frequency ($\\nu$ or $f$)**: The number of complete oscillations executed per unit time:
   $$\\nu = \\frac{1}{T}$$
   SI unit: Hertz ($\\text{Hz} = \\text{s}^{-1}$).
3. **Angular Frequency ($\\omega$)**:
   $$\\omega = 2\\pi \\nu = \\frac{2\\pi}{T}$$
   SI unit: radians per second ($\\text{rad/s}$).
4. **Displacement ($x(t)$)**: The directed physical distance of the oscillating particle from its equilibrium mean position at any time $t$.

### 4. Simple Harmonic Motion (SHM) Defined
**Simple Harmonic Motion** is the simplest and most fundamental form of oscillatory motion, where:
1. The restoring force (and hence acceleration) is directly proportional to the displacement of the particle from the mean position.
2. The restoring force is always directed toward the mean position.

Mathematically:
$$F = -k x$$
$$a = \\frac{d^2x}{dt^2} = -\\omega^2 x$$
where:
- $k$ is the spring or force constant ($\\text{N/m}$).
- $\\omega = \\sqrt{\\frac{k}{m}}$ is the natural angular frequency.

### 5. Harmonic Displacement Function
The general mathematical solution of the linear SHM differential equation is:
$$x(t) = A \\cos(\\omega t + \\phi)$$
or equivalently:
$$x(t) = A \\sin(\\omega t + \\phi')$$
where:
- $A$: **Amplitude**, the maximum displacement from the mean position on either side ($\\text{m}$).
- $(\\omega t + \\phi)$: **Phase** of the motion at time $t$ (radians), determining the exact position and direction of motion.
- $\\phi$: **Initial Phase / Epoch**, the phase at time $t = 0$.

### 6. Socratic Check for Understanding
Consider a particle oscillating between $x = -A$ and $x = +A$:
- At the mean position ($x = 0$): Displacement is zero, restoring force is zero, speed is at its maximum!
- At the extreme positions ($x = \\pm A$): Displacement is maximum, restoring force is maximum, speed momentarily drops to zero!""",
            "svg_code": shm_svg,
            
            
            "concept_questions": [
                {
                    "question": "What is the essential condition for a periodic motion to be classified as Simple Harmonic Motion (SHM)?",
                    "options": [
                        "(Recommended) The restoring acceleration must be directly proportional to displacement from equilibrium and directed towards the mean position (a = -ω^2 x)",
                        "The particle must move in a complete circle at constant speed",
                        "The amplitude must increase exponentially with time",
                        "The velocity must remain constant throughout the motion"
                    ],
                    "correct_answer": "(Recommended) The restoring acceleration must be directly proportional to displacement from equilibrium and directed towards the mean position (a = -ω^2 x)",
                    "explanation": "SHM is mathematically governed by the linear restoring force F = -kx, leading directly to a = -ω^2 x. The minus sign indicates that acceleration always points back towards the equilibrium origin."
                }
            ]
        },

        # Module 78
        {
            "order_index": 78,
            "chapter_number": 13,
            "title": "SHM and Uniform Circular Motion: The Reference Circle & Phasor Projection",
            "term": "Final-Term Examination",
            "unit": "Unit X: Oscillations and Waves",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 13: Oscillations
## Module 78: SHM and Uniform Circular Motion: The Reference Circle & Phasor Projection

### 1. Intuition: The Shadow on the Wall
Imagine a ball attached to the outer rim of a rotating turntable spinning at a constant angular velocity $\\omega$. If you shine a bright horizontal flashlight at the turntable, the shadow of the ball projected onto an adjacent flat screen does not move in a circle: it oscillates back and forth in a straight line, slowing down at the edges and speeding up through the center.
> **Theorem**: *The projection of uniform circular motion along any diameter of the circle executes pure Simple Harmonic Motion!*

### 2. Mathematical Proof via Reference Circle
Let a reference particle $P$ move counter-clockwise along a circle of radius $A$ (called the **reference circle**) with constant angular speed $\\omega$.
- Let the position vector $\\vec{OP}$ make an initial angle $\\phi$ with the positive $x$-axis at time $t = 0$.
- At time $t$, the angle made with the $x$-axis is:
  $$\\theta(t) = \\omega t + \\phi$$

#### Projection on the $x$-Axis (Horizontal Diameter):
Drop a perpendicular from particle $P$ onto the horizontal $x$-axis:
$$x(t) = A \\cos(\\omega t + \\phi)$$
This is precisely the equation of Simple Harmonic Motion!

#### Projection on the $y$-Axis (Vertical Diameter):
Drop a perpendicular from particle $P$ onto the vertical $y$-axis:
$$y(t) = A \\sin(\\omega t + \\phi)$$
This also represents identical Simple Harmonic Motion, phase-shifted by $\\pi/2$ radians ($90^\\circ$).

### 3. Physical Equivalence of Parameters
- **Radius of the Reference Circle ($A$)** $\\iff$ **Amplitude of SHM ($A$)**.
- **Constant Angular Speed of Circle ($\\omega$)** $\\iff$ **Angular Frequency of SHM ($\\omega$)**.
- **Angular Position $\\theta(t) = \\omega t + \\phi$** $\\iff$ **Phase of SHM**.
- **Initial Angle $\\phi$** $\\iff$ **Initial Phase / Epoch of SHM**.
- **One Complete Revolution ($2\\pi$ radians)** $\\iff$ **One Complete Oscillation Period ($T = \\frac{2\\pi}{\\omega}$)**.

### 4. Worked Board Problem
**Problem**: A particle executes SHM of amplitude $5 \\text{ cm}$ and time period $6 \\text{ s}$. At $t = 0$, the particle is at $x = +5 \\text{ cm}$ (positive extreme). Write the equation of motion.
- **Solution**:
  - Amplitude $A = 5 \\text{ cm} = 0.05 \\text{ m}$.
  - Angular frequency $\\omega = \\frac{2\\pi}{T} = \\frac{2\\pi}{6} = \\frac{\\pi}{3} \\text{ rad/s}$.
  - General equation: $x(t) = A \\cos(\\omega t + \\phi)$.
  - At $t = 0, x = +A$:
    $$A = A \\cos(\\phi) \\implies \\cos(\\phi) = 1 \\implies \\phi = 0$$
  - Equation of motion:
    $$x(t) = 5 \\cos\\left(\\frac{\\pi}{3} t\\right) \\text{ cm}$$""",
            "svg_code": shm_svg,
            
            
            "concept_questions": [
                {
                    "question": "What is the projection of a particle moving uniformly along a circle onto its diameter?",
                    "options": [
                        "(Recommended) Pure Simple Harmonic Motion (SHM)",
                        "Uniform linear motion at constant velocity",
                        "Constant accelerated motion under gravity",
                        "Parabolic projectile motion"
                    ],
                    "correct_answer": "(Recommended) Pure Simple Harmonic Motion (SHM)",
                    "explanation": "Projecting position vector r = A[cos(ωt + φ) i + sin(ωt + φ) j] onto any diameter yields x(t) = A cos(ωt + φ), which is the exact definition of SHM."
                }
            ]
        },

        # Module 79
        {
            "order_index": 79,
            "chapter_number": 13,
            "title": "Velocity, Acceleration & Force Law for Simple Harmonic Motion",
            "term": "Final-Term Examination",
            "unit": "Unit X: Oscillations and Waves",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 13: Oscillations
## Module 79: Velocity, Acceleration & Force Law for Simple Harmonic Motion

### 1. Velocity in Simple Harmonic Motion
Given the displacement relation:
$$x(t) = A \\cos(\\omega t + \\phi)$$
Velocity is the time rate of change of displacement:
$$v(t) = \\frac{dx}{dt} = \\frac{d}{dt}[A \\cos(\\omega t + \\phi)] = -\\omega A \\sin(\\omega t + \\phi)$$
Using the trigonometric identity $\\sin\\theta = \\pm\\sqrt{1 - \\cos^2\\theta}$:
$$v = -\\omega A \\sqrt{1 - \\frac{x^2}{A^2}} = \\pm \\omega \\sqrt{A^2 - x^2}$$

#### Analysis of Velocity:
- **At Mean Position ($x = 0$)**:
  $$v_{\\text{max}} = \\pm \\omega A$$
  The particle travels fastest as it flies through its equilibrium center!
- **At Extreme Positions ($x = \\pm A$)**:
  $$v = 0$$
  The particle momentarily comes to rest as it reverses direction.

### 2. Acceleration in Simple Harmonic Motion
Acceleration is the time derivative of velocity:
$$a(t) = \\frac{dv}{dt} = \\frac{d}{dt}[-\\omega A \\sin(\\omega t + \\phi)] = -\\omega^2 A \\cos(\\omega t + \\phi)$$
Since $x(t) = A \\cos(\\omega t + \\phi)$:
$$a(t) = -\\omega^2 x(t)$$

#### Analysis of Acceleration:
- **At Mean Position ($x = 0$)**:
  $$a = 0$$
- **At Extreme Positions ($x = \\pm A$)**:
  $$a_{\\text{max}} = \\mp \\omega^2 A$$
  Acceleration is maximum at the extremes, pointing directly back toward the center!

### 3. Phase Relationships Between $x, v,$ and $a$
- **Displacement**: $x = A \\cos(\\omega t)$
- **Velocity**: $v = \\omega A \\cos\\left(\\omega t + \\frac{\\pi}{2}\\right)$
  $\\implies$ **Velocity leads displacement by a phase angle of $\\frac{\\pi}{2} \\text{ rad}$ ($90^\\circ$)**.
- **Acceleration**: $a = \\omega^2 A \\cos(\\omega t + \\pi)$
  $\\implies$ **Acceleration leads displacement by a phase angle of $\\pi \\text{ rad}$ ($180^\\circ$)** (completely in opposite phase!).

### 4. Force Law for SHM
By Newton's Second Law:
$$F = m a = m(-\\omega^2 x) = -(m \\omega^2) x$$
Defining force constant $k = m \\omega^2$:
$$F = -k x$$
where:
$$\\omega = \\sqrt{\\frac{k}{m}} \\implies T = \\frac{2\\pi}{\\omega} = 2\\pi \\sqrt{\\frac{m}{k}}$$
The restoring force is linear and proportional to negative displacement.""",
            "svg_code": shm_svg,
            
            
            "concept_questions": [
                {
                    "question": "What is the phase difference between velocity and acceleration in Simple Harmonic Motion?",
                    "options": [
                        "(Recommended) π / 2 radians (90°)",
                        "π radians (180°)",
                        "Zero (they are in phase)",
                        "2π radians (360°)"
                    ],
                    "correct_answer": "(Recommended) π / 2 radians (90°)",
                    "explanation": "Velocity leads displacement by π/2, while acceleration leads displacement by π. Therefore, the phase difference between velocity and acceleration is π - π/2 = π/2 radians (90°)."
                }
            ]
        },

        # Module 80
        {
            "order_index": 80,
            "chapter_number": 13,
            "title": "Energy in SHM: Kinetic, Potential & Conservation of Mechanical Energy",
            "term": "Final-Term Examination",
            "unit": "Unit X: Oscillations and Waves",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 13: Oscillations
## Module 80: Energy in SHM: Kinetic, Potential & Conservation of Mechanical Energy

### 1. Kinetic Energy ($K$) in SHM
The kinetic energy of an oscillating mass $m$ with velocity $v$ is:
$$K = \\frac{1}{2} m v^2 = \\frac{1}{2} m \\omega^2 (A^2 - x^2) = \\frac{1}{2} k (A^2 - x^2)$$
As a function of time:
$$K(t) = \\frac{1}{2} m \\omega^2 A^2 \\sin^2(\\omega t + \\phi) = \\frac{1}{2} k A^2 \\sin^2(\\omega t + \\phi)$$
- At mean position ($x = 0$): $K = K_{\\text{max}} = \\frac{1}{2} k A^2$.
- At extreme positions ($x = \\pm A$): $K = 0$.

### 2. Potential Energy ($U$) in SHM
The work done by an external agent against the restoring force $F = -kx$ in displacing the mass from $0$ to $x$:
$$U = \\int_0^x -F_{\\text{restoring}} \\, dx' = \\int_0^x k x' \\, dx' = \\frac{1}{2} k x^2$$
Using $x(t) = A \\cos(\\omega t + \\phi)$:
$$U(t) = \\frac{1}{2} k A^2 \\cos^2(\\omega t + \\phi)$$
- At mean position ($x = 0$): $U = 0$ (assuming potential energy zero at equilibrium).
- At extreme positions ($x = \\pm A$): $U = U_{\\text{max}} = \\frac{1}{2} k A^2$.

### 3. Total Mechanical Energy ($E$)
Summing kinetic and potential energies:
$$E = K + U = \\frac{1}{2} k (A^2 - x^2) + \\frac{1}{2} k x^2 = \\frac{1}{2} k A^2$$
In terms of time:
$$E(t) = \\frac{1}{2} k A^2 [\\sin^2(\\omega t + \\phi) + \\cos^2(\\omega t + \\phi)] = \\frac{1}{2} k A^2 = \\text{constant}$$
> **The Energy Conservation Invariant in SHM**:
> *The total mechanical energy of an undamped simple harmonic oscillator is strictly constant and proportional to the square of its amplitude ($E \\propto A^2$ and $E \\propto \\omega^2$)!*

### 4. Average Energies Over One Full Cycle
- Average Kinetic Energy:
  $$\\langle K \\rangle = \\frac{1}{T} \\int_0^T K(t) \\, dt = \\frac{1}{2} k A^2 \\langle \\sin^2 \\rangle = \\frac{1}{4} k A^2 = \\frac{1}{2} E$$
- Average Potential Energy:
  $$\\langle U \\rangle = \\frac{1}{T} \\int_0^T U(t) \\, dt = \\frac{1}{2} k A^2 \\langle \\cos^2 \\rangle = \\frac{1}{4} k A^2 = \\frac{1}{2} E$$
- Over one cycle, energy is shared equally: exactly $50\\%$ average kinetic energy and $50\\%$ average potential energy!

### 5. Frequency of Energy Oscillations
While displacement, velocity, and acceleration oscillate with frequency $\\nu$ (period $T$), the energies $K(t)$ and $U(t)$ contain $\\sin^2(\\omega t) = \\frac{1 - \\cos(2\\omega t)}{2}$.
Hence:
$$\\text{Frequency of Kinetic / Potential Energy Oscillation} = 2\\nu$$
Energy oscillates **twice as fast** as the mechanical particle itself!""",
            "svg_code": shm_svg,
            
            
            "concept_questions": [
                {
                    "question": "At what displacement from the mean position is the kinetic energy of a simple harmonic oscillator equal to its potential energy?",
                    "options": [
                        "(Recommended) x = ± A / √2 (approximately 0.707 A)",
                        "x = ± A / 2",
                        "x = 0",
                        "x = ± A"
                    ],
                    "correct_answer": "(Recommended) x = ± A / √2 (approximately 0.707 A)",
                    "explanation": "Setting K = U: 1/2 k (A^2 - x^2) = 1/2 k x^2 => A^2 - x^2 = x^2 => 2 x^2 = A^2 => x = ± A / √2."
                }
            ]
        },

        # Module 81
        {
            "order_index": 81,
            "chapter_number": 13,
            "title": "Oscillating Systems: Loaded Springs & The Simple Pendulum",
            "term": "Final-Term Examination",
            "unit": "Unit X: Oscillations and Waves",
            "cadence_stage": "Stage 1 to 4: Real-Life Intuition, Mathematical Formulation & Socratic Derivation",
            "content": """# Chapter 13: Oscillations
## Module 81: Oscillating Systems: Loaded Springs & The Simple Pendulum

### 1. The Spring-Mass System
Consider a block of mass $m$ attached to a massless ideal spring of spring constant $k$ resting on a frictionless horizontal floor:
- Restoring force when pulled by displacement $x$:
  $$F = -k x$$
- By Newton's Second Law:
  $$m \\frac{d^2x}{dt^2} = -k x \\implies \\frac{d^2x}{dt^2} + \\left(\\frac{k}{m}\\right)x = 0$$
- Angular frequency and Time Period:
  $$\\omega = \\sqrt{\\frac{k}{m}} \\implies T = 2\\pi \\sqrt{\\frac{m}{k}}$$

#### Vertical Spring:
When hung vertically, gravity produces an initial static extension $x_0 = \\frac{mg}{k}$. Oscillating about this new equilibrium position yields identical restoring dynamics:
$$T = 2\\pi \\sqrt{\\frac{m}{k}} = 2\\pi \\sqrt{\\frac{x_0}{g}}$$

#### Spring Combinations:
1. **Series Combination**: Two springs ($k_1, k_2$) end-to-end:
   $$\\frac{1}{k_{\\text{eff}}} = \\frac{1}{k_1} + \\frac{1}{k_2} \\implies T = 2\\pi \\sqrt{\\frac{m(k_1 + k_2)}{k_1 k_2}}$$
2. **Parallel Combination**: Side-by-side:
   $$k_{\\text{eff}} = k_1 + k_2 \\implies T = 2\\pi \\sqrt{\\frac{m}{k_1 + k_2}}$$

### 2. The Simple Pendulum
A simple pendulum consists of a point mass (bob) of mass $m$ suspended from a rigid support by an unstretchable, massless string of length $L$.
- Displace the bob by small angle $\\theta$:
  Restoring torque about suspension point $O$:
  $$\\tau = -m g L \\sin\\theta$$
- Moment of inertia of bob about $O$:
  $$I = m L^2$$
- Equation of rotational motion:
  $$\\tau = I \\alpha \\implies m L^2 \\frac{d^2\\theta}{dt^2} = -m g L \\sin\\theta$$
  $$\\frac{d^2\\theta}{dt^2} + \\left(\\frac{g}{L}\\right) \\sin\\theta = 0$$

#### Small Angle Approximation ($\\sin\\theta \\approx \\theta$ for $\\theta < 10^\\circ$):
$$\\frac{d^2\\theta}{dt^2} + \\left(\\frac{g}{L}\\right) \\theta = 0$$
This is the standard differential equation of SHM!
$$\\omega = \\sqrt{\\frac{g}{L}} \\implies T = 2\\pi \\sqrt{\\frac{L}{g}}$$

### 3. Key Invariants of Simple Pendulum
1. **Mass Independence**: $T$ is completely independent of the mass $m$ or material of the bob.
2. **Length Dependence**: $T \\propto \\sqrt{L}$.
3. **Gravity Dependence**: $T \\propto \\frac{1}{\\sqrt{g}}$. At the center of the Earth or in a free-falling elevator ($g_{\\text{eff}} = 0$), $T \\to \\infty$ (the pendulum stops swinging).
4. **Seconds Pendulum**: A pendulum whose half-period is $1 \\text{ second}$ ($T = 2.0 \\text{ s}$).
   $$L = \\frac{g T^2}{4\\pi^2} = \\frac{9.8 \\times 4}{4 \\times (3.1416)^2} \\approx 0.993 \\text{ m} \\approx 1 \\text{ meter}$$""",
            "svg_code": shm_svg,
            
            
            "concept_questions": [
                {
                    "question": "What happens to the time period of a simple pendulum if it is taken to the Moon, where acceleration due to gravity is 1/6th that of Earth?",
                    "options": [
                        "(Recommended) The time period increases by a factor of √6",
                        "The time period decreases by a factor of 6",
                        "The time period remains unchanged",
                        "The pendulum stops swinging completely"
                    ],
                    "correct_answer": "(Recommended) The time period increases by a factor of √6",
                    "explanation": "Since T = 2π √(L/g), if g decreases by a factor of 6, T scales as 1/√(1/6) = √6 times larger (swings much slower)."
                }
            ]
        },

        # Module 82
        {
            "order_index": 82,
            "chapter_number": 13,
            "title": "Comprehensive NCERT Exercises 13.1 to 13.22 Detailed Step-by-Step Solver",
            "term": "Final-Term Examination",
            "unit": "Unit X: Oscillations and Waves",
            "cadence_stage": "Stage 5 to 6: Socratic Check & Exam-Topper Numerical Practice",
            "content": """# Chapter 13: Oscillations
## Module 82: Comprehensive NCERT Exercises 13.1 to 13.22 Detailed Step-by-Step Solver

### Exercise 13.1
**Question**: Which of the following examples represent periodic motion?
1. A swimmer completing one return trip from one bank of a river to the other and back.
2. A freely suspended bar magnet displaced from its N-S direction and released.
3. A hydrogen molecule rotating about its center of mass.
4. An arrow released from a bow.
- **Answers**:
  1. Non-periodic: Swimmer may not repeat the return trip at regular constant intervals.
  2. Periodic (and oscillatory): The restoring magnetic torque causes periodic oscillation about the Earth's magnetic meridian.
  3. Periodic (rotational): Molecular rotation repeats after fixed time period $T$.
  4. Non-periodic: The arrow flies forward and never returns.

---

### Exercise 13.2
**Question**: Which of the following examples represent (nearly) simple harmonic motion and which represent periodic but not simple harmonic motion?
1. The rotation of earth about its axis.
2. Motion of an oscillating mercury column in a U-tube.
3. Motion of a ball bearing inside a smooth curved bowl when released from a point slightly above the lower-most point.
4. General vibrations of a polyatomic molecule about its equilibrium position.
- **Answers**:
  1. Periodic but NOT SHM: Rotational motion, not to-and-fro about a mean point with restoring force $F = -kx$.
  2. SHM: The restoring pressure difference $2h\\rho g A$ is directly proportional to displacement $h$.
  3. SHM: For small angular displacements, restoring force component along tangent is $-mg\\sin\\theta \\approx -mg\\frac{x}{R}$, satisfying $F \\propto -x$.
  4. Periodic, composed of a superposition of several simple harmonic normal modes.

---

### Exercise 13.3
**Question**: A particle is in linear simple harmonic motion between two points $A$ and $B$, $10 \\text{ cm}$ apart. Take the direction from $A$ to $B$ as positive. Give the signs of position, velocity, and acceleration on the particle when:
1. At the end $A$.
2. At the end $B$.
3. At the mid-point of $AB$ going towards $A$.
4. At $2 \\text{ cm}$ away from $B$ going towards $A$.
- **Answers**:
  - Let midpoint $O$ be origin ($x = 0$). Then $A$ is at $x = -5 \\text{ cm}$ and $B$ is at $x = +5 \\text{ cm}$.
  1. At $A$: $x < 0$ (negative), $v = 0$ (zero), $a = -\\omega^2(-5) > 0$ (positive, directed towards $O$).
  2. At $B$: $x > 0$ (positive), $v = 0$ (zero), $a = -\\omega^2(+5) < 0$ (negative, directed towards $O$).
  3. At midpoint towards $A$: $x = 0$ (zero), $v < 0$ (negative), $a = 0$ (zero).
  4. At $2 \\text{ cm}$ from $B$ towards $A$: $x = +3 \\text{ cm} > 0$ (positive), $v < 0$ (negative, moving towards left), $a = -\\omega^2(+3) < 0$ (negative).

---

### Exercise 13.4
**Question**: A simple pendulum of length $1 \\text{ m}$ has a bob of mass $100 \\text{ g}$. It oscillates with an amplitude of $4 \\text{ cm}$. Find:
1. Maximum acceleration of the bob.
2. Maximum tension in the string ($g = 9.8 \\text{ m/s}^2$).
- **Solution**:
  - $L = 1 \\text{ m}, m = 0.1 \\text{ kg}, A = 0.04 \\text{ m}$.
  - Angular frequency $\\omega = \\sqrt{\\frac{g}{L}} = \\sqrt{9.8} \\approx 3.13 \\text{ rad/s}$.
  1. Maximum acceleration:
     $$a_{\\text{max}} = \\omega^2 A = \\frac{g}{L} A = 9.8 \\times 0.04 = 0.392 \\text{ m/s}^2$$
  2. Maximum tension occurs at the lowest point (mean position):
     $$T_{\\text{max}} = mg + \\frac{m v_{\\text{max}}^2}{L} = mg + m \\omega^2 A^2 / L$$
     $$v_{\\text{max}} = \\omega A = 3.13 \\times 0.04 = 0.1252 \\text{ m/s}$$
     $$T_{\\text{max}} = (0.1 \\times 9.8) + \\frac{0.1 \\times (0.1252)^2}{1} = 0.98 + 0.00157 \\approx 0.9816 \\text{ N}$$
- **Boxed Answer**: $a_{\\text{max}} = **0.392 \\text{ m/s}^2$**, $T_{\\text{max}} = **0.982 \\text{ N}$**.""",
            "svg_code": shm_svg,
            
            
            "concept_questions": [
                {
                    "question": "Where does the maximum tension in the string of an oscillating simple pendulum occur?",
                    "options": [
                        "(Recommended) At the lowest point (mean position), where both gravity and centripetal force act in the same downward direction",
                        "At the extreme positions",
                        "Halfway between mean and extreme",
                        "Tension remains constant throughout the swing"
                    ],
                    "correct_answer": "(Recommended) At the lowest point (mean position), where both gravity and centripetal force act in the same downward direction",
                    "explanation": "At the lowest point, speed is maximum (v_max = ωA). The string must support both the weight mg and provide centripetal force m v^2 / L, making tension T = mg + m v_max^2 / L maximum."
                }
            ]
        }
    ]
