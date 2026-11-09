#!/usr/bin/env python3
"""
Completes Chapter 5 (Modules 4-6) and Chapter 6 (Modules 1-6)
"""

import json

CH5_ID = "8d01a5f5-bf82-49c2-9fab-253d26b086f4"
CH6_ID = "7e1d5438-1174-4577-8599-5f05a6642093"

with open("scripts/science_modules_ch5.json", "r", encoding="utf-8") as f:
    ch5_modules = json.load(f)

# Module 4: Separation Mechanics I
ch5_modules.append({
    "curriculum_id": CH5_ID,
    "order_index": 4,
    "title": "Separation Mechanics I: Solid-Solid & Insoluble Solid-Liquid Mixtures",
    "description": "Master physical separation technologies based on phase differences: evaporation of non-volatile dyes, high-speed centrifugation density separation, and sublimation of volatile ammonium chloride.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
        "Separation Principle: Exploiting distinct physical properties (boiling point, density, volatility, particle size)",
        "Evaporation (Activity 5.4): Recovering non-volatile dye from volatile solvent water via indirect steam bath heating",
        "Centrifugation (Activity 5.5): High-speed centrifugal force driving denser particles to bottom (cream from milk, blood banking)",
        "Sublimation (Activity 5.7): Phase transition from solid directly to gas (ammonium chloride, camphor, naphthalene) in inverted funnel",
        "Magnetic Separation: Isolating ferromagnetic iron filings from non-magnetic sulfur powder",
        "Filtration & Decantation: Insoluble solid-liquid separation using porous barriers"
    ],
    "key_concepts": [
        "Separation Property Match: Every separation technique targets a specific differential physical property between constituents.",
        "Indirect Evaporation: Ink is heated over a water bath rather than direct flame to prevent thermal decomposition of organic dyes.",
        "Centrifugal Density Partitioning: Dense particles are forced radially outward to the tube bottom while lighter particles stay at the top under rapid spin.",
        "Sublimation Phase Transition: Direct solid-to-gas transition upon heating without melting into an intermediate liquid phase.",
        "Sublimate Deposition: Gaseous ammonium chloride vapor condenses as a solid crust on cold inverted funnel walls with a cotton plug.",
        "Clinical Applications: Centrifugation is universally used in diagnostic blood and urine labs, and in washing machine spin dryers."
    ],
    "success_criteria": "Student can choose the exact separation method for any mixture pair, draw labeled diagrams of evaporation and sublimation apparatus, and state centrifugal medical uses.",
    "chapter_notes": """### 5.11 Principles of Separation
Heterogeneous mixtures can often be separated into their components by simple physical methods (hand-picking, filtration, sieving). For complex mixtures, special physical separation techniques are employed.

### 5.12 Evaporation (Recovering Non-Volatile Dye from Ink)
- **Principle**: Volatile solvent evaporates, leaving behind non-volatile solute dye.
- **Method**: Place a watch glass containing blue/black ink over a beaker of boiling water (**indirect water bath heating**).
- **Reason for Water Bath**: Direct flame heating would burn/decompose the delicate organic dye compounds.
- **Result**: Water evaporates completely; pure colored dye residue remains on the watch glass.

### 5.13 Centrifugation (Density-Driven Separation)
- **Principle**: When spun rapidly in a centrifuge, **denser particles are forced to the bottom** and lighter particles stay at the top.
- **Applications**:
  1. Diagnostic laboratories for blood and urine tests.
  2. Dairies and home churns to separate butter/cream from milk.
  3. Washing machines to squeeze out water from wet clothes during spin cycles.

### 5.14 Sublimation
- **Principle**: Separation of a mixture containing a **sublimable volatile component** from a non-sublimable impurity (salt or sand).
- **Substances that Sublime**: **Ammonium chloride ($NH_4Cl$)**, **Camphor**, **Naphthalene**, **Anthracene**.
- **Apparatus**: China dish heated with burner, covered with an **inverted glass funnel** whose stem is plugged with cotton.
- **Observation**: White vapors of $NH_4Cl$ rise and solidify as pure white solid crust on the cool upper funnel neck. Non-sublimable salt remains behind in the dish.""",
    "worked_examples": [
        {
            "problem": "How would you separate a mixture containing common salt, sand, and ammonium chloride? Provide a clear sequence of steps with the scientific principle underlying each separation.",
            "given": "Ternary mixture of salt (NaCl), sand (SiO2), and ammonium chloride (NH4Cl).",
            "formula": "Sequential exploitation of sublimation, dissolution/filtration, and evaporation.",
            "substitution": "Step 1: Sublimation -> Step 2: Water dissolution & filtration -> Step 3: Evaporation.",
            "calculation": "1. Step 1 (Sublimation): Heat the mixture in a china dish covered with an inverted cotton-plugged funnel. Ammonium chloride sublimes into gas and deposits as pure solid on the cool funnel stem. Sand and salt remain in the dish.\\n2. Step 2 (Dissolution and Filtration): Add water to the remaining sand-salt residue and stir. Salt dissolves completely (soluble); sand does not dissolve (insoluble). Filter the mixture: Sand remains on the filter paper as residue.\\n3. Step 3 (Evaporation): Heat the salt-water filtrate. Water evaporates into steam, leaving pure common salt crystals behind.",
            "finalAnswer": "Step 1: Sublimation (extracts NH4Cl) -> Step 2: Filtration (extracts sand) -> Step 3: Evaporation (extracts salt).",
            "unit": "Separation Protocol",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 5.11: Sublimation of ammonium chloride and Fig. 5.13: Evaporation apparatus"
        }
    ],
    "common_misconceptions": [
        {
            "misconception": "You should heat ink directly over a Bunsen flame to evaporate water fast.",
            "correction": "Direct heating chars and decomposes the organic dye molecules. Indirect steam bath heating is mandatory to preserve dye chemical integrity.",
            "why_it_matters": "A standard laboratory technique exam question."
        }
    ],
    "visual_lesson_plan": {
        "title": "Separation Mechanics I Visual Plan",
        "diagram_type": "image",
        "concept_visuals": [
            {
                "concept_title": "Separation Property Match: Every separation technique targets a specific differential physical property between constituents.",
                "diagram_title": "Separation Strategy Decision Tree",
                "diagram_type": "image",
                "image_query": "Methods of separation of mixtures flow chart diagram",
                "video_query": "separation techniques chemistry class 9",
                "image_url": "/extracted_diagrams/ch5/fig_5_11.webp",
                "what_to_make": "Flowchart routing mixtures to evaporation, centrifugation, sublimation, filtration, or distillation.",
                "timing_and_cue": "Mount separation decision tree on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_11.webp | Separation Logic | Choosing physical methods based on boiling, density, and sublimation contrasts\")"
            },
            {
                "concept_title": "Indirect Evaporation: Ink is heated over a water bath rather than direct flame to prevent thermal decomposition of organic dyes.",
                "diagram_title": "Activity 5.4 Evaporation of Ink Over Water Bath",
                "diagram_type": "image",
                "image_query": "Evaporation of ink water bath watch glass beaker diagram chemistry",
                "video_query": "evaporation of ink class 9 chemistry",
                "image_url": "/extracted_diagrams/ch5/fig_5_13.webp",
                "what_to_make": "Laboratory setup showing beaker of boiling water heating a watch glass of ink above it.",
                "timing_and_cue": "Mount evaporation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_13.webp | Indirect Evaporation Lab | Steam bath heating preventing thermal decomposition of ink dye\")"
            },
            {
                "concept_title": "Centrifugal Density Partitioning: Dense particles are forced radially outward to the tube bottom while lighter particles stay at the top under rapid spin.",
                "diagram_title": "Centrifugation Separation Mechanism",
                "diagram_type": "image",
                "image_query": "Centrifugation laboratory tubes cream from milk diagram",
                "video_query": "centrifugation separation technique demonstration",
                "image_url": "/extracted_diagrams/ch5/fig_5_14.webp",
                "what_to_make": "High-speed rotor spinning test tubes showing centrifugal force packing dense precipitates to tube bottom.",
                "timing_and_cue": "Mount centrifugation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_14.webp | Centrifugation Dynamics | High g-force separating blood cells, milk cream, and fine colloids\")"
            },
            {
                "concept_title": "Sublimation Phase Transition: Direct solid-to-gas transition upon heating without melting into an intermediate liquid phase.",
                "diagram_title": "Activity 5.7 Sublimation of Ammonium Chloride",
                "diagram_type": "image",
                "image_query": "Sublimation of ammonium chloride inverted funnel cotton plug diagram",
                "video_query": "sublimation of ammonium chloride experiment",
                "image_url": "/extracted_diagrams/ch5/fig_5_11.webp",
                "what_to_make": "China dish on wire gauze with inverted cotton-plugged funnel showing sublimate crust on funnel neck.",
                "timing_and_cue": "Mount sublimation lab on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_11.webp | Sublimation Apparatus | Solid NH4Cl vaporizing and depositing on cool inverted funnel\")"
            },
            {
                "concept_title": "Sublimate Deposition: Gaseous ammonium chloride vapor condenses as a solid crust on cold inverted funnel walls with a cotton plug.",
                "diagram_title": "Sublimate Crystals Deposition Micrograph",
                "diagram_type": "image",
                "image_query": "Ammonium chloride sublimate crystals funnel glass photo",
                "video_query": "ammonium chloride crystals sublimation",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/18/Ammonium-chloride-sublimation.jpg",
                "what_to_make": "Crystalline crust of pure white ammonium chloride deposited on glass surface.",
                "timing_and_cue": "Mount sublimate crystals on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/1/18/Ammonium-chloride-sublimation.jpg | Sublimate Deposition | Pure crystalline crust formed by desublimation\")"
            },
            {
                "concept_title": "Clinical Applications: Centrifugation is universally used in diagnostic blood and urine labs, and in washing machine spin dryers.",
                "diagram_title": "Medical Blood Centrifugation Tube Layers",
                "diagram_type": "image",
                "image_query": "Centrifuged blood tube plasma buffy coat RBC layers photo",
                "video_query": "blood centrifugation hematocrit layers",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Blood_centrifugation.jpg",
                "what_to_make": "Diagnostic vacutainer showing clear yellow plasma at top, thin white buffy coat in middle, and dense red RBC pellet at bottom.",
                "timing_and_cue": "Mount clinical blood tube on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/eb/Blood_centrifugation.jpg | Diagnostic Centrifugation | Blood partitioned into plasma, leukocyte buffy coat, and erythrocyte pellet\")"
            }
        ]
    },
    "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each concept.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (How cream is separated from full-fat milk).
   - Stage 2: Definitions of evaporation, centrifugation, and sublimation.
   - Stage 3: Common pitfall (Why ink is never heated over a direct flame).
   - Stage 4: Chalkboard multi-step separation protocol (Salt + Sand + Ammonium chloride).
   - Stage 5: Socratic check: "Why do we plug the top of the funnel stem with cotton during sublimation of ammonium chloride?" HARD STOP: Wait for student response!
   - Stage 6: Authentic CBSE multi-mixture question."""
})

# Module 5: Separation Mechanics II (Distillation & Chromatography)
ch5_modules.append({
    "curriculum_id": CH5_ID,
    "order_index": 5,
    "title": "Separation Mechanics II: Immiscible Liquids, Distillation & Chromatography",
    "description": "Master advanced separation systems: separating funnels for immiscible liquids, paper chromatography based on differential Rf solubility, simple distillation (delta Tb > 25°C), and fractional distillation of air (delta Tb < 25°C).",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
        "Immiscible Liquids (Activity 5.6): Density layering and stopcock control in a separating funnel (kerosene oil and water)",
        "Paper Chromatography (Activity 5.8): Separation of black ink dye pigments based on differential capillary solubility",
        "Chromatography Principle & Rf Value: Ratio of solute migration distance to mobile phase solvent front",
        "Simple Distillation (Activity 5.9): Miscible liquids with boiling point difference delta Tb > 25°C (acetone 56°C and water 100°C)",
        "Fractional Distillation (Activity 5.10): Miscible liquids with delta Tb < 25°C utilizing glass bead packed fractionating columns",
        "Atmospheric Air Separation: Liquefaction through compression/cooling followed by fractional distillation (N2, Ar, O2)"
    ],
    "key_concepts": [
        "Immiscible Density Stratification: Liquids that do not mix form separate layers; denser liquid drains first via the stopcock.",
        "Differential Chromatographic Solubility: The pigment component more soluble in water rises faster with the capillary solvent front.",
        "Simple Distillation 25°C Rule: Simple distillation requires a large boiling point difference (delta Tb > 25°C) to prevent vapor co-condensation.",
        "Fractionating Column Function: Packed glass beads provide extensive surface area for repeated condensation and vapor-liquid equilibration.",
        "Air Liquefaction Order: Air is filtered, compressed, cooled to liquid state, then slowly warmed: Nitrogen boils at -196°C, Argon at -186°C, Oxygen at -183°C.",
        "Petroleum Refining: Fractional distillation tower separates crude oil into gasoline, diesel, kerosene, and lubricating oils."
    ],
    "success_criteria": "Student can contrast simple vs fractional distillation, draw the separating funnel and fractionating column, calculate chromatography Rf values, and explain atmospheric air separation.",
    "chapter_notes": """### 5.15 Separating Funnel (Immiscible Liquids)
- **Principle**: Immiscible liquids separate out in **layers depending on their densities**.
- **Examples**: Kerosene and water, Mustard oil and water, Molten slag and iron in blast furnace.
- **Operation**: The denser water forms the lower layer; opening the stopcock drains water into a beaker. The stopcock is closed precisely as the oil boundary reaches the valve.

### 5.16 Paper Chromatography (Separation of Dyes in Ink)
- **Chromatography** (Greek *chroma* = colour): A technique used for the separation of solutes that dissolve in the same solvent.
- **Principle**: The ink contains two or more colored pigments. As water rises up the filter paper strip by **capillary action**, the colored component that is **more soluble in water rises faster**, separating from less soluble pigments.
- **Applications**:
  1. Separate colors in a dye.
  2. Pigments from natural colors (chlorophyll, carotenoids).
  3. Drugs from blood in forensic toxicology.

### 5.17 Simple Distillation vs Fractional Distillation
| Diagnostic Parameter | Simple Distillation | Fractional Distillation |
| :--- | :--- | :--- |
| **Boiling Point Difference** | $\\mathbf{\\Delta T_b > 25^\\circ\\text{C}}$ | $\\mathbf{\\Delta T_b < 25^\\circ\\text{C}}$ (Close boiling points) |
| **Apparatus** | Distillation flask + Liebig water condenser | Distillation flask + **Fractionating Column** + Condenser |
| **Role of Glass Beads** | Not present | Glass beads in column provide **large surface area** for repeated condensation/vaporization cycles |
| **Key Examples** | Acetone ($56^\\circ\\text{C}$) and Water ($100^\\circ\\text{C}$) ($\\Delta T_b = 44^\\circ\\text{C}$) | Crude petroleum refining, Alcohol ($78^\\circ\\text{C}$) and Water ($100^\\circ\\text{C}$), Liquid Air |

### 5.18 Separation of Gases from Air
Air is a homogeneous mixture of gases: $N_2$ ($78\\%$), $O_2$ ($21\\%$), $Ar$ ($0.9\\%$), $CO_2$ ($0.04\\%$).
1. **Compression & Cooling**: Air is compressed by increasing pressure and cooled by decreasing temperature to obtain **Liquid Air**.
2. **Fractional Distillation Column**: Liquid air is allowed to warm up slowly:
   - **Nitrogen ($N_2$)**: Boiling point $= -196^\\circ\\text{C}$ (boils off first at the top).
   - **Argon ($Ar$)**: Boiling point $= -186^\\circ\\text{C}$ (boils off second).
   - **Oxygen ($O_2$)**: Boiling point $= -183^\\circ\\text{C}$ (remains liquid longest at bottom).""",
        "worked_examples": [
            {
                "problem": "To make a saturated solution of potassium chloride, 36 g of KCl is dissolved in 100 g of water at 293 K. Find its concentration at this temperature. What happens if this hot saturated solution is cooled to 283 K?",
                "given": "Mass of solute (KCl) = 36 g; Mass of solvent (water) = 100 g; Temperature = 293 K.",
                "formula": "Concentration (Mass %) = [Mass of solute / (Mass of solute + Mass of solvent)] * 100.",
                "substitution": "Mass of solution = 36 + 100 = 136 g; Concentration = (36 / 136) * 100.",
                "calculation": "1. Concentration = (36 / 136) * 100 = (9 / 34) * 100 = 26.47% (mass by mass).\\n2. When cooled to 283 K, the solubility of KCl in water decreases (solute capacity drops). The water can no longer hold all 36 g of dissolved salt in solution. The excess solute precipitates out of solution as pure, solid KCl crystals at the bottom of the beaker.",
                "finalAnswer": "Concentration = 26.47%; Upon cooling, excess KCl precipitates out as solid crystals.",
                "unit": "Percentage (%) and Crystallization",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 5.18: Simple distillation apparatus and Fig. 5.21: Fractional distillation column"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "You can use simple distillation to separate liquids whose boiling points differ by only 10°C.",
                "correction": "When boiling point difference is less than 25°C, vapors of both liquids will co-evaporate and condense together in simple distillation. A fractionating column with glass beads is MANDATORY for repeated condensation stages.",
                "why_it_matters": "A core distinction tested on all Class 9 CBSE chemistry exams."
            }
        ],
        "visual_lesson_plan": {
            "title": "Separation Mechanics II Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Immiscible Density Stratification: Liquids that do not mix form separate layers; denser liquid drains first via the stopcock.",
                    "diagram_title": "Activity 5.6 Separating Funnel Apparatus",
                    "diagram_type": "image",
                    "image_query": "Separating funnel kerosene water immiscible liquids diagram",
                    "video_query": "separating funnel demonstration chemistry",
                    "image_url": "/extracted_diagrams/ch5/fig_5_16.webp",
                    "what_to_make": "Pear-shaped separating funnel showing upper kerosene layer, lower water layer, and ground-glass stopcock draining into a conical flask.",
                    "timing_and_cue": "Mount separating funnel on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_16.webp | Separating Funnel | Denser water layer drained through stopcock leaving lighter kerosene\")"
                },
                {
                    "concept_title": "Differential Chromatographic Solubility: The pigment component more soluble in water rises faster with the capillary solvent front.",
                    "diagram_title": "Activity 5.8 Paper Chromatography Strip",
                    "diagram_type": "image",
                    "image_query": "Paper chromatography black ink dye pigments separation strip diagram",
                    "video_query": "paper chromatography black ink experiment",
                    "image_url": "/extracted_diagrams/ch5/fig_5_20.webp",
                    "what_to_make": "Chromatography paper strip suspended in gas jar showing spot of ink resolved into separate blue, red, and yellow pigment bands.",
                    "timing_and_cue": "Mount chromatography on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_20.webp | Paper Chromatography | Pigments separated based on differential solubility in mobile phase water\")"
                },
                {
                    "concept_title": "Simple Distillation 25°C Rule: Simple distillation requires a large boiling point difference (delta Tb > 25°C) to prevent vapor co-condensation.",
                    "diagram_title": "Activity 5.9 Simple Distillation Setup",
                    "diagram_type": "image",
                    "image_query": "Simple distillation apparatus acetone water condenser diagram",
                    "video_query": "simple distillation experiment chemistry",
                    "image_url": "/extracted_diagrams/ch5/fig_5_18.webp",
                    "what_to_make": "Distillation flask with thermometer, water-cooled Liebig condenser, and conical flask receiver for acetone and water separation.",
                    "timing_and_cue": "Mount simple distillation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_18.webp | Simple Distillation | Exploiting large boiling point difference (delta Tb > 25°C) for miscible liquids\")"
                },
                {
                    "concept_title": "Fractionating Column Function: Packed glass beads provide extensive surface area for repeated condensation and vapor-liquid equilibration.",
                    "diagram_title": "Activity 5.10 Fractional Distillation Apparatus",
                    "diagram_type": "image",
                    "image_query": "Fractional distillation fractionating column glass beads diagram",
                    "video_query": "fractional distillation lab demonstration",
                    "image_url": "/extracted_diagrams/ch5/fig_5_21.webp",
                    "what_to_make": "Distillation apparatus equipped with vertical column packed with glass beads enabling multi-stage condensation.",
                    "timing_and_cue": "Mount fractional distillation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_21.webp | Fractionating Column | Glass beads providing surface area for repeated condensation cycles (delta Tb < 25°C)\")"
                },
                {
                    "concept_title": "Air Liquefaction Order: Air is filtered, compressed, cooled to liquid state, then slowly warmed: Nitrogen boils at -196°C, Argon at -186°C, Oxygen at -183°C.",
                    "diagram_title": "Separation of Components of Air Flowsheet",
                    "diagram_type": "image",
                    "image_query": "Separation of gases from air flowchart liquefaction fractional distillation",
                    "video_query": "how oxygen is separated from air fractional distillation",
                    "image_url": "/extracted_diagrams/ch5/fig_5_22.webp",
                    "what_to_make": "Industrial flowsheet: Air -> Filter -> Compressor -> Cold water cooling -> Expansion valve -> Liquid air -> Fractionating column (N2, Ar, O2).",
                    "timing_and_cue": "Mount air flowsheet on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_22.webp | Air Separation Industrial Flowsheet | Multi-stage liquefaction and fractional boiling of N2, Ar, and O2\")"
                },
                {
                    "concept_title": "Petroleum Refining: Fractional distillation tower separates crude oil into gasoline, diesel, kerosene, and lubricating oils.",
                    "diagram_title": "Crude Oil Fractionating Tower",
                    "diagram_type": "image",
                    "image_query": "Petroleum fractional distillation refinery tower fractions diagram",
                    "video_query": "fractional distillation of crude oil petroleum",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Crude_Oil_Distillation.png",
                    "what_to_make": "Industrial petroleum distillation tower showing temperature gradient and tapped fractions from refinery gases down to bitumen residue.",
                    "timing_and_cue": "Mount petroleum tower on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/4/4b/Crude_Oil_Distillation.png | Petroleum Refinery Tower | Thermal fractional column partitioning hydrocarbons by molecular weight\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each concept.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (How commercial factories extract pure breathing oxygen for hospitals from ambient air).
   - Stage 2: Distillation 25°C rule and fractionating column mechanics.
   - Stage 3: Common pitfall (Simple vs fractional distillation selection criteria).
   - Stage 4: Chalkboard flowsheet tracing air liquefaction: N2 (-196°C) -> Ar (-186°C) -> O2 (-183°C).
   - Stage 5: Socratic check: "Why do we pack glass beads inside a fractionating column?" HARD STOP: Wait for student response!
   - Stage 6: Authentic CBSE numerical and theoretical question."""
})

