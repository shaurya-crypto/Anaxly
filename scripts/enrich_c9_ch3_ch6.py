import json
import os

CURRICULUM_IDS = {
    3: "1053ed93-7167-423b-bdf0-0c73f2b179ff", # Tissues in Action
    4: "b1a05ff2-8ca8-4d59-b7c7-cc0e1304c3ae", # Describing Motion Around Us
    5: "8d01a5f5-bf82-49c2-9fab-253d26b086f4", # Exploring Mixtures and their Separation
    6: "7e1d5438-1174-4577-8599-5f05a6642093"  # How Forces Affect Motion
}

# ==============================================================================
# CHAPTER 3: TISSUES IN ACTION (EXHAUSTIVE SOLVER M7)
# ==============================================================================
def get_ch3_solver_examples():
    return [
        {
            "problem": "Textbook Revise, Reflect, Refine Q1 (Section 3.1, p. 17): Meristematic tissues divide repeatedly. What property of their cells allows them to do this? (i) They have thick walls for protection. (ii) They contain large vacuoles that store nutrients. (iii) They have thin walls, dense cytoplasm and large prominent nucleus. (iv) They are functionally differentiated cells.",
            "given": "Four cytological characterization options for actively dividing plant meristematic cells.",
            "formula": "Cytology of Mitotic Cells: Continuous division requires thin deformable walls, high metabolic turnover (dense cytoplasm, no vacuoles), and active transcription (large prominent nucleus).",
            "substitution": "Evaluate options against meristematic histology.",
            "calculation": "1. Meristematic cells undergo continuous mitotic cycles. Thick walls (i) and functional differentiation (iv) prevent division.\n2. Large vacuoles (ii) store sap and would physically obstruct spindle formation and chromosome segregation.\n3. Thin cellulose walls allow rapid cell expansion; dense protoplasm provides high metabolic energy; and prominent nuclei drive continuous replication.",
            "finalAnswer": "Correct Option: (iii) They have thin walls, dense cytoplasm and large prominent nucleus.",
            "unit": "Cytological Identification",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "meristematic tissue onion root tip cytology",
            "page": 17,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q2 (Section 3.2, p. 17): If a plant is unable to transport food from leaves to roots, which tissue is malfunctioning? (i) Xylem, (ii) Phloem, (iii) Epidermis, (iv) Sclerenchyma.",
            "given": "Failure of bidirectional translocation of photosynthates (sucrose, amino acids) from leaves to roots.",
            "formula": "Vascular translocation: Xylem transports water and minerals unidirectionally; Phloem transports organic nutrients bidirectionally.",
            "substitution": "Identify the conducting tissue responsible for food transport.",
            "calculation": "Leaves synthesize sucrose via photosynthesis. Phloem (specifically sieve tubes and companion cells) translocates this dissolved food to storage sinks and roots using ATP-driven active transport. Failure of food transport indicates phloem dysfunction.",
            "finalAnswer": "Correct Option: (ii) Phloem.",
            "unit": "Plant Vascular Physiology",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "phloem sieve tube companion cell translocation",
            "page": 17,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q3 (Section 3.3, p. 17): Why are the epithelial tissues that line an animal's internal organs usually only one or a few cells thick? (i) To store food efficiently, (ii) To provide maximum strength, (iii) To allow quick exchange of materials across them, (iv) To reduce friction.",
            "given": "Histological thickness of internal epithelial linings (alveoli, nephrons, capillaries, intestine).",
            "formula": "Fick's Diffusion Law: Rate of diffusion is inversely proportional to barrier thickness ($Rate \\propto 1 / \\Delta x$).",
            "substitution": "Evaluate biological utility of thin single-layered epithelium.",
            "calculation": "Epithelial linings in organs such as pulmonary alveoli, capillary walls, and renal tubules are specialized for rapid diffusion, filtration, and absorption. A thin simple epithelium (single cell layer) minimizes the diffusion pathway $\\Delta x$, enabling rapid exchange of respiratory gases, nutrients, and waste products.",
            "finalAnswer": "Correct Option: (iii) To allow quick exchange of materials across them.",
            "unit": "Animal Histology",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "simple squamous epithelium diffusion barrier",
            "page": 17,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q4 & Q5 (Section 3.3, p. 17): You perform two jumps (Fig. 3.21): (a) Straight-leg jump (knees/ankles stiff), (b) Normal jump (knees/ankles bent). How did ankle, knee, and hip positions differ? Which joint is involved when bending knees and ankles?",
            "given": "Kinematic comparison of stiff-legged jump vs normal flexed jump; Joint movement analysis.",
            "formula": "Skeletal biomechanics: Shock absorption via flexor muscles and synovial hinge joints.",
            "substitution": "Evaluate angular displacement of joints and shock impact.",
            "calculation": "1. In normal jumping, hips, knees, and ankles undergo flexion during landing, lengthening impact duration and distributing shock force across quadriceps, gastrocnemius, tendons, and cartilage. In a straight-leg jump, joints remain locked in rigid extension, transmitting high unattenuated impact forces directly into bones and the spine.\n2. The knee and ankle joints are primarily HINGE JOINTS (allowing flexion and extension in a single sagittal plane).",
            "finalAnswer": "Bending knees and ankles elongates landing impact time and cushions shock; the joints involved in bending knees and ankles are (ii) Hinge joints.",
            "unit": "Musculoskeletal Biomechanics",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.21: Straight-leg vs normal jump showing knee and ankle joint mechanics",
            "image_search_query": "knee hinge joint synovial flexion extension anatomy",
            "page": 17,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q6 (Section 3.3, p. 17): Assertion & Reason Analysis: A. Assertion: Epithelium is well-vascularized with rich blood vessels. Reason: It covers outer body surfaces. B. Assertion: Bone matrix is hard and non-flexible. Reason: It is composed of calcium and phosphorus compounds. C. Assertion: Tendons connect bone to bone. Reason: Tendons transmit muscle force. D. Assertion: In a hinge joint, movement occurs in one plane. Reason: Bone ends allow sliding in all directions.",
            "given": "Four assertion-reason pairings on animal tissues and joints.",
            "formula": "Histological principles: Epithelium is avascular; Bone has calcium hydroxyapatite; Ligaments connect bone-to-bone, tendons connect muscle-to-bone; Hinge joints restrict motion to one plane.",
            "substitution": "Evaluate truth value of each Assertion and Reason.",
            "calculation": "A. Epithelium is completely AVASCULAR (nourished by diffusion from underlying connective tissue dermis). Assertion is False; Reason is True ⟶ Option (iv).\nB. Bone matrix is hard and rigid due to calcium phosphate and carbonate salts. Both (A) and (R) are True, and (R) correctly explains (A) ⟶ Option (i).\nC. Tendons connect MUSCLE TO BONE (ligaments connect bone to bone). Assertion is False; Reason is True ⟶ Option (iv).\nD. Hinge joint allows motion strictly in ONE plane (like a door hinge), NOT all directions. Assertion is True; Reason is False ⟶ Option (iii).",
            "finalAnswer": "A: (iv) A is false, R is true; B: (i) Both A and R are true and R explains A; C: (iv) A is false, R is true; D: (iii) A is true, R is false.",
            "unit": "Histological Logic Analysis",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "bone histology haversian system calcium phosphorus",
            "page": 17,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q7 (Section 3.1, p. 18): Data in Table 3.7 gives age of teak tree (5, 10, 20, 25, 30, 40 yrs), diameter DBH (4, 8, 24, 28, 32, 40 cm), and annual rings (5, 10, 20, 25, 30, 40). (i) Analyse stem diameter over time. (ii) Relation between diameter and annual rings. (iii) Which specialised tissue is responsible for girth, and where is it located?",
            "given": "Teak tree growth data from Table 3.7 over a 40-year period.",
            "formula": "Secondary Growth: Lateral meristem (cambium) cuts off secondary xylem (spring wood + autumn wood = 1 annual ring per year).",
            "substitution": "Analyze growth rates and correlate with cambial activity.",
            "calculation": "1. Part (i): DBH increases continuously with age. Growth rate is rapid during the first 20 years (from 4 cm at 5 yr to 24 cm at 20 yr, averaging 1.33 cm/yr) and then stabilizes to a steady linear increment (~0.8 cm/yr from 20 to 40 yr).\n2. Part (ii): Number of annual rings is strictly equal to the age of the tree in years (1:1 direct proportionality). Each year, vascular cambium produces one ring of earlywood and latewood.\n3. Part (iii): The tissue responsible for increasing stem girth is the LATERAL MERISTEM (specifically VASCULAR CAMBIUM and CORK CAMBIUM / PHELLOGEN), located circumferentially beneath the bark as cylindrical dividing layers.",
            "finalAnswer": "(i) Girth increases steadily with time; (ii) Annual rings equal the tree's age (1 ring/year); (iii) Lateral meristem (cambium) located radially beneath the bark.",
            "unit": "Dendrochronology & Secondary Growth",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Table 3.7 & Secondary growth rings in woody dicot stem",
            "image_search_query": "tree annual rings vascular cambium secondary growth",
            "page": 18,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q8 (Section 3.2, p. 18): In a forest, a tree was severely debarked by an elephant to eat the nutrient-rich bark (Fig. 3.22). (i) Which function(s) of the tree are hampered by debarking? (ii) Which plant tissue is lost? (iii) Can the tree survive long term?",
            "given": "Complete removal of outer bark around tree trunk (girdling / debarking).",
            "formula": "Bark anatomy: Cork (protective barrier) + Cork Cambium + Secondary Phloem (nutrient translocation).",
            "substitution": "Analyze structural and physiological consequences of girdling.",
            "calculation": "1. Part (i): Functions hampered: Translocation of prepared organic food (sucrose) from crown leaves down to root system; mechanical protection against fungal/bacterial infections; and prevention of evaporative desiccation.\n2. Part (ii): Debarking removes the protective CORK (phellem), CORK CAMBIUM (phellogen), and crucially the SECONDARY PHLOEM located immediately under the bark.\n3. Part (iii): Without functional phloem, roots are starved of photosynthates. Starved roots eventually fail to absorb water and minerals, leading to systemic tree death within months unless partial vertical bark strips remain intact.",
            "finalAnswer": "(i) Food translocation to roots and pathogen protection are hampered; (ii) Cork and secondary phloem are lost; (iii) Tree dies due to root starvation unless girdling is incomplete.",
            "unit": "Forest Botany & Tissue Pathology",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.22: Tree debarked by elephant showing exposed inner xylem",
            "image_search_query": "tree debarking girdling phloem transport death",
            "page": 18,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q9 (Section 3.2, p. 19): Aamrapali observed that a young mango sapling's stem bends flexibly during monsoon winds without breaking. Which tissue is responsible for this flexibility? Predict the impact if this tissue was replaced by sclerenchyma.",
            "given": "Mechanical flexibility in herbaceous young stems vs rigid brittle woody stems.",
            "formula": "Mechanical plant tissues: Collenchyma provides tensile flexibility; Sclerenchyma provides rigid load-bearing stiffness.",
            "substitution": "Tissue characteristics and functional adaptations.",
            "calculation": "1. The tissue responsible for mechanical flexibility with tensile strength is COLLENCHYMA (characterized by living elongated cells with localized pectin and cellulose thickenings at cell corners).\n2. If collenchyma were replaced by SCLERENCHYMA (dead cells with heavily lignified, rigid, inflexible secondary walls), the sapling stem would lose all elasticity. Instead of bending smoothly with violent monsoon gusts, the brittle stem would snap and break under bending stress.",
            "finalAnswer": "Collenchyma provides bending flexibility; if replaced by sclerenchyma, the stem would become rigid and brittle, snapping in strong winds.",
            "unit": "Plant Mechanical Histology",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "collenchyma corner thickening plant stem flexibility",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q10 (Section 3.1, p. 19): Sohan planted two types of sugarcane cuttings: Type A (internode piece without nodes) and Type B (stem cutting containing intact nodes with lateral buds, Fig. 3.23). After a few weeks, Type B sprouted into plants, but Type A did not sprout. (i) Why did Type B grow while Type A failed? (ii) What was present in Type B? (iii) What parameters ensure a fair comparison?",
            "given": "Sugarcane stem cuttings: Type A (internodal only) vs Type B (nodal with bud).",
            "formula": "Meristematic Localization: Intercalary and axillary meristems are localized strictly at NODES.",
            "substitution": "Correlate presence of dividing meristematic cells with regenerative sprouting.",
            "calculation": "1. Part (i) & (ii): Sugarcane possesses intercalary meristems and dormant vegetative axillary buds situated exclusively at the NODES (joints) of the stem. Type B cuttings possessed intact nodes containing active meristematic tissues capable of mitotic division to initiate roots and shoots. Type A consisted solely of differentiated internodal tissue devoid of meristems, rendering growth impossible.\n2. Part (iii): Controlled parameters: Soil composition, moisture level, temperature, depth of planting, sunlight exposure, and cutting diameter.",
            "finalAnswer": "(i) Type B possessed active meristems at nodes; (ii) Nodal intercalary meristems and axillary buds; (iii) Equal water, soil, sunlight, and cutting size for a fair test.",
            "unit": "Vegetative Regeneration Mechanics",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.23: Sugarcane stem cuttings Type A (no node) vs Type B (with node)",
            "image_search_query": "sugarcane nodes buds intercalary meristem vegetative propagation",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q11 (Section 3.2, p. 19): During class, Rohan states: 'A tissue is a group of similar cells performing similar functions.' Rajiv counter-argues: 'This is true for simple tissues, but different for complex tissues.' Provide your scientific explanation.",
            "given": "Two definitions of biological tissues debated by students.",
            "formula": "Histological taxonomy: Simple permanent tissues (homogeneous) vs Complex permanent tissues (heterogeneous).",
            "substitution": "Evaluate cellular composition of parenchyma vs xylem/phloem.",
            "calculation": "1. Rajiv's counter-argument is scientifically sound and more accurate.\n2. Simple tissues (Parenchyma, Collenchyma, Sclerenchyma) consist of only ONE type of cell that are morphologically identical and work together.\n3. In contrast, Complex tissues (Xylem and Phloem) are composed of MULTIPLE DISTINCT CELL TYPES originating from the same meristem and coordinating to perform a common function. For instance, Xylem comprises four distinct cell types: tracheids, vessels, xylem parenchyma, and xylem fibres.",
            "finalAnswer": "Rajiv is correct: Simple tissues have homogeneous cells (one type), whereas complex tissues like xylem and phloem unite diverse cell types coordinating a shared function.",
            "unit": "Histological Taxonomy",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "xylem complex tissue four elements tracheids vessels",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q12 (Section 3.2, p. 19): Coconut husk fibres are used for making tough, durable mats. Which plant tissue provides this strength? Explain why living parenchyma could not serve this purpose.",
            "given": "Physical characteristics of coir (coconut husk) and functional requirements of floor mats.",
            "formula": "Histological mechanics: Lignified sclerenchyma fibres vs unlignified living parenchyma.",
            "substitution": "Correlate cellular wall composition with tensile wear resistance.",
            "calculation": "1. Coconut husk is composed of SCLERENCHYMA FIBRES (specifically sclerenchymatous sclereids and elongated thick-walled fibres).\n2. Their secondary cell walls are heavily impregnated with LIGNIN, a natural complex polymer that acts as cement, rendering the cells impermeable, rigid, and resistant to decay, microbial rot, and abrasive wear.\n3. Living parenchyma cells have thin cellulose walls, large fluid-filled vacuoles, and soft protoplasm. Under foot pressure or friction, parenchyma cells would compress, tear, rot, and lose all structural integrity instantly.",
            "finalAnswer": "Sclerenchyma provides high tensile toughness via lignified dead cell walls; living parenchyma is soft and fragile, collapsing under abrasive mechanical stress.",
            "unit": "Plant Fiber Mechanics",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "coconut husk coir sclerenchyma fibres lignin",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q13 (Section 3.1, p. 19): Vibha claims to Neha: 'Meristematic cells are located in all parts of a plant, and that is why plants can grow anywhere.' What questions can Neha ask Vibha to help her understand the localized nature of meristematic tissues?",
            "given": "Misconception that plant growth and meristems are uniformly distributed throughout the plant body.",
            "formula": "Socratic inquiry into localized apical, lateral, and intercalary meristem distribution.",
            "substitution": "Formulate targeted diagnostic questions based on plant observations.",
            "calculation": "To guide Vibha to self-correct, Neha can ask:\n1. 'If meristems are everywhere, why does a tree trunk only lengthen at the tips of branches and roots, rather than stretching in the middle of a mature trunk?'\n2. 'If you trim the apical root tip of an onion bulb in water, why does that specific root stop growing in length completely while untouched roots continue to elongate?'\n3. 'Why does secondary thickening (girth expansion) happen strictly in rings around the stem diameter rather than in random lumps?'",
            "finalAnswer": "Neha can ask why growth stops when shoot/root tips are trimmed, and why mature tree trunks elongate exclusively at apical buds rather than everywhere.",
            "unit": "Socratic Pedagogical Inquiry",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "apical lateral intercalary meristems plant zones",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q14 (Section 3.1, p. 19): A plant cell and an animal cell are of the same size. (i) How do their mechanical support strategies differ? (ii) What assumptions are made when comparing their tissue architecture?",
            "given": "Comparative cell and tissue mechanics between plants and animals.",
            "formula": "Stationary autotrophic support (external rigid cell wall) vs Motile heterotrophic support (cytoskeleton + internal extracellular matrix/skeletons).",
            "substitution": "Analyze metabolic energy expenditure vs structural rigidity.",
            "calculation": "1. Part (i): A plant cell relies on an external, non-living cellulose CELL WALL that works in conjunction with internal vacuolar turgor pressure to maintain shape without metabolic expenditure. An animal cell lacks a cell wall and relies on an internal dynamic protein cytoskeleton (microfilaments, microtubules) anchored to an extracellular collagen matrix, bones, and cartilage.\n2. Part (ii): Assumptions: Both cells operate under standard physiological temperature and pressure; the plant cell is fully hydrated in a hypotonic extracellular fluid; and the animal cell is bathed in an isotonic extracellular fluid (interstitial fluid/blood plasma).",
            "finalAnswer": "(i) Plant cells use rigid cellulose walls and turgor pressure; animal cells use protein cytoskeletons and skeletal connective tissues; (ii) Assumes plant cell in hypotonic and animal cell in isotonic media.",
            "unit": "Comparative Cytological Mechanics",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "plant versus animal cell structural support mechanisms",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q15 (Section 3.2, p. 19): A textbook states: 'Each plant tissue performs only one specific function.' What questions would you ask to critically examine this statement, and what investigation would you undertake?",
            "given": "Oversimplified claim regarding tissue monofunctionality.",
            "formula": "Multifunctional tissue biology (e.g. Parenchyma stores food, performs photosynthesis as chlorenchyma, provides buoyancy as aerenchyma, and repairs wounds).",
            "substitution": "Formulate critical scientific questions and experimental investigations.",
            "calculation": "1. Critical Questions:\n   - 'If parenchyma only has one function, why does it perform photosynthesis in leaves (chlorenchyma), store starch in roots, provide floatation in aquatic plants (aerenchyma), and divide to heal graft wounds?'\n   - 'Doesn't xylem conduct water AND simultaneously provide the primary mechanical load-bearing support for massive trees via wood?'\n2. Investigative Procedure: Prepare thin sections of different organs of the same plant (leaf, petiole, aquatic stem, tuber). Stain with safranin and fast green to demonstrate how the same tissue type exhibits structural modifications to execute multiple distinct physiological functions.",
            "finalAnswer": "Critique by noting that parenchyma stores starch, performs photosynthesis, and provides buoyancy; investigate by observing tissue histology across aquatic and terrestrial organs.",
            "unit": "Critical Histological Evaluation",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "parenchyma chlorenchyma aerenchyma multiple functions",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "In-Text Question (Section 3.2, p. 7): (a) Why is a thick waxy cuticle on the outer epidermis an adaptation for desert plants? (b) What will happen if there were no stomata in plant leaves?",
            "given": "Plant epidermal adaptations and stomatal physiology.",
            "formula": "Transpiration biophysics: Cuticular resistance and stomatal pore regulation.",
            "substitution": "Analyze water loss and gas exchange.",
            "calculation": "1. Part (a): Desert xerophytes face intense solar radiation and arid winds. A thick layer of water-impermeable CUTIN (waxy cuticle) on epidermal cells minimizes cuticular transpiration, preventing fatal desiccation.\n2. Part (b): Stomata are microscopic pores guarded by specialized guard cells. Without stomata: (1) Plants could not exchange respiratory and photosynthetic gases (CO₂ uptake for Calvin cycle and O₂ release would cease, halting photosynthesis); (2) Transpirational pull would vanish, arresting the upward ascent of sap (water and minerals) from roots to leaves.",
            "finalAnswer": "(a) Thick waxy cutin minimizes transpiration water loss; (b) Without stomata, photosynthesis stops due to zero CO₂ diffusion, and transpirational water transport collapses.",
            "unit": "Epidermal & Stomatal Physiology",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "desert plant thick cuticle stomata transpiration",
            "page": 7,
            "section": "Section 3.2"
        }
    ]

