#!/usr/bin/env python3
"""
Generator for Class 9 Science:
Chapter 5 (Mixtures & Separation) and Chapter 6 (Forces & Newton's Laws)
"""

import json

CH5_ID = "8d01a5f5-bf82-49c2-9fab-253d26b086f4"  # Exploring Mixtures (6 modules)
CH6_ID = "7e1d5438-1174-4577-8599-5f05a6642093"  # How Forces Affect Motion (6 modules)

# ==============================================================================
# CHAPTER 5: EXPLORING MIXTURES AND THEIR SEPARATION (6 MODULES)
# ==============================================================================
ch5_modules = [
    {
        "curriculum_id": CH5_ID,
        "order_index": 1,
        "title": "Classification of Matter: Pure Substances, Homogeneous & Heterogeneous Systems",
        "description": "Master the fundamental division of matter into pure substances (elements, compounds) and mixtures (homogeneous solutions vs heterogeneous suspensions and colloids).",
        "board": "CBSE",
        "class_level": "Class 9",
        "estimated_minutes": 20,
        "subtopics": [
            "Pure Substances: Elements (metals, non-metals, metalloids) and Compounds (fixed chemical composition)",
            "Mixtures: Variable proportions and retention of constituent properties",
            "Homogeneous Mixtures: Uniform composition throughout (True solutions, brass alloy)",
            "Heterogeneous Mixtures: Non-uniform composition with physically distinct phases (Sand in water, chalk powder)",
            "Activity 5.1: Comparative optical, filtration, and stability test across 4 groups"
        ],
        "key_concepts": [
            "Pure Substance Definition: Matter having invariant chemical composition and definite physical constants (melting/boiling points).",
            "Mixture Definition: Physical combination of two or more substances in any proportion where components retain their individual identities.",
            "Homogeneous System: Uniform single phase without visible boundaries of separation (e.g. Copper sulfate in water, brass).",
            "Heterogeneous System: Physically distinct parts with observable interfaces (e.g. Oil in water, chalk suspension).",
            "Activity 5.1 Group Testing: Differentiating true solution, suspension, and colloid by stability, filtration, and beam scattering."
        ],
        "success_criteria": "Student can classify any given substance as pure or mixture, distinguish homogeneous from heterogeneous systems, and deduce phase boundaries.",
        "chapter_notes": """### 5.1 The Architecture of Matter
All matter is fundamentally divided into:
1. **Pure Substances**:
   - **Elements**: Cannot be broken down into simpler substances by chemical reactions (Copper, Oxygen, Iron).
   - **Compounds**: Fixed composition composed of elements chemically combined in fixed proportion by mass (Water $H_2O$, Salt $NaCl$).
2. **Mixtures**:
   - Two or more pure substances combined physically without chemical bonding.
   - Constituents retain their individual properties and can be separated by physical methods.

### 5.2 Homogeneous vs Heterogeneous Mixtures
| Diagnostic Property | Homogeneous Mixture | Heterogeneous Mixture |
| :--- | :--- | :--- |
| **Composition** | Uniform throughout single phase | Non-uniform with distinct physical boundaries |
| **Particle Size** | $< 1\\text{ nm}$ (molecular level) | $> 1\\text{ nm}$ to $> 1000\\text{ nm}$ |
| **Visibility** | Particles cannot be seen under microscope | Particles often visible to naked eye or light microscope |
| **Filtration** | Passes through filter paper completely | Components can often be separated by filtration |
| **Examples** | Salt solution, Sugar syrup, Air, Brass ($70\\%\\text{ Cu} + 30\\%\\text{ Zn}$) | Muddy water, Chalk in water, Oil-water emulsion |""",
        "worked_examples": [
            {
                "problem": "Classify the following into elements, compounds, and mixtures: (a) Sodium, (b) Soil, (c) Sugar solution, (d) Silver, (e) Calcium carbonate, (f) Tin, (g) Silicon, (h) Coal, (i) Air, (j) Soap, (k) Methane, (l) Carbon dioxide, (m) Blood.",
                "given": "13 common substances from NCERT Exercise 5.",
                "formula": "Element: single atom type | Compound: fixed stoichiometric formula | Mixture: variable physical composition.",
                "substitution": "Elements: Na, Ag, Sn, Si; Compounds: CaCO3, CH4, CO2, Soap; Mixtures: Soil, Sugar solution, Coal, Air, Blood.",
                "calculation": "Sodium, Silver, Tin, Silicon are pure elemental symbols. Calcium carbonate (CaCO3), Methane (CH4), Carbon dioxide (CO2) have fixed stoichiometric bonds. Soil, air, blood, and solutions have variable proportions.",
                "finalAnswer": "Elements: Na, Ag, Sn, Si | Compounds: CaCO3, CH4, CO2, Soap | Mixtures: Soil, Sugar solution, Coal, Air, Blood.",
                "unit": "Chemical Classification",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 5.1: Homogeneous mixture vs Fig. 5.2: Heterogeneous mixture phase boundaries"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Air is a chemical compound because it has a specific density.",
                "correction": "Air is a homogeneous mixture because its constituent gases (N2, O2, Ar, CO2) retain their individual chemical properties, can be separated by physical fractional distillation, and have slightly variable humidity.",
                "why_it_matters": "A high-frequency diagnostic test question."
            }
        ],
        "visual_lesson_plan": {
            "title": "Classification of Matter Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Pure Substance Definition: Matter having invariant chemical composition and definite physical constants (melting/boiling points).",
                    "diagram_title": "Pure Substances vs Mixtures Taxonomy Tree",
                    "diagram_type": "image",
                    "image_query": "Classification of matter elements compounds mixtures diagram",
                    "video_query": "pure substances and mixtures chemistry",
                    "image_url": "/extracted_diagrams/ch5/fig_5_1.webp",
                    "what_to_make": "Classification tree branching from Matter into Pure Substances (Elements, Compounds) and Mixtures (Homogeneous, Heterogeneous).",
                    "timing_and_cue": "Mount classification tree on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_1.webp | Matter Taxonomy | Pure substances with fixed properties vs variable physical mixtures\")"
                },
                {
                    "concept_title": "Mixture Definition: Physical combination of two or more substances in any proportion where components retain their individual identities.",
                    "diagram_title": "Heterogeneous Phase Interface",
                    "diagram_type": "image",
                    "image_query": "Heterogeneous mixture distinct phases sand water microscope",
                    "video_query": "heterogeneous mixture examples",
                    "image_url": "/extracted_diagrams/ch5/fig_5_2.webp",
                    "what_to_make": "Microscopic view of heterogeneous mixture showing distinct phase boundaries between sand grains and water molecules.",
                    "timing_and_cue": "Mount heterogeneous interface on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_2.webp | Heterogeneous Interface | Observable physical boundaries between distinct constituent phases\")"
                },
                {
                    "concept_title": "Homogeneous System: Uniform single phase without visible boundaries of separation (e.g. Copper sulfate in water, brass).",
                    "diagram_title": "Homogeneous Copper Sulfate Solution",
                    "diagram_type": "image",
                    "image_query": "Copper sulfate solution homogeneous blue liquid beaker",
                    "video_query": "homogeneous copper sulfate solution",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/23/Copper_sulfate_solution.jpg",
                    "what_to_make": "Beaker of brilliant blue copper sulfate solution showing completely uniform single-phase color distribution.",
                    "timing_and_cue": "Mount homogeneous solution on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/2/23/Copper_sulfate_solution.jpg | Homogeneous Solution | Uniform molecular dissolution without phase boundaries\")"
                },
                {
                    "concept_title": "Heterogeneous System: Physically distinct parts with observable interfaces (e.g. Oil in water, chalk suspension).",
                    "diagram_title": "Oil and Water Immiscible Heterogeneous System",
                    "diagram_type": "image",
                    "image_query": "Oil and water emulsion heterogeneous two layers beaker",
                    "video_query": "oil and water immiscible mixture",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/73/Oil_and_water.jpg",
                    "what_to_make": "Two-phase system showing lower aqueous layer and upper lipid layer with sharp meniscus boundary.",
                    "timing_and_cue": "Mount oil-water on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/7/73/Oil_and_water.jpg | Two-Phase Heterogeneous System | Immiscible liquids maintaining sharp boundary interface\")"
                },
                {
                    "concept_title": "Activity 5.1 Group Testing: Differentiating true solution, suspension, and colloid by stability, filtration, and beam scattering.",
                    "diagram_title": "Activity 5.1 Four Groups Testing Matrix",
                    "diagram_type": "image",
                    "image_query": "Filtration and stability of mixture test beakers funnel",
                    "video_query": "activity 2.1 class 9 science mixtures",
                    "image_url": "/extracted_diagrams/ch5/fig_5_3.webp",
                    "what_to_make": "Four test beakers undergoing laser beam illumination, filtration, and undisturbed settling.",
                    "timing_and_cue": "Mount Activity 5.1 on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_3.webp | Activity 5.1 Testing Array | Comparing filtration, stability, and optical path across 4 mixtures\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each concept.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (Why salt dissolved in water seems to disappear completely, but chalk powder remains visible).
   - Stage 2: Definition of pure substances vs mixtures.
   - Stage 3: Common pitfall (Alloys like brass are homogeneous mixtures, not compounds).
   - Stage 4: Chalkboard classification table.
   - Stage 5: Socratic check: "Why is an alloy like brass classified as a mixture even though its components cannot be separated by physical filtration?" HARD STOP: Wait for student response!
   - Stage 6: Authentic CBSE classification question."""
    },
    {
        "curriculum_id": CH5_ID,
        "order_index": 2,
        "title": "True Solutions, Solubility Dynamics & Concentration Mathematics",
        "description": "Master the physical chemistry of true solutions: solvent/solute dynamics, saturation points, effect of temperature on solubility, and mathematical concentration calculations (Mass %, Volume %, Mass-by-Volume %).",
        "board": "CBSE",
        "class_level": "Class 9",
        "estimated_minutes": 20,
        "subtopics": [
            "Solution Anatomy: Solute (minor dispersed component) and Solvent (major dissolving medium)",
            "Types of Solutions: Solid-liquid (tincture of iodine), Gas-liquid (soda water), Gas-gas (air), Solid-solid (alloys)",
            "Properties of True Solutions: Particle size < 1 nm, homogeneous, stable, passes through filter paper, zero Tyndall effect",
            "Saturated, Unsaturated, and Supersaturated Solutions: Dynamic equilibrium at given temperature",
            "Solubility: Maximum grams of solute that dissolve in 100 g of solvent at specified temperature",
            "Concentration Formulas: Mass %, Volume %, and Mass-by-Volume % calculations"
        ],
        "key_concepts": [
            "Solution Components: Solute (dissolved substance) + Solvent (dissolving medium) = Solution.",
            "Nanoscale Dimension: True solution solute particles are smaller than 1 nanometer (10^-9 m) and do not scatter light.",
            "Saturation Dynamic: A solution in which no more solute can be dissolved at that specific temperature is called a saturated solution.",
            "Thermal Effect on Solubility: Solubility of solid solutes generally increases with temperature; cooling a saturated solution causes crystallization.",
            "Concentration by Mass %: (Mass of solute / Total mass of solution) * 100.",
            "Concentration by Volume %: (Volume of solute / Total volume of solution) * 100."
        ],
        "success_criteria": "Student can define solute/solvent pairs for uncommon solutions (e.g. tincture of iodine), explain thermal solubility shifts, and solve 100% of NCERT concentration numericals.",
        "chapter_notes": """### 5.3 Anatomy of a True Solution
A solution is a **homogeneous mixture** of two or more substances.
$$\\text{Solute (Minor component)} + \\text{Solvent (Major component)} = \\text{Solution}$$

### 5.4 Unique Solution Examples
- **Tincture of Iodine**: Solute = Solid Iodine ($I_2$), Solvent = Alcohol (Ethanol).
- **Aerated Drinks (Soda)**: Solute = Carbon dioxide gas ($CO_2$), Solvent = Water.
- **Air**: Solute = Oxygen ($21\\%$) and other gases, Solvent = Nitrogen ($78\\%$).
- **Brass**: Solute = Zinc ($30\\%$), Solvent = Copper ($70\\%$).

### 5.5 Saturated vs Unsaturated Solutions
- **Saturated Solution**: A solution in which **no more solute can be dissolved** at a given temperature.
- **Solubility**: The amount of solute present in the saturated solution at this temperature (measured in $\\text{g}$ per $100\\text{ g}$ of solvent).
- **Effect of Temperature**:
  * Increasing temperature increases solubility of solid solutes (more thermal agitation creates larger intermolecular spaces).
  * If a hot saturated solution is cooled down slowly, excess solute precipitates out as pure **crystals**.

### 5.6 Mathematical Concentration Formulas
$$\\text{Mass by Mass \\%} = \\frac{\\text{Mass of Solute}}{\\text{Mass of Solution}} \\times 100 = \\frac{\\text{Mass of Solute}}{\\text{Mass of Solute} + \\text{Mass of Solvent}} \\times 100$$
$$\\text{Mass by Volume \\%} = \\frac{\\text{Mass of Solute}}{\\text{Volume of Solution}} \\times 100$$
$$\\text{Volume by Volume \\%} = \\frac{\\text{Volume of Solute}}{\\text{Volume of Solution}} \\times 100$$""",
        "worked_examples": [
            {
                "problem": "A solution contains 40 g of common salt in 320 g of water. Calculate the concentration in terms of mass by mass percentage of the solution.",
                "given": "Mass of solute (salt) = 40 g; Mass of solvent (water) = 320 g.",
                "formula": "Mass % = [Mass of solute / (Mass of solute + Mass of solvent)] * 100.",
                "substitution": "Mass of solution = 40 + 320 = 360 g; Mass % = (40 / 360) * 100.",
                "calculation": "1. Mass of solution = 40 + 320 = 360 g.\\n2. Mass % = (40 / 360) * 100 = (1 / 9) * 100 = 11.11%.",
                "finalAnswer": "Concentration of the salt solution = 11.11% (mass by mass).",
                "unit": "Percentage (%)",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 5.4: Mass by mass percentage formula calculation layout"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "In the concentration formula denominator, you divide only by the mass of water (solvent).",
                "correction": "You MUST divide by the mass of the TOTAL SOLUTION (Solute + Solvent = 40 + 320 = 360 g), not just the solvent.",
                "why_it_matters": "The single most frequent calculation error on CBSE exams."
            }
        ],
        "visual_lesson_plan": {
            "title": "True Solutions & Concentration Mathematics Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Solution Components: Solute (dissolved substance) + Solvent (dissolving medium) = Solution.",
                    "diagram_title": "Solute and Solvent Dissolution Model",
                    "diagram_type": "image",
                    "image_query": "Solute solvent solution dissolution particles diagram chemistry",
                    "video_query": "how solutions form chemistry solute solvent",
                    "image_url": "/extracted_diagrams/ch5/fig_5_4.webp",
                    "what_to_make": "Microscopic diagram showing solid solute lattice dissolving into solvent liquid molecules.",
                    "timing_and_cue": "Mount dissolution model on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_4.webp | Solution Dissolution | Solute particles completely dispersed in solvent molecular matrix\")"
                },
                {
                    "concept_title": "Nanoscale Dimension: True solution solute particles are smaller than 1 nanometer (10^-9 m) and do not scatter light.",
                    "diagram_title": "Sub-Nanometer Particle Scale",
                    "diagram_type": "image",
                    "image_query": "Nanometer scale true solution colloid suspension particle size diagram",
                    "video_query": "particle size in solutions colloids suspensions",
                    "image_url": "/extracted_diagrams/ch5/fig_5_5.webp",
                    "what_to_make": "Logarithmic scale comparison showing true solution (< 1 nm), colloid (1-100 nm), and suspension (> 100 nm).",
                    "timing_and_cue": "Mount scale on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_5.webp | Particle Scale | Solute particles < 1 nm cannot scatter visible light photons\")"
                },
                {
                    "concept_title": "Saturation Dynamic: A solution in which no more solute can be dissolved at that specific temperature is called a saturated solution.",
                    "diagram_title": "Saturated Solution Dynamic Equilibrium",
                    "diagram_type": "image",
                    "image_query": "Saturated unsaturated solution dynamic equilibrium diagram",
                    "video_query": "saturated and unsaturated solutions chemistry",
                    "image_url": "/extracted_diagrams/ch5/fig_5_6.webp",
                    "what_to_make": "Beaker showing undissolved solute crystals at bottom in dynamic equilibrium with dissolved solute ions.",
                    "timing_and_cue": "Mount saturation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_6.webp | Saturation Equilibrium | Rate of dissolution equals rate of precipitation\")"
                },
                {
                    "concept_title": "Thermal Effect on Solubility: Solubility of solid solutes generally increases with temperature; cooling a saturated solution causes crystallization.",
                    "diagram_title": "Solubility Curves vs Temperature",
                    "diagram_type": "image",
                    "image_query": "Solubility curve temperature graph KNO3 NaCl chemistry",
                    "video_query": "solubility curves chemistry explained",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Solubility_curves.svg",
                    "what_to_make": "Solubility graph plotting grams of solute per 100g water vs temperature for KNO3, NaCl, and CuSO4.",
                    "timing_and_cue": "Mount solubility curves on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/ec/Solubility_curves.svg | Thermal Solubility Curves | Solute capacity expanding with temperature for solid salts\")"
                },
                {
                    "concept_title": "Concentration by Mass %: (Mass of solute / Total mass of solution) * 100.",
                    "diagram_title": "Mass by Mass Concentration Card",
                    "diagram_type": "image",
                    "image_query": "Mass percentage concentration formula chemistry card",
                    "video_query": "how to calculate mass percent concentration",
                    "image_url": "/extracted_diagrams/ch5/fig_5_4.webp",
                    "what_to_make": "Formula card emphasizing Total Mass of Solution = Solute + Solvent in denominator.",
                    "timing_and_cue": "Mount mass percent card on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_4.webp | Mass Percent Formula | Mass % = (m_solute / m_total_solution) * 100\")"
                },
                {
                    "concept_title": "Concentration by Volume %: (Volume of solute / Total volume of solution) * 100.",
                    "diagram_title": "Volume by Volume Concentration in Saline/Alcohol",
                    "diagram_type": "image",
                    "image_query": "Volume percent concentration alcohol in water graduated cylinder",
                    "video_query": "volume percent concentration chemistry",
                    "image_url": "/extracted_diagrams/ch5/fig_5_5.webp",
                    "what_to_make": "Graduated cylinder showing volume by volume solution mixing and meniscus reading.",
                    "timing_and_cue": "Mount volume percent on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_5.webp | Volume Percent Formula | Vol % = (V_solute / V_solution) * 100\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each concept.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (Why sugar dissolves faster in hot tea than cold iced water).
   - Stage 2: Definitions of solute, solvent, saturated, unsaturated, and solubility.
   - Stage 3: Common pitfall (Dividing by solvent mass instead of total solution mass).
   - Stage 4: Chalkboard layout: Given -> Formula -> Substitution -> Calculation -> Boxed Answer.
   - Stage 5: Socratic check: "If a hot saturated salt solution is cooled down to room temperature, what will you observe at the bottom of the beaker?" HARD STOP: Wait for student response!
   - Stage 6: Authentic CBSE numerical question."""
    },
    {
        "curriculum_id": CH5_ID,
        "order_index": 3,
        "title": "Suspensions, Colloidal Dispersions & The Optical Tyndall Effect",
        "description": "Master intermediate heterogeneous systems: unstable coarse suspensions, permanently dispersed colloids, Brownian motion, the 8-class colloidal taxonomy table, and the optical physics of the Tyndall effect.",
        "board": "CBSE",
        "class_level": "Class 9",
        "estimated_minutes": 20,
        "subtopics": [
            "Suspensions: Heterogeneous, particle size > 100 nm, unstable sedimentation, filtration separation",
            "Colloidal Dispersions: Intermediate particle size (1 nm - 100 nm), heterogeneous appearing homogeneous, stable",
            "The Tyndall Effect: Scattering of a light beam by colloidal particles making the path of light visible",
            "Brownian Motion: Continuous erratic zig-zag bombardment by solvent molecules preventing sedimentation",
            "The 8 Colloidal Classes: Dispersed Phase vs Dispersion Medium (Sol, Gel, Emulsion, Aerosol, Foam)",
            "Everyday Colloids: Milk, fog, clouds, smoke, shaving cream, jelly, butter, cheese"
        ],
        "key_concepts": [
            "Suspension Instability: Suspended particles settle down under gravity when left undisturbed; filtration separates them.",
            "Colloid Stability: Colloidal particles do not settle because continuous Brownian thermal impacts overcome gravity.",
            "Tyndall Scattering Physics: Colloidal particles are large enough (1-100 nm) to scatter visible light wavelengths, illuminating the beam path.",
            "Dispersed Phase vs Dispersion Medium: Dispersed phase = solute-like component; Dispersion medium = solvent-like continuous phase.",
            "The 8 Colloidal Classes Table: Master taxonomy pairing phases (Liquid in gas = Aerosol/fog; Liquid in liquid = Emulsion/milk; Solid in liquid = Sol/paint).",
            "Forest Canopy Tyndall Effect: Sunlight passing through tree mist where fine water droplets scatter rays in a dense forest."
        ],
        "success_criteria": "Student can contrast solutions, colloids, and suspensions across 6 physical parameters, classify any colloid using the 8-class table, and explain the Tyndall effect.",
        "chapter_notes": """### 5.7 Suspensions
A **heterogeneous mixture** in which the solute particles do not dissolve but remain suspended throughout the bulk of the medium.
- **Particle Size**: $> 100\\text{ nm}$ (visible to naked eye).
- **Stability**: **Unstable** (particles settle down under gravity when left undisturbed).
- **Filtration**: Can be separated by ordinary filter paper.
- **Tyndall Effect**: Scatters light while particles are suspended; stops scattering once settled.

### 5.8 Colloidal Solutions (Colloids)
A **heterogeneous system** that appears homogeneous to the naked eye.
- **Particle Size**: Intermediate between true solutions and suspensions ($1\\text{ nm} - 100\\text{ nm}$).
- **Stability**: **Very stable** (particles never settle down due to **Brownian motion**).
- **Filtration**: Passes through ordinary filter paper; cannot be separated by filtration (requires centrifugation).
- **Tyndall Effect**: **Strongly scatters light**, making the illuminated light beam clearly visible!

### 5.9 Master Comparison: Solution vs Colloid vs Suspension
| Property | True Solution | Colloidal Solution | Suspension |
| :--- | :--- | :--- | :--- |
| **Nature** | Homogeneous | Heterogeneous (appears homogeneous) | Heterogeneous |
| **Particle Size** | $< 1\\text{ nm}$ | $1\\text{ nm} - 100\\text{ nm}$ | $> 100\\text{ nm}$ |
| **Stability** | Completely stable | Very stable | **Unstable** (sediments) |
| **Filtration** | Passes through filter paper | Passes through filter paper | **Separated by filtration** |
| **Tyndall Effect** | **Negative** (No scattering) | **Positive** (Strong scattering) | Positive (temporary until settled) |
| **Examples** | Salt solution, Sugar syrup | Milk, Fog, Starch in water, Ink | Muddy water, Chalk powder in water |

### 5.10 Master Colloidal Taxonomy Table (The 8 Classes)
| Dispersed Phase | Dispersion Medium | Colloidal Type | Common Examples |
| :--- | :--- | :--- | :--- |
| Liquid | Gas | **Aerosol** | Fog, clouds, mist |
| Solid | Gas | **Aerosol** | Smoke, automobile exhaust |
| Gas | Liquid | **Foam** | Shaving cream |
| Liquid | Liquid | **Emulsion** | Milk, face cream |
| Solid | Liquid | **Sol** | Milk of magnesia, mud |
| Gas | Solid | **Foam** | Sponge, pumice stone |
| Liquid | Solid | **Gel** | Jelly, cheese, butter |
| Solid | Solid | **Solid Sol** | Coloured gemstone, milky glass |""",
        "worked_examples": [
            {
                "problem": "Explain why a beam of light passing through a glass beaker containing milk is illuminated and visible, but the same beam passing through a salt solution is completely dark and invisible.",
                "given": "Beaker A = Milk (colloid); Beaker B = Salt solution (true solution).",
                "formula": "The Tyndall Effect (Rayleigh/Mie scattering based on particle diameter).",
                "substitution": "Colloid particle size 1-100 nm vs True solution particle size < 1 nm.",
                "calculation": "1. In milk, fat droplets and protein micelles have dimensions between 1 nm and 100 nm. These dimensions are comparable to the wavelength of visible light (~400-700 nm). When photons collide with these colloidal particles, the light is scattered in all directions, illuminating the beam path (Tyndall Effect).\\n2. In a salt solution, the sodium (Na+) and chloride (Cl-) ions are sub-nanometer (< 1 nm). They are far too small to scatter visible light wavelengths; the light passes straight through without deviation, leaving the beam invisible.",
                "finalAnswer": "Milk scatters light because its colloidal particles (1-100 nm) cause the Tyndall effect; salt solution particles (< 1 nm) are too small to scatter light.",
                "unit": "Optical Physics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 5.3: Passing laser light through salt solution (invisible path) vs colloid/milk (visible Tyndall cone)"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Milk is a true solution because it looks completely uniform and white.",
                "correction": "Milk is an EMULSION (liquid fat droplets dispersed in liquid water). It is heterogeneous; under a light microscope, distinct fat globules are clearly visible.",
                "why_it_matters": "A standard trick question in CBSE Class 9 chemistry."
            }
        ],
        "visual_lesson_plan": {
            "title": "Suspensions, Colloids & Tyndall Effect Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Suspension Instability: Suspended particles settle down under gravity when left undisturbed; filtration separates them.",
                    "diagram_title": "Suspension Sedimentation & Filtration",
                    "diagram_type": "image",
                    "image_query": "Chalk water suspension sedimentation beaker filter funnel diagram",
                    "video_query": "suspension settling sedimentation chemistry",
                    "image_url": "/extracted_diagrams/ch5/fig_5_7.webp",
                    "what_to_make": "Beaker of muddy suspension showing coarse particles settling to bottom and clear supernatant liquid above.",
                    "timing_and_cue": "Mount suspension on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_7.webp | Suspension Sedimentation | Coarse particles (> 100 nm) settling under gravity\")"
                },
                {
                    "concept_title": "Colloid Stability: Colloidal particles do not settle because continuous Brownian thermal impacts overcome gravity.",
                    "diagram_title": "Brownian Motion in Colloidal Sol",
                    "diagram_type": "image",
                    "image_query": "Brownian motion zig zag particle trajectory colloid diagram",
                    "video_query": "brownian motion microscope colloidal particles",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/30/Brownian_motion_large.gif",
                    "what_to_make": "Erratic zig-zag trajectory of colloidal particle buffeted by invisible thermal collisions with solvent molecules.",
                    "timing_and_cue": "Mount Brownian motion on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/3/30/Brownian_motion_large.gif | Brownian Motion | Continuous thermal impacts preventing colloidal sedimentation\")"
                },
                {
                    "concept_title": "Tyndall Scattering Physics: Colloidal particles are large enough (1-100 nm) to scatter visible light wavelengths, illuminating the beam path.",
                    "diagram_title": "Laser Beam Tyndall Scattering in Colloid",
                    "diagram_type": "image",
                    "image_query": "Tyndall effect laser beam through solution and colloid beaker photo",
                    "video_query": "tyndall effect laser light experiment",
                    "image_url": "/extracted_diagrams/ch5/fig_5_3.webp",
                    "what_to_make": "Side-by-side comparison of red laser beam passing invisibly through copper sulfate but brightly illuminating milk colloid.",
                    "timing_and_cue": "Mount Tyndall effect on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_3.webp | Tyndall Optical Cone | Colloid particles (1-100 nm) scattering visible light photons\")"
                },
                {
                    "concept_title": "Dispersed Phase vs Dispersion Medium: Dispersed phase = solute-like component; Dispersion medium = solvent-like continuous phase.",
                    "diagram_title": "Colloidal Component Architecture",
                    "diagram_type": "image",
                    "image_query": "Dispersed phase dispersion medium colloid diagram",
                    "video_query": "dispersed phase dispersion medium chemistry",
                    "image_url": "/extracted_diagrams/ch5/fig_5_8.webp",
                    "what_to_make": "Diagram showing microscopic micelles of dispersed phase suspended in continuous dispersion medium.",
                    "timing_and_cue": "Mount colloidal components on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_8.webp | Colloidal Architecture | Dispersed Phase (solute analog) in Dispersion Medium (solvent analog)\")"
                },
                {
                    "concept_title": "The 8 Colloidal Classes Table: Master taxonomy pairing phases (Liquid in gas = Aerosol/fog; Liquid in liquid = Emulsion/milk; Solid in liquid = Sol/paint).",
                    "diagram_title": "Master 8 Colloidal Types Chart",
                    "diagram_type": "image",
                    "image_query": "Types of colloids table aerosol foam emulsion sol gel",
                    "video_query": "8 types of colloids classification table",
                    "image_url": "/extracted_diagrams/ch5/fig_5_9.webp",
                    "what_to_make": "NCERT 8-colloid master matrix pairing phase states with everyday consumer examples.",
                    "timing_and_cue": "Mount colloid table on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_9.webp | Master Colloid Taxonomy | Aerosol, Foam, Emulsion, Sol, and Gel classifications\")"
                },
                {
                    "concept_title": "Forest Canopy Tyndall Effect: Sunlight passing through tree mist where fine water droplets scatter rays in a dense forest.",
                    "diagram_title": "Sunlight Beams in Misty Forest Canopy",
                    "diagram_type": "image",
                    "image_query": "Sunlight rays through forest canopy mist Tyndall effect photo",
                    "video_query": "sunlight rays in forest mist tyndall effect",
                    "image_url": "/extracted_diagrams/ch5/fig_5_10.webp",
                    "what_to_make": "Sunbeams streaming through dark canopy of forest scattered by tiny atmospheric water droplet aerosols.",
                    "timing_and_cue": "Mount forest canopy on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_10.webp | Natural Tyndall Effect | Sunbeams illuminated by mist droplet aerosol in dense forest\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each concept.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (Why you can see sunbeams streaming through a dusty room or forest canopy).
   - Stage 2: Definition of Tyndall effect and Brownian motion.
   - Stage 3: Common pitfall (Milk is an emulsion/colloid, not a true solution).
   - Stage 4: Chalkboard 8-class colloidal taxonomy table.
   - Stage 5: Socratic check: "Why do colloidal particles never settle to the bottom of the container like sand particles in water?" HARD STOP: Wait for student response!
   - Stage 6: Authentic CBSE classification question."""
    }
]

print(f"Synthesized Chapter 5 partial: {len(ch5_modules)} modules.")

output_path_ch5 = "scripts/science_modules_ch5.json"
with open(output_path_ch5, "w", encoding="utf-8") as f:
    json.dump(ch5_modules, f, indent=2, ensure_ascii=False)
print(f"Saved Chapter 5 modules to {output_path_ch5}")
