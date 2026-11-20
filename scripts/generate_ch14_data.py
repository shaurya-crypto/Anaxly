import json

def build_ch14():
    with open("scripts/physics_class11_modules/physics_modules_ch14.json", "r", encoding="utf-8") as f:
        modules = json.load(f)

    # -------------------------------------------------------------
    # Module 83: Transverse & Longitudinal Waves & Progressive Wave Equation
    # -------------------------------------------------------------
    modules[0]["worked_examples"] = [
        {
            "problem": "NCERT Example 14.1: Given below are some examples of wave motion. State in each case if the wave motion is transverse, longitudinal, or a combination of both:\n(a) Motion of a kink in a longitudinal spring produced by displacing one end of the spring sideways.\n(b) Waves produced in a cylinder containing a liquid by moving its piston back and forth.\n(c) Waves produced by a motorboat sailing in water.\n(d) Ultrasonic waves in air produced by an oscillating quartz crystal.",
            "given": "Four mechanical wave propagation scenarios",
            "to_calculate": "Classification of wave type with physical justification",
            "formula": "Transverse wave: Medium particles oscillate perpendicular to wave propagation direction.\nLongitudinal wave: Medium particles oscillate parallel to wave propagation direction.\nSurface wave / combination: Particles execute orbital motion involving both longitudinal and transverse components.",
            "substitution": "Analyze direction of particle oscillation relative to energy transport for each case",
            "calculation": "(a) Transverse: Displacing the spring sideways makes coils oscillate perpendicular to the length of the spring along which the kink propagates.\n(b) Longitudinal: Moving the piston back and forth compresses and rarefies the liquid along the cylinder axis, so liquid particles oscillate parallel to the wave propagation direction.\n(c) Combination of both: The motorboat generates surface water ripples where water particles describe circular or elliptical orbital paths having both vertical (transverse) and horizontal (longitudinal) displacements.\n(d) Longitudinal: Ultrasonic sound waves in air propagate strictly via compressions and rarefactions because fluids cannot sustain static shearing stresses.",
            "rough_work": "[ROUGH_WORK]\n(a) Sideways kink: transverse.\n(b) Piston in liquid: longitudinal.\n(c) Water waves: transverse + longitudinal (elliptical orbits).\n(d) Ultrasound in air: longitudinal.",
            "finalAnswer": "(a) Transverse wave; (b) Longitudinal wave; (c) Combination of transverse and longitudinal; (d) Longitudinal wave",
            "unit": "Qualitative Classification",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Example 14.1, Page 280",
            "image_search_query": "transverse versus longitudinal wave particle motion"
        },
        {
            "problem": "NCERT Example 14.2: A wave travelling along a string is described by:\ny(x, t) = 0.005 · sin(80.0 x - 3.0 t)\nin which the numerical constants are in SI units (0.005 m, 80.0 rad m⁻¹, and 3.0 rad s⁻¹). Calculate (a) the amplitude, (b) the wavelength, and (c) the period and frequency of the wave. Also, calculate the displacement y of the wave at a distance x = 30.0 cm and time t = 20 s.",
            "given": "Wave equation: y(x, t) = 0.005 sin(80.0 x - 3.0 t) m\nSI coefficients: a = 0.005 m, k = 80.0 rad m⁻¹, ω = 3.0 rad s⁻¹\nPoint coordinates: x = 30.0 cm = 0.30 m, t = 20 s",
            "to_calculate": "(a) Amplitude a, (b) Wavelength λ, (c) Period T and frequency ν, (d) Displacement y(0.30, 20)",
            "formula": "Standard progressive harmonic wave travelling in +x direction: y(x, t) = a · sin(k x - ω t)\n(a) Amplitude = a\n(b) Propagation constant k = 2π / λ => λ = 2π / k\n(c) Angular frequency ω = 2π / T = 2π ν => T = 2π / ω and ν = ω / 2π\n(d) Displacement: substitute x and t into the given function.",
            "substitution": "(a) a = 0.005 m = 5.0 mm\n(b) λ = 2π / 80.0 = 2 × 3.1416 / 80.0 m\n(c) T = 2π / 3.0 = 2 × 3.1416 / 3.0 s; ν = 3.0 / (2π) s⁻¹\n(d) Argument θ = (80.0 × 0.30) - (3.0 × 20) = 24.0 - 60.0 = -36.0 rad\ny = 0.005 · sin(-36.0 rad) = -0.005 · sin(36.0 rad)",
            "calculation": "(a) a = 0.005 m = 0.5 cm = 5.0 mm\n(b) λ = 6.2832 / 80.0 = 0.07854 m ≈ 7.85 cm\n(c) T = 6.2832 / 3.0 = 2.094 s ≈ 2.09 s; ν = 1 / 2.094 = 0.477 Hz ≈ 0.48 Hz\n(d) 36.0 radians in revolutions:\n36.0 / (2π) = 36.0 / 6.2832 = 5.72957 revolutions\nDecimal fraction = 0.72957 × 2π = 4.584 rad\nsin(-36.0 rad) = -sin(36.0 rad) = -(-0.99177) = +0.9918\ny = 0.005 × (+0.9918) = +0.004959 m ≈ +4.96 mm ≈ +5.0 mm",
            "rough_work": "[ROUGH_WORK]\nk = 80 => λ = 2pi/80 = 0.0785 m\nw = 3 => T = 2pi/3 = 2.09 s, ν = 0.48 Hz\n80(0.3) - 3(20) = 24 - 60 = -36 rad\n36 rad = 5.7296 × 2pi => remainder = 4.584 rad\nsin(-36) = -sin(4.584) = -(-0.9918) = +0.9918\ny = 0.005 × 0.9918 = 0.00496 m = 4.96 mm.",
            "finalAnswer": "(a) Amplitude a = 0.005 m (5 mm); (b) Wavelength λ = 0.0785 m (7.85 cm); (c) Period T = 2.09 s, Frequency ν = 0.48 Hz; (d) Displacement at x=0.30 m, t=20 s is y = +4.96 mm",
            "unit": "m, s, Hz, mm",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Example 14.2, Page 283",
            "image_search_query": "progressive harmonic wave equation amplitude wavelength frequency"
        }
    ]

    modules[0]["concept_questions"] = [
        {
            "question": "In a progressive travelling mechanical wave y(x, t) = a · sin(kx - ωt), what physical quantity is transported across space by the wave without the net transport of matter?",
            "options": [
                "(Recommended) Energy and linear momentum",
                "Mass of the constituent medium particles",
                "Static gravitational potential",
                "Electric charge of the particles"
            ],
            "correctAnswer": "(Recommended) Energy and linear momentum",
            "correct_answer": "(Recommended) Energy and linear momentum",
            "explanation": "Mechanical waves propagate energy and momentum through elastic interactions between neighboring medium particles. Each individual particle merely oscillates about its local equilibrium position without any net bulk translation.",
            "hint": "Analyze what moves continuously across space in a wave vs what oscillates locally.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 14.2, Page 279",
            "image_search_query": "wave transport of energy and momentum no mass"
        },
        {
            "question": "What is the relation between wave propagation speed v, angular frequency ω, and propagation constant (wavenumber) k?",
            "options": [
                "(Recommended) v = ω / k = ν · λ",
                "v = k / ω",
                "v = ω · k",
                "v = √(ω / k)"
            ],
            "correctAnswer": "(Recommended) v = ω / k = ν · λ",
            "correct_answer": "(Recommended) v = ω / k = ν · λ",
            "explanation": "Since k = 2π / λ and ω = 2π ν, dividing yields ω / k = (2π ν) / (2π / λ) = ν · λ = v, which is the phase velocity of the wave.",
            "hint": "Divide ω by k using their definitions.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 14.3, Page 282",
            "image_search_query": "wave speed omega over k frequency wavelength"
        },
        {
            "question": "Why can transverse mechanical waves propagate ONLY through solids and along liquid surfaces, but CANNOT propagate through the interior of gases or liquids?",
            "options": [
                "(Recommended) Because fluids possess zero static shear modulus (they cannot sustain shearing deformation)",
                "Because fluid molecules move faster than the speed of light",
                "Because fluids have zero density",
                "Because longitudinal waves reflect internally inside fluids"
            ],
            "correctAnswer": "(Recommended) Because fluids possess zero static shear modulus (they cannot sustain shearing deformation)",
            "correct_answer": "(Recommended) Because fluids possess zero static shear modulus (they cannot sustain shearing deformation)",
            "explanation": "Transverse wave propagation requires an elastic restoring force against shear (shear modulus G). Fluids (liquids and gases) can deform continuously under shear without restoring force (G = 0), so transverse shear waves cannot propagate through bulk fluids.",
            "hint": "Consider the elastic property required to resist shape distortion.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 14.2, Page 280",
            "image_search_query": "transverse waves shear modulus solids fluids"
        },
        {
            "question": "A travelling wave is described by y(x, t) = a · sin(kx + ωt). In which direction is this wave propagating?",
            "options": [
                "(Recommended) Along the negative x-direction (-x direction)",
                "Along the positive x-direction (+x direction)",
                "Along the positive y-direction (+y direction)",
                "Stationary (standing wave with no propagation)"
            ],
            "correctAnswer": "(Recommended) Along the negative x-direction (-x direction)",
            "correct_answer": "(Recommended) Along the negative x-direction (-x direction)",
            "explanation": "For any point of constant phase: kx + ωt = constant. Differentiating gives k (dx/dt) + ω = 0 => dx/dt = -ω/k < 0. The wave phase pattern moves towards negative x.",
            "hint": "Set kx + ωt = constant and find the sign of dx/dt.",
            "blooms_level": "Apply",
            "textbook_reference": "Section 14.3, Page 282",
            "image_search_query": "wave propagation direction plus minus sign kx omega t"
        }
    ]

    # -------------------------------------------------------------
    # Module 84: Speed of Waves: Strings & Newton-Laplace Sound
    # -------------------------------------------------------------
    modules[1]["worked_examples"] = [
        {
            "problem": "NCERT Example 14.3: A steel wire 0.72 m long has a mass of 5.0 × 10⁻³ kg. If the wire is under a tension of 60 N, what is the speed of transverse waves on the wire?",
            "given": "Length of wire L = 0.72 m, Mass of wire m = 5.0 × 10⁻³ kg, Tension in wire T = 60 N",
            "to_calculate": "Speed of transverse waves v on the wire",
            "formula": "Linear mass density: μ = m / L\nTransverse wave speed on a stretched string: v = √(T / μ)",
            "substitution": "μ = (5.0 × 10⁻³ kg) / (0.72 m) = 6.944 × 10⁻³ kg m⁻¹\nv = √[ (60 N) / (6.944 × 10⁻³ kg m⁻¹) ]",
            "calculation": "v = √[ 60 × 0.72 / (5.0 × 10⁻³) ] = √[ 43.2 / 0.005 ] = √8640 = 92.95 m s⁻¹ ≈ 93 m s⁻¹",
            "rough_work": "[ROUGH_WORK]\nμ = 0.005 / 0.72 = 0.006944 kg/m\nv = sqrt(60 / 0.006944) = sqrt(8640) = 92.95 m/s ≈ 93 m/s.",
            "finalAnswer": "The speed of transverse waves on the wire is 93 m s⁻¹",
            "unit": "m s⁻¹",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Example 14.3, Page 284",
            "image_search_query": "transverse wave speed stretched string tension linear density"
        },
        {
            "problem": "NCERT Example 14.4: Estimate the speed of sound in air at standard temperature and pressure (STP: T = 273.15 K, P = 1.013 × 10⁵ Pa). The mass of 1 mole of air is 29.0 × 10⁻³ kg. Compare the result calculated using (a) Newton's formula (isothermal assumption), and (b) Laplace's correction (adiabatic assumption with γ = 1.40).",
            "given": "Pressure P = 1.013 × 10⁵ Pa, Temperature T = 273.15 K, Molar mass of air M = 29.0 × 10⁻³ kg mol⁻¹, Volume of 1 mole at STP V = 22.4 L = 22.4 × 10⁻³ m³, Density of air ρ = M / V = (29.0 × 10⁻³ kg) / (22.4 × 10⁻³ m³) = 1.295 kg m⁻³, Adiabatic index γ = 1.40",
            "to_calculate": "(a) Newton's speed v_Newton, (b) Laplace's corrected speed v_Laplace, and compare with experimental speed (331.3 m s⁻¹)",
            "formula": "(a) Newton's formula (Isothermal bulk modulus B_iso = P): v_Newton = √(P / ρ)\n(b) Laplace's formula (Adiabatic bulk modulus B_adia = γ P): v_Laplace = √(γ · P / ρ) = √γ · v_Newton",
            "substitution": "(a) v_Newton = √[ (1.013 × 10⁵ Pa) / (1.295 kg m⁻³) ]\n(b) v_Laplace = √[ 1.40 × (1.013 × 10⁵ Pa) / (1.295 kg m⁻³) ] = √1.40 × v_Newton",
            "calculation": "(a) v_Newton = √78224 = 279.7 m s⁻¹ ≈ 280 m s⁻¹ (underestimates by ~15%)\n(b) v_Laplace = √1.40 × 279.7 = 1.1832 × 279.7 = 330.9 m s⁻¹ ≈ 331 m s⁻¹\nThis matches the experimentally observed value of 331.3 m s⁻¹ at 0 °C with exceptional precision.",
            "rough_work": "[ROUGH_WORK]\nρ = 29 / 22.4 = 1.2946 kg/m³\nP/ρ = 101300 / 1.2946 = 78248\nsqrt(78248) = 279.7 m/s\nsqrt(1.4 × 78248) = 330.98 m/s ≈ 331 m/s.",
            "finalAnswer": "(a) Newton's formula speed v_Newton = 280 m s⁻¹; (b) Laplace's corrected speed v_Laplace = 331 m s⁻¹ (in excellent agreement with experimental 331.3 m s⁻¹)",
            "unit": "m s⁻¹",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Example 14.4, Page 285",
            "image_search_query": "newton laplace formula speed of sound air derivation"
        }
    ]

    modules[1]["concept_questions"] = [
        {
            "question": "Why did Newton's calculation of the speed of sound in air (v = √(P/ρ) ≈ 280 m/s) fail to match the experimental value of 332 m/s?",
            "options": [
                "(Recommended) Newton assumed that sound propagation is an isothermal process, whereas rapid compressions and rarefactions occur adiabatically with zero time for heat exchange",
                "Newton used the wrong value for atmospheric pressure",
                "Newton ignored the viscosity of the atmosphere",
                "Newton assumed that air consists exclusively of nitrogen"
            ],
            "correctAnswer": "(Recommended) Newton assumed that sound propagation is an isothermal process, whereas rapid compressions and rarefactions occur adiabatically with zero time for heat exchange",
            "correct_answer": "(Recommended) Newton assumed that sound propagation is an isothermal process, whereas rapid compressions and rarefactions occur adiabatically with zero time for heat exchange",
            "explanation": "Compressions and rarefactions in a sound wave take place so rapidly that heat cannot flow between adjacent regions. Air is also a poor thermal conductor. Thus the process is adiabatic (B = γP), not isothermal (B = P).",
            "hint": "Analyze the rate of compression/rarefaction compared to thermal conduction.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 14.4.2, Page 285",
            "image_search_query": "laplace correction adiabatic bulk modulus speed of sound"
        },
        {
            "question": "How does the speed of sound in air change when the atmospheric pressure doubles at constant temperature?",
            "options": [
                "(Recommended) The speed remains completely unchanged",
                "The speed doubles",
                "The speed increases by a factor of √2",
                "The speed is halved"
            ],
            "correctAnswer": "(Recommended) The speed remains completely unchanged",
            "correct_answer": "(Recommended) The speed remains completely unchanged",
            "explanation": "From v = √(γ P / ρ) and ideal gas law P / ρ = R T / M, we have v = √(γ R T / M). At constant temperature T, doubling pressure doubles density (P/ρ = constant), leaving the speed of sound strictly unchanged.",
            "hint": "Express speed of sound in terms of temperature T and molar mass M.",
            "blooms_level": "Apply",
            "textbook_reference": "Section 14.4.2, Page 285",
            "image_search_query": "speed of sound pressure independence constant temperature"
        },
        {
            "question": "Why does the speed of sound increase on a hot and humid rainy day compared to a dry cold day?",
            "options": [
                "(Recommended) High temperature increases thermal speed (v ∝ √T), and humid air has water vapour (M = 18) which lowers the effective molar mass of air (v ∝ 1/√M)",
                "Water droplets push the sound wave forward mechanically",
                "Sound travels faster in liquids than in air",
                "Atmospheric pressure is always higher during rain"
            ],
            "correctAnswer": "(Recommended) High temperature increases thermal speed (v ∝ √T), and humid air has water vapour (M = 18) which lowers the effective molar mass of air (v ∝ 1/√M)",
            "correct_answer": "(Recommended) High temperature increases thermal speed (v ∝ √T), and humid air has water vapour (M = 18) which lowers the effective molar mass of air (v ∝ 1/√M)",
            "explanation": "Speed v = √(γ R T / M). Higher T directly increases v. Water vapour has molar mass 18 g/mol, which is lighter than dry air (29 g/mol). Adding moisture lowers effective molar mass M, thereby increasing sound speed.",
            "hint": "Analyze the effects of T and molar mass M in v = √(γRT/M).",
            "blooms_level": "Analyze",
            "textbook_reference": "Section 14.4.2, Page 285",
            "image_search_query": "speed of sound humidity temperature effect"
        },
        {
            "question": "If the tension in a guitar string is quadrupled (T' = 4T), by what factor does the speed of transverse waves on the string increase?",
            "options": [
                "(Recommended) 2 times (doubled)",
                "4 times",
                "16 times",
                "√2 times"
            ],
            "correctAnswer": "(Recommended) 2 times (doubled)",
            "correct_answer": "(Recommended) 2 times (doubled)",
            "explanation": "Wave speed on a string is v = √(T / μ). Since v ∝ √T, quadrupling tension increases speed by √4 = 2.",
            "hint": "Use v = √(T/μ).",
            "blooms_level": "Apply",
            "textbook_reference": "Section 14.4.1, Page 284",
            "image_search_query": "guitar string wave speed tension proportionality"
        }
    ]

    # -------------------------------------------------------------
    # Module 85: Superposition Principle & Reflection at Boundaries
    # -------------------------------------------------------------
    modules[2]["worked_examples"] = [
        {
            "problem": "Two harmonic waves of the same frequency ν = 100 Hz and amplitude a = 3.0 mm travel along the positive x-direction on a string. They differ in phase by φ. (a) Derive the expression for the resultant wave using the principle of superposition. (b) Find the amplitude of the resultant wave when φ = 0 (in phase), φ = π/3 rad (60°), and φ = π rad (180° out of phase).",
            "given": "Two waves: y₁(x, t) = a sin(kx - ωt) and y₂(x, t) = a sin(kx - ωt + φ), Amplitude a = 3.0 mm, Frequency ν = 100 Hz",
            "to_calculate": "(a) Resultant wave equation y(x, t), (b) Resultant amplitude A_res for φ = 0, π/3, and π",
            "formula": "Superposition: y = y₁ + y₂ = a [ sin(kx - ωt) + sin(kx - ωt + φ) ]\nUsing sin C + sin D = 2 sin((C+D)/2) cos((C-D)/2):\ny(x, t) = [ 2a · cos(φ / 2) ] · sin(kx - ωt + φ / 2)\nResultant amplitude: A_res = 2a · |cos(φ / 2)|",
            "substitution": "(b1) For φ = 0: A_res = 2 × 3.0 mm × cos(0)\n(b2) For φ = π/3 (60°): A_res = 2 × 3.0 mm × cos(π/6) = 6.0 × (√3 / 2)\n(b3) For φ = π (180°): A_res = 2 × 3.0 mm × cos(π/2)",
            "calculation": "(b1) A_res = 2 × 3.0 × 1.0 = 6.0 mm (constructive interference)\n(b2) A_res = 6.0 × 0.8660 = 5.196 mm ≈ 5.2 mm\n(b3) A_res = 6.0 × 0 = 0 mm (complete destructive interference)",
            "rough_work": "[ROUGH_WORK]\n2a cos(phi/2)\nphi = 0 => 2(3) = 6 mm\nphi = pi/3 => 6 cos(pi/6) = 6 × 0.866 = 5.20 mm\nphi = pi => 6 cos(pi/2) = 0 mm.",
            "finalAnswer": "(a) Resultant wave: y = [2a cos(φ/2)] sin(kx - ωt + φ/2); (b) Resultant amplitudes: at φ=0, A = 6.0 mm; at φ=π/3, A = 5.2 mm; at φ=π, A = 0 mm",
            "unit": "mm",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Section 14.5, Page 286",
            "image_search_query": "superposition of two harmonic waves interference amplitude"
        },
        {
            "problem": "Explain the physical mechanism of reflection of a transverse wave pulse travelling on a string when it encounters: (a) a rigid fixed boundary (fixed end), and (b) an open or free boundary (free end attached to a frictionless ring on a vertical rod). State the phase change in each case.",
            "given": "Incident transverse wave pulse travelling towards boundary at x = 0: y_i(x, t) = a · f(kx - ωt)",
            "to_calculate": "Reflected wave equation y_r(x, t) and phase change Δφ for rigid and free boundaries",
            "formula": "Boundary conditions:\n1. Fixed end (Rigid boundary): Displacement at x = 0 must be strictly zero at all times: y_net(0, t) = y_i(0, t) + y_r(0, t) = 0 => y_r(0, t) = -y_i(0, t).\nReflected wave is inverted: y_r(x, t) = -a · f(-kx - ωt) = a · f(-kx - ωt + π). Phase shift Δφ = π radians (180°).\n2. Free end (Open boundary): Restoring force is zero, meaning slope ∂y/∂x at x = 0 must be zero: [∂y_i/∂x + ∂y_r/∂x]_{x=0} = 0 => y_r(0, t) = +y_i(0, t).\nReflected wave is upright (non-inverted): y_r(x, t) = +a · f(-kx - ωt). Phase shift Δφ = 0 radians.",
            "substitution": "Apply boundary conditions at x = 0",
            "calculation": "(a) At a rigid end, the incident pulse exerts an upward force on the fixed support. By Newton's Third Law, the rigid support exerts an equal downward reaction force on the string, generating an inverted reflected pulse with phase change of π radians.\n(b) At a free end, the frictionless ring overshoots to twice the incident pulse amplitude (2a) as it encounters no opposing reaction force. It generates an upright reflected pulse propagating backward with zero phase change.",
            "rough_work": "[ROUGH_WORK]\nFixed boundary: y(0, t) = 0 => y_r = -y_i => phase change = pi rad.\nFree boundary: dy/dx = 0 => y_r = +y_i => phase change = 0.",
            "finalAnswer": "(a) Rigid boundary: Pulse is inverted, Phase shift Δφ = π radians (180°); (b) Free boundary: Pulse is upright, Phase shift Δφ = 0 radians (0°)",
            "unit": "rad, Qualitative Derivation",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Section 14.5.2, Pages 287-288",
            "image_search_query": "wave reflection fixed free boundary phase change"
        }
    ]

    modules[2]["concept_questions"] = [
        {
            "question": "What is the boundary condition for wave displacement at a rigidly clamped end of a stretched string?",
            "options": [
                "(Recommended) The total displacement must remain strictly zero at all times (node, y = 0)",
                "The total displacement must reach maximum amplitude (antinode)",
                "The velocity must equal the speed of sound",
                "The tension in the string must drop to zero"
            ],
            "correctAnswer": "(Recommended) The total displacement must remain strictly zero at all times (node, y = 0)",
            "correct_answer": "(Recommended) The total displacement must remain strictly zero at all times (node, y = 0)",
            "explanation": "Because the string is rigidly clamped to an immovable clamp, its displacement is constrained to be identically zero (y = 0) at that point for all t. A node is formed.",
            "hint": "Consider the physical motion possible at an immovable clamp.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 14.5.2, Page 287",
            "image_search_query": "rigid boundary condition node zero displacement"
        },
        {
            "question": "When a sound wave in air reflects from a rigid wall, what happens to the displacement and pressure of the wave at the wall surface?",
            "options": [
                "(Recommended) The wall is a displacement node (zero particle vibration) and a pressure antinode (maximum pressure fluctuation)",
                "The wall is a displacement antinode and a pressure node",
                "Both displacement and pressure are zero",
                "Both displacement and pressure reach maximum values"
            ],
            "correctAnswer": "(Recommended) The wall is a displacement node (zero particle vibration) and a pressure antinode (maximum pressure fluctuation)",
            "correct_answer": "(Recommended) The wall is a displacement node (zero particle vibration) and a pressure antinode (maximum pressure fluctuation)",
            "explanation": "Air particles cannot penetrate the rigid wall, so their displacement must be zero (displacement node). However, air compresses strongly against the immovable wall, creating maximum pressure variations ΔP = -B (∂y/∂x) (pressure antinode).",
            "hint": "Remember that displacement node corresponds to pressure antinode and vice versa.",
            "blooms_level": "Analyze",
            "textbook_reference": "Section 14.5.2, Page 288",
            "image_search_query": "displacement node pressure antinode sound wave reflection"
        },
        {
            "question": "If two identical harmonic waves with equal amplitude a and frequency ω interfere destructively with a phase difference of π radians, what is the resultant intensity of the combined wave?",
            "options": [
                "(Recommended) Zero (I = 0)",
                "2 I_0",
                "4 I_0",
                "I_0 / 2"
            ],
            "correctAnswer": "(Recommended) Zero (I = 0)",
            "correct_answer": "(Recommended) Zero (I = 0)",
            "explanation": "Resultant amplitude A = 2a cos(φ/2) = 2a cos(π/2) = 0. Since intensity is proportional to amplitude squared (I ∝ A²), the resultant intensity is zero.",
            "hint": "Substitute φ = π into A = 2a cos(φ/2).",
            "blooms_level": "Apply",
            "textbook_reference": "Section 14.5.1, Page 286",
            "image_search_query": "destructive interference zero intensity phase difference pi"
        },
        {
            "question": "Under what condition does the principle of linear superposition fail for wave phenomena?",
            "options": [
                "(Recommended) When wave amplitudes become extremely large, inducing non-linear elastic stress-strain behavior in the medium (e.g., shock waves)",
                "When waves travel through a vacuum",
                "When wave frequency exceeds 20 kHz",
                "When waves travel in opposite directions"
            ],
            "correctAnswer": "(Recommended) When wave amplitudes become extremely large, inducing non-linear elastic stress-strain behavior in the medium (e.g., shock waves)",
            "correct_answer": "(Recommended) When wave amplitudes become extremely large, inducing non-linear elastic stress-strain behavior in the medium (e.g., shock waves)",
            "explanation": "The superposition principle is based on the linearity of the wave equation, which assumes Hooke's law (linear elasticity). For huge amplitudes (such as explosions or shock waves), non-linear elastic response breaks superposition.",
            "hint": "Think about when Hooke's law ceases to hold.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 14.5, Page 286",
            "image_search_query": "non linear wave superposition breakdown shock waves"
        }
    ]

    # -------------------------------------------------------------
    # Module 86: Standing Waves & Normal Modes: Strings & Pipes
    # -------------------------------------------------------------
    modules[3]["worked_examples"] = [
        {
            "problem": "NCERT Example 14.5: A pipe 30.0 cm long is open at both ends. Which harmonic mode of the pipe resonates with a 1.1 kHz source? Will resonance with the same source be observed if one end of the pipe is closed? (Take speed of sound in air v = 330 m s⁻¹)",
            "given": "Length of pipe L = 30.0 cm = 0.30 m, Source frequency ν = 1.1 kHz = 1100 Hz, Speed of sound v = 330 m s⁻¹",
            "to_calculate": "(a) Harmonic mode n for open pipe, (b) Possibility of resonance for closed pipe with same source",
            "formula": "1. Pipe open at both ends:\nResonant frequencies: ν_n = n · (v / 2L) for n = 1, 2, 3, ... (all harmonics present)\nFundamental frequency: ν₁ = v / 2L\n2. Pipe closed at one end:\nResonant frequencies: ν_m = m · (v / 4L) for odd integers m = 1, 3, 5, ... (only odd harmonics present)\nFundamental frequency: ν₁' = v / 4L",
            "substitution": "1. Open pipe:\nν₁ = 330 / (2 × 0.30) = 330 / 0.60 = 550 Hz\nHarmonic order: n = ν / ν₁ = 1100 Hz / 550 Hz\n2. Closed pipe:\nν₁' = 330 / (4 × 0.30) = 330 / 1.20 = 275 Hz\nRequired mode: m = ν / ν₁' = 1100 Hz / 275 Hz",
            "calculation": "1. Open pipe: n = 1100 / 550 = 2.0 (Exact integer n = 2).\nThis corresponds to the second harmonic (first overtone).\n2. Closed pipe: m = 1100 / 275 = 4.0.\nSince a pipe closed at one end can ONLY support odd harmonics (m = 1, 3, 5, ...), the mode m = 4 is strictly forbidden.\nTherefore, NO resonance will be observed with the 1.1 kHz source if one end is closed.",
            "rough_work": "[ROUGH_WORK]\nOpen pipe: ν₁ = 330 / (2 × 0.3) = 550 Hz\n1100 / 550 = 2 => Second harmonic resonates.\nClosed pipe: ν₁ = 330 / (4 × 0.3) = 275 Hz\nAllowed frequencies: 275, 825, 1375 Hz...\n1100 / 275 = 4 (even number) => cannot resonate.",
            "finalAnswer": "(a) The second harmonic (n = 2, first overtone) of the open pipe resonates with the 1.1 kHz source; (b) No resonance will occur if one end is closed, because m = 4 is an even harmonic, which does not exist in a closed pipe",
            "unit": "Harmonic mode, Resonance condition",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Example 14.5, Page 291",
            "image_search_query": "organ pipe harmonics open closed resonance standing waves"
        },
        {
            "problem": "A stretched string of length L = 1.0 m and mass m = 2.0 × 10⁻³ kg is clamped at both ends under a tension of 80 N. Calculate (a) the speed of transverse waves on the string, (b) the fundamental frequency of vibration, (c) the frequencies of the second and third harmonics, and (d) the separation between two successive nodes in the third harmonic mode.",
            "given": "Length L = 1.0 m, Mass m = 2.0 × 10⁻³ kg, Tension T = 80 N, String clamped at both ends (nodes at x = 0 and x = L)",
            "to_calculate": "(a) Wave speed v, (b) Fundamental frequency ν₁, (c) Harmonics ν₂ and ν₃, (d) Node separation Δx in 3rd harmonic",
            "formula": "Linear density: μ = m / L\nWave speed: v = √(T / μ)\nNormal mode frequencies: ν_n = n · (v / 2L) for n = 1, 2, 3, ...\nWavelength of n-th mode: λ_n = 2L / n\nDistance between successive nodes: Δx = λ_n / 2 = L / n",
            "substitution": "μ = 2.0 × 10⁻³ kg / 1.0 m = 2.0 × 10⁻³ kg m⁻¹\nv = √(80 / (2.0 × 10⁻³)) = √40000 m s⁻¹\nν₁ = v / (2 × 1.0)\nν₂ = 2 · ν₁, ν₃ = 3 · ν₁\nΔx₃ = 1.0 m / 3",
            "calculation": "(a) v = 200 m s⁻¹\n(b) ν₁ = 200 / 2.0 = 100 Hz\n(c) ν₂ = 2 × 100 = 200 Hz; ν₃ = 3 × 100 = 300 Hz\n(d) Δx₃ = 1.0 / 3 = 0.333 m = 33.3 cm",
            "rough_work": "[ROUGH_WORK]\nμ = 0.002 kg/m\nv = sqrt(80 / 0.002) = sqrt(40000) = 200 m/s\nν₁ = 200 / 2 = 100 Hz\nν₂ = 200 Hz, ν₃ = 300 Hz\nNode separation = L/3 = 33.3 cm.",
            "finalAnswer": "(a) Speed v = 200 m s⁻¹; (b) Fundamental frequency ν₁ = 100 Hz; (c) Second harmonic ν₂ = 200 Hz, Third harmonic ν₃ = 300 Hz; (d) Successive node distance in 3rd mode = 33.3 cm",
            "unit": "m s⁻¹, Hz, cm",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Section 14.6, Page 290",
            "image_search_query": "standing wave normal modes stretched string nodes antinodes"
        }
    ]

    modules[3]["concept_questions"] = [
        {
            "question": "What is the distance between two consecutive nodes (or two consecutive antinodes) in any standing wave of wavelength λ?",
            "options": [
                "(Recommended) λ / 2",
                "λ / 4",
                "λ",
                "2λ"
            ],
            "correctAnswer": "(Recommended) λ / 2",
            "correct_answer": "(Recommended) λ / 2",
            "explanation": "In a standing wave y = 2a sin(kx) cos(ωt), nodes occur where sin(kx) = 0 => kx = nπ => (2π/λ) x = nπ => x = n(λ/2). The distance between consecutive nodes is Δx = λ/2.",
            "hint": "Find the spacing between successive zeros of sin(kx).",
            "blooms_level": "Understand",
            "textbook_reference": "Section 14.6, Page 290",
            "image_search_query": "distance between consecutive nodes lambda over 2"
        },
        {
            "question": "Why does a musical wind instrument open at both ends (like a flute) sound richer in tone quality than an instrument closed at one end (like a clarinet)?",
            "options": [
                "(Recommended) Because an open pipe produces all harmonics (both even and odd: 1, 2, 3, 4, ...), whereas a closed pipe produces only odd harmonics (1, 3, 5, ...)",
                "Because an open pipe has a higher speed of sound inside",
                "Because air in a closed pipe suffers destructive interference at all frequencies",
                "Because closed pipes have no antinodes"
            ],
            "correctAnswer": "(Recommended) Because an open pipe produces all harmonics (both even and odd: 1, 2, 3, 4, ...), whereas a closed pipe produces only odd harmonics (1, 3, 5, ...)",
            "correct_answer": "(Recommended) Because an open pipe produces all harmonics (both even and odd: 1, 2, 3, 4, ...), whereas a closed pipe produces only odd harmonics (1, 3, 5, ...)",
            "explanation": "The harmonic series for an open pipe contains all integer multiples of the fundamental frequency (ν, 2ν, 3ν, 4ν...), generating a rich acoustic spectrum. Closed pipes lack all even harmonics (2ν, 4ν, 6ν...), producing a hollower timbre.",
            "hint": "Compare the harmonic spectrum of open and closed organ pipes.",
            "blooms_level": "Analyze",
            "textbook_reference": "Section 14.6, Page 291",
            "image_search_query": "harmonics open vs closed organ pipes timbre quality"
        },
        {
            "question": "Do standing waves transport net mechanical energy across space from one point to another?",
            "options": [
                "(Recommended) No, energy remains trapped and oscillates between kinetic and potential forms within each half-wavelength segment bounded by nodes",
                "Yes, they transport energy at the phase velocity v = ω/k",
                "Yes, but only in the forward direction",
                "Yes, energy flows continuously from antinodes into nodes"
            ],
            "correctAnswer": "(Recommended) No, energy remains trapped and oscillates between kinetic and potential forms within each half-wavelength segment bounded by nodes",
            "correct_answer": "(Recommended) No, energy remains trapped and oscillates between kinetic and potential forms within each half-wavelength segment bounded by nodes",
            "explanation": "Because nodes have permanently zero displacement (y = 0) and zero velocity at all times, no mechanical energy can pass across a node. Hence standing (stationary) waves have zero net energy transport.",
            "hint": "Analyze energy flow across a node where displacement is permanently zero.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 14.6, Page 289",
            "image_search_query": "stationary standing wave energy localization nodes"
        },
        {
            "question": "What is the relationship between the fundamental frequency of an open organ pipe (ν_open) and a closed organ pipe (ν_closed) of the exact same physical length L?",
            "options": [
                "(Recommended) ν_open = 2 · ν_closed (the open pipe fundamental frequency is double that of the closed pipe)",
                "ν_closed = 2 · ν_open",
                "ν_open = ν_closed",
                "ν_open = 4 · ν_closed"
            ],
            "correctAnswer": "(Recommended) ν_open = 2 · ν_closed (the open pipe fundamental frequency is double that of the closed pipe)",
            "correct_answer": "(Recommended) ν_open = 2 · ν_closed (the open pipe fundamental frequency is double that of the closed pipe)",
            "explanation": "For an open pipe, λ₁ = 2L => ν_open = v / 2L. For a closed pipe, λ₁' = 4L => ν_closed = v / 4L. Thus ν_open = 2 · ν_closed.",
            "hint": "Compare ν_open = v/2L and ν_closed = v/4L.",
            "blooms_level": "Apply",
            "textbook_reference": "Section 14.6, Page 291",
            "image_search_query": "fundamental frequency open vs closed pipe double"
        }
    ]

    # -------------------------------------------------------------
    # Module 87: Acoustic Beats: Derivation & Tuning Applications
    # -------------------------------------------------------------
    modules[4]["worked_examples"] = [
        {
            "problem": "NCERT Example 14.6: Two sitar strings A and B playing the note 'Dha' are slightly out of tune and produce beats of frequency 5 Hz. The tension of string B is slightly increased and the beat frequency is found to reduce to 3 Hz. If the original frequency of string A is 427 Hz, what is the original frequency of string B?",
            "given": "Original frequency of string A: ν_A = 427 Hz\nInitial beat frequency: ν_b = |ν_A - ν_B| = 5 Hz\nTension in string B (T_B) is increased => frequency of B (ν_B) increases (since ν ∝ √T)\nNew beat frequency: ν_b' = 3 Hz",
            "to_calculate": "Original frequency of string B, ν_B",
            "formula": "Beat frequency: ν_b = |ν_A - ν_B| => ν_B can be either:\nPossibility 1: ν_B = ν_A + 5 = 427 + 5 = 432 Hz\nPossibility 2: ν_B = ν_A - 5 = 427 - 5 = 422 Hz\nFrequency dependence on tension: ν_B ∝ √T_B. When T_B increases, ν_B must increase.",
            "substitution": "Test Possibility 1 (ν_B = 432 Hz):\nIf ν_B increases (say to 433 Hz), new beat frequency = |427 - 433| = 6 Hz (increases, contradicts observed decrease to 3 Hz).\nTest Possibility 2 (ν_B = 422 Hz):\nIf ν_B increases (say to 424 Hz), new beat frequency = |427 - 424| = 3 Hz (decreases, perfectly matches observed reduction to 3 Hz!).",
            "calculation": "Since increasing ν_B reduces the beat frequency from 5 Hz to 3 Hz, ν_B must originally have been lower than ν_A.\nTherefore: ν_B = ν_A - 5 = 427 - 5 = 422 Hz.",
            "rough_work": "[ROUGH_WORK]\n|427 - ν_B| = 5 => ν_B = 432 or 422.\nIncreasing T_B increases ν_B.\nIf ν_B was 432, increasing it makes beats 6, 7 Hz (wrong).\nIf ν_B was 422, increasing it brings it closer to 427, so beats become 4, 3 Hz (correct!).\nSo ν_B = 422 Hz.",
            "finalAnswer": "Original frequency of string B was 422 Hz",
            "unit": "Hz",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Example 14.6, Page 293",
            "image_search_query": "sitar strings tuning beats frequency calculation tension"
        },
        {
            "problem": "Starting from the principle of superposition, give the analytical derivation for the phenomenon of beats produced by two sound waves of equal amplitude a and slightly different angular frequencies ω₁ and ω₂. Show that the beat frequency is given by ν_b = |ν₁ - ν₂|.",
            "given": "Two sound waves at x = 0:\ns₁(t) = a · cos(ω₁ t)\ns₂(t) = a · cos(ω₂ t) where ω₁ ≈ ω₂",
            "to_calculate": "Derivation of modulated resultant displacement s(t) and beat frequency ν_b",
            "formula": "Superposition: s(t) = s₁(t) + s₂(t) = a [ cos(ω₁ t) + cos(ω₂ t) ]\nUsing identity cos C + cos D = 2 cos((C-D)/2) cos((C+D)/2):\ns(t) = [ 2a · cos((ω₁ - ω₂) t / 2) ] · cos((ω₁ + ω₂) t / 2)\nLet envelope amplitude: A(t) = 2a · cos(ω_mod · t) where ω_mod = (ω₁ - ω₂) / 2\nCarrier frequency: ω_avg = (ω₁ + ω₂) / 2",
            "substitution": "Intensity I(t) ∝ A(t)² = 4a² · cos²((ω₁ - ω₂) t / 2) = 2a² · [ 1 + cos((ω₁ - ω₂) t) ]",
            "calculation": "Intensity maxima occur whenever cos²((ω₁ - ω₂) t / 2) = 1, which happens when:\n(ω₁ - ω₂) t / 2 = m π => (2π ν₁ - 2π ν₂) t / 2 = m π => (ν₁ - ν₂) t = m for m = 0, 1, 2, ...\nTime interval between successive intensity maxima (beat period): T_b = t_(m+1) - t_m = 1 / |ν₁ - ν₂|\nBeat frequency: ν_b = 1 / T_b = |ν₁ - ν₂| (Hence Proved).",
            "rough_work": "[ROUGH_WORK]\ncos(w₁t) + cos(w₂t) = 2 cos((w₁-w₂)t/2) cos((w₁+w₂)t/2)\nIntensity ∝ cos² => period of cos² is pi / ((w₁-w₂)/2) = 2pi / (w₁-w₂) = 1 / (ν₁-ν₂)\nν_b = |ν₁ - ν₂|.",
            "finalAnswer": "Resultant wave: s(t) = [2a cos((ω₁-ω₂)t/2)] cos((ω₁+ω₂)t/2); Beat frequency ν_b = |ν₁ - ν₂| (Hence Proved)",
            "unit": "Hz, Analytical Derivation",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Section 14.7, Pages 292-293",
            "image_search_query": "acoustic beats envelope wave superposition derivation"
        }
    ]

    modules[4]["concept_questions"] = [
        {
            "question": "What is the maximum frequency difference between two sound notes for which the human ear can comfortably perceive distinct, periodic acoustic beats?",
            "options": [
                "(Recommended) Approximately 10 Hz (limited by the persistence of hearing of 0.1 s)",
                "Up to 200 Hz",
                "Over 1000 Hz",
                "Beats can be heard at any arbitrary frequency difference"
            ],
            "correctAnswer": "(Recommended) Approximately 10 Hz (limited by the persistence of hearing of 0.1 s)",
            "correct_answer": "(Recommended) Approximately 10 Hz (limited by the persistence of hearing of 0.1 s)",
            "explanation": "The human ear has a temporal persistence of hearing of approximately 0.1 s. If the beat frequency exceeds ~10 Hz (period < 0.1 s), successive intensity waxing and waning blend into a single continuous sensation of harsh consonance or dissonance.",
            "hint": "Recall the human persistence of hearing (1/10th of a second).",
            "blooms_level": "Understand",
            "textbook_reference": "Section 14.7, Page 293",
            "image_search_query": "persistence of hearing maximum beat frequency 10 hz"
        },
        {
            "question": "Two tuning forks A and B produce 4 beats per second. When a small amount of wax is attached to the prongs of fork A, the beat frequency decreases to 2 beats per second. If the frequency of fork B is 256 Hz, what is the frequency of fork A?",
            "options": [
                "(Recommended) 260 Hz",
                "252 Hz",
                "258 Hz",
                "254 Hz"
            ],
            "correctAnswer": "(Recommended) 260 Hz",
            "correct_answer": "(Recommended) 260 Hz",
            "explanation": "ν_A can be 256 + 4 = 260 Hz or 256 - 4 = 252 Hz. Loading wax onto fork A increases its mass, which reduces its frequency. If ν_A was 260 Hz, loading reduces it towards 256 Hz, decreasing the beat frequency to 2 Hz. (If it were 252 Hz, loading would reduce it further, increasing beats to 6 Hz). Hence ν_A = 260 Hz.",
            "hint": "Loading wax onto a tuning fork lowers its frequency.",
            "blooms_level": "Apply",
            "textbook_reference": "Section 14.7, Page 294",
            "image_search_query": "tuning fork loading wax beat frequency calculation"
        },
        {
            "question": "What musical application relies directly on the acoustic phenomenon of beats?",
            "options": [
                "(Recommended) Tuning musical instruments (pianos, violins, guitars, sitars) by adjusting tension until beats slow down to zero",
                "Amplifying sound using electronic loudspeakers",
                "Measuring the acoustic reverberation time of an auditorium",
                "Transmitting radio waves through satellite links"
            ],
            "correctAnswer": "(Recommended) Tuning musical instruments (pianos, violins, guitars, sitars) by adjusting tension until beats slow down to zero",
            "correct_answer": "(Recommended) Tuning musical instruments (pianos, violins, guitars, sitars) by adjusting tension until beats slow down to zero",
            "explanation": "Musicians sound a reference fork and the instrument string together. By adjusting the string tension, they bring the beat frequency closer and closer to zero. When beats completely disappear, perfect unison tuning is achieved.",
            "hint": "Think about tuning a string against a reference pitch.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 14.7, Page 294",
            "image_search_query": "tuning musical instruments acoustic beats unison"
        },
        {
            "question": "How is the amplitude of the envelope in a beat pattern related to the amplitudes a₁ and a₂ of the two interfering waves?",
            "options": [
                "(Recommended) It varies periodically between a maximum of (a₁ + a₂) and a minimum of |a₁ - a₂|",
                "It remains strictly constant at √(a₁² + a₂²)",
                "It varies between 2(a₁ + a₂) and zero",
                "It is inversely proportional to frequency difference"
            ],
            "correctAnswer": "(Recommended) It varies periodically between a maximum of (a₁ + a₂) and a minimum of |a₁ - a₂|",
            "correct_answer": "(Recommended) It varies periodically between a maximum of (a₁ + a₂) and a minimum of |a₁ - a₂|",
            "explanation": "When waves are in phase, amplitudes add constructively: A_max = a₁ + a₂. When exactly out of phase, they interfere destructively: A_min = |a₁ - a₂|. If a₁ = a₂, intensity drops completely to zero at the minima.",
            "hint": "Evaluate the envelope at constructive and destructive alignment.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 14.7, Page 293",
            "image_search_query": "beat envelope amplitude maximum minimum constructive destructive"
        }
    ]

    # -------------------------------------------------------------
    # Module 88: Comprehensive NCERT Exercises 14.1 to 14.22 Solver
    # -------------------------------------------------------------
    modules[5]["worked_examples"] = [
        {
            "problem": "NCERT Exercise 14.1: A string of mass 2.50 kg is under a tension of 200 N. The length of the stretched string is 20.0 m. If the transverse jerk is struck at one end of the string, how long does the disturbance take to reach the other end?",
            "given": "Mass of string M = 2.50 kg, Tension T = 200 N, Length of string L = 20.0 m",
            "to_calculate": "Time t taken by transverse pulse to travel length L",
            "formula": "Linear mass density: μ = M / L\nWave speed: v = √(T / μ) = √(T · L / M)\nTime of transit: t = L / v = L / √(T · L / M) = √(M · L / T)",
            "substitution": "μ = 2.50 kg / 20.0 m = 0.125 kg m⁻¹\nv = √(200 N / 0.125 kg m⁻¹)\nt = 20.0 m / v",
            "calculation": "v = √1600 = 40.0 m s⁻¹\nt = 20.0 m / 40.0 m s⁻¹ = 0.50 s",
            "rough_work": "[ROUGH_WORK]\nμ = 2.5 / 20 = 0.125 kg/m\nv = sqrt(200 / 0.125) = sqrt(1600) = 40 m/s\nt = 20 / 40 = 0.5 s.",
            "finalAnswer": "Time taken by disturbance to reach other end t = 0.50 s",
            "unit": "s",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.1, Page 298",
            "image_search_query": "transverse pulse string transit time calculation"
        },
        {
            "problem": "NCERT Exercise 14.2: A stone dropped from the top of a tower of height 300 m splashes into the water of a pond near the base of the tower. When is the splash heard at the top? Given that the speed of sound in air is 340 m s⁻¹ and g = 9.8 m s⁻².",
            "given": "Height of tower h = 300 m, Initial velocity of stone u = 0, Acceleration due to gravity g = 9.8 m s⁻², Speed of sound in air v_s = 340 m s⁻¹",
            "to_calculate": "Total elapsed time t_total = t₁ (stone fall) + t₂ (sound travel)",
            "formula": "1. Time for stone to fall: h = ½ g t₁² => t₁ = √(2h / g)\n2. Time for sound of splash to travel up: t₂ = h / v_s\n3. Total time: t_total = t₁ + t₂",
            "substitution": "t₁ = √(2 × 300 / 9.8) = √(600 / 9.8)\nt₂ = 300 m / 340 m s⁻¹",
            "calculation": "600 / 9.8 = 61.2245 s²\nt₁ = √61.2245 = 7.8246 s ≈ 7.82 s\nt₂ = 300 / 340 = 0.8824 s ≈ 0.88 s\nt_total = 7.8246 s + 0.8824 s = 8.707 s ≈ 8.71 s",
            "rough_work": "[ROUGH_WORK]\nt₁ = sqrt(600/9.8) = 7.825 s\nt₂ = 300/340 = 0.882 s\nt_total = 7.825 + 0.882 = 8.707 s ≈ 8.7 s.",
            "finalAnswer": "The splash is heard at the top after 8.71 s (or 8.7 s)",
            "unit": "s",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.2, Page 298",
            "image_search_query": "stone dropped tower splash heard sound time"
        },
        {
            "problem": "NCERT Exercise 14.3: A steel wire has a length of 12.0 m and a mass of 2.10 kg. What should be the tension in the wire so that speed of a transverse wave on the wire equals the speed of sound in dry air at 20 °C (which is 343 m s⁻¹)?",
            "given": "Length of wire L = 12.0 m, Mass of wire M = 2.10 kg, Desired wave speed v = 343 m s⁻¹",
            "to_calculate": "Required tension T in the wire",
            "formula": "Linear mass density: μ = M / L\nWave speed: v = √(T / μ) => v² = T / μ => T = μ · v² = (M / L) · v²",
            "substitution": "μ = 2.10 kg / 12.0 m = 0.175 kg m⁻¹\nT = (0.175 kg m⁻¹) × (343 m s⁻¹)²",
            "calculation": "(343)² = 117649 m² s⁻²\nT = 0.175 × 117649 = 20588.57 N ≈ 2.06 × 10⁴ N",
            "rough_work": "[ROUGH_WORK]\nμ = 2.1 / 12 = 0.175 kg/m\n343² = 117,649\nT = 0.175 × 117,649 = 20,588.6 N ≈ 2.06 × 10⁴ N.",
            "finalAnswer": "Tension required in the wire T = 2.06 × 10⁴ N",
            "unit": "N",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.3, Page 298",
            "image_search_query": "steel wire tension speed of sound calculation"
        },
        {
            "problem": "NCERT Exercise 14.4: Use the formula v = √(γ P / ρ) to explain why the speed of sound in air:\n(a) is independent of pressure,\n(b) increases with temperature,\n(c) increases with humidity.",
            "given": "Laplace formula for speed of sound: v = √(γ P / ρ)\nIdeal gas equation: P V = μ R T = (m / M) R T => P / ρ = R T / M",
            "to_calculate": "Scientific explanations for properties (a), (b), and (c)",
            "formula": "Substituting P / ρ = R T / M into Laplace's formula:\nv = √(γ · R · T / M)",
            "substitution": "Apply dependencies on P, T, and M",
            "calculation": "(a) Independent of pressure: From v = √(γRT/M), pressure P does not appear in the equation at a given temperature. If pressure P increases at constant T, density ρ increases in the exact same proportion (Boyle's law: P/ρ = constant), leaving the ratio P/ρ and therefore speed v unchanged.\n(b) Increases with temperature: v = √(γRT/M) ∝ √T. As absolute temperature T increases, the root-mean-square speed of molecules increases, which speeds up the propagation of compressional pulses.\n(c) Increases with humidity: Moist air contains water vapour (molar mass M_H₂O = 18 g/mol) displacing dry air molecules (nitrogen M = 28 g/mol and oxygen M = 32 g/mol, effective dry air M ≈ 29 g/mol). Thus humid air has a lower effective molar mass M (and lower density ρ at same P and T). Since v ∝ 1/√M, sound travels faster in humid air than in dry air.",
            "rough_work": "[ROUGH_WORK]\n(a) P/ρ = RT/M => independent of P at const T.\n(b) v ∝ √T => increases with T.\n(c) M_water (18) < M_air (29) => humid air lighter => v ∝ 1/√M increases.",
            "finalAnswer": "Explanations verified: (a) P/ρ is constant at constant T; (b) v ∝ √T; (c) Water vapour reduces effective molar mass M, so v ∝ 1/√M increases.",
            "unit": "Qualitative Derivation",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.4, Page 298",
            "image_search_query": "speed of sound dependence pressure temperature humidity"
        },
        {
            "problem": "NCERT Exercise 14.5: You have learnt that a travelling wave in one dimension is represented by a function y = f(x, t) where x and t must appear in the combination (x - vt) or (x + vt), i.e., y = f(x ± vt). Is the converse true? Examine if the following functions for y can possibly represent a travelling wave:\n(a) (x - vt)²\n(b) log[(x + vt) / x_0]\n(c) 1 / (x + vt)",
            "given": "Three mathematical functions of (x ± vt)",
            "to_calculate": "Determine if converse is true and examine validity of (a), (b), (c) as physical travelling waves",
            "formula": "A function represents a physical travelling wave ONLY IF:\n1. It depends on (x ± vt).\n2. It remains finite, single-valued, and bounded for all values of x and t (-∞ < x < ∞, t ≥ 0).",
            "substitution": "Examine boundedness as x ± vt → ±∞ or 0",
            "calculation": "Converse is NOT true in general: Not every function of (x ± vt) represents a physical wave.\n(a) y = (x - vt)²: As x → ∞ or t → ∞, y → ∞. The displacement diverges to infinity; hence it cannot represent a physical wave.\n(b) y = log[(x + vt) / x_0]: As (x + vt) → 0, y → -∞; as (x + vt) → ∞, y → +∞. The displacement diverges; hence it cannot represent a physical wave.\n(c) y = 1 / (x + vt): At x = -vt, y → ∞. The displacement blows up to infinity; hence it cannot represent a physical wave.\nConclusion: None of the three functions can represent a real physical travelling wave.",
            "rough_work": "[ROUGH_WORK]\nPhysical wave requires finite bounded displacement everywhere.\n(a) diverges as x -> inf.\n(b) diverges at 0 and inf.\n(c) diverges at x = -vt.\nConverse is false; none are valid physical waves.",
            "finalAnswer": "The converse is NOT true. None of the functions (a), (b), or (c) can represent a physical travelling wave because they are not bounded (they diverge to infinity).",
            "unit": "Mathematical Analysis",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.5, Page 298",
            "image_search_query": "travelling wave function condition finite bounded"
        },
        {
            "problem": "NCERT Exercise 14.6: A bat emits ultrasonic sound of frequency 1000 kHz in air. If the sound meets a water surface, what is the wavelength of (a) the reflected sound, and (b) the transmitted sound? Speed of sound in air is 340 m s⁻¹ and in water is 1486 m s⁻¹.",
            "given": "Frequency of ultrasound ν = 1000 kHz = 1.0 × 10⁶ Hz, Speed of sound in air v_air = 340 m s⁻¹, Speed of sound in water v_water = 1486 m s⁻¹",
            "to_calculate": "(a) Reflected wavelength λ_r (in air), (b) Transmitted wavelength λ_t (in water)",
            "formula": "Frequency ν is a characteristic of the vibrating source and remains strictly unchanged upon reflection and refraction across media.\nWavelength in a medium: λ = v / ν",
            "substitution": "(a) Reflected wave (in air): λ_r = v_air / ν = (340 m s⁻¹) / (1.0 × 10⁶ Hz)\n(b) Transmitted wave (in water): λ_t = v_water / ν = (1486 m s⁻¹) / (1.0 × 10⁶ Hz)",
            "calculation": "(a) λ_r = 340 × 10⁻⁶ m = 3.4 × 10⁻⁴ m = 0.34 mm\n(b) λ_t = 1486 × 10⁻⁶ m = 1.486 × 10⁻³ m = 1.49 mm",
            "rough_work": "[ROUGH_WORK]\nFrequency constant = 10⁶ Hz.\nλ_air = 340 / 10⁶ = 3.4 × 10⁻⁴ m = 0.34 mm.\nλ_water = 1486 / 10⁶ = 1.486 × 10⁻³ m = 1.49 mm.",
            "finalAnswer": "(a) Reflected wavelength in air λ_r = 3.4 × 10⁻⁴ m (0.34 mm); (b) Transmitted wavelength in water λ_t = 1.49 × 10⁻³ m (1.49 mm)",
            "unit": "m (or mm)",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.6, Page 298",
            "image_search_query": "ultrasonic sound reflection transmission water wavelength"
        },
        {
            "problem": "NCERT Exercise 14.7: A hospital uses an ultrasonic scanner to locate tumours in a tissue. What is the wavelength of sound in the tissue in which the speed of sound is 1.7 km s⁻¹? The operating frequency of the scanner is 4.2 MHz.",
            "given": "Speed of sound in tissue v = 1.7 km s⁻¹ = 1.7 × 10³ m s⁻¹ = 1700 m s⁻¹, Operating frequency ν = 4.2 MHz = 4.2 × 10⁶ Hz",
            "to_calculate": "Wavelength of ultrasound in tissue λ",
            "formula": "Wave relation: v = ν · λ => λ = v / ν",
            "substitution": "λ = (1.7 × 10³ m s⁻¹) / (4.2 × 10⁶ Hz)",
            "calculation": "λ = (1.7 / 4.2) × 10⁻³ m = 0.40476 × 10⁻³ m ≈ 4.05 × 10⁻⁴ m = 0.405 mm",
            "rough_work": "[ROUGH_WORK]\n1700 / (4.2 × 10⁶) = 1.7 / 4200 = 4.048 × 10⁻⁴ m ≈ 0.40 mm.",
            "finalAnswer": "Wavelength of sound in tissue λ = 4.05 × 10⁻⁴ m (or 0.41 mm)",
            "unit": "m (or mm)",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.7, Page 298",
            "image_search_query": "ultrasound scanner medical tissue wavelength calculation"
        },
        {
            "problem": "NCERT Exercise 14.8: A transverse harmonic wave on a string is described by:\ny(x, t) = 3.0 · sin(36 t + 0.018 x + π/4)\nwhere x and y are in cm and t in s. The positive direction of x is from left to right.\n(a) Is this a travelling wave or a stationary wave? If it is travelling, what are the speed and direction of its propagation?\n(b) What are its amplitude and frequency?\n(c) What is the initial phase at the origin?\n(d) What is the least distance between two successive crests in the wave?",
            "given": "Equation: y(x, t) = 3.0 sin(36 t + 0.018 x + π/4) with x, y in cm and t in s.\nCoefficients: a = 3.0 cm, ω = 36 rad s⁻¹, k = 0.018 rad cm⁻¹, φ_0 = π/4 rad",
            "to_calculate": "(a) Wave type, speed v, direction; (b) Amplitude a, frequency ν; (c) Initial phase φ_0; (d) Wavelength λ",
            "formula": "Standard progressive wave form: y = a · sin(ωt + kx + φ_0)\n(a) The argument is of form (ωt + kx) => travelling wave propagating in negative x-direction (right to left).\nSpeed: v = ω / k\n(b) Amplitude = a; Frequency ν = ω / 2π\n(c) Initial phase at x = 0, t = 0 is φ_0\n(d) Least distance between successive crests is wavelength: λ = 2π / k",
            "substitution": "(a) v = (36 rad s⁻¹) / (0.018 rad cm⁻¹)\n(b) a = 3.0 cm; ν = 36 / (2 × 3.1416) s⁻¹\n(c) φ_0 = π/4 rad (or 45°)\n(d) λ = 2π / (0.018 cm⁻¹)",
            "calculation": "(a) Travelling wave travelling from right to left (-x direction).\nSpeed: v = 36 / 0.018 = 2000 cm s⁻¹ = 20 m s⁻¹\n(b) Amplitude a = 3.0 cm = 0.030 m; Frequency ν = 36 / 6.2832 = 5.7296 Hz ≈ 5.73 Hz\n(c) Initial phase at origin = π/4 rad (45°)\n(d) Wavelength λ = 6.2832 / 0.018 = 349.07 cm ≈ 3.49 m",
            "rough_work": "[ROUGH_WORK]\nArgument (36t + 0.018x) => propagates in -x.\nv = 36 / 0.018 = 2000 cm/s = 20 m/s.\na = 3 cm, ν = 36 / 2pi = 5.73 Hz.\nφ = pi/4.\nλ = 2pi / 0.018 = 349 cm = 3.49 m.",
            "finalAnswer": "(a) Travelling wave propagating towards negative x (right to left) with speed 20 m s⁻¹; (b) Amplitude a = 3.0 cm, Frequency ν = 5.73 Hz; (c) Initial phase = π/4 rad; (d) Wavelength λ = 3.49 m",
            "unit": "m s⁻¹, cm, Hz, rad, m",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.8, Page 298",
            "image_search_query": "transverse harmonic wave propagation speed direction wavelength"
        },
        {
            "problem": "NCERT Exercise 14.9: For the wave described in Exercise 14.8 (y(x, t) = 3.0 sin(36 t + 0.018 x + π/4)), plot the displacement (y) versus (t) graphs for x = 0, 2 and 4 cm. What are the shapes of these graphs? In which aspects does the oscillatory motion in travelling wave differ from one point to another: amplitude, frequency or phase?",
            "given": "Equation: y(x, t) = 3.0 sin(36 t + 0.018 x + π/4) cm\nx values: x = 0 cm, x = 2 cm, x = 4 cm",
            "to_calculate": "Equations for y(t) at x = 0, 2, 4 cm, shapes of graphs, and comparison of amplitude, frequency, and phase",
            "formula": "At fixed x, y(t) = a · sin(ωt + φ(x)) where φ(x) = kx + π/4.",
            "substitution": "For x = 0: y_0(t) = 3.0 sin(36t + π/4) cm\nFor x = 2 cm: φ₂ = 0.018(2) + π/4 = 0.036 + 0.7854 = 0.8214 rad => y₂(t) = 3.0 sin(36t + 0.821) cm\nFor x = 4 cm: φ₄ = 0.018(4) + π/4 = 0.072 + 0.7854 = 0.8574 rad => y₄(t) = 3.0 sin(36t + 0.857) cm",
            "calculation": "Shapes: All three graphs are sinusoidal curves with the exact same amplitude (a = 3.0 cm) and the exact same time period (T = 2π/36 = 0.175 s, frequency ν = 5.73 Hz).\nComparison: In a travelling wave, all medium particles oscillate with identical amplitude (3.0 cm) and identical frequency (5.73 Hz). The oscillatory motion differs from one point to another ONLY in its phase (phase advances by Δφ = k · Δx).",
            "rough_work": "[ROUGH_WORK]\nAt fixed x, motion is SHM.\nAmplitude = 3 cm for all points.\nFrequency = 5.73 Hz for all points.\nPhase differs by k Δx.",
            "finalAnswer": "The graphs are sinusoidal waves. The oscillatory motion across points has identical amplitude and identical frequency; it differs ONLY in phase.",
            "unit": "Qualitative Graphical Analysis",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.9, Page 298",
            "image_search_query": "displacement time graph travelling wave phase difference"
        },
        {
            "problem": "NCERT Exercise 14.10: For the travelling harmonic wave:\ny(x, t) = 2.0 · cos 2π(10 t - 0.0080 x + 0.35)\nwhere x and y are in cm and t in s. Calculate the phase difference between oscillatory motion of two points separated by a distance of:\n(a) 4.0 m,\n(b) 0.50 m,\n(c) λ / 2,\n(d) 3λ / 4.",
            "given": "Wave equation: y(x, t) = 2.0 cos(20π t - 0.016π x + 0.70π) with x in cm, t in s.\nPropagation constant k = 2π × 0.0080 cm⁻¹ = 0.016π rad cm⁻¹ = 1.6π rad m⁻¹\nWavelength: λ = 2π / k = 2π / (0.016π cm⁻¹) = 1 / 0.0080 cm = 125 cm = 1.25 m\nSeparations: (a) Δx = 4.0 m = 400 cm, (b) Δx = 0.50 m = 50 cm, (c) Δx = λ/2, (d) Δx = 3λ/4",
            "to_calculate": "Phase difference Δφ = k · Δx = (2π / λ) · Δx for parts (a), (b), (c), and (d)",
            "formula": "Phase difference: Δφ = (2π / λ) · Δx = k · Δx",
            "substitution": "(a) Δφ = (2π / 1.25 m) × 4.0 m = (8.0 / 1.25) π\n(b) Δφ = (2π / 1.25 m) × 0.50 m = (1.0 / 1.25) π\n(c) Δφ = (2π / λ) × (λ / 2)\n(d) Δφ = (2π / λ) × (3λ / 4)",
            "calculation": "(a) Δφ = 6.4π rad = 20.11 rad\n(b) Δφ = 0.8π rad = (4/5)π rad = 2.51 rad\n(c) Δφ = π rad (180°)\n(d) Δφ = (3/2)π rad = 1.5π rad (270°)",
            "rough_work": "[ROUGH_WORK]\nλ = 1/0.008 cm = 125 cm = 1.25 m\n(a) Δx = 4 m => Δφ = 2pi × 4 / 1.25 = 6.4 pi = 20.1 rad\n(b) Δx = 0.5 m => Δφ = 2pi × 0.5 / 1.25 = 0.8 pi = 2.51 rad\n(c) λ/2 => pi rad\n(d) 3λ/4 => 1.5 pi rad.",
            "finalAnswer": "(a) Δφ = 6.4π rad (20.1 rad); (b) Δφ = 0.8π rad (2.51 rad); (c) Δφ = π rad; (d) Δφ = 1.5π rad (3π/2 rad)",
            "unit": "rad",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.10, Page 298",
            "image_search_query": "phase difference path difference wave formula"
        },
        {
            "problem": "NCERT Exercise 14.11: The transverse displacement of a string (clamped at both ends) is given by:\ny(x, t) = 0.06 · sin(2π x / 3) · cos(120π t)\nwhere x and y are in m and t in s. The length of the string is 1.5 m and its mass is 3.0 × 10⁻² kg.\nAnswer the following:\n(a) Does the function represent a travelling wave or a stationary wave?\n(b) Interpret the wave as a superposition of two waves travelling in opposite directions. What is the wavelength, frequency, and speed of each wave?\n(c) Determine the tension in the string.",
            "given": "Standing wave equation: y(x, t) = 0.06 sin((2π/3) x) cos(120π t) m\nLength of string L = 1.5 m, Mass M = 3.0 × 10⁻² kg",
            "to_calculate": "(a) Wave type, (b) Parameters of constituent travelling waves (λ, ν, v), (c) Tension T",
            "formula": "(a) Product of space-dependent sine and time-dependent cosine represents a stationary (standing) wave.\n(b) Using 2 sin A cos B = sin(A - B) + sin(A + B):\ny = 0.03 [ sin((2π/3) x - 120π t) + sin((2π/3) x + 120π t) ]\nConstituent parameters: k = 2π / 3 m⁻¹ => λ = 2π / k = 3.0 m; ω = 120π rad s⁻¹ => ν = ω / 2π = 60 Hz; Speed v = ν · λ = ω / k\n(c) Linear mass density μ = M / L; Wave speed v = √(T / μ) => T = μ · v²",
            "substitution": "(b) k = 2π/3 m⁻¹ => λ = 3.0 m; ω = 120π => ν = 60 Hz; v = 60 Hz × 3.0 m\n(c) μ = 3.0 × 10⁻² kg / 1.5 m = 2.0 × 10⁻² kg m⁻¹; T = (2.0 × 10⁻² kg m⁻¹) × (180 m s⁻¹)²",
            "calculation": "(a) Stationary (standing) wave.\n(b) Constituent waves: Wavelength λ = 3.0 m, Frequency ν = 60 Hz, Speed v = 180 m s⁻¹.\n(c) μ = 0.020 kg m⁻¹; v² = (180)² = 32400 m² s⁻²\nT = 0.020 × 32400 = 648 N.",
            "rough_work": "[ROUGH_WORK]\ny = 0.06 sin(kx) cos(wt) => standing wave.\nk = 2pi/3 => λ = 3 m\nw = 120pi => ν = 60 Hz\nv = w/k = 120pi / (2pi/3) = 180 m/s\nμ = 0.03 / 1.5 = 0.02 kg/m\nT = μ v² = 0.02 × 32400 = 648 N.",
            "finalAnswer": "(a) Stationary wave; (b) Each wave has λ = 3.0 m, ν = 60 Hz, v = 180 m s⁻¹; (c) Tension in the string T = 648 N",
            "unit": "m, Hz, m s⁻¹, N",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.11, Page 298",
            "image_search_query": "standing wave on clamped string tension calculation"
        },
        {
            "problem": "NCERT Exercise 14.12: (i) For the wave on a string described in Exercise 14.11 (y = 0.06 sin(2πx / 3) cos(120π t)), do all the points on the string oscillate with the same (a) frequency, (b) phase, (c) amplitude? Explain your answers.\n(ii) What is the amplitude of a point 0.375 m away from one end?",
            "given": "From Exercise 14.11: y(x, t) = 0.06 sin(2πx / 3) cos(120π t) m\nx = 0.375 m = 3/8 m",
            "to_calculate": "(i) Uniformity of frequency, phase, and amplitude across points, (ii) Numerical amplitude at x = 0.375 m",
            "formula": "Amplitude profile in standing wave: A(x) = |0.06 · sin(2πx / 3)|\nTime dependence: cos(120π t) is common to all positions.",
            "substitution": "(ii) A(0.375) = 0.06 × |sin( (2π / 3) × 0.375 )| = 0.06 × |sin( (2π / 3) × (3 / 8) )| = 0.06 × |sin(π / 4)|",
            "calculation": "(i) (a) Frequency: Yes. All points oscillate with the exact same frequency ν = 60 Hz.\n(b) Phase: Points situated within the same loop (between two consecutive nodes) oscillate in phase. Points in adjacent loops are 180° (π rad) out of phase.\n(c) Amplitude: No. Amplitude varies with position according to A(x) = 0.06 |sin(2πx/3)|, from zero at nodes to 0.06 m at antinodes.\n(ii) A = 0.06 × sin(π/4) = 0.06 × (1 / √2) = 0.06 × 0.7071 m = 0.0424 m = 4.24 cm ≈ 4.2 cm.",
            "rough_work": "[ROUGH_WORK]\n2pi/3 × 0.375 = 2pi/3 × 3/8 = pi/4\nsin(pi/4) = 1/sqrt(2) = 0.707\nA = 0.06 × 0.707 = 0.0424 m = 4.24 cm.",
            "finalAnswer": "(i) (a) Same frequency (60 Hz); (b) Phase is identical within a loop, opposite between adjacent loops; (c) Amplitudes differ with position; (ii) Amplitude at x = 0.375 m is 0.042 m (4.2 cm)",
            "unit": "cm (or m), Qualitative Analysis",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.12, Page 299",
            "image_search_query": "standing wave amplitude profile node loop phase"
        },
        {
            "problem": "NCERT Exercise 14.13: Given below are some functions of x and t to represent the displacement (transverse or longitudinal) of an elastic wave. State which of these represent (i) a travelling wave, (ii) a stationary wave or (iii) none at all:\n(a) y = 2 · cos(3x) · sin(10t)\n(b) y = 2 · √(x - vt)\n(c) y = 3 · sin(5x - 0.5t) + 4 · cos(5x - 0.5t)\n(d) y = cos x · sin t + cos 2x · sin 2t",
            "given": "Four mathematical displacement expressions",
            "to_calculate": "Classification into travelling wave, stationary wave, or none",
            "formula": "1. Stationary wave: Product of pure spatial harmonic and pure temporal harmonic: f(x) · g(t).\n2. Travelling wave: Harmonic function of linear combination (kx ± ωt).\n3. Non-wave: Divergent, non-harmonic, or non-bounded functions.",
            "substitution": "Inspect functional forms for each expression",
            "calculation": "(a) y = 2 cos(3x) sin(10t): Product of spatial harmonic cos(3x) and temporal harmonic sin(10t). Represents a STATIONARY WAVE.\n(b) y = 2 √(x - vt): Does not satisfy linear wave boundary conditions (unbounded as x → ∞, undefined for x < vt). Represents NONE AT ALL.\n(c) y = 3 sin(5x - 0.5t) + 4 cos(5x - 0.5t): Can be rewritten as 5 sin(5x - 0.5t + 0.927). Single harmonic travelling in +x direction. Represents a TRAVELLING WAVE.\n(d) y = cos x sin t + cos 2x sin 2t: Sum of two distinct stationary wave modes with different frequencies. While each term is stationary, the sum is a periodic non-harmonic standing vibration, typically classified as a superposition of STATIONARY WAVES.",
            "rough_work": "[ROUGH_WORK]\n(a) product of cos(3x) and sin(10t) => stationary wave.\n(b) sqrt(x-vt) not bounded => none.\n(c) 3 sin(u) + 4 cos(u) = 5 sin(u + phi) => travelling wave.\n(d) sum of two stationary waves.",
            "finalAnswer": "(a) Stationary wave; (b) None at all; (c) Travelling wave; (d) Superposition of stationary waves (Stationary)",
            "unit": "Classification",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.13, Page 299",
            "image_search_query": "classification travelling stationary wave functions"
        },
        {
            "problem": "NCERT Exercise 14.14: A wire stretched between two rigid supports vibrates in its fundamental mode with a frequency of 45 Hz. The mass of the wire is 3.5 × 10⁻² kg and its linear mass density is 4.0 × 10⁻² kg m⁻¹. What is (a) the speed of a transverse wave on the string, and (b) the tension in the string?",
            "given": "Fundamental frequency ν₁ = 45 Hz, Total mass M = 3.5 × 10⁻² kg, Linear mass density μ = 4.0 × 10⁻² kg m⁻¹",
            "to_calculate": "(a) Wave speed v, (b) Tension T",
            "formula": "Length of wire: L = M / μ\nFor fundamental mode of clamped string: L = λ₁ / 2 => λ₁ = 2L\n(a) Wave speed: v = ν₁ · λ₁ = 2 · ν₁ · L = 2 · ν₁ · (M / μ)\n(b) Wave speed on string: v = √(T / μ) => T = μ · v²",
            "substitution": "L = (3.5 × 10⁻² kg) / (4.0 × 10⁻² kg m⁻¹) = 3.5 / 4.0 = 0.875 m\n(a) v = 2 × 45 s⁻¹ × 0.875 m\n(b) T = (4.0 × 10⁻² kg m⁻¹) × (v)²",
            "calculation": "(a) L = 0.875 m; v = 90 × 0.875 = 78.75 m s⁻¹\n(b) v² = (78.75)² = 6201.56 m² s⁻²\nT = 0.040 × 6201.56 = 248.06 N ≈ 248 N",
            "rough_work": "[ROUGH_WORK]\nL = 3.5 / 4.0 = 0.875 m\nv = 2 × 45 × 0.875 = 78.75 m/s\nT = 0.04 × (78.75)² = 0.04 × 6201.56 = 248.06 N.",
            "finalAnswer": "(a) Wave speed v = 78.75 m s⁻¹ (≈ 78.8 m s⁻¹); (b) Tension T = 248 N",
            "unit": "m s⁻¹, N",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.14, Page 299",
            "image_search_query": "stretched wire fundamental frequency tension wave speed"
        },
        {
            "problem": "NCERT Exercise 14.15: A metre-long tube open at one end, with a movable piston at the other end, shows resonance with a fixed frequency source (a tuning fork of frequency 340 Hz) when the tube length is 25.5 cm or 79.3 cm. Estimate the speed of sound in air at the temperature of the experiment. The edge effects may be neglected.",
            "given": "Tuning fork frequency ν = 340 Hz, Resonant column lengths: l₁ = 25.5 cm = 0.255 m, l₂ = 79.3 cm = 0.793 m",
            "to_calculate": "Speed of sound in air v",
            "formula": "For a closed tube (closed by piston):\nFirst resonance (fundamental): l₁ + e = λ / 4\nSecond resonance (first overtone): l₂ + e = 3λ / 4\nSubtracting eliminates the end correction e:\nl₂ - l₁ = 3λ/4 - λ/4 = λ / 2 => λ = 2 · (l₂ - l₁)\nSpeed of sound: v = ν · λ = 2 · ν · (l₂ - l₁)",
            "substitution": "l₂ - l₁ = 0.793 m - 0.255 m = 0.538 m\nv = 2 × 340 s⁻¹ × 0.538 m",
            "calculation": "λ = 2 × 0.538 m = 1.076 m\nv = 680 × 0.538 = 345.84 m s⁻¹ ≈ 346 m s⁻¹",
            "rough_work": "[ROUGH_WORK]\nλ/2 = 79.3 - 25.5 = 53.8 cm = 0.538 m\nλ = 1.076 m\nv = 340 × 1.076 = 345.84 m/s ≈ 346 m/s.",
            "finalAnswer": "Speed of sound in air v = 345.8 m s⁻¹ (≈ 346 m s⁻¹)",
            "unit": "m s⁻¹",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.15, Page 299",
            "image_search_query": "resonance tube method speed of sound two resonances"
        },
        {
            "problem": "NCERT Exercise 14.16: A steel rod 100 cm long is clamped at its middle. The fundamental frequency of longitudinal vibrations of the rod is given to be 2.53 kHz. What is the speed of sound in steel?",
            "given": "Length of rod L = 100 cm = 1.0 m, Clamped at middle (displacement node at center x = L/2, free ends at x = 0 and x = L are displacement antinodes), Fundamental frequency ν = 2.53 kHz = 2.53 × 10³ Hz = 2530 Hz",
            "to_calculate": "Speed of sound v in steel",
            "formula": "For a rod clamped at its middle, the fundamental mode has:\nAntinode at one end, Node at center, Antinode at other end.\nDistance between two antinodes = λ / 2 = L => λ = 2L\nSpeed of sound: v = ν · λ = ν · (2L)",
            "substitution": "λ = 2 × 1.0 m = 2.0 m\nv = 2530 s⁻¹ × 2.0 m",
            "calculation": "v = 5060 m s⁻¹ = 5.06 km s⁻¹",
            "rough_work": "[ROUGH_WORK]\nCenter clamped: λ/2 = L => λ = 2L = 2 m\nv = ν λ = 2530 × 2 = 5060 m/s = 5.06 km/s.",
            "finalAnswer": "Speed of sound in steel v = 5060 m s⁻¹ (or 5.06 km s⁻¹)",
            "unit": "m s⁻¹ (or km s⁻¹)",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.16, Page 299",
            "image_search_query": "steel rod clamped at middle longitudinal vibration speed"
        },
        {
            "problem": "NCERT Exercise 14.17: A pipe 20 cm long is closed at one end. Which harmonic mode of the pipe is resonantly excited by a 430 Hz source? Will the same source be in resonance with the pipe if both ends are open? (Take speed of sound in air v = 340 m s⁻¹)",
            "given": "Length of pipe L = 20 cm = 0.20 m, Source frequency ν = 430 Hz, Speed of sound v = 340 m s⁻¹",
            "to_calculate": "(a) Resonant harmonic mode for closed pipe, (b) Resonance test for open pipe",
            "formula": "1. Closed pipe (closed at one end):\nNatural frequencies: ν_m = m · (v / 4L) for odd integers m = 1, 3, 5, ...\nFundamental frequency: ν₁ = v / 4L\n2. Open pipe (open at both ends):\nNatural frequencies: ν_n = n · (v / 2L) for n = 1, 2, 3, ...\nFundamental frequency: ν₁' = v / 2L",
            "substitution": "1. Closed pipe:\nν₁ = 340 / (4 × 0.20) = 340 / 0.80 = 425 Hz\nHarmonic order: m = ν / ν₁ = 430 / 425 = 1.012 ≈ 1 (Fundamental mode / First harmonic)\n2. Open pipe:\nν₁' = 340 / (2 × 0.20) = 340 / 0.40 = 850 Hz",
            "calculation": "1. For the closed pipe, the fundamental frequency is 425 Hz, which is approximately in resonance with the 430 Hz source (m = 1, first harmonic).\n2. For the open pipe, the fundamental frequency is 850 Hz. The source frequency 430 Hz is well below the fundamental mode (430 / 850 = 0.51, which is not an integer). Hence, NO resonance will occur with the open pipe.",
            "rough_work": "[ROUGH_WORK]\nClosed pipe: ν₁ = 340 / 0.8 = 425 Hz ≈ 430 Hz (m = 1, fundamental mode).\nOpen pipe: ν₁ = 340 / 0.4 = 850 Hz. 430 Hz is less than fundamental => no resonance.",
            "finalAnswer": "(a) The first harmonic (fundamental mode, m = 1) of the closed pipe is resonantly excited; (b) No, the open pipe cannot resonate with the 430 Hz source because its lowest resonant frequency is 850 Hz",
            "unit": "Harmonic mode, Resonance Analysis",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.17, Page 299",
            "image_search_query": "pipe closed at one end resonance harmonic mode"
        },
        {
            "problem": "NCERT Exercise 14.18: Two sitar strings A and B playing the note 'Ga' are slightly out of tune and produce beats of frequency 6 Hz. The tension in string A is slightly reduced and the beat frequency is found to reduce to 3 Hz. If the original frequency of A is 324 Hz, what is the frequency of B?",
            "given": "Original frequency of string A: ν_A = 324 Hz\nOriginal beat frequency: ν_b = |ν_A - ν_B| = 6 Hz\nTension in string A is reduced => frequency ν_A decreases (since ν ∝ √T)\nNew beat frequency: ν_b' = 3 Hz",
            "to_calculate": "Frequency of string B, ν_B",
            "formula": "ν_b = |ν_A - ν_B| => ν_B can be:\nPossibility 1: ν_B = ν_A + 6 = 324 + 6 = 330 Hz\nPossibility 2: ν_B = ν_A - 6 = 324 - 6 = 318 Hz\nWhen tension in A decreases, ν_A decreases (say from 324 Hz to 321 Hz).",
            "substitution": "Test Possibility 1 (ν_B = 330 Hz):\nIf ν_A decreases to 321 Hz, new beat frequency = |321 - 330| = 9 Hz (increases, contradicts reduction to 3 Hz).\nTest Possibility 2 (ν_B = 318 Hz):\nIf ν_A decreases to 321 Hz, new beat frequency = |321 - 318| = 3 Hz (decreases, matches observed reduction to 3 Hz!).",
            "calculation": "Because reducing ν_A decreases the beat frequency from 6 Hz to 3 Hz, ν_A must originally have been higher than ν_B.\nTherefore: ν_B = ν_A - 6 = 324 - 6 = 318 Hz.",
            "rough_work": "[ROUGH_WORK]\n|324 - ν_B| = 6 => ν_B = 330 or 318.\nDecreasing T_A decreases ν_A.\nIf ν_B = 330, lowering ν_A increases gap (beats increase to 7, 8, 9 Hz).\nIf ν_B = 318, lowering ν_A narrows gap (beats decrease from 6 to 3 Hz).\nHence ν_B = 318 Hz.",
            "finalAnswer": "The frequency of string B is 318 Hz",
            "unit": "Hz",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.18, Page 299",
            "image_search_query": "sitar strings beat frequency tension reduced calculation"
        },
        {
            "problem": "NCERT Exercise 14.19: Explain why (or how):\n(a) In a sound wave, a displacement node is a pressure antinode and vice versa.\n(b) Bats can ascertain distances, directions, nature, and sizes of obstacles without any 'eyes'.\n(c) A violin note and sitar note may have the same fundamental frequency, yet we can easily distinguish between the two notes.\n(d) Solids can support both longitudinal and transverse waves, but only longitudinal waves can propagate in gases.\n(e) The shape of a pulse gets distorted during propagation in a dispersive medium.",
            "given": "Five core conceptual principles of acoustics and wave dynamics",
            "to_calculate": "Rigorous scientific explanations for parts (a) through (e)",
            "formula": "(a) Acoustic excess pressure: ΔP = -B · (∂y / ∂x)\n(b) Echolocation: Δt = 2d / v; Doppler shift Δν = 2v_target ν / v\n(c) Timbre / Harmonic spectrum: Fourier harmonic series\n(d) Shear modulus G > 0 for solids; G = 0 for fluids\n(e) Dispersion: Phase velocity v(ω) depends on frequency ω",
            "substitution": "Scientific reasoning for each case",
            "calculation": "(a) Excess acoustic pressure is proportional to the negative spatial gradient of displacement: ΔP = -B (∂y/∂x). At a displacement node (y = 0), the gradient ∂y/∂x is maximum, producing maximum compression or rarefaction (pressure antinode). At a displacement antinode (y = max), ∂y/∂x = 0, so pressure variation is zero (pressure node).\n(b) Bats emit high-frequency ultrasonic chirps (20 to 100 kHz). By measuring the time delay Δt between emission and echo return (d = v Δt / 2), the bat gauges distance. By detecting subtle Doppler frequency shifts, it gauges obstacle velocity; and by analyzing relative echo intensities at its two ears, it determines direction and texture.\n(c) Tone quality (timbre) depends on the harmonic content (the number, frequencies, and relative amplitudes of overtones) accompanying the fundamental pitch. The physical construction, bow excitation (violin) vs plucked plectrum (sitar) generate completely distinct Fourier spectra, allowing our auditory cortex to distinguish them.\n(d) Transverse mechanical waves require a shear restoring force (non-zero shear modulus G). Solids have fixed crystalline lattices that resist shearing (G > 0). Gases have no fixed shape and slide freely under shear (G = 0), so only compressional (longitudinal) bulk modulus waves can propagate.\n(e) An arbitrary wave pulse is a Fourier packet composed of multiple harmonic Fourier components of differing frequencies. In a dispersive medium, wave speed depends on frequency (v = v(ω)). As the pulse travels, its high-frequency and low-frequency components travel at different speeds, spreading out and distorting the pulse envelope.",
            "rough_work": "[ROUGH_WORK]\n(a) ΔP = -B dy/dx => node in y is max in dy/dx (antinode in P).\n(b) Echolocation: time delay for distance, Doppler for speed.\n(c) Timbre: different harmonic overtone spectra.\n(d) Shear modulus non-zero in solids, zero in gases.\n(e) Dispersion: v depends on w, Fourier components separate.",
            "finalAnswer": "Explanations verified: (a) ΔP = -B(∂y/∂x); (b) Ultrasonic echolocation; (c) Timbre and harmonic overtone content; (d) Non-zero shear modulus in solids vs G = 0 in gases; (e) Frequency-dependent phase velocity v(ω) separates Fourier components.",
            "unit": "Qualitative Conceptual Explanations",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Exercise 14.19, Page 299",
            "image_search_query": "displacement node pressure antinode bats echolocation timbre dispersion"
        },
        {
            "problem": "NCERT Exercise 14.20: A train, sounding its whistle at a frequency of 400 Hz, approaches a stationary observer on a platform with a speed of 20 m s⁻¹. Calculate (a) the apparent frequency heard by the observer as the train approaches, and (b) the apparent frequency heard by the observer after the train passes by and recedes at 20 m s⁻¹. (Take speed of sound in air v = 340 m s⁻¹)",
            "given": "Source frequency ν_0 = 400 Hz, Speed of source v_s = 20 m s⁻¹, Speed of sound v = 340 m s⁻¹, Observer is stationary (v_o = 0)",
            "to_calculate": "(a) Apparent frequency on approach ν_app, (b) Apparent frequency on recession ν_rec",
            "formula": "Doppler effect in sound:\n(a) Source approaching stationary observer:\nν_app = ν_0 · [ v / (v - v_s) ]\n(b) Source receding from stationary observer:\nν_rec = ν_0 · [ v / (v + v_s) ]",
            "substitution": "(a) ν_app = 400 Hz × [ 340 / (340 - 20) ] = 400 × (340 / 320)\n(b) ν_rec = 400 Hz × [ 340 / (340 + 20) ] = 400 × (340 / 360)",
            "calculation": "(a) ν_app = 400 × 1.0625 = 425 Hz\n(b) ν_rec = 400 × (17 / 18) = 6800 / 18 = 377.78 Hz ≈ 378 Hz",
            "rough_work": "[ROUGH_WORK]\nApproach: 400 × 340 / 320 = 400 × 17/16 = 425 Hz\nRecede: 400 × 340 / 360 = 400 × 17/18 = 377.78 Hz.",
            "finalAnswer": "(a) Frequency on approach ν_app = 425 Hz; (b) Frequency on recession ν_rec = 378 Hz",
            "unit": "Hz",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Additional Exercise 14.20",
            "image_search_query": "doppler effect train whistle approach recede calculation"
        },
        {
            "problem": "NCERT Exercise 14.21: A sonar system installed in a submarine operates at a frequency of 40.0 kHz. An enemy submarine is moving towards the sonar with a speed of 360 km h⁻¹. What is the frequency of the sound reflected by the enemy submarine as detected by the observer on the first submarine? (Take speed of sound in water v = 1450 m s⁻¹)",
            "given": "Source frequency ν_0 = 40.0 kHz = 4.0 × 10⁴ Hz, Speed of sound in water v = 1450 m s⁻¹, Speed of target submarine v_t = 360 km h⁻¹ = 360 × (5/18) m s⁻¹ = 100 m s⁻¹ (moving towards sonar)",
            "to_calculate": "Reflected frequency detected by the first submarine ν''",
            "formula": "Step 1: Frequency received by moving target (acting as moving observer approaching source):\nν' = ν_0 · [ (v + v_t) / v ]\nStep 2: The target reflects this sound, acting as a moving source approaching the stationary detector:\nν'' = ν' · [ v / (v - v_t) ] = ν_0 · [ (v + v_t) / (v - v_t) ]",
            "substitution": "ν'' = (40.0 kHz) × [ (1450 + 100) / (1450 - 100) ] = 40.0 × (1550 / 1350)",
            "calculation": "1550 / 1350 = 31 / 27 ≈ 1.14815\nν'' = 40.0 kHz × 1.14815 = 45.926 kHz ≈ 45.93 kHz",
            "rough_work": "[ROUGH_WORK]\nv_t = 360 × 5/18 = 100 m/s\nν'' = 40 × (1450 + 100) / (1450 - 100) = 40 × 1550 / 1350 = 40 × 31/27 = 45.926 kHz.",
            "finalAnswer": "Frequency of reflected signal detected by sonar ν'' = 45.93 kHz (or 45.9 kHz)",
            "unit": "kHz",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Additional Exercise 14.21",
            "image_search_query": "sonar doppler effect submarine moving target frequency"
        },
        {
            "problem": "NCERT Exercise 14.22: Earthquakes generate sound waves inside the Earth. Unlike a gas, the Earth can experience both transverse (S) and longitudinal (P) sound waves. Typically the speed of P waves is about 8.0 km s⁻¹, and that of S waves is about 4.5 km s⁻¹. A seismograph records P and S waves from an earthquake. The first P wave arrives 4.0 minutes before the first S wave. Assuming the waves travel in straight lines, at what distance does the earthquake occur?",
            "given": "Speed of longitudinal P waves v_P = 8.0 km s⁻¹ = 8000 m s⁻¹\nSpeed of transverse S waves v_S = 4.5 km s⁻¹ = 4500 m s⁻¹\nTime delay between arrivals: Δt = t_S - t_P = 4.0 min = 4.0 × 60 s = 240 s",
            "to_calculate": "Distance d to the earthquake epicenter",
            "formula": "Time taken by P wave: t_P = d / v_P\nTime taken by S wave: t_S = d / v_S\nTime lag: Δt = t_S - t_P = d / v_S - d / v_P = d · [ (v_P - v_S) / (v_P · v_S) ]\nEpicenter distance: d = Δt · [ (v_P · v_S) / (v_P - v_S) ]",
            "substitution": "d = 240 s × [ (8.0 km s⁻¹ × 4.5 km s⁻¹) / (8.0 km s⁻¹ - 4.5 km s⁻¹) ] = 240 × [ 36.0 / 3.5 ] km",
            "calculation": "36.0 / 3.5 = 10.2857 km s⁻¹\nd = 240 × 10.2857 = 2468.57 km ≈ 2469 km ≈ 2.47 × 10³ km",
            "rough_work": "[ROUGH_WORK]\nΔt = 240 s\nv_P = 8 km/s, v_S = 4.5 km/s\n1/4.5 - 1/8 = (8 - 4.5) / 36 = 3.5 / 36\nd = 240 × 36 / 3.5 = 8640 / 3.5 = 2468.57 km.",
            "finalAnswer": "The earthquake occurred at a distance of 2470 km (2.47 × 10⁶ m)",
            "unit": "km (or m)",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 14, Additional Exercise 14.22",
            "image_search_query": "seismic waves p and s wave earthquake epicenter distance"
        }
    ]

    modules[5]["concept_questions"] = [
        {
            "question": "In NCERT Exercise 14.2, why is the splash from a 300 m high tower heard after 8.71 s rather than just the free-fall time of 7.82 s?",
            "options": [
                "(Recommended) Because sound takes an additional 0.88 s to travel the 300 m distance from the pond back up to the top of the tower at 340 m/s",
                "Because air drag increases the falling time of the stone",
                "Because water surface tension delays the impact",
                "Because the speed of sound decreases with altitude"
            ],
            "correctAnswer": "(Recommended) Because sound takes an additional 0.88 s to travel the 300 m distance from the pond back up to the top of the tower at 340 m/s",
            "correct_answer": "(Recommended) Because sound takes an additional 0.88 s to travel the 300 m distance from the pond back up to the top of the tower at 340 m/s",
            "explanation": "Total elapsed time is t_total = t_fall + t_sound. The stone takes t₁ = √(2h/g) = 7.82 s to fall. The acoustic splash pulse then travels upward at 340 m/s, taking t₂ = 300/340 = 0.88 s. Total time = 7.82 + 0.88 = 8.70 s.",
            "hint": "Remember sound has a finite propagation speed of 340 m/s.",
            "blooms_level": "Understand",
            "textbook_reference": "Exercise 14.2, Page 298",
            "image_search_query": "stone splash time fall time sound transit time"
        },
        {
            "question": "In NCERT Exercise 14.15, when measuring the speed of sound with a resonance tube, why does taking the difference between two resonant lengths (l₂ - l₁ = λ/2) eliminate the end correction error?",
            "options": [
                "(Recommended) Because the acoustic antinode extends slightly beyond the tube edge by the identical end correction e for both resonances (l₁ + e = λ/4 and l₂ + e = 3λ/4), which cancels out completely upon subtraction",
                "Because end correction vanishes at frequencies above 300 Hz",
                "Because the movable piston reflects sound with zero phase shift",
                "Because wavelength doubles inside the tube"
            ],
            "correctAnswer": "(Recommended) Because the acoustic antinode extends slightly beyond the tube edge by the identical end correction e for both resonances (l₁ + e = λ/4 and l₂ + e = 3λ/4), which cancels out completely upon subtraction",
            "correct_answer": "(Recommended) Because the acoustic antinode extends slightly beyond the tube edge by the identical end correction e for both resonances (l₁ + e = λ/4 and l₂ + e = 3λ/4), which cancels out completely upon subtraction",
            "explanation": "Due to air inertia at the open lip, the displacement antinode forms at distance e ≈ 0.6r outside the tube. Writing l₁ + e = λ/4 and l₂ + e = 3λ/4, subtracting gives (l₂ + e) - (l₁ + e) = l₂ - l₁ = λ/2, eliminating e entirely.",
            "hint": "Subtract the two resonance equations containing end correction e.",
            "blooms_level": "Analyze",
            "textbook_reference": "Exercise 14.15, Page 299",
            "image_search_query": "resonance tube end correction cancellation difference"
        },
        {
            "question": "Why does a 100 cm steel rod clamped at its center have a fundamental wavelength of 200 cm (NCERT Exercise 14.16), rather than 100 cm?",
            "options": [
                "(Recommended) Clamping at the middle creates a displacement node at the center and antinodes at both free ends, making the length of the rod equal to half a wavelength (L = λ/2 => λ = 2L)",
                "Because steel has twice the density of aluminum",
                "Because longitudinal waves reflect with a phase shift of 360°",
                "Because sound travels in opposite directions simultaneously"
            ],
            "correctAnswer": "(Recommended) Clamping at the middle creates a displacement node at the center and antinodes at both free ends, making the length of the rod equal to half a wavelength (L = λ/2 => λ = 2L)",
            "correct_answer": "(Recommended) Clamping at the middle creates a displacement node at the center and antinodes at both free ends, making the length of the rod equal to half a wavelength (L = λ/2 => λ = 2L)",
            "explanation": "The distance between the two free-end antinodes is L. In any standing wave, the distance between two consecutive antinodes with one node in between is λ/2. Thus L = λ/2 => λ = 2L = 200 cm.",
            "hint": "Analyze the distance between two antinodes with a single node between them.",
            "blooms_level": "Understand",
            "textbook_reference": "Exercise 14.16, Page 299",
            "image_search_query": "rod clamped middle standing wave lambda 2L"
        },
        {
            "question": "In NCERT Exercise 14.22, how do seismologists determine the exact distance to an earthquake epicenter using P and S seismic waves?",
            "options": [
                "(Recommended) By measuring the time lag Δt between the arrival of fast P-waves (8.0 km/s) and slower S-waves (4.5 km/s), using d = Δt · (v_P · v_S) / (v_P - v_S)",
                "By measuring the frequency of surface Rayleigh waves",
                "By measuring the total amplitude of ground acceleration",
                "By recording the temperature rise of the bedrock"
            ],
            "correctAnswer": "(Recommended) By measuring the time lag Δt between the arrival of fast P-waves (8.0 km/s) and slower S-waves (4.5 km/s), using d = Δt · (v_P · v_S) / (v_P - v_S)",
            "correct_answer": "(Recommended) By measuring the time lag Δt between the arrival of fast P-waves (8.0 km/s) and slower S-waves (4.5 km/s), using d = Δt · (v_P · v_S) / (v_P - v_S)",
            "explanation": "Because longitudinal P-waves travel much faster (8.0 km/s) than transverse S-waves (4.5 km/s), the time lag Δt between their first arrivals widens linearly with distance: Δt = d(1/v_S - 1/v_P). A single station determines distance d, and three stations triangulate the exact location.",
            "hint": "Relate distance d to the difference in arrival times.",
            "blooms_level": "Apply",
            "textbook_reference": "Exercise 14.22, Page 299",
            "image_search_query": "earthquake epicenter triangulation p and s wave arrival time"
        },
        {
            "question": "In NCERT Exercise 14.18, why must the original frequency of sitar string B be 318 Hz rather than 330 Hz when beats reduce from 6 Hz to 3 Hz as tension in A is decreased?",
            "options": [
                "(Recommended) Because reducing tension in A lowers its frequency from 324 Hz towards 318 Hz, narrowing the frequency gap from 6 Hz to 3 Hz",
                "Because string B is made of brass which has lower natural pitch",
                "Because beat frequency is always the sum of frequencies",
                "Because decreasing tension increases frequency"
            ],
            "correctAnswer": "(Recommended) Because reducing tension in A lowers its frequency from 324 Hz towards 318 Hz, narrowing the frequency gap from 6 Hz to 3 Hz",
            "correct_answer": "(Recommended) Because reducing tension in A lowers its frequency from 324 Hz towards 318 Hz, narrowing the frequency gap from 6 Hz to 3 Hz",
            "explanation": "Since ν ∝ √T, decreasing tension in string A lowers its frequency below 324 Hz. If ν_B were 330 Hz, lowering ν_A would widen the difference (increasing beats to 7, 8 Hz). Since beats decreased to 3 Hz, ν_A moved closer to ν_B, meaning ν_B must be 318 Hz.",
            "hint": "Determine whether lowering ν_A brings it closer to or farther from ν_B.",
            "blooms_level": "Analyze",
            "textbook_reference": "Exercise 14.18, Page 299",
            "image_search_query": "sitar string beat frequency decrease tuning tension"
        },
        {
            "question": "For the travelling wave y(x, t) = 2.0 cos 2π(10 t - 0.0080 x + 0.35) in NCERT Exercise 14.10, what is the phase difference between two points separated by half a wavelength (Δx = λ / 2)?",
            "options": [
                "(Recommended) π radians (180°)",
                "2π radians (360°)",
                "π / 2 radians (90°)",
                "3π / 4 radians (135°)"
            ],
            "correctAnswer": "(Recommended) π radians (180°)",
            "correct_answer": "(Recommended) π radians (180°)",
            "explanation": "Phase difference Δφ = (2π / λ) · Δx. For Δx = λ / 2: Δφ = (2π / λ) · (λ / 2) = π radians (180°). Two points half a wavelength apart always oscillate in exact antiphase.",
            "hint": "Substitute Δx = λ/2 into Δφ = (2π/λ) Δx.",
            "blooms_level": "Understand",
            "textbook_reference": "Exercise 14.10, Page 298",
            "image_search_query": "phase difference half wavelength pi radians antiphase"
        }
    ]

    with open("scripts/physics_class11_modules/physics_modules_ch14.json", "w", encoding="utf-8") as f:
        json.dump(modules, f, indent=2, ensure_ascii=False)
    print("Chapter 14 successfully enriched!")

if __name__ == "__main__":
    build_ch14()