def update_ch3():
    with open("scripts/science_modules_ch3.json", "r", encoding="utf-8") as f:
        mods = json.load(f)
    
    # Update curriculum_id and class_level on all modules
    for m in mods:
        m["curriculum_id"] = CURRICULUM_IDS[3]
        m["class_level"] = "Class 9"
        m["board"] = "CBSE"
        # ensure worked_examples have image_search_query
        for we in m.get("worked_examples", []):
            if "image_search_query" not in we or not we["image_search_query"]:
                we["image_search_query"] = "plant animal tissues class 9 ncert"
            if "page" not in we:
                we["page"] = 28 + m["order_index"]
            if "section" not in we:
                we["section"] = f"Section 3.{m['order_index']}"
                
    # Replace solver module (M7) with the complete 15-question exhaustive ledger
    m7 = mods[-1]
    m7["title"] = "Master Problem Solver & Comprehensive Textbook Exercise Ledger (Revise, Reflect, Refine Q1 to Q15)"
    m7["worked_examples"] = get_ch3_solver_examples()
    m7["description"] = "Exhaustive step-by-step master solutions for all in-text questions and all 15 'Revise, Reflect, Refine' chapter-end exercise problems from NCERT Exploration Grade 9 Chapter 3."
    
    with open("scripts/science_modules_ch3.json", "w", encoding="utf-8") as f:
        json.dump(mods, f, indent=2)
    print("Updated scripts/science_modules_ch3.json successfully!")

if __name__ == "__main__":
    update_ch3()
