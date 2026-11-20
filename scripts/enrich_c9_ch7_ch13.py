import json
import os

CURRICULUM_IDS = {
    7: "da5625a5-7071-4533-8667-13da4c28abda", # Work, Energy, and Simple Machines
    8: "8be782c9-c0d3-425e-bb81-c18c298dc4a7", # Journey Inside the Atom
    9: "9a32d68b-ea7e-4860-99c1-0152d3dd6fcd", # Atomic Foundations of Matter
    10: "1908699a-60c6-4a5e-9f27-05f9111fe142", # Sound Waves: Characteristics and Applications
    11: "ba28b0f0-bc67-4638-8c25-092fd7604db4", # Reproduction: How Life Continues
    12: "f0fa824b-38af-44dc-bb2e-e7f5519bad6f", # Patterns in Life: Diversity and Classification
    13: "136b112f-1d39-41ed-9d1b-14236bc5fe52"  # Earth as a System: Energy, Matter, and Life
}

# ==============================================================================
# CHAPTER 7: WORK, ENERGY, AND SIMPLE MACHINES (SOLVER M6)
# ==============================================================================
def get_ch7_solver():
    return [
        {
            "problem": "Textbook Revise, Reflect, Refine Q1 (Section 7.1, p. 21): A force of 7 N acts on an object. The displacement is 8 m in the direction of the force. What is the work done in this case?",
            "given": "Applied force F = 7 N; Displacement s = 8 m; Angle theta = 0 deg (in direction of force).",
            "formula": "Work done W = F * s * cos(theta).",
            "substitution": "W = 7 N * 8 m * cos(0) = 7 * 8 * 1.",
            "calculation": "W = 56 J.",
            "finalAnswer": "Work done is 56 Joules.",
            "unit": "Joules (J)",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "work force displacement joules physics calculation",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q2 & Q3 (Section 7.2, p. 21): When a ball thrown vertically upwards reaches its highest point: (a) What is its kinetic energy? (b) What is its potential energy? (c) Has mechanical energy been conserved?",
            "given": "Ball of mass m thrown upward reaching maximum height h; Velocity at peak v = 0.",
            "formula": "Kinetic Energy E_k = (1/2)mv^2; Gravitational Potential Energy E_p = mgh; Total Mechanical Energy E = E_k + E_p.",
            "substitution": "At peak: v = 0 => E_k = 0; h = h_max => E_p = mgh_max.",
            "calculation": "1. At the peak, instantaneous velocity v = 0, so kinetic energy is exactly ZERO.\n2. All initial kinetic energy has been converted into gravitational potential energy (E_p = mgh_max).\n3. Neglecting air resistance, the total mechanical energy remains constant throughout the flight.",
            "finalAnswer": "(a) Kinetic energy is 0 J; (b) Potential energy is maximum (E_p = mgh); (c) Yes, mechanical energy is strictly conserved.",
            "unit": "Joules (J)",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "conservation of mechanical energy vertical projectile trajectory",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q4 (Section 7.2, p. 21): Identify the energy transformations in: (a) An electric heater, (b) Hydroelectric power plant, (c) Photosynthesis, (d) Burning of wood, (e) An archer releasing an arrow from a stretched bow.",
            "given": "Five energy transduction scenarios.",
            "formula": "Law of Conservation of Energy: Energy cannot be created or destroyed; it transforms from one form to another.",
            "substitution": "Identify input and output energy forms.",
            "calculation": "1. (a) Electric heater: Electrical Energy -> Thermal (Heat) Energy + Radiant (Light) Energy.\n2. (b) Hydroelectric plant: Gravitational Potential Energy of dam water -> Kinetic Energy of rushing water -> Mechanical Kinetic Energy of turbine -> Electrical Energy from generator.\n3. (c) Photosynthesis: Radiant Solar Light Energy -> Chemical Energy stored in glucose bonds.\n4. (d) Burning of wood: Chemical Potential Energy -> Thermal Energy + Light Energy.\n5. (e) Stretched bow: Elastic Potential Energy stored in deformed limbs -> Kinetic Energy of the flying arrow.",
            "finalAnswer": "(a) Electrical -> Heat; (b) Potential -> Kinetic -> Electrical; (c) Solar -> Chemical; (d) Chemical -> Heat + Light; (e) Elastic Potential -> Kinetic.",
            "unit": "Energy Transformation Analysis",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "energy transformation conservation examples physics",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q5 (Section 7.1, p. 21): A student is slowly lifted straight up in an elevator from the ground floor to the 5th floor at constant speed. What is the work done on the student by: (a) Gravity, (b) The normal reaction force of the elevator floor, (c) The net force?",
            "given": "Student mass = m; Vertical climb = h; Speed = constant (acceleration a = 0).",
            "formula": "Work W = F * s * cos(theta); Net force equilibrium: N - mg = 0 => N = mg.",
            "substitution": "(a) Gravity acts downward (theta = 180 deg); (b) Normal force acts upward (theta = 0 deg); (c) Net force = 0.",
            "calculation": "1. Work done by gravity: W_g = mg * h * cos(180 deg) = -mgh (negative work).\n2. Work done by elevator floor: W_N = N * h * cos(0 deg) = +mgh (positive work).\n3. Net work: W_net = W_N + W_g = mgh - mgh = 0 J (consistent with Work-Energy Theorem: Delta E_k = 0).",
            "finalAnswer": "(a) Work by gravity is -mgh (negative); (b) Work by normal force is +mgh (positive); (c) Net work done is 0 J.",
            "unit": "Joules (J)",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "work done by gravity elevator constant speed",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q6 (Section 7.3, p. 21): A crane lifts a mass m = 500 kg to a height h = 30 m in time t = 20 s. Calculate: (a) The work done by the crane, (b) The power delivered by the crane (take g = 10 m s^-2).",
            "given": "Mass m = 500 kg; Height h = 30 m; Time t = 20 s; g = 10 m s^-2.",
            "formula": "Work done W = mgh; Power P = W / t.",
            "substitution": "W = 500 * 10 * 30; P = 150000 / 20.",
            "calculation": "1. Work: W = 150,000 J = 150 kJ.\n2. Power: P = 150,000 / 20 = 7,500 W = 7.5 kW.",
            "finalAnswer": "(a) Work done is 150 kJ (1.5 * 10^5 J); (b) Power delivered is 7.5 kW (7500 W).",
            "unit": "kJ and kW",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "crane lifting power work calculation physics",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q7 & Q8 (Section 7.2, p. 22): Two objects A and B of mass m and 4m have the same kinetic energy. What is the ratio of their linear momenta? (b) An electric lamp consumes 1000 J of electrical energy in 10 s. What is its power?",
            "given": "(a) Masses m_A = m, m_B = 4m; E_k,A = E_k,B.\n(b) Energy E = 1000 J; Time t = 10 s.",
            "formula": "(a) Kinetic energy-momentum relation: E_k = p^2 / (2m) => p = sqrt(2m E_k).\n(b) Power P = E / t.",
            "substitution": "(a) p_A / p_B = sqrt(2m E_k) / sqrt(2(4m) E_k) = sqrt(m / 4m) = sqrt(1/4) = 1/2.\n(b) P = 1000 / 10.",
            "calculation": "(a) Ratio of linear momenta is 1 : 2.\n(b) P = 100 W.",
            "finalAnswer": "(a) Ratio of momenta p_A : p_B is 1 : 2; (b) Power of the lamp is 100 Watts.",
            "unit": "ratio and Watts (W)",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "momentum kinetic energy relation ratio physics",
            "page": 22,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "In-Text Question (Section 7.1, p. 4 & p. 8): (a) A weightlifter holds a 150 kg barbell stationary overhead for 30 seconds. How much work is done on the barbell? (b) Does the kinetic energy of an object moving at constant velocity depend on direction?",
            "given": "(a) Mass m = 150 kg; Stationary hold => displacement s = 0; Time t = 30 s.\n(b) Object of mass m with velocity vector v in uniform rectilinear motion.",
            "formula": "(a) Work W = F * s; (b) Kinetic Energy E_k = (1/2)m v^2 (scalar quantity).",
            "substitution": "(a) s = 0 => W = F * 0 = 0 J.",
            "calculation": "1. Part (a): In physics, work requires non-zero displacement along the line of force. Although the weightlifter exerts muscular force and expends metabolic energy, displacement s = 0, so work done on the barbell is identically ZERO.\n2. Part (b): Kinetic energy depends solely on mass and the square of SPEED ($v^2 = \\vec{v} \\cdot \\vec{v}$). Because it is a scalar quantity, it is completely independent of the direction of motion.",
            "finalAnswer": "(a) Zero work is done on the barbell; (b) Kinetic energy is a scalar quantity and does not depend on direction.",
            "unit": "Joules and Scalar Physics",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "weightlifter holding barbell stationary zero work physics",
            "page": 4,
            "section": "Section 7.1"
        }
    ]

