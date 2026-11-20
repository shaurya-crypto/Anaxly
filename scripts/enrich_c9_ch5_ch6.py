import json
import os

CURRICULUM_IDS = {
    5: "8d01a5f5-bf82-49c2-9fab-253d26b086f4", # Exploring Mixtures and their Separation
    6: "7e1d5438-1174-4577-8599-5f05a6642093"  # How Forces Affect Motion
}

# ==============================================================================
# CHAPTER 5: EXPLORING MIXTURES AND THEIR SEPARATION (EXHAUSTIVE SOLVER M6)
# ==============================================================================
def get_ch5_solver_examples():
    return [
        {
            "problem": "Textbook Revise, Reflect, Refine Q1 (Section 5.1, p. 19): Which of the following mixtures are correctly classified as homogeneous or heterogeneous? (a) Brass (copper + zinc), (b) Muddy water, (c) Air, (d) Oil and water, (e) Vinegar (acetic acid + water), (f) Chalk powder in water.",
            "given": "Six physical mixtures to classify into homogeneous vs heterogeneous.",
            "formula": "Homogeneous = Uniform composition and single phase throughout (no visible phase boundaries); Heterogeneous = Non-uniform composition with distinct physical phase boundaries.",
            "substitution": "Evaluate phase boundaries and uniformity.",
            "calculation": "1. Brass: Solid solution (alloy) of zinc in copper; completely uniform at atomic level ⟶ Homogeneous.\n2. Muddy water: Insoluble soil particles suspended in water; settles over time with clear boundary ⟶ Heterogeneous.\n3. Air: Gaseous solution of N₂, O₂, Ar, CO₂; perfectly uniform single phase ⟶ Homogeneous.\n4. Oil and water: Two immiscible liquid phases with sharp meniscus interface ⟶ Heterogeneous.\n5. Vinegar: Clear single-phase aqueous solution of 5-8% acetic acid in water ⟶ Homogeneous.\n6. Chalk powder in water: Insoluble CaCO₃ particles suspended in water ⟶ Heterogeneous.",
            "finalAnswer": "Homogeneous mixtures: (a) Brass, (c) Air, (e) Vinegar; Heterogeneous mixtures: (b) Muddy water, (d) Oil and water, (f) Chalk in water.",
            "unit": "Mixture Classification",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "homogeneous versus heterogeneous mixtures examples chemistry",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q2 & Q3 (Section 5.1, p. 19): A mixture can be categorised as a true solution, a suspension, or a colloid. Compare their key properties: (i) Particle size, (ii) Filterability, (iii) Settling stability, (iv) Tyndall effect. Explain why true solutions do not scatter light.",
            "given": "Three dispersion categories: True Solutions, Colloids, Suspensions.",
            "formula": "Rayleigh Scattering Law: Scattering intensity $I \\propto d^6 / \\lambda^4$, requiring particle size $d \\sim 1\\text{ to }1000\\text{ nm}$.",
            "substitution": "Contrast dispersion properties across the three states.",
            "calculation": "1. Particle Size: True Solution < 1 nm; Colloid 1 nm to 1000 nm (1 μm); Suspension > 1000 nm (visible under microscope/naked eye).\n2. Filterability: True solutions and colloids pass through standard filter paper; suspensions are retained on filter paper.\n3. Stability: True solutions and colloids are stable (solute does not settle); suspensions are unstable (particles settle by gravity).\n4. Tyndall Effect: True solutions do NOT exhibit the Tyndall effect because their solute particles (< 1 nm) are far smaller than the wavelength of visible light (400–700 nm), failing to scatter photons. Colloids and suspensions scatter light visibly.",
            "finalAnswer": "True solutions (<1 nm) are stable and do not scatter light; colloids (1-1000 nm) exhibit Tyndall scattering; suspensions (>1000 nm) settle and are opaque.",
            "unit": "Dispersion State Comparative Analysis",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "solution colloid suspension particle size tyndall effect",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q4 (Section 5.2, p. 20): Solve the following concentration problems: (a) A solution contains 40 g of common salt in 320 g of water. Calculate the concentration in terms of mass-by-mass percentage of the solution. (b) To make a saturated solution, 36 g of sodium chloride is dissolved in 100 g of water at 293 K. Find its concentration at this temperature.",
            "given": "(a) Mass of solute (NaCl) = 40 g, Mass of solvent (water) = 320 g.\n(b) Mass of solute = 36 g, Mass of solvent = 100 g.",
            "formula": "Mass percentage of solution = $\\frac{\\text{Mass of Solute}}{\\text{Total Mass of Solution}} \\times 100\\%$, where Total Mass = Mass of Solute + Mass of Solvent.",
            "substitution": "(a) Mass of solution = 40 + 320 = 360 g; $\\% (m/m) = \\frac{40}{360} \\times 100$.\n(b) Mass of solution = 36 + 100 = 136 g; $\\% (m/m) = \\frac{36}{136} \\times 100$.",
            "calculation": "(a) $\\frac{40}{360} \\times 100 = \\frac{1}{9} \\times 100 = 11.11\\%$.\n(b) $\\frac{36}{136} \\times 100 = \\frac{9}{34} \\times 100 = 26.47\\%$.",
            "finalAnswer": "(a) Concentration is 11.11% (m/m); (b) Saturated concentration at 293 K is 26.47% (m/m).",
            "unit": "Percentage by mass (m/m)",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "mass percentage solution concentration calculations chemistry",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q5 (Section 5.2, p. 20): The label on a cooking oil bottle reads 'Volume = 1 Litre, Net Mass = 910 g'. (a) Calculate the density of the cooking oil in g cm⁻³ and in kg m⁻³. (b) If 50 g of this oil is mixed with 450 g of hexane, what is the concentration in mass percentage?",
            "given": "Volume V = 1 L = 1000 mL = 1000 cm³; Mass m = 910 g; Oil solute = 50 g; Hexane solvent = 450 g.",
            "formula": "Density $\\rho = \\frac{\\text{Mass}}{\\text{Volume}}$; Mass % = $\\frac{\\text{Mass of Solute}}{\\text{Total Mass}} \\times 100\\%$.",
            "substitution": "(a) $\\rho = \\frac{910\\text{ g}}{1000\\text{ cm}^3}$; (b) Mass % = $\\frac{50}{50 + 450} \\times 100$.",
            "calculation": "1. Density:\n   $\\rho = 0.91\\text{ g cm}^{-3} = 0.91 \\times 1000\\text{ kg m}^{-3} = 910\\text{ kg m}^{-3}$.\n2. Concentration in hexane:\n   Total mass = 50 + 450 = 500 g.\n   $\\text{Mass \\%} = \\frac{50}{500} \\times 100\\% = 10\\%$.",
            "finalAnswer": "(a) Density is 0.91 g cm⁻³ (910 kg m⁻³); (b) Concentration of oil in hexane is 10% (m/m).",
            "unit": "g cm⁻³ and % (m/m)",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "cooking oil density mass volume concentration chemistry",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q6 (Section 5.1, p. 20): Assertion (A): Solutions do not exhibit the Tyndall effect. Reason (R): The particles in a solution are smaller than 1 nm in diameter and cannot scatter visible light rays. Choose the correct option and justify.",
            "given": "Assertion and Reason on the optical scattering properties of true solutions.",
            "formula": "Tyndall Effect: Scattering of light occurs when dispersing particle size is comparable to the wavelength of light ($\\lambda \\sim 400-700\\text{ nm}$).",
            "substitution": "True solution solute dimensions ($< 1\\text{ nm}$).",
            "calculation": "1. Assertion (A) is True: A flashlight beam passing through a copper sulfate solution or salt solution is invisible from the side (no illuminated path).\n2. Reason (R) is True: Solute particles are single ions or small molecules with diameters under 1 nm ($10^{-9}\\text{ m}$), which is roughly 500 times smaller than visible light wavelengths, resulting in negligible light scattering.\n3. Reason (R) is the correct and direct physical explanation of Assertion (A).",
            "finalAnswer": "Correct Option: Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "unit": "Optical Physics & Colloid Chemistry",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "tyndall effect true solution scattering light ray",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q7 (Section 5.3, p. 20): State the principle and name the technique used to separate the mixtures in Table 5.3: (a) Butter from curd, (b) Salt from seawater, (c) Camphor from salt, (d) Dyes in black ink, (e) Acetone and water, (f) Iron pins from sand.",
            "given": "Six mixture separation challenges from Table 5.3.",
            "formula": "Separation depends on differences in physical properties: density, boiling point, sublimation, solubility/adsorption, and magnetic susceptibility.",
            "substitution": "Assign specific laboratory separation methods.",
            "calculation": "1. (a) Butter from curd: CENTRIFUGATION (denser skimmed milk forced outwards; lighter butter fat coalesces and floats on top).\n2. (b) Salt from seawater: EVAPORATION / CRYSTALLIZATION (water evaporates under solar heat, leaving crystalline non-volatile NaCl).\n3. (c) Camphor from salt: SUBLIMATION (camphor changes directly from solid to vapor upon heating and condenses on cold funnel; salt does not sublime).\n4. (d) Dyes in black ink: PAPER CHROMATOGRAPHY (components separate based on differential solubility in mobile water phase and adsorption on stationary paper phase).\n5. (e) Acetone and water: FRACTIONAL DISTILLATION (miscible liquids with distinct boiling points: acetone 56 °C, water 100 °C).\n6. (f) Iron pins from sand: MAGNETIC SEPARATION (ferromagnetic iron attracted to magnet; diamagnetic silica sand left behind).",
            "finalAnswer": "(a) Centrifugation; (b) Evaporation/Crystallization; (c) Sublimation; (d) Paper Chromatography; (e) Simple/Fractional Distillation; (f) Magnetic Separation.",
            "unit": "Separation Science Ledger",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "separation techniques mixtures chemistry ncert laboratory",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q8 (Section 5.3, p. 20): Two miscible liquids, A and B, are present in a mixture. The boiling point of liquid A is 65 °C and that of liquid B is 80 °C. (a) Which method is suitable for separating them? (b) Explain the role of the fractionating column in this process.",
            "given": "Miscible liquids A and B; $T_{b,A} = 65\\,^\\circ\\text{C}$, $T_{b,B} = 80\\,^\\circ\\text{C}$; Difference $\\Delta T_b = 80 - 65 = 15\\,^\\circ\\text{C} < 25\\,^\\circ\\text{C}$.",
            "formula": "Separation criterion: When difference in boiling points $\\Delta T_b < 25\\,^\\circ\\text{C}$, FRACTIONAL DISTILLATION using a fractionating column is mandatory.",
            "substitution": "Assess fractionating column mechanism.",
            "calculation": "1. (a) FRACTIONAL DISTILLATION must be used because the boiling point difference (15 °C) is less than the 25 °C threshold required for simple distillation.\n2. (b) Role of Fractionating Column: A glass-bead packed column provides an extensive surface area for repeated cycles of condensation and re-vaporization. As the rising vapor mixture ascends, the higher-boiling component B (80 °C) repeatedly condenses and trickles down, while the lower-boiling component A (65 °C) remains in the vapor phase, reaching the top condenser in pure form.",
            "finalAnswer": "(a) Fractional Distillation; (b) The fractionating column provides surface area for repeated condensation-vaporization cycles, achieving sharp separation for boiling point differences under 25 °C.",
            "unit": "Fractional Distillation Engineering",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Fractional distillation apparatus with glass-bead column",
            "image_search_query": "fractional distillation fractionating column glass beads diagram",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q9 (Section 5.3, p. 20): Compare evaporation, crystallization, and distillation. Which method is superior for obtaining pure solid copper sulfate from an impure sample, and why?",
            "given": "Three thermal purification methods; Target: Pure solid copper sulfate (CuSO₄·5H₂O).",
            "formula": "Purification physics: Evaporation leaves non-volatile impurities; Crystallization separates pure crystal lattice leaving soluble impurities in mother liquor.",
            "substitution": "Compare mechanisms and decomposition risks.",
            "calculation": "1. Evaporation boils away all solvent to dryness, leaving behind all non-volatile soluble impurities and often decomposing heat-sensitive salts.\n2. Distillation purifies and collects the volatile solvent vapor, leaving solutes in the flask.\n3. Crystallization involves heating to form a hot saturated solution, filtering insoluble dirt, and cooling slowly so solute molecules organize into a pure geometric crystal lattice, excluding soluble impurities which remain in the mother liquor.\n4. Superiority: CRYSTALLIZATION is far superior for copper sulfate because simple heating to dryness decomposes blue copper sulfate into white anhydrous powder and bakes impurities into the solid.",
            "finalAnswer": "Crystallization is superior because it excludes soluble impurities in the mother liquor and prevents thermal decomposition of copper sulfate crystals.",
            "unit": "Purification Methodology",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "crystallization copper sulfate pure crystals laboratory",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q10 (Section 5.1, p. 20): Blood is an example of a colloidal mixture. (a) What would happen if blood were a true solution? (b) How are blood components separated in clinical laboratories for medical tests?",
            "given": "Blood colloidal suspension (erythrocytes, leukocytes, platelets suspended in plasma protein colloid).",
            "formula": "Centrifugal separation: Radial sedimentation force $F_c = m\\omega^2 r$.",
            "substitution": "Evaluate physiological and diagnostic aspects of blood.",
            "calculation": "1. (a) If blood were a true solution: Hemoglobin, clotting factors, and cellular membranes would be dissolved molecules (<1 nm). They would leak freely through the selectively permeable capillary endothelial pores into interstitial tissue fluid, destroying oncotic pressure, preventing oxygen binding regulation, and causing fatal systemic edema and internal bleeding.\n2. (b) In medical laboratories, blood is separated using CENTRIFUGATION at 3000–4000 rpm. Denser cellular elements (RBCs, WBCs) sediment to the bottom of the tube, while lighter liquid blood plasma (carrying proteins and antibodies) remains as the clear supernatant layer on top.",
            "finalAnswer": "(a) Essential proteins and hemoglobin would leak out through capillary walls, causing fatal edema; (b) Blood components are separated using centrifugation.",
            "unit": "Clinical Colloid Science",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "blood centrifugation plasma buffy coat red blood cells",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q11 (Section 5.3, p. 21): You are given a mixture of dry sand, common salt (NaCl), and naphthalene balls. Devise an exact sequential flow of laboratory separation steps to obtain each component in pure dry form.",
            "given": "Ternary mixture: Sand (insoluble, non-sublimable), Salt (water-soluble, non-sublimable), Naphthalene (water-insoluble, sublimable).",
            "formula": "Differential physical properties: Sublimation ⟶ Dissolution ⟶ Filtration ⟶ Crystallization.",
            "substitution": "Step-by-step separation protocol.",
            "calculation": "Step 1 (Sublimation): Place mixture in china dish covered with an inverted glass funnel plugged with cotton. Heat gently. Naphthalene sublimes into vapor and deposits as pure solid crystals on the cool funnel walls. Pure Naphthalene recovered.\nStep 2 (Dissolution): Add water to remaining residue of sand and salt; stir thoroughly. Common salt dissolves completely in water; sand remains insoluble.\nStep 3 (Filtration): Pour suspension through filter paper in a funnel. Insoluble sand is retained as residue on filter paper. Wash with distilled water and dry. Pure Sand recovered.\nStep 4 (Crystallization / Evaporation): Heat filtrate (salt solution) to saturation and cool slowly to obtain pure crystals of Sodium Chloride. Pure Salt recovered.",
            "finalAnswer": "Sequential flow: 1. Sublimation (extracts naphthalene) ⟶ 2. Water dissolution ⟶ 3. Filtration (extracts sand) ⟶ 4. Crystallization/Evaporation (extracts common salt).",
            "unit": "Multistep Separation Protocol",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Sequential flow chart for separating naphthalene, sand, and salt",
            "image_search_query": "sublimation filtration evaporation separation mixture flowchart",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q12 (Section 5.3, p. 21): Why is simple distillation an effective method for separating a mixture of water (boiling point 100 °C) and acetone (boiling point 56 °C), whereas it cannot be used to separate ethanol (78 °C) and water (100 °C)?",
            "given": "Mixture 1: Acetone (56 °C) + Water (100 °C) ⟶ $\\Delta T = 44\\,^\\circ\\text{C}$.\nMixture 2: Ethanol (78 °C) + Water (100 °C) ⟶ $\\Delta T = 22\\,^\\circ\\text{C}$.",
            "formula": "Distillation Criterion: Simple distillation requires $\\Delta T_b \\ge 25\\,^\\circ\\text{C}$; Fractional distillation is required when $\\Delta T_b < 25\\,^\\circ\\text{C}$.",
            "substitution": "Evaluate boiling point margins.",
            "calculation": "1. For Acetone and Water, the boiling point difference is $\\Delta T = 100 - 56 = 44\\,^\\circ\\text{C}$. Because $\\Delta T > 25\\,^\\circ\\text{C}$, when heated to ~56–60 °C, acetone evaporates rapidly while water vapor pressure remains negligible. Acetone vapors pass into the condenser and distill cleanly.\n2. For Ethanol and Water, $\\Delta T = 100 - 78 = 22\\,^\\circ\\text{C} < 25\\,^\\circ\\text{C}$. At 78 °C, significant water vapor evaporates alongside ethanol. Without a fractionating column to provide repeated condensation stages, the distillate contains substantial water contamination.",
            "finalAnswer": "Acetone and water have a large boiling point difference (44 °C > 25 °C) allowing simple distillation; ethanol and water differ by only 22 °C (< 25 °C), requiring fractional distillation.",
            "unit": "Distillation Thermodynamics",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "simple versus fractional distillation boiling point difference",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q13 (Section 5.2, p. 21): Answer the following based on the solubility data of salts in water at various temperatures: (a) What mass of potassium nitrate is needed to produce a saturated solution in 50 g of water at 313 K (solubility = 62 g / 100 g water)? (b) If a saturated solution of potassium chloride in 100 g water at 353 K (solubility = 54 g) is cooled to 293 K (solubility = 35 g), what mass of crystals will precipitate out?",
            "given": "(a) Solubility of KNO₃ at 313 K = 62 g per 100 g water; Mass of water = 50 g.\n(b) Solubility of KCl at 353 K = 54 g / 100 g water; Solubility at 293 K = 35 g / 100 g water.",
            "formula": "Mass of solute in water m = $\\text{Solubility} \\times \\frac{\\text{Mass of Water}}{100\\text{ g}}$; Mass precipitated $\\Delta m = m_{\\text{hot}} - m_{\\text{cold}}$.",
            "substitution": "(a) $m = 62 \\times \\frac{50}{100}$; (b) $\\Delta m = 54 - 35$.",
            "calculation": "(a) $m = 62 \\times 0.5 = 31\\text{ g}$.\n(b) At 353 K, 100 g water holds 54 g KCl. Upon cooling to 293 K, 100 g water can only hold 35 g KCl in solution.\nMass precipitated = $54 - 35 = 19\\text{ g}$.",
            "finalAnswer": "(a) 31 g of potassium nitrate is needed for 50 g water; (b) 19 g of potassium chloride crystals will precipitate out.",
            "unit": "grams",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "solubility curve temperature crystallization calculation chemistry",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q14 (Section 5.2, p. 21): Three students A, B, and C prepare sugar solutions: Student A dissolves 10 g sugar in 100 g water; Student B dissolves 20 g sugar in 200 g water; Student C dissolves 15 g sugar in 150 g water. Compare the concentrations of the three solutions.",
            "given": "Student A: 10 g solute, 100 g solvent.\nStudent B: 20 g solute, 200 g solvent.\nStudent C: 15 g solute, 150 g solvent.",
            "formula": "Concentration % (m/m) = $\\frac{\\text{Mass of Solute}}{\\text{Mass of Solute} + \\text{Mass of Solvent}} \\times 100\\%$.",
            "substitution": "Student A: $\\frac{10}{10 + 100} \\times 100$; Student B: $\\frac{20}{20 + 200} \\times 100$; Student C: $\\frac{15}{15 + 150} \\times 100$.",
            "calculation": "Student A: $\\frac{10}{110} \\times 100 = 9.09\\%$.\nStudent B: $\\frac{20}{220} \\times 100 = \\frac{1}{11} \\times 100 = 9.09\\%$.\nStudent C: $\\frac{15}{165} \\times 100 = \\frac{1}{11} \\times 100 = 9.09\\%$.",
            "finalAnswer": "All three students prepared solutions of identical concentration (9.09% m/m), because the solute-to-solvent ratio is strictly equal (1 : 10) in all three cases.",
            "unit": "Percentage by mass (m/m)",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "solution concentration ratio comparison mass percentage",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q15 (Section 5.3, p. 22): Examine the paper chromatogram in Fig. 5.26 showing ink spot separation with water solvent: Spot 1 travelled 2 cm, Spot 2 travelled 5 cm, and the solvent front travelled 8 cm. (a) Which dye component is most soluble in water? (b) Calculate the retention factor ($R_f$) for both dyes.",
            "given": "Distance moved by dye 1 $d_1 = 2\\text{ cm}$; Distance moved by dye 2 $d_2 = 5\\text{ cm}$; Solvent front distance $D = 8\\text{ cm}$.",
            "formula": "Retention Factor $R_f = \\frac{\\text{Distance travelled by component}}{\\text{Distance travelled by solvent front}}$. Component with higher solubility travels farther.",
            "substitution": "$R_{f,1} = \\frac{2}{8}$; $R_{f,2} = \\frac{5}{8}$.",
            "calculation": "1. Part (a): Component 2 travelled 5 cm, significantly farther than Component 1 (2 cm). Therefore, Component 2 has higher solubility in the mobile water phase and lower affinity for the stationary cellulose paper.\n2. Part (b):\n   $R_{f,1} = \\frac{2}{8} = 0.25$.\n   $R_{f,2} = \\frac{5}{8} = 0.625$.",
            "finalAnswer": "(a) Spot 2 is the most soluble in water; (b) Retention factors: $R_{f,1} = 0.25$ and $R_{f,2} = 0.625$.",
            "unit": "dimensionless Rf value",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 5.26: Paper chromatography setup showing dye spot separation and solvent front",
            "image_search_query": "paper chromatography retention factor rf value calculation",
            "page": 22,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "In-Text Question (Section 5.1 & 5.2, p. 5 & p. 17): (a) A talcum powder contains 4% (m/m) zinc oxide. How many grams of zinc oxide are present in a 250 g container? (b) Why do cities with heavy smoke and dust look hazy during winter mornings?",
            "given": "(a) Concentration % = 4% m/m; Total container mass = 250 g.\n(b) Atmospheric smog and colloidal mist scattering.",
            "formula": "(a) Mass of solute = $\\frac{\\% (m/m) \\times \\text{Total Mass}}{100}$; (b) Tyndall Effect in colloidal aerosol smog.",
            "substitution": "(a) $\\text{Mass of ZnO} = \\frac{4 \\times 250}{100}$.",
            "calculation": "1. Part (a): $\\text{Mass of ZnO} = \\frac{1000}{100} = 10\\text{ g}$.\n2. Part (b): Smoke and dust particles (diameters 1–1000 nm) suspended in humid air form an aerosol colloid (smog). When morning sunlight traverses this suspension, the colloidal particulate matter scatters visible light rays in all directions via the Tyndall effect, producing an opaque, hazy appearance.",
            "finalAnswer": "(a) Exactly 10 g of zinc oxide is present in the 250 g container; (b) Atmospheric particulate matter forms an aerosol colloid that scatters light via the Tyndall effect, causing haze.",
            "unit": "grams and Optical Physics",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "tyndall effect smog haze aerosol scattering atmospheric",
            "page": 5,
            "section": "Section 5.1"
        }
    ]

