import json

def build_ch12():
    with open("scripts/physics_class11_modules/physics_modules_ch12.json", "r", encoding="utf-8") as f:
        modules = json.load(f)

    # -------------------------------------------------------------
    # Module 71: Molecular Nature of Matter & Ideal Gas Equation
    # -------------------------------------------------------------
    modules[0]["worked_examples"] = [
        {
            "problem": "NCERT Example 12.1: The density of water is 1000 kg m⁻³. The density of water vapour at 100 °C and 1 atm pressure is 0.6 kg m⁻³. The volume of a molecule multiplied by the total number gives what is called molecular volume. Estimate the ratio (or fraction) of the molecular volume to the total volume occupied by water vapour under these conditions.",
            "given": "Density of liquid water ρ_liquid = 1000 kg m⁻³, Density of water vapour ρ_vapour = 0.6 kg m⁻³, Temperature T = 100 °C = 373 K, Pressure P = 1 atm",
            "to_calculate": "Ratio of molecular volume to total volume (V_molecular / V_total)",
            "formula": "Consider 1 kg of water:\nVolume in liquid state: V_liquid = M / ρ_liquid = 1 / 1000 m³ = 1.0 × 10⁻³ m³\nVolume in vapour state: V_vapour = M / ρ_vapour = 1 / 0.6 m³ = 1.67 m³\nIn liquid state, molecules are tightly packed, so molecular volume V_molecular ≈ V_liquid.\nFraction = V_molecular / V_total = V_liquid / V_vapour = ρ_vapour / ρ_liquid",
            "substitution": "Fraction = (0.6 kg m⁻³) / (1000 kg m⁻³)",
            "calculation": "Fraction = 0.6 × 10⁻³ = 6.0 × 10⁻⁴ ≈ 1 / 1670",
            "rough_work": "[ROUGH_WORK]\n0.6 / 1000 = 6 × 10⁻⁴\n1 / 1.67 = 0.6",
            "finalAnswer": "The fraction of molecular volume to the total volume occupied by water vapour is 6.0 × 10⁻⁴ (or 1 / 1670)",
            "unit": "Dimensionless ratio",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Example 12.1, Page 247",
            "image_search_query": "molecular volume vs total volume water vapour"
        },
        {
            "problem": "NCERT Example 12.2: Estimate the volume of a water molecule using the data in Example 12.1.",
            "given": "Density of water ρ = 1000 kg m⁻³, Molar mass of water M = 18 g mol⁻¹ = 18 × 10⁻³ kg mol⁻¹, Avogadro's number N_A = 6.023 × 10²³ molecules mol⁻¹",
            "to_calculate": "Volume of a single water molecule V_molecule",
            "formula": "Mass of one mole of water = 18 × 10⁻³ kg\nVolume of one mole of liquid water: V_mole = M / ρ\nNumber of molecules in one mole = N_A\nVolume per molecule: V_molecule = V_mole / N_A = M / (ρ · N_A)",
            "substitution": "V_molecule = (18 × 10⁻³ kg mol⁻¹) / [ (1000 kg m⁻³) × (6.023 × 10²³ mol⁻¹) ]",
            "calculation": "V_molecule = 18 × 10⁻³ / (6.023 × 10²⁶) = 2.988 × 10⁻²⁹ m³ ≈ 3.0 × 10⁻²⁹ m³",
            "rough_work": "[ROUGH_WORK]\n18 / 6.023 = 2.9885\n10⁻³ / 10²⁶ = 10⁻²⁹ m³",
            "finalAnswer": "Volume of a water molecule V_molecule = 3.0 × 10⁻²⁹ m³",
            "unit": "m³",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Example 12.2, Page 248",
            "image_search_query": "water molecule volume estimate avogadro"
        },
        {
            "problem": "NCERT Example 12.3: What is the average distance between atoms (interatomic distance) in water? Use the data given in Examples 12.1 and 12.2.",
            "given": "Volume of one water molecule V_molecule ≈ 3.0 × 10⁻²⁹ m³ from Example 12.2, One molecule of H₂O contains 3 atoms (2 Hydrogen + 1 Oxygen)",
            "to_calculate": "Average interatomic distance d_interatomic",
            "formula": "Volume per atom: V_atom = V_molecule / 3\nAssuming each atom occupies a cubic volume of side d: V_atom = d³ => d = (V_atom)^(1/3) = [ V_molecule / 3 ]^(1/3)",
            "substitution": "V_atom = (3.0 × 10⁻²⁹ m³) / 3 = 1.0 × 10⁻²⁹ m³\nd = (10 × 10⁻³⁰ m³)^(1/3) = (10)^(1/3) × 10⁻¹⁰ m",
            "calculation": "(10)^(1/3) ≈ 2.154\nd = 2.154 × 10⁻¹⁰ m ≈ 2.2 × 10⁻¹⁰ m = 2.2 Å (or 0.22 nm)",
            "rough_work": "[ROUGH_WORK]\n10^(1/3) = 2.1544\nd ≈ 2.2 Å",
            "finalAnswer": "The average interatomic distance in liquid water is approximately 2.2 Å (2.2 × 10⁻¹⁰ m)",
            "unit": "m (or Å)",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Example 12.3, Page 248",
            "image_search_query": "interatomic distance water molecules angstrom"
        },
        {
            "problem": "NCERT Example 12.4: A vessel contains two non-reactive gases: neon (monatomic) and oxygen (diatomic). The ratio of their partial pressures is 3 : 2. Estimate the ratio of (i) number of molecules, and (ii) mass density of neon to oxygen in the vessel. (Given atomic mass of Ne = 20.2 u, molecular mass of O₂ = 32.0 u)",
            "given": "Vessel volume V and temperature T are common to both gases.\nRatio of partial pressures P_Ne / P_O₂ = 3 / 2 = 1.5\nAtomic mass of neon M_Ne = 20.2 g mol⁻¹\nMolecular mass of oxygen M_O₂ = 32.0 g mol⁻¹",
            "to_calculate": "(i) Ratio of number of molecules (N_Ne / N_O₂), (ii) Ratio of mass densities (ρ_Ne / ρ_O₂)",
            "formula": "(i) Ideal gas equation: P = n · k_B · T = (N / V) · k_B · T => P₁ / P₂ = N₁ / N₂\n(ii) Density ρ = (total mass) / V = (μ · M) / V = (P · M) / (R · T) => ρ₁ / ρ₂ = (P₁ / P₂) · (M₁ / M₂)",
            "substitution": "(i) N_Ne / N_O₂ = P_Ne / P_O₂ = 3 / 2\n(ii) ρ_Ne / ρ_O₂ = (3 / 2) × (20.2 / 32.0)",
            "calculation": "(i) N_Ne / N_O₂ = 3 : 2 = 1.5\n(ii) ρ_Ne / ρ_O₂ = 1.5 × (20.2 / 32.0) = 1.5 × 0.63125 = 0.947 ≈ 0.95",
            "rough_work": "[ROUGH_WORK]\n3/2 = 1.5\n1.5 × 20.2 / 32 = 30.3 / 32 = 0.946875 ≈ 0.95",
            "finalAnswer": "(i) Ratio of number of molecules N_Ne : N_O₂ = 3 : 2; (ii) Ratio of mass densities ρ_Ne : ρ_O₂ = 0.95 : 1 (or 30.3 / 32)",
            "unit": "Dimensionless ratio",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Example 12.4, Page 248",
            "image_search_query": "dalton law partial pressure gas mixture density"
        }
    ]

    modules[0]["concept_questions"] = [
        {
            "question": "Under what physical conditions does a real gas behave most closely like an ideal gas obeying PV = μRT?",
            "options": [
                "(Recommended) At low pressure and high temperature",
                "At high pressure and low temperature",
                "At very low temperature and high pressure",
                "At critical temperature and high density"
            ],
            "correctAnswer": "(Recommended) At low pressure and high temperature",
            "correct_answer": "(Recommended) At low pressure and high temperature",
            "explanation": "At low pressures, intermolecular distances are large, making intermolecular attractive forces negligible. At high temperatures, molecular kinetic energies vastly exceed intermolecular potential energies, satisfying ideal gas postulates.",
            "hint": "Think about when intermolecular forces and molecular volume become negligible.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 12.3, Page 246",
            "image_search_query": "real gas ideal gas low pressure high temperature"
        },
        {
            "question": "What is the physical interpretation of the universal gas constant R in the ideal gas equation PV = μRT?",
            "options": [
                "(Recommended) The mechanical work done by 1 mole of an ideal gas when its temperature is increased by 1 K at constant pressure (R = P·ΔV)",
                "The total kinetic energy of 1 kg of any gas at absolute zero",
                "The force exerted by 1 molecule per unit container area",
                "The ratio of specific heat capacities γ = C_p / C_v"
            ],
            "correctAnswer": "(Recommended) The mechanical work done by 1 mole of an ideal gas when its temperature is increased by 1 K at constant pressure (R = P·ΔV)",
            "correct_answer": "(Recommended) The mechanical work done by 1 mole of an ideal gas when its temperature is increased by 1 K at constant pressure (R = P·ΔV)",
            "explanation": "From P·V = R·T for 1 mole, at constant pressure: P·ΔV = R·ΔT. For ΔT = 1 K, external work done is W = P·ΔV = R. Hence R (8.314 J mol⁻¹ K⁻¹) represents the expansion work per mole per kelvin.",
            "hint": "Consider isobaric expansion work W = P·ΔV for ΔT = 1 K.",
            "blooms_level": "Analyze",
            "textbook_reference": "Section 12.3, Page 246",
            "image_search_query": "universal gas constant work per mole kelvin"
        },
        {
            "question": "According to Avogadro's hypothesis, what is true for equal volumes of all ideal gases at identical temperature and pressure?",
            "options": [
                "(Recommended) They contain an identical number of molecules",
                "They possess identical total mass and density",
                "Their molecules travel at the exact same root mean square speed",
                "They exert pressures inversely proportional to their molar masses"
            ],
            "correctAnswer": "(Recommended) They contain an identical number of molecules",
            "correct_answer": "(Recommended) They contain an identical number of molecules",
            "explanation": "From P·V = N·k_B·T, if P, V, and T are identical, then N = PV / (k_B·T) must be strictly identical for all gases regardless of molecular composition.",
            "hint": "Check the relation N = PV / (k_B·T).",
            "blooms_level": "Understand",
            "textbook_reference": "Section 12.3, Page 247",
            "image_search_query": "avogadro hypothesis equal volumes equal molecules"
        },
        {
            "question": "What is the value of Boltzmann's constant k_B in terms of the universal gas constant R and Avogadro's number N_A?",
            "options": [
                "(Recommended) k_B = R / N_A = 1.38 × 10⁻²³ J K⁻¹",
                "k_B = R · N_A = 5.00 × 10²⁴ J K⁻¹",
                "k_B = N_A / R = 7.24 × 10²² J K⁻¹",
                "k_B = √(R · N_A)"
            ],
            "correctAnswer": "(Recommended) k_B = R / N_A = 1.38 × 10⁻²³ J K⁻¹",
            "correct_answer": "(Recommended) k_B = R / N_A = 1.38 × 10⁻²³ J K⁻¹",
            "explanation": "Boltzmann's constant is the gas constant per individual molecule: k_B = R / N_A = 8.314 / (6.022 × 10²³) = 1.38 × 10⁻²³ J K⁻¹.",
            "hint": "Divide the molar gas constant by the number of molecules per mole.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 12.3, Page 247",
            "image_search_query": "boltzmann constant definition r over na"
        }
    ]

    # -------------------------------------------------------------
    # Module 72: Kinetic Theory Postulates & Derivation of Pressure
    # -------------------------------------------------------------
    modules[1]["worked_examples"] = [
        {
            "problem": "NCERT Example 12.5: A flask contains argon and chlorine in the ratio of 2 : 1 by mass. The temperature of the mixture is 27 °C. Obtain the ratio of (i) average kinetic energy per molecule, and (ii) root mean square speed v_rms of the molecules of the two gases. (Atomic mass of argon Ar = 39.9 u, Molecular mass of chlorine Cl₂ = 70.9 u)",
            "given": "Mass ratio m_Ar / m_Cl₂ = 2 / 1, Temperature of mixture T = 27 °C = 300.15 K (common to both gases), Molar mass of Argon M_Ar = 39.9 g mol⁻¹, Molar mass of Chlorine M_Cl₂ = 70.9 g mol⁻¹",
            "to_calculate": "(i) Ratio of average kinetic energy per molecule (E_Ar / E_Cl₂), (ii) Ratio of root mean square speed (v_rms(Ar) / v_rms(Cl₂))",
            "formula": "(i) Average translational kinetic energy per molecule depends solely on absolute temperature: E = (3/2) · k_B · T. Since T is identical for both gases, E₁ / E₂ = 1.\n(ii) Root-mean-square speed: v_rms = √(3 · k_B · T / m) = √(3 · R · T / M) => v_rms(Ar) / v_rms(Cl₂) = √(M_Cl₂ / M_Ar)",
            "substitution": "(i) E_Ar / E_Cl₂ = (3/2 k_B T) / (3/2 k_B T) = 1.0\n(ii) v_rms(Ar) / v_rms(Cl₂) = √(70.9 / 39.9)",
            "calculation": "(i) Ratio of average KE per molecule = 1 : 1 = 1.0\n(ii) 70.9 / 39.9 = 1.7769\n√(1.7769) = 1.333 ≈ 1.33",
            "rough_work": "[ROUGH_WORK]\nKE depends only on T => ratio = 1\nv_rms ∝ 1/sqrt(M)\nsqrt(70.9 / 39.9) = sqrt(1.777) = 1.333",
            "finalAnswer": "(i) Ratio of average translational kinetic energy per molecule = 1 : 1; (ii) Ratio of rms speed v_rms(Ar) : v_rms(Cl₂) = 1.33 : 1",
            "unit": "Dimensionless ratio",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Example 12.5, Page 250",
            "image_search_query": "rms speed kinetic energy temperature gas mixture"
        },
        {
            "problem": "NCERT Example 12.6: Uranium has two isotopes of masses 235 and 238 units. If both are present in Uranium hexafluoride (UF₆) gas, which would have the larger average speed? If atomic mass of fluorine is 19 units, calculate the percentage difference in their average speeds.",
            "given": "Molar masses of isotopes:\n²³⁵UF₆: M₁ = 235 + 6 × 19 = 235 + 114 = 349 g mol⁻¹\n²³⁸UF₆: M₂ = 238 + 6 × 19 = 238 + 114 = 352 g mol⁻¹\nGas is in thermal equilibrium at temperature T",
            "to_calculate": "Which isotope molecule has larger speed, and percentage difference in speeds Δv / v",
            "formula": "Average speed v_avg ∝ 1 / √M. Since M₁ < M₂, the lighter molecule ²³⁵UF₆ has a larger average speed.\nSpeed ratio: v₁ / v₂ = √(M₂ / M₁) = (M₂ / M₁)^(1/2)\nFractional difference: (v₁ - v₂) / v₂ = √(M₂ / M₁) - 1 ≈ ½ · (M₂ - M₁) / M₂",
            "substitution": "v₁ / v₂ = √(352 / 349) = (1 + 3/349)^(1/2) ≈ 1 + ½ · (3 / 349)",
            "calculation": "Fractional difference = ½ × (3 / 349) = 1.5 / 349 = 0.004298\nPercentage difference = 0.004298 × 100% = 0.43%",
            "rough_work": "[ROUGH_WORK]\n352 / 349 = 1.008596\nsqrt(1.008596) = 1.004288\nDifference = 0.004288 × 100 = 0.43%",
            "finalAnswer": "²³⁵UF₆ has the larger average speed. The percentage difference in their average speeds is 0.43%",
            "unit": "%",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Example 12.6, Page 251",
            "image_search_query": "uranium hexafluoride isotope separation diffusion speed"
        }
    ]

    modules[1]["concept_questions"] = [
        {
            "question": "In the derivation of ideal gas pressure P = (1/3) ρ v_rms², where does the factor of 1/3 originate physically?",
            "options": [
                "(Recommended) From the three-dimensional isotropy of molecular motion: <v_x²> = <v_y²> = <v_z²> = (1/3) <v²>",
                "From the three atoms present in a typical gas molecule",
                "From the ratio of elastic collision momentum before and after impact",
                "From the spherical geometry of the container walls"
            ],
            "correctAnswer": "(Recommended) From the three-dimensional isotropy of molecular motion: <v_x²> = <v_y²> = <v_z²> = (1/3) <v²>",
            "correct_answer": "(Recommended) From the three-dimensional isotropy of molecular motion: <v_x²> = <v_y²> = <v_z²> = (1/3) <v²>",
            "explanation": "Molecules move randomly with equal probability in all three Cartesian dimensions. Because <v²> = <v_x²> + <v_y²> + <v_z²> and motion is isotropic, <v_x²> = (1/3) <v²>. Only the component normal to the wall delivers momentum.",
            "hint": "Analyze the spatial distribution of velocity vectors in 3D space.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 12.4, Page 249",
            "image_search_query": "derivation ideal gas pressure isotropy 1 3"
        },
        {
            "question": "What is the change in momentum of a gas molecule of mass m travelling with velocity component v_x when it collides elastically with a perpendicular rigid wall?",
            "options": [
                "(Recommended) Δp_x = -2 m v_x (transferring +2 m v_x to the wall)",
                "Δp_x = 0 (momentum is conserved with zero exchange)",
                "Δp_x = -m v_x (the molecule stops at the wall)",
                "Δp_x = -½ m v_x²"
            ],
            "correctAnswer": "(Recommended) Δp_x = -2 m v_x (transferring +2 m v_x to the wall)",
            "correct_answer": "(Recommended) Δp_x = -2 m v_x (transferring +2 m v_x to the wall)",
            "explanation": "Initial momentum is +m v_x. For a perfectly elastic collision with a stationary massive wall, it rebounds with speed -v_x. Change in momentum = (-m v_x) - (m v_x) = -2 m v_x.",
            "hint": "Subtract final momentum (-m v_x) from initial momentum (+m v_x).",
            "blooms_level": "Apply",
            "textbook_reference": "Section 12.4, Page 249",
            "image_search_query": "elastic collision molecule wall momentum transfer"
        },
        {
            "question": "If the absolute temperature of an ideal gas in a rigid container is quadrupled (T' = 4T), by what factors do the root mean square speed v_rms and the pressure P change?",
            "options": [
                "(Recommended) v_rms doubles (×2), and P quadruples (×4)",
                "v_rms quadruples (×4), and P doubles (×2)",
                "v_rms quadruples (×4), and P quadruples (×4)",
                "v_rms doubles (×2), and P remains constant"
            ],
            "correctAnswer": "(Recommended) v_rms doubles (×2), and P quadruples (×4)",
            "correct_answer": "(Recommended) v_rms doubles (×2), and P quadruples (×4)",
            "explanation": "v_rms = √(3k_B T / m) ∝ √T => for T' = 4T, v_rms' = √4 · v_rms = 2 v_rms. By Gay-Lussac's law at constant volume, P ∝ T => P' = 4P.",
            "hint": "Note that v_rms scales as √T while P scales linearly as T.",
            "blooms_level": "Apply",
            "textbook_reference": "Section 12.4, Page 250",
            "image_search_query": "rms speed pressure temperature proportionality"
        },
        {
            "question": "Which basic postulate of kinetic theory of gases directly implies that the pressure exerted by a gas is completely uniform in all directions?",
            "options": [
                "(Recommended) Random, chaotic molecular motion with isotropic velocity distribution in all spatial directions",
                "Molecules are hard point masses with zero gravitational attraction",
                "The duration of collision is much smaller than time between collisions",
                "Collisions between molecules and walls are perfectly inelastic"
            ],
            "correctAnswer": "(Recommended) Random, chaotic molecular motion with isotropic velocity distribution in all spatial directions",
            "correct_answer": "(Recommended) Random, chaotic molecular motion with isotropic velocity distribution in all spatial directions",
            "explanation": "Complete spatial randomness and isotropic velocities guarantee that equal numbers of molecules strike any equal area of the container walls per second from all directions, rendering pressure a scalar quantity.",
            "hint": "Focus on the isotropy of velocity vectors.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 12.4, Page 249",
            "image_search_query": "isotropic pressure gas kinetic theory"
        }
    ]

    # -------------------------------------------------------------
    # Module 73: Kinetic Interpretation of Temperature & Speeds
    # -------------------------------------------------------------
    modules[2]["worked_examples"] = [
        {
            "problem": "NCERT Example 12.7: (a) When a molecule (or an elastic ball) hits a massive stationary wall, it rebounds with the same speed. However, when the bat is moving towards the ball with speed u, show that the ball rebounds with speed (v + 2u). (b) Explain on this basis how the temperature of a gas rises when it is rapidly compressed by a moving piston.",
            "given": "Initial ball/molecule speed = v (towards wall/bat), Piston/bat speed = u (towards ball/molecule), Massive piston (M >> m), Perfectly elastic collision",
            "to_calculate": "(a) Rebound speed in lab frame, (b) Mechanism of temperature rise during compression",
            "formula": "Transform to frame of moving piston:\nIn piston frame, initial approaching speed = v + u.\nSince collision is elastic and piston is massive, rebound speed in piston frame = v + u.\nTransform back to laboratory frame:\nRebound speed in lab frame v' = (rebound speed relative to piston) + (piston speed) = (v + u) + u = v + 2u.\nChange in kinetic energy: ΔK = ½ m (v')² - ½ m v² = ½ m (v + 2u)² - ½ m v² > 0.",
            "substitution": "v' = v + 2u\nΔK = ½ m [ (v + 2u)² - v² ] = ½ m [ 4uv + 4u² ] = 2 m u (v + u)",
            "calculation": "Each molecular collision with the advancing piston imparts extra kinetic energy ΔK = 2mu(v+u) to the molecule.\nSince temperature T is directly proportional to average molecular translational kinetic energy (<E> = 3/2 k_B T), the incessant collisions with the inward-moving piston increase the mean kinetic energy of all gas molecules, causing the macroscopic temperature to rise.",
            "rough_work": "[ROUGH_WORK]\nRelative velocity before = v + u\nRelative velocity after = -(v + u)\nIn lab frame: -(v + u) + u = -(v + 2u)\nSpeed increases by 2u.",
            "finalAnswer": "(a) Rebound speed = v + 2u; (b) Each collision with advancing piston increases molecular kinetic energy, raising average KE and thus raising macroscopic temperature T.",
            "unit": "m s⁻¹, Conceptual",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Example 12.7, Pages 251-252",
            "image_search_query": "elastic collision moving piston gas heating"
        },
        {
            "problem": "Calculate and compare the root-mean-square speed (v_rms), average speed (v_avg), and most probable speed (v_mp) of oxygen molecules (O₂, M = 32.0 × 10⁻³ kg mol⁻¹) at room temperature T = 300 K. (Take R = 8.314 J mol⁻¹ K⁻¹, π = 3.1416)",
            "given": "Gas: Oxygen (O₂), Molar mass M = 32.0 × 10⁻³ kg mol⁻¹, Absolute temperature T = 300 K, Gas constant R = 8.314 J mol⁻¹ K⁻¹",
            "to_calculate": "Values of v_mp, v_avg, and v_rms and verify their ratio",
            "formula": "v_mp = √(2 · R · T / M)\nv_avg = √(8 · R · T / (π · M))\nv_rms = √(3 · R · T / M)\nRatio: v_mp : v_avg : v_rms = √2 : √(8/π) : √3 ≈ 1 : 1.128 : 1.225",
            "substitution": "Factor (R · T / M) = (8.314 × 300) / (0.032) = 2494.2 / 0.032 = 77943.75 m² s⁻²\nv_mp = √(2 × 77943.75) = √(155887.5)\nv_avg = √(8 × 77943.75 / 3.1416) = √(198481.6)\nv_rms = √(3 × 77943.75) = √(233831.25)",
            "calculation": "v_mp = 394.8 m s⁻¹ ≈ 395 m s⁻¹\nv_avg = 445.5 m s⁻¹ ≈ 446 m s⁻¹\nv_rms = 483.6 m s⁻¹ ≈ 484 m s⁻¹\nRatio check: 395 : 446 : 484 = 1 : 1.129 : 1.225.",
            "rough_work": "[ROUGH_WORK]\nRT/M = 77943.75\nsqrt(2 × 77943.75) = 394.82 m/s\nsqrt(8 × 77943.75 / pi) = 445.51 m/s\nsqrt(3 × 77943.75) = 483.56 m/s",
            "finalAnswer": "For O₂ at 300 K: v_mp = 395 m s⁻¹, v_avg = 446 m s⁻¹, v_rms = 484 m s⁻¹ (v_mp < v_avg < v_rms)",
            "unit": "m s⁻¹",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Section 12.4, Page 252",
            "image_search_query": "maxwell distribution rms average most probable speed"
        }
    ]

    modules[2]["concept_questions"] = [
        {
            "question": "What is the physical meaning of absolute zero temperature (0 K) in the framework of the classical kinetic theory of gases?",
            "options": [
                "(Recommended) The theoretical temperature at which all random translational molecular motion completely ceases (<v²> = 0)",
                "The freezing temperature of liquid water at 1 atm",
                "The point where all gases dissociate into individual atomic nuclei and electrons",
                "The temperature where the gas density reaches infinity"
            ],
            "correctAnswer": "(Recommended) The theoretical temperature at which all random translational molecular motion completely ceases (<v²> = 0)",
            "correct_answer": "(Recommended) The theoretical temperature at which all random translational molecular motion completely ceases (<v²> = 0)",
            "explanation": "Since average translational kinetic energy is ½ m <v²> = 3/2 k_B T, as T → 0 K, the mean square molecular velocity <v²> approaches zero, meaning classical thermal motion ceases.",
            "hint": "Relate temperature T directly to mean squared molecular velocity <v²>.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 12.4.2, Page 251",
            "image_search_query": "absolute zero molecular motion kinetic theory"
        },
        {
            "question": "At the same temperature T, how does the average kinetic energy per molecule of hydrogen (H₂) compare with that of oxygen (O₂)?",
            "options": [
                "(Recommended) They are strictly identical, both equal to (3/2) k_B T",
                "Hydrogen has 16 times higher kinetic energy because it is lighter",
                "Oxygen has 16 times higher kinetic energy because of greater mass",
                "Hydrogen has 4 times higher kinetic energy"
            ],
            "correctAnswer": "(Recommended) They are strictly identical, both equal to (3/2) k_B T",
            "correct_answer": "(Recommended) They are strictly identical, both equal to (3/2) k_B T",
            "explanation": "Average translational kinetic energy per molecule depends solely on absolute temperature: <E> = (3/2) k_B T, completely independent of the mass or nature of the gas molecule.",
            "hint": "Check if mass m appears in the formula for average kinetic energy per molecule.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 12.4.2, Page 251",
            "image_search_query": "average kinetic energy temperature independence mass"
        },
        {
            "question": "For any ideal gas at thermal equilibrium, what is the exact mathematical ordering of the three characteristic molecular speeds?",
            "options": [
                "(Recommended) v_mp < v_avg < v_rms",
                "v_rms < v_avg < v_mp",
                "v_avg < v_mp < v_rms",
                "v_mp = v_avg = v_rms"
            ],
            "correctAnswer": "(Recommended) v_mp < v_avg < v_rms",
            "correct_answer": "(Recommended) v_mp < v_avg < v_rms",
            "explanation": "v_mp = √(2RT/M) ≈ 1.414 √(RT/M); v_avg = √(8RT/πM) ≈ 1.596 √(RT/M); v_rms = √(3RT/M) ≈ 1.732 √(RT/M). Therefore, v_mp < v_avg < v_rms.",
            "hint": "Compare the numerical coefficients √2, √(8/π), and √3.",
            "blooms_level": "Analyze",
            "textbook_reference": "Section 12.4, Page 252",
            "image_search_query": "maxwell speed distribution ordering rms avg mp"
        },
        {
            "question": "Why does the Earth's atmosphere retain oxygen and nitrogen molecules but possesses virtually zero free hydrogen or helium gas?",
            "options": [
                "(Recommended) The root-mean-square speeds of hydrogen and helium at atmospheric temperatures exceed the Earth's escape velocity (11.2 km/s), allowing them to escape into space",
                "Hydrogen and helium are chemically unstable in sunlight",
                "Heavier gases exert gravitational repulsion on light gases",
                "Light gases dissolve completely into the oceans"
            ],
            "correctAnswer": "(Recommended) The root-mean-square speeds of hydrogen and helium at atmospheric temperatures exceed the Earth's escape velocity (11.2 km/s), allowing them to escape into space",
            "correct_answer": "(Recommended) The root-mean-square speeds of hydrogen and helium at atmospheric temperatures exceed the Earth's escape velocity (11.2 km/s), allowing them to escape into space",
            "explanation": "Because v_rms ∝ 1/√M, light molecules like H₂ and He have significantly higher speeds in the high-energy tail of the Maxwell distribution that exceed Earth's escape velocity (11.2 km/s), evaporating into space over geological time.",
            "hint": "Compare v_rms for light gases with Earth's escape velocity.",
            "blooms_level": "Apply",
            "textbook_reference": "Section 12.4, Page 252",
            "image_search_query": "planetary atmosphere escape velocity rms speed"
        }
    ]

    # -------------------------------------------------------------
    # Module 74: Equipartition of Energy & Specific Heats
    # -------------------------------------------------------------
    modules[3]["worked_examples"] = [
        {
            "problem": "NCERT Example 12.8: A cylinder of fixed capacity 44.8 litres contains helium gas at standard temperature and pressure (STP). What is the amount of heat needed to raise the temperature of the gas in the cylinder by 15.0 °C ? (Take R = 8.31 J mol⁻¹ K⁻¹)",
            "given": "Volume of cylinder V = 44.8 L = 44.8 × 10⁻³ m³, Fixed capacity => Constant volume process (isochoric, dV = 0), Gas: Helium (monatomic => degrees of freedom f = 3), Standard temperature and pressure (STP) where 1 mole occupies 22.4 L, Temperature rise ΔT = 15.0 °C = 15.0 K, Gas constant R = 8.31 J mol⁻¹ K⁻¹",
            "to_calculate": "Heat required at constant volume Q_v",
            "formula": "Number of moles: μ = V / V_molar = 44.8 L / 22.4 L = 2.0 mol\nFor monatomic gas: C_v = (3/2) · R\nHeat supplied at constant volume: Q_v = μ · C_v · ΔT = μ · (3/2 R) · ΔT",
            "substitution": "μ = 2.0 mol\nC_v = 1.5 × 8.31 J mol⁻¹ K⁻¹ = 12.465 J mol⁻¹ K⁻¹\nQ_v = 2.0 mol × 12.465 J mol⁻¹ K⁻¹ × 15.0 K",
            "calculation": "Q_v = 2.0 × 15.0 × 12.465 = 30.0 × 12.465 = 373.95 J ≈ 374 J",
            "rough_work": "[ROUGH_WORK]\n44.8 / 22.4 = 2 moles\n3/2 × 8.31 = 12.465\nQ = 2 × 12.465 × 15 = 30 × 12.465 = 373.95 J",
            "finalAnswer": "The amount of heat needed to raise the temperature is 374 J",
            "unit": "J",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Example 12.8, Page 254",
            "image_search_query": "molar heat capacity helium constant volume stp"
        },
        {
            "problem": "Using the Law of Equipartition of Energy, calculate the theoretical molar heat capacities C_v, C_p, and the ratio γ = C_p / C_v for Carbon Dioxide (CO₂, a linear triatomic molecule) at high temperatures where its vibrational modes become active. (Linear molecule has 3 translational, 2 rotational, and 4 vibrational modes with each vibrational mode contributing 2 quadratic terms: KE + PE)",
            "given": "Molecule: CO₂ (linear triatomic: O=C=O)\nTranslational degrees of freedom f_trans = 3\nRotational degrees of freedom f_rot = 2\nVibrational modes = 3N - 5 = 3(3) - 5 = 4 modes\nEach vibrational mode has 2 quadratic energy terms (kinetic + potential) => f_vib = 4 × 2 = 8 terms",
            "to_calculate": "Total internal energy U, C_v, C_p, and γ",
            "formula": "Total energy per molecule: E = (f_trans/2 + f_rot/2 + f_vib/2) · k_B · T = (3/2 + 2/2 + 8/2) · k_B · T = (13/2) · k_B · T\nMolar internal energy: U = (13/2) · R · T\nC_v = dU / dT = (13/2) · R\nC_p = C_v + R = (15/2) · R\nγ = C_p / C_v = 15 / 13",
            "substitution": "C_v = 6.5 × 8.314 J mol⁻¹ K⁻¹\nC_p = 7.5 × 8.314 J mol⁻¹ K⁻¹\nγ = 15 / 13",
            "calculation": "C_v = 54.04 J mol⁻¹ K⁻¹\nC_p = 62.36 J mol⁻¹ K⁻¹\nγ = 15 / 13 = 1.154 ≈ 1.15",
            "rough_work": "[ROUGH_WORK]\nf_total = 3 + 2 + 8 = 13\nC_v = 13/2 R = 6.5 × 8.314 = 54.041\nC_p = 15/2 R = 7.5 × 8.314 = 62.355\nγ = 15/13 = 1.1538",
            "finalAnswer": "For CO₂ with active vibrational modes: C_v = 54.04 J mol⁻¹ K⁻¹, C_p = 62.36 J mol⁻¹ K⁻¹, γ = 1.15",
            "unit": "J mol⁻¹ K⁻¹",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Section 12.6, Page 254",
            "image_search_query": "equipartition energy vibrational degrees of freedom co2"
        }
    ]

    modules[3]["concept_questions"] = [
        {
            "question": "According to the Law of Equipartition of Energy, what is the average thermal energy associated with each independent quadratic degree of freedom of a molecule in thermal equilibrium at absolute temperature T?",
            "options": [
                "(Recommended) ½ k_B T",
                "k_B T",
                "3/2 k_B T",
                "2 k_B T"
            ],
            "correctAnswer": "(Recommended) ½ k_B T",
            "correct_answer": "(Recommended) ½ k_B T",
            "explanation": "The Law of Equipartition states that the total energy of a dynamical system in thermal equilibrium is distributed equally among its degrees of freedom, each quadratic mode contributing an average energy of ½ k_B T.",
            "hint": "Recall the fundamental factor per quadratic term in the energy expression.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 12.5, Page 253",
            "image_search_query": "law of equipartition of energy half kbt"
        },
        {
            "question": "Why does a vibrational degree of freedom contribute k_B T (i.e., 2 × ½ k_B T) to the molar energy of a molecule, whereas a translational degree of freedom contributes only ½ k_B T?",
            "options": [
                "(Recommended) Because a vibrational mode contains two quadratic energy terms: kinetic energy (½ m v²) and potential energy (½ k x²)",
                "Because vibrational frequency is twice the collision frequency",
                "Because vibration involves two bonded atoms moving simultaneously",
                "Because vibrational modes are strictly quantum mechanical"
            ],
            "correctAnswer": "(Recommended) Because a vibrational mode contains two quadratic energy terms: kinetic energy (½ m v²) and potential energy (½ k x²)",
            "correct_answer": "(Recommended) Because a vibrational mode contains two quadratic energy terms: kinetic energy (½ m v²) and potential energy (½ k x²)",
            "explanation": "A harmonic oscillator possesses both kinetic energy (½ m (dx/dt)²) and potential energy (½ k x²). By equipartition, each quadratic term contributes ½ k_B T, yielding a total of k_B T per vibrational mode.",
            "hint": "Count the number of quadratic coordinates in harmonic oscillation.",
            "blooms_level": "Analyze",
            "textbook_reference": "Section 12.5, Page 253",
            "image_search_query": "vibrational modes kinetic potential energy equipartition"
        },
        {
            "question": "According to the Dulong-Petit Law, what is the molar specific heat capacity of most solid elements at high temperatures?",
            "options": [
                "(Recommended) 3 R (≈ 24.9 J mol⁻¹ K⁻¹)",
                "(3/2) R",
                "(5/2) R",
                "(7/2) R"
            ],
            "correctAnswer": "(Recommended) 3 R (≈ 24.9 J mol⁻¹ K⁻¹)",
            "correct_answer": "(Recommended) 3 R (≈ 24.9 J mol⁻¹ K⁻¹)",
            "explanation": "Atoms in a 3D solid lattice oscillate about fixed positions with 3 vibrational modes, each having 2 quadratic terms. Total energy per atom = 3 × (2 × ½ k_B T) = 3 k_B T. For 1 mole, U = 3 R T => C = dU/dT = 3 R.",
            "hint": "Consider 3 independent vibrational directions in a 3D solid lattice.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 12.6, Page 255",
            "image_search_query": "dulong petit law 3r molar heat capacity solids"
        },
        {
            "question": "Why do vibrational degrees of freedom in diatomic gases like H₂ and N₂ remain 'frozen out' (inactive) at ordinary room temperatures?",
            "options": [
                "(Recommended) The quantum energy spacing ΔE = hν of vibrational levels is much larger than the available thermal energy k_B T at room temperature",
                "Molecules collide too infrequently to stimulate vibrations",
                "Vibrational motion is prohibited by the First Law of Thermodynamics",
                "Diatomic bonds are completely rigid and can never vibrate"
            ],
            "correctAnswer": "(Recommended) The quantum energy spacing ΔE = hν of vibrational levels is much larger than the available thermal energy k_B T at room temperature",
            "correct_answer": "(Recommended) The quantum energy spacing ΔE = hν of vibrational levels is much larger than the available thermal energy k_B T at room temperature",
            "explanation": "Quantum mechanics dictates that a mode can be excited only when thermal collision energy k_B T is comparable to or exceeds the energy quantum ΔE = hν. For N₂ and H₂, hν/k_B is thousands of kelvins, so vibrations are frozen out at 300 K.",
            "hint": "Compare thermal energy k_B T with quantum excitation energy hν.",
            "blooms_level": "Analyze",
            "textbook_reference": "Section 12.6, Page 255",
            "image_search_query": "quantum freeze out vibrational degrees of freedom"
        }
    ]

    # -------------------------------------------------------------
    # Module 75: Mean Free Path & Molecular Collisions
    # -------------------------------------------------------------
    modules[4]["worked_examples"] = [
        {
            "problem": "NCERT Example 12.9: Estimate the mean free path for a water molecule in water vapour at temperature T = 373 K and pressure P = 1.01 × 10⁵ Pa. Assume the molecular diameter d is 2.0 Å (2.0 × 10⁻¹⁰ m). (Take k_B = 1.38 × 10⁻²³ J K⁻¹)",
            "given": "Temperature T = 373 K, Pressure P = 1.01 × 10⁵ Pa, Molecular diameter d = 2.0 Å = 2.0 × 10⁻¹⁰ m, Boltzmann constant k_B = 1.38 × 10⁻²³ J K⁻¹",
            "to_calculate": "Mean free path λ of the water molecule",
            "formula": "Number density: n = P / (k_B · T)\nMean free path accounting for relative molecular motion: λ = 1 / (√2 · n · π · d²)",
            "substitution": "n = (1.01 × 10⁵ Pa) / [ (1.38 × 10⁻²³ J K⁻¹) × (373 K) ]\nλ = 1 / [ √2 × n × 3.1416 × (2.0 × 10⁻¹⁰ m)² ]",
            "calculation": "n = 1.01 × 10⁵ / (5.1474 × 10⁻²¹) = 1.962 × 10²⁵ molecules m⁻³\nCross section σ = π d² = 3.1416 × 4.0 × 10⁻²⁰ = 1.2566 × 10⁻¹⁹ m²\nDenominator = 1.4142 × (1.962 × 10²⁵) × (1.2566 × 10⁻¹⁹) = 3.487 × 10⁶ m⁻¹\nλ = 1 / (3.487 × 10⁶) = 2.868 × 10⁻⁷ m ≈ 2.9 × 10⁻⁷ m (or 290 nm)",
            "rough_work": "[ROUGH_WORK]\nk_B × 373 = 5.1474 × 10⁻²¹\nn = 1.01 × 10⁵ / 5.1474 × 10⁻²¹ = 1.962 × 10²⁵\nsqrt(2) × n × pi × d² = 1.414 × 1.962 × 10²⁵ × 1.257 × 10⁻¹⁹ = 3.486 × 10⁶\nλ = 2.87 × 10⁻⁷ m",
            "finalAnswer": "The mean free path of a water molecule in water vapour at 373 K is approximately 2.9 × 10⁻⁷ m (290 nm)",
            "unit": "m (or nm)",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Example 12.9, Page 255",
            "image_search_query": "mean free path collision cylinder derivation"
        },
        {
            "problem": "Calculate the collision frequency (number of collisions per second, Z) and the mean relaxation time (time between collisions, τ) for nitrogen gas molecules at STP (T = 273 K, P = 1.013 × 10⁵ Pa, molecular diameter d = 3.0 Å = 3.0 × 10⁻¹⁰ m, molar mass M = 28.0 × 10⁻³ kg mol⁻¹).",
            "given": "T = 273 K, P = 1.013 × 10⁵ Pa, d = 3.0 × 10⁻¹⁰ m, M = 28.0 × 10⁻³ kg mol⁻¹, R = 8.314 J mol⁻¹ K⁻¹, k_B = 1.38 × 10⁻²³ J K⁻¹",
            "to_calculate": "(a) Mean free path λ, (b) Average molecular speed v_avg, (c) Collision frequency Z, (d) Relaxation time τ",
            "formula": "n = P / (k_B · T)\nλ = 1 / (√2 · n · π · d²)\nv_avg = √(8 · R · T / (π · M))\nCollision frequency: Z = v_avg / λ\nRelaxation time: τ = 1 / Z = λ / v_avg",
            "substitution": "n = (1.013 × 10⁵) / (1.38 × 10⁻²³ × 273) = 2.689 × 10²⁵ m⁻³\nλ = 1 / [ 1.4142 × 2.689 × 10²⁵ × 3.1416 × (3.0 × 10⁻¹⁰)² ]\nv_avg = √(8 × 8.314 × 273 / (3.1416 × 0.028))",
            "calculation": "λ = 1 / (1.075 × 10⁷) = 9.30 × 10⁻⁸ m\nv_avg = √(18157.8 / 0.08796) = √206432 = 454.3 m s⁻¹\nZ = 454.3 / (9.30 × 10⁻⁸) = 4.885 × 10⁹ s⁻¹ ≈ 4.9 × 10⁹ collisions s⁻¹\nτ = 1 / Z = 2.05 × 10⁻¹⁰ s",
            "rough_work": "[ROUGH_WORK]\nn = 2.69 × 10²⁵\npi × d² = 2.827 × 10⁻¹⁹\nsqrt(2) × n × pi × d² = 1.075 × 10⁷\nλ = 9.3 × 10⁻⁸ m\nv_avg = 454.3 m/s\nZ = 4.9 × 10⁹ s⁻¹\nτ = 2.05 × 10⁻¹⁰ s",
            "finalAnswer": "(a) Mean free path λ = 9.3 × 10⁻⁸ m; (b) Average speed v_avg = 454 m s⁻¹; (c) Collision frequency Z = 4.9 × 10⁹ s⁻¹; (d) Relaxation time τ = 2.05 × 10⁻¹⁰ s",
            "unit": "m, m s⁻¹, s⁻¹, s",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Section 12.7, Page 256",
            "image_search_query": "collision frequency relaxation time mean free path"
        }
    ]

    modules[4]["concept_questions"] = [
        {
            "question": "How does the mean free path λ of an ideal gas depend on the absolute temperature T and pressure P?",
            "options": [
                "(Recommended) λ is directly proportional to temperature and inversely proportional to pressure (λ ∝ T / P)",
                "λ is directly proportional to pressure and inversely proportional to temperature (λ ∝ P / T)",
                "λ is independent of temperature and depends only on P²",
                "λ is proportional to √T and independent of P"
            ],
            "correctAnswer": "(Recommended) λ is directly proportional to temperature and inversely proportional to pressure (λ ∝ T / P)",
            "correct_answer": "(Recommended) λ is directly proportional to temperature and inversely proportional to pressure (λ ∝ T / P)",
            "explanation": "Since number density n = P / (k_B T), substituting into λ = 1 / (√2 n π d²) gives λ = (k_B T) / (√2 π d² P). Hence λ ∝ T / P.",
            "hint": "Express number density n in terms of P and T using the ideal gas law.",
            "blooms_level": "Analyze",
            "textbook_reference": "Section 12.7, Page 256",
            "image_search_query": "mean free path temperature pressure dependence"
        },
        {
            "question": "In the derivation of mean free path, why does the factor of √2 appear in the denominator of λ = 1 / (√2 n π d²)?",
            "options": [
                "(Recommended) To account for the relative motion of target gas molecules, where average relative speed between colliding molecules is v_rel = √2 · v",
                "Because collisions occur in two-dimensional planes",
                "From the root mean square velocity formula",
                "Due to the spherical curvature of the colliding molecules"
            ],
            "correctAnswer": "(Recommended) To account for the relative motion of target gas molecules, where average relative speed between colliding molecules is v_rel = √2 · v",
            "correct_answer": "(Recommended) To account for the relative motion of target gas molecules, where average relative speed between colliding molecules is v_rel = √2 · v",
            "explanation": "If other molecules were stationary, λ = 1 / (n π d²). Because all molecules are in incessant random thermal motion, the average relative speed v_rel = √2 · v, sweeping out volume √2 times faster and reducing λ by 1/√2.",
            "hint": "Consider that target molecules are not stationary targets.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 12.7, Page 255",
            "image_search_query": "mean free path relative velocity root 2"
        },
        {
            "question": "If the diameter of a gas molecule is doubled (d' = 2d) while keeping density and temperature constant, how does the mean free path λ change?",
            "options": [
                "(Recommended) It becomes 1/4th of its original value (λ' = λ / 4)",
                "It is halved (λ' = λ / 2)",
                "It doubles (λ' = 2λ)",
                "It remains unchanged"
            ],
            "correctAnswer": "(Recommended) It becomes 1/4th of its original value (λ' = λ / 4)",
            "correct_answer": "(Recommended) It becomes 1/4th of its original value (λ' = λ / 4)",
            "explanation": "Mean free path is inversely proportional to the collision cross section σ = π d², so λ ∝ 1 / d². Doubling diameter increases collision area by a factor of 4, reducing mean free path to 1/4th.",
            "hint": "Look at the power of d in the denominator of λ.",
            "blooms_level": "Apply",
            "textbook_reference": "Section 12.7, Page 255",
            "image_search_query": "mean free path molecular diameter dependence"
        },
        {
            "question": "What macroscopic transport phenomenon is directly explained by molecular collisions and the finite mean free path of gas molecules?",
            "options": [
                "(Recommended) Viscosity, thermal conduction, and molecular diffusion in gases",
                "Gravitational acceleration of heavy gas masses",
                "Electromagnetic radiation of blackbodies",
                "Nuclear fusion of atmospheric atoms"
            ],
            "correctAnswer": "(Recommended) Viscosity, thermal conduction, and molecular diffusion in gases",
            "correct_answer": "(Recommended) Viscosity, thermal conduction, and molecular diffusion in gases",
            "explanation": "Transport phenomena arise from molecules carrying physical properties across mean free path distances: momentum transport gives viscosity (η), thermal energy transport gives thermal conductivity (K), and mass transport gives diffusion (D).",
            "hint": "Identify phenomena where momentum, heat, or particles diffuse across layers.",
            "blooms_level": "Understand",
            "textbook_reference": "Section 12.7, Page 256",
            "image_search_query": "transport phenomena viscosity thermal conduction diffusion"
        }
    ]

    # -------------------------------------------------------------
    # Module 76: Comprehensive NCERT Exercises 12.1 to 12.14 Solver
    # -------------------------------------------------------------
    modules[5]["worked_examples"] = [
        {
            "problem": "NCERT Exercise 12.1: Estimate the fraction of molecular volume to the actual volume occupied by oxygen gas at STP. Take the diameter of an oxygen molecule to be 3.0 Å.",
            "given": "Gas: Oxygen (O₂), Molecular diameter d = 3.0 Å = 3.0 × 10⁻¹⁰ m => radius r = 1.5 × 10⁻¹⁰ m, STP condition: 1 mole occupies V_molar = 22.4 L = 22.4 × 10⁻³ m³, Avogadro number N_A = 6.022 × 10²³ mol⁻¹",
            "to_calculate": "Fraction of molecular volume to actual molar volume (V_molecules / V_molar)",
            "formula": "Volume of one spherical molecule: V_single = (4/3) · π · r³\nTotal molecular volume in 1 mole: V_molecules = N_A · V_single = N_A · (4/3) · π · r³\nFraction = V_molecules / V_molar",
            "substitution": "V_single = (4/3) × 3.1416 × (1.5 × 10⁻¹⁰ m)³ = (4/3) × 3.1416 × 3.375 × 10⁻³⁰ m³ = 1.4137 × 10⁻²⁹ m³\nV_molecules = 6.022 × 10²³ × 1.4137 × 10⁻²⁹ m³ = 8.513 × 10⁻⁶ m³\nFraction = (8.513 × 10⁻⁶ m³) / (22.4 × 10⁻³ m³)",
            "calculation": "Fraction = 8.513 × 10⁻⁶ / (2.24 × 10⁻²) = 3.80 × 10⁻⁴ ≈ 4.0 × 10⁻⁴",
            "rough_work": "[ROUGH_WORK]\n4/3 × pi × 1.5³ = 14.137 × 10⁻³⁰ m³ = 1.414 × 10⁻²⁹ m³\n6.022 × 1.414 = 8.515 × 10⁻⁶ m³\n8.515 × 10⁻⁶ / 0.0224 = 3.80 × 10⁻⁴",
            "finalAnswer": "Fraction of molecular volume to actual volume occupied is 3.8 × 10⁻⁴ (approximately 4 × 10⁻⁴)",
            "unit": "Dimensionless ratio",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Exercise 12.1, Page 257",
            "image_search_query": "molecular volume actual volume oxygen gas stp"
        },
        {
            "problem": "NCERT Exercise 12.2: Molar volume is the volume occupied by 1 mol of any (ideal) gas at standard temperature and pressure (STP: 1 atmospheric pressure = 1.013 × 10⁵ Pa, 0 °C = 273.15 K). Show that it is 22.4 litres.",
            "given": "Number of moles μ = 1.0 mol, Standard pressure P = 1.013 × 10⁵ Pa, Standard temperature T = 273.15 K, Universal gas constant R = 8.314 J mol⁻¹ K⁻¹",
            "to_calculate": "Molar volume V_molar in m³ and litres",
            "formula": "Ideal gas equation: P · V = μ · R · T => V = (μ · R · T) / P",
            "substitution": "V = (1.0 mol × 8.314 J mol⁻¹ K⁻¹ × 273.15 K) / (1.013 × 10⁵ Pa)",
            "calculation": "Numerator = 8.314 × 273.15 = 2271.07 J\nV = 2271.07 / (1.013 × 10⁵) = 0.022419 m³\nConverting to litres (1 m³ = 1000 L):\nV = 0.022419 × 1000 L = 22.42 L ≈ 22.4 L",
            "rough_work": "[ROUGH_WORK]\n8.314 × 273.15 = 2271.07\n2271.07 / 101300 = 0.022419 m³ = 22.42 L.",
            "finalAnswer": "Molar volume V_molar = 22.4 litres (Hence Proved)",
            "unit": "L (or m³)",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Exercise 12.2, Page 257",
            "image_search_query": "molar volume ideal gas stp 22.4 litres derivation"
        },
        {
            "problem": "NCERT Exercise 12.3: Figure 12.8 shows plot of PV/T versus P for 1.00 × 10⁻³ kg of oxygen gas at two different temperatures T₁ and T₂.\n(a) What does the dotted horizontal plot signify?\n(b) Which is true: T₁ > T₂ or T₁ < T₂?\n(c) What is the value of PV/T where the curves meet on the y-axis?\n(d) If we obtained similar plots for 1.00 × 10⁻³ kg of hydrogen, would we get the same value of PV/T at the y-axis? If not, what mass of hydrogen yields the same value? (M_H₂ = 2.02 u, M_O₂ = 32.0 u, R = 8.31 J mol⁻¹ K⁻¹)",
            "given": "Mass of oxygen gas m = 1.00 × 10⁻³ kg = 1.00 g, M_O₂ = 32.0 g mol⁻¹ = 32.0 × 10⁻³ kg mol⁻¹, M_H₂ = 2.02 g mol⁻¹, R = 8.31 J mol⁻¹ K⁻¹, Figure 12.8 shows curves for T₁ and T₂ approaching y-axis",
            "to_calculate": "(a) Significance of dotted line, (b) Comparison of T₁ and T₂, (c) Intercept value on y-axis, (d) Mass of H₂ for equal intercept",
            "formula": "(a) For ideal gas, PV = μRT => PV/T = μR = constant (horizontal line).\n(b) Real gases approach ideal gas behavior as temperature increases. The curve closer to the ideal dotted line corresponds to higher temperature.\n(c) As P → 0, real gas becomes ideal: (PV/T)_0 = μ · R = (m / M_O₂) · R.\n(d) For H₂ to have the same intercept: μ_H₂ = μ_O₂ => m_H₂ / M_H₂ = m_O₂ / M_O₂ => m_H₂ = m_O₂ · (M_H₂ / M_O₂).",
            "substitution": "(c) (PV/T)_0 = (1.00 × 10⁻³ kg / 32.0 × 10⁻³ kg mol⁻¹) × 8.31 J mol⁻¹ K⁻¹ = (1 / 32) × 8.31 J K⁻¹\n(d) m_H₂ = (1.00 × 10⁻³ kg) × (2.02 / 32.0)",
            "calculation": "(a) The dotted plot represents the behavior of an ideal gas, for which PV/T = μR is strictly independent of pressure P.\n(b) The curve for T₁ is flatter and closer to the ideal gas line than T₂. Real gases approach ideal behavior at higher temperatures. Hence, T₁ > T₂.\n(c) Value on y-axis = 8.31 / 32 = 0.2597 J K⁻¹ ≈ 0.26 J K⁻¹\n(d) No, because M_H₂ ≠ M_O₂. Mass of hydrogen required: m_H₂ = 1.00 × (2.02 / 32.0) = 0.0631 × 10⁻³ kg = 0.0631 g = 6.31 × 10⁻⁵ kg.",
            "rough_work": "[ROUGH_WORK]\n8.31 / 32 = 0.25968 J/K\n1.0 × 2.02 / 32 = 0.063125 g = 6.31 × 10⁻⁵ kg.",
            "finalAnswer": "(a) Dotted plot signifies ideal gas behavior; (b) T₁ > T₂; (c) Intercept = 0.26 J K⁻¹; (d) No; Required mass of hydrogen = 6.31 × 10⁻⁵ kg (0.063 g)",
            "unit": "J K⁻¹, kg",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Exercise 12.3, Pages 257-258",
            "figure_reference": "Fig. 12.8",
            "image_search_query": "pv over t versus p graph real gas ideal gas"
        },
        {
            "problem": "NCERT Exercise 12.4: An oxygen cylinder of volume 30 litre has an initial gauge pressure of 15 atm and a temperature of 27 °C. After some oxygen is withdrawn from the cylinder, the gauge pressure drops to 11 atm and its temperature drops to 17 °C. Estimate the mass of oxygen taken out of the cylinder. (Take R = 8.31 J mol⁻¹ K⁻¹, molecular mass of O₂ = 32 u, 1 atm = 1.013 × 10⁵ Pa)",
            "given": "Volume V = 30 L = 30 × 10⁻³ m³ = 0.030 m³, Atmospheric pressure P_atm = 1.0 atm\nInitial State:\nGauge pressure P_g1 = 15 atm => Absolute pressure P₁ = 15 + 1 = 16 atm = 16 × 1.013 × 10⁵ Pa = 1.621 × 10⁶ Pa\nTemperature T₁ = 27 °C = (27 + 273.15) K = 300.15 K ≈ 300 K\nFinal State:\nGauge pressure P_g2 = 11 atm => Absolute pressure P₂ = 11 + 1 = 12 atm = 12 × 1.013 × 10⁵ Pa = 1.216 × 10⁶ Pa\nTemperature T₂ = 17 °C = (17 + 273.15) K = 290.15 K ≈ 290 K\nMolar mass M = 32 × 10⁻³ kg mol⁻¹, R = 8.31 J mol⁻¹ K⁻¹",
            "to_calculate": "Mass of oxygen withdrawn Δm = m₁ - m₂",
            "formula": "Ideal gas law: P · V = (m / M) · R · T => m = (P · V · M) / (R · T)\nMass withdrawn: Δm = (V · M / R) · [ (P₁ / T₁) - (P₂ / T₂) ]",
            "substitution": "Initial mass m₁ = (1.621 × 10⁶ × 0.030 × 32 × 10⁻³) / (8.31 × 300)\nFinal mass m₂ = (1.216 × 10⁶ × 0.030 × 32 × 10⁻³) / (8.31 × 290)",
            "calculation": "m₁ = (1.556 × 10³ × 10⁻³) / (2493) = 1.556 / 2.493 = 0.6241 kg\nm₂ = (1.167 × 10³ × 10⁻³) / (2409.9) = 1.167 / 2.410 = 0.4842 kg\nΔm = m₁ - m₂ = 0.6241 kg - 0.4842 kg = 0.1399 kg ≈ 0.14 kg = 140 g",
            "rough_work": "[ROUGH_WORK]\nm₁ = 16 × 101300 × 0.030 × 0.032 / (8.31 × 300) = 1555.97 / 2493 = 0.6241 kg\nm₂ = 12 × 101300 × 0.030 × 0.032 / (8.31 × 290) = 1166.98 / 2409.9 = 0.4842 kg\nΔm = 0.6241 - 0.4842 = 0.1399 kg ≈ 140 g",
            "finalAnswer": "Mass of oxygen taken out of the cylinder Δm = 0.14 kg (or 140 g)",
            "unit": "kg (or g)",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Exercise 12.4, Page 258",
            "image_search_query": "oxygen cylinder gauge pressure mass withdrawn calculation"
        },
        {
            "problem": "NCERT Exercise 12.5: An air bubble of volume 1.0 cm³ rises from the bottom of a lake 40 m deep at a temperature of 12 °C. To what volume does it grow when it reaches the surface, which is at a temperature of 35 °C ? (Take g = 9.8 m s⁻², density of lake water ρ = 1000 kg m⁻³, atmospheric pressure P_0 = 1.01 × 10⁵ Pa)",
            "given": "Initial State (Bottom of lake, depth h = 40 m):\nVolume V₁ = 1.0 cm³ = 1.0 × 10⁻⁶ m³\nTemperature T₁ = 12 °C = (12 + 273.15) K = 285.15 K\nPressure P₁ = P_0 + ρ · g · h = 1.01 × 10⁵ + (1000 × 9.8 × 40) = 1.01 × 10⁵ + 3.92 × 10⁵ = 4.93 × 10⁵ Pa\nFinal State (Surface of lake, h = 0):\nPressure P₂ = P_0 = 1.01 × 10⁵ Pa\nTemperature T₂ = 35 °C = (35 + 273.15) K = 308.15 K",
            "to_calculate": "Final volume V₂ of the air bubble at the surface",
            "formula": "Combined gas law: (P₁ · V₁) / T₁ = (P₂ · V₂) / T₂ => V₂ = V₁ · (P₁ / P₂) · (T₂ / T₁)",
            "substitution": "V₂ = (1.0 cm³) × (4.93 × 10⁵ Pa / 1.01 × 10⁵ Pa) × (308.15 K / 285.15 K)",
            "calculation": "Pressure ratio P₁ / P₂ = 4.93 / 1.01 = 4.8812\nTemperature ratio T₂ / T₁ = 308.15 / 285.15 = 1.08066\nV₂ = 1.0 × 4.8812 × 1.08066 = 5.275 cm³ ≈ 5.3 cm³",
            "rough_work": "[ROUGH_WORK]\nP₁ = 101000 + 392000 = 493000 Pa\nP₁/P₂ = 493/101 = 4.881\nT₂/T₁ = 308.15 / 285.15 = 1.0807\nV₂ = 4.881 × 1.0807 = 5.275 cm³",
            "finalAnswer": "The volume of the bubble grows to 5.3 cm³ at the surface",
            "unit": "cm³",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Exercise 12.5, Page 258",
            "image_search_query": "air bubble rising lake expansion combined gas law"
        },
        {
            "problem": "NCERT Exercise 12.6: Estimate the total number of air molecules (inclusive of oxygen, nitrogen, water vapour and other constituents) in a room of capacity 25.0 m³ at a temperature of 27 °C and 1.0 atm pressure.",
            "given": "Room capacity V = 25.0 m³, Temperature T = 27 °C = (27 + 273.15) K = 300.15 K ≈ 300 K, Pressure P = 1.0 atm = 1.013 × 10⁵ Pa, Boltzmann constant k_B = 1.38 × 10⁻²³ J K⁻¹",
            "to_calculate": "Total number of air molecules N",
            "formula": "Ideal gas equation in molecular form: P · V = N · k_B · T => N = (P · V) / (k_B · T)",
            "substitution": "N = [ (1.013 × 10⁵ Pa) × (25.0 m³) ] / [ (1.38 × 10⁻²³ J K⁻¹) × (300 K) ]",
            "calculation": "Numerator = 1.013 × 10⁵ × 25.0 = 2.5325 × 10⁶ J\nDenominator = 1.38 × 10⁻²³ × 300 = 4.14 × 10⁻²¹ J\nN = (2.5325 × 10⁶) / (4.14 × 10⁻²¹) = 0.6117 × 10²⁷ = 6.12 × 10²⁶ molecules",
            "rough_work": "[ROUGH_WORK]\n25 × 101300 = 2,532,500\n1.38 × 300 = 414\n2532500 / (4.14 × 10⁻²¹) = 6.117 × 10²⁶",
            "finalAnswer": "Total number of air molecules in the room N = 6.1 × 10²⁶ molecules",
            "unit": "Molecules",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Exercise 12.6, Page 258",
            "image_search_query": "number of air molecules in room calculation boltzmann"
        },
        {
            "problem": "NCERT Exercise 12.7: Estimate the average thermal energy of a helium atom at (i) room temperature (27 °C), (ii) the temperature on the surface of the Sun (6000 K), and (iii) the temperature of 10 million kelvin (the typical core temperature in the case of a star).",
            "given": "Helium is monatomic => 3 translational degrees of freedom\nBoltzmann constant k_B = 1.38 × 10⁻²³ J K⁻¹\nTemperatures: (i) T₁ = 27 °C = 300 K, (ii) T₂ = 6000 K, (iii) T₃ = 10 × 10⁶ K = 1.0 × 10⁷ K",
            "to_calculate": "Average thermal kinetic energy E_avg = (3/2) k_B T for cases (i), (ii), and (iii)",
            "formula": "Average translational kinetic energy: E = (3/2) · k_B · T",
            "substitution": "(i) E₁ = 1.5 × (1.38 × 10⁻²³ J K⁻¹) × (300 K)\n(ii) E₂ = 1.5 × (1.38 × 10⁻²³ J K⁻¹) × (6000 K)\n(iii) E₃ = 1.5 × (1.38 × 10⁻²³ J K⁻¹) × (1.0 × 10⁷ K)",
            "calculation": "(i) E₁ = 2.07 × 10⁻²³ × 300 = 6.21 × 10⁻²¹ J (or ≈ 0.039 eV)\n(ii) E₂ = 2.07 × 10⁻²³ × 6000 = 1.242 × 10⁻¹⁹ J (or ≈ 0.78 eV)\n(iii) E₃ = 2.07 × 10⁻²³ × 1.0 × 10⁷ = 2.07 × 10⁻¹⁶ J (or ≈ 1.29 keV)",
            "rough_work": "[ROUGH_WORK]\n1.5 × 1.38 = 2.07\n2.07 × 300 = 621 × 10⁻²³ = 6.21 × 10⁻²¹ J\n2.07 × 6000 = 1.242 × 10⁻¹⁹ J\n2.07 × 10⁷ = 2.07 × 10⁻¹⁶ J",
            "finalAnswer": "(i) Room temperature (300 K): E = 6.21 × 10⁻²¹ J; (ii) Solar surface (6000 K): E = 1.24 × 10⁻¹⁹ J; (iii) Stellar core (10⁷ K): E = 2.07 × 10⁻¹⁶ J",
            "unit": "J",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Exercise 12.7, Page 258",
            "image_search_query": "average thermal energy helium atom temperature sun core"
        },
        {
            "problem": "NCERT Exercise 12.8: Three vessels of equal capacity have gases at the same temperature and pressure. The first vessel contains neon (monatomic), the second contains chlorine (diatomic), and the third contains uranium hexafluoride (polyatomic). Do the vessels contain equal number of respective molecules ? Is the root mean square speed of molecules the same in the three cases? If not, in which case is v_rms the largest?",
            "given": "Equal volume V, equal pressure P, and equal temperature T for all three vessels.\nGases: Neon (Ne, M = 20.2 u), Chlorine (Cl₂, M = 70.9 u), Uranium Hexafluoride (UF₆, M = 352 u)",
            "to_calculate": "(a) Comparison of number of molecules N, (b) Comparison of v_rms, and identification of largest v_rms",
            "formula": "(a) Avogadro's Law / Ideal Gas Equation: N = (P · V) / (k_B · T)\n(b) Root mean square speed: v_rms = √(3 · k_B · T / m) = √(3 · R · T / M)",
            "substitution": "N_Ne = N_Cl₂ = N_UF₆ = P · V / (k_B · T)\nv_rms ∝ 1 / √M",
            "calculation": "(a) Yes. Since P, V, and T are identical for all three vessels, by Avogadro's hypothesis, each vessel contains the exact same number of molecules N.\n(b) No. The root mean square speed depends inversely on the square root of molar mass (v_rms ∝ 1 / √M). Since M_Ne (20.2 u) < M_Cl₂ (70.9 u) < M_UF₆ (352 u), the rms speeds are different.\nv_rms is the largest for Neon, because it has the smallest molecular mass.",
            "rough_work": "[ROUGH_WORK]\nN = PV/kT => same for all.\nv_rms = sqrt(3RT/M) => smaller M gives larger v_rms.\nM_Ne = 20.2, M_Cl₂ = 71, M_UF₆ = 352\n=> v_rms(Ne) > v_rms(Cl₂) > v_rms(UF₆).",
            "finalAnswer": "(a) Yes, all three vessels contain the identical number of molecules; (b) No, v_rms differs across gases; v_rms is the largest for Neon (the lightest gas)",
            "unit": "Qualitative Comparison",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Exercise 12.8, Page 258",
            "image_search_query": "avogadro hypothesis equal molecules rms speed molar mass"
        },
        {
            "problem": "NCERT Exercise 12.9: At what temperature is the root mean square speed of an atom in an argon gas cylinder equal to the rms speed of a helium gas atom at -20 °C ? (Atomic mass of Ar = 39.9 u, Atomic mass of He = 4.0 u)",
            "given": "Gas 1: Helium (He), M₁ = 4.0 u, Temperature T₁ = -20 °C = (-20 + 273.15) K = 253.15 K\nGas 2: Argon (Ar), M₂ = 39.9 u, Temperature T₂\nCondition: v_rms(Ar) = v_rms(He)",
            "to_calculate": "Temperature of Argon T₂ in kelvins and degrees Celsius",
            "formula": "v_rms = √(3 · R · T / M)\nEquating speeds: √(3 · R · T₂ / M_Ar) = √(3 · R · T₁ / M_He) => T₂ / M_Ar = T₁ / M_He => T₂ = T₁ · (M_Ar / M_He)",
            "substitution": "T₂ = 253.15 K × (39.9 u / 4.0 u)",
            "calculation": "39.9 / 4.0 = 9.975\nT₂ = 253.15 × 9.975 = 2525.17 K ≈ 2.52 × 10³ K\nIn Celsius: t₂ = 2525.17 - 273.15 = 2252 °C",
            "rough_work": "[ROUGH_WORK]\n253.15 × 9.975 = 2525.17 K\n2525.17 - 273.15 = 2252.02 °C",
            "finalAnswer": "Temperature of argon must be 2525 K (or 2252 °C)",
            "unit": "K (or °C)",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Exercise 12.9, Page 258",
            "image_search_query": "argon helium rms speed temperature ratio calculation"
        },
        {
            "problem": "NCERT Exercise 12.10: Estimate the mean free path and collision frequency of a nitrogen molecule in a cylinder containing nitrogen at 2.0 atm and temperature 17 °C. Take the radius of a nitrogen molecule to be roughly 1.0 Å. Compare the collision time with the time the molecule moves freely between two successive collisions. (Molecular mass of N₂ = 28.0 u, k_B = 1.38 × 10⁻²³ J K⁻¹, R = 8.31 J mol⁻¹ K⁻¹)",
            "given": "Pressure P = 2.0 atm = 2.0 × 1.013 × 10⁵ Pa = 2.026 × 10⁵ Pa, Temperature T = 17 °C = (17 + 273.15) K = 290.15 K, Molecular radius r = 1.0 Å => diameter d = 2.0 Å = 2.0 × 10⁻¹⁰ m, Molar mass M = 28.0 × 10⁻³ kg mol⁻¹",
            "to_calculate": "(a) Mean free path λ, (b) Collision frequency Z, (c) Collision time τ_c and free transit time τ, and their ratio",
            "formula": "Number density: n = P / (k_B · T)\nMean free path: λ = 1 / (√2 · n · π · d²)\nAverage speed: v_avg = √(8 · R · T / (π · M))\nCollision frequency: Z = v_avg / λ\nFree transit time: τ = λ / v_avg = 1 / Z\nCollision duration: τ_c = d / v_avg",
            "substitution": "n = (2.026 × 10⁵ Pa) / [ (1.38 × 10⁻²³ J K⁻¹) × (290.15 K) ]\nλ = 1 / [ 1.4142 × n × 3.1416 × (2.0 × 10⁻¹⁰ m)² ]\nv_avg = √(8 × 8.31 × 290.15 / (3.1416 × 0.028))",
            "calculation": "n = 2.026 × 10⁵ / (4.004 × 10⁻²¹) = 5.060 × 10²⁵ m⁻³\nDenominator = 1.4142 × 5.060 × 10²⁵ × 3.1416 × 4.0 × 10⁻²⁰ = 8.992 × 10⁶ m⁻¹\nλ = 1 / (8.992 × 10⁶) = 1.112 × 10⁻⁷ m ≈ 1.11 × 10⁻⁷ m = 111 nm\nv_avg = √(19288 / 0.08796) = √219275 = 468.3 m s⁻¹\nZ = 468.3 / (1.112 × 10⁻⁷) = 4.21 × 10⁹ s⁻¹ (collisions per second)\nFree time τ = 1 / Z = 2.37 × 10⁻¹⁰ s\nCollision duration τ_c = d / v_avg = (2.0 × 10⁻¹⁰ m) / (468.3 m s⁻¹) = 4.27 × 10⁻¹³ s\nRatio τ_c / τ = (4.27 × 10⁻¹³) / (2.37 × 10⁻¹⁰) = 1.8 × 10⁻⁴ ≈ 1 / 555",
            "rough_work": "[ROUGH_WORK]\nn = 5.06 × 10²⁵\nλ = 1.11 × 10⁻⁷ m\nv_avg = 468 m/s\nZ = 4.2 × 10⁹ /s\nτ = 2.37 × 10⁻¹⁰ s\nτ_c = 4.27 × 10⁻¹³ s\nτ_c is over 500 times smaller than free time.",
            "finalAnswer": "(a) Mean free path λ = 1.11 × 10⁻⁷ m (111 nm); (b) Collision frequency Z = 4.21 × 10⁹ s⁻¹; (c) Collision time τ_c ≈ 4.3 × 10⁻¹³ s is roughly 550 times shorter than free time between collisions τ = 2.4 × 10⁻¹⁰ s",
            "unit": "m, s⁻¹, s, Dimensionless ratio",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Exercise 12.10, Page 258",
            "image_search_query": "mean free path collision frequency nitrogen molecule cylinder"
        },
        {
            "problem": "NCERT Exercise 12.11: A gas mixture consists of 8.0 g of oxygen (O₂) and 14.0 g of nitrogen (N₂) at temperature T = 27 °C in a closed vessel. Calculate (a) the total internal energy of the mixture, and (b) the effective ratio of specific heats γ_mix = C_p,mix / C_v,mix. (Given M_O₂ = 32 g mol⁻¹, M_N₂ = 28 g mol⁻¹, R = 8.314 J mol⁻¹ K⁻¹)",
            "given": "Oxygen: m₁ = 8.0 g, M₁ = 32 g mol⁻¹ => μ₁ = 8/32 = 0.25 mol\nNitrogen: m₂ = 14.0 g, M₂ = 28 g mol⁻¹ => μ₂ = 14/28 = 0.50 mol\nBoth gases are diatomic (f = 5 degrees of freedom at 27 °C)\nTemperature T = 27 °C = 300.15 K ≈ 300 K, R = 8.314 J mol⁻¹ K⁻¹",
            "to_calculate": "(a) Total internal energy U_total, (b) Effective ratio γ_mix",
            "formula": "(a) Internal energy of diatomic gas: U = μ · (5/2 R) · T\nU_total = (μ₁ + μ₂) · (5/2 R) · T\n(b) Since both gases are diatomic with identical degrees of freedom f = 5:\nC_v,mix = (5/2) R and C_p,mix = (7/2) R => γ_mix = C_p / C_v = 7/5 = 1.40",
            "substitution": "Total moles μ_total = 0.25 + 0.50 = 0.75 mol\nU_total = 0.75 mol × (2.5 × 8.314 J mol⁻¹ K⁻¹) × (300 K)",
            "calculation": "U_total = 0.75 × 20.785 × 300 = 0.75 × 6235.5 = 4676.6 J ≈ 4.68 kJ\nγ_mix = 1.40",
            "rough_work": "[ROUGH_WORK]\n0.75 × 2.5 × 8.314 × 300 = 4676.625 J\nγ = 7/5 = 1.40.",
            "finalAnswer": "(a) Total internal energy U_total = 4.68 kJ; (b) Effective ratio γ_mix = 1.40",
            "unit": "kJ, Dimensionless ratio",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Additional Exercise 12.11",
            "image_search_query": "gas mixture internal energy specific heat ratio"
        },
        {
            "problem": "NCERT Exercise 12.12: One mole of an ideal monatomic gas (γ₁ = 5/3) is mixed with one mole of an ideal diatomic gas (γ₂ = 7/5). Calculate the equivalent molar heat capacities C_v,mix, C_p,mix and the equivalent adiabatic index γ_mix of the mixture.",
            "given": "μ₁ = 1.0 mol monatomic gas (f₁ = 3): C_v1 = (3/2) R, C_p1 = (5/2) R\nμ₂ = 1.0 mol diatomic gas (f₂ = 5): C_v2 = (5/2) R, C_p2 = (7/2) R\nR = 8.314 J mol⁻¹ K⁻¹",
            "to_calculate": "C_v,mix, C_p,mix, and γ_mix",
            "formula": "C_v,mix = (μ₁ · C_v1 + μ₂ · C_v2) / (μ₁ + μ₂)\nC_p,mix = C_v,mix + R\nγ_mix = C_p,mix / C_v,mix",
            "substitution": "C_v,mix = [ 1 × (1.5 R) + 1 × (2.5 R) ] / (1 + 1) = 4.0 R / 2 = 2.0 R\nC_p,mix = 2.0 R + R = 3.0 R\nγ_mix = 3.0 R / 2.0 R = 1.50",
            "calculation": "C_v,mix = 2.0 × 8.314 J mol⁻¹ K⁻¹ = 16.63 J mol⁻¹ K⁻¹\nC_p,mix = 3.0 × 8.314 J mol⁻¹ K⁻¹ = 24.94 J mol⁻¹ K⁻¹\nγ_mix = 3/2 = 1.50",
            "rough_work": "[ROUGH_WORK]\n(1.5 + 2.5)/2 = 2 R\nC_p = 3 R\nγ = 3/2 = 1.5",
            "finalAnswer": "Equivalent values: C_v,mix = 2.0 R = 16.63 J mol⁻¹ K⁻¹; C_p,mix = 3.0 R = 24.94 J mol⁻¹ K⁻¹; γ_mix = 1.50",
            "unit": "J mol⁻¹ K⁻¹, Dimensionless ratio",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Additional Exercise 12.12",
            "image_search_query": "molar heat capacity gas mixture monatomic diatomic"
        },
        {
            "problem": "NCERT Exercise 12.13: State Maxwell's speed distribution law for an ideal gas, and write down the expressions for the most probable speed (v_mp), the average speed (v_avg), and the root mean square speed (v_rms). Show that their numerical ratio is 1 : 1.128 : 1.224.",
            "given": "Maxwell-Boltzmann speed distribution function: P(v) dv = 4π (m / (2π k_B T))^(3/2) · v² · exp(-m v² / (2 k_B T)) dv",
            "to_calculate": "Derivation of formulas and verification of numerical ratio v_mp : v_avg : v_rms",
            "formula": "1. Most probable speed (maximizing P(v)): dP/dv = 0 => v_mp = √(2 · R · T / M)\n2. Average speed: v_avg = ∫ v P(v) dv = √(8 · R · T / (π · M))\n3. Root-mean-square speed: v_rms = √(∫ v² P(v) dv) = √(3 · R · T / M)\nRatio = √2 : √(8/π) : √3",
            "substitution": "Divide each term by √2:\nTerm 1 = 1.000\nTerm 2 = √(4/π) = 2 / √3.14159 = 2 / 1.77245 = 1.1284\nTerm 3 = √(3/2) = √1.5 = 1.2247",
            "calculation": "Ratio = 1.000 : 1.128 : 1.225 (verified)",
            "rough_work": "[ROUGH_WORK]\nsqrt(2) = 1.4142\nsqrt(8/pi) = 1.5958\nsqrt(3) = 1.7321\nRatio / 1.4142: 1 : 1.1284 : 1.2247",
            "finalAnswer": "Ratio v_mp : v_avg : v_rms = 1 : 1.128 : 1.224 (Hence Proved)",
            "unit": "Dimensionless ratio",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Additional Exercise 12.13",
            "image_search_query": "maxwell speed distribution ratio most probable average rms"
        },
        {
            "problem": "NCERT Exercise 12.14: State Graham's Law of Diffusion. Two flasks of equal volume containing hydrogen (H₂, M₁ = 2.0 g mol⁻¹) and oxygen (O₂, M₂ = 32.0 g mol⁻¹) at the same temperature and pressure are allowed to effuse through identical porous pinholes. Find the ratio of their rates of diffusion (r_H₂ / r_O₂).",
            "given": "Molar mass of hydrogen M₁ = 2.0 g mol⁻¹, Molar mass of oxygen M₂ = 32.0 g mol⁻¹, Same temperature T and pressure P, Identical pinhole orifice area A",
            "to_calculate": "Ratio of diffusion rates r₁ / r₂",
            "formula": "Rate of effusion/diffusion r is proportional to average molecular speed: r ∝ v_avg ∝ 1 / √M.\nGraham's Law: r₁ / r₂ = √(M₂ / M₁)",
            "substitution": "r_H₂ / r_O₂ = √(32.0 / 2.0) = √16.0",
            "calculation": "r_H₂ / r_O₂ = 4.0",
            "rough_work": "[ROUGH_WORK]\nsqrt(32 / 2) = sqrt(16) = 4.",
            "finalAnswer": "Ratio of rates of diffusion r_H₂ : r_O₂ = 4 : 1 (Hydrogen diffuses 4 times faster than oxygen)",
            "unit": "Dimensionless ratio",
            "textbook_reference": "NCERT Class 11 Physics Part 2, Chapter 12, Additional Exercise 12.14",
            "image_search_query": "graham law diffusion effusion pinhole gas rates"
        }
    ]

    modules[5]["concept_questions"] = [
        {
            "question": "In NCERT Exercise 12.4, why must absolute pressures (16 atm and 12 atm) be used in the ideal gas law calculation rather than the raw gauge pressures (15 atm and 11 atm)?",
            "options": [
                "(Recommended) Because the equation of state PV = μRT relates the total absolute mechanical pressure exerted by the gas molecules to volume and temperature",
                "Because gauge pressure ignores the temperature of the gas",
                "Because atmospheric pressure cancels out only at 0 °C",
                "Because gauge pressure applies strictly to liquids"
            ],
            "correctAnswer": "(Recommended) Because the equation of state PV = μRT relates the total absolute mechanical pressure exerted by the gas molecules to volume and temperature",
            "correct_answer": "(Recommended) Because the equation of state PV = μRT relates the total absolute mechanical pressure exerted by the gas molecules to volume and temperature",
            "explanation": "Gauge pressure measures the pressure difference relative to local atmospheric pressure (P_gauge = P_abs - P_atm). The fundamental equation of state requires the total absolute collision momentum transferred per unit area, P_abs = P_gauge + P_atm.",
            "hint": "Recall the definition of absolute pressure vs gauge pressure.",
            "blooms_level": "Understand",
            "textbook_reference": "Exercise 12.4, Page 258",
            "image_search_query": "absolute pressure versus gauge pressure ideal gas"
        },
        {
            "question": "In NCERT Exercise 12.5, as an air bubble rises 40 m from the bottom of a lake to the surface, its volume increases by a factor of 5.3. What is the dominant physical cause of this volume expansion?",
            "options": [
                "(Recommended) The dramatic reduction in hydrostatic pressure (from 4.93 atm at the bottom to 1.0 atm at the surface)",
                "The thermal expansion caused by the temperature rise from 12 °C to 35 °C",
                "Air dissolving from the lake water into the bubble",
                "Water molecules converting into water vapour inside the bubble"
            ],
            "correctAnswer": "(Recommended) The dramatic reduction in hydrostatic pressure (from 4.93 atm at the bottom to 1.0 atm at the surface)",
            "correct_answer": "(Recommended) The dramatic reduction in hydrostatic pressure (from 4.93 atm at the bottom to 1.0 atm at the surface)",
            "explanation": "The pressure factor P₁/P₂ is 4.88, which accounts for over 92% of the expansion. The temperature factor T₂/T₁ = 308/285 is only 1.08. Thus hydrostatic pressure release dominates.",
            "hint": "Compare the ratio P₁/P₂ ≈ 4.9 with T₂/T₁ ≈ 1.08.",
            "blooms_level": "Analyze",
            "textbook_reference": "Exercise 12.5, Page 258",
            "image_search_query": "air bubble lake hydrostatic pressure boyle law"
        },
        {
            "question": "In NCERT Exercise 12.10, the collision duration τ_c is calculated to be roughly 4.3 × 10⁻¹³ s while the free transit time τ between collisions is 2.4 × 10⁻¹⁰ s. What fundamental kinetic theory assumption does this validate?",
            "options": [
                "(Recommended) That molecular collisions are instantaneous, so molecules spend virtually all their time moving freely without interacting",
                "That the gas is completely ionized into plasma",
                "That molecules behave as perfectly inelastic particles",
                "That the mean free path is zero"
            ],
            "correctAnswer": "(Recommended) That molecular collisions are instantaneous, so molecules spend virtually all their time moving freely without interacting",
            "correct_answer": "(Recommended) That molecular collisions are instantaneous, so molecules spend virtually all their time moving freely without interacting",
            "explanation": "Because τ_c / τ ≈ 1/550 << 1, the time spent during collisions is negligible compared to the time between collisions. This validates the core postulate that intermolecular potential energy during transit is zero.",
            "hint": "Compare collision duration with time spent in free flight.",
            "blooms_level": "Understand",
            "textbook_reference": "Exercise 12.10, Page 258",
            "image_search_query": "instantaneous collision duration kinetic theory postulate"
        },
        {
            "question": "Why does Helium have a higher root mean square speed than Argon at any given temperature (NCERT Exercise 12.9)?",
            "options": [
                "(Recommended) Because v_rms is inversely proportional to the square root of molecular mass (v_rms = √(3RT/M)), and Helium has a much smaller molar mass (4 u vs 40 u)",
                "Because Helium has more degrees of freedom than Argon",
                "Because Helium atoms possess stronger electric charge",
                "Because Argon atoms experience relativistic drag"
            ],
            "correctAnswer": "(Recommended) Because v_rms is inversely proportional to the square root of molecular mass (v_rms = √(3RT/M)), and Helium has a much smaller molar mass (4 u vs 40 u)",
            "correct_answer": "(Recommended) Because v_rms is inversely proportional to the square root of molecular mass (v_rms = √(3RT/M)), and Helium has a much smaller molar mass (4 u vs 40 u)",
            "explanation": "At a given temperature, average kinetic energy ½ m v_rms² = 3/2 k_B T is identical for all gases. To maintain equal kinetic energy, the lighter helium atom (m = 4 u) must move √10 ≈ 3.16 times faster than argon (m = 40 u).",
            "hint": "Check the inverse dependence on √M in v_rms = √(3RT/M).",
            "blooms_level": "Understand",
            "textbook_reference": "Exercise 12.9, Page 258",
            "image_search_query": "helium argon rms speed molar mass comparison"
        },
        {
            "question": "When 1 mole of a monatomic gas (C_v = 1.5 R) is mixed with 1 mole of a diatomic gas (C_v = 2.5 R) (NCERT Exercise 12.12), what is the resulting adiabatic index γ_mix?",
            "options": [
                "(Recommended) 1.50",
                "1.67",
                "1.40",
                "1.33"
            ],
            "correctAnswer": "(Recommended) 1.50",
            "correct_answer": "(Recommended) 1.50",
            "explanation": "C_v,mix = (1.5 R + 2.5 R) / 2 = 2.0 R. C_p,mix = C_v,mix + R = 3.0 R. Hence γ_mix = C_p / C_v = 3.0 R / 2.0 R = 1.50.",
            "hint": "Compute average C_v, then C_p = C_v + R, and take their ratio.",
            "blooms_level": "Apply",
            "textbook_reference": "Additional Exercise 12.12",
            "image_search_query": "mixture adiabatic index gamma ratio"
        },
        {
            "question": "According to Graham's Law of Diffusion (NCERT Exercise 12.14), if hydrogen gas diffuses 4 times faster than oxygen gas, what is the ratio of their molar masses (M_O₂ / M_H₂)?",
            "options": [
                "(Recommended) 16 : 1",
                "4 : 1",
                "2 : 1",
                "64 : 1"
            ],
            "correctAnswer": "(Recommended) 16 : 1",
            "correct_answer": "(Recommended) 16 : 1",
            "explanation": "r₁ / r₂ = √(M₂ / M₁) => 4 = √(M_O₂ / M_H₂) => M_O₂ / M_H₂ = 4² = 16. In reality, 32 g/mol / 2 g/mol = 16.",
            "hint": "Square both sides of r₁/r₂ = √(M₂/M₁).",
            "blooms_level": "Apply",
            "textbook_reference": "Additional Exercise 12.14",
            "image_search_query": "grahams law diffusion square root molar mass ratio"
        }
    ]

    with open("scripts/physics_class11_modules/physics_modules_ch12.json", "w", encoding="utf-8") as f:
        json.dump(modules, f, indent=2, ensure_ascii=False)
    print("Chapter 12 successfully enriched!")

if __name__ == "__main__":
    build_ch12()