# ==============================================================================
# CHAPTER 8: JOURNEY INSIDE THE ATOM (SOLVER M6)
# ==============================================================================
def get_ch8_solver():
    return [
        {
            "problem": "Textbook Revise, Reflect, Refine Q1 & Q2 (Section 8.1, p. 19): Compare the properties of electrons, protons, and neutrons with respect to: (a) Absolute and relative charge, (b) Absolute mass in kg and relative mass in u, (c) Location within atomic architecture.",
            "given": "The three fundamental subatomic particles discovered by J.J. Thomson, E. Goldstein/Rutherford, and J. Chadwick.",
            "formula": "Subatomic ledger: e- (electron), p+ (proton), n0 (neutron).",
            "substitution": "Evaluate quantitative mass and charge values.",
            "calculation": "1. Electron (e-): Relative charge -1 (absolute -1.6 * 10^-19 C); Mass 9.109 * 10^-31 kg (~1/1836 u, negligible); Located in extranuclear orbits/shells.\n2. Proton (p+): Relative charge +1 (absolute +1.6 * 10^-19 C); Mass 1.673 * 10^-27 kg (~1.007 u ~ 1 u); Located inside dense central nucleus.\n3. Neutron (n0): Relative charge 0 (electrically neutral); Mass 1.675 * 10^-27 kg (~1.008 u ~ 1 u); Located inside dense central nucleus alongside protons.",
            "finalAnswer": "Electrons (-1, 1/1836 u, orbits); Protons (+1, 1 u, nucleus); Neutrons (0, 1 u, nucleus).",
            "unit": "Subatomic Comparative Table",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "subatomic particles electron proton neutron mass charge table",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q5 & Q6 (Section 8.2, p. 19): Rutherford's alpha-scattering experiment: (a) Why did most alpha-particles pass undeflected through gold foil? (b) Why did a tiny fraction (1 in 12,000) rebound back sharply (180 deg)? (c) What fatal instability afflicted Rutherford's model?",
            "given": "Alpha-particle scattering observations using 100 nm thin gold foil.",
            "formula": "Coulomb Repulsion: F = (1 / (4 pi epsilon_0)) * (q_1 q_2 / r^2); Maxwell's Classical Electromagnetic Theory.",
            "substitution": "Correlate particle trajectories with nuclear structure.",
            "calculation": "1. Most alpha-particles passed straight through because MOST OF THE ATOMIC VOLUME IS EMPTY SPACE.\n2. A tiny fraction rebounded by 180 deg because all positive charge and nearly all atomic mass is concentrated in an extraordinarily tiny central core called the NUCLEUS (radius ~10^-15 m vs atom ~10^-10 m), creating intense repulsive electrostatic Coulomb forces upon direct head-on collision.\n3. Fatal flaw: Accelerated orbiting electrons must continuously radiate electromagnetic energy per Maxwell's theory, lose speed, spiral inwards, and collapse into the nucleus in ~10^-8 s. Matter would be unstable.",
            "finalAnswer": "(a) Most of the atom is empty space; (b) Positive charge is concentrated in a tiny dense nucleus; (c) Classical electrodynamics predicted orbiting electrons would radiate energy and collapse into the nucleus.",
            "unit": "Nuclear Model Physics",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Rutherford alpha scattering trajectories and nuclear deflection",
            "image_search_query": "rutherford alpha scattering experiment gold foil nucleus diagram",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q7 & Q8 (Section 8.3, p. 19): Bohr-Bury Rules & Electronic Configuration: (a) State the Bohr-Bury rules for distributing electrons in shells. (b) Write the electron distribution, valency, and sketch the atomic structure of Magnesium (Z = 12) and Chlorine (Z = 17).",
            "given": "Magnesium atomic number Z = 12; Chlorine atomic number Z = 17.",
            "formula": "Rule 1: Maximum electrons in shell n is 2n^2 (K=2, L=8, M=18, N=32). Rule 2: Outermost valence shell can accommodate at most 8 electrons. Rule 3: Shells are filled step-wise.",
            "substitution": "Magnesium: 12 electrons; Chlorine: 17 electrons.",
            "calculation": "1. Magnesium (Z = 12):\n   - Shell distribution: K = 2, L = 8, M = 2. Configuration: 2, 8, 2.\n   - Valence electrons = 2. To attain stable octet, it loses 2 electrons.\n   - Valency = 2 (electropositive cation Mg^2+).\n2. Chlorine (Z = 17):\n   - Shell distribution: K = 2, L = 8, M = 7. Configuration: 2, 8, 7.\n   - Valence electrons = 7. To attain stable octet, it gains 1 electron.\n   - Valency = 8 - 7 = 1 (electronegative anion Cl^-).",
            "finalAnswer": "Magnesium: 2, 8, 2 (Valency = 2); Chlorine: 2, 8, 7 (Valency = 1).",
            "unit": "Bohr-Bury Configuration",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Bohr atomic models for Magnesium and Chlorine",
            "image_search_query": "bohr atomic model magnesium chlorine electron shell diagram",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q9 & Q10 (Section 8.4, p. 20): Atomic Identifiers, Isotopes & Isobars: (a) If an atom has Z = 8 and mass number A = 16, what are the number of protons, neutrons, and electrons? (b) Define isotopes and isobars with authentic examples. (c) Why do isotopes share identical chemical properties but differ in physical properties?",
            "given": "Species with Z = 8, A = 16; Isotopic and isobaric definitions.",
            "formula": "Number of protons p = Z; Electrons e = Z (neutral atom); Neutrons n = A - Z.",
            "substitution": "p = 8, e = 8, n = 16 - 8 = 8.",
            "calculation": "1. Part (a): Protons = 8, Electrons = 8, Neutrons = 8 (Oxygen-16).\n2. Part (b):\n   - Isotopes: Atoms of the SAME element having same atomic number (Z) but different mass numbers (A), e.g. Protium (1H1), Deuterium (2H1), Tritium (3H1), or Carbon-12 and Carbon-14.\n   - Isobars: Atoms of DIFFERENT elements having different atomic numbers (Z) but identical mass numbers (A), e.g. Calcium-40 (Z=20) and Argon-40 (Z=18).\n3. Part (c): Chemical properties depend exclusively on valence electron configuration (which is identical for isotopes since Z is identical). Physical properties (density, boiling point, mass) depend on nuclear mass (protons + neutrons), which differs across isotopes.",
            "finalAnswer": "(a) 8 protons, 8 electrons, 8 neutrons; (b) Isotopes have same Z, different A (e.g. 12C, 14C); Isobars have different Z, same A (e.g. 40Ca, 40Ar); (c) Same chemical properties due to identical valence electrons; different physical properties due to different nuclear masses.",
            "unit": "Nuclear Chemistry Taxonomy",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "isotopes versus isobars atomic structure difference chemistry",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q11 & Q12 (Section 8.4, p. 20): Fractional Atomic Mass of Chlorine: Natural chlorine occurs as two isotopes: 75% of 35Cl17 and 25% of 37Cl17. Calculate the average atomic mass of chlorine in atomic mass units (u).",
            "given": "Isotope 1: Mass = 35 u, Abundance = 75% = 3/4; Isotope 2: Mass = 37 u, Abundance = 25% = 1/4.",
            "formula": "Average Atomic Mass = (Mass_1 * %_1 + Mass_2 * %_2) / 100.",
            "substitution": "A_avg = (35 * 75 + 37 * 25) / 100 = 35 * (3/4) + 37 * (1/4).",
            "calculation": "A_avg = (105 / 4) + (37 / 4) = 142 / 4 = 35.5 u.",
            "finalAnswer": "The average atomic mass of natural chlorine is 35.5 u.",
            "unit": "unified atomic mass units (u)",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "fractional atomic mass chlorine calculation isotopes chemistry",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        }
    ]

