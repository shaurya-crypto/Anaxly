"""
ch1_units_and_measurements.py
CBSE Class 11 Physics - Chapter 1: Units and Measurements
Part 1 (Mid-Term Syllabus, Unit I: Physical World and Measurement)
Target Pacing: November 12, 2026 to November 16, 2026 (5 Modules, 5 Days)
"""

import sys
import os
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

import svg_builder_physics11 as sb

CURRICULUM_ID = "c11_phy_ch01_units_measurements"
CLASS_LEVEL = "Class 11"
BOARD = "CBSE"
SUBJECT = "Physics"

def get_modules():
    modules = []

    # -------------------------------------------------------------
    # MODULE 1: Systems of Units & Base SI Units
    # Date: 2026-11-12
    # -------------------------------------------------------------
    mod1_svg = sb.build_measurement_apparatus_svg(apparatus="vernier", title="Vernier Callipers: Least Count & Measurement", caption="LC = 1 MSD - 1 VSD = 0.1 mm = 0.01 cm")
    modules.append({
        "order_index": 1,
        "title": "Systems of Units, SI Base Quantities & Standards of Measurement",
        "description": "Comprehensive study of physical quantities, fundamental versus derived units, evolution of systems (CGS, MKS, FPS), the international SI system, and 7 base SI standards.",
        "target_completion_date": "2026-11-12",
        "syllabus_pacing": "Day 1 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Need for measurement and definition of physical quantities",
            "Fundamental vs derived physical quantities and units",
            "Historical systems: CGS (Gaussian), MKS, FPS (British engineering)",
            "The International System of Units (SI): 7 base units and 2 supplementary units",
            "Operational definitions of Metre, Kilogram, Second, Ampere, Kelvin, Mole, Candela",
            "Measurement of large distances: Parallax method and astronomical units"
        ],
        "key_concepts": [
            "Fundamental vs Derived Quantities",
            "The 7 SI Base Units & Supplementary Units (Radian & Steradian)",
            "Parallax Method for Astronomical Distances",
            "Measurement of Very Small Distances & Molecular Sizes"
        ],
        "success_criteria": [
            "Define physical quantity and distinguish fundamental from derived units with SI standards",
            "State the SI base units, symbols, and supplementary plane/solid angle units (rad, sr)",
            "Apply the parallax formula b = D θ to determine planetary distances and angular diameters",
            "Estimate molecular sizes of oleic acid monolayers using volumetric dilutions"
        ],
        "chapter_notes": """# CHAPTER 1: UNITS AND MEASUREMENTS
## MODULE 1: Systems of Units & Standards of Measurement

### 1. The Nature of Measurement in Physics
Physics is a quantitative experimental science. Any quantity that can be measured and in terms of which the laws of physics can be described is called a **physical quantity**.
Every measurement consists of two essential parts:
$$\\text{Magnitude of physical quantity } Q = n \\times u$$
where $n$ is the numerical value (number of times the unit is contained) and $u$ is the chosen standard unit. Since the magnitude $Q$ is constant:
$$n_1 u_1 = n_2 u_2 \\implies n \\propto \\frac{1}{u}$$
A larger unit yields a smaller numerical measure.

### 2. Fundamental vs. Derived Units
- **Fundamental (Base) Quantities**: Independent quantities that cannot be defined in terms of other quantities (Length, Mass, Time, etc.).
- **Derived Quantities**: Quantities that can be expressed as mathematical combinations (products/powers) of fundamental quantities (Velocity = Length/Time, Force = Mass × Acceleration).

### 3. The 7 SI Base Units and 2 Supplementary Units
Established by the General Conference on Weights and Measures (CGPM) in 1971:
1. **Length**: metre (m) - defined via speed of light in vacuum ($c = 299,792,458\\text{ m/s}$).
2. **Mass**: kilogram (kg) - defined via Planck's constant ($h = 6.62607015 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$).
3. **Time**: second (s) - defined via cesium-133 hyperfine transition frequency ($9,192,631,770\\text{ Hz}$).
4. **Electric Current**: ampere (A) - defined via elementary charge ($e = 1.602176634 \\times 10^{-19}\\text{ C}$).
5. **Thermodynamic Temperature**: kelvin (K) - defined via Boltzmann constant ($k_B = 1.380649 \\times 10^{-23}\\text{ J/K}$).
6. **Amount of Substance**: mole (mol) - defined via Avogadro constant ($N_A = 6.02214076 \\times 10^{23}\\text{ mol}^{-1}$).
7. **Luminous Intensity**: candela (cd) - monochromatic radiation of frequency $540 \\times 10^{12}\\text{ Hz}$.

**Supplementary Units**:
- **Plane Angle ($d\\theta$)**: $\\text{radian (rad)} = \\frac{ds}{r}$. Total angle in circle $= 2\\pi\\text{ rad} = 360^\\circ$.
- **Solid Angle ($d\\Omega$)**: $\\text{steradian (sr)} = \\frac{dA}{r^2}$. Total solid angle subtended by sphere $= 4\\pi\\text{ sr}$.

### 4. Measurement of Astronomical Distances: The Parallax Method
Parallax is the apparent shift in the position of an object relative to a distant background when viewed from two separated observation points $A$ and $B$.
- Let baseline $AB = b$.
- Parallactic angle subtended at distant planet $P$ is $\\theta$ (in radians).
- Since distance $D \\gg b$, the arc $b \\approx D \\theta$:
$$D = \\frac{b}{\\theta}$$
To determine planetary diameter $d$, observer measures angular diameter $\\alpha$ subtended at Earth:
$$d = D \\alpha$$
""",
        "worked_examples": [
            {
                "problem": "Textbook Example: Calculate the angle of (a) 1° (degree), (b) 1' (minute of arc), and (c) 1\" (second of arc) in radians. Use 360° = 2π rad, 1° = 60', and 1' = 60\".",
                "given": "360° = 2π rad, 1° = 60', 1' = 60\".",
                "formula": "θ(rad) = θ(deg) × (π / 180)",
                "substitution": "(a) 1° = π/180 rad = 3.14159 / 180; (b) 1' = (1/60)°; (c) 1\" = (1/3600)°.",
                "calculation": "(a) 1° = 1.745 × 10⁻² rad; (b) 1' = 1.745 × 10⁻² / 60 = 2.908 × 10⁻⁴ rad; (c) 1\" = 2.908 × 10⁻⁴ / 60 = 4.848 × 10⁻⁶ rad.",
                "finalAnswer": "1° = 1.75 × 10⁻² rad, 1' = 2.91 × 10⁻⁴ rad, 1\" = 4.85 × 10⁻⁶ rad",
                "unit": "rad",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            },
            {
                "problem": "Textbook Example: A person wishes to measure the distance of a nearby tower from him. He stands at a point A in front of the tower C and spots a very distant object O in line with AC. He then walks perpendicular to AC up to B by a distance of 100 m, and looks at O and C again. Since O is very distant, the direction BO is practically the same as AO; but he finds the line of sight of C shifted from the original direction by an angle θ = 40° (θ is known as 'parallax'). Estimate the distance of the tower C from his original position A.",
                "given": "Baseline AB = 100 m, parallax angle θ = 40°.",
                "formula": "tan θ = AC / AB => AC = AB / tan θ  or in right triangle: tan 40° = AB / AC => AC = AB / tan 40°",
                "substitution": "AC = 100 m / tan 40° = 100 / 0.8391",
                "calculation": "AC = 119.17 m ≈ 119 m.",
                "finalAnswer": "Distance of tower AC = 119 m",
                "unit": "m",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            },
            {
                "problem": "Textbook Example: The moon is observed from two diametrically opposite points A and B on Earth. The angle θ subtended at the moon by the two directions of observation is 1° 54'. Given the diameter of the Earth to be about 1.276 × 10⁷ m, compute the distance of the moon from the Earth.",
                "given": "Baseline b = 1.276 × 10⁷ m, Parallactic angle θ = 1° 54' = 114' = 114 × 2.908 × 10⁻⁴ rad = 3.315 × 10⁻² rad.",
                "formula": "Distance D = b / θ",
                "substitution": "D = (1.276 × 10⁷ m) / (3.315 × 10⁻² rad)",
                "calculation": "D = 3.849 × 10⁸ m ≈ 3.84 × 10⁸ m.",
                "finalAnswer": "Distance of moon D = 3.84 × 10⁸ m",
                "unit": "m",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            }
        ],
        "common_misconceptions": [
            "Confusing radian with degree: All physics formulas involving angular displacement (θ = s/r) require θ strictly in RADIANS, never degrees!",
            "Assuming SI base units are immutable physical artifacts: In 2019, SI units were redefined strictly in terms of universal physical constants (c, h, e, kB, NA), discarding the physical iridium-platinum cylinder in Paris."
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod1_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Fundamental vs Derived Quantities",
                    "diagram_title": "SI Units Hierarchy & Dimensional Independence",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "SI base units standard physical quantities metrology chart",
                    "video_search_query": "SI base units explanation definition metrology",
                    "what_to_make": "Hierarchical diagram showing 7 base units feeding into mechanical, thermodynamic and electromagnetic derived units",
                    "what_to_explain": "Explain why mass, length, and time are mutually independent base dimensions",
                    "timing_and_cue": "Step 1 (Intuition)"
                },
                {
                    "concept_index": 1,
                    "concept_title": "The 7 SI Base Units & Supplementary Units",
                    "diagram_title": "Solid & Plane Angle Geometry",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "solid angle steradian plane angle radian geometry diagram",
                    "video_search_query": "radian and steradian supplementary units physics",
                    "what_to_make": "Sphere sector illustrating solid angle dOmega = dA / r^2 and circle sector for dTheta = ds / r",
                    "what_to_explain": "Contrast dimensionless supplementary units with standard dimensional units",
                    "timing_and_cue": "Step 2 (Definition)"
                },
                {
                    "concept_index": 2,
                    "concept_title": "Parallax Method for Astronomical Distances",
                    "diagram_title": "Parallax Triangle Geometry for Moon & Planets",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "astronomical parallax baseline angle distance physics diagram",
                    "video_search_query": "parallax method measuring distance to moon stars physics",
                    "what_to_make": "Earth diameter baseline AB forming slender isosceles triangle with distant celestial object",
                    "what_to_explain": "Show how small angles allow the arc-length approximation b = D * theta",
                    "timing_and_cue": "Step 3 (Numerical Application)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "Why cannot the units of velocity and force be chosen as fundamental units in classical mechanics alongside length and time?",
                            "ideal_answer": "Because velocity (Length/Time) and force (Mass × Length/Time²) are algebraically derived from length, mass, and time; fundamental units must be mutually independent.",
                            "socratic_hint": "Check whether velocity can be defined using length and time alone.",
                            "type": "Conceptual"
                        },
                        {
                            "question": "What is the difference between plane angle and solid angle in terms of dimensions and SI units?",
                            "ideal_answer": "Both are dimensionless quantities (M⁰L⁰T⁰). Plane angle is subtended in 2D by an arc and measured in radians (rad); solid angle is subtended in 3D by an area and measured in steradians (sr).",
                            "socratic_hint": "Think about ratio of length to length versus area to radius squared.",
                            "type": "Checkpoint"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 2: Errors in Measurement & Error Propagation
    # Date: 2026-11-13
    # -------------------------------------------------------------
    mod2_svg = sb.build_measurement_apparatus_svg(apparatus="screw_gauge", title="Micrometer Screw Gauge: Pitch & Error", caption="Zero Error = ±(HSR × LC); Correct Reading = Measured - Zero Error")
    modules.append({
        "order_index": 2,
        "title": "Errors in Measurement: Systematic, Random & Mathematical Error Propagation",
        "description": "Comprehensive analysis of precision, accuracy, systematic errors, random errors, absolute error, relative error, percentage error, and error propagation rules for sum, difference, product, quotient, and powers.",
        "target_completion_date": "2026-11-13",
        "syllabus_pacing": "Day 2 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Distinction between Accuracy and Precision with target analogies",
            "Systematic errors: Instrumental, imperfection in experimental technique, personal",
            "Random errors and statistical elimination via arithmetic mean",
            "Absolute error (Δa_i), Mean absolute error (Δa_mean)",
            "Relative error and Percentage error formulas",
            "Combination/Propagation of errors in addition and subtraction: ΔZ = ΔA + ΔB",
            "Combination/Propagation of errors in multiplication and division: ΔZ/Z = ΔA/A + ΔB/B",
            "Error in quantity raised to a power: Z = A^p B^q / C^r => ΔZ/Z = p(ΔA/A) + q(ΔB/B) + r(ΔC/C)"
        ],
        "key_concepts": [
            "Accuracy vs Precision",
            "Absolute, Relative & Percentage Errors",
            "Error Propagation in Sums & Differences (Max Absolute Error)",
            "Error Propagation in Products, Quotients & Powers (Max Relative Error)"
        ],
        "success_criteria": [
            "Distinguish accuracy (closeness to true value) from precision (resolution of measuring tool)",
            "Compute mean value, absolute errors, mean absolute error, and percentage error for repeated trials",
            "Apply the power rule ΔZ/Z = Σ |p_i| (ΔA_i / A_i) to solve board-exam experimental numericals",
            "State why errors always add up to find the maximum possible uncertainty"
        ],
        "chapter_notes": """# CHAPTER 1: UNITS AND MEASUREMENTS
## MODULE 2: Errors in Measurement & Error Propagation

### 1. Accuracy vs Precision
- **Accuracy**: Measure of how close the measured value is to the true or accepted standard value.
- **Precision**: Measure of the resolution or limit to which the physical quantity is measured by the instrument (determined by the instrument's Least Count).
*Note*: A measurement can be highly precise (e.g. 3.456 cm with small least count) but inaccurate if there is a zero error.

### 2. Classification of Errors
1. **Systematic Errors**: Errors that tend to occur in one direction (consistently positive or consistently negative).
   - *Instrumental errors*: Zero error of vernier/screw gauge.
   - *Imperfection in experimental technique*: Thermometer in armpit measuring slightly less than body temperature.
   - *Personal errors*: Parallax error due to eye position not perpendicular to scale.
   *Remedy*: Calibrate instruments, apply zero correction, improve procedure.
2. **Random Errors**: Errors that occur irregularly due to unpredictable fluctuations in experimental conditions (voltage fluctuations, temperature drift, mechanical vibrations).
   *Remedy*: Take arithmetic mean of $n$ observations:
   $$a_{\\text{mean}} = \\frac{1}{n} \\sum_{i=1}^n a_i$$
   The standard error decreases as $1/\\sqrt{n}$.
3. **Least Count Error**: The smallest value that can be measured by the measuring instrument.

### 3. Mathematical Formulation of Errors
For measurements $a_1, a_2, \\dots, a_n$:
1. **True Value**: Best estimate is arithmetic mean $a_{\\text{mean}}$.
2. **Absolute Error**: $\\Delta a_i = |a_i - a_{\\text{mean}}|$
3. **Mean Absolute Error**:
   $$\\Delta a_{\\text{mean}} = \\frac{1}{n} \\sum_{i=1}^n |\\Delta a_i|$$
   Final reported value: $a = a_{\\text{mean}} \\pm \\Delta a_{\\text{mean}}$
4. **Relative Error (Fractional Error)**:
   $$\\text{Relative Error} = \\frac{\\Delta a_{\\text{mean}}}{a_{\\text{mean}}}$$
5. **Percentage Error**:
   $$\\delta a = \\left(\\frac{\\Delta a_{\\text{mean}}}{a_{\\text{mean}}}\\right) \\times 100\\%$$

### 4. Propagation of Errors (Combination of Errors)
To find the **maximum possible error**:
1. **Sum and Difference ($Z = A \\pm B$)**:
   $$\\Delta Z = \\Delta A + \\Delta B$$
   *Law*: When two quantities are added or subtracted, the absolute error in the final result is the sum of the absolute errors in the individual quantities.
2. **Product and Quotient ($Z = A \\times B$ or $Z = A / B$)**:
   $$\\frac{\\Delta Z}{Z} = \\frac{\\Delta A}{A} + \\frac{\\Delta B}{B}$$
   *Law*: When two quantities are multiplied or divided, the fractional error in the final result is the sum of the fractional errors in the individual quantities.
3. **Measured Quantity Raised to a Power ($Z = \\frac{A^p B^q}{C^r}$)**:
   $$\\frac{\\Delta Z}{Z} = p \\left(\\frac{\\Delta A}{A}\\right) + q \\left(\\frac{\\Delta B}{B}\\right) + r \\left(\\frac{\\Delta C}{C}\\right)$$
   *Percentage error*:
   $$\\% \\text{ error in } Z = p (\\% A) + q (\\% B) + r (\\% C)$$
   *Examiner Invariant*: Notice the terms are strictly added with positive signs, even though $C^r$ is in the denominator, because we evaluate the worst-case maximum possible error!
""",
        "worked_examples": [
            {
                "problem": "Textbook Example: Two resistances R₁ = (100 ± 3) Ω and R₂ = (200 ± 4) Ω are connected (a) in series, (b) in parallel. Find the equivalent resistance of the (a) series combination, (b) parallel combination. Use for (a) the relation R = R₁ + R₂ and for (b) 1/R' = 1/R₁ + 1/R₂ and ΔR'/R'² = ΔR₁/R₁² + ΔR₂/R₂².",
                "given": "R₁ = (100 ± 3) Ω, R₂ = (200 ± 4) Ω.",
                "formula": "(a) R_s = R₁ + R₂, ΔR_s = ΔR₁ + ΔR₂; (b) R_p = (R₁ R₂) / (R₁ + R₂), ΔR_p = R_p² [ΔR₁/R₁² + ΔR₂/R₂²].",
                "substitution": "(a) R_s = 100 + 200 = 300 Ω; ΔR_s = 3 + 4 = 7 Ω. (b) R_p = (100 × 200)/(100 + 200) = 20000/300 = 66.7 Ω; ΔR_p = (66.7)² [3/(100)² + 4/(200)²] = 4448.9 [0.0003 + 0.0001] = 4448.9 × 0.0004 = 1.78 Ω ≈ 1.8 Ω.",
                "calculation": "(a) R_s = (300 ± 7) Ω; (b) R_p = (66.7 ± 1.8) Ω.",
                "finalAnswer": "Series R_s = (300 ± 7) Ω; Parallel R_p = (66.7 ± 1.8) Ω",
                "unit": "Ω",
                "has_diagram": True,
                "diagram_svg": mod2_svg
            },
            {
                "problem": "Textbook Example: Find the relative error in Z, if Z = A⁴ B^(1/3) / (C D^(3/2)).",
                "given": "Function Z = A⁴ B^(1/3) / (C D^(3/2)).",
                "formula": "ΔZ / Z = 4 (ΔA / A) + (1/3) (ΔB / B) + (ΔC / C) + (3/2) (ΔD / D)",
                "substitution": "Apply logarithmic differentiation: d(ln Z) = 4 d(ln A) + 1/3 d(ln B) - d(ln C) - 3/2 d(ln D). For maximum error, change all signs to positive.",
                "calculation": "ΔZ / Z = 4 (ΔA / A) + (1/3) (ΔB / B) + (ΔC / C) + (3/2) (ΔD / D).",
                "finalAnswer": "Relative error ΔZ/Z = 4(ΔA/A) + 1/3(ΔB/B) + (ΔC/C) + 3/2(ΔD/D)",
                "unit": "fraction",
                "has_diagram": True,
                "diagram_svg": mod2_svg
            },
            {
                "problem": "Textbook Example: The period of oscillation of a simple pendulum is T = 2π √(L/g). Measured value of L is 20.0 cm known to 1 mm accuracy and time for 100 oscillations of the pendulum is found to be 90 s using a wrist watch of 1 s resolution. What is the accuracy in the determination of g?",
                "given": "T = 2π √(L/g) => g = 4π² L / T²; L = 20.0 cm = 0.200 m, ΔL = 1 mm = 0.1 cm; Total time t = 90 s for n = 100 oscillations, Δt = 1 s.",
                "formula": "Δg / g = (ΔL / L) + 2 (ΔT / T) = (ΔL / L) + 2 (Δt / t)",
                "substitution": "Δg / g = (0.1 cm / 20.0 cm) + 2 × (1 s / 90 s) = 0.005 + 2 × 0.0111 = 0.005 + 0.0222 = 0.0272",
                "calculation": "% error = 0.0272 × 100% = 2.72% ≈ 3%",
                "finalAnswer": "Accuracy in determination of g = 2.7% (or approx 3%)",
                "unit": "%",
                "has_diagram": True,
                "diagram_svg": mod2_svg
            }
        ],
        "common_misconceptions": [
            "Subtracting errors in division or subtraction: Errors ALWAYS combine additively to calculate the worst-case maximum uncertainty. Never subtract errors!",
            "Forgetting the factor in time period: ΔT/T = Δt/t where t is total time for n oscillations. The resolution of the stopwatch (1 s) is divided by the total time (90 s), NOT the time for one oscillation!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod2_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Accuracy vs Precision",
                    "diagram_title": "Target Analogy: High Precision vs High Accuracy",
                    "diagram_type": "svg",
                    "svg": mod2_svg,
                    "image_search_query": "accuracy vs precision target dartboard science diagram",
                    "video_search_query": "accuracy and precision difference physics animation",
                    "what_to_make": "Four target boards showing combinations of high/low accuracy and high/low precision",
                    "what_to_explain": "Demonstrate that precision reflects reproducibility while accuracy reflects truth",
                    "timing_and_cue": "Step 1 (Intuition)"
                },
                {
                    "concept_index": 1,
                    "concept_title": "Error Propagation in Products, Quotients & Powers",
                    "diagram_title": "Power Rule Uncertainty Scaling Diagram",
                    "diagram_type": "svg",
                    "svg": mod2_svg,
                    "image_search_query": "propagation of errors physics formulas diagram",
                    "video_search_query": "propagation of error power rule simple pendulum physics",
                    "what_to_make": "Bar chart illustrating how exponents amplify percentage uncertainty",
                    "what_to_explain": "Highlight why the quantity with the highest exponent must be measured with highest precision",
                    "timing_and_cue": "Step 3 (Numerical Mastery)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 1,
                    "questions": [
                        {
                            "question": "In an experiment to determine g using T = 2π √(L/g), if the percentage error in length L is 1% and in time period T is 2%, what is the maximum percentage error in g?",
                            "ideal_answer": "Since g = 4π² L / T², the percentage error is %g = (%L) + 2(%T) = 1% + 2(2%) = 5%.",
                            "socratic_hint": "Express g as a formula and apply the power rule for L and T.",
                            "type": "Numerical"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 3: Significant Figures & Rounding Off
    # Date: 2026-11-14
    # -------------------------------------------------------------
    modules.append({
        "order_index": 3,
        "title": "Significant Figures, Rounding-Off Rules & Scientific Notation",
        "description": "Rules for identifying significant digits, handling leading/trailing zeros, scientific exponential notation, rounding off guidelines, and significant figure rules in addition, subtraction, multiplication, and division.",
        "target_completion_date": "2026-11-14",
        "syllabus_pacing": "Day 3 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 50,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Definition of Significant Figures: Reliable digits plus first uncertain digit",
            "Core rules for determining significant figures in whole numbers and decimals",
            "Role of decimal points and non-significant trailing zeros",
            "Eliminating ambiguities using scientific notation (a × 10^b)",
            "Strict rounding-off rules (including even-number rule for digit 5)",
            "Arithmetic operations rule for addition and subtraction (least decimal places)",
            "Arithmetic operations rule for multiplication and division (least significant figures)"
        ],
        "key_concepts": [
            "Significant Figure Rules",
            "Scientific Exponential Notation (a × 10^b)",
            "Rounding-Off Rules (Preceding Odd/Even Rule for 5)",
            "Significant Figures in Addition, Subtraction, Multiplication & Division"
        ],
        "success_criteria": [
            "Determine the exact number of significant figures in any measured quantity",
            "Apply the round-off rule for terminating 5: increase by 1 if preceded by odd, leave unchanged if even",
            "Express products, quotients, sums, and differences to the correct number of significant digits",
            "State why pure numbers and conversion factors have infinite significant figures"
        ],
        "chapter_notes": """# CHAPTER 1: UNITS AND MEASUREMENTS
## MODULE 3: Significant Figures & Scientific Computation

### 1. Definition of Significant Figures
In any measured quantity, the **significant figures** are the digits that are known reliably plus the one first digit that is uncertain.
*Example*: A length measured as $16.2\\text{ cm}$ means $1$ and $6$ are reliable, while $2$ is uncertain (lying between $16.1\\text{ cm}$ and $16.3\\text{ cm}$). Thus it has $3$ significant figures.

### 2. Rules for Determining Number of Significant Figures
1. **All non-zero digits are significant**: $2875\\text{ m}$ has $4$ SF.
2. **All zeros between two non-zero digits are significant** (no matter where decimal point is): $2005\\text{ s}$ has $4$ SF; $2.005\\text{ s}$ has $4$ SF.
3. **If number is less than 1, zeros to right of decimal point but to left of first non-zero digit are NOT significant**: In $\\underline{0.00}2308$, the underlined zeros are non-significant $\\implies 4$ SF.
4. **Terminal or trailing zeros in a number without a decimal point are NOT significant**: $12300\\text{ m}$ has $3$ SF (zeros are place holders).
5. **Trailing zeros in a number with a decimal point ARE significant**: $4.700\\text{ g}$ has $4$ SF; $0.06900\\text{ m}$ has $4$ SF.

### 3. Scientific Notation: Eliminating Ambiguity
To eliminate ambiguity about trailing zeros:
$$\\text{Report as } a \\times 10^b \\quad (1 \\le a < 10)$$
The powers of 10 are non-significant place-holders:
- $4.700 \\times 10^2\\text{ m} \\implies 4$ SF
- $4.70 \\times 10^2\\text{ m} \\implies 3$ SF
- $4.7 \\times 10^2\\text{ m} \\implies 2$ SF

### 4. Rules for Rounding Off
Let the insignificant digit to be dropped be $d$:
1. If $d < 5$, preceding digit is left unchanged ($2.743 \\to 2.74$).
2. If $d > 5$, preceding digit is raised by $1$ ($2.747 \\to 2.75$).
3. **If $d = 5$ (or $5$ followed by zeros)**:
   - If preceding digit is **even**, leave it unchanged ($2.7450 \\to 2.74$).
   - If preceding digit is **odd**, raise it by $1$ ($2.7350 \\to 2.74$).

### 5. Rules in Arithmetic Operations
1. **Multiplication and Division**: The final result should retain only as many significant figures as are there in the original number with the **least significant figures**.
2. **Addition and Subtraction**: The final result should retain only as many decimal places as are there in the number with the **least decimal places**.
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 1.1: Each side of a cube is measured to be 7.203 m. What are the total surface area and the volume of the cube to appropriate significant figures?",
                "given": "Side of cube a = 7.203 m (4 significant figures).",
                "formula": "Total Surface Area A = 6 a²; Volume V = a³.",
                "substitution": "A = 6 × (7.203 m)² = 6 × 51.883209 m² = 311.299254 m²; V = (7.203 m)³ = 373.714754 m³.",
                "calculation": "Since 7.203 has 4 significant figures (and 6 is an exact number with infinite SF), both results must be rounded off to 4 significant figures: A = 311.3 m², V = 373.7 m³.",
                "finalAnswer": "Total Surface Area = 311.3 m², Volume = 373.7 m³",
                "unit": "m², m³",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            },
            {
                "problem": "Textbook Example 1.2: 5.74 g of a substance occupies 1.2 cm³. Express its density by keeping the significant figures in view.",
                "given": "Mass m = 5.74 g (3 SF), Volume V = 1.2 cm³ (2 SF).",
                "formula": "Density ρ = m / V",
                "substitution": "ρ = 5.74 g / 1.2 cm³ = 4.78333... g/cm³",
                "calculation": "The least number of significant figures in the given data is 2 (in volume 1.2). Therefore, round off the result to 2 significant figures: ρ = 4.8 g/cm³.",
                "finalAnswer": "Density ρ = 4.8 g/cm³",
                "unit": "g/cm³",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            }
        ],
        "common_misconceptions": [
            "Applying the least significant figures rule to addition/subtraction: Addition and subtraction depend on LEAST DECIMAL PLACES, not least significant figures!",
            "Treating pure mathematical constants (like 6 in surface area or 2π in circumference) as having 1 significant figure: Pure numbers have infinite significant figures and do not restrict calculation precision."
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod1_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Significant Figure Rules",
                    "diagram_title": "Decision Flowchart for Significant Figures",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "significant figures rules flowchart physics chemistry",
                    "video_search_query": "significant figures rules explained physics tutorial",
                    "what_to_make": "Flowchart guiding classification of non-zeroes, leading zeroes, trapped zeroes and trailing zeroes",
                    "what_to_explain": "Walk through each decision branch for determining significant digits",
                    "timing_and_cue": "Step 2 (Rules Definition)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "How many significant figures are in 0.002500 kg and 2.500 × 10³ kg?",
                            "ideal_answer": "Both quantities have 4 significant figures. Leading zeroes are placeholders, while trailing zeroes after a decimal point are significant.",
                            "socratic_hint": "Check whether the leading zeroes define magnitude or precision.",
                            "type": "Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 4: Dimensions of Physical Quantities & Dimensional Analysis
    # Date: 2026-11-15
    # -------------------------------------------------------------
    modules.append({
        "order_index": 4,
        "title": "Dimensions of Physical Quantities, Principle of Homogeneity & Dimensional Applications",
        "description": "In-depth derivation of dimensional formulas [M^a L^b T^c], Principle of Homogeneity, and the three major applications of dimensional analysis: checking consistency, deriving physical equations, and conversion of units.",
        "target_completion_date": "2026-11-15",
        "syllabus_pacing": "Day 4 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Dimensions of a physical quantity: Powers to which fundamental units must be raised",
            "Dimensional formula and dimensional equations",
            "Dimensional formulas of mechanics: Force, Work, Energy, Power, Pressure, Gravitational Constant",
            "Dimensional formulas of electricity and thermodynamics: Charge, Resistance, Specific Heat",
            "Principle of Homogeneity of Dimensions: Only quantities with identical dimensions can be added/subtracted",
            "Application 1: Checking correctness/consistency of physical equations",
            "Application 2: Deriving relations among physical quantities via dimensional synthesis",
            "Application 3: Conversion of a physical quantity from one system of units to another",
            "Limitations of dimensional analysis: Dimensionless constants, exponential/trigonometric arguments"
        ],
        "key_concepts": [
            "Dimensional Formulae & Equations [M^a L^b T^c]",
            "Principle of Homogeneity of Dimensions",
            "Checking Consistency of Physical Equations",
            "Deriving Physical Relations via Dimensional Analysis",
            "Conversion of Units (n₁ u₁ = n₂ u₂)"
        ],
        "success_criteria": [
            "Derive dimensional formulas for any physical quantity using fundamental definitions",
            "Apply Principle of Homogeneity to verify consistency of kinematic and dynamic formulas",
            "Derive formulas like simple pendulum period T = k √(l/g) and Stokes' law F = 6πηrv",
            "Convert energy from Joules to ergs and force from Newtons to dynes using dimensional equations",
            "Identify the fundamental limitations of dimensional analysis"
        ],
        "chapter_notes": """# CHAPTER 1: UNITS AND MEASUREMENTS
## MODULE 4: Dimensions & Dimensional Analysis

### 1. Concept of Dimensions
The **dimensions** of a physical quantity are the powers (or exponents) to which the base quantities are raised to represent that quantity.
Notation: $[M]$ for Mass, $[L]$ for Length, $[T]$ for Time, $[A]$ for Current, $[K]$ for Temperature, etc.
- Velocity $= [L T^{-1}]$
- Acceleration $= [L T^{-2}]$
- Force $= [M L T^{-2}]$
- Work / Energy $= [M L^2 T^{-2}]$
- Power $= [M L^2 T^{-3}]$
- Pressure / Stress $= [M L^{-1} T^{-2}]$
- Universal Gravitational Constant $G = [M^{-1} L^3 T^{-2}]$ (from $F = G m_1 m_2 / r^2$)
- Planck's Constant $h = [M L^2 T^{-1}]$ (from $E = h \\nu$)
- Coefficient of Viscosity $\\eta = [M L^{-1} T^{-1}]$ (from $F = \\eta A dv/dx$)

### 2. Principle of Homogeneity of Dimensions
*Statement*: A physical equation is dimensionally correct if and only if the dimensions of all terms on both sides of the equation are identical.
$$\\text{In equation } A + B = C - D, \\quad [A] = [B] = [C] = [D]$$
Furthermore, arguments of trigonometric, exponential, and logarithmic functions must be strictly **dimensionless** ($[M^0 L^0 T^0]$).

### 3. Application 1: Checking Dimensional Consistency
If dimensions of LHS $\\neq$ RHS, the equation is physically wrong. If LHS $=$ RHS, it is dimensionally consistent (though pure numerical constants cannot be verified).

### 4. Application 2: Deriving Relations Among Quantities
Assume quantity $Q$ depends on $q_1^a, q_2^b, q_3^c$:
$$Q = k \\, q_1^a q_2^b q_3^c$$
Equating powers of $M, L, T$ on both sides yields a system of linear equations in $a, b, c$.

### 5. Application 3: Conversion of Units
Magnitude $Q = n_1 u_1 = n_2 u_2$:
$$n_2 = n_1 \\left[\\frac{M_1}{M_2}\\right]^a \\left[\\frac{L_1}{L_2}\\right]^b \\left[\\frac{T_1}{T_2}\\right]^c$$

### 6. Limitations of Dimensional Analysis
1. Cannot determine dimensionless constants of proportionality (e.g. $1/2$ in $K = \\frac{1}{2}mv^2$ or $2\\pi$ in $T = 2\\pi\\sqrt{l/g}$).
2. Fails if a physical quantity depends on more than three variables in mechanics (as there are only 3 fundamental equations for $M, L, T$).
3. Cannot derive formulas containing trigonometric, exponential, or logarithmic functions.
4. Does not distinguish whether a quantity is a scalar or a vector.
""",
        "worked_examples": [
            {
                "problem": "Textbook Example 1.3: Let us consider an equation 1/2 m v² = m g h where m is the mass of the body, v its velocity, g is the acceleration due to gravity and h is the height. Check whether this equation is dimensionally correct.",
                "given": "LHS = (1/2) m v², RHS = m g h.",
                "formula": "[LHS] = [m][v]²; [RHS] = [m][g][h]",
                "substitution": "[LHS] = [M] [L T⁻¹]² = [M L² T⁻²]; [RHS] = [M] [L T⁻²] [L] = [M L² T⁻²]",
                "calculation": "Dimensions of LHS = [M L² T⁻²] = Dimensions of RHS.",
                "finalAnswer": "The equation is dimensionally correct (homogenous).",
                "unit": "M L² T⁻²",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            },
            {
                "problem": "Textbook Example 1.5: Consider a simple pendulum, having a bob attached to a string, that oscillates under the action of the force of gravity. Suppose that the period of oscillation of the simple pendulum depends on its length (l), mass of the bob (m) and acceleration due to gravity (g). Derive the expression for its time period using method of dimensions.",
                "given": "T depends on m^a, l^b, g^c.",
                "formula": "T = k m^a l^b g^c",
                "substitution": "[M⁰ L⁰ T¹] = [M]^a [L]^b [L T⁻²]^c = [M^a L^(b+c) T^(-2c)]",
                "calculation": "Equating powers: a = 0; b + c = 0 => b = -c; -2c = 1 => c = -1/2 => b = 1/2. Thus T = k m⁰ l^(1/2) g^(-1/2) = k √(l/g).",
                "finalAnswer": "T = k √(l/g), where k is a dimensionless constant (found experimentally to be 2π).",
                "unit": "s",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            }
        ],
        "common_misconceptions": [
            "Assuming dimensionally correct means physically correct: An equation can be dimensionally correct but physically wrong (e.g. s = vt is dimensionally correct for accelerated motion, but physically incomplete without ½at²).",
            "Attempting to derive relations with sums: Dimensional analysis cannot derive relations having more than one term separated by plus or minus (like v² = u² + 2as)."
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod1_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Principle of Homogeneity of Dimensions",
                    "diagram_title": "Dimensional Balancing Scale Architecture",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "dimensional analysis principle of homogeneity physics diagram",
                    "video_search_query": "dimensional analysis principle of homogeneity class 11 physics",
                    "what_to_make": "Vector diagram of a two-pan balance weighing dimensions of LHS vs RHS terms",
                    "what_to_explain": "Show how units and dimensions cancel out in trigonometric arguments",
                    "timing_and_cue": "Step 2 (Formulation)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "Can a quantity have units but no dimensions? Give an authentic example.",
                            "ideal_answer": "Yes. Plane angle (unit: radian) and solid angle (unit: steradian) have physical units but are completely dimensionless ([M⁰L⁰T⁰]).",
                            "socratic_hint": "Recall the supplementary units in the SI system.",
                            "type": "Conceptual"
                        }
                    ]
                }
            ]
        }
    })

    # -------------------------------------------------------------
    # MODULE 5: Complete NCERT Textbook Exercise Solver
    # Date: 2026-11-16
    # -------------------------------------------------------------
    modules.append({
        "order_index": 5,
        "title": "Exercise 1.1 to 1.18 Complete Solver: Units, Errors & Dimensional Mastery",
        "description": "Exhaustive step-by-step solutions to every textbook exercise question (Exercises 1.1 through 1.18) covering conversion of units, significant figures, parallax measurements, and dimensional proofs.",
        "target_completion_date": "2026-11-16",
        "syllabus_pacing": "Day 5 of 35 (Part 1 Mid-Term Mastery)",
        "estimated_minutes": 60,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Exercise 1.1: Fill in the blanks with unit conversions (volume, density, speed, G)",
            "Exercise 1.2: Conversions by convenient units (kg m² s⁻², m/s, acceleration)",
            "Exercise 1.3: Calorie to new unit system conversion using dimensional method",
            "Exercise 1.4: Analysis of clarity in statement of precision",
            "Exercise 1.5: Length measurement comparisons (vernier, optical microscope, screw gauge)",
            "Exercise 1.6 to 1.10: Magnification, hair thickness, thread diameter, thread winding method",
            "Exercise 1.11 to 1.15: Significant figures count and arithmetic results",
            "Exercise 1.16 to 1.18: Dimensional deduction of Van der Waals equation and relativistic mass"
        ],
        "key_concepts": [
            "Unit Conversions (Joule to erg, Newton to dyne, G in CGS)",
            "Step-by-Step Exercise Solver (1.1 to 1.18)",
            "Van der Waals Equation Dimensional Constants (P + a/V²)(V - b) = RT",
            "Relativistic Mass Formula Dimensional Verification"
        ],
        "success_criteria": [
            "Solve every part of Exercise 1.1 through 1.18 with flawless mathematical rigor",
            "Determine dimensions of constants a and b in Van der Waals equation",
            "Convert any physical quantity to custom system with arbitrary units of mass, length, time",
            "Attain 100% mastery of Unit I for the upcoming Mid-Term Examination"
        ],
        "chapter_notes": """# CHAPTER 1: UNITS AND MEASUREMENTS
## MODULE 5: Complete NCERT Exercise Solver

### Summary of Core Solutions
- **Exercise 1.1 (Conversions)**:
  - (a) Volume of cube of side $1\\text{ cm} = (10^{-2}\\text{ m})^3 = 10^{-6}\\text{ m}^3$.
  - (b) Surface area of cylinder ($r=2\\text{ cm}, h=10\\text{ cm}$) $= 2\\pi r(r+h) = 2 \\times 3.14 \\times 2 \\times 12 = 150.72\\text{ cm}^2 = 1.5 \\times 10^4\\text{ mm}^2$.
  - (c) Vehicle moving at $18\\text{ km/h} = 18 \\times (5/18)\\text{ m/s} = 5\\text{ m/s} \\implies 5\\text{ m}$ in $1\\text{ s}$.
  - (d) Relative density of lead is $11.3 \\implies \\rho = 11.3\\text{ g/cm}^3 = 1.13 \\times 10^4\\text{ kg/m}^3$.

- **Exercise 1.3 (Calorie Conversion)**:
  $1\\text{ cal} = 4.2\\text{ J} = 4.2\\text{ kg m}^2\\text{ s}^{-2}$.
  In new units with mass $\\alpha\\text{ kg}$, length $\\beta\\text{ m}$, time $\\gamma\\text{ s}$:
  $$n_2 = 4.2 \\left[\\frac{1\\text{ kg}}{\\alpha\\text{ kg}}\\right]^1 \\left[\\frac{1\\text{ m}}{\\beta\\text{ m}}\\right]^2 \\left[\\frac{1\\text{ s}}{\\gamma\\text{ s}}\\right]^{-2} = 4.2 \\, \\alpha^{-1} \\beta^{-2} \\gamma^2$$

- **Exercise 1.16 (Van der Waals Constants)**:
  $$\\left(P + \\frac{a}{V^2}\\right)(V - b) = R T$$
  By Principle of Homogeneity:
  $$\\left[\\frac{a}{V^2}\\right] = [P] = [M L^{-1} T^{-2}] \\implies [a] = [P][V^2] = [M L^{-1} T^{-2}][L^6] = [M L^5 T^{-2}]$$
  $$[b] = [V] = [L^3]$$
""",
        "worked_examples": [
            {
                "problem": "NCERT Exercise 1.3: A calorie is a unit of heat or energy and it equals about 4.2 J where 1 J = 1 kg m² s⁻². Suppose we employ a system of units in which the unit of mass equals α kg, the unit of length equals β m, the unit of time is γ s. Show that a calorie has a magnitude 4.2 α⁻¹ β⁻² γ² in terms of the new units.",
                "given": "1 calorie = 4.2 kg m² s⁻²; new units: mass = α kg, length = β m, time = γ s.",
                "formula": "n₂ = n₁ [M₁/M₂]^a [L₁/L₂]^b [T₁/T₂]^c",
                "substitution": "Dimensions of energy = [M¹ L² T⁻²], so a = 1, b = 2, c = -2. n₂ = 4.2 × [1 kg / α kg]¹ × [1 m / β m]² × [1 s / γ s]⁻²",
                "calculation": "n₂ = 4.2 × α⁻¹ × β⁻² × γ² = 4.2 α⁻¹ β⁻² γ².",
                "finalAnswer": "Magnitude of calorie in new units = 4.2 α⁻¹ β⁻² γ²",
                "unit": "new units",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            },
            {
                "problem": "NCERT Exercise 1.14: A book with many printing errors contains four different formulas for the displacement y of a particle undergoing a certain periodic motion: (a) y = a sin(2π t / T), (b) y = a sin(vt), (c) y = (a/T) sin(t/a), (d) y = (a √2) [sin(2π t / T) + cos(2π t / T)]. Rule out the wrong formulas on dimensional grounds.",
                "given": "y is displacement [L], a is amplitude [L], v is speed [L T⁻¹], t is time [T], T is period [T].",
                "formula": "The argument of trigonometric sine/cosine must be dimensionless [M⁰L⁰T⁰], and [y] must equal [amplitude].",
                "substitution": "(a) [2π t / T] = [T / T] = 1 (dimensionless), [y] = [a] = [L] => Correct. (b) [vt] = [L T⁻¹][T] = [L] ≠ 1 => Dimensionally WRONG. (c) [t / a] = [T / L] ≠ 1, and [a / T] = [L T⁻¹] ≠ [L] => Dimensionally WRONG. (d) [2π t / T] = 1, [y] = [a √2] = [L] => Correct.",
                "calculation": "Formulas (b) and (c) are ruled out on dimensional grounds.",
                "finalAnswer": "Formulas (b) and (c) are wrong; (a) and (d) are dimensionally valid.",
                "unit": "dimensionless analysis",
                "has_diagram": True,
                "diagram_svg": mod1_svg
            }
        ],
        "common_misconceptions": [
            "Thinking that an argument of a sine or cosine can have dimensions: In any trigonometric function sin(k x - ω t), the entire argument MUST be dimensionless. Thus [k] = [L⁻¹] and [ω] = [T⁻¹]!"
        ],
        "visual_lesson_plan": {
            "diagram_type": "svg",
            "svg": mod1_svg,
            "concept_visuals": [
                {
                    "concept_index": 0,
                    "concept_title": "Van der Waals Equation Dimensional Constants",
                    "diagram_title": "Real Gas Intermolecular Volume and Pressure Correction",
                    "diagram_type": "svg",
                    "svg": mod1_svg,
                    "image_search_query": "van der waals equation molecular attraction volume correction diagram",
                    "video_search_query": "van der waals equation dimensional analysis derivation",
                    "what_to_make": "Cylinder of gas showing excluded volume b and intermolecular attraction pressure correction a/V^2",
                    "what_to_explain": "Derive dimensions of a = [M L^5 T^-2] and b = [L^3]",
                    "timing_and_cue": "Step 2 (Board Problem)"
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "questions": [
                        {
                            "question": "What are the dimensions of a/b in the Van der Waals equation (P + a/V²)(V - b) = RT?",
                            "ideal_answer": "Since [a] = [M L⁵ T⁻²] and [b] = [L³], the ratio [a/b] = [M L⁵ T⁻²] / [L³] = [M L² T⁻²], which has the dimensions of work or energy!",
                            "socratic_hint": "Divide the dimensions of constant a by constant b.",
                            "type": "Board PYQ"
                        }
                    ]
                }
            ]
        }
    })

    return modules