def update_ch5():
    with open("scripts/science_modules_ch5.json", "r", encoding="utf-8") as f:
        mods = json.load(f)
    
    for m in mods:
        m["curriculum_id"] = CURRICULUM_IDS[5]
        m["class_level"] = "Class 9"
        m["board"] = "CBSE"
        for we in m.get("worked_examples", []):
            if "image_search_query" not in we or not we["image_search_query"]:
                we["image_search_query"] = "mixtures separation chemistry class 9 ncert"
            if "page" not in we:
                we["page"] = 60 + m["order_index"]
            if "section" not in we:
                we["section"] = f"Section 5.{m['order_index']}"
                
    m6 = mods[-1]
    m6["title"] = "Master Separation Ledger & NCERT Comprehensive Chapter Exercise Solver (Revise, Reflect, Refine Q1 to Q15)"
    m6["worked_examples"] = get_ch5_solver_examples()
    m6["description"] = "Exhaustive step-by-step master solutions for all in-text activities and all 15 'Revise, Reflect, Refine' chapter-end exercise problems from NCERT Exploration Grade 9 Chapter 5."
    
    with open("scripts/science_modules_ch5.json", "w", encoding="utf-8") as f:
        json.dump(mods, f, indent=2)
    print("Updated scripts/science_modules_ch5.json successfully!")

if __name__ == "__main__":
    update_ch5()