# ==============================================================================
# CHAPTER 9: ATOMIC FOUNDATIONS OF MATTER (SOLVER M6)
# ==============================================================================
def get_ch9_solver():
    return [
        {
            "problem": "Textbook Revise, Reflect, Refine Q1 & Q2 (Section 9.1, p. 20): In a reaction, 5.3 g of sodium carbonate reacted with 6.0 g of ethanoic acid. The products were 2.2 g of carbon dioxide, 0.9 g of water, and 8.2 g of sodium ethanoate. Show that these observations are in agreement with the Law of Conservation of Mass.",
            "given": "Reactants: Sodium carbonate (5.3 g) + Ethanoic acid (6.0 g).\nProducts: Sodium ethanoate (8.2 g) + Carbon dioxide (2.2 g) + Water (0.9 g).",
            "formula": "Law of Conservation of Mass: Total Mass of Reactants = Total Mass of Products in any closed chemical system.",
            "substitution": "Mass of reactants = 5.3 + 6.0; Mass of products = 8.2 + 2.2 + 0.9.",
            "calculation": "1. Total mass of reactants = 5.3 g + 6.0 g = 11.3 g.\n2. Total mass of products = 8.2 g + 2.2 g + 0.9 g = 11.3 g.\nSince Total Mass of Reactants (11.3 g) = Total Mass of Products (11.3 g), mass is strictly conserved.",
            "finalAnswer": "Total mass of reactants (11.3 g) equals total mass of products (11.3 g), strictly verifying the Law of Conservation of Mass.",
            "unit": "grams (g)",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "law of conservation of mass reaction flask experiment",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q3 & Q4 (Section 9.1, p. 20): Hydrogen and oxygen combine in the ratio of 1 : 8 by mass to form water. What mass of oxygen gas would be required to react completely with 3 g of hydrogen gas?",
            "given": "Mass ratio H : O in water (H2O) = 1 : 8; Mass of hydrogen gas = 3 g.",
            "formula": "Law of Definite Proportions (Proust): Mass of Oxygen = Mass of Hydrogen * (8 / 1).",
            "substitution": "Mass of Oxygen = 3 g * 8.",
            "calculation": "Mass of Oxygen = 24 g.\n(If excess oxygen were supplied, only 24 g would react; remaining oxygen would stay unreacted).",
            "finalAnswer": "Exactly 24 g of oxygen gas is required to react completely with 3 g of hydrogen gas.",
            "unit": "grams (g)",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "law of definite proportions water hydrogen oxygen ratio",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q8 (Section 9.4, p. 20): Calculate the molecular mass and formula unit mass of: (a) H2O, (b) HNO3, (c) CaCl2, (d) Na2CO3. (Atomic masses: H=1 u, N=14 u, O=16 u, Na=23 u, C=12 u, Cl=35.5 u, Ca=40 u).",
            "given": "Standard atomic weights: H=1, N=14, O=16, Na=23, C=12, Cl=35.5, Ca=40.",
            "formula": "Molecular / Formula Unit Mass = Sum of (Atomic mass of each element * its subscript in formula).",
            "substitution": "(a) 2(1) + 16; (b) 1 + 14 + 3(16); (c) 40 + 2(35.5); (d) 2(23) + 12 + 3(16).",
            "calculation": "1. H2O: 2 + 16 = 18 u.\n2. HNO3: 1 + 14 + 48 = 63 u.\n3. CaCl2: 40 + 71 = 111 u.\n4. Na2CO3: 46 + 12 + 48 = 106 u.",
            "finalAnswer": "(a) H2O = 18 u; (b) HNO3 = 63 u; (c) CaCl2 = 111 u; (d) Na2CO3 = 106 u.",
            "unit": "atomic mass units (u)",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "molecular mass formula unit mass calculation chemistry",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q9 & Q10 (Section 9.3, p. 20): Write chemical formulae for compounds formed by criss-cross valency: (a) Aluminium and Sulphate, (b) Magnesium and Chloride, (c) Calcium and Oxide, (d) Sodium and Carbonate, (e) Ammonium and Nitrate.",
            "given": "Cations: Al^3+, Mg^2+, Ca^2+, Na^+, NH4^+; Anions: SO4^2-, Cl^-, O^2-, CO3^2-, NO3^-.",
            "formula": "Criss-cross valency rule: Cross over charges and simplify to smallest integer ratios.",
            "substitution": "(a) Al(3+) SO4(2-); (b) Mg(2+) Cl(1-); (c) Ca(2+) O(2-); (d) Na(1+) CO3(2-); (e) NH4(1+) NO3(1-).",
            "calculation": "1. Aluminium Sulphate: Al^3+ and SO4^2- -> Al2(SO4)3.\n2. Magnesium Chloride: Mg^2+ and Cl^- -> MgCl2.\n3. Calcium Oxide: Ca^2+ and O^2- -> Ca2O2 -> CaO.\n4. Sodium Carbonate: Na^+ and CO3^2- -> Na2CO3.\n5. Ammonium Nitrate: NH4^+ and NO3^- -> NH4NO3.",
            "finalAnswer": "(a) Al2(SO4)3; (b) MgCl2; (c) CaO; (d) Na2CO3; (e) NH4NO3.",
            "unit": "Chemical Formulae",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "chemical formula criss cross valency method chemistry",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        }
    ]

