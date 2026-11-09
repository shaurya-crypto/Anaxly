import json
import os

CH5_ID = '8d01a5f5-bf82-49c2-9fab-253d26b086f4'
CH6_ID = '7e1d5438-1174-4577-8599-5f05a6642093'
CH7_ID = 'da5625a5-7071-4533-8667-13da4c28abda'
CH8_ID = '8be782c9-c0d3-425e-bb81-c18c298dc4a7'

# Load existing ch5Modules from node script or define them cleanly
# Let's define the comprehensive modules for chapters 5, 6, 7, 8 in python data structures

all_modules = []

# --- CHAPTER 5 ---
ch5 = [
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
      "Pure Substance: Matter having invariant chemical composition and definite physical constants (melting/boiling points).",
      "Mixture: Combination of two or more substances in any proportion where components retain their individual identities.",
      "Homogeneous System: Uniform phase without visible boundaries of separation (e.g. Copper sulfate in water).",
      "Heterogeneous System: Physically distinct parts with observable interfaces (e.g. Oil in water, chalk in water)."
    ],
    "success_criteria": "Student can classify any given substance as pure or mixture, distinguish homogeneous from heterogeneous systems, and deduce their phase characteristics.",
    "chapter_notes": """### 5.1 The Architecture of Matter
All matter is fundamentally divided into:
1. **Pure Substances**:
   - **Elements**: Cannot be broken down into simpler substances by chemical reactions (e.g. Copper, Oxygen, Iron).
   - **Compounds**: Fixed composition composed of elements combined in a fixed ratio by mass (e.g. Water H2O, Salt NaCl).
2. **Mixtures**:
   - Two or more pure substances combined physically without chemical bonding.
   - Constituents retain their individual properties and can be separated by physical methods.

### 5.2 Homogeneous vs Heterogeneous Mixtures
| Property | Homogeneous Mixture | Heterogeneous Mixture |
| :--- | :--- | :--- |
| **Composition** | Uniform throughout single phase | Non-uniform with distinct boundaries |
| **Particle Size** | < 1 nm (molecular level) | > 1 nm to > 1000 nm |
| **Visibility** | Particles cannot be seen even under microscope | Particles often visible to naked eye or microscope |
| **Filtration** | Passes through filter paper completely | Components can often be separated by filtration |
| **Examples** | Salt solution, Sugar syrup, Air, Brass (70% Cu + 30% Zn) | Muddy water, Chalk in water, Oil-water emulsion |""",
    "worked_examples": [
      {
        "problem": "Classify the following into elements, compounds, and mixtures: (a) Sodium, (b) Soil, (c) Sugar solution, (d) Silver, (e) Calcium carbonate, (f) Tin, (g) Silicon, (h) Coal, (i) Air, (j) Soap, (k) Methane, (l) Carbon dioxide, (m) Blood.",
        "given": "13 common substances from NCERT Exercise 5.",
        "formula": "Element: single atom type | Compound: fixed chemical formula | Mixture: variable physical mix",
        "substitution": "Elements: Na, Ag, Sn, Si; Compounds: CaCO3, CH4, CO2, Soap; Mixtures: Soil, Sugar solution, Coal, Air, Blood",
        "calculation": "Sodium, Silver, Tin, Silicon are pure elemental symbols. Calcium carbonate (CaCO3), Methane (CH4), Carbon dioxide (CO2) have fixed stoichiometric bonds. Soil, air, blood, and solutions have variable proportions.",
        "finalAnswer": "Elements: Na, Ag, Sn, Si | Compounds: CaCO3, CH4, CO2, Soap | Mixtures: Soil, Sugar solution, Coal, Air, Blood",
        "unit": "Chemical Classification"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Air is a compound because it contains oxygen and nitrogen.",
        "correction": "Air is a homogeneous mixture because its constituent gases (N2 78%, O2 21%, Ar 0.9%, CO2 0.04%) retain their individual chemical properties and can be separated by fractional distillation.",
        "why_it_matters": "Compounds have fixed ratios and new chemical properties; mixtures retain constituent identities."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Classification of Matter Tree Flowchart",
      "diagram_type": "flowchart",
      "concept_visuals": [
        {
          "concept_title": "Pure Substances vs Mixtures Taxonomy",
          "diagram_title": "Matter Classification Flowchart",
          "diagram_type": "flowchart",
          "what_to_make": "Matter -> Pure Substances | Mixtures; Pure Substances -> Elements | Compounds; Mixtures -> Homogeneous Solutions | Heterogeneous Suspensions and Colloids",
          "timing_and_cue": "Mount matter classification flowchart on Step 1: write_chalkboard(action=\"draw_flowchart\", content=\"Matter -> Pure Substances | Mixtures; Pure Substances -> Elements | Compounds; Mixtures -> Homogeneous Solutions | Heterogeneous Suspensions and Colloids\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, call write_chalkboard(action=\"draw_flowchart\", content=\"Matter -> Pure Substances | Mixtures; Pure Substances -> Elements | Compounds; Mixtures -> Homogeneous Solutions | Heterogeneous Suspensions and Colloids\").\n2. 6-STAGE SOCRATIC CADENCE: Real-life hook -> Formal definition -> Common pitfall -> Tabular comparison -> Socratic check -> Authentic CBSE board exam question."
  },
  {
    "curriculum_id": CH5_ID,
    "order_index": 2,
    "title": "True Solutions, Solubility Dynamics & Concentration Mathematics",
    "description": "Understand solute-solvent interactions, saturated vs unsaturated states, temperature dependence of solubility, and calculate mass by mass and mass by volume percentage concentrations.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Components of a Solution: Solvent (dissolving medium) and Solute (substance dissolved)",
      "Properties of True Solutions: Particle diameter < 1 nm (10^-9 m), non-scattering of light, non-sedimenting",
      "Saturated, Unsaturated, and Supersaturated Solutions",
      "Solubility: Maximum grams of solute dissolved in 100 g solvent at specified temperature",
      "Mathematical Expressions of Concentration: Mass %, Volume %, Mass-by-Volume %"
    ],
    "key_concepts": [
      "Solvent: Component present in largest amount that determines physical state of solution.",
      "Saturated Solution: Solution in which no more solute can be dissolved at that specific temperature.",
      "Solubility: Mass in grams of solute required to saturate 100 g of solvent at given temperature.",
      "Mass Percentage: Mass % = (Mass of solute / Mass of solution) * 100"
    ],
    "success_criteria": "Student can solve any NCERT concentration numerical, distinguish saturated from unsaturated states, and interpret solubility-temperature curves.",
    "chapter_notes": """### 5.3 Nature of True Solutions
A **solution** is a homogeneous mixture of two or more substances:
- **Solute**: Dispersed component (smaller quantity, e.g. salt).
- **Solvent**: Continuous dissolving medium (larger quantity, e.g. water).

### 5.4 Saturated vs Unsaturated State
- **Unsaturated Solution**: Can dissolve more solute at the given temperature.
- **Saturated Solution**: Contains maximum amount of dissolved solute at that temperature.
- **Effect of Temperature**:
  - Increasing temperature increases solubility of most solids.
  - Cooling a hot saturated solution leads to crystallization of excess solute.

### 5.5 Concentration Formulas
1. **Mass by Mass Percentage**:
   Mass % = (Mass of Solute / Mass of Solution) * 100
2. **Mass by Volume Percentage**:
   Mass/Vol % = (Mass of Solute in g / Volume of Solution in mL) * 100""",
    "worked_examples": [
      {
        "problem": "A solution contains 40 g of common salt in 320 g of water. Calculate the concentration in terms of mass by mass percentage of the solution.",
        "given": "Mass of solute (salt) = 40 g | Mass of solvent (water) = 320 g",
        "formula": "Mass of Solution = Mass of Solute + Mass of Solvent; Concentration = (Mass of Solute / Mass of Solution) * 100",
        "substitution": "Mass of Solution = 40 g + 320 g = 360 g; Conc = (40 / 360) * 100",
        "calculation": "40 / 360 = 1 / 9 = 0.1111...; 0.1111 * 100 = 11.11%",
        "finalAnswer": "11.11% (w/w)",
        "unit": "Percentage"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "The mass of the solution is just the mass of the water.",
        "correction": "Mass of solution = Mass of solute + Mass of solvent! If 40 g salt is in 320 g water, the solution mass is 360 g, NOT 320 g.",
        "why_it_matters": "Dividing 40 by 320 gives 12.5%, which loses full marks on CBSE board exams; correct is 40/360 = 11.1%."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Solubility vs Temperature Curves Graph",
      "diagram_type": "graph",
      "concept_visuals": [
        {
          "concept_title": "Temperature Dependence of Salt Solubility",
          "diagram_title": "Solubility vs Temperature Dynamic Graph",
          "diagram_type": "graph",
          "what_to_make": "Mafs interactive coordinate plot of Solubility (g/100g water) vs Temperature (Celsius)",
          "timing_and_cue": "Mount solubility curves graph on Step 1: plot_mathematical_graph(formula=\"0.8*x + 20\", domain=\"[0, 100]\", range=\"[0, 120]\", title=\"Solubility of Salts vs Temperature (Celsius)\", callout=\"Solubility rises sharply with temperature\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, call plot_mathematical_graph(formula=\"0.8*x + 20\", domain=\"[0, 100]\", range=\"[0, 120]\", title=\"Solubility vs Temperature (Celsius)\", callout=\"Endothermic salt dissolution rises with temperature\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH5_ID,
    "order_index": 3,
    "title": "Suspensions, Colloidal Dispersions & The Optical Tyndall Effect",
    "description": "Differentiate true solutions from suspensions and colloids, understand dispersed phase vs dispersion medium, and unpack Brownian motion and Tyndall scattering.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Suspensions: Heterogeneous, visible particles (> 1000 nm), unstable, separates upon standing",
      "Colloids: Intermediate size (1 to 1000 nm), appears homogeneous but is heterogeneous, stable",
      "Components of Colloid: Dispersed Phase (solute analogue) and Dispersion Medium (solvent analogue)",
      "The Tyndall Effect: Scattering of a light beam by colloidal particles making path visible",
      "Classification Table 5.1: Aerosol, Foam, Emulsion, Sol, Gel, Solid Sol with real-world examples"
    ],
    "key_concepts": [
      "Suspension: Heterogeneous mixture where solute particles do not dissolve but remain suspended throughout bulk medium.",
      "Colloid: Heterogeneous mixture where particle size is between 1 nm and 1000 nm, passing through filter paper without settling.",
      "Tyndall Effect: Optical phenomenon where colloidal particles scatter light rays, rendering beam path visible."
    ],
    "success_criteria": "Student can distinguish the 3 states of dispersion, identify dispersed phase and medium in any common colloid, and explain Tyndall scattering.",
    "chapter_notes": """### 5.6 The Trio of Liquid Systems
| Feature | True Solution | Colloid | Suspension |
| :--- | :--- | :--- | :--- |
| **Particle Size** | < 1 nm | 1 nm - 1000 nm | > 1000 nm |
| **Nature** | Homogeneous | Heterogeneous | Heterogeneous |
| **Stability** | Completely stable | Stable | Unstable (settles) |
| **Filtration** | Passes through filter | Passes through filter | Retained on filter |
| **Tyndall Effect**| Negative | Positive (scatters light) | Variable |

### 5.7 The Tyndall Effect
When a fine beam of light passes through a colloidal solution:
- Colloidal particles have dimensions comparable to wavelengths of visible light (400-700 nm).
- The particles absorb and re-radiate light in all directions, illuminating the path of the beam.""",
    "worked_examples": [
      {
        "problem": "Which of the following will show the Tyndall effect? (a) Salt solution, (b) Milk, (c) Copper sulfate solution, (d) Starch solution.",
        "given": "Four test mixtures from NCERT Question 2.",
        "formula": "Tyndall effect is exhibited ONLY by colloidal dispersions and unstable suspensions with particle size 1-1000 nm.",
        "substitution": "Salt solution = true solution (<1 nm, no); Milk = colloid (fat in water, yes); CuSO4 = true solution (no); Starch solution = colloid (yes).",
        "calculation": "Salt and copper sulfate dissolve into individual ions < 1 nm. Milk and starch form colloidal micelles that scatter light.",
        "finalAnswer": "Milk and Starch solution will exhibit the Tyndall effect.",
        "unit": "Optical Verification"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Milk is a true homogeneous solution because it looks completely white and smooth.",
        "correction": "Milk is a heterogeneous colloidal emulsion of liquid butterfat globules dispersed in aqueous liquid. Under a microscope, distinct fat droplets are clearly visible.",
        "why_it_matters": "CBSE questions frequently test why milk scatters laser light while sugar water does not."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Tyndall Effect in Colloids vs True Solutions",
      "diagram_type": "image",
      "concept_visuals": [
        {
          "concept_title": "Laser Beam Scattering in Colloid vs True Solution",
          "diagram_title": "Tyndall Effect Optical Scattering",
          "diagram_type": "image",
          "image_search_query": "Tyndall effect colloid laser beam true solution",
          "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Tyndall_cube.jpg",
          "what_to_make": "Photograph of laser beam passing invisibly through a true solution on left, and producing a brilliant illuminated path through a colloidal solution on right.",
          "timing_and_cue": "Mount authentic Tyndall effect photo on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/ec/Tyndall_cube.jpg | Tyndall Optical Scattering | Invisible beam in true solution vs brilliant illuminated beam path in colloidal dispersion\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount authentic Tyndall effect photo: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/ec/Tyndall_cube.jpg | Tyndall Effect | Laser beam invisible in solution, scattered in colloid\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH5_ID,
    "order_index": 4,
    "title": "Separation Mechanics I: Solid-Solid & Insoluble Solid-Liquid Mixtures",
    "description": "Master practical laboratory separation techniques including filtration, decantation, crystallization of copper sulfate, and sublimation of volatile substances.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Principles of Separation: Exploiting differences in physical properties (density, solubility, volatility)",
      "Filtration & Decantation: Apparatus setup, filter cone folding, residue vs filtrate",
      "Evaporation to Dryness vs Crystallization: Why crystallization is superior (prevents thermal decomposition)",
      "Activity 5.3: Preparation of pure Copper Sulfate crystals from impure commercial sample",
      "Sublimation: Solid-to-gas phase transition (Ammonium chloride, Camphor, Naphthalene, Anthracene)"
    ],
    "key_concepts": [
      "Filtration: Separation of insoluble solid particles from a liquid using a porous barrier.",
      "Crystallization: Process that separates a pure solid in the form of crystals from a hot saturated solution upon slow cooling.",
      "Sublimation: Direct transition of a solid into vapor phase on heating without passing through the intermediate liquid state."
    ],
    "success_criteria": "Student can design separation apparatus workflows, explain why crystallization is superior to evaporation, and sketch sublimation setups.",
    "chapter_notes": """### 5.8 Solid-Liquid Separation Techniques
1. **Filtration**: Insoluble solid is retained on filter paper as **residue**; clear liquid passing through is **filtrate**.
2. **Crystallization**:
   - Why superior to simple evaporation to dryness?
     1. Some solids decompose or char (like sugar) on heating to dryness.
     2. Soluble impurities remain dissolved in mother liquor, yielding pure crystals.
3. **Sublimation**: Applicable when one component is **sublimable** (volatile solid) and other is non-sublimable (e.g. NH4Cl, Camphor, Naphthalene).""",
    "worked_examples": [
      {
        "problem": "How will you separate a mixture containing common salt, sand, and ammonium chloride? Give the step-by-step sequential flowchart.",
        "given": "Trio mixture of NaCl, Sand, and NH4Cl.",
        "formula": "Sequential property exploitation: Sublimation -> Dissolution/Filtration -> Crystallization/Evaporation",
        "substitution": "Step 1: Sublimation heats NH4Cl into gas, condensing on cool funnel. Step 2: Add water to salt+sand, filter to collect sand. Step 3: Evaporate filtrate to recover pure NaCl.",
        "calculation": "NH4Cl sublimes at 340°C. Sand SiO2 is insoluble in water. NaCl has high solubility of 36 g / 100 mL.",
        "finalAnswer": "Step 1: Sublimation (removes NH4Cl) | Step 2: Filtration (removes Sand) | Step 3: Evaporation/Crystallization (yields pure NaCl)",
        "unit": "Separation Flowchart"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Evaporation to dryness is the best way to purify all salts from solution.",
        "correction": "Evaporation leaves behind all soluble chemical impurities and can thermally decompose delicate salts. Crystallization yields pure geometric crystals.",
        "why_it_matters": "CBSE frequently asks: 'Why is crystallization preferred over evaporation?'"
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Sublimation Laboratory Apparatus Schematic",
      "diagram_type": "image",
      "concept_visuals": [
        {
          "concept_title": "Laboratory Sublimation Apparatus Setup",
          "diagram_title": "Sublimation of Ammonium Chloride Setup",
          "diagram_type": "image",
          "image_search_query": "Sublimation apparatus inverted funnel cotton plug china dish",
          "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Sublimation_apparatus.svg",
          "what_to_make": "Vector schematic of burner, china dish containing mixture, inverted glass funnel with cotton plug, and pure sublimate depositing on cool funnel walls.",
          "timing_and_cue": "Mount sublimation schematic on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/4/4e/Sublimation_apparatus.svg | Sublimation Apparatus Setup | Inverted funnel with cotton plug capturing ammonium chloride sublimate\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount sublimation setup: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/4/4e/Sublimation_apparatus.svg | Sublimation Setup | Inverted funnel with cotton plug capturing volatile sublimate\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH5_ID,
    "order_index": 5,
    "title": "Separation Mechanics II: Immiscible Liquids, Distillation & Chromatography",
    "description": "Master liquid-liquid separation using a separating funnel, simple distillation for large boiling point differences, fractional distillation with fractionating columns, and paper chromatography.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Separation of Immiscible Liquids: Separating funnel stopcock mechanics and density stratification",
      "Simple Distillation: Principle of vaporization followed by condensation (boiling point gap > 25 K)",
      "Fractional Distillation: Fractionating column packed with glass beads for liquids with boiling point gap < 25 K",
      "Air Separation: Fractional distillation of liquid air to separate Nitrogen, Argon, and Oxygen",
      "Paper Chromatography: Principle of differential partition between mobile phase (solvent) and stationary phase (paper)"
    ],
    "key_concepts": [
      "Immiscible Liquids: Liquids that do not dissolve in each other and separate into distinct layers based on density.",
      "Simple Distillation: Separation of miscible liquids having boiling point difference greater than 25°C without decomposition.",
      "Fractional Distillation: Separation technique using a fractionating column for miscible liquids with boiling point difference less than 25 K.",
      "Chromatography: Technique used for separation of solutes that dissolve in the same solvent with differing rates of migration."
    ],
    "success_criteria": "Student can select the correct distillation method based on boiling points, explain how a fractionating column works, and interpret chromatograms.",
    "chapter_notes": """### 5.10 Separation of Liquid Mixtures
1. **Immiscible Liquids (Separating Funnel)**: Denser liquid drained through stopcock first.
2. **Simple vs Fractional Distillation**:
   - **Simple Distillation**: Used when boiling point difference > 25 K.
   - **Fractional Distillation**: Used when boiling point difference < 25 K. Fractionating column packed with glass beads provides large surface area for repeated condensation-vaporization cycles.
3. **Paper Chromatography**: Solutes separate based on differential solubility in mobile phase.""",
    "worked_examples": [
      {
        "problem": "Two miscible liquids A (BP 65°C) and B (BP 78°C) are mixed. Can they be separated by simple distillation? What technique should be used?",
        "given": "Liquid A (65°C), Liquid B (78°C). Delta BP = 78 - 65 = 13°C (13 K).",
        "formula": "If Delta BP < 25 K, use Fractional Distillation; if > 25 K, use Simple Distillation.",
        "substitution": "Delta BP = 13 K < 25 K.",
        "calculation": "Simple distillation fails because both boil together. Fractional distillation with bead-packed column is required.",
        "finalAnswer": "No, cannot use simple distillation. Fractional distillation is mandatory.",
        "unit": "Technique Selection"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Simple distillation can separate any two liquids that mix together.",
        "correction": "If boiling points are close (< 25 K), vapors of both condense together. A fractionating column is essential.",
        "why_it_matters": "CBSE regularly asks students to explain why a fractionating column is needed."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Fractional Distillation Apparatus with Fractionating Column",
      "diagram_type": "image",
      "concept_visuals": [
        {
          "concept_title": "Fractional Distillation Apparatus Schematic",
          "diagram_title": "Fractional Distillation Apparatus",
          "diagram_type": "image",
          "image_search_query": "Fractional distillation apparatus fractionating column Liebig condenser",
          "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/18/Fractional_distillation_lab_apparatus.svg",
          "what_to_make": "Vector diagram showing distillation flask, fractionating column with bead packing, thermometer at neck, Liebig water condenser, and receiver flask.",
          "timing_and_cue": "Mount fractional distillation apparatus on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/1/18/Fractional_distillation_lab_apparatus.svg | Fractional Distillation Apparatus | Distillation flask, bead-packed fractionating column, water condenser, and distillate receiver\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount fractional distillation diagram: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/1/18/Fractional_distillation_lab_apparatus.svg | Fractional Distillation | Distillation flask, fractionating column, Liebig condenser\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH5_ID,
    "order_index": 6,
    "title": "Master Separation Solver & Comprehensive NCERT Chapter Review",
    "description": "Master multi-step industrial and laboratory separation schemes, solve complex concentration numericals, and conduct the 10-MCQ diagnostic evaluation.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Comprehensive Multi-Step Separation Strategies for Multi-Component Mixtures",
      "Purification of Drinking Water in Municipal Waterworks (Sedimentation -> Loading -> Filtration -> Chlorination)",
      "Physical vs Chemical Changes: Reversibility, energy exchange, and creation of new chemical bonds",
      "NCERT In-Text and Chapter-End Master Problem Solutions",
      "Diagnostic 10-MCQ Evaluation Quiz"
    ],
    "key_concepts": [
      "Separation Strategy: Designing sequential operations based on differences in density, solubility, boiling point, and volatility.",
      "Municipal Waterworks: Systematic sequence of sedimentation, alum loading, sand filtration, and chlorine disinfection.",
      "Physical Change: Alteration in state or appearance without altering chemical composition.",
      "Chemical Change: Process involving chemical reactions yielding new substances with distinct chemical bonds."
    ],
    "success_criteria": "Student achieves 100% mastery on multi-step separation flowcharts and achieves >= 80% on the final chapter evaluation quiz.",
    "chapter_notes": """### 5.11 Municipal Water Purification Workflow
1. Reservoir -> 2. Sedimentation Tank (gravity settling) -> 3. Loading Tank (alum neutralizes colloidal charges) -> 4. Filtration Tank (sand/gravel filters fine particles) -> 5. Chlorination (kills bacteria) -> Tap Water.

### 5.12 Physical vs Chemical Changes
- **Physical**: No new substance, reversible (e.g. melting ice, cutting trees).
- **Chemical**: New substances with new bonds, irreversible (e.g. rusting of iron, burning candle).""",
    "worked_examples": [
      {
        "problem": "Classify as chemical or physical changes: (a) Cutting trees, (b) Melting butter, (c) Rusting almirah, (d) Boiling water, (e) Electrolysis of water, (f) Dissolving salt in water, (g) Burning paper and wood.",
        "given": "7 daily phenomena from NCERT Exercise.",
        "formula": "Physical: same chemical identity | Chemical: new chemical bonds formed",
        "substitution": "Cutting trees: physical; Melting butter: physical; Rusting: chemical; Boiling: physical; Electrolysis: chemical; Dissolving salt: physical; Burning: chemical.",
        "calculation": "Electrolysis and combustion alter molecular structures. Phase transitions preserve chemical identity.",
        "finalAnswer": "Physical: (a), (b), (d), (f) | Chemical: (c), (e), (g)",
        "unit": "Change Classification"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Burning of a candle is only a physical change because the wax melts.",
        "correction": "Burning a candle involves BOTH: Melting of wax is a physical change, but burning wax vapor into CO2 and H2O is a chemical change.",
        "why_it_matters": "Classic CBSE trick question testing identification of dual changes."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Water Purification Plant Flowchart",
      "diagram_type": "flowchart",
      "concept_visuals": [
        {
          "concept_title": "Municipal Water Purification System",
          "diagram_title": "Water Purification Plant Stages",
          "diagram_type": "flowchart",
          "what_to_make": "Reservoir -> Sedimentation Tank -> Loading Tank (Alum) -> Filtration Tank (Sand/Gravel) -> Chlorination Tank -> Clean Tap Water",
          "timing_and_cue": "Mount waterworks flowchart on Step 1: write_chalkboard(action=\"draw_flowchart\", content=\"Reservoir -> Sedimentation Tank -> Loading Tank (Alum) -> Filtration Tank -> Chlorination Tank -> Tap Water\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount water purification stages: write_chalkboard(action=\"draw_flowchart\", content=\"Reservoir -> Sedimentation Tank -> Loading Tank (Alum) -> Filtration Tank -> Chlorination Tank -> Tap Water\").\n2. 6-STAGE SOCRATIC CADENCE."
  }
]
all_modules.extend(ch5)

# --- CHAPTER 6 ---
ch6 = [
  {
    "curriculum_id": CH6_ID,
    "order_index": 1,
    "title": "The Nature of Force: Measuring Magnitude, Balanced vs Unbalanced Forces & Friction",
    "description": "Understand forces as vector interactions, distinguish balanced forces (net zero acceleration) from unbalanced forces (causes acceleration), and explore static, sliding, and rolling friction.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "The Concept of Force: Push, pull, or drag changing state of motion or shape",
      "Measuring Force: The Spring Balance and the SI unit Newton (N)",
      "Balanced Forces: Net force = 0, state of rest or uniform motion preserved",
      "Unbalanced Forces: Net force != 0, causes change in speed, direction, or acceleration",
      "Frictional Force: Static friction, limiting friction, sliding (kinetic) friction, rolling friction"
    ],
    "key_concepts": [
      "Force: Vector quantity that changes or tends to change the state of rest, uniform motion, or geometry of an object.",
      "Balanced Forces: Forces acting on a body whose vector sum is zero, resulting in zero net acceleration.",
      "Unbalanced Forces: Resultant force is non-zero, producing an acceleration in the direction of the net force.",
      "Friction: Contact force that opposes relative motion between two surfaces in contact."
    ],
    "success_criteria": "Student can draw free body diagrams with balanced and unbalanced forces, calculate net force, and compare types of friction.",
    "chapter_notes": """### 6.1 What is Force?
A force is an external influence capable of changing the velocity or shape of an object:
- SI Unit: **Newton (N)**, where $1\\text{ N} = 1\\text{ kg}\\cdot\\text{m/s}^2$.
- Vector quantity: Has both **magnitude** and **direction**.

### 6.2 Balanced vs Unbalanced Forces
- **Balanced Forces**: $\\sum \\vec{F} = 0$. Do not produce acceleration. Can only change shape/size (e.g. compressing a balloon).
- **Unbalanced Forces**: $\\sum \\vec{F} \\neq 0$. Produce acceleration in the direction of net force ($a = F_{\\text{net}} / m$).

### 6.3 Friction Dynamics
- Opposes relative sliding motion between contacting surfaces.
- Magnitude hierarchy: $\\text{Static Friction (max)} > \\text{Sliding/Kinetic Friction} > \\text{Rolling Friction}$.
- Rolling friction is 10 to 100 times smaller than sliding friction, which is why ball bearings and wheels are ubiquitous in transport.""",
    "worked_examples": [
      {
        "problem": "A wooden block of mass 5 kg is pushed horizontally on a table. The applied force is 25 N, and the opposing frictional force is 10 N. Calculate: (a) Net unbalanced force, (b) Acceleration of the block.",
        "given": "Mass m = 5 kg | Applied force F_app = 25 N (forward) | Friction f = 10 N (backward)",
        "formula": "F_net = F_app - f; a = F_net / m",
        "substitution": "F_net = 25 N - 10 N = 15 N; a = 15 N / 5 kg",
        "calculation": "15 / 5 = 3 m/s^2",
        "finalAnswer": "(a) Net force = 15 N forward, (b) Acceleration = 3 m/s^2",
        "unit": "m/s^2"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "A continuous force is required to keep an object moving at constant velocity.",
        "correction": "Aristotelian fallacy! According to Galileo and Newton, an object in motion requires NO force to keep moving at constant velocity in the absence of friction. Force is only needed to OVERCOME friction.",
        "why_it_matters": "Fundamental foundation of Newtonian physics tested in every standard exam."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Free Body Diagram of Balanced vs Unbalanced Forces",
      "diagram_type": "flowchart",
      "concept_visuals": [
        {
          "concept_title": "Free Body Diagram of Friction and Motion",
          "diagram_title": "Forces on a Sliding Block",
          "diagram_type": "flowchart",
          "what_to_make": "Vertical: Normal Reaction (N) = Gravity (mg) [Balanced] | Horizontal: Applied Force (25 N) > Friction (10 N) -> Net Force = 15 N -> Acceleration a = 3 m/s^2",
          "timing_and_cue": "Mount FBD on Step 1: write_chalkboard(action=\"draw_flowchart\", content=\"Vertical: Normal N = Weight mg (Balanced) | Horizontal: Applied 25N > Friction 10N -> Net 15N -> Acceleration a = 3 m/s^2\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount FBD: write_chalkboard(action=\"draw_flowchart\", content=\"Vertical: Normal N = Weight mg (Balanced) | Horizontal: Applied 25N > Friction 10N -> Net 15N -> Acceleration a = 3 m/s^2\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH6_ID,
    "order_index": 2,
    "title": "Galileo's Inclined Plane Intuition & Newton's First Law of Motion (Inertia)",
    "description": "Trace Galileo's thought experiments with double inclined planes, formalize Newton's First Law of Motion, and explore inertia of rest, motion, and direction with mass as quantitative measure.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Galileo's Double Inclined Plane Experiment: Natural state of an uninhibited object",
      "Newton's First Law of Motion: Statement and physical meaning",
      "Inertia of Rest: Dust falling from carpet when beaten, passenger jerking backward when bus starts",
      "Inertia of Motion: Passenger jerking forward when bus brakes abruptly, athlete running before jump",
      "Inertia of Direction: Mud flying tangentially off rotating bicycle tire",
      "Mass as the Quantitative Measure of Inertia"
    ],
    "key_concepts": [
      "Newton's First Law: An object remains in a state of rest or of uniform motion in a straight line unless acted upon by an unbalanced external force.",
      "Inertia: Inherent property of a body by virtue of which it resists any change in its state of rest or uniform motion.",
      "Mass & Inertia: Greater the mass of a body, greater is its inertia (Heavier body requires greater force to change motion)."
    ],
    "success_criteria": "Student can explain everyday inertia phenomena using scientific terminology and relate mass quantitatively to inertia.",
    "chapter_notes": """### 6.4 Galileo's Revolutionary Insight
- Galileo observed a marble rolling down an inclined plane speeds up, and rolling up slows down.
- On a **double inclined plane**: If slope angles are equal, the marble climbs to the same vertical height.
- If the second plane is made horizontal, the marble must travel forever to reach its initial height if friction is absent!

### 6.5 Newton's First Law of Motion (Law of Inertia)
$$\\sum \\vec{F} = 0 \\implies \\vec{v} = \\text{constant} \\quad (\\vec{a} = 0)$$

### 6.6 The Three Dimensions of Inertia
1. **Inertia of Rest**: Tendency to remain at rest (e.g. When a bus abruptly starts, passengers fall backward because their feet move forward with the floor while upper body stays at rest).
2. **Inertia of Motion**: Tendency to continue moving at constant speed (e.g. When a moving bus stops suddenly, passengers lean forward).
3. **Inertia of Direction**: Tendency to maintain direction (e.g. When a car takes a sharp curve, passengers lean outward).""",
    "worked_examples": [
      {
        "problem": "Which of the following has more inertia: (a) A rubber ball and a stone of the same size? (b) A bicycle and a train? (c) A five-rupee coin and a one-rupee coin?",
        "given": "Three pairs of objects from NCERT Exercise Question 1.",
        "formula": "Inertia is directly proportional to mass (Inertia \\propto Mass).",
        "substitution": "Stone mass > rubber ball mass; Train mass >> bicycle mass; 5-rupee coin mass > 1-rupee coin mass.",
        "calculation": "Because mass is the quantitative measure of inertia, the heavier object in each pair possesses greater inertia.",
        "finalAnswer": "(a) Stone, (b) Train, (c) Five-rupee coin.",
        "unit": "Comparative Inertia"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "A running fan turns off immediately when the switch is flipped.",
        "correction": "The fan continues rotating for several seconds due to its rotational inertia of motion; friction in bearings and air drag slowly dissipate its kinetic energy.",
        "why_it_matters": "Real-world intuition connecting electricity disconnect with mechanical inertia."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Galileo Double Inclined Plane Schematic",
      "diagram_type": "image",
      "concept_visuals": [
        {
          "concept_title": "Galileo Double Inclined Plane Thought Experiment",
          "diagram_title": "Galileo Inclined Plane Thought Experiment",
          "diagram_type": "image",
          "image_search_query": "Galileo inclined plane thought experiment inertia",
          "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Galileo%27s_experiment_on_inclined_planes.svg",
          "what_to_make": "Vector diagram of ball rolling down plane 1 to height h, climbing plane 2 to height h, and traveling indefinitely on horizontal plane.",
          "timing_and_cue": "Mount Galileo inclined planes on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/e0/Galileo%27s_experiment_on_inclined_planes.svg | Galileo Double Inclined Plane | Ball reaching identical height h; horizontal plane requires indefinite motion to reach h\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount Galileo planes: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/e0/Galileo%27s_experiment_on_inclined_planes.svg | Galileo Inclined Plane | Ball climbs to same height h; on flat plane motion continues indefinitely\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH6_ID,
    "order_index": 3,
    "title": "Momentum Dynamics & Newton's Second Law of Motion (F = ma & Impulse)",
    "description": "Define linear momentum, derive Newton's Second Law F = ma from rate of change of momentum, and explore impulse and safety impact-time extensions.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Linear Momentum: Definition p = mv, vector nature, SI unit kg m/s",
      "Newton's Second Law: Rate of change of momentum is proportional to applied unbalanced force",
      "Mathematical Derivation: F = k * m * (v - u) / t = k * ma, establishing k = 1",
      "Definition of 1 Newton: Force that produces acceleration of 1 m/s^2 on a mass of 1 kg",
      "Impulse and Impact Duration: F = Delta p / Delta t, cricket fielder pulling hands back, high jump sandbeds"
    ],
    "key_concepts": [
      "Linear Momentum: Quantity of motion in a body, defined as product of mass and velocity ($p = mv$).",
      "Newton's Second Law: The rate of change of momentum of an object is directly proportional to the applied unbalanced force in the direction of the force ($F = ma$).",
      "Impulse: Product of force and time duration ($J = F \\Delta t = \\Delta p$).",
      "Impact Force Mitigation: Increasing contact time $\\Delta t$ drastically reduces impact force $F$ for the same momentum change."
    ],
    "success_criteria": "Student can derive F = ma step-by-step, solve complex force-momentum numericals, and explain safety engineering using impulse.",
    "chapter_notes": """### 6.7 Linear Momentum
$$p = mv \\quad [\\text{SI unit: } \\text{kg}\\cdot\\text{m/s}]$$
- Vector quantity having the same direction as velocity.

### 6.8 Derivation of Newton's Second Law
Let an object of mass $m$ have initial velocity $u$. An unbalanced force $F$ acts for time $t$, changing velocity to $v$:
1. Initial momentum $p_1 = mu$, Final momentum $p_2 = mv$.
2. Change in momentum $\\Delta p = p_2 - p_1 = m(v - u)$.
3. Rate of change of momentum $= \\frac{m(v - u)}{t} = ma$.
4. By Newton's Second Law:
   $$F \\propto \\frac{\\Delta p}{t} \\implies F = kma$$
5. Setting $k = 1$ when $F = 1\\text{ N}$, $m = 1\\text{ kg}$, $a = 1\\text{ m/s}^2$:
   $$F = ma$$

### 6.9 Impulse and Impact Physics
$$F = \\frac{\\Delta p}{\\Delta t}$$
- If $\\Delta t$ increases, force $F$ decreases proportionately!
- **Cricket Fielder**: Pulls hands backward to increase time $\\Delta t$ taken to bring ball's velocity to zero, minimizing force on hands and avoiding injury.
- **Seatbelts & Airbags**: Extend deceleration time during collision, preventing lethal forces on the skull and chest.""",
    "worked_examples": [
      {
        "problem": "A constant force acts on an object of mass 5 kg for a duration of 2 s. It increases the object's velocity from 3 m/s to 7 m/s. Find the magnitude of the applied force. If the force were applied for a duration of 5 s, what would be the final velocity?",
        "given": "Mass m = 5 kg | Time t1 = 2 s | Initial velocity u = 3 m/s | Final velocity v1 = 7 m/s",
        "formula": "a = (v1 - u) / t1; F = ma; v2 = u + a * t2",
        "substitution": "a = (7 - 3) / 2 = 4 / 2 = 2 m/s^2; F = 5 * 2 = 10 N; v2 = 3 + (2 * 5)",
        "calculation": "F = 10 N; v2 = 3 + 10 = 13 m/s",
        "finalAnswer": "Force = 10 N; Final velocity after 5 s = 13 m/s",
        "unit": "N and m/s"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Heavier objects always fall faster because they have more gravitational force.",
        "correction": "Gravitational force is F = mg, but acceleration is a = F / m = mg / m = g! The mass cancels out completely, so all objects accelerate at g = 9.8 m/s^2 in vacuum.",
        "why_it_matters": "Crucial distinction between force (proportional to mass) and acceleration (independent of mass)."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Newton Second Law F = ma Coordinate Plot",
      "diagram_type": "graph",
      "concept_visuals": [
        {
          "concept_title": "Force vs Acceleration Linear Proportionality",
          "diagram_title": "Force vs Acceleration Graph",
          "diagram_type": "graph",
          "what_to_make": "Mafs linear coordinate plot of F = m * a where slope equals mass m",
          "timing_and_cue": "Mount F = ma graph on Step 1: plot_mathematical_graph(formula=\"5*x\", domain=\"[0, 10]\", range=\"[0, 50]\", title=\"Force (N) vs Acceleration (m/s^2) for m = 5 kg\", callout=\"Linear slope represents mass m = 5 kg\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, call plot_mathematical_graph(formula=\"5*x\", domain=\"[0, 10]\", range=\"[0, 50]\", title=\"Force vs Acceleration for m = 5 kg\", callout=\"Slope = mass m = 5 kg\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH6_ID,
    "order_index": 4,
    "title": "Action, Reaction & Newton's Third Law of Motion",
    "description": "Understand action-reaction force pairs, why action and reaction never cancel out (acting on distinct bodies), and analyze walking, rowing, balloon rockets, and horse-cart mechanics.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Newton's Third Law Statement: To every action, there is an equal and opposite reaction",
      "The Invariant: Action and reaction forces act simultaneously on TWO DIFFERENT BODIES",
      "Why Action and Reaction Never Cancel Out: Equal and opposite forces on different objects do not equilibrate",
      "Walking Biomechanics: Foot pushes ground backward (action), ground pushes foot forward (reaction)",
      "Rowing a Boat & Swimmer Propulsion: Pushing water backward to move body forward",
      "The Horse and Cart Problem: Resolution of contact forces"
    ],
    "key_concepts": [
      "Newton's Third Law: When one body exerts a force on a second body, the second body simultaneously exerts an equal in magnitude and opposite in direction force on the first body ($F_{AB} = -F_{BA}$).",
      "Dual Body Invariant: Action and reaction forces NEVER act on the same body and therefore can never cancel each other.",
      "Simultaneity: There is no time delay between action and reaction forces."
    ],
    "success_criteria": "Student can identify action and reaction force pairs in any physical scenario and demonstrate why they do not cancel out.",
    "chapter_notes": """### 6.10 Newton's Third Law of Motion
$$\\vec{F}_{AB} = -\\vec{F}_{BA}$$
- **Key Characteristics**:
  1. Forces always occur in **matched pairs**. A single isolated force cannot exist in nature.
  2. Action and reaction forces act on **two different interacting objects**.
  3. They are **equal in magnitude** and **opposite in direction**.
  4. They act **simultaneously**.

### 6.11 Why Action & Reaction Never Cancel Out
- Forces can only cancel out and produce equilibrium if they act on the **SAME body** (like two people pulling the same rope in opposite directions).
- In Newton's Third Law:
  - $F_{\\text{foot on ground}}$ acts on the Earth.
  - $F_{\\text{ground on foot}}$ acts on the human body.
  - Because each force acts on a different body, they cannot cancel each other!""",
    "worked_examples": [
      {
        "problem": "Explain why a cricketer or swimmer is able to propel forward according to Newton's Third Law. State the action and reaction forces explicitly.",
        "given": "Swimmer pushing water in swimming pool.",
        "formula": "F_swimmer_on_water = - F_water_on_swimmer",
        "substitution": "Action: Swimmer exerts backward force on water using arms and legs. Reaction: Water exerts equal and opposite forward force on swimmer's body.",
        "calculation": "Because the reaction force acts on the swimmer, it accelerates the swimmer forward through the water.",
        "finalAnswer": "Action: Backward push on water | Reaction: Forward thrust on swimmer",
        "unit": "Force Pair Identification"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Action occurs first, and reaction occurs a moment later as a response.",
        "correction": "Action and reaction are perfectly simultaneous! Neither force is the cause or the effect; both exist at the exact same instant.",
        "why_it_matters": "Tested in conceptual board questions to verify students do not treat reaction as a delayed echo."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Newton Third Law Force Pair Diagram",
      "diagram_type": "image",
      "concept_visuals": [
        {
          "concept_title": "Action-Reaction Pair on Interacting Bodies",
          "diagram_title": "Newton Third Law Action Reaction Pair",
          "diagram_type": "image",
          "image_search_query": "Newton third law action reaction skater wall",
          "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Action-reaction_forces.svg",
          "what_to_make": "Vector diagram of two skaters pushing each other with equal and opposite force vectors Fab and -Fba.",
          "timing_and_cue": "Mount action-reaction vector diagram on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/3/36/Action-reaction_forces.svg | Action Reaction Force Pairs | Equal and opposite forces acting on two distinct bodies\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount action-reaction diagram: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/3/36/Action-reaction_forces.svg | Action Reaction Force Pairs | Equal and opposite forces acting on two distinct bodies\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH6_ID,
    "order_index": 5,
    "title": "Conservation of Linear Momentum: Isolated Systems & Recoil Mechanics",
    "description": "Derive the Law of Conservation of Momentum from Newton's Second and Third Laws, calculate recoil velocities of firearms, and analyze inelastic collisions.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Isolated System Concept: External net force F_ext = 0",
      "Mathematical Derivation: Collision between two spheres of masses m1 and m2",
      "Law of Conservation of Linear Momentum: m1*u1 + m2*u2 = m1*v1 + m2*v2",
      "Recoil Velocity of a Gun: V_recoil = - (m_bullet * v_bullet) / M_gun",
      "Inelastic Collisions: Objects sticking together after impact (m1+m2)*v_common",
      "Rocket Propulsion Principle: Expulsion of high-velocity exhaust gases"
    ],
    "key_concepts": [
      "Law of Conservation of Momentum: In an isolated system where no external unbalanced force acts, the total linear momentum remains constant.",
      "Gun Recoil: As bullet moves forward with positive momentum, gun recoils backward with equal negative momentum to keep total momentum zero.",
      "Collision Invariant: Total momentum before collision equals total momentum after collision."
    ],
    "success_criteria": "Student can derive momentum conservation, calculate recoil velocity of weapons, and solve collision problems.",
    "chapter_notes": """### 6.12 Derivation of Conservation of Momentum
Consider two spheres $A$ and $B$ of masses $m_1$ and $m_2$ moving with initial velocities $u_1$ and $u_2$ ($u_1 > u_2$):
1. During collision for time $t$, $A$ exerts force $F_{AB}$ on $B$, and $B$ exerts force $F_{BA}$ on $A$.
2. By Newton's Second Law:
   $$F_{AB} = m_2 \\frac{(v_2 - u_2)}{t}, \\quad F_{BA} = m_1 \\frac{(v_1 - u_1)}{t}$$
3. By Newton's Third Law ($F_{AB} = -F_{BA}$):
   $$m_2 \\frac{(v_2 - u_2)}{t} = -m_1 \\frac{(v_1 - u_1)}{t}$$
4. Multiplying by $t$ and rearranging:
   $$m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2$$

### 6.13 Gun Recoil Formula
Before firing, gun and bullet are at rest: $p_{\\text{initial}} = 0$.
After firing:
$$M_{\\text{gun}} V_{\\text{recoil}} + m_{\\text{bullet}} v_{\\text{bullet}} = 0 \\implies V_{\\text{recoil}} = -\\frac{m_{\\text{bullet}} v_{\\text{bullet}}}{M_{\\text{gun}}}$$
The negative sign confirms the recoil is backward.""",
    "worked_examples": [
      {
        "problem": "A bullet of mass 20 g is horizontally fired with a velocity 150 m/s from a pistol of mass 2 kg. What is the recoil velocity of the pistol?",
        "given": "Mass of bullet m1 = 20 g = 0.02 kg | Velocity of bullet v1 = 150 m/s | Mass of pistol m2 = 2 kg",
        "formula": "Total momentum before = Total momentum after: 0 = m1*v1 + m2*v2 => v2 = - (m1*v1) / m2",
        "substitution": "v2 = - (0.02 kg * 150 m/s) / 2 kg",
        "calculation": "0.02 * 150 = 3 kg*m/s; v2 = -3 / 2 = -1.5 m/s",
        "finalAnswer": "Recoil velocity of pistol = -1.5 m/s (1.5 m/s backward)",
        "unit": "m/s"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "The gun kicks backward because gunpowder pushes against the air behind it.",
        "correction": "Rocket and gun recoil work perfectly in a vacuum! The backward force on the gun is solely the reaction to the forward momentum given to the bullet by expanding gases inside the closed chamber.",
        "why_it_matters": "Space rockets operate in pure vacuum where there is no air to push against."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Conservation of Linear Momentum Collision Schematic",
      "diagram_type": "image",
      "concept_visuals": [
        {
          "concept_title": "Collision and Recoil Momentum Conservation",
          "diagram_title": "Conservation of Momentum Collision",
          "diagram_type": "image",
          "image_search_query": "Conservation of linear momentum collision two spheres",
          "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e9/Colliding_balls.svg",
          "what_to_make": "Vector diagram of before collision, during collision (Fab and Fba), and after collision velocities.",
          "timing_and_cue": "Mount collision momentum schematic on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/e9/Colliding_balls.svg | Momentum Conservation Collision | Before, during, and after collision momentum conservation\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount collision diagram: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/e9/Colliding_balls.svg | Momentum Conservation | Total momentum before equals total momentum after\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH6_ID,
    "order_index": 6,
    "title": "Master Dynamics Problem Solver: Authentic NCERT & Board Exam Numericals",
    "description": "Meticulously lay out step-by-step solutions for complex multi-body systems, braking forces, kinematic motion integration, and conduct the 10-MCQ diagnostic evaluation.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Trio Layout for Senior Board Numericals: Given -> Formula -> Substitution -> Rough Work -> Boxed Answer",
      "Integrating Kinematic Equations (v = u + at, s = ut + 0.5at^2, v^2 - u^2 = 2as) with F = ma",
      "Train and Wagon Mechanics: Engine tractive force, track friction, and coupling tension",
      "Velocity-Time Graph Integration to deduce force and mass",
      "Diagnostic 10-MCQ Evaluation Quiz"
    ],
    "key_concepts": [
      "Kinematic-Dynamic Coupling: Using equations of motion to find acceleration, then applying Newton's Second Law to calculate force ($F = ma$).",
      "Tension in Couplings: Internal forces within multi-mass systems determined by isolated free body analysis."
    ],
    "success_criteria": "Student solves any multi-step dynamics numerical flawlessly and scores >= 80% on chapter quiz.",
    "chapter_notes": """### 6.14 Kinematic-Dynamic Integration Framework
1. **Find acceleration $a$ from kinematics**:
   - $v = u + at$
   - $s = ut + \\frac{1}{2}at^2$
   - $v^2 - u^2 = 2as$
2. **Compute force from dynamics**:
   - $F = ma$
   - If friction opposes: $F_{\\text{net}} = F_{\\text{engine}} - f_{\\text{friction}} = m_{\\text{total}} a$""",
    "worked_examples": [
      {
        "problem": "An 8000 kg engine pulls a train of 5 wagons, each of 2000 kg, along a horizontal track. If the engine exerts a force of 40,000 N and the track offers a friction force of 5000 N, then calculate: (a) Net accelerating force, (b) Acceleration of the train, (c) The force of wagon 1 on wagon 2.",
        "given": "Engine mass = 8000 kg | 5 wagons each 2000 kg => Total wagon mass = 10,000 kg | Total mass M = 18,000 kg | Applied force F = 40,000 N | Friction f = 5000 N",
        "formula": "(a) F_net = F - f; (b) a = F_net / M; (c) F_12 = mass of remaining 4 wagons * a",
        "substitution": "F_net = 40,000 - 5000 = 35,000 N; a = 35,000 / 18,000; Mass of wagons 2,3,4,5 = 4 * 2000 = 8000 kg; F_12 = 8000 * 1.944",
        "calculation": "a = 35 / 18 = 1.944 m/s^2; F_12 = 8000 * (35/18) = 15,555.5 N",
        "finalAnswer": "(a) Net force = 35,000 N | (b) Acceleration = 1.944 m/s^2 | (c) Force of wagon 1 on 2 = 15,555.5 N",
        "unit": "N and m/s^2"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Wagon 1 pulls all 5 wagons.",
        "correction": "Wagon 1 only pulls the 4 wagons behind it (wagons 2, 3, 4, 5)! The mass accelerated by the coupling between wagon 1 and 2 is 4 * 2000 = 8000 kg, not 10,000 kg.",
        "why_it_matters": "High-yield CBSE 5-mark question where students frequently miscount the pulled mass."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Multi-Wagon Train Free Body Diagram",
      "diagram_type": "flowchart",
      "concept_visuals": [
        {
          "concept_title": "Train and Wagons Tractive Force Breakdown",
          "diagram_title": "Train Wagon Coupling Diagram",
          "diagram_type": "flowchart",
          "what_to_make": "Engine (40,000 N) -> Wagon 1 -> Wagon 2 -> Wagon 3 -> Wagon 4 -> Wagon 5; Net Force 35,000 N over total mass 18,000 kg",
          "timing_and_cue": "Mount train coupling flowchart on Step 1: write_chalkboard(action=\"draw_flowchart\", content=\"Engine (40000N) - Track Friction (5000N) = Net Accelerating Force 35000N; Total Mass = 18000kg -> a = 1.94 m/s^2\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount train coupling layout: write_chalkboard(action=\"draw_flowchart\", content=\"Engine (40000N) - Friction (5000N) = Net 35000N; Mass 18000kg -> a = 1.94 m/s^2\").\n2. 6-STAGE SOCRATIC CADENCE."
  }
]
all_modules.extend(ch6)

# --- CHAPTER 7 ---
ch7 = [
  {
    "curriculum_id": CH7_ID,
    "order_index": 1,
    "title": "The Physics of Work: Definition, Sign Conventions & Zero-Work Conditions",
    "description": "Establish the scientific definition of work W = F * s * cos(theta), understand 1 Joule, distinguish positive, negative, and zero work, and analyze porter and satellite scenarios.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Scientific Conception of Work: Must have applied force and displacement along direction of force",
      "Work Done by Constant Force: W = F * s, SI unit Joule (J)",
      "Definition of 1 Joule: 1 J = 1 N * 1 m",
      "General Formula: W = F * s * cos(theta)",
      "Positive Work: Theta = 0 degrees (Force in direction of displacement)",
      "Negative Work: Theta = 180 degrees (Frictional force opposing displacement)",
      "Zero Work Conditions: Displacement = 0 or Theta = 90 degrees (Porter carrying suitcase horizontally, moon orbiting Earth)"
    ],
    "key_concepts": [
      "Work: Scalar quantity defined as the product of the component of force along displacement and the magnitude of displacement ($W = F s \\cos\\theta$).",
      "Joule: 1 Joule of work is done when a force of 1 Newton displaces an object by 1 meter in the direction of the force.",
      "Zero Work: No work is done if displacement is zero OR if force is perpendicular to displacement ($\\cos 90^\\circ = 0$)."
    ],
    "success_criteria": "Student can calculate work with proper sign, identify zero-work situations, and explain why daily 'mental effort' is not physics work.",
    "chapter_notes": """### 7.1 What is Work in Physics?
For work to be done, two conditions must be satisfied:
1. A force must act on the object.
2. The object must be displaced.

$$W = F \\cdot s \\cdot \\cos\\theta \\quad [\\text{SI unit: } \\text{Joule (J)}]$$

### 7.2 Sign Conventions of Work
- **Positive Work** ($0^\\circ \\le \\theta < 90^\\circ$): Force assists motion. Example: Pulling a cart forward ($W = +Fs$).
- **Negative Work** ($90^\\circ < \\theta \\le 180^\\circ$): Force opposes motion. Example: Friction on a skidding car ($W = -fs$).
- **Zero Work** ($\\theta = 90^\\circ$ or $s = 0$):
  1. A porter carrying a 50 kg trunk on his head while walking horizontally: Force of gravity is vertical ($90^\\circ$ to horizontal displacement), so $W_{\\text{gravity}} = mg s \\cos 90^\\circ = 0$!
  2. Centripetal force on Earth orbiting Sun ($F \\perp v$).""",
    "worked_examples": [
      {
        "problem": "A force of 7 N acts on an object. The displacement is 8 m in the direction of the force. What is the work done in this case?",
        "given": "Force F = 7 N | Displacement s = 8 m | Angle theta = 0 degrees",
        "formula": "W = F * s * cos(0) = F * s",
        "substitution": "W = 7 N * 8 m",
        "calculation": "7 * 8 = 56 J",
        "finalAnswer": "Work done = 56 Joules",
        "unit": "Joules (J)"
      },
      {
        "problem": "A porter lifts luggage of 15 kg from the ground and puts it on his head 1.5 m above the ground. Calculate the work done by him on the luggage. (Take g = 10 m/s^2)",
        "given": "Mass m = 15 kg | Height h = 1.5 m | g = 10 m/s^2",
        "formula": "W = F * s = (mg) * h",
        "substitution": "W = (15 kg * 10 m/s^2) * 1.5 m",
        "calculation": "150 N * 1.5 m = 225 J",
        "finalAnswer": "Work done = 225 Joules",
        "unit": "Joules (J)"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "A student standing still for 3 hours reading a heavy textbook has done immense physics work.",
        "correction": "Because the displacement of the book is s = 0, work done is exactly 0 Joules! In physics, physical displacement is mandatory.",
        "why_it_matters": "Distinguishes physiological muscular fatigue from the rigorous physics definition of work."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Work Done Sign Convention Vectors",
      "diagram_type": "flowchart",
      "concept_visuals": [
        {
          "concept_title": "Work Vector Angles and Sign Conventions",
          "diagram_title": "Work Done Vector Angles",
          "diagram_type": "flowchart",
          "what_to_make": "Theta = 0 deg -> Positive Work (W = +Fs) | Theta = 90 deg -> Zero Work (Porter carrying load) | Theta = 180 deg -> Negative Work (Friction W = -Fs)",
          "timing_and_cue": "Mount work vector angles on Step 1: write_chalkboard(action=\"draw_flowchart\", content=\"Theta = 0 deg -> Positive Work W = +Fs | Theta = 90 deg -> Zero Work W = 0 | Theta = 180 deg -> Negative Work W = -fs\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount work vector angles: write_chalkboard(action=\"draw_flowchart\", content=\"Theta = 0 deg -> Positive Work W = +Fs | Theta = 90 deg -> Zero Work W = 0 | Theta = 180 deg -> Negative Work W = -fs\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH7_ID,
    "order_index": 2,
    "title": "Kinetic Energy & The Work-Energy Theorem",
    "description": "Derive kinetic energy K = 1/2 m v^2 from kinematic equations of motion, establish the Work-Energy Theorem W_net = Delta K, and solve deceleration work problems.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Energy Definition: The capacity of an object to perform mechanical work",
      "Kinetic Energy (K): Energy possessed by an object due to its motion",
      "Mathematical Derivation: Combining W = F * s with v^2 - u^2 = 2as",
      "The Work-Energy Theorem: Net work done on an object equals change in its kinetic energy (W_net = K_f - K_i)",
      "Kinetic Energy Scaling: Doubling velocity quadruples kinetic energy (K proportional to v^2)"
    ],
    "key_concepts": [
      "Kinetic Energy: Scalar energy of motion, defined as $K = \\frac{1}{2}mv^2$.",
      "Work-Energy Theorem: The net work done by all forces on a particle equals the change in its kinetic energy ($W_{\\text{net}} = \\Delta K = \\frac{1}{2}mv^2 - \\frac{1}{2}mu^2$).",
      "Quadratic Velocity Dependence: Kinetic energy grows with the square of velocity, making speeding cars exponentially more dangerous to brake."
    ],
    "success_criteria": "Student can derive K = 1/2 m v^2 step-by-step and calculate braking work using the Work-Energy Theorem.",
    "chapter_notes": """### 7.3 Derivation of Kinetic Energy
Consider an object of mass $m$ at rest ($u = 0$). A constant force $F$ acts, accelerating it to velocity $v$ over displacement $s$:
1. Work done: $W = F \\cdot s$.
2. By Newton's Second Law: $F = ma$.
3. By third equation of motion: $v^2 - u^2 = 2as \\implies s = \\frac{v^2 - u^2}{2a}$.
4. Substituting $F$ and $s$:
   $$W = (ma) \\left(\\frac{v^2 - u^2}{2a}\\right) = \\frac{1}{2}m(v^2 - u^2)$$
5. Since $u = 0$:
   $$K = \\frac{1}{2}mv^2 \\quad [\\text{SI unit: } \\text{Joule (J)}]$$

### 7.4 The Work-Energy Theorem
$$W_{\\text{net}} = K_{\\text{final}} - K_{\\text{initial}} = \\frac{1}{2}mv^2 - \\frac{1}{2}mu^2$$
- If work done is positive, speed increases.
- If work done is negative (braking), speed decreases to zero.""",
    "worked_examples": [
      {
        "problem": "An object of mass 15 kg is moving with a uniform velocity of 4 m/s. What is the kinetic energy possessed by the object?",
        "given": "Mass m = 15 kg | Velocity v = 4 m/s",
        "formula": "K = 1/2 * m * v^2",
        "substitution": "K = 0.5 * 15 kg * (4 m/s)^2",
        "calculation": "4^2 = 16; 0.5 * 15 * 16 = 15 * 8 = 120 J",
        "finalAnswer": "Kinetic Energy = 120 Joules",
        "unit": "Joules (J)"
      },
      {
        "problem": "What is the work to be done to increase the velocity of a car from 30 km/h to 60 km/h if the mass of the car is 1500 kg?",
        "given": "Mass m = 1500 kg | u = 30 km/h = 30 * 5/18 = 25/3 m/s | v = 60 km/h = 60 * 5/18 = 50/3 m/s",
        "formula": "W = Delta K = 1/2 * m * (v^2 - u^2)",
        "substitution": "W = 0.5 * 1500 * [(50/3)^2 - (25/3)^2]",
        "calculation": "v^2 - u^2 = (2500 - 625) / 9 = 1875 / 9; W = 750 * (1875 / 9) = 156,250 J",
        "finalAnswer": "Work done = 156,250 Joules (156.25 kJ)",
        "unit": "Joules (J)"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Doubling a car's speed doubles its stopping distance.",
        "correction": "Stopping distance quadruples! Since K is proportional to v^2, doubling speed from 30 to 60 multiplies kinetic energy by 4. Under constant braking force, W = F * s = Delta K requires 4 times the distance.",
        "why_it_matters": "Crucial road safety concept and common board exam numerical."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Kinetic Energy Parabola Coordinate Plot",
      "diagram_type": "graph",
      "concept_visuals": [
        {
          "concept_title": "Kinetic Energy Quadratic Growth Curve",
          "diagram_title": "Kinetic Energy vs Velocity Parabola",
          "diagram_type": "graph",
          "what_to_make": "Mafs quadratic curve of K = 0.5 * m * v^2 demonstrating parabolic growth",
          "timing_and_cue": "Mount K vs v parabola on Step 1: plot_mathematical_graph(formula=\"0.5*2*x^2\", domain=\"[0, 10]\", range=\"[0, 100]\", title=\"Kinetic Energy (J) vs Velocity (m/s) for m = 2 kg\", callout=\"Parabolic curve: K grows quadratically with velocity\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, call plot_mathematical_graph(formula=\"0.5*2*x^2\", domain=\"[0, 10]\", range=\"[0, 100]\", title=\"Kinetic Energy vs Velocity for m = 2 kg\", callout=\"K is proportional to v^2\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH7_ID,
    "order_index": 3,
    "title": "Gravitational Potential Energy & Law of Conservation of Mechanical Energy",
    "description": "Derive gravitational potential energy U = mgh, understand path independence, and prove the Law of Conservation of Mechanical Energy for free-falling bodies.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Potential Energy (U): Energy stored in an object by virtue of its position or configuration",
      "Gravitational Potential Energy Derivation: U = mgh against uniform gravity",
      "Path Independence: Work done against gravity depends only on initial and final vertical height, not the path taken",
      "Law of Conservation of Mechanical Energy: Total mechanical energy E = K + U remains constant in conservative field",
      "Free Fall Proof: Total energy evaluation at height h, at intermediate height h-x, and at ground level"
    ],
    "key_concepts": [
      "Potential Energy: Stored energy due to position or deformation ($U = mgh$ for gravity, $U = \\frac{1}{2}kx^2$ for spring).",
      "Path Independence: Gravitational force is conservative; work done is identical whether lifted straight up or dragged along an incline of the same height.",
      "Conservation of Mechanical Energy: In the absence of air resistance, $K + U = \\text{constant}$."
    ],
    "success_criteria": "Student can prove energy conservation during free fall and calculate interchange between potential and kinetic energy.",
    "chapter_notes": """### 7.5 Gravitational Potential Energy
To raise an object of mass $m$ to height $h$:
- Minimum upward force required $= mg$.
- Work done $W = F \\cdot s = mg \\cdot h$.
- This work is stored as **gravitational potential energy**:
  $$U = mgh \\quad [\\text{SI unit: } \\text{Joule (J)}]$$

### 7.6 Mathematical Proof of Conservation of Mechanical Energy
Consider a body of mass $m$ falling freely from height $h$ ($g$ constant):
1. **At Top (Point A, height $h$)**:
   - $v_A = 0 \\implies K_A = 0$.
   - $U_A = mgh$.
   - Total Energy $E_A = K_A + U_A = mgh$.
2. **At Intermediate Point B (fallen distance $x$, height $h-x$)**:
   - Velocity $v_B^2 = u^2 + 2gx = 2gx$.
   - $K_B = \\frac{1}{2}m v_B^2 = \\frac{1}{2}m(2gx) = mgx$.
   - $U_B = mg(h - x)$.
   - Total Energy $E_B = mgx + mg(h - x) = mgh$.
3. **At Ground (Point C, fallen distance $h$, height $0$)**:
   - Velocity $v_C^2 = 2gh$.
   - $K_C = \\frac{1}{2}m(2gh) = mgh$.
   - $U_C = 0$.
   - Total Energy $E_C = mgh + 0 = mgh$.

Hence, $E_A = E_B = E_C = mgh$ at all points!""",
    "worked_examples": [
      {
        "problem": "Find the energy possessed by an object of mass 10 kg when it is at a height of 6 m above the ground. Given g = 9.8 m/s^2.",
        "given": "Mass m = 10 kg | Height h = 6 m | g = 9.8 m/s^2",
        "formula": "U = mgh",
        "substitution": "U = 10 kg * 9.8 m/s^2 * 6 m",
        "calculation": "98 * 6 = 588 J",
        "finalAnswer": "Potential Energy = 588 Joules",
        "unit": "Joules (J)"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Dragging an object up a ramp requires more work against gravity than lifting it straight up.",
        "correction": "Gravitational potential energy is strictly path-independent! The vertical height h is the only variable that determines gravitational work W = mgh. (The ramp reduces required force by increasing distance).",
        "why_it_matters": "Fundamental conservative force property tested on CBSE physics exams."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Free Fall Conservation of Energy Graph",
      "diagram_type": "graph",
      "concept_visuals": [
        {
          "concept_title": "Interchange of Kinetic and Potential Energy",
          "diagram_title": "Energy vs Height Coordinate Plot",
          "diagram_type": "graph",
          "what_to_make": "Dual plot of U = mgh (linear decline) and K = mg(H-h) (linear rise) summing to constant horizontal line E = mgh",
          "timing_and_cue": "Mount energy conservation plot on Step 1: plot_mathematical_graph(formula=\"-10*x + 100; 10*x; 100\", domain=\"[0, 10]\", range=\"[0, 120]\", title=\"Conservation of Mechanical Energy: U, K, and Total E\", callout=\"U decreases as K increases, keeping Total E = 100 J constant\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, call plot_mathematical_graph(formula=\"-10*x + 100; 10*x; 100\", domain=\"[0, 10]\", range=\"[0, 120]\", title=\"Conservation of Energy: U, K, and Total E\", callout=\"Sum is constant 100 J\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH7_ID,
    "order_index": 4,
    "title": "Power Dynamics & Commercial Electrical Energy Measurement",
    "description": "Define power as rate of doing work P = W/t, understand 1 Watt and Horsepower, calculate commercial electrical energy consumption in kilowatt-hours (kWh), and solve utility billing numericals.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Power Definition: Rate of doing work or rate of energy consumption (P = W/t)",
      "Units of Power: Watt (W), Kilowatt (kW), Megawatt (MW), Horsepower (1 hp = 746 W)",
      "Average Power: Total energy consumed divided by total time taken",
      "Commercial Unit of Electrical Energy: Kilowatt-hour (kWh) or 'Unit'",
      "Conversion: 1 kWh = 3.6 * 10^6 Joules (3.6 MJ)",
      "Household Electricity Bill Calculation: Summing appliance wattage * hours used"
    ],
    "key_concepts": [
      "Power: Rate at which work is done or energy is transformed ($P = \\frac{W}{t} = F \\cdot v$).",
      "Watt: Power of an appliance that consumes 1 Joule of energy in 1 second ($1\\text{ W} = 1\\text{ J/s}$).",
      "Commercial Unit (kWh): Energy consumed by a 1000 Watt appliance running for 1 hour ($1\\text{ kWh} = 3.6 \\times 10^6\\text{ J}$).",
      "Electrical Billing: Energy in $\\text{kWh} = \\frac{\\text{Power (W)} \\times \\text{Time (hours)}}{1000}$."
    ],
    "success_criteria": "Student can compute power output, convert kilowatt-hours to joules, and calculate monthly household electricity bills.",
    "chapter_notes": """### 7.7 Power: Rate of Energy Transfer
$$P = \\frac{W}{t} = \\frac{E}{t} \\quad [\\text{SI unit: } \\text{Watt (W)}]$$
- $1\\text{ Watt} = 1\\text{ J/s}$.
- $1\\text{ Kilowatt (kW)} = 1000\\text{ W}$.
- $1\\text{ Horsepower (hp)} = 746\\text{ W}$.

### 7.8 Commercial Unit of Energy: Kilowatt-hour (kWh)
The Joule is too small for commercial billing:
$$1\\text{ kWh} = 1\\text{ kW} \\times 1\\text{ hour} = 1000\\text{ W} \\times 3600\\text{ s} = 3,600,000\\text{ J} = 3.6 \\times 10^6\\text{ J}$$
- 1 kilowatt-hour is commonly termed **1 Unit** of electricity on electric meters.""",
    "worked_examples": [
      {
        "problem": "An electric bulb of 60 W is used for 6 hours per day. Calculate the 'units' of energy consumed in one day by the bulb.",
        "given": "Power P = 60 W = 60 / 1000 kW = 0.06 kW | Time t = 6 hours",
        "formula": "Energy = Power (kW) * Time (hours)",
        "substitution": "Energy = 0.06 kW * 6 hours",
        "calculation": "0.06 * 6 = 0.36 kWh",
        "finalAnswer": "Energy consumed = 0.36 units (0.36 kWh)",
        "unit": "kWh (units)"
      },
      {
        "problem": "Two girls, each of weight 400 N, climb up a rope through a height of 8 m. Girl A takes 20 s while Girl B takes 50 s. What is the power expended by each girl?",
        "given": "Weight mg = 400 N | Height h = 8 m | Work W = 400 * 8 = 3200 J | t_A = 20 s | t_B = 50 s",
        "formula": "Power P = Work / time",
        "substitution": "P_A = 3200 / 20; P_B = 3200 / 50",
        "calculation": "P_A = 160 W; P_B = 64 W",
        "finalAnswer": "Girl A Power = 160 W | Girl B Power = 64 W",
        "unit": "Watts (W)"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Kilowatt-hour is a unit of power because it has kilowatt in the name.",
        "correction": "Kilowatt-hour is a unit of ENERGY! Power multiplied by time (kW * h) yields work or energy (Joules).",
        "why_it_matters": "Universal board exam trap question testing definition of kWh."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Commercial Electricity Measurement Flowchart",
      "diagram_type": "flowchart",
      "concept_visuals": [
        {
          "concept_title": "Watts to Kilowatt-Hours and Monthly Billing Workflow",
          "diagram_title": "Electricity Billing Calculation Flowchart",
          "diagram_type": "flowchart",
          "what_to_make": "Watts * Hours / 1000 -> Daily kWh -> Total 30 Days Units -> Multiply by Rate per Unit = Final Bill",
          "timing_and_cue": "Mount electricity calculation flowchart on Step 1: write_chalkboard(action=\"draw_flowchart\", content=\"Appliance Wattage * Daily Hours / 1000 -> Daily kWh (Units) -> Monthly Units (x30) -> Total Bill (Units x Tariff Rate)\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount electricity billing flowchart: write_chalkboard(action=\"draw_flowchart\", content=\"Appliance Wattage * Daily Hours / 1000 -> Daily Units -> Monthly Units -> Total Bill\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH7_ID,
    "order_index": 5,
    "title": "Simple Machines: Mechanical Advantage, Velocity Ratio, Pulleys, Inclined Planes & Levers",
    "description": "Understand how simple machines transform effort into load, define Mechanical Advantage, Velocity Ratio, and Efficiency, and analyze Class 1, 2, 3 levers, pulleys, and inclined planes.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Simple Machine Principle: Magnifying force or changing direction without violating conservation of energy",
      "Key Metrics: Mechanical Advantage (MA = Load/Effort), Velocity Ratio (VR = dE/dL), Efficiency (eta = MA/VR)",
      "Pulleys: Single fixed pulley (VR = 1, changes direction) vs Single movable pulley (VR = 2, force multiplier)",
      "Inclined Plane: Mechanical advantage MA = L / h = 1 / sin(theta)",
      "Levers: Fulcrum, Load, Effort; Principle of Moments (Load * Load Arm = Effort * Effort Arm)",
      "Three Classes of Levers: Class 1 (Fulcrum in middle: scissors), Class 2 (Load in middle: wheelbarrow), Class 3 (Effort in middle: tweezers)"
    ],
    "key_concepts": [
      "Mechanical Advantage: Ratio of resistance force (Load) to applied force (Effort): $MA = \\frac{L}{E}$.",
      "Velocity Ratio: Ratio of distance moved by effort to distance moved by load: $VR = \\frac{d_E}{d_L}$.",
      "Efficiency: $\\eta = \\frac{\\text{Work Output}}{\\text{Work Input}} = \\frac{MA}{VR}$. In ideal frictionless machine, $\\eta = 100\\%$ ($MA = VR$).",
      "Levers Classification: Mnemonic FLE (1 = Fulcrum middle, 2 = Load middle, 3 = Effort middle)."
    ],
    "success_criteria": "Student can identify lever classes, calculate mechanical advantage and efficiency of pulleys and inclined planes, and state the Principle of Moments.",
    "chapter_notes": """### 7.9 Physics of Simple Machines
A simple machine does not create energy; it reduces the required effort force by increasing effort distance:
$$\\text{Work Input } (E \\cdot d_E) \\ge \\text{Work Output } (L \\cdot d_L)$$

### 7.10 The Core Performance Formulas
1. **Mechanical Advantage (MA)**: $MA = \\frac{\\text{Load (L)}}{\\text{Effort (E)}}$
2. **Velocity Ratio (VR)**: $VR = \\frac{\\text{Distance moved by Effort } (d_E)}{\\text{Distance moved by Load } (d_L)}$
3. **Efficiency ($\\eta$)**: $\\eta = \\frac{\\text{Work Output}}{\\text{Work Input}} = \\frac{MA}{VR} \\times 100\\%$

### 7.11 The Three Classes of Levers (FLE Rule)
| Class | Middle Element | Formula / MA | Real-World Examples |
| :--- | :--- | :--- | :--- |
| **Class 1** | **Fulcrum (F)** | $MA > 1, = 1, < 1$ | Crowbar, See-saw, Scissors, Pliers |
| **Class 2** | **Load (L)** | $MA > 1$ (Force multiplier) | Wheelbarrow, Nutcracker, Bottle opener |
| **Class 3** | **Effort (E)** | $MA < 1$ (Speed/Distance multiplier) | Tongs, Tweezers, Human forearm, Fishing rod |""",
    "worked_examples": [
      {
        "problem": "A crowbar 2 m long is used to lift a rock of weight 1000 N. The fulcrum is placed 0.4 m from the rock. Calculate: (a) Effort arm, (b) Mechanical advantage of crowbar, (c) Minimum effort required.",
        "given": "Total length = 2 m | Load arm = 0.4 m | Load = 1000 N",
        "formula": "Effort arm = Total length - Load arm; MA = Effort arm / Load arm; Effort = Load / MA",
        "substitution": "Effort arm = 2 - 0.4 = 1.6 m; MA = 1.6 / 0.4; Effort = 1000 / 4",
        "calculation": "MA = 4; Effort = 250 N",
        "finalAnswer": "(a) Effort arm = 1.6 m | (b) MA = 4 | (c) Minimum effort = 250 N",
        "unit": "N and dimensionless"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "A machine with efficiency less than 100% is useless.",
        "correction": "All real machines have friction (eta < 100%), but they remain invaluable because they allow lifting a huge load with tiny human effort or changing direction comfortably.",
        "why_it_matters": "Clarifies practical engineering utility vs thermodynamic conservation of energy."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Classes of Levers FLE Schematic",
      "diagram_type": "flowchart",
      "concept_visuals": [
        {
          "concept_title": "Class 1, 2, and 3 Levers Comparison",
          "diagram_title": "Levers Classification Diagram",
          "diagram_type": "flowchart",
          "what_to_make": "Class 1: Effort - Fulcrum - Load | Class 2: Fulcrum - Load - Effort (MA > 1) | Class 3: Fulcrum - Effort - Load (Speed multiplier)",
          "timing_and_cue": "Mount lever classes flowchart on Step 1: write_chalkboard(action=\"draw_flowchart\", content=\"Class 1: Effort - Fulcrum - Load (Scissors) | Class 2: Fulcrum - Load - Effort (Wheelbarrow MA>1) | Class 3: Fulcrum - Effort - Load (Tweezers Speed Multiplier)\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount lever classes flowchart: write_chalkboard(action=\"draw_flowchart\", content=\"Class 1: Effort-Fulcrum-Load | Class 2: Fulcrum-Load-Effort (MA>1) | Class 3: Fulcrum-Effort-Load (Tweezers)\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH7_ID,
    "order_index": 6,
    "title": "Master Numerical Solver: Work, Energy, Power & Machine Calculations",
    "description": "Solve high-yield board exam numericals on elevator lifting power, bullet stopping distance, pendulum energy transformation, and complete the 10-MCQ diagnostic evaluation.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Elevator and Pump Power Calculations with Gravity and Friction",
      "Bullet Penetration Work and Kinetic Energy Depletion",
      "Simple Pendulum Energy Transformation at Mean vs Extreme Positions",
      "Comprehensive NCERT Chapter-End Problem Review",
      "Diagnostic 10-MCQ Evaluation Quiz"
    ],
    "key_concepts": [
      "Pump & Elevator Power: $P = \\frac{mgh}{t} = \\rho V g \\frac{h}{t}$.",
      "Bullet Penetration: Average retarding force $F = \\frac{\\frac{1}{2}mv^2}{s}$.",
      "Simple Pendulum Invariant: At extreme position, energy is 100% potential ($mgh$); at mean position, energy is 100% kinetic ($\\frac{1}{2}mv^2$)."
    ],
    "success_criteria": "Student completes all multi-tier physics calculations with correct SI units and achieves >= 80% on chapter quiz.",
    "chapter_notes": """### 7.12 Master Problem Solving Formulas
1. **Work**: $W = F s \\cos\\theta$
2. **Kinetic Energy**: $K = \\frac{1}{2}mv^2$
3. **Potential Energy**: $U = mgh$
4. **Conservation of Energy**: $K_1 + U_1 = K_2 + U_2$
5. **Power**: $P = \\frac{W}{t} = \\frac{mgh}{t}$
6. **Commercial Energy**: $\\text{Units (kWh)} = \\frac{\\text{Watts} \\times \\text{hours}}{1000}$""",
    "worked_examples": [
      {
        "problem": "An electric pump of power 2 kW lifts water through a height of 10 m in 1 minute. How much water in liters can it lift? (Take g = 10 m/s^2, density of water = 1000 kg/m^3)",
        "given": "Power P = 2 kW = 2000 W | Height h = 10 m | Time t = 1 min = 60 s | g = 10 m/s^2",
        "formula": "P = mgh / t => m = (P * t) / (gh)",
        "substitution": "m = (2000 * 60) / (10 * 10)",
        "calculation": "Numerator = 120,000; Denominator = 100; m = 120,000 / 100 = 1200 kg. Since 1 kg water = 1 L, Volume = 1200 L.",
        "finalAnswer": "Mass = 1200 kg; Volume = 1200 Liters",
        "unit": "Liters"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Time in power formulas can be in minutes.",
        "correction": "SI unit of time is SECONDS! If time is given in minutes or hours, it MUST be converted to seconds (1 min = 60 s) before calculating Watts.",
        "why_it_matters": "Using minutes directly leads to an answer 60 times smaller, losing full numerical marks."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Work Energy Power Master Formula Sheet",
      "diagram_type": "flowchart",
      "concept_visuals": [
        {
          "concept_title": "Energy Transformation and Power Matrix",
          "diagram_title": "Work Energy Power Synthesis Flowchart",
          "diagram_type": "flowchart",
          "what_to_make": "Force x Displacement -> Work (J) -> Rate of Work -> Power (W) -> Commercial Energy -> Units (kWh)",
          "timing_and_cue": "Mount master formula flowchart on Step 1: write_chalkboard(action=\"draw_flowchart\", content=\"Force x Distance -> Work (Joules) -> / Time -> Power (Watts) -> x Hours / 1000 -> Commercial Units (kWh)\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount formula flowchart: write_chalkboard(action=\"draw_flowchart\", content=\"Force x Distance -> Work (Joules) -> / Time -> Power (Watts) -> Commercial Units (kWh)\").\n2. 6-STAGE SOCRATIC CADENCE."
  }
]
all_modules.extend(ch7)

# --- CHAPTER 8 ---
ch8 = [
  {
    "curriculum_id": CH8_ID,
    "order_index": 1,
    "title": "The Subatomic Revolution: Cathode Rays, Canal Rays & Discovery of Electron and Proton",
    "description": "Trace the experimental collapse of Dalton's indivisible atom, explore gas discharge tube experiments by J.J. Thomson (electrons) and E. Goldstein (canal rays/protons).",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Dalton's Atomic Theory Limitation: Assumption of indivisible, indestructible hard spheres",
      "Static Electricity Evidence: Rubbing glass rod with silk or comb with dry hair proving charge transfer",
      "Cathode Ray Discharge Tube Experiment (J.J. Thomson, 1897): Low pressure, high voltage, green ZnS glow",
      "Properties of Cathode Rays: Travel in straight lines, possess mass, deflected toward positive plate (negatively charged electrons)",
      "Canal Rays (Anode Rays) Discovery (E. Goldstein, 1886): Perforated cathode, positively charged subatomic ions (protons)"
    ],
    "key_concepts": [
      "Subatomic Particles: The atom is not indivisible; it is composed of smaller subatomic particles (electrons, protons, neutrons).",
      "Electron: Negatively charged subatomic particle discovered by J.J. Thomson (charge: $-1.6 \\times 10^{-19}\\text{ C}$, mass: $9.1 \\times 10^{-31}\\text{ kg} \\approx 1/2000\\text{ mass of H atom}$).",
      "Proton: Positively charged subatomic particle discovered by E. Goldstein (charge: $+1.6 \\times 10^{-19}\\text{ C}$, mass: $1.67 \\times 10^{-27}\\text{ kg} \\approx 1\\text{ u}$).",
      "Electrical Neutrality: An atom is electrically neutral because total positive proton charge equals total negative electron charge."
    ],
    "success_criteria": "Student can compare electron and proton masses and charges, sketch cathode ray tube apparatus, and explain why Dalton's theory was revised.",
    "chapter_notes": """### 8.1 The Fall of Indivisibility
Dalton's model regarded atoms as ultimate indivisible particles. Late 19th-century experiments proved atoms are divisible:
1. **Discovery of the Electron (J.J. Thomson, 1897)**:
   - High voltage ($10,000\\text{ V}$) applied across electrodes in a glass discharge tube at ultra-low gas pressure ($0.01\\text{ mm Hg}$).
   - Rays emitted from cathode (negative) traveling toward anode (positive), causing a green phosphorescent glow on zinc sulfide screen.
   - Deflection toward the positive plate in an electric field proved these particles carry **negative charge**.
   - Mass $= \\frac{1}{1840}$ of a hydrogen atom ($9.1 \\times 10^{-31}\\text{ kg}$).

2. **Discovery of the Proton (E. Goldstein, 1886)**:
   - Using a **perforated cathode** in discharge tube, rays traveling in opposite direction from anode through holes were discovered (Canal Rays).
   - Consisted of positively charged particles. Mass $\\approx 2000$ times that of an electron ($1.67 \\times 10^{-27}\\text{ kg}$).""",
    "worked_examples": [
      {
        "problem": "Compare an electron and a proton with respect to: (a) Charge, (b) Mass, (c) Location in the atom.",
        "given": "Subatomic comparison between e- and p+.",
        "formula": "Tabular comparative matrix of fundamental subatomic particles.",
        "substitution": "Electron: -1.6e-19 C, 1/1840 u, extra-nuclear orbits; Proton: +1.6e-19 C, 1 u, inside nucleus.",
        "calculation": "Charge magnitude is identical (1.602 * 10^-19 C) but opposite in sign. Proton is 1840 times heavier than electron.",
        "finalAnswer": "Electron: -1 charge, 9.1x10^-31 kg, orbits | Proton: +1 charge, 1.67x10^-27 kg, nucleus",
        "unit": "Subatomic Comparison"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Protons and electrons have different amounts of electrical charge.",
        "correction": "The MAGNITUDE of charge is exactly identical (1.602 * 10^-19 C)! Only the sign is opposite (+1 vs -1), which guarantees total electrical neutrality.",
        "why_it_matters": "Core foundational principle for atomic number and chemical valency."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Cathode Ray Discharge Tube Apparatus Schematic",
      "diagram_type": "image",
      "concept_visuals": [
        {
          "concept_title": "Cathode Ray Gas Discharge Tube Setup",
          "diagram_title": "Cathode Ray Tube Schematic",
          "diagram_type": "image",
          "image_search_query": "Cathode ray tube experiment JJ Thomson diagram",
          "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Crookes_tube_diagram-en.svg",
          "what_to_make": "Vector diagram of cathode, anode, high-voltage induction source, vacuum pump connection, and fluorescent glow screen.",
          "timing_and_cue": "Mount discharge tube on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/ea/Crookes_tube_diagram-en.svg | Cathode Ray Tube Setup | High-voltage gas discharge tube with cathode rays deflecting toward positive plate\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount discharge tube: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/ea/Crookes_tube_diagram-en.svg | Cathode Ray Tube Setup | JJ Thomson discharge tube proving existence of negatively charged electrons\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH8_ID,
    "order_index": 2,
    "title": "Thomson's Plum Pudding Model vs Rutherford's Gold Foil Scattering Experiment",
    "description": "Contrast J.J. Thomson's plum pudding model with Ernest Rutherford's historic alpha-particle gold foil scattering experiment, analyzing observations and nuclear inferences.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Thomson's Model of the Atom: Positive sphere with embedded electrons ('Plum pudding' or 'Watermelon' model)",
      "Success and Failure of Thomson's Model: Explained electrical neutrality but failed scattering tests",
      "Rutherford's Alpha-Particle Scattering Experiment: Setup (Alpha-source, thin gold foil 100 nm, ZnS circular screen)",
      "Three Landmark Observations: (1) Most pass straight, (2) Small deflections, (3) 1 in 12,000 rebounds at 180 degrees",
      "Three Inferences: Most of atom is empty space, positive charge concentrated in tiny volume, mass concentrated in nucleus"
    ],
    "key_concepts": [
      "Thomson's Model: Atom consists of a positively charged sphere with electrons embedded in it like raisins in a pudding.",
      "Alpha Particle: Doubly-charged helium ion ($He^{2+}$, mass = $4\\text{ u}$, high kinetic energy).",
      "Rutherford's Inferences: (1) Most space in an atom is empty, (2) Positive charge occupies very little volume, (3) All mass is concentrated in a tiny central nucleus ($10^{-15}\\text{ m}$ vs atom $10^{-10}\\text{ m}$)."
    ],
    "success_criteria": "Student can sketch the gold foil experiment, list all 3 observations with corresponding inferences, and explain why alpha particles rebounded.",
    "chapter_notes": """### 8.2 Thomson's Plum Pudding Model (1904)
- Atom proposed as a uniform positively charged sphere of radius $\\approx 10^{-10}\\text{ m}$.
- Electrons embedded throughout like seeds in a watermelon or raisins in pudding.
- Major failure: Could not explain why alpha particles scatter at large angles!

### 8.3 Rutherford's Gold Foil Scattering Experiment (1911)
- Targeted high-energy $\\alpha$-particles ($He^{2+}$) at an ultra-thin gold sheet ($1000$ atoms thick $\\approx 0.00004\\text{ cm}$).
- **Observations and Inferences**:
  | Observation | Physical Inference |
  | :--- | :--- |
  | 1. Most $\\alpha$-particles passed straight through without deflection ($> 99\\%$) | Most of the interior of the atom is **empty space**. |
  | 2. A small fraction deflected through small angles | Positive charge is **concentrated** in a small localized region, repelling positive $\\alpha$-particles. |
  | 3. Surprisingly, 1 in 12,000 rebounded straight back ($180^\\circ$) | Nucleus is **extremely dense, heavy, and tiny**, carrying almost all atomic mass! |""",
    "worked_examples": [
      {
        "problem": "On the basis of Rutherford's model of an atom, which subatomic particle is present in the nucleus of an atom?",
        "given": "Rutherford nuclear model.",
        "formula": "Central heavy positive charge.",
        "substitution": "Positive charge in nucleus is due to protons.",
        "calculation": "Rutherford proved the nucleus contains all positive charge (protons) and almost the entire atomic mass, while electrons orbit outside.",
        "finalAnswer": "The proton (positively charged subatomic particle) is present in the nucleus.",
        "unit": "Nuclear Subatomic Location"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Alpha particles rebounded because they hit electrons.",
        "correction": "Alpha particles are 7300 times heavier than electrons! An alpha particle would easily plow through an electron. It rebounded because it encountered the intensely concentrated positive electrostatic field and mass of the gold nucleus.",
        "why_it_matters": "Rutherford famous quote: 'It was as if you fired a 15-inch shell at a piece of tissue paper and it came back and hit you.'"
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Rutherford Alpha Scattering Experiment Schematic",
      "diagram_type": "image",
      "concept_visuals": [
        {
          "concept_title": "Rutherford Gold Foil Experiment Setup & Rays",
          "diagram_title": "Rutherford Gold Foil Scattering Setup",
          "diagram_type": "image",
          "image_search_query": "Rutherford gold foil experiment alpha scattering diagram",
          "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/77/Geiger-Marsden_experiment_expectation_and_result.svg",
          "what_to_make": "Vector diagram comparing Thomson's expected undeflected rays on left vs Rutherford's actual deflected and rebounding rays on right.",
          "timing_and_cue": "Mount Rutherford scattering diagram on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/7/77/Geiger-Marsden_experiment_expectation_and_result.svg | Rutherford Gold Foil Scattering | Expected plum pudding rays vs actual rebounding nuclear deflection\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount Rutherford scattering comparison: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/7/77/Geiger-Marsden_experiment_expectation_and_result.svg | Rutherford Gold Foil Scattering | Alpha deflection proving tiny dense central nucleus\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH8_ID,
    "order_index": 3,
    "title": "Rutherford's Planetary Model, Its Fatal Limitation & Bohr's Quantum Paradigm",
    "description": "Analyze Rutherford's planetary model, understand the electromagnetic radiation collapse paradox, and explore Neils Bohr's revolutionary postulates of quantized stationary orbits.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Rutherford's Nuclear Planetary Model: Central positive nucleus orbited by electrons in circular paths",
      "The Fatal Limitation (Maxwell's Classical Electrodynamics): Accelerated charges radiate electromagnetic energy",
      "The Collapse Paradox: Spiraling electron must crash into nucleus within 10^-8 seconds, making matter unstable",
      "Neils Bohr's Postulates (1913): Discrete stationary orbits with non-radiating states",
      "Energy Levels: Quantum numbers n = 1, 2, 3, 4 corresponding to K, L, M, N electron shells",
      "Photon Emission and Absorption: Delta E = E2 - E1 = h*nu during orbital transitions"
    ],
    "key_concepts": [
      "Electromagnetic Instability: According to classical physics, an electron in circular orbit experiences centripetal acceleration and must radiate energy, spiraling into the nucleus.",
      "Bohr's First Postulate: Only certain special discrete orbits known as **stationary orbits** of electrons are allowed inside the atom.",
      "Bohr's Second Postulate: While revolving in discrete orbits, electrons **do not radiate energy**.",
      "Energy Shells: Concentric shells labeled $K, L, M, N$ or integers $n = 1, 2, 3, 4$ representing fixed energy levels."
    ],
    "success_criteria": "Student can explain the failure of Rutherford's model, state Bohr's two postulates, and draw Bohr's concentric energy shell model.",
    "chapter_notes": """### 8.4 Rutherford's Nuclear Model of the Atom
1. Positive charge and mass concentrated in a very small nucleus.
2. Electrons revolve around the nucleus in circular orbits.
3. Size of nucleus is very small ($10^{-5}$ times) compared to the atom.

### 8.5 The Fatal Flaw of Rutherford's Model
- Any charged particle undergoing circular motion accelerates centripetally.
- According to Maxwell's electromagnetic theory, accelerated charges must continuously radiate energy.
- Thus, the revolving electron would lose energy continuously, its orbit would shrink in a spiral, and it would crash into the nucleus in $10^{-8}\\text{ s}$.
- But atoms are completely **stable**! Rutherford's model could not explain atomic stability.

### 8.6 Neils Bohr's Quantum Breakthrough (1913)
To resolve this paradox, Neils Bohr formulated two revolutionary postulates:
1. **Discrete Non-Radiating Orbits**: Only certain special orbits called **stationary orbits** are permitted.
2. **Radiation-Free Motion**: While revolving in these discrete orbits, electrons do not radiate energy.
3. Electrons only radiate or absorb energy when jumping from one energy level to another:
   $$\\Delta E = E_{\\text{higher}} - E_{\\text{lower}} = h\\nu$$
4. These orbits/shells are designated by letters **K, L, M, N...** or quantum numbers **n = 1, 2, 3, 4...**""",
    "worked_examples": [
      {
        "problem": "State the limitations of Rutherford's model of the atom and how Neils Bohr overcame them.",
        "given": "Comparison of Rutherford vs Bohr models from NCERT Section 8.2.",
        "formula": "Limitation: Accelerated charge radiates energy -> orbital collapse. Bohr solution: Discrete stationary non-radiating energy shells.",
        "substitution": "Rutherford could not explain atomic stability under Maxwell electrodynamics. Bohr postulated quantized orbits K, L, M, N where electrons revolve without radiating energy.",
        "calculation": "In Bohr orbits, angular momentum is quantized: mvr = n*h / (2*pi). Energy changes only during inter-shell transitions.",
        "finalAnswer": "Rutherford's model suffered electromagnetic collapse; Bohr introduced stationary non-radiating energy shells (K, L, M, N).",
        "unit": "Atomic Theory Evolution"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Electrons continuously radiate light as they orbit the nucleus.",
        "correction": "Electrons radiate ZERO light while in their stable stationary orbits! They emit light only when jumping downward from a higher energy shell to a lower energy shell.",
        "why_it_matters": "Bohr's fundamental quantum postulate explaining why matter does not collapse."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Bohr Concentric Energy Shells Diagram",
      "diagram_type": "image",
      "concept_visuals": [
        {
          "concept_title": "Bohr Atomic Model Energy Levels K, L, M, N",
          "diagram_title": "Bohr Model Energy Shells",
          "diagram_type": "image",
          "image_search_query": "Bohr model atom concentric energy shells K L M N",
          "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/55/Bohr-atom-PAR.svg",
          "what_to_make": "Vector diagram of central nucleus (+), with concentric circular shells n=1 (K), n=2 (L), n=3 (M), n=4 (N) and transition energy emission arrows.",
          "timing_and_cue": "Mount Bohr concentric shells on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/5/55/Bohr-atom-PAR.svg | Bohr Concentric Energy Shells | Stationary orbits n=1 (K), n=2 (L), n=3 (M), n=4 (N) with zero radiation in orbit\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount Bohr energy shells: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/5/55/Bohr-atom-PAR.svg | Bohr Energy Levels | Concentric stationary non-radiating shells K, L, M, N\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH8_ID,
    "order_index": 4,
    "title": "Electron Distribution (Bohr-Bury Rules), Atomic Shell Filling & Discovery of Neutron",
    "description": "Master the Bohr-Bury rules for distributing electrons in shells (2n^2, octet rule), trace the discovery of the neutron by James Chadwick (1932), and write configurations for elements 1 to 20.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Discovery of the Neutron (James Chadwick, 1932): Bombarding Beryllium with alpha particles",
      "Properties of Neutron: Neutral charge, mass 1.675 * 10^-27 kg approx 1 u, located in nucleus",
      "Bohr-Bury Rule 1: Maximum electron capacity of shell is 2n^2 (K=2, L=8, M=18, N=32)",
      "Bohr-Bury Rule 2: Maximum number of electrons in outermost valence shell is 8 (Octet Rule)",
      "Bohr-Bury Rule 3: Step-wise shell filling (inner shells must fill before outer shell begins)",
      "Electronic Configurations of First 20 Elements: Hydrogen (1) to Calcium (2, 8, 8, 2)"
    ],
    "key_concepts": [
      "Neutron ($n$): Subatomic particle residing in the nucleus having no electrical charge and mass equal to $1.00866\\text{ u} \\approx 1\\text{ u}$.",
      "Bohr-Bury $2n^2$ Rule: Shell capacities are $K(n=1) = 2$, $L(n=2) = 8$, $M(n=3) = 18$, $N(n=4) = 32$.",
      "Octet Rule: The outermost shell cannot hold more than 8 electrons, regardless of whether its maximum $2n^2$ capacity is higher.",
      "Step-wise Filling: Electrons cannot occupy a higher shell until the inner shells are fully filled."
    ],
    "success_criteria": "Student can write electronic configurations for elements 1 through 20 (H to Ca) and apply Bohr-Bury rules correctly.",
    "chapter_notes": """### 8.7 Discovery of the Neutron (Chadwick, 1932)
- In 1932, **J. Chadwick** discovered an uncharged subatomic particle by bombarding a thin sheet of beryllium with $\\alpha$-particles:
  $$^9_4\\text{Be} + ^4_2\\alpha \\to ^{12}_6\\text{C} + ^1_0n$$
- Mass $\\approx$ mass of proton ($1.675 \\times 10^{-27}\\text{ kg}$). Symbol: $n$.
- Located inside the nucleus alongside protons. (Hydrogen atom $^1_1H$ is the ONLY atom with NO neutrons).

### 8.8 The Bohr-Bury Rules for Electron Distribution
1. **Rule 1 (Formula $2n^2$)**:
   - $K$-shell ($n=1$): $2(1)^2 = \\mathbf{2}$
   - $L$-shell ($n=2$): $2(2)^2 = \\mathbf{8}$
   - $M$-shell ($n=3$): $2(3)^2 = \\mathbf{18}$
   - $N$-shell ($n=4$): $2(4)^2 = \\mathbf{32}$
2. **Rule 2 (Octet Boundary)**:
   - The maximum number of electrons that can be accommodated in the outermost shell is **8**.
3. **Rule 3 (Step-wise Inward Filling)**:
   - Electrons are not accommodated in a given shell unless the inner shells are filled.
   - Example: Potassium ($Z=19$) fills as $2, 8, 8, 1$ (NOT $2, 8, 9$) because outer shell cannot exceed 8 before starting next shell! Calcium ($Z=20$) is $2, 8, 8, 2$.""",
    "worked_examples": [
      {
        "problem": "Write the distribution of electrons in carbon and sodium atoms.",
        "given": "Carbon (Atomic number Z = 6), Sodium (Atomic number Z = 11).",
        "formula": "Bohr-Bury distribution: 2n^2 rule and octet boundary.",
        "substitution": "Carbon: K=2, L=4; Sodium: K=2, L=8, M=1.",
        "calculation": "For Carbon: 6 electrons -> K shell takes 2, remaining 4 go to L shell. For Sodium: 11 electrons -> K takes 2, L takes 8 (now full), remaining 1 goes to M shell.",
        "finalAnswer": "Carbon = (2, 4) | Sodium = (2, 8, 1)",
        "unit": "Electronic Configuration"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Potassium (Z=19) configuration is 2, 8, 9 because the M shell can hold up to 18 electrons.",
        "correction": "Rule 2 dictates the outermost shell CANNOT hold more than 8 electrons! Once the M shell reaches 8, the next electron must enter the N shell, giving 2, 8, 8, 1 for K and 2, 8, 8, 2 for Ca.",
        "why_it_matters": "One of the most frequently failed questions on CBSE Class 9 science exams."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Electronic Configuration of First 20 Elements Table",
      "diagram_type": "flowchart",
      "concept_visuals": [
        {
          "concept_title": "Bohr-Bury Shell Capacities and Sequence",
          "diagram_title": "Bohr-Bury Shell Capacity Table",
          "diagram_type": "flowchart",
          "what_to_make": "K (n=1, max 2) -> L (n=2, max 8) -> M (n=3, max 18, octet 8) -> N (n=4, max 32); Examples: H(1), He(2), C(2,4), Na(2,8,1), Cl(2,8,7), Ca(2,8,8,2)",
          "timing_and_cue": "Mount shell filling flowchart on Step 1: write_chalkboard(action=\"draw_flowchart\", content=\"K (n=1, max 2) -> L (n=2, max 8) -> M (n=3, max 18, octet 8) -> N (n=4, max 32); Examples: H(1), He(2), C(2,4), Na(2,8,1), Cl(2,8,7), Ca(2,8,8,2)\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount Bohr-Bury shell layout: write_chalkboard(action=\"draw_flowchart\", content=\"K(2) -> L(8) -> M(18, octet 8) -> N(32); Examples: H(1), He(2), C(2,4), Na(2,8,1), Cl(2,8,7), Ca(2,8,8,2)\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH8_ID,
    "order_index": 5,
    "title": "Valence Electrons, Valency Mechanics & Chemical Stability",
    "description": "Understand valence electrons, define valency as combining capacity to achieve duplet/octet stability, calculate valency for metals and non-metals, and explain noble gas unreactivity.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Valence Electrons: Electrons present in the outermost shell of an atom",
      "Chemical Stability: The Duplet Rule (Helium: 2) and Octet Rule (Neon, Argon: 8)",
      "Definition of Valency: Combining capacity of an atom to attain stable noble gas configuration",
      "Valency Calculation for Metals (Valence e- = 1, 2, 3): Valency = valence electrons (loss of electrons)",
      "Valency Calculation for Non-metals (Valence e- = 5, 6, 7): Valency = 8 - valence electrons (gain of electrons)",
      "Zero Valency of Inert Noble Gases: Completely filled valence shell"
    ],
    "key_concepts": [
      "Valence Electrons: Outermost shell electrons that take part in chemical bonding.",
      "Valency: Combining capacity of an element, determined by the number of electrons an atom must gain, lose, or share to attain an octet.",
      "Metal Rule: $\\text{Valency} = \\text{number of valence electrons}$ (e.g. $Na(2,8,1) \\implies 1$, $Mg(2,8,2) \\implies 2$, $Al(2,8,3) \\implies 3$).",
      "Non-metal Rule: $\\text{Valency} = 8 - \\text{valence electrons}$ (e.g. $N(2,5) \\implies 8-5=3$, $O(2,6) \\implies 8-6=2$, $F(2,7) \\implies 8-7=1$).",
      "Noble Gas Rule: Valency $= 0$ because valence shell is already completely saturated."
    ],
    "success_criteria": "Student can determine the valency of any element from its atomic number and explain why atoms bond chemically.",
    "chapter_notes": """### 8.9 Valence Electrons & The Octet Rule
- An atom with an outermost shell having **8 electrons** (or **2 electrons** for Helium) possesses maximum stability.
- Atoms react chemically by gaining, losing, or sharing electrons to achieve this stable octet configuration.

### 8.10 Computing Valency
1. **If valence electrons are 1, 2, 3, or 4**:
   - Easier to lose these electrons to reveal the stable inner octet.
   - $\\mathbf{\\text{Valency} = \\text{Valence electrons}}$
   - Examples: Lithium (2, 1) $\\to 1$; Magnesium (2, 8, 2) $\\to 2$; Aluminum (2, 8, 3) $\\to 3$; Carbon (2, 4) $\\to 4$.
2. **If valence electrons are 5, 6, or 7**:
   - Easier to gain electrons to complete the octet.
   - $\\mathbf{\\text{Valency} = 8 - \\text{Valence electrons}}$
   - Examples: Nitrogen (2, 5) $\\to 8 - 5 = 3$; Oxygen (2, 6) $\\to 8 - 6 = 2$; Chlorine (2, 8, 7) $\\to 8 - 7 = 1$.
3. **If valence shell is full (8 electrons, or 2 for He)**:
   - Cannot gain or lose electrons. $\\mathbf{\\text{Valency} = 0}$ (Helium, Neon, Argon).""",
    "worked_examples": [
      {
        "problem": "How will you find the valency of chlorine, sulfur and magnesium?",
        "given": "Atomic numbers: Cl (Z = 17), S (Z = 16), Mg (Z = 12).",
        "formula": "1. Write configuration -> 2. Count valence electrons -> 3. Apply metal/non-metal valency rule.",
        "substitution": "Cl: 2, 8, 7 -> valence = 7 -> Valency = 8 - 7 = 1; S: 2, 8, 6 -> valence = 6 -> Valency = 8 - 6 = 2; Mg: 2, 8, 2 -> valence = 2 -> Valency = 2.",
        "calculation": "Cl gains 1 electron to form Cl-. S gains 2 electrons to form S2-. Mg loses 2 electrons to form Mg2+.",
        "finalAnswer": "Valency of Chlorine = 1 | Valency of Sulfur = 2 | Valency of Magnesium = 2",
        "unit": "Chemical Valency"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "Valence electrons and valency are always the exact same number.",
        "correction": "Valence electrons is the TOTAL number in the outer shell; Valency is the COMBINING CAPACITY. For Nitrogen, valence electrons = 5, but its valency is 8 - 5 = 3!",
        "why_it_matters": "Confusing valence electrons with valency costs marks on every chemistry paper."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Valence Electrons vs Valency Summary Table",
      "diagram_type": "flowchart",
      "concept_visuals": [
        {
          "concept_title": "Valency Rules for Metals and Non-Metals",
          "diagram_title": "Valency Determination Flowchart",
          "diagram_type": "flowchart",
          "what_to_make": "Valence e- (1,2,3,4) -> Valency = e- (Metals) | Valence e- (5,6,7) -> Valency = 8 - e- (Non-metals) | Valence e- (8 or He 2) -> Valency = 0 (Noble Gases)",
          "timing_and_cue": "Mount valency determination flowchart on Step 1: write_chalkboard(action=\"draw_flowchart\", content=\"Valence e- 1,2,3,4 -> Valency = Valence e- | Valence e- 5,6,7 -> Valency = 8 - Valence e- | Saturated e- (8 or He 2) -> Valency = 0\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount valency rule flowchart: write_chalkboard(action=\"draw_flowchart\", content=\"Valence 1,2,3,4 -> Valency = e- | Valence 5,6,7 -> Valency = 8 - e- | Noble Gases 8 -> Valency = 0\").\n2. 6-STAGE SOCRATIC CADENCE."
  },
  {
    "curriculum_id": CH8_ID,
    "order_index": 6,
    "title": "Atomic Identifiers, Isotopes, Isobars & Master Nuclear Solver",
    "description": "Master atomic number (Z), mass number (A), fractional atomic mass calculations of isotopes (Chlorine-35/37), medical and industrial isotope applications, and isobar distinctions.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
      "Atomic Number (Z): Total number of protons in the nucleus of an atom",
      "Mass Number (A): Total number of protons and neutrons (nucleons) in the nucleus (A = Z + n)",
      "Standard Atomic Notation: ^A_Z X layout",
      "Isotopes: Atoms of same element having identical atomic number Z but different mass number A (Protium, Deuterium, Tritium)",
      "Fractional Atomic Mass: Calculation of average atomic mass from natural percentage abundance (Chlorine 35.5 u)",
      "Applications of Isotopes: Uranium-235 (fuel), Cobalt-60 (cancer therapy), Iodine-131 (goitre treatment)",
      "Isobars: Atoms of different elements having same mass number A but different atomic numbers Z (Argon-40 and Calcium-40)",
      "Diagnostic 10-MCQ Evaluation Quiz"
    ],
    "key_concepts": [
      "Atomic Number ($Z$): Number of protons; uniquely identifies chemical identity of an element.",
      "Mass Number ($A$): Sum of protons and neutrons in nucleus ($A = Z + N$).",
      "Isotopes: Same element ($Z$ equal), different neutrons ($A$ different). Chemical properties identical, physical properties differ.",
      "Average Atomic Mass: Weighted sum of isotopic masses based on percentage abundances: $\\text{Mass} = \\sum (\\text{Mass}_i \\times \\%_i)$.",
      "Isobars: Different elements ($Z$ different), identical mass number ($A$ equal, e.g. ${}_{18}^{40}\\text{Ar}$ and ${}_{20}^{40}\\text{Ca}$). Chemical properties differ completely."
    ],
    "success_criteria": "Student can calculate number of neutrons, compute average fractional atomic mass, contrast isotopes vs isobars, and score >= 80% on chapter quiz.",
    "chapter_notes": """### 8.11 Atomic Identifiers
- **Atomic Number ($Z$)**: Number of protons in the nucleus. In neutral atom: $Z = \\text{protons} = \\text{electrons}$.
- **Mass Number ($A$)**: Total number of nucleons:
  $$A = Z + n \\implies n = A - Z$$
- **Standard Notation**: $^{A}_{Z}X$ (e.g. $^{14}_{7}N$, $^{35}_{17}Cl$).

### 8.12 Isotopes & Fractional Atomic Mass
- **Isotopes**: Same $Z$, different $A$.
  - Hydrogen isotopes: Protium ($^1_1H$), Deuterium ($^2_1H$), Tritium ($^3_1H$).
  - Carbon isotopes: $^{12}_6C, ^{14}_6C$.
  - Chlorine isotopes: $^{35}_{17}Cl$ ($75\\%$) and $^{37}_{17}Cl$ ($25\\%$, ratio $3:1$).
- **Calculating Fractional Atomic Mass of Chlorine**:
  $$\\text{Average Mass} = \\left(35 \\times \\frac{75}{100}\\right) + \\left(37 \\times \\frac{25}{100}\\right) = \\frac{105}{4} + \\frac{37}{4} = \\frac{142}{4} = \\mathbf{35.5\\text{ u}}$$

### 8.13 High-Yield Applications of Isotopes
1. **Uranium-235**: Nuclear fuel in atomic power reactors.
2. **Cobalt-60**: Radiation therapy for cancer treatment.
3. **Iodine-131**: Medical tracer and treatment for goitre (thyroid disorders).

### 8.14 Isobars
- Atoms of **different elements** having different atomic numbers $Z$ but the **same mass number $A$**.
- Example: $^{40}_{18}Ar$ (18 protons, 22 neutrons) and $^{40}_{20}Ca$ (20 protons, 20 neutrons).""",
    "worked_examples": [
      {
        "problem": "Composition of the nuclei of two atomic species X and Y are given as under: Protons of X = 6, Neutrons of X = 6. Protons of Y = 6, Neutrons of Y = 8. Give the mass numbers of X and Y. What is the relation between the two species?",
        "given": "Species X: p = 6, n = 6 | Species Y: p = 6, n = 8",
        "formula": "Mass number A = protons + neutrons; Same protons = same element = isotopes",
        "substitution": "A_X = 6 + 6 = 12; A_Y = 6 + 8 = 14",
        "calculation": "Atomic number Z = 6 for both, representing Carbon-12 and Carbon-14.",
        "finalAnswer": "Mass number of X = 12, Mass number of Y = 14. They are isotopes of carbon.",
        "unit": "Atomic Mass & Isotope"
      }
    ],
    "common_misconceptions": [
      {
        "misconception": "A sample of chlorine gas contains atoms that each have a mass of 35.5 u.",
        "correction": "NO single chlorine atom has a mass of 35.5 u! Any individual atom is either Chlorine-35 (mass 35 u) or Chlorine-37 (mass 37 u). 35.5 u is the statistical WEIGHTED AVERAGE of a macroscopic sample.",
        "why_it_matters": "Universal misconception clarifying individual discrete atoms vs bulk statistical averages."
      }
    ],
    "visual_lesson_plan": {
      "diagram_title": "Isotopes vs Isobars Comparison Matrix",
      "diagram_type": "flowchart",
      "concept_visuals": [
        {
          "concept_title": "Isotopes vs Isobars Distinction Matrix",
          "diagram_title": "Isotopes vs Isobars Taxonomy",
          "diagram_type": "flowchart",
          "what_to_make": "Isotopes: Same Z, Different A (Cl-35 & Cl-37, same chemistry) || Isobars: Different Z, Same A (Ar-40 & Ca-40, different chemistry)",
          "timing_and_cue": "Mount isotopes vs isobars flowchart on Step 1: write_chalkboard(action=\"draw_flowchart\", content=\"Isotopes: Same Z, Different A (Cl-35 vs Cl-37, same chemistry) | Isobars: Different Z, Same A (Ar-40 vs Ca-40, different chemistry)\")"
        }
      ]
    },
    "ai_system_prompt_context": "MANDATORY LIVE CHALKBOARD INVARIANTS:\n1. STEP 1 VISUAL MOUNTING: On Step 1, mount isotopes vs isobars flowchart: write_chalkboard(action=\"draw_flowchart\", content=\"Isotopes: Same Z, Diff A (Cl-35 vs Cl-37) | Isobars: Diff Z, Same A (Ar-40 vs Ca-40)\").\n2. 6-STAGE SOCRATIC CADENCE."
  }
]
all_modules.extend(ch8)

print(f"Total modules synthesized across Chapters 5, 6, 7, 8: {len(all_modules)}")

# Generate JS seed file
js_content = """const { supabase } = require('./db_helper');

const modules = """ + json.dumps(all_modules, indent=2) + """;

async function seed() {
  console.log('Seeding', modules.length, 'modules across Chapters 5, 6, 7, 8...');
  
  const chIds = [
    '8d01a5f5-bf82-49c2-9fab-253d26b086f4',
    '7e1d5438-1174-4577-8599-5f05a6642093',
    'da5625a5-7071-4533-8667-13da4c28abda',
    '8be782c9-c0d3-425e-bb81-c18c298dc4a7'
  ];

  // 1. Clean existing modules for these 4 chapters
  for (const cid of chIds) {
    const { error: delErr } = await supabase.from('syllabus_modules').delete().eq('curriculum_id', cid);
    if (delErr) {
      console.error('Error clearing old modules for', cid, delErr);
    } else {
      console.log('Cleared old modules for curriculum', cid);
    }
  }

  // 2. Insert new comprehensive modules in batches
  for (const m of modules) {
    const { data, error } = await supabase.from('syllabus_modules').insert([m]).select('id, title, order_index, curriculum_id');
    if (error) {
      console.error('Error inserting module:', m.title, error);
    } else {
      console.log('Inserted:', data[0].order_index, data[0].title);
    }
  }

  console.log('All modules seeded successfully into Supabase!');
}

seed().catch(console.error);
"""

with open("scripts/seed_chapters_5_to_8.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("scripts/seed_chapters_5_to_8.js successfully written!")
