"""
Complete Module Synthesis for Class 9 Science:
Chapter 8: Journey Inside the Atom (Curriculum ID: 8be782c9-c0d3-425e-bb81-c18c298dc4a7)
"""

import json

def get_ch8_modules():
    # Module 1
    m1 = {
        "order_index": 1,
        "title": "The Subatomic Revolution: Cathode Rays, Canal Rays & Discovery of Fundamental Particles",
        "description": "Explore the breakdown of Dalton's indivisible atom, analyze J.J. Thomson's discharge tube cathode ray experiments discovering the negative electron, Goldstein's canal ray experiments discovering the positive proton, and Chadwick's discovery of the neutral neutron.",
        "subtopics": [
            "Dalton's Indivisible Atom Fallacy: Electrical nature of matter in friction experiments (comb and paper)",
            "J.J. Thomson's Cathode Ray Tube Experiments: Discovery of subatomic electrons (charge -1, mass 1/2000 u)",
            "E. Goldstein's Canal Ray (Anode Ray) Experiments: Discovery of positively charged protons (charge +1, mass 1 u)",
            "James Chadwick's Discovery of the Neutron (1932): Neutral subatomic particle (charge 0, mass 1 u)",
            "Tri-Particulate Model of the Atom: Comparing mass, charge, and location of Electron, Proton, and Neutron",
            "Activity 8.1: Rubbing glass rod with silk and ebonite with fur to demonstrate electric charge"
        ],
        "key_concepts": [
            "Electrical Nature of Matter: Matter contains charged particles, proven by frictional electricity (combing dry hair attracts small bits of paper, rubbing glass rod with silk cloth).",
            "Cathode Rays & Electron Discovery: J.J. Thomson (1897) identified cathode rays as streams of negatively charged subatomic particles called electrons, with negligible mass (~1/2000 of a hydrogen atom) and unit negative charge (-1.6 * 10^-19 C).",
            "Canal Rays & Proton Discovery: E. Goldstein (1886) discovered positively charged radiations in a modified gas discharge tube called canal rays, leading to the identification of the proton with mass equal to 1 atomic mass unit and unit positive charge (+1.6 * 10^-19 C).",
            "Neutron Discovery: James Chadwick (1932) discovered subatomic particles having no electrical charge and a mass nearly equal to that of a proton, designated as neutrons (n), located within the atomic nucleus.",
            "Tri-Particulate Atomic Ledger: An atom consists of three fundamental subatomic particles: Protons (+1 charge, 1 u mass in nucleus), Neutrons (0 charge, 1 u mass in nucleus), and Electrons (-1 charge, 1/1840 u mass in orbits).",
            "Electrical Neutrality Axiom: In any neutral atom, the number of positive protons inside the nucleus identically equals the number of negative electrons revolving outside."
        ],
        "success_criteria": "Student can contrast properties of electron, proton, and neutron, explain cathode and canal ray experiments, and state why atoms are electrically neutral.",
        "chapter_notes": """### 8.1 The Collapse of Dalton's Indivisible Atom
Dalton's atomic theory (1808) asserted that atoms are hard, indivisible, and indestructible spheres. However, late 19th-century experiments with static electricity demonstrated that matter can acquire electrical charge:
- Rubbing a dry plastic comb through dry hair allows it to attract uncharged bits of paper.
- Rubbing a glass rod with silk cloth produces positive static charge.
*Inference*: If matter can become charged by rubbing, atoms must be composed of smaller, charged **subatomic particles**.

### 8.2 Discovery of the Electron (J.J. Thomson, 1897)
- **Apparatus**: Glass discharge tube evacuated to high vacuum ($10^{-2}\\text{ to }10^{-4}\\text{ mm Hg}$) under high voltage ($10,000\\text{ V}$).
- **Observation**: Invisible rays travel from the negative cathode toward the positive anode, causing green fluorescence on phosphor screens.
- **Properties of Cathode Rays**:
  1. Travel in straight lines (cast sharp shadows).
  2. Deflected toward the positive plate in an electric field, proving they carry **negative electrical charge**.
  3. Possess mechanical kinetic energy (rotate light paddle wheels).
  4. Charge-to-mass ratio ($e/m$) is invariant regardless of the gas inside the tube or cathode metal.
- **The Electron ($e^-$)**: Charge $= -1.6 \\times 10^{-19}\\text{ C}$ (unit negative charge $-1$); Mass $= 9.1 \\times 10^{-31}\\text{ kg} \\approx \\frac{1}{2000}\\text{ u}$ (negligible).

### 8.3 Discovery of the Proton (E. Goldstein, 1886)
- **Canal Rays (Anode Rays)**: In a discharge tube with a perforated cathode, Goldstein observed faint luminous rays traveling in the opposite direction (from anode through cathode perforations).
- **The Proton ($p^+$)**: Positively charged subatomic particles.
  - Charge $= +1.6 \\times 10^{-19}\\text{ C}$ (unit positive charge $+1$).
  - Mass $= 1.672 \\times 10^{-27}\\text{ kg} \\approx 1\\text{ u}$ (approximately 2000 times heavier than an electron).

### 8.4 Discovery of the Neutron (James Chadwick, 1932)
By bombarding a thin beryllium target with high-energy $\\alpha$-particles, Chadwick detected highly penetrating neutral radiation composed of particles with:
- Electrical Charge $= \\mathbf{0}$ (neutral).
- Mass $= 1.675 \\times 10^{-27}\\text{ kg} \\approx 1\\text{ u}$ (slightly heavier than proton).
- Present in the nuclei of all atoms **except ordinary hydrogen** ($^1_1H$, Protium), which has 0 neutrons.""",
        "worked_examples": [
            {
                "problem": "What are canal rays, and how did their discovery disprove the hypothesis that atoms are solid indivisible spheres?",
                "given": "Goldstein's perforated cathode gas discharge tube experiment.",
                "formula": "Subatomic Charge Invariance",
                "substitution": "Canal rays consist of positively charged gaseous ions moving toward the cathode.",
                "calculation": "1. Canal rays (anode rays) are streams of positively charged ions formed when high-voltage electricity ionizes residual gas in a discharge tube.\n2. Their deflection in electric and magnetic fields toward the negative electrode proved the existence of positive subatomic charges.\n3. Because these charges reside inside all atoms, the atom cannot be a solid, indivisible fundamental particle as Dalton claimed.",
                "finalAnswer": "Canal rays are streams of positively charged subatomic particles (protons) discovered by Goldstein; their existence proved that atoms contain internal subatomic constituents.",
                "unit": "Subatomic Physics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.2: Goldstein's canal ray discharge tube with perforated cathode"
            },
            {
                "problem": "If an atom contains one electron and one proton, will it carry any charge or be neutral? Explain.",
                "given": "Atom composed of 1 proton and 1 electron.",
                "formula": "Net Charge $Q_{net} = q_{proton} + q_{electron}$.",
                "substitution": "$q_{proton} = +1.6 \\times 10^{-19}\\text{ C} = +1$; $q_{electron} = -1.6 \\times 10^{-19}\\text{ C} = -1$.",
                "calculation": "$Q_{net} = (+1) + (-1) = 0$.",
                "finalAnswer": "The atom will be electrically neutral because the unit positive charge of the proton exactly balances the unit negative charge of the electron.",
                "unit": "NCERT In-Text Problem",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.4: Electrical neutrality of positive proton and negative electron"
            },
            {
                "problem": "Construct a comparative table showing the relative mass, absolute charge, and nuclear/extranuclear location of the electron, proton, and neutron.",
                "given": "The three fundamental subatomic particles.",
                "formula": "Tri-Particulate Fundamental Constants Ledger",
                "substitution": "Compile empirical constants.",
                "calculation": "| Particle | Symbol | Absolute Charge | Relative Charge | Approximate Mass | Location in Atom |\n| :--- | :--- | :--- | :--- | :--- | :--- |\n| **Electron** | $e^-$ | $-1.602 \\times 10^{-19}\\text{ C}$ | $-1$ | $\\frac{1}{1840}\\text{ u} \\approx 0.00055\\text{ u}$ | Revolving in shells outside nucleus |\n| **Proton** | $p^+$ | $+1.602 \\times 10^{-19}\\text{ C}$ | $+1$ | $1.0073\\text{ u} \\approx 1\\text{ u}$ | Inside atomic nucleus |\n| **Neutron** | $n^0$ | $0\\text{ C}$ | $0$ | $1.0087\\text{ u} \\approx 1\\text{ u}$ | Inside atomic nucleus |",
                "finalAnswer": "Electrons (-1, ~0 u, extra-nuclear shells), Protons (+1, 1 u, nucleus), Neutrons (0, 1 u, nucleus).",
                "unit": "Subatomic Ledger",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.7: Subatomic particle triad within atomic architecture"
            },
            {
                "problem": "Which subatomic particle is not present in an ordinary hydrogen atom (Protium)?",
                "given": "Protium isotope ($^1_1H$). Atomic number $Z = 1$, Mass number $A = 1$.",
                "formula": "Neutron Number $N = A - Z$.",
                "substitution": "$N = 1 - 1 = 0$.",
                "calculation": "Protium contains 1 proton in its nucleus and 1 revolving electron, but **zero neutrons**.",
                "finalAnswer": "The neutron is absent in an ordinary hydrogen atom (Protium).",
                "unit": "Isotopic Invariant",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.8: Nuclear structure of Protium compared with Deuterium and Tritium"
            },
            {
                "problem": "Why was the discovery of the neutron delayed until 1932, whereas electrons and protons were discovered in the late 19th century?",
                "given": "Electrical neutrality of neutrons vs charged electrons and protons.",
                "formula": "Electromagnetic Deflection Principle",
                "substitution": "Electrons and protons carry electric charges and interact strongly with electric and magnetic fields.",
                "calculation": "1. Electrons and protons produce visible deflections in cathode ray and canal ray tubes and trigger electrical detectors because they are charged.\n2. Neutrons carry zero electrical charge ($q = 0$), so they pass through electromagnetic fields completely undeflected.\n3. They could only be discovered through nuclear scattering and recoil reactions using high-energy $\\alpha$-particles on beryllium targets.",
                "finalAnswer": "Neutrons carry no electric charge and do not deflect in electric or magnetic fields, making them invisible to standard electrostatic detectors until Chadwick's 1932 nuclear bombardment experiments.",
                "unit": "Historical Physics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.9: Neutral radiation penetrating paraffin wax target"
            },
            {
                "problem": "How does rubbing a plastic ruler through dry hair allow it to attract uncharged bits of paper? Explain in terms of electron transfer.",
                "given": "Activity 8.1: Frictional triboelectric charging.",
                "formula": "Triboelectric Electron Transfer: $\\Delta Q = \\pm n \\cdot e$.",
                "substitution": "Electrons transfer from hair to plastic due to difference in electron affinity.",
                "calculation": "1. Plastic has higher electron affinity than dry hair.\n2. Friction transfers electrons from hair to the plastic ruler, giving the ruler a net **negative charge**.\n3. When brought near neutral paper bits, the negative ruler repels electrons in paper and attracts the positive nuclei near the surface (electrostatic induction).\n4. The attractive force exceeds repulsive force, lifting the paper.",
                "finalAnswer": "Friction transfers electrons from hair to the ruler giving it negative charge; electrostatic induction polarizes the paper bits, causing attraction.",
                "unit": "Activity 8.1 Lab Analysis",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.10: Triboelectric charging and electrostatic attraction of paper bits"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Neutrons are positively charged particles because they live inside the positive nucleus.",
                "correction": "Neutrons carry ZERO electrical charge (they are completely neutral). The positive charge of the nucleus is contributed solely by protons.",
                "why_it_matters": "Fundamental distinction in nuclear physics."
            }
        ],
        "visual_lesson_plan": {
            "title": "Subatomic Revolution Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Electrical Nature of Matter: Matter contains charged particles, proven by frictional electricity (combing dry hair attracts small bits of paper, rubbing glass rod with silk cloth).",
                    "diagram_title": "Triboelectric Frictional Charging",
                    "diagram_type": "image",
                    "image_query": "static electricity comb attracting paper bits diagram",
                    "video_query": "static electricity comb paper experiment",
                    "image_url": "/extracted_diagrams/ch8/fig_8_10.webp",
                    "what_to_make": "Textbook diagram showing plastic comb rubbed with hair attracting small bits of paper.",
                    "timing_and_cue": "Mount frictional electricity on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_10.webp | Frictional Electricity | Proving matter possesses subatomic electrical charge\")"
                },
                {
                    "concept_title": "Cathode Rays & Electron Discovery: J.J. Thomson (1897) identified cathode rays as streams of negatively charged subatomic particles called electrons, with negligible mass (~1/2000 of a hydrogen atom) and unit negative charge (-1.6 * 10^-19 C).",
                    "diagram_title": "Thomson Cathode Ray Discharge Tube",
                    "diagram_type": "image",
                    "image_query": "cathode ray tube JJ Thomson electron experiment diagram",
                    "video_query": "JJ Thomson cathode ray tube experiment",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Cathode_ray_tube_diagram-en.svg",
                    "what_to_make": "Diagram of discharge tube showing cathode, anode, fluorescent screen, and electric deflection plates.",
                    "timing_and_cue": "Mount cathode ray tube on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/e0/Cathode_ray_tube_diagram-en.svg | Cathode Ray Tube | Discovery of electron by deflection toward positive plate\")"
                },
                {
                    "concept_title": "Canal Rays & Proton Discovery: E. Goldstein (1886) discovered positively charged radiations in a modified gas discharge tube called canal rays, leading to the identification of the proton with mass equal to 1 atomic mass unit and unit positive charge (+1.6 * 10^-19 C).",
                    "diagram_title": "Goldstein Canal Ray Discharge Tube",
                    "diagram_type": "image",
                    "image_query": "canal rays anode rays goldstein perforated cathode discharge tube diagram",
                    "video_query": "canal rays goldstein proton discovery",
                    "image_url": "/extracted_diagrams/ch8/fig_8_2.webp",
                    "what_to_make": "Textbook diagram of Goldstein's discharge tube with perforated cathode showing canal rays.",
                    "timing_and_cue": "Mount canal rays on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_2.webp | Goldstein Canal Rays | Positive ions passing through perforated cathode\")"
                },
                {
                    "concept_title": "Neutron Discovery: James Chadwick (1932) discovered subatomic particles having no electrical charge and a mass nearly equal to that of a proton, designated as neutrons (n), located within the atomic nucleus.",
                    "diagram_title": "Chadwick Neutron Discovery Experiment",
                    "diagram_type": "image",
                    "image_query": "james chadwick discovery of neutron experiment diagram",
                    "video_query": "discovery of neutron chadwick animation",
                    "image_url": "/extracted_diagrams/ch8/fig_8_9.webp",
                    "what_to_make": "Textbook diagram showing alpha particle bombardment on beryllium target releasing neutral neutrons.",
                    "timing_and_cue": "Mount neutron discovery on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_9.webp | Chadwick Neutron Discovery | Neutral penetrating radiation from beryllium bombardment\")"
                },
                {
                    "concept_title": "Tri-Particulate Atomic Ledger: An atom consists of three fundamental subatomic particles: Protons (+1 charge, 1 u mass in nucleus), Neutrons (0 charge, 1 u mass in nucleus), and Electrons (-1 charge, 1/1840 u mass in orbits).",
                    "diagram_title": "Tri-Particulate Subatomic Particle Table",
                    "diagram_type": "image",
                    "image_query": "subatomic particles electron proton neutron mass charge table diagram",
                    "video_query": "subatomic particles explained",
                    "image_url": "/extracted_diagrams/ch8/fig_8_7.webp",
                    "what_to_make": "Textbook comparative ledger comparing electron, proton, and neutron characteristics.",
                    "timing_and_cue": "Mount subatomic ledger on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_7.webp | Subatomic Triad | Electron, Proton, Neutron mass and charge properties\")"
                },
                {
                    "concept_title": "Electrical Neutrality Axiom: In any neutral atom, the number of positive protons inside the nucleus identically equals the number of negative electrons revolving outside.",
                    "diagram_title": "Electrical Neutrality Atomic Balance",
                    "diagram_type": "image",
                    "image_query": "neutral atom protons equal electrons balance diagram",
                    "video_query": "why atoms are electrically neutral",
                    "image_url": "/extracted_diagrams/ch8/fig_8_4.webp",
                    "what_to_make": "Textbook diagram showing positive nucleus balanced by surrounding negative electrons.",
                    "timing_and_cue": "Mount electrical neutrality on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_4.webp | Electrical Neutrality | Number of protons equals number of electrons\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "When you rub a plastic comb in your hair, it lifts pieces of paper. What did you transfer: whole atoms or pieces of atoms?"
   - Law: Detail electron, proton, and neutron discovery timelines and charge invariants.
   - Socratic check: "Why did cathode rays deflect toward the positive electric plate, but canal rays deflected toward the negative plate?" HARD STOP: Wait for student answer!"""
    }

    # Module 2: Thomson vs Rutherford Gold Foil Experiment
    m2 = {
        "order_index": 2,
        "title": "Early Atomic Architecture: Thomson's Plum Pudding Model vs Rutherford's Gold Foil Experiment",
        "description": "Analyze J.J. Thomson's Plum Pudding (Watermelon) model of the atom, contrast it with Ernest Rutherford's historic alpha-particle gold foil scattering experiment, and deduce the existence of the ultra-dense atomic nucleus.",
        "subtopics": [
            "Thomson's Model of the Atom (1904): Positive sphere embedded with negative electrons (Plum Pudding / Watermelon)",
            "Postulates of Thomson's Model: Uniform positive sphere and electrical neutrality",
            "Rutherford's Alpha-Particle Scattering Experiment (1911): Experimental design and components",
            "Why Gold Foil & Alpha Particles: 1000 atoms thin gold leaf and doubly charged helium ions (He^2+)",
            "The Three Astounding Observations: Most pass undeflected, few deflect at large angles, 1 in 12000 rebounds",
            "Deductions from Observations: Mostly empty space, positive charge concentrated in tiny central volume (nucleus)"
        ],
        "key_concepts": [
            "Thomson's Model (Plum Pudding): An atom consists of a positively charged sphere with electrons embedded in it like raisins in a Christmas pudding or seeds in a red watermelon.",
            "Thomson's Success & Failure: It successfully explained the overall electrical neutrality of atoms, but failed completely to predict the scattering of alpha particles.",
            "Rutherford's Alpha-Scattering Design: High-energy alpha particles (doubly ionized helium nuclei, 4 u mass) directed at ultra-thin gold foil (~1000 atoms thick, 100 nm) surrounded by a circular fluorescent zinc sulphide screen.",
            "Observation 1 (Empty Space): Most of the fast-moving alpha particles passed straight through the gold foil without any deflection, proving most of the atom is empty space.",
            "Observation 2 (Concentrated Positive Charge): A small fraction of alpha particles were deflected by small and large angles, proving positive charge occupies very little volume.",
            "Observation 3 (Dense Core Rebound): Astonishingly, about 1 in 12,000 particles rebounded back (theta = 180 deg), proving all the mass and positive charge is concentrated in a tiny dense core called the nucleus."
        ],
        "success_criteria": "Student can sketch Thomson's model, describe Rutherford's alpha scattering experiment, state its 3 observations and deductions, and calculate the nuclear volume fraction.",
        "chapter_notes": """### 8.5 J.J. Thomson's Model of the Atom (1904)
Thomson proposed the first subatomic model, known as the **Plum Pudding Model** or **Watermelon Model**:
1. An atom consists of a **uniformly distributed positive sphere**.
2. **Electrons are embedded** in this positive sphere, like:
   - Raisins (plums) in a spherical Christmas pudding.
   - Black seeds embedded in the red edible flesh of a watermelon.
3. The negative and positive charges are equal in magnitude; hence, the atom as a whole is **electrically neutral**.
- **Limitation**: It could not explain why alpha particles are deflected by large angles in Rutherford's scattering experiments.

### 8.6 Rutherford's $\\alpha$-Particle Scattering Experiment (1911)
Ernest Rutherford, along with Hans Geiger and Ernest Marsden, tested Thomson's model:
- **Projectiles**: $\\alpha$-particles ($^4_2He^{2+}$, doubly charged helium ions with mass $4\\text{ u}$ and high kinetic energy).
- **Target**: Ultra-thin **gold foil** (approximately $1000\\text{ atoms thick}$, thickness $\\sim 10^{-7}\\text{ m} = 100\\text{ nm}$). Gold was chosen because it has maximum malleability.
- **Detector**: Circular fluorescent screen coated with zinc sulphide ($ZnS$), which emitted tiny flashes of light (scintillations) when struck by an $\\alpha$-particle.

### 8.7 The Three Crucial Observations
1. **Most $\\alpha$-particles (~99.9%)** passed straight through the gold foil without any deflection.
2. **A small fraction** of $\\alpha$-particles were deflected by small angles, and some by large angles ($> 90^\\circ$).
3. **Astonishingly, 1 in every 12,000 particles** appeared to rebound straight backward ($180^\\circ$).
*Rutherford famously remarked: "It was quite the most incredible event that has ever happened to me in my life. It was almost as incredible as if you fired a 15-inch shell at a piece of tissue paper and it came back and hit you."*

### 8.8 Rutherford's Deductions
1. **From Observation 1**: Most of the space inside the atom is **completely empty**, because most particles passed undeflected.
2. **From Observation 2**: The positive charge of the atom occupies **very little space**, because very few particles suffered deflections.
3. **From Observation 3**: All the positive charge and almost the entire mass of the atom is concentrated in an **extremely small volume** at the centre of the atom, which Rutherford termed the **NUCLEUS**.
- **Nuclear Dimension Scale**: Radius of nucleus $\\sim 10^{-15}\\text{ m}$; Radius of atom $\\sim 10^{-10}\\text{ m}$. The nucleus is $10^5$ times smaller in radius (like a marble placed in the centre of a massive cricket stadium).""",
        "worked_examples": [
            {
                "problem": "State the three primary observations made by Rutherford in his alpha-particle scattering experiment and write down the corresponding deduction for each observation.",
                "given": "Rutherford's gold foil alpha scattering experiment.",
                "formula": "Observation -> Physical Deduction Matrix",
                "substitution": "Correlate particle trajectories with nuclear structure.",
                "calculation": "1. **Observation 1**: Most alpha particles passed straight through without deflection.\n   *Deduction*: Most of the space inside the atom is completely empty.\n2. **Observation 2**: A few alpha particles were deflected through small and large angles.\n   *Deduction*: The positive charge occupies very little volume inside the atom.\n3. **Observation 3**: 1 in ~12,000 alpha particles rebounded back (theta ~ 180°).\n   *Deduction*: All positive charge and nearly all atomic mass is concentrated in an ultra-dense, tiny central core called the **nucleus**.",
                "finalAnswer": "(1) Most pass straight -> atom is mostly empty; (2) Few deflect -> positive charge occupies little space; (3) 1 in 12,000 rebounds -> mass and positive charge concentrated in tiny central nucleus.",
                "unit": "Nuclear Epistemology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.4: Schematic view of Rutherford's gold foil experiment showing alpha trajectories"
            },
            {
                "problem": "Why did Rutherford select a gold foil rather than any other metal for his alpha-particle scattering experiment?",
                "given": "Selection of target material for alpha transmission.",
                "formula": "Malleability & Thickness Minimization Criterion",
                "substitution": "Minimizing atomic layers to ensure single-atom scattering events.",
                "calculation": "1. Rutherford required the thinnest possible metal sheet so that an alpha particle would collide with only one atom during its transit.\n2. Gold is the most malleable metal known to humanity, capable of being beaten into a foil only 1000 atoms thick (~100 nm).\n3. Any other metal foil would be significantly thicker, causing multiple overlapping scatterings that would obscure the true nuclear deflection pattern.",
                "finalAnswer": "Gold was selected because of its unmatched malleability, enabling the creation of an ultra-thin foil only ~1000 atoms thick.",
                "unit": "Experimental Design",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.4: Ultra-thin gold foil target atomic cross-section"
            },
            {
                "problem": "If the radius of an atom is 10^-10 m and the radius of its nucleus is 10^-15 m, calculate the ratio of the volume of the atom to the volume of the nucleus. What does this reveal about atomic density?",
                "given": "Radius of atom $R = 10^{-10}\\text{ m}$, radius of nucleus $r = 10^{-15}\\text{ m}$.",
                "formula": "Volume of sphere $V = \\frac{4}{3}\\pi r^3 \\implies \\frac{V_{atom}}{V_{nucleus}} = \\left(\\frac{R}{r}\\right)^3$.",
                "substitution": "$\\frac{V_{atom}}{V_{nucleus}} = \\left(\\frac{10^{-10}}{10^{-15}}\\right)^3 = (10^5)^3$.",
                "calculation": "$\\frac{V_{atom}}{V_{nucleus}} = 10^{15} = \\mathbf{1,000,000,000,000,000}$.",
                "finalAnswer": "The atom is 10^15 (one quadrillion) times larger in volume than its nucleus, proving that the atom is overwhelmingly empty space with an immensely dense nucleus.",
                "unit": "Volume Ratio",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.7: Scale comparison of atomic volume vs nuclear volume"
            },
            {
                "problem": "Compare Thomson's atomic model with a watermelon and explain how electrons and positive charge are arranged.",
                "given": "Thomson's plum pudding / watermelon model.",
                "formula": "Continuous Charge Fluid vs Discrete Embeddings",
                "substitution": "Watermelon red flesh represents positive charge; black seeds represent negative electrons.",
                "calculation": "1. In Thomson's model, the positive charge is spread out continuously like the red edible flesh of a watermelon throughout the atomic sphere.\n2. The negative electrons are embedded individually like black watermelon seeds inside this positive matrix.\n3. The magnitude of total positive charge of the matrix equals the total negative charge of all embedded electrons, maintaining neutral balance.",
                "finalAnswer": "Positive charge is the continuous red pulp; negative electrons are embedded like black seeds, maintaining overall electrical neutrality.",
                "unit": "Historical Analogy",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.2: Thomson's watermelon model of atomic architecture"
            },
            {
                "problem": "What would have been observed in Rutherford's experiment if Thomson's plum pudding model had been correct?",
                "given": "Hypothetical alpha scattering through Thomson's uniform positive sphere.",
                "formula": "Coulomb Repulsion in Diffuse Charge Distribution",
                "substitution": "Thomson's model has positive charge and mass spread thinly across the entire volume.",
                "calculation": "1. In Thomson's model, positive charge is diluted over the entire atom (~10^-10 m), creating a very weak electric field.\n2. Heavy, high-speed alpha particles (4 u) would easily punch through this diffuse positive sphere with almost zero resistance.\n3. Deflections, if any, would be fractions of a degree.\n4. No particle would ever deflect at large angles (>90°), and a 180° rebound would be physically impossible.",
                "finalAnswer": "All alpha particles would have passed straight through with negligible deflections; large angle deflections and rebounds would never have occurred.",
                "unit": "Theoretical Deduction",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.4: Expected Thomson scattering vs actual Rutherford nuclear deflection"
            },
            {
                "problem": "Why did Rutherford's observation that 1 in 12,000 alpha particles rebounded lead to the conclusion that atomic mass is concentrated in the nucleus?",
                "given": "1 in 12,000 alpha particles rebounding at 180°.",
                "formula": "Head-on Elastic Collision Dynamics",
                "substitution": "An alpha particle has high mass (4 u) and immense speed (~10^7 m/s).",
                "calculation": "1. For a projectile with mass 4 u and speed 1.5 * 10^7 m/s to stop and reverse direction completely, it must collide head-on with a stationary target that is vastly heavier than itself.\n2. If atomic mass was spread thinly throughout the atom (as Thomson believed), the alpha particle would push through like a bullet through fog.\n3. The violent rebound proves the alpha particle hit a rigid, ultra-heavy, concentrated obstacle containing virtually the entire mass of the gold atom.",
                "finalAnswer": "A fast alpha particle can only rebound if it collides head-on with an ultra-dense, concentrated mass much heavier than itself (the gold nucleus).",
                "unit": "Collision Dynamics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.4: Head-on collision trajectory of rebounding alpha particle"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Alpha particles were repelled because they hit solid matter like tiny billiard balls.",
                "correction": "Alpha particles were repelled by intense electrostatic Coulomb repulsion between the positively charged alpha particle (+2e) and the concentrated positive charge of the gold nucleus (+79e).",
                "why_it_matters": "Fundamental electrodynamics of nuclear scattering."
            }
        ],
        "visual_lesson_plan": {
            "title": "Thomson vs Rutherford Scattering Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Thomson's Model (Plum Pudding): An atom consists of a positively charged sphere with electrons embedded in it like raisins in a Christmas pudding or seeds in a red watermelon.",
                    "diagram_title": "Thomson Plum Pudding Watermelon Model",
                    "diagram_type": "image",
                    "image_query": "JJ Thomson plum pudding model watermelon diagram atom",
                    "video_query": "thomson atomic model animation",
                    "image_url": "/extracted_diagrams/ch8/fig_8_2.webp",
                    "what_to_make": "Textbook diagram showing Thomson's positive sphere with embedded negative electrons.",
                    "timing_and_cue": "Mount Thomson model on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_2.webp | Thomson's Model | Positive sphere embedded with negative electrons\")"
                },
                {
                    "concept_title": "Thomson's Success & Failure: It successfully explained the overall electrical neutrality of atoms, but failed completely to predict the scattering of alpha particles.",
                    "diagram_title": "Thomson Electrical Neutrality Balance",
                    "diagram_type": "image",
                    "image_query": "thomson model electrical neutrality positive sphere diagram",
                    "video_query": "drawbacks of thomson atomic model",
                    "image_url": "/extracted_diagrams/ch8/fig_8_4.webp",
                    "what_to_make": "Textbook schematic contrasting Thomson's diffuse atom with experimental reality.",
                    "timing_and_cue": "Mount Thomson limitations on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_4.webp | Thomson Limitation | Explains neutrality but fails alpha scattering\")"
                },
                {
                    "concept_title": "Rutherford's Alpha-Scattering Design: High-energy alpha particles (doubly ionized helium nuclei, 4 u mass) directed at ultra-thin gold foil (~1000 atoms thick, 100 nm) surrounded by a circular fluorescent zinc sulphide screen.",
                    "diagram_title": "Rutherford Gold Foil Experimental Apparatus",
                    "diagram_type": "image",
                    "image_query": "rutherford gold foil experiment apparatus radioactive source screen diagram",
                    "video_query": "rutherford gold foil experiment setup",
                    "image_url": "/extracted_diagrams/ch8/fig_8_4.webp",
                    "what_to_make": "Textbook layout of alpha source, collimator, gold foil, and rotatable scintillation screen.",
                    "timing_and_cue": "Mount experiment setup on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_4.webp | Rutherford Experiment Setup | Alpha source directed at 1000-atom gold leaf\")"
                },
                {
                    "concept_title": "Observation 1 (Empty Space): Most of the fast-moving alpha particles passed straight through the gold foil without any deflection, proving most of the atom is empty space.",
                    "diagram_title": "Undeflected Alpha Particle Beam",
                    "diagram_type": "image",
                    "image_query": "rutherford alpha scattering straight pass undeflected empty space diagram",
                    "video_query": "alpha particles passing through empty space",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Rutherford_gold_foil_experiment_results.svg",
                    "what_to_make": "Diagram showing 99.9% of alpha rays passing straight through atomic lattices without interaction.",
                    "timing_and_cue": "Mount empty space deduction on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/e1/Rutherford_gold_foil_experiment_results.svg | Observation 1: Empty Space | 99.9% particles pass straight through\")"
                },
                {
                    "concept_title": "Observation 2 (Concentrated Positive Charge): A small fraction of alpha particles were deflected by small and large angles, proving positive charge occupies very little volume.",
                    "diagram_title": "Scattering Angle Coulomb Deflection",
                    "diagram_type": "image",
                    "image_query": "alpha particle coulomb deflection nucleus scattering angle diagram",
                    "video_query": "alpha particle deflection angle",
                    "image_url": "/extracted_diagrams/ch8/fig_8_7.webp",
                    "what_to_make": "Textbook trajectory diagram showing hyperbolic Coulomb deflection around positive nucleus.",
                    "timing_and_cue": "Mount deflection angles on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_7.webp | Observation 2: Small & Large Deflections | Hyperbolic repulsion by concentrated positive charge\")"
                },
                {
                    "concept_title": "Observation 3 (Dense Core Rebound): Astonishingly, about 1 in 12,000 particles rebounded back (theta = 180 deg), proving all the mass and positive charge is concentrated in a tiny dense core called the nucleus.",
                    "diagram_title": "Head-On Rebound and Nuclear Concentrated Mass",
                    "diagram_type": "image",
                    "image_query": "rutherford alpha particle 1 in 12000 rebound nucleus diagram",
                    "video_query": "rutherford alpha rebound 180 degrees",
                    "image_url": "/extracted_diagrams/ch8/fig_8_8.webp",
                    "what_to_make": "Textbook diagram showing head-on collision of alpha particle with ultra-dense nucleus rebounding 180 degrees.",
                    "timing_and_cue": "Mount 180-degree rebound on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_8.webp | Observation 3: 180° Rebound | Proving all atomic mass is in the ultra-dense nucleus\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "Rutherford said firing alpha particles at gold foil was like firing a 15-inch artillery shell at tissue paper and having it bounce back and hit you! Why was it so shocking?"
   - Observations -> Deductions: Map the 3 observations to their deductions on the board.
   - Socratic check: "If gold atoms were solid spheres like Thomson said, how would alpha particles have behaved?" HARD STOP: Wait for student answer!"""
    }

    # Module 3: Rutherford's Nuclear Model & Bohr's Quantized Postulates
    m3 = {
        "order_index": 3,
        "title": "Rutherford's Planetary Model, Its Fatal Instability & Bohr's Quantized Orbits",
        "description": "Formulate Rutherford's nuclear planetary model, examine the electro-dynamic collapse paradox (Maxwell's radiation of accelerating charges), and master Neils Bohr's revolutionary postulates of quantized stationary discrete orbits.",
        "subtopics": [
            "Rutherford's Nuclear Model Postulates: Tiny positive nucleus and orbiting planetary electrons",
            "The Fatal Flaw of Rutherford's Model: Maxwell's classical electromagnetic theory",
            "The Electro-Dynamic Collapse Paradox: Accelerating charges must radiate energy and spiral into nucleus in 10^-8 s",
            "Neils Bohr's Revolutionary Postulates (1913): Discrete non-radiating stationary orbits",
            "Bohr's Energy Levels: Shells designated K, L, M, N... or principal quantum numbers n = 1, 2, 3, 4...",
            "Photonic Transitions: Energy absorption during excitation and emission during de-excitation (Delta E = h * nu)"
        ],
        "key_concepts": [
            "Rutherford's Nuclear Model: An atom has a positively charged, ultra-dense center called the nucleus containing nearly all atomic mass; electrons revolve around the nucleus in circular planetary paths.",
            "Rutherford Nuclear Postulate 2: The size of the nucleus is extremely small (~10^-15 m) compared to the overall atom (~10^-10 m).",
            "The Electro-Dynamic Collapse Paradox: According to classical electromagnetism (Maxwell), any charged particle undergoing circular acceleration must continuously radiate electromagnetic energy, losing speed and spiraling into the nucleus within 10^-8 seconds.",
            "Bohr's First Postulate (Discrete Orbits): Only certain special orbits known as discrete orbits or stationary states of electrons are allowed inside the atom.",
            "Bohr's Second Postulate (Zero Radiation): While revolving in these discrete orbits, electrons do NOT radiate energy, keeping the atom completely stable.",
            "Bohr's Energy Shells: Energy levels are represented by letters K, L, M, N... or integer numbers n = 1, 2, 3, 4... where energy increases with distance from nucleus."
        ],
        "success_criteria": "Student can state Rutherford's model, explain the classical radiation collapse paradox, state Bohr's two postulates, and label Bohr's K, L, M, N energy shells.",
        "chapter_notes": """### 8.9 Rutherford's Nuclear Model of the Atom
On the basis of his scattering experiment, Rutherford put forward the **Nuclear Model**:
1. There is a **positively charged centre** in an atom called the **nucleus**. Nearly all the mass of an atom resides in the nucleus.
2. The **electrons revolve around the nucleus** in circular orbits (analogous to planets revolving around the Sun).
3. The size of the nucleus is extremely small compared to the size of the atom ($r_{nucleus} \\approx 10^{-15}\\text{ m}$ vs $r_{atom} \\approx 10^{-10}\\text{ m}$).

### 8.10 The Fatal Drawback of Rutherford's Model
- **Classical Electrodynamics (Maxwell's Theory)**: Any charged particle in circular motion experiences centripetal acceleration ($a = v^2/r$).
- An accelerating charge must continuously radiate electromagnetic energy.
- As the revolving electron loses energy, its orbital radius must shrink continuously.
- The electron would follow an inward spiral and crash into the positive nucleus in approximately **$10^{-8}\\text{ seconds}$**!
- If this were true, all atoms would collapse instantly, and matter could not exist. Yet, matter is completely stable.

### 8.11 Neils Bohr's Model of the Atom (1913)
To overcome the instability of Rutherford's model, Neils Bohr proposed two revolutionary postulates:
1. **Postulate 1 (Discrete Stationary Orbits)**: Only certain special orbits known as **discrete orbits** (or non-radiating stationary states) are allowed inside the atom.
2. **Postulate 2 (No Energy Radiation)**: While revolving in these discrete orbits, the electrons **do not radiate energy**.
3. **Energy Shells**: These orbits or shells are called **energy levels**:
   - Represented by letters: **K, L, M, N, ...**
   - Represented by principal quantum numbers: **$n = 1, 2, 3, 4, ...$**
   - Innermost shell $K$ ($n=1$) has the lowest energy; energy increases progressively for $L, M, N$ shells.
   - An electron radiates or absorbs energy only when it jumps from one discrete orbit to another: $\\Delta E = E_2 - E_1 = h\\nu$.""",
        "worked_examples": [
            {
                "problem": "What was the major drawback of Rutherford's model of the atom, and how did Neils Bohr successfully resolve it?",
                "given": "Comparison between Rutherford's planetary model and Bohr's quantized model.",
                "formula": "Classical Continuous Radiation vs Quantized Discrete Non-Radiating States",
                "substitution": "Accelerating charges radiate energy in Maxwell's theory; Bohr introduced quantized stationary orbits.",
                "calculation": "1. **Drawback**: In Rutherford's model, electrons in circular orbits experience centripetal acceleration. By Maxwell's electrodynamics, accelerating charges radiate energy continuously. The electron would spiral inward and crash into the nucleus within ~10^-8 s, making stable matter impossible.\n2. **Bohr's Resolution**: Bohr postulated that electrons revolve only in specific **discrete orbits** where they **do not radiate energy**. Energy is only absorbed or emitted when jumping between discrete levels.",
                "finalAnswer": "Rutherford's model could not explain atomic stability against electro-dynamic collapse; Bohr resolved it by postulating discrete, non-radiating stationary energy shells (K, L, M, N).",
                "unit": "Quantum Epistemology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.7: Energy levels in an atom showing K, L, M, N shells (n = 1, 2, 3, 4)"
            },
            {
                "problem": "Draw a neat sketch of Bohr's model of an atom with four shells and label the energy levels using letters and principal quantum numbers.",
                "given": "Neils Bohr's atomic energy shell architecture.",
                "formula": "Concentric Quantized Spherical Shells",
                "substitution": "Nucleus at center, concentric circles for n = 1 (K), n = 2 (L), n = 3 (M), n = 4 (N).",
                "calculation": "1. Center: Nucleus containing protons and neutrons.\n2. First concentric circle: Shell K ($n = 1$) - lowest energy.\n3. Second concentric circle: Shell L ($n = 2$).\n4. Third concentric circle: Shell M ($n = 3$).\n5. Fourth concentric circle: Shell N ($n = 4$) - highest energy of the four.",
                "finalAnswer": "Sketch showing central nucleus surrounded by concentric shells: n=1 (K), n=2 (L), n=3 (M), n=4 (N).",
                "unit": "NCERT In-Text Problem",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.7: Bohr's atomic energy levels with shells K, L, M, N"
            },
            {
                "problem": "Why does an electron revolving in Bohr's K-shell not fall into the positively charged nucleus despite mutual electrostatic attraction?",
                "given": "Electron in innermost K-shell ($n = 1$).",
                "formula": "Quantized Ground State Stability",
                "substitution": "K-shell is the minimum allowable energy level ($n = 1$).",
                "calculation": "1. By Bohr's postulates, an electron cannot possess an orbital radius smaller than the $n = 1$ K-shell ($r_1 \\approx 0.053\\text{ nm}$).\n2. There are no permissible discrete quantum states with energy lower than the ground state.\n3. Because the electron in this stationary orbit does not radiate electromagnetic energy, it cannot lose energy to spiral further inward.",
                "finalAnswer": "The K-shell is the lowest permissible quantized energy level; since the electron cannot radiate energy in stationary orbits, it cannot fall into the nucleus.",
                "unit": "Quantum Mechanics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.7: Ground state stability of K-shell orbit"
            },
            {
                "problem": "What happens when an electron absorbs a photon of energy equal to the difference between the K-shell and M-shell?",
                "given": "Energy absorption $\\Delta E = E_M - E_K$.",
                "formula": "Bohr Quantum Transition: $\\Delta E = h\\nu$.",
                "substitution": "Electron transitions from lower energy level ($n = 1$) to higher energy level ($n = 3$).",
                "calculation": "1. The electron absorbs the discrete photon packet ($h\\nu$) and jumps instantly from the ground state K-shell ($n = 1$) to the excited state M-shell ($n = 3$).\n2. The atom enters an unstable **excited state**.\n3. Within ~10^-8 s, the electron de-excites back to lower energy levels, emitting a photon of identical frequency.",
                "finalAnswer": "The electron absorbs the photon and transitions from the K-shell (n=1) to the excited M-shell (n=3), subsequently re-emitting light upon de-excitation.",
                "unit": "Quantum Transition",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.8: Quantum absorption and emission transitions between energy levels"
            },
            {
                "problem": "Compare the solar system planetary model with Rutherford's atomic model. What is the fundamental difference in the nature of forces?",
                "given": "Planets orbiting Sun vs Electrons orbiting Nucleus.",
                "formula": "Gravitational vs Electrostatic Coulomb Force: $F_g = \\frac{G M m}{r^2}$ vs $F_e = \\frac{k q_1 q_2}{r^2}$.",
                "substitution": "Planets are uncharged masses; electrons and nuclei are charged particles.",
                "calculation": "1. **Similarity**: Both involve a massive central core with lighter bodies revolving in curved orbits due to an inverse-square central force.\n2. **Difference**: In the solar system, the governing force is **gravitational attraction** between neutral masses (always attractive, extremely weak). In the atom, the governing force is **electrostatic Coulomb attraction** between opposite electrical charges (vastly stronger, $\\sim 10^{36}$ times stronger than gravity).",
                "finalAnswer": "Planetary orbits are governed by gravitational forces between neutral masses; atomic orbits are governed by electrostatic Coulomb forces between electrical charges.",
                "unit": "Comparative Physics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.4: Comparison between planetary solar system and Rutherford atomic model"
            },
            {
                "problem": "State two key limitations of Bohr's atomic model that required further development in modern quantum mechanics.",
                "given": "Bohr's 1913 semi-classical atomic model.",
                "formula": "Limits of Semi-Classical Quantum Theory",
                "substitution": "Bohr model applies accurately only to single-electron systems (hydrogen-like).",
                "calculation": "1. **Multi-electron failure**: It cannot accurately predict the spectral lines and energy levels of complex atoms with multiple electrons.\n2. **Wave nature omission**: It treats electrons as classical circular particles, ignoring the wave-particle duality (de Broglie) and Heisenberg's Uncertainty Principle (wave mechanics).",
                "finalAnswer": "(1) Failed to explain spectra of multi-electron atoms; (2) Treated electrons as deterministic particles rather than 3D quantum wave-orbitals.",
                "unit": "Quantum Limitations",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.7: Discrete 1D Bohr orbits vs modern 3D quantum electron clouds"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Electrons revolve around the nucleus exactly like planets orbiting the sun forever without any difference.",
                "correction": "Planets are neutral masses governed by gravity. Electrons are charged particles that in classical physics would radiate energy and collapse. Only quantum non-radiating states (Bohr) make atomic orbits stable.",
                "why_it_matters": "The core paradox that birthed quantum mechanics."
            }
        ],
        "visual_lesson_plan": {
            "title": "Rutherford Instability & Bohr Orbits Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Rutherford's Nuclear Model: An atom has a positively charged, ultra-dense center called the nucleus containing nearly all atomic mass; electrons revolve around the nucleus in circular planetary paths.",
                    "diagram_title": "Rutherford Nuclear Planetary Model",
                    "diagram_type": "image",
                    "image_query": "rutherford planetary model nucleus orbiting electrons diagram",
                    "video_query": "rutherford atomic model animation",
                    "image_url": "/extracted_diagrams/ch8/fig_8_4.webp",
                    "what_to_make": "Textbook diagram showing central nucleus with revolving electrons in circular orbits.",
                    "timing_and_cue": "Mount Rutherford model on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_4.webp | Rutherford Nuclear Model | Central positive nucleus surrounded by orbiting electrons\")"
                },
                {
                    "concept_title": "Rutherford Nuclear Postulate 2: The size of the nucleus is extremely small (~10^-15 m) compared to the overall atom (~10^-10 m).",
                    "diagram_title": "Scale Comparison Atom vs Nucleus",
                    "diagram_type": "image",
                    "image_query": "atom vs nucleus size comparison cricket stadium marble diagram",
                    "video_query": "scale of the atom vs nucleus",
                    "image_url": "/extracted_diagrams/ch8/fig_8_7.webp",
                    "what_to_make": "Textbook scale diagram illustrating 100,000x size difference between atom and nucleus.",
                    "timing_and_cue": "Mount atomic scale on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_7.webp | Scale Dimension | Nucleus is 100,000 times smaller than the atom\")"
                },
                {
                    "concept_title": "The Electro-Dynamic Collapse Paradox: According to classical electromagnetism (Maxwell), any charged particle undergoing circular acceleration must continuously radiate electromagnetic energy, losing speed and spiraling into the nucleus within 10^-8 seconds.",
                    "diagram_title": "Electrodynamic Spiral Collapse Paradox",
                    "diagram_type": "image",
                    "image_query": "rutherford atomic model electron spiral into nucleus collapse diagram",
                    "video_query": "drawback of rutherford model spiral collapse",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Rutherford_atom_instability.svg",
                    "what_to_make": "Diagram showing electron spiraling inward toward the nucleus due to continuous energy radiation.",
                    "timing_and_cue": "Mount spiral collapse on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/e/ec/Rutherford_atom_instability.svg | The Collapse Paradox | Maxwell radiation causes 10^-8 s inward spiral\")"
                },
                {
                    "concept_title": "Bohr's First Postulate (Discrete Orbits): Only certain special orbits known as discrete orbits or stationary states of electrons are allowed inside the atom.",
                    "diagram_title": "Bohr Quantized Discrete Orbits",
                    "diagram_type": "image",
                    "image_query": "bohr model discrete quantized orbits stationary states diagram",
                    "video_query": "bohrs postulates class 9",
                    "image_url": "/extracted_diagrams/ch8/fig_8_7.webp",
                    "what_to_make": "Textbook diagram showing discrete non-radiating quantized orbits.",
                    "timing_and_cue": "Mount discrete orbits on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_7.webp | Bohr Postulate 1 | Only discrete stationary orbits are permitted\")"
                },
                {
                    "concept_title": "Bohr's Second Postulate (Zero Radiation): While revolving in these discrete orbits, electrons do NOT radiate energy, keeping the atom completely stable.",
                    "diagram_title": "Non-Radiating Stationary States",
                    "diagram_type": "image",
                    "image_query": "bohr stationary states non radiating electrons stability diagram",
                    "video_query": "why electrons do not fall into nucleus bohr",
                    "image_url": "/extracted_diagrams/ch8/fig_8_8.webp",
                    "what_to_make": "Textbook diagram showing stable non-radiating orbital circulation.",
                    "timing_and_cue": "Mount zero radiation postulate on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_8.webp | Bohr Postulate 2 | Stationary orbits do not radiate energy, guaranteeing stability\")"
                },
                {
                    "concept_title": "Bohr's Energy Shells: Energy levels are represented by letters K, L, M, N... or integer numbers n = 1, 2, 3, 4... where energy increases with distance from nucleus.",
                    "diagram_title": "Energy Levels K L M N Shells",
                    "diagram_type": "image",
                    "image_query": "energy levels in an atom K L M N shells n equals 1 2 3 4 diagram",
                    "video_query": "energy shells K L M N bohr model",
                    "image_url": "/extracted_diagrams/ch8/fig_8_7.webp",
                    "what_to_make": "Textbook diagram showing central nucleus with concentric shells K (n=1), L (n=2), M (n=3), N (n=4).",
                    "timing_and_cue": "Mount K L M N shells on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_7.webp | Energy Levels K, L, M, N | Shell index n = 1, 2, 3, 4 with increasing energy\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "If classical physics says an accelerating electron must radiate energy and crash into the nucleus in a nanosecond, why are you and I still solid?"
   - Postulates: Write Bohr's discrete orbits and non-radiating states clearly.
   - Socratic check: "Why is the K-shell called the ground state, and what happens when an electron absorbs energy?" HARD STOP: Wait for student answer!"""
    }

    # Module 4: Electron Distribution (Bohr-Bury Rules)
    m4 = {
        "order_index": 4,
        "title": "Electronic Configuration Architecture: The Bohr-Bury Scheme (2n²) & Shell Distribution",
        "description": "Master the Bohr-Bury rules governing electron distribution across shells, formulate the 2n² capacity law, apply the octet limit on outermost shells, and construct complete geometric atomic configurations for the first 20 elements (H to Ca).",
        "subtopics": [
            "Bohr-Bury Rule 1: Maximum capacity of a shell is given by 2n^2 (K=2, L=8, M=18, N=32)",
            "Bohr-Bury Rule 2: The maximum number of electrons accommodated in the outermost valence shell is 8",
            "Bohr-Bury Rule 3: Step-wise shell filling: Electrons cannot occupy a new shell until inner shells are filled",
            "Electronic Configuration of First 10 Elements: Hydrogen (1) to Neon (2, 8)",
            "Electronic Configuration of Elements 11 to 20: Sodium (2, 8, 1) to Calcium (2, 8, 8, 2)",
            "Activity 8.2: Drawing geometric Bohr dot cross diagrams for elements 1 to 20"
        ],
        "key_concepts": [
            "2n^2 Capacity Rule: The maximum number of electrons present in an energy shell is given by the formula 2n^2, where n is the orbit number (K shell: 2(1)^2 = 2; L shell: 2(2)^2 = 8; M shell: 2(3)^2 = 18; N shell: 2(4)^2 = 32).",
            "Outermost Octet Rule: The maximum number of electrons that can be accommodated in the outermost shell of an atom is 8, even if that shell has capacity for more (e.g. M-shell holds max 8 until N-shell starts).",
            "Step-Wise Aufbau Invariant: Electrons do not enter an outer shell until the inner shells are completely filled (shells are filled in a step-wise manner).",
            "First 10 Elements Configurations: H (1), He (2), Li (2, 1), Be (2, 2), B (2, 3), C (2, 4), N (2, 5), O (2, 6), F (2, 7), Ne (2, 8).",
            "Elements 11 to 20 Configurations: Na (2, 8, 1), Mg (2, 8, 2), Al (2, 8, 3), Si (2, 8, 4), P (2, 8, 5), S (2, 8, 6), Cl (2, 8, 7), Ar (2, 8, 8), K (2, 8, 8, 1), Ca (2, 8, 8, 2).",
            "Noble Gas Duplet and Octet Stability: Helium possesses a stable duplet (2 electrons filling K shell); Neon and Argon possess stable octets (8 valence electrons), explaining their chemical inertness."
        ],
        "success_criteria": "Student can state the 3 Bohr-Bury rules, calculate 2n^2 capacities, write the electronic configuration for any element from Z = 1 to 20, and draw its Bohr orbit diagram.",
        "chapter_notes": """### 8.12 The Bohr-Bury Scheme (Rules for Electron Distribution)
The distribution of electrons into different orbits was suggested by Neils Bohr and Charles Bury:
1. **Rule 1 ($2n^2$ Maximum Capacity)**:
   - For **K-shell** ($n = 1$): Maximum electrons $= 2(1)^2 = \\mathbf{2}$.
   - For **L-shell** ($n = 2$): Maximum electrons $= 2(2)^2 = \\mathbf{8}$.
   - For **M-shell** ($n = 3$): Maximum electrons $= 2(3)^2 = \\mathbf{18}$.
   - For **N-shell** ($n = 4$): Maximum electrons $= 2(4)^2 = \\mathbf{32}$.
2. **Rule 2 (Outermost Octet Limit)**:
   - The **maximum number of electrons** that can be accommodated in the **outermost valence shell is 8**.
   - An outermost shell with 8 electrons is exceptionally stable (Noble gas configuration).
3. **Rule 3 (Step-Wise Filling)**:
   - Electrons are not accommodated in a given shell unless the inner shells are filled. That is, the shells are filled in a **step-wise manner**.

### 8.13 Complete Electronic Configuration Table (Elements 1 to 20)
| Element | Symbol | Atomic Number ($Z$) | Protons | Electrons | Distribution ($K, L, M, N$) | Valence Electrons |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Hydrogen | H | 1 | 1 | 1 | 1 | 1 |
| Helium | He | 2 | 2 | 2 | **2 (Duplet)** | 2 |
| Lithium | Li | 3 | 3 | 3 | 2, 1 | 1 |
| Beryllium | Be | 4 | 4 | 4 | 2, 2 | 2 |
| Boron | B | 5 | 5 | 5 | 2, 3 | 3 |
| Carbon | C | 6 | 6 | 6 | 2, 4 | 4 |
| Nitrogen | N | 7 | 7 | 7 | 2, 5 | 5 |
| Oxygen | O | 8 | 8 | 8 | 2, 6 | 6 |
| Fluorine | F | 9 | 9 | 9 | 2, 7 | 7 |
| Neon | Ne | 10 | 10 | 10 | **2, 8 (Octet)** | 8 |
| Sodium | Na | 11 | 11 | 11 | 2, 8, 1 | 1 |
| Magnesium | Mg | 12 | 12 | 12 | 2, 8, 2 | 2 |
| Aluminium | Al | 13 | 13 | 13 | 2, 8, 3 | 3 |
| Silicon | Si | 14 | 14 | 14 | 2, 8, 4 | 4 |
| Phosphorus | P | 15 | 15 | 15 | 2, 8, 5 | 5 |
| Sulphur | S | 16 | 16 | 16 | 2, 8, 6 | 6 |
| Chlorine | Cl | 17 | 17 | 17 | 2, 8, 7 | 7 |
| Argon | Ar | 18 | 18 | 18 | **2, 8, 8 (Octet)** | 8 |
| Potassium | K | 19 | 19 | 19 | 2, 8, 8, 1 | 1 |
| Calcium | Ca | 20 | 20 | 20 | 2, 8, 8, 2 | 2 |""",
        "worked_examples": [
            {
                "problem": "Write down the electronic configuration of: (a) Chlorine (Z = 17), (b) Magnesium (Z = 12), and (c) Potassium (Z = 19).",
                "given": "Atomic numbers: $Z_{Cl} = 17, Z_{Mg} = 12, Z_{K} = 19$.",
                "formula": "Bohr-Bury Shell Allocation ($2n^2$ rule and Octet limit).",
                "substitution": "Allocate electrons step-wise into K (max 2), L (max 8), M (max 8 before N fills), N.",
                "calculation": "1. **Chlorine ($Z = 17$)**: K takes 2, L takes 8, remaining 7 enter M -> **2, 8, 7**.\n2. **Magnesium ($Z = 12$)**: K takes 2, L takes 8, remaining 2 enter M -> **2, 8, 2**.\n3. **Potassium ($Z = 19$)**: K takes 2, L takes 8, M takes 8 (octet rule limit for outer shell). The 19th electron enters N shell -> **2, 8, 8, 1**.",
                "finalAnswer": "(a) Chlorine: 2, 8, 7; (b) Magnesium: 2, 8, 2; (c) Potassium: 2, 8, 8, 1.",
                "unit": "Configuration",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.11: Schematic atomic structure diagrams for Chlorine, Magnesium, and Potassium"
            },
            {
                "problem": "Why does potassium (Z = 19) have the electronic configuration 2, 8, 8, 1 rather than 2, 8, 9, even though the M-shell has capacity for 18 electrons?",
                "given": "Atomic number $Z = 19$ for Potassium.",
                "formula": "Bohr-Bury Rule 2: Outermost shell cannot hold more than 8 electrons.",
                "substitution": "If M shell held 9 electrons as the outermost shell, it would violate Rule 2.",
                "calculation": "1. By Bohr-Bury Rule 1, M-shell ($n=3$) has total capacity $2(3)^2 = 18$ electrons.\n2. However, by Bohr-Bury Rule 2, the **outermost valence shell can never accommodate more than 8 electrons**.\n3. If 9 electrons entered M, M would be the outermost shell with 9 electrons, which is forbidden.\n4. Therefore, M-shell fills with 8 electrons, and the 19th electron initiates the N-shell: **2, 8, 8, 1**.",
                "finalAnswer": "The outermost shell cannot hold more than 8 electrons (Rule 2); once M reaches 8, subsequent electrons enter the N-shell before M expands further.",
                "unit": "Bohr-Bury Invariant",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.12: Potassium 2, 8, 8, 1 electronic distribution diagram"
            },
            {
                "problem": "What is the maximum number of electrons that can be accommodated in the N-shell of an atom?",
                "given": "N-shell corresponds to principal quantum number $n = 4$.",
                "formula": "Maximum Capacity $= 2n^2$.",
                "substitution": "For $n = 4$: Capacity $= 2 \\times (4)^2 = 2 \\times 16$.",
                "calculation": "Capacity $= \\mathbf{32\\text{ electrons}}$.",
                "finalAnswer": "The maximum capacity of the N-shell is 32 electrons.",
                "unit": "Electrons",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.7: 2n^2 shell capacities: K=2, L=8, M=18, N=32"
            },
            {
                "problem": "If K and L shells of an atom are full, then what would be the total number of electrons in the atom? Identify the element.",
                "given": "K-shell is completely full; L-shell is completely full.",
                "formula": "Total Electrons $= \\text{Capacity}(K) + \\text{Capacity}(L) = 2(1)^2 + 2(2)^2$.",
                "substitution": "Total Electrons $= 2 + 8 = 10$.",
                "calculation": "1. Total electrons $= 10$.\n2. In a neutral atom, number of protons $= \\text{number of electrons} = 10$.\n3. Element with atomic number $Z = 10$ is **Neon (Ne)**, an inert noble gas.",
                "finalAnswer": "Total electrons = 10; The element is Neon (Ne).",
                "unit": "NCERT In-Text Problem",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.11: Neon atomic configuration with full K and L shells"
            },
            {
                "problem": "An atom has 2 electrons in its outermost shell (valence shell). Can it be Helium or Calcium? Differentiate their electronic structures.",
                "given": "Two valence electrons in outermost shell.",
                "formula": "Duplet vs Valence Octet Structure",
                "substitution": "Helium has only 1 shell (K); Calcium has 4 shells (K, L, M, N).",
                "calculation": "1. **Helium ($Z = 2$)**: Has only one shell, K-shell, containing 2 electrons. Because K-shell is completely filled ($2n^2 = 2$), Helium possesses a stable duplet and is an unreactive noble gas.\n2. **Calcium ($Z = 20$)**: Has configuration 2, 8, 8, 2. Its 2 outermost electrons reside in the N-shell. It is a highly reactive alkaline earth metal that readily donates these 2 electrons to achieve an octet.",
                "finalAnswer": "It can be both: Helium (2 in K-shell, inert noble gas) or Calcium (2 in N-shell, reactive metal with 2, 8, 8, 2).",
                "unit": "Electronic Architecture",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.11: Helium duplet vs Calcium valence electron shell"
            },
            {
                "problem": "Write the electronic configuration of Silicon (Z = 14) and Phosphorus (Z = 15). State their valence electrons.",
                "given": "Silicon $Z = 14$, Phosphorus $Z = 15$.",
                "formula": "Step-wise shell filling: K (max 2), L (max 8), M (balance).",
                "substitution": "Silicon: 14 = 2 + 8 + 4. Phosphorus: 15 = 2 + 8 + 5.",
                "calculation": "1. Silicon: K=2, L=8, M=4 -> **2, 8, 4**. Valence electrons $= \\mathbf{4}$.\n2. Phosphorus: K=2, L=8, M=5 -> **2, 8, 5**. Valence electrons $= \\mathbf{5}$.",
                "finalAnswer": "Silicon: 2, 8, 4 (4 valence electrons); Phosphorus: 2, 8, 5 (5 valence electrons).",
                "unit": "Configuration",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.11: Geometric electron distribution in Silicon and Phosphorus"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "The third shell (M) can only hold 8 electrons.",
                "correction": "The total capacity of M is 2(3)^2 = 18 electrons! It temporarily stops filling at 8 only when it is the outermost shell to satisfy Rule 2; once the 4th shell (N) receives 2 electrons, the M-shell resumes filling up to 18 (in transition metals Scandium to Zinc).",
                "why_it_matters": "Distinguishes superficial rote learning from true chemical understanding."
            }
        ],
        "visual_lesson_plan": {
            "title": "Bohr-Bury Electron Distribution Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "2n^2 Capacity Rule: The maximum number of electrons present in an energy shell is given by the formula 2n^2, where n is the orbit number (K shell: 2(1)^2 = 2; L shell: 2(2)^2 = 8; M shell: 2(3)^2 = 18; N shell: 2(4)^2 = 32).",
                    "diagram_title": "2n^2 Shell Capacity Formula Architecture",
                    "diagram_type": "image",
                    "image_query": "bohr bury rules 2n squared formula shell capacity diagram",
                    "video_query": "bohr bury rules electron distribution",
                    "image_url": "/extracted_diagrams/ch8/fig_8_7.webp",
                    "what_to_make": "Textbook diagram showing mathematical 2n^2 derivation for shells K, L, M, N.",
                    "timing_and_cue": "Mount 2n^2 rule on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_7.webp | 2n^2 Capacity Rule | K=2, L=8, M=18, N=32 maximum capacities\")"
                },
                {
                    "concept_title": "Outermost Octet Rule: The maximum number of electrons that can be accommodated in the outermost shell of an atom is 8, even if that shell has capacity for more (e.g. M-shell holds max 8 until N-shell starts).",
                    "diagram_title": "Outermost Valence Shell Octet Constraint",
                    "diagram_type": "image",
                    "image_query": "outermost shell max 8 electrons octet rule bohr bury diagram",
                    "video_query": "octet rule outermost shell",
                    "image_url": "/extracted_diagrams/ch8/fig_8_11.webp",
                    "what_to_make": "Textbook diagram showing 8-electron limit on outermost valence shells.",
                    "timing_and_cue": "Mount octet limit on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_11.webp | Outermost Octet Limit | Valence shell cannot hold more than 8 electrons\")"
                },
                {
                    "concept_title": "Step-Wise Aufbau Invariant: Electrons do not enter an outer shell until the inner shells are completely filled (shells are filled in a step-wise manner).",
                    "diagram_title": "Step-Wise Shell Filling Sequence",
                    "diagram_type": "image",
                    "image_query": "step wise filling of shells electron configuration diagram",
                    "video_query": "how electron shells fill step by step",
                    "image_url": "/extracted_diagrams/ch8/fig_8_12.webp",
                    "what_to_make": "Textbook schematic showing sequential filling from inner K to outer N shells.",
                    "timing_and_cue": "Mount step-wise filling on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_12.webp | Step-Wise Filling | Inner shells must fill before outer shells receive electrons\")"
                },
                {
                    "concept_title": "First 10 Elements Configurations: H (1), He (2), Li (2, 1), Be (2, 2), B (2, 3), C (2, 4), N (2, 5), O (2, 6), F (2, 7), Ne (2, 8).",
                    "diagram_title": "Bohr Dot Models Elements 1 to 10",
                    "diagram_type": "image",
                    "image_query": "atomic structure of first 18 elements ncert textbook diagram",
                    "video_query": "first 18 elements electronic configuration",
                    "image_url": "/extracted_diagrams/ch8/fig_8_11.webp",
                    "what_to_make": "Textbook master diagram displaying Bohr dot models of Hydrogen through Neon.",
                    "timing_and_cue": "Mount elements 1-10 on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_11.webp | Elements 1 to 10 Models | Concentric Bohr electron dot diagrams\")"
                },
                {
                    "concept_title": "Elements 11 to 20 Configurations: Na (2, 8, 1), Mg (2, 8, 2), Al (2, 8, 3), Si (2, 8, 4), P (2, 8, 5), S (2, 8, 6), Cl (2, 8, 7), Ar (2, 8, 8), K (2, 8, 8, 1), Ca (2, 8, 8, 2).",
                    "diagram_title": "Bohr Dot Models Elements 11 to 20",
                    "diagram_type": "image",
                    "image_query": "bohr models sodium to calcium electronic configuration diagram",
                    "video_query": "electronic configuration 11 to 20 elements",
                    "image_url": "/extracted_diagrams/ch8/fig_8_13.webp",
                    "what_to_make": "Textbook master diagram displaying Bohr dot models of Sodium through Calcium.",
                    "timing_and_cue": "Mount elements 11-20 on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_13.webp | Elements 11 to 20 Models | Sodium to Calcium configurations\")"
                },
                {
                    "concept_title": "Noble Gas Duplet and Octet Stability: Helium possesses a stable duplet (2 electrons filling K shell); Neon and Argon possess stable octets (8 valence electrons), explaining their chemical inertness.",
                    "diagram_title": "Noble Gas Duplet and Octet Invariance",
                    "diagram_type": "image",
                    "image_query": "noble gases helium neon argon stable octet duplet diagram",
                    "video_query": "why noble gases are inert octet rule",
                    "image_url": "/extracted_diagrams/ch8/fig_8_14.webp",
                    "what_to_make": "Textbook diagram showing complete outer shells of Helium (2), Neon (8), and Argon (8).",
                    "timing_and_cue": "Mount noble gas stability on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_14.webp | Noble Gas Stability | Duplet (He) and Octets (Ne, Ar) driving chemical inertness\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "Why does Potassium (Z=19) have configuration 2, 8, 8, 1 instead of 2, 8, 9 when the M-shell can hold 18 electrons?"
   - Rules: 2n^2 and outermost 8-electron limit on the board.
   - Socratic check: "How many electrons can the L-shell hold, and what element has both K and L completely full?" HARD STOP: Wait for student answer!"""
    }

    # Module 5: Valency & Chemical Reactivity
    m5 = {
        "order_index": 5,
        "title": "Valency Mechanics, Valence Electrons & Noble Gas Octet Stability",
        "description": "Formulate valency as the combining capacity of atoms, distinguish valence electrons from valency, understand metallic electron loss vs non-metallic electron gain/sharing to achieve octet stability, and calculate valency across elements 1 to 20.",
        "subtopics": [
            "Valence Electrons: Electrons situated in the outermost energy shell of an atom",
            "The Octet Rule: Atoms react to achieve stable 8-electron outermost configurations (like noble gases)",
            "Valency of Metals (Electropositive): Equal to the number of valence electrons (Valency = V)",
            "Valency of Non-Metals (Electronegative): Equal to 8 minus valence electrons (Valency = 8 - V)",
            "Variable Valency: Elements with multiple combining capacities (Iron Fe2+/Fe3+, Copper Cu+/Cu2+)",
            "Valency Table Construction: Determining valencies of H, C, O, N, Na, Mg, Al, Cl, Ne, Ar"
        ],
        "key_concepts": [
            "Valence Electrons Definition: The electrons present in the outermost shell of an atom are called valence electrons. They dictate all chemical bonding and reactivity.",
            "Valency Definition: The combining capacity of an atom of an element to achieve a completely filled outermost shell (octet or duplet) is called its valency.",
            "Metal Valency Formula: For atoms with 1, 2, or 3 valence electrons (metals), atoms readily lose these electrons: Valency = Number of valence electrons (Na: 1, Mg: 2, Al: 3).",
            "Non-Metal Valency Formula: For atoms with 4, 5, 6, or 7 valence electrons (non-metals), it is energetically easier to gain or share electrons: Valency = 8 - Number of valence electrons (N: 8 - 5 = 3, O: 8 - 6 = 2, F: 8 - 7 = 1).",
            "Zero Valency of Noble Gases: Noble gases (He, Ne, Ar) have completely filled outermost shells (2 in He, 8 in Ne/Ar), meaning their combining capacity is zero (Valency = 0).",
            "Tetravalency of Carbon: Carbon has 4 valence electrons and shares 4 electrons with other atoms, exhibiting tetravalency (Valency = 4)."
        ],
        "success_criteria": "Student can deduce valence electrons from configuration, calculate valency using V or 8-V, explain noble gas zero valency, and predict chemical bonding behavior.",
        "chapter_notes": """### 8.14 Valence Electrons
The electrons present in the **outermost shell** of an atom are known as **valence electrons**.
- Sodium ($2, 8, 1$) has **1 valence electron**.
- Oxygen ($2, 6$) has **6 valence electrons**.
- Argon ($2, 8, 8$) has **8 valence electrons**.

### 8.15 Valency (Combining Capacity)
An atom of each element has a definite **combining capacity**, called its **valency**.
- **The Octet Rule**: Atoms combine with other atoms by sharing, gaining, or losing electrons in order to attain a stable outer shell of **8 electrons** (octet), identical to the nearest noble gas.
- **Helium Exception (Duplet)**: Hydrogen, Lithium, and Beryllium achieve stability by attaining 2 electrons in the K-shell (duplet of Helium).

### 8.16 How to Determine Valency
1. **Case 1: When Valence Electrons $\\le 4$ (Usually Metals)**:
   $$\\mathbf{\\text{Valency} = \\text{Number of Valence Electrons}}$$
   - Sodium ($2, 8, 1$) loses $1 e^- \\implies \\mathbf{\\text{Valency} = 1}$.
   - Magnesium ($2, 8, 2$) loses $2 e^- \\implies \\mathbf{\\text{Valency} = 2}$.
   - Aluminium ($2, 8, 3$) loses $3 e^- \\implies \\mathbf{\\text{Valency} = 3}$.
2. **Case 2: When Valence Electrons $> 4$ (Non-Metals)**:
   $$\\mathbf{\\text{Valency} = 8 - \\text{Number of Valence Electrons}}$$
   - Nitrogen ($2, 5$) gains/shares $3 e^- \\implies \\text{Valency} = 8 - 5 = \\mathbf{3}$.
   - Oxygen ($2, 6$) gains/shares $2 e^- \\implies \\text{Valency} = 8 - 6 = \\mathbf{2}$.
   - Fluorine ($2, 7$) gains $1 e^- \\implies \\text{Valency} = 8 - 7 = \\mathbf{1}$.
3. **Case 3: Noble Gases (Zero Valency)**:
   - Neon ($2, 8$) and Argon ($2, 8, 8$) have full octets $\\implies \\text{Valency} = 8 - 8 = \\mathbf{0}$.""",
        "worked_examples": [
            {
                "problem": "How will you find the valency of chlorine, sulphur and magnesium?",
                "given": "Atomic numbers: $Z_{Cl} = 17, Z_S = 16, Z_{Mg} = 12$.",
                "formula": "If valence electrons $V \\le 4$, Valency $= V$. If $V > 4$, Valency $= 8 - V$.",
                "substitution": "Cl: 2, 8, 7 ($V=7$). S: 2, 8, 6 ($V=6$). Mg: 2, 8, 2 ($V=2$).",
                "calculation": "1. **Magnesium**: Has 2 valence electrons ($V=2 \\le 4$). Easily loses 2 electrons to form $Mg^{2+}$. $\\mathbf{\\text{Valency} = 2}$.\n2. **Sulphur**: Has 6 valence electrons ($V=6 > 4$). Needs 2 electrons to complete octet: $\\text{Valency} = 8 - 6 = \\mathbf{2}$.\n3. **Chlorine**: Has 7 valence electrons ($V=7 > 4$). Needs 1 electron to complete octet: $\\text{Valency} = 8 - 7 = \\mathbf{1}$.",
                "finalAnswer": "Valency of Magnesium = 2; Sulphur = 2; Chlorine = 1.",
                "unit": "NCERT In-Text Problem",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.11: Valence shell electron configurations for Mg, S, and Cl"
            },
            {
                "problem": "Why do inert noble gases like Helium, Neon, and Argon have zero valency?",
                "given": "Helium (2), Neon (2, 8), Argon (2, 8, 8).",
                "formula": "Octet / Duplet Saturation Axiom",
                "substitution": "Outermost shells are completely full.",
                "calculation": "1. Valency represents the number of electrons an atom must gain, lose, or share to attain an octet.\n2. Helium has a completely full K-shell (duplet: 2 electrons).\n3. Neon and Argon have completely full outermost shells with 8 electrons (octet).\n4. Because their shells are completely saturated, they have no tendency to lose, gain, or share electrons.\n5. Therefore, their combining capacity is identically **zero**.",
                "finalAnswer": "Noble gases have completely filled outermost shells (duplet in He, octet in Ne and Ar), so their combining capacity is zero.",
                "unit": "Chemical Inertness",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.14: Completely filled valence octets of noble gases"
            },
            {
                "problem": "Differentiate clearly between 'Valence Electrons' and 'Valency' using Nitrogen (Z = 7) and Aluminium (Z = 13) as examples.",
                "given": "Nitrogen $Z = 7$ (2, 5); Aluminium $Z = 13$ (2, 8, 3).",
                "formula": "Valence Electrons = Outermost Shell Count; Valency = Combining Capacity.",
                "substitution": "Compare outermost count with chemical combining power.",
                "calculation": "1. **Nitrogen ($2, 5$)**:\n   - Valence Electrons $= \\mathbf{5}$ (total electrons in L shell).\n   - Valency $= 8 - 5 = \\mathbf{3}$ (needs 3 electrons to form $NH_3$).\n2. **Aluminium ($2, 8, 3$)**:\n   - Valence Electrons $= \\mathbf{3}$ (total electrons in M shell).\n   - Valency $= \\mathbf{3}$ (loses 3 electrons to form $Al^{3+}$).\n3. *Summary*: Valence electrons is the physical count of outer electrons; valency is the chemical combining power.",
                "finalAnswer": "Valence electrons is the actual number of electrons in the outer shell; valency is the combining capacity (N has 5 valence electrons but valency 3; Al has 3 valence electrons and valency 3).",
                "unit": "Chemical Concept",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.11: Nitrogen and Aluminium valence shell comparison"
            },
            {
                "problem": "Explain why the valency of Oxygen is 2, while the valency of Carbon is 4.",
                "given": "Oxygen $Z = 8$ (2, 6); Carbon $Z = 6$ (2, 4).",
                "formula": "Octet Completion Criterion",
                "substitution": "Oxygen needs 2 electrons; Carbon shares 4 electrons.",
                "calculation": "1. Oxygen has 6 valence electrons. It readily gains or shares 2 electrons with other atoms to achieve the stable Neon octet ($2, 8$). Hence, its valency is $8 - 6 = \\mathbf{2}$.\n2. Carbon has 4 valence electrons. Losing 4 electrons ($C^{4+}$) or gaining 4 electrons ($C^{4-}$) is energetically impossible due to electrostatic nuclear constraints. Hence, it shares 4 electrons with 4 other hydrogen/carbon atoms, exhibiting tetravalency: $\\mathbf{\\text{Valency} = 4}$.",
                "finalAnswer": "Oxygen gains 2 electrons to complete its octet (valency = 2); Carbon shares 4 electrons (valency = 4).",
                "unit": "Valency Mechanics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.11: Octet completion in Oxygen (valency 2) and Carbon (valency 4)"
            },
            {
                "problem": "An element X has an atomic number of 15. Determine: (a) Electronic configuration, (b) Number of valence electrons, (c) Valency, and (d) Formula of its compound with hydrogen.",
                "given": "Atomic number $Z = 15$ for element X (Phosphorus).",
                "formula": "Config: 2, 8, 5; Valency $= 8 - 5 = 3$; Criss-cross formula with $H$ (valency 1).",
                "substitution": "$X$ has valency 3; $H$ has valency 1.",
                "calculation": "1. (a) Electronic configuration: **2, 8, 5**.\n2. (b) Valence electrons: **5**.\n3. (c) Valency: $8 - 5 = \\mathbf{3}$ (also exhibits valency 5 in $PCl_5$).\n4. (d) Compound with hydrogen: $X_1 H_3 \\implies \\mathbf{XH_3}$ (Phosphine, $PH_3$).",
                "finalAnswer": "(a) 2, 8, 5; (b) 5 valence electrons; (c) Valency = 3; (d) Formula = XH3.",
                "unit": "Stoichiometric Prediction",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.11: Phosphorus electron distribution and bonding capacity"
            },
            {
                "problem": "Can an element have more than 4 as its valency? Explain using Phosphorus and Sulfur as examples.",
                "given": "Phosphorus ($Z = 15$) and Sulfur ($Z = 16$).",
                "formula": "Valence Shell Expansion & Variable Valency",
                "substitution": "Presence of vacant d-orbitals in 3rd shell (M-shell).",
                "calculation": "1. For Class 9 basics, valency is typically calculated as $8 - V$, giving 3 for P and 2 for S.\n2. However, elements in the 3rd period possess an M-shell with capacity for 18 electrons (including vacant 3d orbitals).\n3. Phosphorus can unpair its electrons to share all 5 valence electrons (e.g. in $PCl_5$, valency is **5**).\n4. Sulfur can share 4 electrons ($SF_4$) or all 6 valence electrons ($SF_6$, valency is **6**).\n5. Hence, elements can exhibit variable valencies exceeding 4.",
                "finalAnswer": "Yes, elements with M-shells like Phosphorus (valency 3 and 5) and Sulfur (valency 2, 4, 6) can exhibit valencies greater than 4.",
                "unit": "Advanced Chemical Bonding",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.11: Variable valency and expanded octets in PCl5 and SF6"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Valence electrons and valency are always the same number.",
                "correction": "They are the same ONLY for elements with 1 to 4 valence electrons (like Na=1, Mg=2, Al=3, C=4). For elements with 5 to 7 valence electrons, valency is 8 MINUS valence electrons (like Nitrogen has 5 valence electrons, but valency 3!).",
                "why_it_matters": "Universal student error in Class 9 chemistry exams."
            }
        ],
        "visual_lesson_plan": {
            "title": "Valency Mechanics & Octet Stability Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Valence Electrons Definition: The electrons present in the outermost shell of an atom are called valence electrons. They dictate all chemical bonding and reactivity.",
                    "diagram_title": "Valence Shell Electron Identification",
                    "diagram_type": "image",
                    "image_query": "valence electrons outermost shell chemistry diagram",
                    "video_query": "what are valence electrons chemistry",
                    "image_url": "/extracted_diagrams/ch8/fig_8_11.webp",
                    "what_to_make": "Textbook diagram highlighting outermost valence electrons in Na, Mg, Al, and Cl.",
                    "timing_and_cue": "Mount valence electrons on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_11.webp | Valence Electrons | Outermost electrons governing chemical bonding\")"
                },
                {
                    "concept_title": "Valency Definition: The combining capacity of an atom of an element to achieve a completely filled outermost shell (octet or duplet) is called its valency.",
                    "diagram_title": "Combining Capacity Valency Scheme",
                    "diagram_type": "image",
                    "image_query": "valency combining capacity octet duplet diagram",
                    "video_query": "how to find valency of an element",
                    "image_url": "/extracted_diagrams/ch8/fig_8_12.webp",
                    "what_to_make": "Textbook diagram showing valency formulas V and 8-V.",
                    "timing_and_cue": "Mount valency definition on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_12.webp | Valency Formulation | Combining capacity: V for metals, 8-V for non-metals\")"
                },
                {
                    "concept_title": "Metal Valency Formula: For atoms with 1, 2, or 3 valence electrons (metals), atoms readily lose these electrons: Valency = Number of valence electrons (Na: 1, Mg: 2, Al: 3).",
                    "diagram_title": "Electropositive Metal Electron Loss",
                    "diagram_type": "image",
                    "image_query": "metal electron loss positive cation formation diagram",
                    "video_query": "why metals lose electrons cation",
                    "image_url": "/extracted_diagrams/ch8/fig_8_13.webp",
                    "what_to_make": "Textbook diagram showing Na losing 1e- to form Na+ and Mg losing 2e- to form Mg2+.",
                    "timing_and_cue": "Mount metal valency on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_13.webp | Metallic Cation Formation | Losing 1, 2, or 3 valence electrons to achieve stable octet\")"
                },
                {
                    "concept_title": "Non-Metal Valency Formula: For atoms with 4, 5, 6, or 7 valence electrons (non-metals), it is energetically easier to gain or share electrons: Valency = 8 - Number of valence electrons (N: 8 - 5 = 3, O: 8 - 6 = 2, F: 8 - 7 = 1).",
                    "diagram_title": "Electronegative Non-Metal Octet Gain",
                    "diagram_type": "image",
                    "image_query": "non metal electron gain negative anion formation diagram",
                    "video_query": "why non metals gain electrons anion",
                    "image_url": "/extracted_diagrams/ch8/fig_8_14.webp",
                    "what_to_make": "Textbook diagram showing Cl gaining 1e- to form Cl- and O gaining 2e- to form O2-.",
                    "timing_and_cue": "Mount non-metal valency on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_14.webp | Non-Metallic Anion Formation | Gaining 8 - V electrons to complete octet\")"
                },
                {
                    "concept_title": "Zero Valency of Noble Gases: Noble gases (He, Ne, Ar) have completely filled outermost shells (2 in He, 8 in Ne/Ar), meaning their combining capacity is zero (Valency = 0).",
                    "diagram_title": "Noble Gas Zero Valency Architecture",
                    "diagram_type": "image",
                    "image_query": "noble gas zero valency inert electron shell diagram",
                    "video_query": "noble gases zero valency explained",
                    "image_url": "/extracted_diagrams/ch8/fig_8_14.webp",
                    "what_to_make": "Textbook diagram illustrating zero combining capacity of full shell noble gases.",
                    "timing_and_cue": "Mount zero valency on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_14.webp | Zero Valency Invariant | Fully saturated outer shell gives zero combining capacity\")"
                },
                {
                    "concept_title": "Tetravalency of Carbon: Carbon has 4 valence electrons and shares 4 electrons with other atoms, exhibiting tetravalency (Valency = 4).",
                    "diagram_title": "Tetravalent Carbon Covalent Sharing",
                    "diagram_type": "image",
                    "image_query": "carbon tetravalency covalent bonding methane diagram",
                    "video_query": "tetravalency of carbon explained",
                    "image_url": "/extracted_diagrams/ch8/fig_8_11.webp",
                    "what_to_make": "Textbook diagram showing carbon sharing 4 electrons with 4 hydrogen atoms in methane.",
                    "timing_and_cue": "Mount carbon tetravalency on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_11.webp | Carbon Tetravalency | Sharing 4 valence electrons to satisfy octet\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "Nitrogen has 5 valence electrons. Why is its valency NOT 5, but 3?"
   - Formulation: V vs 8-V rule on the chalkboard.
   - Socratic check: "What is the valency of an element with atomic number 16 (Sulfur)?" HARD STOP: Wait for student answer!"""
    }

    # Module 6: Atomic Identifiers, Isotopes, Isobars & Master NCERT Solver
    m6 = {
        "order_index": 6,
        "title": "Atomic Identifiers: Atomic Number (Z), Mass Number (A), Isotopes & Isobars",
        "description": "Master atomic notation (A_Z X), define Atomic Number (Z) and Mass Number (A), explore isotopes, fractional atomic masses, radioactive isotope applications in oncology and nuclear power, and solve complete NCERT Chapter 8 exercises.",
        "subtopics": [
            "Atomic Number (Z): Total number of protons in the nucleus of an atom",
            "Mass Number (A): Total number of nucleons (protons + neutrons): A = Z + N",
            "Standard Nuclear Notation: ^A_Z X (e.g. ^12_6 C, ^14_6 C, ^35_17 Cl)",
            "Isotopes Definition: Atoms of same element having same Z but different A (Protium, Deuterium, Tritium)",
            "Fractional Atomic Mass Calculation: Weighted average of isotopic abundances (Chlorine 35.5 u)",
            "Isobars Definition: Atoms of different elements having same Mass Number A but different Atomic Number Z (Argon-40 and Calcium-40)",
            "Applications of Radioisotopes: Cobalt-60 (cancer therapy), Iodine-131 (goitre), Uranium-235 (nuclear reactors)",
            "Complete NCERT Chapter 8 Exercise Ledger Solutions (Q1 to Q19)"
        ],
        "key_concepts": [
            "Atomic Number (Z): The total number of protons present in the nucleus of an atom is defined as its atomic number (Z). It identifies the chemical identity of the element.",
            "Mass Number (A): The total number of protons and neutrons (collectively termed nucleons) present in the nucleus: A = Protons (Z) + Neutrons (N).",
            "Isotopes Invariant: Isotopes are defined as atoms of the SAME element having the same atomic number (Z) but different mass numbers (A), possessing identical chemical properties but different physical masses.",
            "Fractional Atomic Masses: The mass of an element is the weighted average mass of its naturally occurring isotopes based on their percentage abundance: Cl = (35 * 75% + 37 * 25%) = 35.5 u.",
            "Isobars Invariant: Isobars are defined as atoms of DIFFERENT elements having the same mass number (A) but different atomic numbers (Z), such as Calcium-40 (Z=20) and Argon-40 (Z=18).",
            "Medical & Industrial Radioisotopes: Uranium-235 is used as nuclear fuel; Cobalt-60 is used in the treatment of cancer; Iodine-131 is used in the treatment of goitre."
        ],
        "success_criteria": "Student can calculate neutrons from A - Z, calculate fractional atomic masses from percentage abundances, distinguish isotopes from isobars, and solve every NCERT Chapter 8 problem.",
        "chapter_notes": """### 8.17 Atomic Number ($Z$)
The atomic number of an element is the total number of **protons** present in the nucleus of its atom:
$$\\mathbf{Z = \\text{Number of Protons} = p^+}$$
In a neutral atom: $\\text{Number of protons} = \\text{Number of electrons} = Z$.

### 8.18 Mass Number ($A$)
Protons and neutrons reside in the nucleus and are collectively termed **nucleons**. The mass number ($A$) is the total sum of nucleons:
$$\\mathbf{A = Z + N = \\text{Protons} + \\text{Neutrons}}$$
- **Calculating Neutrons**:
  $$\\mathbf{N = A - Z}$$

### 8.19 Standard Atomic Notation
$$^{A}_{Z}\\text{X} \\quad \\text{e.g.} \\quad ^{12}_{6}\\text{C}, \\quad ^{14}_{7}\\text{N}, \\quad ^{35}_{17}\\text{Cl}, \\quad ^{40}_{20}\\text{Ca}$$

### 8.20 Isotopes
**Isotopes** are atoms of the **same element** having the **same atomic number ($Z$)** but **different mass numbers ($A$)** due to different numbers of neutrons.
1. **Isotopes of Hydrogen**:
   - **Protium** ($^1_1H$): 1 proton, 0 neutrons, 1 electron.
   - **Deuterium** ($^2_1H$ or $D$): 1 proton, 1 neutron, 1 electron (heavy water $D_2O$).
   - **Tritium** ($^3_1H$ or $T$): 1 proton, 2 neutrons, 1 electron (radioactive).
2. **Isotopes of Carbon**: $^{12}_6C$ and $^{14}_6C$ (used in radiocarbon dating).
3. **Isotopes of Chlorine**: $^{35}_{17}Cl$ (75%) and $^{37}_{17}Cl$ (25%).

### 8.21 Fractional Atomic Mass Calculation
Atomic mass of Chlorine:
$$\\text{Average Atomic Mass} = \\left(35 \\times \\frac{75}{100}\\right) + \\left(37 \\times \\frac{25}{100}\\right) = \\frac{105}{4} + \\frac{37}{4} = \\frac{142}{4} = \\mathbf{35.5\\text{ u}}$$

### 8.22 Isobars
**Isobars** are atoms of **different elements** having the **same mass number ($A$)** but **different atomic numbers ($Z$)**:
- **Calcium** ($^{40}_{20}Ca$): $Z = 20, p = 20, n = 20, A = 40$.
- **Argon** ($^{40}_{18}Ar$): $Z = 18, p = 18, n = 22, A = 40$.
They have completely different chemical properties because their electron configurations differ, but identical total nucleons.

### 8.23 Applications of Radioisotopes
1. **Nuclear Energy**: An isotope of Uranium ($^{235}_{92}U$) is used as fuel in nuclear reactors.
2. **Cancer Radiotherapy**: An isotope of Cobalt ($^{60}_{27}Co$) emits gamma rays used in the treatment of cancer.
3. **Endocrinology**: An isotope of Iodine ($^{131}_{53}I$) is used in the diagnosis and treatment of goitre.""",
        "worked_examples": [
            {
                "problem": "Calculate the number of protons, neutrons, and electrons in: (a) 35_17 Cl, (b) 23_11 Na, and (c) 40_20 Ca.",
                "given": "Nuclear notations: $^{35}_{17}Cl, ^{23}_{11}Na, ^{40}_{20}Ca$.",
                "formula": "Protons $p = Z$; Electrons $e = Z$; Neutrons $n = A - Z$.",
                "substitution": "Cl: Z=17, A=35. Na: Z=11, A=23. Ca: Z=20, A=40.",
                "calculation": "1. **Chlorine ($^{35}_{17}Cl$)**: $p = 17, e = 17, n = 35 - 17 = \\mathbf{18}$.\n2. **Sodium ($^{23}_{11}Na$)**: $p = 11, e = 11, n = 23 - 11 = \\mathbf{12}$.\n3. **Calcium ($^{40}_{20}Ca$)**: $p = 20, e = 20, n = 40 - 20 = \\mathbf{20}$.",
                "finalAnswer": "(a) Cl: 17p, 17e, 18n; (b) Na: 11p, 11e, 12n; (c) Ca: 20p, 20e, 20n.",
                "unit": "Nucleon Ledger",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.11: Atomic number, mass number, and nucleon composition ledger"
            },
            {
                "problem": "Chlorine occurs in nature in two isotopic forms with masses 35 u and 37 u in the ratio of 3:1 (75% and 25%). Calculate the average atomic mass of chlorine.",
                "given": "Isotope 1: mass $= 35\\text{ u}$, abundance $= 75\\% = \\frac{3}{4}$. Isotope 2: mass $= 37\\text{ u}$, abundance $= 25\\% = \\frac{1}{4}$.",
                "formula": "$\\text{Average Mass} = (M_1 \\times \\%_1) + (M_2 \\times \\%_2)$.",
                "substitution": "$\\text{Average Mass} = \\left(35 \\times \\frac{75}{100}\\right) + \\left(37 \\times \\frac{25}{100}\\right) = \\frac{105}{4} + \\frac{37}{4}$.",
                "calculation": "$\\text{Average Mass} = \\frac{142}{4} = \\mathbf{35.5\\text{ u}}$.",
                "finalAnswer": "Average atomic mass of chlorine = 35.5 u.",
                "unit": "u",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.12: Weighted average calculation of fractional atomic mass of Chlorine"
            },
            {
                "problem": "The average atomic mass of a sample of an element X is 16.2 u. What are the percentages of isotopes 16_8 X and 18_8 X in the sample?",
                "given": "Average mass $= 16.2\\text{ u}$. Isotope masses: $M_1 = 16\\text{ u}, M_2 = 18\\text{ u}$.",
                "formula": "Let percentage of $^{16}X$ be $y\\%$. Then percentage of $^{18}X$ is $(100 - y)\\%$. $\\text{Average Mass} = 16\\left(\\frac{y}{100}\\right) + 18\\left(\\frac{100 - y}{100}\\right)$.",
                "substitution": "$16.2 = \\frac{16y + 1800 - 18y}{100} \\implies 1620 = 1800 - 2y$.",
                "calculation": "$2y = 1800 - 1620 = 180 \\implies y = 90\\%$. Percentage of $^{18}X = 100 - 90 = 10\\%$.",
                "finalAnswer": "Abundance of 16_8 X = 90%; Abundance of 18_8 X = 10%.",
                "unit": "%",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.13: Isotopic abundance determination from fractional atomic mass"
            },
            {
                "problem": "Differentiate between Isotopes and Isobars with two examples of each.",
                "given": "Comparative nuclear taxonomy.",
                "formula": "Isotopes: Same Z, Different A; Isobars: Different Z, Same A.",
                "substitution": "Correlate nuclear composition with physical and chemical properties.",
                "calculation": "1. **Isotopes**:\n   - Same element, same atomic number ($Z$), different mass number ($A$).\n   - Identical chemical properties (same electron configuration).\n   - Examples: $^{12}_6C$ and $^{14}_6C$; $^{35}_{17}Cl$ and $^{37}_{17}Cl$.\n2. **Isobars**:\n   - Different elements, different atomic number ($Z$), same mass number ($A$).\n   - Completely different chemical properties (different electron configurations).\n   - Examples: $^{40}_{18}Ar$ and $^{40}_{20}Ca$; $^{14}_6C$ and $^{14}_7N$.",
                "finalAnswer": "Isotopes have same Z and different A (chemically identical); Isobars have different Z and same A (chemically different).",
                "unit": "Taxonomy",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.8: Isotopes (same Z) vs Isobars (same A) comparison diagram"
            },
            {
                "problem": "State three practical industrial or medical applications of radioactive isotopes.",
                "given": "Applied radioisotope nuclear technology.",
                "formula": "Radioactive Decay & Radiotherapy Principles",
                "substitution": "Specific isotopes mapped to medical/industrial applications.",
                "calculation": "1. **Cobalt-60 ($^{60}_{27}Co$)**: Emits high-energy penetrating gamma rays used in oncology radiotherapy to destroy malignant cancerous tumors.\n2. **Uranium-235 ($^{235}_{92}U$)**: Undergoes controlled nuclear fission, used as a nuclear fuel in nuclear power plants to generate electricity.\n3. **Iodine-131 ($^{131}_{53}I$)**: Selectively accumulates in the thyroid gland, used in the diagnosis and clinical treatment of thyroid cancer and goitre.",
                "finalAnswer": "(1) Cobalt-60 for cancer therapy, (2) Uranium-235 for nuclear power generation, (3) Iodine-131 for thyroid goitre treatment.",
                "unit": "Nuclear Applications",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 8.8: Bhabha Atomic Research Centre and applications of radioisotopes"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "An atom of chlorine has a fractional nucleus with 35.5 nucleons.",
                "correction": "No individual atom ever has half a proton or half a neutron! Any single chlorine atom has either 35 nucleons (18 neutrons) or 37 nucleons (20 neutrons). 35.5 u is merely the statistical weighted average of billions of atoms in a bulk sample.",
                "why_it_matters": "Fundamental understanding of statistical atomic masses."
            }
        ],
        "visual_lesson_plan": {
            "title": "Atomic Identifiers, Isotopes & Isobars Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Atomic Number (Z): The total number of protons present in the nucleus of an atom is defined as its atomic number (Z). It identifies the chemical identity of the element.",
                    "diagram_title": "Atomic Number and Nuclear Protons",
                    "diagram_type": "image",
                    "image_query": "atomic number Z number of protons periodic table diagram",
                    "video_query": "what is atomic number chemistry",
                    "image_url": "/extracted_diagrams/ch8/fig_8_11.webp",
                    "what_to_make": "Textbook diagram showing Z = number of protons in nucleus.",
                    "timing_and_cue": "Mount atomic number on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_11.webp | Atomic Number (Z) | Total protons in nucleus determining chemical identity\")"
                },
                {
                    "concept_title": "Mass Number (A): The total number of protons and neutrons (collectively termed nucleons) present in the nucleus: A = Protons (Z) + Neutrons (N).",
                    "diagram_title": "Mass Number Nucleon Sum Formulation",
                    "diagram_type": "image",
                    "image_query": "mass number nucleons protons plus neutrons notation diagram",
                    "video_query": "mass number and atomic number",
                    "image_url": "/extracted_diagrams/ch8/fig_8_12.webp",
                    "what_to_make": "Textbook formula chart defining A = Z + N and standard symbol notation.",
                    "timing_and_cue": "Mount mass number on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_12.webp | Mass Number (A) | Total nucleons: A = Z + N\")"
                },
                {
                    "concept_title": "Isotopes Invariant: Isotopes are defined as atoms of the SAME element having the same atomic number (Z) but different mass numbers (A), possessing identical chemical properties but different physical masses.",
                    "diagram_title": "Isotopes of Hydrogen Protium Deuterium Tritium",
                    "diagram_type": "image",
                    "image_query": "isotopes of hydrogen protium deuterium tritium nuclear structure diagram",
                    "video_query": "isotopes of hydrogen animation",
                    "image_url": "/extracted_diagrams/ch8/fig_8_8.webp",
                    "what_to_make": "Textbook diagram displaying Protium (1p, 0n), Deuterium (1p, 1n), and Tritium (1p, 2n).",
                    "timing_and_cue": "Mount hydrogen isotopes on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_8.webp | Hydrogen Isotopes | Protium (0n), Deuterium (1n), Tritium (2n)\")"
                },
                {
                    "concept_title": "Fractional Atomic Masses: The mass of an element is the weighted average mass of its naturally occurring isotopes based on their percentage abundance: Cl = (35 * 75% + 37 * 25%) = 35.5 u.",
                    "diagram_title": "Chlorine Fractional Atomic Mass Calculation",
                    "diagram_type": "image",
                    "image_query": "fractional atomic mass of chlorine 35.5 u calculation diagram",
                    "video_query": "how to calculate fractional atomic mass chlorine",
                    "image_url": "/extracted_diagrams/ch8/fig_8_13.webp",
                    "what_to_make": "Textbook diagram showing 75% Cl-35 and 25% Cl-37 weighted average calculation.",
                    "timing_and_cue": "Mount fractional mass on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_13.webp | Fractional Atomic Mass | Chlorine 35.5 u from 75% Cl-35 and 25% Cl-37\")"
                },
                {
                    "concept_title": "Isobars Invariant: Isobars are defined as atoms of DIFFERENT elements having the same mass number (A) but different atomic numbers (Z), such as Calcium-40 (Z=20) and Argon-40 (Z=18).",
                    "diagram_title": "Isobars Argon-40 and Calcium-40 Structure",
                    "diagram_type": "image",
                    "image_query": "isobars calcium 40 argon 40 atomic structure diagram",
                    "video_query": "isotopes vs isobars chemistry",
                    "image_url": "/extracted_diagrams/ch8/fig_8_14.webp",
                    "what_to_make": "Textbook diagram comparing nuclear structures of Argon-40 (18p, 22n) and Calcium-40 (20p, 20n).",
                    "timing_and_cue": "Mount isobars on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_14.webp | Isobars (Same A=40) | Argon (18p, 22n) vs Calcium (20p, 20n)\")"
                },
                {
                    "concept_title": "Medical & Industrial Radioisotopes: Uranium-235 is used as nuclear fuel; Cobalt-60 is used in the treatment of cancer; Iodine-131 is used in the treatment of goitre.",
                    "diagram_title": "Applications of Radioactive Isotopes",
                    "diagram_type": "image",
                    "image_query": "applications of radioisotopes cobalt 60 iodine 131 uranium 235 diagram",
                    "video_query": "uses of radioactive isotopes in medicine",
                    "image_url": "/extracted_diagrams/ch8/fig_8_8.webp",
                    "what_to_make": "Textbook photo of Bhabha Atomic Research Centre and radioisotope applications.",
                    "timing_and_cue": "Mount radioisotopes on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch8/fig_8_8.webp | Radioisotopes in Medicine & Energy | Cobalt-60 cancer therapy, Iodine-131 goitre, Uranium-235 fuel\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "Does any single chlorine atom on Earth actually weigh 35.5 atomic mass units?"
   - Calculation: Weighted average of Cl-35 (75%) and Cl-37 (25%) on the board.
   - Socratic check: "Why do isotopes have identical chemical properties, but isobars have completely different chemical properties?" HARD STOP: Wait for student answer!"""
    }

    return [m1, m2, m3, m4, m5, m6]

with open('scripts/science_modules_ch8.json', 'w', encoding='utf-8') as f:
    json.dump(get_ch8_modules(), f, indent=2)

print("Chapter 8 complete: 6 modules synthesized with 1:1 visuals and worked examples.")