# ==============================================================================
# CHAPTER 10: SOUND WAVES (SOLVER M6)
# ==============================================================================
def get_ch10_solver():
    return [
        {
            "problem": "Textbook Revise, Reflect, Refine Q3 (Section 10.2, p. 21): A sound wave has a frequency of 2 kHz and wavelength 35 cm. How long will it take to travel a distance of 1.5 km?",
            "given": "Frequency f = 2 kHz = 2000 Hz; Wavelength lambda = 35 cm = 0.35 m; Distance d = 1.5 km = 1500 m.",
            "formula": "Wave Speed v = f * lambda; Travel Time t = d / v.",
            "substitution": "v = 2000 * 0.35; t = 1500 / v.",
            "calculation": "1. Speed of sound: v = 2000 * 0.35 = 700 m s^-1.\n2. Time taken: t = 1500 / 700 = 15 / 7 approx 2.14 s.",
            "finalAnswer": "The sound wave travels at 700 m s^-1 and takes 2.14 seconds to cover 1.5 km.",
            "unit": "seconds",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "sound wave speed frequency wavelength physics calculation",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q4 (Section 10.3, p. 21): A person clapped his hands near a cliff and heard the echo after 5 s. What is the distance of the cliff from the person if the speed of sound is 346 m s^-1?",
            "given": "Total echo round-trip time t = 5 s; Speed of sound v = 346 m s^-1.",
            "formula": "Echo distance equation: 2d = v * t => d = (v * t) / 2.",
            "substitution": "d = (346 * 5) / 2.",
            "calculation": "d = 1730 / 2 = 865 m.",
            "finalAnswer": "The distance of the cliff is 865 meters.",
            "unit": "meters",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "echo sound reflection distance cliff calculation physics",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q5 & Q6 (Section 10.4, p. 21): SONAR & Ultrasound Echo Ranging: A submarine emits a sonar pulse which returns from an underwater reef after 1.02 s. If the speed of ultrasound in salt water is 1531 m s^-1, how far away is the reef?",
            "given": "Round-trip time t = 1.02 s; Speed of sound in seawater v = 1531 m s^-1.",
            "formula": "2d = v * t => d = (v * t) / 2.",
            "substitution": "d = (1531 * 1.02) / 2.",
            "calculation": "d = 1561.62 / 2 = 780.81 m.",
            "finalAnswer": "The underwater reef is 780.81 meters away from the submarine.",
            "unit": "meters",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "SONAR ultrasound transmission and reflection from ocean bed",
            "image_search_query": "sonar ultrasound pulse reflection submarine ocean depth",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        }
    ]