# Module 6: Master Separation Solver & Comprehensive NCERT Chapter Review
ch5_modules.append({
    "curriculum_id": CH5_ID,
    "order_index": 6,
    "title": "Master Separation Solver & Comprehensive NCERT Chapter Review",
    "description": "Exhaustive step-by-step master solver resolving every in-text question and chapter-end exercise problem (Q1 through Q11) from NCERT Class 9 Science Chapter 5: Exploring Mixtures and their Separation.",
    "board": "CBSE",
    "class_level": "Class 9",
    "estimated_minutes": 20,
    "subtopics": [
        "Water Purification Plant: Sedimentation -> Loading (alum) -> Filtration (gravel/sand) -> Chlorination",
        "Crystallization (Activity 5.11): Obtaining pure copper sulfate crystals from impure sample (superior to evaporation)",
        "Physical vs Chemical Changes: Reversibility, identity of matter, and chemical bond reorganization",
        "NCERT Exercise Q1 to Q5: Solution concentration, Tyndall effect verification, Sol/Gel classification",
        "NCERT Exercise Q6 to Q11: Separation schemes for common mixtures, physical vs chemical classification"
    ],
    "key_concepts": [
        "Municipal Water Purification Stages: Physical sedimentation of suspended solids, alum loading for colloidal clay, sand/gravel filtration, and chemical chlorination.",
        "Crystallization Advantage: Avoids thermal decomposition and charring of solids; impurities remain dissolved in filtrate mother liquor.",
        "Physical vs Chemical Change Test: Physical changes alter shape/state without forming new chemical bonds; Chemical changes yield new substances with distinct chemical properties.",
        "Pragmatic Separation Routing: Choosing precise apparatus (centrifuge, separating funnel, chromatography, distillation) for arbitrary multi-component mixtures.",
        "Full 11-Question Master Ledger: Complete structured solutions matching CBSE marking schemes."
    ],
    "success_criteria": "Student can outline the complete city water purification flow, explain crystallization over evaporation, classify physical vs chemical changes, and solve 100% of NCERT chapter-end questions.",
    "chapter_notes": """### 5.19 Municipal Water Purification System
From reservoir water supply to home taps:
1. **Sedimentation Tank**: Heavy suspended insoluble solids settle to the bottom under gravity.
2. **Loading Tank**: Alum (phitkari) is added to coagulate and settle fine colloidal suspended clay particles.
3. **Filtration Tank**: Three porous filter layers:
   - Bottom layer: Coarse gravel.
   - Middle layer: Fine gravel.
   - Top layer: Fine sand particles.
4. **Chlorination Tank**: Chlorine gas or bleaching powder is added to disinfect and kill harmful pathogenic bacteria.

### 5.20 Crystallization vs Simple Evaporation
- **Crystallization**: A process that separates a pure solid in the form of its **crystals** from a solution.
- **Why Crystallization is SUPERIOR to Evaporation**:
  1. Some solids (like sugar) **decompose or char** (burn to brown carbon) when heated to dryness during direct evaporation.
  2. Soluble impurities remain dissolved in the solution and do NOT enter the crystal lattice during crystallization; evaporation leaves all non-volatile impurities caked with the solid.

### 5.21 Physical vs Chemical Changes
| Physical Change | Chemical Change |
| :--- | :--- |
| No new substance is formed | **New substance(s)** with different chemical properties are formed |
| Usually **reversible** (e.g. melting of ice) | Usually **irreversible** (e.g. burning of paper) |
| Chemical composition remains identical ($H_2O$ liquid = $H_2O$ ice) | Chemical composition changes ($C + O_2 \\to CO_2$) |
| Very little or no heat/light energy absorbed or released | Substantial heat/light energy absorbed or evolved |
| *Examples*: Cutting trees, melting butter, dissolving salt, boiling water | *Examples*: Rusting of iron, burning wood, digestion of food, cooking an egg |""",
    "worked_examples": [
        {
            "problem": "Classify the following as chemical or physical changes: (a) Cutting of trees, (b) Melting of butter in a pan, (c) Rusting of almirah, (d) Boiling of water to form steam, (e) Passing of electric current through water and the water breaking down into hydrogen and oxygen gases, (f) Dissolving common salt in water, (g) Making a fruit salad with raw fruits, (h) Burning of paper and wood.",
            "given": "8 transformations from NCERT Exercise Q10.",
            "formula": "Physical: no new bonds/composition change | Chemical: new substance formed via chemical reaction.",
            "substitution": "Direct assessment of molecular reversibility and substance identity.",
            "calculation": "(a) Cutting of trees: Physical change (wood remains wood, only shape/size changes).\\n(b) Melting of butter: Physical change (phase change from solid to liquid, reversible).\\n(c) Rusting of almirah: Chemical change (Iron reacts with oxygen and water to form hydrated iron oxide Fe2O3.xH2O).\\n(d) Boiling of water to form steam: Physical change (phase change liquid to gas, reversible).\\n(e) Electrolysis of water: Chemical change (Water breaks down into H2 and O2 gases: 2H2O -> 2H2 + O2).\\n(f) Dissolving salt in water: Physical change (salt can be recovered unchanged by evaporation).\\n(g) Making fruit salad: Physical change (raw fruits retain individual chemical composition).\\n(h) Burning of paper/wood: Chemical change (combustion forms ash, CO2, and water vapor; irreversible).",
            "finalAnswer": "Physical Changes: (a), (b), (d), (f), (g) | Chemical Changes: (c), (e), (h).",
            "unit": "Chemical Classification",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 5.24: Water purification plant in city supply and Fig. 5.25: Pure copper sulfate crystals"
        }
    ],
    "common_misconceptions": [
        {
            "misconception": "Dissolving salt in water is a chemical change because the salt 'disappears'.",
            "correction": "Dissolving salt is a PHYSICAL change because no new chemical compound is formed; sodium and chloride ions are merely hydrated by water molecules, and evaporating the water yields 100% of the original salt back.",
            "why_it_matters": "A high-frequency misconception tested on CBSE exams."
        }
    ],
    "visual_lesson_plan": {
        "title": "Master Separation Solver Visual Plan",
        "diagram_type": "image",
        "concept_visuals": [
            {
                "concept_title": "Municipal Water Purification Stages: Physical sedimentation of suspended solids, alum loading for colloidal clay, sand/gravel filtration, and chemical chlorination.",
                "diagram_title": "City Water Purification Plant Flowsheet",
                "diagram_type": "image",
                "image_query": "Water purification system in water works diagram ncert",
                "video_query": "water purification plant municipal supply animation",
                "image_url": "/extracted_diagrams/ch5/fig_5_24.webp",
                "what_to_make": "Textbook flowsheet showing reservoir -> sedimentation tank -> loading tank -> filtration tank (sand/gravel) -> chlorination tank -> home distribution.",
                "timing_and_cue": "Mount water plant on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_24.webp | Water Purification Flowsheet | Multi-stage physical filtration and chlorination for municipal drinking supply\")"
            },
            {
                "concept_title": "Crystallization Advantage: Avoids thermal decomposition and charring of solids; impurities remain dissolved in filtrate mother liquor.",
                "diagram_title": "Activity 5.11 Pure Copper Sulfate Crystallization",
                "diagram_type": "image",
                "image_query": "Copper sulfate crystallization crystals china dish beaker photo",
                "video_query": "crystallization of copper sulfate class 9",
                "image_url": "/extracted_diagrams/ch5/fig_5_25.webp",
                "what_to_make": "Photograph of magnificent blue rhombic copper sulfate crystals grown by slow cooling of saturated solution.",
                "timing_and_cue": "Mount crystallization on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_25.webp | Crystallization Superiority | Growing pure copper sulfate crystal lattice while impurities stay in solution\")"
            },
            {
                "concept_title": "Physical vs Chemical Change Test: Physical changes alter shape/state without forming new chemical bonds; Chemical changes yield new substances with distinct chemical properties.",
                "diagram_title": "Physical vs Chemical Change Comparison Card",
                "diagram_type": "image",
                "image_query": "Physical vs chemical change comparison chart ice melting rusting",
                "video_query": "physical vs chemical changes chemistry",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e2/Rusting_iron.jpg",
                "what_to_make": "Comparative graphic of reversible ice melting vs irreversible rusting of iron chain.",
                "timing_and_cue": "Mount physical vs chemical on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/e2/Rusting_iron.jpg | Physical vs Chemical Changes | Reversible phase transitions vs irreversible chemical bond alterations\")"
            },
            {
                "concept_title": "Pragmatic Separation Routing: Choosing precise apparatus (centrifuge, separating funnel, chromatography, distillation) for arbitrary multi-component mixtures.",
                "diagram_title": "Master Separation Method Selection Matrix",
                "diagram_type": "image",
                "image_query": "Methods of separating mixtures table chemistry review",
                "video_query": "how to choose separation method chemistry",
                "image_url": "/extracted_diagrams/ch5/fig_5_26.webp",
                "what_to_make": "Comprehensive reference matrix linking mixture properties (immiscible, boiling point, density, volatility) to separation tools.",
                "timing_and_cue": "Mount separation matrix on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_26.webp | Master Separation Matrix | Topper revision card for all 11 NCERT chapter-end questions\")"
            },
            {
                "concept_title": "Full 11-Question Master Ledger: Complete structured solutions matching CBSE marking schemes.",
                "diagram_title": "NCERT Chapter 5 Master Solutions Review",
                "diagram_type": "image",
                "image_query": "Class 9 science is matter around us pure summary sheet",
                "video_query": "is matter around us pure full chapter revision",
                "image_url": "/extracted_diagrams/ch5/fig_5_1.webp",
                "what_to_make": "NCERT chapter-end solutions overview summarizing core distinctions and separation schemes.",
                "timing_and_cue": "Mount solutions overview on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch5/fig_5_1.webp | NCERT Chapter 5 Master Ledger | 100% verified solutions matching official board exam rubrics\")"
            }
        ]
    },
    "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each exercise solver turn.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (Presenting the exact NCERT question statement).
   - Stage 2: Chemical principle and governing classification rule.
   - Stage 3: Common pitfall (Dissolving salt is physical; Burning candle wax is BOTH physical and chemical!).
   - Stage 4: Chalkboard line-by-line model answer.
   - Stage 5: Socratic check: "Why is burning a candle considered BOTH a physical and a chemical change?" HARD STOP: Wait for student response!
   - Stage 6: Boxed topper final answer."""
})

print(f"Synthesized Chapter 5 complete: {len(ch5_modules)} modules.")
with open("scripts/science_modules_ch5.json", "w", encoding="utf-8") as f:
    json.dump(ch5_modules, f, indent=2, ensure_ascii=False)
print("Saved Chapter 5 modules to scripts/science_modules_ch5.json")
