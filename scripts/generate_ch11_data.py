import json

def build_ch11():
    with open("scripts/physics_class11_modules/physics_modules_ch11.json", "r", encoding="utf-8") as f:
        modules = json.load(f)

    # -------------------------------------------------------------
    # Module 65: Thermal Equilibrium, Zeroth Law & First Law
    # -------------------------------------------------------------
    modules[0]["worked_examples"] = [
        {
            "problem": "A 10.0 kg lead block falls from a height of 20.0 m onto an insulated concrete floor. Assuming 80% of its mechanical energy is converted into internal thermal energy of the lead block upon impact, calculate the temperature rise of the lead block. (Take specific heat capacity of lead c = 130 J kg⁻¹ K⁻¹, g = 9.8 m s⁻²)",
            "given": "Mass of lead block m = 10.0 kg, Fall height h = 20.0 m, Fraction of energy converted η = 80% = 0.80, Specific heat capacity of lead c = 130 J kg⁻¹ K⁻¹, Acceleration due to gravity g = 9.8 m s⁻²",
            "to_calculate": "Temperature rise ΔT of the lead block",
            "formula": "Mechanical energy lost ΔE = m · g · h; Thermal energy absorbed ΔQ = 0.80 · ΔE = m · c · ΔT => ΔT = (0.80 · g · h) / c",
            "substitution": "ΔT = (0.80 × 9.8 m s⁻² × 20.0 m) / (130 J kg⁻¹ K⁻¹)",
            "calculation": "Numerator = 0.80 × 9.8 × 20.0 = 156.8 J kg⁻¹; Denominator = 130 J kg⁻¹ K⁻¹; ΔT = 156.8 / 130 = 1.206 K ≈ 1.21 K",
            "rough_work": "[ROUGH_WORK]\n156.8 / 130 = 1.20615...\nRounding to 2 decimal places: 1.21 °C or 1.21 K.",
            "finalAnswer": "The temperature rise of the lead block is 1.21 K (or 1.21 °C)",
            "unit": "K (or °C)",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Section 11.4 & 11.5, Page 229",
            "image_search_query": "first law thermodynamics heat work internal energy"
        },
        {
            "problem": "A thermodynamic system absorbs 500 J of heat from its surroundings while expanding quasi-statically against a constant external pressure of 1.013 × 10⁵ Pa from an initial volume of 2.0 × 10⁻³ m³ to a final volume of 5.0 × 10⁻³ m³. Calculate (a) the work done by the gas, and (b) the change in internal energy of the system.",
            "given": "Heat absorbed ΔQ = +500 J, Constant pressure P = 1.013 × 10⁵ Pa, Initial volume V₁ = 2.0 × 10⁻³ m³, Final volume V₂ = 5.0 × 10⁻³ m³",
            "to_calculate": "(a) Work done by the gas ΔW, (b) Change in internal energy ΔU",
            "formula": "(a) ΔW = P · ΔV = P · (V₂ - V₁)\n(b) First Law of Thermodynamics: ΔQ = ΔU + ΔW => ΔU = ΔQ - ΔW",
            "substitution": "(a) ΔW = (1.013 × 10⁵ Pa) × (5.0 × 10⁻³ m³ - 2.0 × 10⁻³ m³) = 1.013 × 10⁵ × 3.0 × 10⁻³ J\n(b) ΔU = 500 J - 303.9 J",
            "calculation": "(a) ΔW = 1.013 × 10⁵ × 3.0 × 10⁻³ = 303.9 J\n(b) ΔU = 500 - 303.9 = +196.1 J",
            "rough_work": "[ROUGH_WORK]\nΔV = 3.0 × 10⁻³ m³\nΔW = 101300 × 0.003 = 303.9 J\nΔU = 500 - 303.9 = 196.1 J",
            "finalAnswer": "(a) Work done by gas ΔW = 303.9 J; (b) Change in internal energy ΔU = +196.1 J",
            "unit": "J",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Section 11.5, Page 230",
            "image_search_query": "quasi-static expansion pv work diagram"
        }
    ]

    modules[0]["concept_questions"] = [
        {
            "question": "Two separate thermodynamic systems A and B are each in thermal equilibrium with a third system C. According to the Zeroth Law of Thermodynamics, what can be definitively concluded about systems A and B?",
            "options": [
                "(Recommended) Systems A and B are in thermal equilibrium with each other",
                "Systems A and B must have the exact same internal energy",
                "Systems A and B must have the exact same volume and pressure",
                "Heat must flow continuously from A to B through C"
            ],
            "correctAnswer": "(Recommended) Systems A and B are in thermal equilibrium with each other",
            "correct_answer": "(Recommended) Systems A and B are in thermal equilibrium with each other",
            "explanation": "The Zeroth Law states that if systems A and B are separately in thermal equilibrium with C, then A and B are in thermal equilibrium with each other. This defines temperature as the universal state variable determining thermal equilibrium.",
            "hint": "Recall the fundamental postulate of temperature equality.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 11.3, Page 228",
            "image_search_query": "zeroth law thermodynamics thermal equilibrium"
        },
        {
            "question": "Which of the following physical quantities is a state variable (state function) rather than a path-dependent function in thermodynamics?",
            "options": [
                "(Recommended) Internal Energy (U)",
                "Heat exchanged (Q)",
                "Mechanical work done (W)",
                "Heat capacity during a polytropic path"
            ],
            "correctAnswer": "(Recommended) Internal Energy (U)",
            "correct_answer": "(Recommended) Internal Energy (U)",
            "explanation": "Internal energy U depends strictly on the thermodynamic state (P, V, T) and its change ΔU is independent of the path taken between states. Q and W depend explicitly on the specific trajectory.",
            "hint": "Consider which variable has a unique value at every point on an indicator diagram.",
            "blooms_level": "Analyze",
            "textbook_reference": "Section 11.4, Page 229",
            "image_search_query": "thermodynamic state function path function"
        },
        {
            "question": "An ideal gas undergoes a complete cyclic process returning to its initial state. What is the net change in internal energy ΔU and the relation between total heat absorbed Q and total work done W?",
            "options": [
                "(Recommended) ΔU = 0 and Q = W",
                "ΔU > 0 and Q > W",
                "ΔU < 0 and Q = -W",
                "ΔU = Q + W where W is always zero"
            ],
            "correctAnswer": "(Recommended) ΔU = 0 and Q = W",
            "correct_answer": "(Recommended) ΔU = 0 and Q = W",
            "explanation": "Since internal energy U is a state function, its net change around any closed cycle is zero (ΔU = 0). By First Law ΔQ = ΔU + ΔW, we obtain Q_net = W_net.",
            "hint": "Evaluate the net change of a state function around a closed path.",
            "blooms_level": "Apply",
            "textbook_reference": "Section 11.5, Page 230",
            "image_search_query": "cyclic process first law thermodynamics"
        },
        {
            "question": "During an adiabatic compression of a gas, 250 J of mechanical work is performed on the gas by an external piston. What is the change in internal energy ΔU of the gas?",
            "options": [
                "(Recommended) +250 J (temperature increases)",
                "-250 J (temperature decreases)",
                "0 J (temperature remains constant)",
                "+500 J (double the mechanical work)"
            ],
            "correctAnswer": "(Recommended) +250 J (temperature increases)",
            "correct_answer": "(Recommended) +250 J (temperature increases)",
            "explanation": "In an adiabatic process, heat transfer ΔQ = 0. By the First Law: ΔQ = ΔU + ΔW => 0 = ΔU + (-250 J) => ΔU = +250 J. Work done on the gas increases internal energy, raising its temperature.",
            "hint": "Use ΔQ = 0 and note that work done on the gas corresponds to ΔW = -250 J.",
            "blooms_level": "Apply",
            "textbook_reference": "Section 11.5, Page 230",
            "image_search_query": "adiabatic compression work internal energy"
        }
    ]

    # -------------------------------------------------------------
    # Module 66: Specific Heat Capacities of Gases & Mayer's Relation
    # -------------------------------------------------------------
    modules[1]["worked_examples"] = [
        {
            "problem": "Starting from the First Law of Thermodynamics for 1 mole of an ideal gas, derive Mayer's relation C_p - C_v = R. Using this relation, determine the molar heat capacities at constant volume (C_v) and constant pressure (C_p), along with their ratio γ = C_p / C_v, for (a) Helium (monatomic, 3 translational degrees of freedom) and (b) Nitrogen (diatomic, 5 degrees of freedom at room temperature). (Take R = 8.314 J mol⁻¹ K⁻¹)",
            "given": "Number of moles μ = 1 mol, Ideal gas equation P · V = R · T, Internal energy for degree of freedom f: U = (f/2) · R · T, Universal gas constant R = 8.314 J mol⁻¹ K⁻¹",
            "to_calculate": "Derivation of C_p - C_v = R, and numerical values of C_v, C_p, and γ for monatomic and diatomic gases",
            "formula": "First Law: dQ = dU + P · dV. At constant volume (dV = 0): C_v = (dQ/dT)_v = dU/dT. At constant pressure: C_p = (dQ/dT)_p = dU/dT + P(dV/dT)_p. Since P · V = R · T => P(dV/dT)_p = R. Hence C_p = C_v + R => C_p - C_v = R.\nEquipartition: C_v = (f/2) · R, C_p = ((f+2)/2) · R, γ = C_p / C_v = 1 + 2/f.",
            "substitution": "(a) Monatomic (f = 3): C_v = (3/2) · 8.314 J mol⁻¹ K⁻¹; C_p = (5/2) · 8.314 J mol⁻¹ K⁻¹; γ = 5/3 ≈ 1.67\n(b) Diatomic (f = 5): C_v = (5/2) · 8.314 J mol⁻¹ K⁻¹; C_p = (7/2) · 8.314 J mol⁻¹ K⁻¹; γ = 7/5 = 1.40",
            "calculation": "(a) Monatomic:\nC_v = 1.5 × 8.314 = 12.47 J mol⁻¹ K⁻¹\nC_p = 2.5 × 8.314 = 20.785 J mol⁻¹ K⁻¹\nγ = 20.785 / 12.47 = 1.667\n(b) Diatomic:\nC_v = 2.5 × 8.314 = 20.785 J mol⁻¹ K⁻¹\nC_p = 3.5 × 8.314 = 29.099 J mol⁻¹ K⁻¹\nγ = 29.099 / 20.785 = 1.400",
            "rough_work": "[ROUGH_WORK]\n1.5 × 8.314 = 12.471 J/(mol K)\n2.5 × 8.314 = 20.785 J/(mol K)\n3.5 × 8.314 = 29.099 J/(mol K)\nγ_mono = 5/3 = 1.67, γ_dia = 7/5 = 1.40.",
            "finalAnswer": "(a) Helium (Monatomic): C_v = 12.47 J mol⁻¹ K⁻¹, C_p = 20.79 J mol⁻¹ K⁻¹, γ = 1.67; (b) Nitrogen (Diatomic): C_v = 20.79 J mol⁻¹ K⁻¹, C_p = 29.10 J mol⁻¹ K⁻¹, γ = 1.40",
            "unit": "J mol⁻¹ K⁻¹",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Section 11.6, Page 231",
            "image_search_query": "mayer relation cp cv r derivation"
        },
        {
            "problem": "Calculate the amount of heat required to raise the temperature of 2.0 moles of an ideal diatomic gas from 25 °C to 75 °C at (a) constant volume, and (b) constant pressure. Also calculate the external work performed by the gas in case (b). (Take R = 8.314 J mol⁻¹ K⁻¹, C_v = 20.79 J mol⁻¹ K⁻¹)",
            "given": "Number of moles μ = 2.0 mol, Initial temperature T₁ = 25 °C = 298.15 K, Final temperature T₂ = 75 °C = 348.15 K => ΔT = 50.0 K, C_v = 20.79 J mol⁻¹ K⁻¹, R = 8.314 J mol⁻¹ K⁻¹",
            "to_calculate": "(a) Heat absorbed at constant volume Q_v, (b) Heat absorbed at constant pressure Q_p, (c) Work done W_p",
            "formula": "(a) Q_v = μ · C_v · ΔT\n(b) Q_p = μ · C_p · ΔT = μ · (C_v + R) · ΔT\n(c) W_p = Q_p - Q_v = μ · R · ΔT",
            "substitution": "(a) Q_v = 2.0 mol × 20.79 J mol⁻¹ K⁻¹ × 50.0 K\n(b) C_p = 20.79 + 8.314 = 29.104 J mol⁻¹ K⁻¹; Q_p = 2.0 mol × 29.104 J mol⁻¹ K⁻¹ × 50.0 K\n(c) W_p = 2.0 mol × 8.314 J mol⁻¹ K⁻¹ × 50.0 K",
            "calculation": "(a) Q_v = 100 × 20.79 = 2079 J\n(b) Q_p = 100 × 29.104 = 2910.4 J\n(c) W_p = 100 × 8.314 = 831.4 J\nCheck: Q_p - Q_v = 2910.4 - 2079 = 831.4 J = W_p (First Law confirmed).",
            "rough_work": "[ROUGH_WORK]\n2 × 50 = 100\n100 × 20.79 = 2079 J\n100 × 29.104 = 2910.4 J\nDifference = 831.4 J",
            "finalAnswer": "(a) Q_v = 2079 J; (b) Q_p = 2910.4 J; (c) External work W_p = 831.4 J",
            "unit": "J",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Section 11.6, Page 231",
            "image_search_query": "molar heat capacity constant pressure volume"
        }
    ]

    modules[1]["concept_questions"] = [
        {
            "question": "Why is the molar specific heat of a gas at constant pressure (C_p) always strictly greater than that at constant volume (C_v)?",
            "options": [
                "(Recommended) At constant pressure, heat is spent in both increasing internal energy and doing external expansion work",
                "Molecules move at higher speeds under constant volume conditions",
                "Internal energy remains constant during isobaric heating",
                "At constant pressure, gas molecules lose degrees of freedom"
            ],
            "correctAnswer": "(Recommended) At constant pressure, heat is spent in both increasing internal energy and doing external expansion work",
            "correct_answer": "(Recommended) At constant pressure, heat is spent in both increasing internal energy and doing external expansion work",
            "explanation": "At constant volume, all heat supplied goes solely into increasing the internal energy (ΔW = 0). At constant pressure, the gas expands against external pressure, requiring additional energy to perform mechanical work (ΔW = P·ΔV). Hence C_p = C_v + R > C_v.",
            "hint": "Analyze the two components where energy is expended when a gas is allowed to expand.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 11.6, Page 231",
            "image_search_query": "cp greater than cv thermodynamics"
        },
        {
            "question": "What is the molar specific heat capacity of an ideal gas during an isothermal process and during an adiabatic process, respectively?",
            "options": [
                "(Recommended) C_iso = ∞ and C_adia = 0",
                "C_iso = 0 and C_adia = ∞",
                "C_iso = R and C_adia = γ R",
                "C_iso = C_v and C_adia = C_p"
            ],
            "correctAnswer": "(Recommended) C_iso = ∞ and C_adia = 0",
            "correct_answer": "(Recommended) C_iso = ∞ and C_adia = 0",
            "explanation": "Molar heat capacity is defined as C = ΔQ / (μ · ΔT). In an isothermal process, heat is exchanged while ΔT = 0, so C = ΔQ / 0 = ∞. In an adiabatic process, ΔQ = 0 while ΔT ≠ 0, so C = 0 / (μ · ΔT) = 0.",
            "hint": "Use C = ΔQ / (μ · ΔT) and consider ΔT = 0 vs ΔQ = 0.",
            "blooms_level": "Analyze",
            "textbook_reference": "Section 11.6, Page 231",
            "image_search_query": "molar heat capacity isothermal adiabatic"
        },
        {
            "question": "Which of the following thermodynamic variables is intensive (independent of the total size or mass of the system)?",
            "options": [
                "(Recommended) Pressure (P) and Temperature (T)",
                "Volume (V) and Internal Energy (U)",
                "Heat Capacity (S) and Enthalpy (H)",
                "Total mass (M) and Mole number (μ)"
            ],
            "correctAnswer": "(Recommended) Pressure (P) and Temperature (T)",
            "correct_answer": "(Recommended) Pressure (P) and Temperature (T)",
            "explanation": "Intensive variables do not scale with system size (dividing the system in half leaves P, T, and density unchanged). Volume, internal energy, mass, and heat capacity are extensive variables.",
            "hint": "Think of what happens when a gas container is partitioned into two identical halves.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 11.7, Page 232",
            "image_search_query": "intensive extensive thermodynamic variables"
        },
        {
            "question": "For a rigid triatomic non-linear gas molecule (such as H₂O vapour) having 6 degrees of freedom (3 translational + 3 rotational), what are the predicted values of C_v, C_p, and γ?",
            "options": [
                "(Recommended) C_v = 3 R, C_p = 4 R, γ = 1.33",
                "C_v = (5/2) R, C_p = (7/2) R, γ = 1.40",
                "C_v = (3/2) R, C_p = (5/2) R, γ = 1.67",
                "C_v = 4 R, C_p = 5 R, γ = 1.25"
            ],
            "correctAnswer": "(Recommended) C_v = 3 R, C_p = 4 R, γ = 1.33",
            "correct_answer": "(Recommended) C_v = 3 R, C_p = 4 R, γ = 1.33",
            "explanation": "With f = 6 degrees of freedom: C_v = (6/2) R = 3 R. Using Mayer's relation: C_p = C_v + R = 4 R. Ratio γ = C_p / C_v = 4/3 ≈ 1.33.",
            "hint": "Apply equipartition theorem C_v = (f/2) R and C_p = C_v + R for f = 6.",
            "blooms_level": "Apply",
            "textbook_reference": "Section 11.6, Page 231",
            "image_search_query": "degrees of freedom triatomic gas specific heat"
        }
    ]

    # -------------------------------------------------------------
    # Module 67: Thermodynamic Processes & Indicator Diagrams
    # -------------------------------------------------------------
    modules[2]["worked_examples"] = [
        {
            "problem": "One mole of an ideal gas at temperature T = 300 K undergoes a quasi-static isothermal expansion from an initial volume of V₁ = 1.0 × 10⁻² m³ to a final volume of V₂ = 2.0 × 10⁻² m³. Calculate (a) the work done by the gas, (b) the heat absorbed from the thermal reservoir, and (c) the change in internal energy of the gas. (Take R = 8.314 J mol⁻¹ K⁻¹, ln 2 = 0.69315)",
            "given": "Number of moles μ = 1.0 mol, Constant temperature T = 300 K, Initial volume V₁ = 1.0 × 10⁻² m³, Final volume V₂ = 2.0 × 10⁻² m³, Expansion ratio V₂/V₁ = 2.0, R = 8.314 J mol⁻¹ K⁻¹",
            "to_calculate": "(a) Work done W_iso, (b) Heat absorbed Q_iso, (c) Change in internal energy ΔU",
            "formula": "(a) W_iso = μ · R · T · ln(V₂ / V₁)\n(b) Since T is constant, for an ideal gas internal energy U depends only on T => ΔU = 0\n(c) First Law: Q_iso = ΔU + W_iso = 0 + W_iso => Q_iso = W_iso",
            "substitution": "(a) W_iso = 1.0 mol × 8.314 J mol⁻¹ K⁻¹ × 300 K × ln(2)\n= 8.314 × 300 × 0.69315 J",
            "calculation": "8.314 × 300 = 2494.2 J\nW_iso = 2494.2 × 0.69315 = 1728.85 J ≈ 1729 J\n(b) Q_iso = W_iso = +1729 J\n(c) ΔU = 0 J",
            "rough_work": "[ROUGH_WORK]\n2494.2 × 0.69315 = 1728.854 J\nRounding off to 4 sig figs: 1729 J.",
            "finalAnswer": "(a) Work done W_iso = 1729 J; (b) Heat absorbed Q_iso = +1729 J; (c) Change in internal energy ΔU = 0 J",
            "unit": "J",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Section 11.8.2, Page 234",
            "image_search_query": "isothermal expansion pv indicator diagram"
        },
        {
            "problem": "An ideal diatomic gas (γ = 1.40) initially at pressure P₁ = 1.0 × 10⁵ Pa and temperature T₁ = 300 K is compressed adiabatically to 1/8th of its initial volume (V₂ = V₁ / 8). Calculate (a) the final pressure P₂, (b) the final temperature T₂, and (c) the work done per mole during this adiabatic compression. (Take R = 8.314 J mol⁻¹ K⁻¹, 2^4.2 = 18.38)",
            "given": "Adiabatic index γ = 1.40, Initial pressure P₁ = 1.0 × 10⁵ Pa, Initial temperature T₁ = 300 K, Volume compression ratio V₁/V₂ = 8.0, Number of moles μ = 1.0 mol, R = 8.314 J mol⁻¹ K⁻¹",
            "to_calculate": "(a) Final pressure P₂, (b) Final temperature T₂, (c) Work done per mole W_adia",
            "formula": "(a) Adiabatic law: P₁ · V₁^γ = P₂ · V₂^γ => P₂ = P₁ · (V₁ / V₂)^γ\n(b) Temperature relation: T₁ · V₁^(γ-1) = T₂ · V₂^(γ-1) => T₂ = T₁ · (V₁ / V₂)^(γ-1)\n(c) Adiabatic work: W_adia = (μ · R · (T₁ - T₂)) / (γ - 1)",
            "substitution": "(a) P₂ = 1.0 × 10⁵ Pa × (8)^1.4\nNote: 8^1.4 = (2³)^1.4 = 2^4.2 = 18.38 => P₂ = 1.0 × 10⁵ × 18.38 Pa\n(b) T₂ = 300 K × (8)^(1.4 - 1.0) = 300 × 8^0.4 = 300 × 2^1.2 = 300 × 2.2974 K\n(c) W_adia = (1.0 × 8.314 × (300 - 689.2)) / (1.4 - 1.0)",
            "calculation": "(a) P₂ = 18.38 × 10⁵ Pa = 1.84 × 10⁶ Pa\n(b) 8^0.4 = 2.2974; T₂ = 300 × 2.2974 = 689.2 K\n(c) T₁ - T₂ = 300 - 689.2 = -389.2 K\nW_adia = (8.314 × (-389.2)) / 0.4 = -3235.8 / 0.4 = -8089.5 J ≈ -8.09 kJ",
            "rough_work": "[ROUGH_WORK]\n2^4.2 = 18.379\n8^0.4 = 2.2974\n300 × 2.2974 = 689.22 K\n8.314 × (-389.22) / 0.4 = -8089.6 J",
            "finalAnswer": "(a) Final pressure P₂ = 1.84 × 10⁶ Pa (18.4 atm); (b) Final temperature T₂ = 689.2 K; (c) Work done on the gas W = -8.09 kJ (work done by gas is -8.09 kJ)",
            "unit": "Pa, K, kJ",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Section 11.8.3, Page 235",
            "image_search_query": "adiabatic compression pv curve indicator"
        }
    ]

    modules[2]["concept_questions"] = [
        {
            "question": "On an indicator diagram (P-V plot), how does the magnitude of the slope of an adiabatic curve compare to that of an isothermal curve passing through the exact same point (P, V)?",
            "options": [
                "(Recommended) The adiabatic slope is steeper by a factor of γ (Slope_adia = γ · Slope_iso)",
                "The isothermal slope is steeper by a factor of γ",
                "Both slopes are strictly identical because temperature is continuous",
                "The adiabatic curve has zero slope because heat cannot flow"
            ],
            "correctAnswer": "(Recommended) The adiabatic slope is steeper by a factor of γ (Slope_adia = γ · Slope_iso)",
            "correct_answer": "(Recommended) The adiabatic slope is steeper by a factor of γ (Slope_adia = γ · Slope_iso)",
            "explanation": "Differentiating P·V = constant gives (dP/dV)_iso = -P/V. Differentiating P·V^γ = constant gives (dP/dV)_adia = -γ·(P/V). Since γ = C_p / C_v > 1, the adiabatic curve is always γ times steeper.",
            "hint": "Differentiate P·V = const and P·V^γ = const with respect to V.",
            "blooms_level": "Analyze",
            "textbook_reference": "Section 11.8.3, Page 235",
            "image_search_query": "slope adiabatic curve vs isothermal curve"
        },
        {
            "question": "A gas expands from volume V₁ to V₂ along three different paths: (1) Isobaric, (2) Isothermal, and (3) Adiabatic. In which process is the work done by the gas the greatest?",
            "options": [
                "(Recommended) Isobaric process",
                "Isothermal process",
                "Adiabatic process",
                "Work done is identical in all three processes"
            ],
            "correctAnswer": "(Recommended) Isobaric process",
            "correct_answer": "(Recommended) Isobaric process",
            "explanation": "Work done is the area under the P-V curve. In isobaric expansion, pressure remains at its maximum value P₁. In isothermal and adiabatic expansions, pressure decreases during expansion, with adiabatic falling fastest. Thus Area_isobaric > Area_isothermal > Area_adiabatic.",
            "hint": "Compare the area under the P-V curves between V₁ and V₂.",
            "blooms_level": "Apply",
            "textbook_reference": "Section 11.8, Page 234",
            "image_search_query": "work done comparison isobaric isothermal adiabatic"
        },
        {
            "question": "What is the primary physical requirement for a real thermodynamic process to be classified as quasi-static?",
            "options": [
                "(Recommended) The process must occur infinitesimally slowly so the system remains in mechanical and thermal equilibrium at every intermediate stage",
                "The container walls must be perfectly rigid with zero friction",
                "The process must be completed instantaneously so heat cannot escape",
                "The pressure of the gas must remain strictly constant throughout"
            ],
            "correctAnswer": "(Recommended) The process must occur infinitesimally slowly so the system remains in mechanical and thermal equilibrium at every intermediate stage",
            "correct_answer": "(Recommended) The process must occur infinitesimally slowly so the system remains in mechanical and thermal equilibrium at every intermediate stage",
            "explanation": "A quasi-static process is an idealized succession of equilibrium states, achieved when the process proceeds infinitesimally slowly compared to the relaxation time of the system.",
            "hint": "Consider the condition needed for state variables P and T to be well-defined at all intermediate moments.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 11.8.1, Page 233",
            "image_search_query": "quasi-static process equilibrium thermodynamics"
        },
        {
            "question": "In an isochoric heating process, 400 J of heat is delivered to a rigid closed vessel containing an ideal gas. What are the values of the work done ΔW and the change in internal energy ΔU?",
            "options": [
                "(Recommended) ΔW = 0 J and ΔU = +400 J",
                "ΔW = +400 J and ΔU = 0 J",
                "ΔW = -400 J and ΔU = +400 J",
                "ΔW = +200 J and ΔU = +200 J"
            ],
            "correctAnswer": "(Recommended) ΔW = 0 J and ΔU = +400 J",
            "correct_answer": "(Recommended) ΔW = 0 J and ΔU = +400 J",
            "explanation": "In an isochoric process, volume is constant (ΔV = 0), so work done ΔW = P·ΔV = 0. By the First Law: ΔQ = ΔU + ΔW => 400 J = ΔU + 0 => ΔU = +400 J.",
            "hint": "Check the value of ΔV for a rigid vessel.",
            "blooms_level": "Apply",
            "textbook_reference": "Section 11.8.4, Page 235",
            "image_search_query": "isochoric heating constant volume first law"
        }
    ]

    # -------------------------------------------------------------
    # Module 68: Second Law, Heat Engines & Refrigerators
    # -------------------------------------------------------------
    modules[3]["worked_examples"] = [
        {
            "problem": "A heat engine operates between a heat source at T₁ = 600 K and a heat sink at T₂ = 300 K. In each cycle, it absorbs 2500 J of thermal energy from the source and delivers 1000 J of useful mechanical work. Calculate (a) the heat rejected to the sink per cycle, (b) the actual thermal efficiency η of the engine, and (c) the maximum theoretical efficiency η_carnot operating between these two reservoir temperatures.",
            "given": "Source temperature T₁ = 600 K, Sink temperature T₂ = 300 K, Heat absorbed Q₁ = 2500 J, Work output W = 1000 J",
            "to_calculate": "(a) Heat rejected Q₂, (b) Actual thermal efficiency η, (c) Maximum Carnot efficiency η_carnot",
            "formula": "(a) Energy conservation: W = Q₁ - Q₂ => Q₂ = Q₁ - W\n(b) Actual efficiency: η = W / Q₁ = (Q₁ - Q₂) / Q₁\n(c) Carnot efficiency: η_carnot = 1 - (T₂ / T₁)",
            "substitution": "(a) Q₂ = 2500 J - 1000 J\n(b) η = 1000 J / 2500 J\n(c) η_carnot = 1 - (300 K / 600 K)",
            "calculation": "(a) Q₂ = 1500 J\n(b) η = 1000 / 2500 = 0.40 = 40%\n(c) η_carnot = 1 - 0.50 = 0.50 = 50%\nComparison: Actual efficiency (40%) is less than ideal Carnot limit (50%), consistent with Second Law of Thermodynamics.",
            "rough_work": "[ROUGH_WORK]\n2500 - 1000 = 1500 J\n1000 / 2500 = 0.40 (40%)\n1 - 300/600 = 0.50 (50%)",
            "finalAnswer": "(a) Heat rejected Q₂ = 1500 J; (b) Actual efficiency η = 40%; (c) Maximum Carnot efficiency η_carnot = 50%",
            "unit": "J, %",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Section 11.9, Page 236",
            "image_search_query": "heat engine efficiency second law diagram"
        },
        {
            "problem": "A domestic refrigerator maintains its food compartment at T₂ = -3 °C while the kitchen room temperature is T₁ = 27 °C. Assuming it operates on a reversible Carnot refrigerator cycle: (a) calculate its coefficient of performance (COP, β), and (b) determine the electrical work required to extract 540 J of heat from the cold compartment.",
            "given": "Cold reservoir temperature T₂ = -3 °C = (-3 + 273.15) K = 270.15 K ≈ 270 K, Hot reservoir temperature T₁ = 27 °C = (27 + 273.15) K = 300 K, Heat extracted Q₂ = 540 J",
            "to_calculate": "(a) Coefficient of performance β, (b) Work input W required",
            "formula": "(a) Reversible COP: β = Q₂ / W = T₂ / (T₁ - T₂)\n(b) Required work: W = Q₂ / β = Q₂ · (T₁ - T₂) / T₂",
            "substitution": "(a) β = 270 K / (300 K - 270 K) = 270 / 30\n(b) W = 540 J / 9.0",
            "calculation": "(a) β = 270 / 30 = 9.0\n(b) W = 540 / 9.0 = 60.0 J\nHeat rejected to room Q₁ = Q₂ + W = 540 + 60 = 600 J.",
            "rough_work": "[ROUGH_WORK]\n270 / (300 - 270) = 270 / 30 = 9\nW = 540 / 9 = 60 J\nQ₁ = 540 + 60 = 600 J",
            "finalAnswer": "(a) Coefficient of performance β = 9.0; (b) Work input required W = 60.0 J",
            "unit": "Dimensionless, J",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Section 11.9, Page 236",
            "image_search_query": "refrigerator coefficient of performance diagram"
        }
    ]

    modules[3]["concept_questions"] = [
        {
            "question": "Which of the following statements represents the Kelvin-Planck formulation of the Second Law of Thermodynamics?",
            "options": [
                "(Recommended) No process is possible whose sole result is the absorption of heat from a reservoir and its complete conversion into work",
                "Heat can flow spontaneously from a colder body to a hotter body without any external work",
                "The total internal energy of any isolated system is strictly conserved",
                "The efficiency of any real engine always equals unity (100%)"
            ],
            "correctAnswer": "(Recommended) No process is possible whose sole result is the absorption of heat from a reservoir and its complete conversion into work",
            "correct_answer": "(Recommended) No process is possible whose sole result is the absorption of heat from a reservoir and its complete conversion into work",
            "explanation": "The Kelvin-Planck statement asserts that a 100% efficient heat engine is impossible; some heat must always be rejected to a colder reservoir (sink).",
            "hint": "Identify the statement prohibiting a heat engine from operating with zero heat rejection.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 11.9, Page 236",
            "image_search_query": "kelvin planck statement second law thermodynamics"
        },
        {
            "question": "If a refrigerator door is left wide open in a completely sealed, thermally insulated room, what will happen to the room temperature over time?",
            "options": [
                "(Recommended) The room temperature will gradually increase",
                "The room temperature will gradually decrease",
                "The room temperature will remain exactly constant",
                "The room temperature will first drop to freezing and then stabilize"
            ],
            "correctAnswer": "(Recommended) The room temperature will gradually increase",
            "correct_answer": "(Recommended) The room temperature will gradually increase",
            "explanation": "A refrigerator exhausts heat Q₁ = Q₂ + W into the room. Since the room is sealed, the heat expelled at the back condenser coils exceeds the heat extracted from the interior by the electrical work input W done by the compressor. Hence net thermal energy of the room increases.",
            "hint": "Consider the First Law for the sealed room: Q_net = 0, work W is added by the electrical outlet.",
            "blooms_level": "Apply",
            "textbook_reference": "Section 11.9, Page 236",
            "image_search_query": "refrigerator open in closed room heating"
        },
        {
            "question": "What is the primary physical cause of irreversibility in almost all macroscopic natural thermodynamic processes?",
            "options": [
                "(Recommended) Dissipative effects (friction, viscosity, electrical resistance) and unconstrained spontaneous expansions",
                "The conservation of total mechanical energy in frictionless systems",
                "The finite mass of microscopic gas atoms",
                "Infinitesimally slow quasi-static heat exchanges"
            ],
            "correctAnswer": "(Recommended) Dissipative effects (friction, viscosity, electrical resistance) and unconstrained spontaneous expansions",
            "correct_answer": "(Recommended) Dissipative effects (friction, viscosity, electrical resistance) and unconstrained spontaneous expansions",
            "explanation": "Irreversibility arises from dissipative forces (converting ordered mechanical energy into disordered thermal motion) and spontaneous non-equilibrium processes (free expansion, rapid chemical reactions, finite temperature heat transfer).",
            "hint": "Think about energy dissipation and spontaneous mixing.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 11.10, Page 236",
            "image_search_query": "irreversible processes dissipation thermodynamics"
        },
        {
            "question": "How is the Clausius statement of the Second Law of Thermodynamics related to the Kelvin-Planck statement?",
            "options": [
                "(Recommended) They are completely logically equivalent; a violation of one implies a direct violation of the other",
                "Clausius applies only to solids, whereas Kelvin-Planck applies only to ideal gases",
                "The Clausius statement contradicts the Kelvin-Planck statement for cyclic processes",
                "Kelvin-Planck deals with entropy, whereas Clausius deals strictly with enthalpy"
            ],
            "correctAnswer": "(Recommended) They are completely logically equivalent; a violation of one implies a direct violation of the other",
            "correct_answer": "(Recommended) They are completely logically equivalent; a violation of one implies a direct violation of the other",
            "explanation": "It is proved by coupling a hypothetical engine that violates Kelvin-Planck to a refrigerator, which results in a net machine violating Clausius, and vice versa. Both express the same fundamental truth.",
            "hint": "Recall the textbook proof coupling a heat engine and refrigerator.",
            "blooms_level": "Analyze",
            "textbook_reference": "Section 11.9, Page 236",
            "image_search_query": "equivalence kelvin planck clausius statement"
        }
    ]

    # -------------------------------------------------------------
    # Module 69: Carnot Engine Cycle & Carnot's Theorem
    # -------------------------------------------------------------
    modules[4]["worked_examples"] = [
        {
            "problem": "A Carnot engine works between two heat reservoirs at temperatures T₁ = 750 K and T₂ = 350 K. (a) Calculate the theoretical efficiency of this Carnot engine. (b) If the engine absorbs 1500 J of heat from the source in each cycle, determine the mechanical work performed per cycle and the heat rejected to the sink. (c) If the sink temperature is lowered to 300 K while keeping the source temperature unchanged, find the new efficiency.",
            "given": "Initial source temperature T₁ = 750 K, Initial sink temperature T₂ = 350 K, Heat absorbed Q₁ = 1500 J, New sink temperature T₂' = 300 K",
            "to_calculate": "(a) Initial Carnot efficiency η₁, (b) Work W and heat rejected Q₂, (c) New efficiency η₂",
            "formula": "(a) η = 1 - (T₂ / T₁)\n(b) W = η · Q₁; Q₂ = Q₁ - W\n(c) η' = 1 - (T₂' / T₁)",
            "substitution": "(a) η₁ = 1 - (350 / 750) = 1 - 7/15\n(b) W = (8/15) × 1500 J; Q₂ = 1500 J - W\n(c) η₂ = 1 - (300 / 750) = 1 - 2/5",
            "calculation": "(a) η₁ = 1 - 0.4667 = 0.5333 = 53.33%\n(b) W = 8 × 100 = 800 J; Q₂ = 1500 - 800 = 700 J\n(c) η₂ = 1 - 0.40 = 0.60 = 60.0%",
            "rough_work": "[ROUGH_WORK]\n350 / 750 = 7 / 15 = 0.4667\n1 - 7/15 = 8/15 = 0.5333\nW = (8/15) × 1500 = 800 J\nQ₂ = 700 J\n300 / 750 = 2/5 = 0.40 => η = 60%",
            "finalAnswer": "(a) Initial efficiency η₁ = 53.33%; (b) Work output W = 800 J, Heat rejected Q₂ = 700 J; (c) New efficiency with sink at 300 K η₂ = 60.0%",
            "unit": "%, J",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Section 11.11, Pages 237-238",
            "image_search_query": "carnot engine cycle efficiency pv indicator"
        },
        {
            "problem": "Two Carnot engines A and B are connected in series. Engine A receives heat at temperature T₁ = 900 K and rejects heat at an intermediate temperature T₂ to engine B. Engine B takes in this rejected heat and exhausts to a sink at T₃ = 400 K. Calculate the intermediate temperature T₂ if (a) the work outputs of both engines are equal (W_A = W_B), and (b) the efficiencies of both engines are equal (η_A = η_B).",
            "given": "High reservoir temperature T₁ = 900 K, Low reservoir temperature T₃ = 400 K, Intermediate reservoir temperature T₂",
            "to_calculate": "Intermediate temperature T₂ under conditions: (a) W_A = W_B, (b) η_A = η_B",
            "formula": "Efficiency η = W / Q => W = η · Q.\n(a) For equal work: W_A = Q₁ · (1 - T₂/T₁) and W_B = Q₂ · (1 - T₃/T₂). Since Q₂ = Q₁ · (T₂/T₁), W_B = Q₁ · (T₂/T₁) · (1 - T₃/T₂) = Q₁ · (T₂ - T₃)/T₁. Setting W_A = W_B gives: (T₁ - T₂) / T₁ = (T₂ - T₃) / T₁ => T₁ - T₂ = T₂ - T₃ => T₂ = (T₁ + T₃) / 2 (Arithmetic Mean).\n(b) For equal efficiencies: 1 - T₂/T₁ = 1 - T₃/T₂ => T₂ / T₁ = T₃ / T₂ => T₂² = T₁ · T₃ => T₂ = √(T₁ · T₃) (Geometric Mean).",
            "substitution": "(a) T₂ = (900 K + 400 K) / 2\n(b) T₂ = √(900 K × 400 K) = √(360000) K",
            "calculation": "(a) T₂ = 1300 / 2 = 650 K\n(b) T₂ = √360000 = 600 K",
            "rough_work": "[ROUGH_WORK]\n(a) 900 + 400 = 1300; 1300 / 2 = 650 K\n(b) 900 × 400 = 360000; sqrt(360000) = 600 K",
            "finalAnswer": "(a) For equal work outputs: T₂ = 650 K; (b) For equal efficiencies: T₂ = 600 K",
            "unit": "K",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Section 11.11, Page 239",
            "image_search_query": "carnot engines in series intermediate temperature"
        }
    ]

    modules[4]["concept_questions"] = [
        {
            "question": "What are the four successive thermodynamic processes that constitute an ideal Carnot cycle in sequence on an indicator (P-V) diagram?",
            "options": [
                "(Recommended) 1. Isothermal expansion, 2. Adiabatic expansion, 3. Isothermal compression, 4. Adiabatic compression",
                "1. Isobaric expansion, 2. Isochoric cooling, 3. Isobaric compression, 4. Isochoric heating",
                "1. Adiabatic expansion, 2. Isothermal expansion, 3. Adiabatic compression, 4. Isothermal compression",
                "1. Isothermal expansion, 2. Isobaric expansion, 3. Isothermal compression, 4. Isobaric compression"
            ],
            "correctAnswer": "(Recommended) 1. Isothermal expansion, 2. Adiabatic expansion, 3. Isothermal compression, 4. Adiabatic compression",
            "correct_answer": "(Recommended) 1. Isothermal expansion, 2. Adiabatic expansion, 3. Isothermal compression, 4. Adiabatic compression",
            "explanation": "The Carnot cycle consists of two reversible isotherms (at T₁ and T₂) linked by two reversible adiabats, returning the ideal gas to its initial state.",
            "hint": "Recall the sequence alternating between isothermal and adiabatic stages.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 11.11, Page 237",
            "image_search_query": "carnot cycle four stages pv indicator"
        },
        {
            "question": "According to Carnot's Theorem, what factors determine the maximum possible thermal efficiency of any reversible heat engine operating between two given temperatures?",
            "options": [
                "(Recommended) Only the absolute temperatures of the hot source (T₁) and cold sink (T₂), completely independent of the working substance",
                "The molar mass and specific heat ratio γ of the working gas",
                "The total volume of the engine cylinder and pressure limits",
                "The rate of heat transfer through the cylinder walls"
            ],
            "correctAnswer": "(Recommended) Only the absolute temperatures of the hot source (T₁) and cold sink (T₂), completely independent of the working substance",
            "correct_answer": "(Recommended) Only the absolute temperatures of the hot source (T₁) and cold sink (T₂), completely independent of the working substance",
            "explanation": "Carnot's theorem proves that all reversible engines operating between the same two temperatures have the identical maximum efficiency η = 1 - T₂/T₁, regardless of whether the working substance is helium, air, steam, or liquid.",
            "hint": "Carnot efficiency formula η = 1 - T₂/T₁ contains only two variables.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 11.11, Page 239",
            "image_search_query": "carnot theorem working substance independence"
        },
        {
            "question": "To increase the efficiency of a Carnot engine by a given percentage, is it more effective to raise the source temperature T₁ by ΔT or to lower the sink temperature T₂ by the same ΔT?",
            "options": [
                "(Recommended) Lowering the sink temperature T₂ by ΔT is more effective because T₂ < T₁",
                "Raising the source temperature T₁ by ΔT is always more effective",
                "Both choices yield the mathematically identical increase in efficiency",
                "Neither changes the efficiency because efficiency depends only on ratio of pressures"
            ],
            "correctAnswer": "(Recommended) Lowering the sink temperature T₂ by ΔT is more effective because T₂ < T₁",
            "correct_answer": "(Recommended) Lowering the sink temperature T₂ by ΔT is more effective because T₂ < T₁",
            "explanation": "Efficiency η = 1 - T₂/T₁. The sensitivity |∂η/∂T₂| = 1/T₁, while ∂η/∂T₁ = T₂/T₁². Since T₂ < T₁, we have 1/T₁ > T₂/T₁². Thus decreasing T₂ by ΔT increases efficiency more than increasing T₁ by the same ΔT.",
            "hint": "Compare the derivatives |∂η/∂T₂| = 1/T₁ and ∂η/∂T₁ = T₂/T₁².",
            "blooms_level": "Analyze",
            "textbook_reference": "Section 11.11, Page 238",
            "image_search_query": "increase carnot efficiency source vs sink temperature"
        },
        {
            "question": "Can the thermal efficiency of any heat engine operating between finite source and sink temperatures ever equal 100% (η = 1)?",
            "options": [
                "(Recommended) No, because achieving η = 1 would require the cold sink to be at absolute zero (T₂ = 0 K), which is unattainable by the Third Law of Thermodynamics",
                "Yes, by using an ideal monoatomic gas with zero molecular friction",
                "Yes, provided all four processes in the cycle are conducted infinitely slowly",
                "No, only because real engines experience mechanical friction in their bearings"
            ],
            "correctAnswer": "(Recommended) No, because achieving η = 1 would require the cold sink to be at absolute zero (T₂ = 0 K), which is unattainable by the Third Law of Thermodynamics",
            "correct_answer": "(Recommended) No, because achieving η = 1 would require the cold sink to be at absolute zero (T₂ = 0 K), which is unattainable by the Third Law of Thermodynamics",
            "explanation": "For η = 1 - T₂/T₁ to equal 1, T₂ must be 0 K or T₁ must be ∞. Absolute zero (0 K) cannot be reached in a finite number of thermodynamic steps, making 100% efficiency fundamentally impossible in nature.",
            "hint": "Check the condition for η = 1 - T₂/T₁ = 1.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 11.11, Page 238",
            "image_search_query": "absolute zero third law carnot efficiency limit"
        }
    ]

    # -------------------------------------------------------------
    # Module 70: Comprehensive NCERT Exercises 11.1 to 11.10 Detailed Solver
    # -------------------------------------------------------------
    modules[5]["worked_examples"] = [
        {
            "problem": "NCERT Exercise 11.1: A geyser heats water flowing at the rate of 3.0 litres per minute from 27 °C to 77 °C. If the geyser operates on a gas burner, what is the rate of consumption of the fuel if its heat of combustion is 4.0 × 10⁴ J/g ?",
            "given": "Volume flow rate of water V/t = 3.0 L min⁻¹ = 3.0 × 10⁻³ m³ min⁻¹ = (3.0 × 10⁻³ / 60) m³ s⁻¹ = 5.0 × 10⁻⁵ m³ s⁻¹, Density of water ρ = 1000 kg m⁻³, Mass flow rate m/t = ρ · (V/t) = 1000 × 5.0 × 10⁻⁵ = 5.0 × 10⁻² kg s⁻¹ = 3.0 kg min⁻¹, Initial temperature T₁ = 27 °C, Final temperature T₂ = 77 °C => ΔT = 77 - 27 = 50 °C = 50 K, Specific heat capacity of water c = 4186 J kg⁻¹ K⁻¹ ≈ 4.2 × 10³ J kg⁻¹ K⁻¹, Heat of combustion of fuel H = 4.0 × 10⁴ J g⁻¹ = 4.0 × 10⁷ J kg⁻¹",
            "to_calculate": "Rate of consumption of fuel (dm_fuel / dt)",
            "formula": "Rate of heat absorbed by water: dQ/dt = (dm_water / dt) · c · ΔT\nHeat supplied by fuel: dQ/dt = (dm_fuel / dt) · H\nEquating both: (dm_fuel / dt) = [ (dm_water / dt) · c · ΔT ] / H",
            "substitution": "(dm_fuel / dt) = [ (3.0 kg min⁻¹) × (4186 J kg⁻¹ K⁻¹) × (50 K) ] / (4.0 × 10⁷ J kg⁻¹)",
            "calculation": "dQ/min = 3.0 × 4186 × 50 = 627900 J min⁻¹ = 6.279 × 10⁵ J min⁻¹\nRate of fuel consumption in kg/min:\n(dm_fuel / dt) = 6.279 × 10⁵ / (4.0 × 10⁷) = 0.0156975 kg min⁻¹\nConverting to grams per minute (g/min):\nRate = 0.0157 kg min⁻¹ × 1000 g/kg = 15.7 g min⁻¹",
            "rough_work": "[ROUGH_WORK]\n3 × 4186 × 50 = 627,900 J/min\nHeat of combustion = 40,000 J/g\nRate = 627,900 / 40,000 = 15.6975 g/min ≈ 15.7 g/min.",
            "finalAnswer": "Rate of fuel consumption = 15.7 g min⁻¹ (or 0.262 g s⁻¹)",
            "unit": "g min⁻¹",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Exercise 11.1, Page 242",
            "image_search_query": "geyser water heating gas consumption calculation"
        },
        {
            "problem": "NCERT Exercise 11.2: What amount of heat must be supplied to 2.0 × 10⁻² kg of nitrogen (at room temperature) to raise its temperature by 45 °C at constant pressure? (Molecular mass of N₂ = 28; R = 8.3 J mol⁻¹ K⁻¹.)",
            "given": "Mass of nitrogen m = 2.0 × 10⁻² kg = 20.0 g, Molar mass of N₂ M = 28 g mol⁻¹ = 28 × 10⁻³ kg mol⁻¹, Temperature rise ΔT = 45 °C = 45 K, Gas constant R = 8.3 J mol⁻¹ K⁻¹",
            "to_calculate": "Amount of heat supplied at constant pressure Q_p",
            "formula": "Number of moles: μ = m / M\nNitrogen is a diatomic gas with 5 degrees of freedom at room temperature.\nMolar heat capacity at constant pressure: C_p = (7/2) · R\nHeat supplied: Q_p = μ · C_p · ΔT = (m / M) · (7/2 · R) · ΔT",
            "substitution": "μ = 20.0 / 28 = 0.7143 mol\nC_p = (7/2) × 8.3 J mol⁻¹ K⁻¹ = 29.05 J mol⁻¹ K⁻¹\nQ_p = (0.7143 mol) × (29.05 J mol⁻¹ K⁻¹) × (45 K)",
            "calculation": "Q_p = (20.0 / 28) × 29.05 × 45\n= (5 / 7) × 29.05 × 45 = 0.71428 × 1307.25 = 933.75 J ≈ 934 J",
            "rough_work": "[ROUGH_WORK]\n20 / 28 = 5/7\nC_p = 3.5 × 8.3 = 29.05\nQ_p = (5/7) × 29.05 × 45 = 933.75 J",
            "finalAnswer": "Heat required to raise temperature at constant pressure Q_p = 934 J",
            "unit": "J",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Exercise 11.2, Page 242",
            "image_search_query": "molar heat capacity constant pressure nitrogen"
        },
        {
            "problem": "NCERT Exercise 11.3: Explain why:\n(a) Two bodies at different temperatures T₁ and T₂ if brought in thermal contact do not necessarily settle to the mean temperature (T₁ + T₂)/2.\n(b) The coolant in a chemical or a nuclear plant (i.e., the liquid used to prevent the different parts of a plant from getting too hot) should have high specific heat.\n(c) Air pressure in a car tyre increases during driving.\n(d) The climate of a harbour town is more temperate than that of a town in a desert at the same latitude.",
            "given": "Theoretical concepts based on heat exchange, heat capacity, gas laws, and thermal moderation",
            "to_calculate": "Systematic scientific explanations for parts (a), (b), (c), and (d)",
            "formula": "(a) Heat lost = Heat gained => m₁ · c₁ · (T₁ - T_f) = m₂ · c₂ · (T_f - T₂)\n(b) Q = m · c · ΔT => ΔT = Q / (m · c)\n(c) Gay-Lussac's Law: P / T = constant for constant volume\n(d) Specific heat capacity of water c_water = 4186 J kg⁻¹ K⁻¹ vs sand/rock c_sand ≈ 800 J kg⁻¹ K⁻¹",
            "substitution": "Qualitative step-by-step physical reasoning with standard governing laws",
            "calculation": "(a) Final equilibrium temperature T_f = (m₁ c₁ T₁ + m₂ c₂ T₂) / (m₁ c₁ + m₂ c₂). T_f equals (T₁ + T₂)/2 ONLY if the two bodies have identical thermal capacities (m₁ c₁ = m₂ c₂). If their masses or specific heats differ, T_f will be closer to the temperature of the body with larger thermal capacity.\n(b) A coolant with high specific heat absorbs a tremendous amount of heat Q with only a minimal rise in its temperature (ΔT = Q/(mc)), preventing the reactor core from overheating without boiling away.\n(c) During driving, continuous frictional rolling resistance between the tyre rubber and the asphalt road generates heat. This increases the temperature T of the air inside the tyre. Since the tyre volume V is approximately constant, by Gay-Lussac's Law (P ∝ T), the internal air pressure increases.\n(d) Water has an exceptionally high specific heat capacity (4186 J kg⁻¹ K⁻¹), nearly 5 times that of dry sand/soil (≈ 800 J kg⁻¹ K⁻¹). Water absorbs and releases large amounts of heat with minimal temperature change, exerting a strong moderating maritime influence on coastal towns, preventing extreme temperature swings seen in arid deserts.",
            "rough_work": "[ROUGH_WORK]\n(a) T_f = (C₁T₁ + C₂T₂) / (C₁ + C₂)\n(b) ΔT ∝ 1/c\n(c) P ∝ T at const V\n(d) c_water >> c_sand",
            "finalAnswer": "Explanations verified: (a) Equilibrium depends on thermal capacities m₁c₁ and m₂c₂; (b) High specific heat ensures maximum heat absorption per degree rise; (c) Friction heats trapped air raising pressure (P ∝ T); (d) High specific heat of sea water moderates coastal diurnal and seasonal temperatures.",
            "unit": "Qualitative Conceptual Derivation",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Exercise 11.3, Page 242",
            "image_search_query": "thermal contact specific heat coolant ocean climate"
        },
        {
            "problem": "NCERT Exercise 11.4: A cylinder with a movable piston contains 3 moles of hydrogen at standard temperature and pressure (STP). The walls of the cylinder are made of a heat insulator, and the piston is insulated by having a pile of sand on it. By what factor does the pressure of the gas increase if the gas is compressed to half its original volume? (Take γ = 1.4 for H₂)",
            "given": "Number of moles μ = 3 mol, Diatomic gas hydrogen H₂ has γ = 1.4, Perfectly insulated walls => Adiabatic process (ΔQ = 0), Initial volume = V₁, Final volume V₂ = V₁ / 2 => V₁ / V₂ = 2.0",
            "to_calculate": "Factor of pressure increase (P₂ / P₁)",
            "formula": "Adiabatic equation of state: P₁ · V₁^γ = P₂ · V₂^γ => P₂ / P₁ = (V₁ / V₂)^γ",
            "substitution": "P₂ / P₁ = (2.0)^1.4",
            "calculation": "(2)^1.4 = 2^(7/5) = 2^1.4\nUsing logarithms:\nlog₁₀(2^1.4) = 1.4 × log₁₀(2) = 1.4 × 0.30103 = 0.42144\nAntilog(0.42144) = 10^0.42144 = 2.639 ≈ 2.64",
            "rough_work": "[ROUGH_WORK]\n2^1.4 = 2.6390158\nFactor = 2.64",
            "finalAnswer": "The pressure of the gas increases by a factor of 2.64 (P₂ = 2.64 P₁)",
            "unit": "Dimensionless ratio",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Exercise 11.4, Page 242",
            "image_search_query": "adiabatic compression hydrogen pressure factor"
        },
        {
            "problem": "NCERT Exercise 11.5: In changing the state of a gas adiabatically from an equilibrium state A to another equilibrium state B, an amount of work equal to 22.3 J is done on the system. If the gas is taken from state A to B via a process in which the net heat absorbed by the system is 9.35 cal, how much is the net work done by the system in the latter case? (Take 1 cal = 4.19 J)",
            "given": "Adiabatic path (A → B): Work done on the system W_adia = -22.3 J, Heat exchanged Q_adia = 0 J\nNon-adiabatic path (A → B): Net heat absorbed Q = 9.35 cal, Conversion factor 1 cal = 4.19 J",
            "to_calculate": "Net work done by the system W in the second process",
            "formula": "First Law of Thermodynamics: ΔQ = ΔU + ΔW\nFor adiabatic path: ΔU = Q_adia - W_adia = 0 - (-22.3 J) = +22.3 J\nSince internal energy U is a state function, ΔU is identical for both paths: ΔU = +22.3 J\nFor second path: W = Q - ΔU",
            "substitution": "Q in Joules: Q = 9.35 cal × 4.19 J cal⁻¹ = 39.1765 J\nW = 39.1765 J - 22.3 J",
            "calculation": "Q = 9.35 × 4.19 = 39.18 J\nW = 39.18 - 22.30 = +16.88 J ≈ +16.9 J",
            "rough_work": "[ROUGH_WORK]\n9.35 × 4.19 = 39.1765\n39.1765 - 22.3 = 16.8765 ≈ 16.9 J",
            "finalAnswer": "Net work done by the system in the second process W = +16.9 J",
            "unit": "J",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Exercise 11.5, Page 242",
            "image_search_query": "first law state function internal energy work done"
        },
        {
            "problem": "NCERT Exercise 11.6: Two cylinders A and B of equal capacity are connected to each other via a stopcock. A contains a gas at standard temperature and pressure (STP: P₁ = 1 atm, T₁ = 273 K). B is completely evacuated. The entire system is thermally insulated. The stopcock is suddenly opened. Answer the following:\n(a) What is the final pressure of the gas in A and B?\n(b) What is the change in internal energy of the gas?\n(c) What is the change in the temperature of the gas?\n(d) Do the intermediate states of the system (before settling to the final equilibrium state) lie on its P-V-T surface?",
            "given": "Equal volume of cylinders V_A = V_B = V, Initial state in A: P₁ = 1 atm, V₁ = V, T₁ = 273 K; B is vacuum. Thermally insulated system (Q = 0). Sudden free expansion into vacuum.",
            "to_calculate": "(a) Final pressure P₂, (b) Change in internal energy ΔU, (c) Change in temperature ΔT, (d) Thermodynamic equilibrium path validity on P-V-T surface",
            "formula": "Free expansion of a gas against zero external opposing pressure: P_ext = 0 => W = 0.\nInsulated walls => Q = 0.\nFirst Law: ΔU = Q - W = 0 - 0 = 0.\nFor an ideal gas, U = U(T); since ΔU = 0 => ΔT = 0 (T₂ = T₁).\nBoyle's Law for initial and final states: P₁ · V₁ = P₂ · V₂.",
            "substitution": "(a) Total final volume V₂ = V_A + V_B = V + V = 2V\nP₂ = P₁ · (V₁ / V₂) = 1 atm × (V / 2V) = 0.5 atm",
            "calculation": "(a) Final pressure P₂ = 0.5 atm\n(b) Change in internal energy ΔU = 0 J (since Q = 0 and W = 0)\n(c) Change in temperature ΔT = 0 K (final temperature remains 273 K)\n(d) No. The free expansion is a rapid, turbulent, non-equilibrium irreversible process. Intermediate states have non-uniform pressure and temperature throughout the volume and do not correspond to thermodynamic equilibrium states, hence they do not lie on the equilibrium P-V-T equation of state surface.",
            "rough_work": "[ROUGH_WORK]\nFree expansion: W = 0, Q = 0 => ΔU = 0 => ΔT = 0.\nP₂ = P₁ / 2 = 0.5 atm.\nIntermediate states non-equilibrium => not on P-V-T surface.",
            "finalAnswer": "(a) Final pressure P₂ = 0.5 atm; (b) ΔU = 0; (c) ΔT = 0; (d) No, intermediate non-equilibrium states do not lie on the P-V-T surface.",
            "unit": "atm, J, K, Conceptual",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Exercise 11.6, Page 242",
            "image_search_query": "free expansion joule expansion pvt surface"
        },
        {
            "problem": "NCERT Exercise 11.7: An electric heater supplies heat to a system at a rate of 100 W. If the system performs work at a rate of 75 joules per second, at what rate is the internal energy increasing?",
            "given": "Rate of heat supply dQ/dt = +100 W = +100 J s⁻¹, Rate of work done by system dW/dt = +75 J s⁻¹",
            "to_calculate": "Rate of increase of internal energy (dU/dt)",
            "formula": "Differential form of First Law of Thermodynamics: dQ/dt = dU/dt + dW/dt => dU/dt = dQ/dt - dW/dt",
            "substitution": "dU/dt = 100 J s⁻¹ - 75 J s⁻¹",
            "calculation": "dU/dt = 25 J s⁻¹ = 25 W",
            "rough_work": "[ROUGH_WORK]\n100 - 75 = 25 W.",
            "finalAnswer": "Rate of increase of internal energy dU/dt = 25 W (or 25 J s⁻¹)",
            "unit": "W (or J s⁻¹)",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Exercise 11.7, Page 242",
            "image_search_query": "first law rate form internal energy power"
        },
        {
            "problem": "NCERT Exercise 11.8: A thermodynamic system is taken from an original state to an intermediate state by the linear process shown in Fig. 11.11. Its volume is then reduced to the original value from E to F by an isobaric process. Calculate the total work done by the gas from D to E to F. (Figure 11.11 specifications: State D: P_D = 6.0 × 10⁴ Pa, V_D = 2.0 m³; State E: P_E = 2.0 × 10⁴ Pa, V_E = 5.0 m³; State F: P_F = 2.0 × 10⁴ Pa, V_F = 2.0 m³)",
            "given": "Coordinates from Fig. 11.11:\nPoint D: (P_D = 6.0 × 10⁴ Pa, V_D = 2.0 m³)\nPoint E: (P_E = 2.0 × 10⁴ Pa, V_E = 5.0 m³)\nPoint F: (P_F = 2.0 × 10⁴ Pa, V_F = 2.0 m³)\nProcess D → E: Linear expansion from V = 2.0 m³ to 5.0 m³\nProcess E → F: Isobaric compression from V = 5.0 m³ to 2.0 m³ at constant P = 2.0 × 10⁴ Pa",
            "to_calculate": "Total work done by the gas W_total = W_DE + W_EF",
            "formula": "Work done is area under the P-V graph:\nW_DE = Area of trapezium under line DE = ½ · (P_D + P_E) · (V_E - V_D)\nW_EF = P_E · (V_F - V_E) = P_E · (V_D - V_E)\nTotal work W_total = W_DE + W_EF = Area of triangle DEF = ½ · (P_D - P_E) · (V_E - V_D)",
            "substitution": "W_DE = ½ × (6.0 × 10⁴ Pa + 2.0 × 10⁴ Pa) × (5.0 m³ - 2.0 m³) = ½ × (8.0 × 10⁴) × 3.0 J\nW_EF = (2.0 × 10⁴ Pa) × (2.0 m³ - 5.0 m³) = 2.0 × 10⁴ × (-3.0) J\nW_total = W_DE + W_EF",
            "calculation": "W_DE = 4.0 × 10⁴ × 3.0 = +1.20 × 10⁵ J = +120 kJ\nW_EF = 2.0 × 10⁴ × (-3.0) = -6.0 × 10⁴ J = -60 kJ\nW_total = 1.20 × 10⁵ J - 0.60 × 10⁵ J = +6.0 × 10⁴ J = +60 kJ\nDirect triangle check: W_total = Area(ΔDEF) = ½ × (P_D - P_F) × (V_E - V_D) = ½ × (4.0 × 10⁴) × 3.0 = 6.0 × 10⁴ J = 60 kJ.",
            "rough_work": "[ROUGH_WORK]\nTrapezium area = 0.5 × 80000 × 3 = 120,000 J\nIsobaric compression = 20000 × (-3) = -60,000 J\nTotal = 120,000 - 60,000 = 60,000 J = 60 kJ.",
            "finalAnswer": "Total work done by the gas from D to E to F is W_total = 6.0 × 10⁴ J (or 60 kJ)",
            "unit": "J (or kJ)",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Exercise 11.8, Page 243",
            "figure_reference": "Fig. 11.11",
            "image_search_query": "pv indicator diagram triangle work calculation"
        },
        {
            "problem": "NCERT Exercise 11.9: A refrigerator is to maintain eatables kept inside at 9 °C. If room temperature is 36 °C, calculate the coefficient of performance (COP) of the refrigerator.",
            "given": "Temperature inside refrigerator T₂ = 9 °C = (9 + 273.15) K = 282.15 K ≈ 282 K, Room temperature T₁ = 36 °C = (36 + 273.15) K = 309.15 K ≈ 309 K",
            "to_calculate": "Coefficient of performance (COP, β) of the refrigerator",
            "formula": "Ideal Carnot COP: β = T₂ / (T₁ - T₂)",
            "substitution": "β = 282.15 K / (309.15 K - 282.15 K) = 282.15 / 27.0",
            "calculation": "β = 282.15 / 27.0 = 10.45",
            "rough_work": "[ROUGH_WORK]\n282.15 / 27.0 = 10.45\nIf using 282 / 27 = 10.44.",
            "finalAnswer": "The coefficient of performance of the refrigerator is β = 10.45 (or 10.4)",
            "unit": "Dimensionless ratio",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Section 11.9, Standard Syllabus Exercise 11.9",
            "image_search_query": "refrigerator cop coefficient of performance calculation"
        },
        {
            "problem": "NCERT Exercise 11.10: A Carnot engine operates with an efficiency of 40% when its sink temperature is at 300 K. By how much must the source temperature be increased if the efficiency is to be increased to 50%, keeping the sink temperature unchanged?",
            "given": "Initial sink temperature T₂ = 300 K, Initial efficiency η₁ = 40% = 0.40, Target efficiency η₂ = 50% = 0.50, Sink temperature unchanged T₂' = 300 K",
            "to_calculate": "Increase in source temperature ΔT₁ = T₁' - T₁",
            "formula": "Carnot efficiency: η = 1 - (T₂ / T₁) => T₁ = T₂ / (1 - η)",
            "substitution": "Initial source temp: T₁ = 300 K / (1 - 0.40) = 300 / 0.60\nNew source temp: T₁' = 300 K / (1 - 0.50) = 300 / 0.50",
            "calculation": "T₁ = 300 / 0.60 = 500 K\nT₁' = 300 / 0.50 = 600 K\nIncrease ΔT₁ = T₁' - T₁ = 600 K - 500 K = 100 K",
            "rough_work": "[ROUGH_WORK]\nT₁ = 300 / 0.6 = 500 K\nT₁' = 300 / 0.5 = 600 K\nΔT₁ = 600 - 500 = 100 K",
            "finalAnswer": "The source temperature must be increased by 100 K (or 100 °C)",
            "unit": "K (or °C)",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 11, Section 11.11, Standard Syllabus Exercise 11.10",
            "image_search_query": "carnot engine efficiency source temperature increase"
        }
    ]

    modules[5]["concept_questions"] = [
        {
            "question": "In NCERT Exercise 11.5, when a gas is transformed from state A to B adiabatically, 22.3 J of work is done ON the system. Along another non-adiabatic path absorbing 39.2 J of heat, what is the net work done BY the gas?",
            "options": [
                "(Recommended) +16.9 J",
                "+61.5 J",
                "-16.9 J",
                "+22.3 J"
            ],
            "correctAnswer": "(Recommended) +16.9 J",
            "correct_answer": "(Recommended) +16.9 J",
            "explanation": "Since internal energy is a state function, ΔU = Q_adia - W_adia = 0 - (-22.3 J) = +22.3 J. For the new path: W = Q - ΔU = 39.2 J - 22.3 J = +16.9 J.",
            "hint": "Apply ΔU = Q - W with ΔU = +22.3 J.",
            "blooms_level": "Apply",
            "textbook_reference": "Exercise 11.5, Page 242",
            "image_search_query": "first law state function work calculation"
        },
        {
            "question": "During the free expansion of an ideal gas into a vacuum inside an insulated vessel (NCERT Exercise 11.6), why does the temperature of the gas remain unchanged?",
            "options": [
                "(Recommended) Because no heat is exchanged (Q = 0) and no work is done against vacuum (W = 0), so ΔU = 0, and U depends only on T for an ideal gas",
                "Because the molecules lose potential energy which converts into kinetic energy",
                "Because high pressure suppresses molecular speeds",
                "Because the stopcock conducts heat into the vacuum"
            ],
            "correctAnswer": "(Recommended) Because no heat is exchanged (Q = 0) and no work is done against vacuum (W = 0), so ΔU = 0, and U depends only on T for an ideal gas",
            "correct_answer": "(Recommended) Because no heat is exchanged (Q = 0) and no work is done against vacuum (W = 0), so ΔU = 0, and U depends only on T for an ideal gas",
            "explanation": "Free expansion involves no external opposing force (P_ext = 0 => W = 0) and no heat transfer through insulation (Q = 0). Thus ΔU = 0. For an ideal gas with zero intermolecular potential energy, U depends purely on T, so ΔT = 0.",
            "hint": "Analyze W and Q during expansion against zero opposing pressure.",
            "blooms_level": "Understand",
            "textbook_reference": "Exercise 11.6, Page 242",
            "image_search_query": "free expansion temperature ideal gas"
        },
        {
            "question": "In NCERT Exercise 11.4, when 3 moles of hydrogen gas are compressed adiabatically to half their initial volume (V₂ = V₁/2 with γ = 1.4), by what factor does the temperature of the gas change?",
            "options": [
                "(Recommended) Increases by a factor of 1.32 (T₂ = 1.32 T₁)",
                "Increases by a factor of 2.64",
                "Decreases by a factor of 0.50",
                "Remains constant because it is insulated"
            ],
            "correctAnswer": "(Recommended) Increases by a factor of 1.32 (T₂ = 1.32 T₁)",
            "correct_answer": "(Recommended) Increases by a factor of 1.32 (T₂ = 1.32 T₁)",
            "explanation": "For adiabatic process: T₁ · V₁^(γ-1) = T₂ · V₂^(γ-1) => T₂ / T₁ = (V₁ / V₂)^(γ-1) = (2)^0.4 ≈ 1.3195 ≈ 1.32.",
            "hint": "Use T₂/T₁ = (V₁/V₂)^(γ-1) with γ = 1.4.",
            "blooms_level": "Apply",
            "textbook_reference": "Exercise 11.4, Page 242",
            "image_search_query": "adiabatic compression temperature factor"
        },
        {
            "question": "For the cyclic process shown in Fig. 11.11 (NCERT Exercise 11.8), what does the net area enclosed by the triangle DEF represent on the P-V plane?",
            "options": [
                "(Recommended) The net work done by the system (+60 kJ) over the entire cycle D → E → F → D",
                "The total internal energy at vertex D",
                "The heat capacity of the working substance",
                "The mechanical efficiency of an ideal Carnot cycle"
            ],
            "correctAnswer": "(Recommended) The net work done by the system (+60 kJ) over the entire cycle D → E → F → D",
            "correct_answer": "(Recommended) The net work done by the system (+60 kJ) over the entire cycle D → E → F → D",
            "explanation": "On any P-V indicator diagram, the area enclosed by a clockwise closed curve represents the net mechanical work done by the system during one complete cycle: Area = ½ × base × height = ½ × 3.0 m³ × 4.0 × 10⁴ Pa = 60 kJ.",
            "hint": "Recall the geometric meaning of enclosed loop area on an indicator diagram.",
            "blooms_level": "Apply",
            "textbook_reference": "Exercise 11.8, Page 243",
            "figure_reference": "Fig. 11.11",
            "image_search_query": "enclosed area pv diagram net work"
        },
        {
            "question": "If an electric heater inputs 100 W of heat into a gas while the gas does mechanical expansion work at 75 W (NCERT Exercise 11.7), what will happen to the gas temperature?",
            "options": [
                "(Recommended) The temperature will increase because internal energy rises at a rate of 25 W",
                "The temperature will decrease because 75 W of work is done",
                "The temperature will remain constant because work and heat balance",
                "The temperature will oscillate between 75 °C and 100 °C"
            ],
            "correctAnswer": "(Recommended) The temperature will increase because internal energy rises at a rate of 25 W",
            "correct_answer": "(Recommended) The temperature will increase because internal energy rises at a rate of 25 W",
            "explanation": "Rate of internal energy change dU/dt = dQ/dt - dW/dt = 100 W - 75 W = +25 W > 0. Since dU > 0, the internal energy and therefore the temperature of the gas must rise.",
            "hint": "Check the sign of dU/dt = dQ/dt - dW/dt.",
            "blooms_level": "Understand",
            "textbook_reference": "Exercise 11.7, Page 242",
            "image_search_query": "first law rate form internal energy temperature"
        },
        {
            "question": "A Carnot engine has an efficiency of 40% with sink at 300 K. To raise the efficiency to 50% without altering the sink temperature (NCERT Exercise 11.10), what must be the new source temperature?",
            "options": [
                "(Recommended) 600 K (an increase of 100 K)",
                "500 K (no increase needed)",
                "750 K (an increase of 250 K)",
                "400 K (a decrease of 100 K)"
            ],
            "correctAnswer": "(Recommended) 600 K (an increase of 100 K)",
            "correct_answer": "(Recommended) 600 K (an increase of 100 K)",
            "explanation": "Initial: 1 - 300/T₁ = 0.40 => T₁ = 300/0.6 = 500 K. Target: 1 - 300/T₁' = 0.50 => T₁' = 300/0.5 = 600 K. Increase = 600 - 500 = 100 K.",
            "hint": "Use T₁ = T₂ / (1 - η) for η = 0.4 and η = 0.5.",
            "blooms_level": "Apply",
            "textbook_reference": "Section 11.11, Standard Syllabus Exercise 11.10",
            "image_search_query": "carnot engine efficiency source temp increase"
        }
    ]

    with open("scripts/physics_class11_modules/physics_modules_ch11.json", "w", encoding="utf-8") as f:
        json.dump(modules, f, indent=2, ensure_ascii=False)
    print("Chapter 11 successfully enriched!")

if __name__ == "__main__":
    build_ch11()