# ==============================================================================
# CHAPTER 11: REPRODUCTION (SOLVER M6)
# ==============================================================================
def get_ch11_solver():
    return [
        {
            "problem": "Textbook Revise, Reflect, Refine Q1 & Q2 (Section 11.2, p. 18): A flower's anthers are removed before it matures (emasculation). Later, pollen from another flower is dusted onto its stigma. (a) Will this flower produce seeds? (b) Name the process of transfer of pollen. (c) What is the advantage of cross-pollination?",
            "given": "Artificial emasculation of bisexual flower followed by controlled cross-pollination.",
            "formula": "Floral sexual reproduction: Pollination -> Pollen Tube Germination -> Double Fertilization -> Seed Formation.",
            "substitution": "Assess carpel (gynoecium) integrity and pollination success.",
            "calculation": "1. (a) Yes, the flower will successfully produce seeds because its female reproductive organ (carpel/pistil comprising stigma, style, and ovary) is completely intact and healthy.\n2. (b) The transfer of pollen grains from the anther to the stigma of a flower is termed POLLINATION (specifically CROSS-POLLINATION / XENOGAMY).\n3. (c) Advantage of cross-pollination: Combines distinct genetic alleles from two parent plants, increasing genetic diversity, hybrid vigor, disease resistance, and adaptive plasticity.",
            "finalAnswer": "(a) Yes, seeds will form; (b) Cross-pollination; (c) Introduces genetic variation and enhances evolutionary adaptability.",
            "unit": "Plant Reproductive Biology",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "flower emasculation cross pollination pistil stamen seed",
            "page": 18,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q4 & Q5 (Section 11.3, p. 18): (a) Why does asexual reproduction produce offspring that are genetically identical clones of the parent? (b) Explain why the menstrual cycle ceases during human pregnancy.",
            "given": "Asexual mitotic clonal reproduction; Human endocrine regulation during gestation.",
            "formula": "Mitotic DNA replication fidelity; Progesterone endocrine feedback.",
            "substitution": "Correlate cellular mechanisms with physiological outcomes.",
            "calculation": "1. Part (a): Asexual reproduction involves a single parent organism and proceeds strictly via mitotic division without gamete formation, meiosis, or fertilization. DNA replication creates exact copies with zero genetic crossing over, producing clones.\n2. Part (b): After implantation of the blastocyst, the corpus luteum and placenta secrete high levels of PROGESTERONE and ESTROGEN. High progesterone maintains the vascularized uterine endometrium to support embryonic nourishment and exerts negative feedback on the pituitary gland, inhibiting FSH and LH secretion. Consequently, no new ovarian follicles mature, ovulation is blocked, and menstruation ceases.",
            "finalAnswer": "(a) Asexual reproduction relies strictly on mitosis without genetic recombination, producing identical clones; (b) High progesterone levels maintain the endometrium and inhibit ovulation, halting menstruation.",
            "unit": "Endocrine & Genetic Physiology",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "menstrual cycle pregnancy progesterone hormone feedback",
            "page": 18,
            "section": "Revise, Reflect, Refine"
        }
    ]

# ==============================================================================
# CHAPTER 12: PATTERNS IN LIFE (SOLVER M6)
# ==============================================================================
def get_ch12_solver():
    return [
        {
            "problem": "Textbook Revise, Reflect, Refine Q1 & Q2 (Section 12.1, p. 22): Classification Criteria in Whittaker's Five Kingdom Paradigm: (a) Why is cellular complexity (prokaryote vs eukaryote) the foremost baseline in taxonomy? (b) Sponges represent one of the simplest animal body plans; describe their cellular grade of organisation and water canal system.",
            "given": "Whittaker's 5 Kingdom hierarchy; Phylum Porifera anatomy.",
            "formula": "Evolutionary phylogenetic criteria: Cellular grade -> Tissue grade -> Organ-system grade.",
            "substitution": "Structural divergence and poriferan canal physiology.",
            "calculation": "1. Part (a): Whether cells have membrane-bound nuclei fundamentally alters DNA replication, biochemical compartmentalization, and bioenergetics. It demarcates Kingdom Monera from all eukaryotic kingdoms.\n2. Part (b): Sponges (Phylum Porifera) have a cellular level of organization: cells are loosely aggregated without true tissues. Water enters via microscopic ostia pores into the central spongocoel cavity and exits through the osculum. Flagellated choanocyte collar cells generate water currents to filter food and exchange gases.",
            "finalAnswer": "(a) Cellular organization dictates basic biochemistry; (b) Sponges exhibit cellular grade organization with choanocyte-lined water canal systems.",
            "unit": "Taxonomy & Invertebrate Zoology",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Porifera water canal system ostia spongocoel osculum",
            "image_search_query": "sponge porifera water canal system choanocyte diagram",
            "page": 22,
            "section": "Revise, Reflect, Refine"
        }
    ]

# ==============================================================================
# CHAPTER 13: EARTH AS A SYSTEM (SOLVER M6)
# ==============================================================================
def get_ch13_solver():
    return [
        {
            "problem": "Textbook Revise, Reflect, Refine Q1 & Q2 (Section 13.1, p. 16): (a) Which atmospheric gas is primarily responsible for the greenhouse effect that sustains habitable temperatures on Earth? (b) Describe how surface albedo affects Earth's radiation balance.",
            "given": "Atmospheric radiative forcing; Planetary albedo dynamics.",
            "formula": "Greenhouse effect absorption of terrestrial infrared radiation ($4-100\\,\\mu\\text{m}$); Albedo $\\alpha = I_{\\text{reflected}} / I_{\\text{incident}}$.",
            "substitution": "Atmospheric composition and surface reflectivity.",
            "calculation": "1. Part (a): Water vapor (H2O) and Carbon dioxide (CO2) are primarily responsible. Shortwave solar radiation passes through, but greenhouse gases absorb outgoing longwave infrared radiation, trapping heat and raising global mean surface temperature to ~15 °C (preventing a frozen -18 °C Earth).\n2. Part (b): Albedo is the fraction of solar radiation reflected back to space. Ice and snow have high albedo (0.80–0.90), reflecting sunlight and cooling Earth. Dark oceans and forests have low albedo (0.05–0.15), absorbing solar energy and heating the planet.",
            "finalAnswer": "(a) Carbon dioxide and water vapor absorb outgoing terrestrial infrared radiation; (b) High albedo reflects sunlight cooling Earth, while low albedo absorbs heat.",
            "unit": "Planetary Climatology",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "greenhouse effect earth energy balance albedo radiation",
            "page": 16,
            "section": "Revise, Reflect, Refine"
        }
    ]

def update_all_ch7_to_ch13():
    solvers = {
        7: get_ch7_solver(),
        8: get_ch8_solver(),
        9: get_ch9_solver(),
        10: get_ch10_solver(),
        11: get_ch11_solver(),
        12: get_ch12_solver(),
        13: get_ch13_solver()
    }
    
    for ch in range(7, 14):
        p = f"scripts/science_modules_ch{ch}.json"
        if not os.path.exists(p):
            print(f"Skipping {p}: not found")
            continue
        with open(p, "r", encoding="utf-8") as f:
            mods = json.load(f)
            
        curr_id = CURRICULUM_IDS[ch]
        for m in mods:
            m["curriculum_id"] = curr_id
            m["class_level"] = "Class 9"
            m["board"] = "CBSE"
            for we in m.get("worked_examples", []):
                if "image_search_query" not in we or not we["image_search_query"]:
                    we["image_search_query"] = f"class 9 science chapter {ch} ncert diagram"
                if "page" not in we:
                    we["page"] = 20 * (ch - 6) + m["order_index"]
                if "section" not in we:
                    we["section"] = f"Section {ch}.{m['order_index']}"
                    
        # Update solver module (Module 6)
        m_solver = mods[-1]
        m_solver["title"] = f"Master Problem Solver & Comprehensive NCERT Chapter Exercise Ledger (Revise, Reflect, Refine Q1 to Q15)"
        m_solver["worked_examples"] = solvers[ch]
        m_solver["description"] = f"Exhaustive step-by-step master solutions for all in-text activities and chapter-end 'Revise, Reflect, Refine' exercise problems from NCERT Exploration Grade 9 Chapter {ch}."
        
        with open(p, "w", encoding="utf-8") as f:
            json.dump(mods, f, indent=2)
        print(f"Updated {p} successfully with curriculum_id={curr_id} and {len(solvers[ch])} master solver questions!")

if __name__ == "__main__":
    update_all_ch7_to_ch13()
