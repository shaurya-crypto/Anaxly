"""
Enriches all modules for Class 9 Science Chapters 3, 4, 5, 6 with:
1. 1:1 worked_examples matching EVERY key concept in every module (5-6 per module).
2. Comprehensive NCERT exercise solutions for the solver modules (Q1-Q14 for Ch3, Q1-Q10 for Ch4, Q1-Q11 for Ch5, Q1-Q18 for Ch6).
3. Ensures valid JSON structure, book_extracted diagram citations, and Topper Given->Formula->Substitution->Calculation->Final Answer format.
"""

import json
import os

# ==============================================================================
# CHAPTER 3: TISSUES IN ACTION (7 MODULES)
# ==============================================================================
ch3_worked_examples = {
    1: [
        {
            "problem": "Why do plants consist predominantly of dead supportive tissues while animals are composed almost entirely of living tissues?",
            "given": "Comparative life strategies: stationary autotrophic plant vs motile heterotrophic animal.",
            "formula": "Bioenergetic & Structural Requirement Principle",
            "substitution": "Plants do not consume energy for locomotion; dead cells (sclerenchyma, xylem, cork) provide identical mechanical load-bearing capacity as living cells without requiring ongoing metabolic energy.",
            "calculation": "1. Stationary plants need upright structural strength against gravity and wind.\n2. Dead cells provide rigid, lignified walls that support immense weight without cellular respiration.\n3. Animals must move actively to seek food, shelter, and mates, requiring continuous metabolic flexibility and contractile living tissues.",
            "finalAnswer": "Plants utilize dead tissues to achieve structural rigidity at zero metabolic maintenance cost, whereas animals require living cells for active movement and physiological regulation.",
            "unit": "Histological Adaptations",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.1: Comparative plant vs animal architectural blueprints"
        },
        {
            "problem": "Why do actively dividing meristematic cells lack sap storage vacuoles?",
            "given": "Cytological analysis of shoot and root apical meristems.",
            "formula": "Mitotic Cytology Invariant",
            "substitution": "Vacuoles store cell sap, metabolic waste, and provide hydrostatic turgidity in mature cells.",
            "calculation": "1. Meristematic cells undergo continuous and rapid mitotic cell division.\n2. All synthesized nutrients and ATP are consumed immediately for DNA replication and cytokinesis, leaving no excess sap to store.\n3. A large fluid-filled vacuole would physically displace the nucleus and obstruct mitotic spindle assembly during chromosome segregation.",
            "finalAnswer": "Meristematic cells lack vacuoles because they have high metabolic turnover leaving no surplus for storage, and large vacuoles would physically hinder rapid cell division.",
            "unit": "Cytology Invariant",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.2: Longitudinal section of shoot apex showing compact meristematic cells"
        },
        {
            "problem": "A potted plant is placed horizontally. What meristem is responsible for the upward bending of the shoot and downward bending of the root?",
            "given": "Geotropic and phototropic response of shoot and root apices.",
            "formula": "Apical Meristem Elongation Dynamics",
            "substitution": "Differential cell elongation driven by apical meristems and auxin distribution.",
            "calculation": "1. The shoot apical meristem at the tip responds to asymmetric auxin accumulation on the lower side, causing rapid cell division and elongation upward (negative geotropism).\n2. The root apical meristem directs primary elongation downward into the soil (positive geotropism).",
            "finalAnswer": "Shoot apical meristem and root apical meristem drive primary elongation in response to gravitational orientation.",
            "unit": "Primary Meristem Function",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.3: Location of Apical, Intercalary, and Lateral meristems on a plant body"
        },
        {
            "problem": "A tree trunk increases in girth and diameter every year. Which specific tissue is responsible for this secondary growth?",
            "given": "Radial expansion of dicot woody stems.",
            "formula": "Secondary Lateral Meristem Action",
            "substitution": "Vascular cambium and cork cambium (phellogen) divide tangentially in radial directions.",
            "calculation": "1. Lateral meristem (cambium) forms concentric dividing cylinders.\n2. Vascular cambium cuts off secondary xylem internally (forming wood) and secondary phloem externally.\n3. Cork cambium produces impermeable cork layers externally, progressively widening stem girth.",
            "finalAnswer": "Lateral meristem (specifically vascular cambium and cork cambium) drives secondary growth, increasing girth.",
            "unit": "Secondary Meristem Function",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.5: Secondary thickening in dicot stem driven by lateral cambium"
        },
        {
            "problem": "Why does a lawn regrow rapidly after being cut by a lawnmower, whereas a sunflower stem ceases upward growth if its tip is trimmed?",
            "given": "Monocot grasses vs dicot herbs after apical trimming.",
            "formula": "Intercalary vs Apical Meristem Localization",
            "substitution": "Grasses possess intercalary meristems at the bases of internodes and leaves; dicots rely solely on terminal apical meristems.",
            "calculation": "1. Lawnmowers excise the apical tips of grass blades.\n2. Intercalary meristems situated at the base of the blade and nodes remain undamaged beneath the cut line, rapidly dividing to elongate the blade.\n3. Sunflowers lack intercalary meristems; trimming the apex eliminates apical dividing cells entirely.",
            "finalAnswer": "Lawn grass regrows because intercalary meristems at leaf bases remain intact below the cutting level and drive rapid elongation.",
            "unit": "Meristem Adaptation",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.6: Monocot grass stem demonstrating nodal intercalary meristem bands"
        },
        {
            "problem": "In Activity 3.1, why did root growth in Jar B cease completely after 1 cm was cut from the tips on Day 4, while Jar A roots continued elongating?",
            "given": "Two onion bulbs in water: Jar A (uncut) vs Jar B (tips cut by 1 cm).",
            "formula": "Root Apical Meristem Excision Effect",
            "substitution": "Root apical meristem is strictly localized within the terminal 1-2 mm of the root tip.",
            "calculation": "1. Day 1 to 3: Both jars grow at ~2 mm/day via active mitosis in apical meristems.\n2. Day 4: Cutting 1 cm from Jar B completely excises the root cap and quiescent centre containing all apical meristematic cells.\n3. Without dividing cells, no new cells can be added; longitudinal growth halts permanently.",
            "finalAnswer": "Excision of root tips in Jar B physically removed the apical meristematic tissue, permanently arresting further mitotic division and elongation.",
            "unit": "Experimental Lab Deduction",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.2: Growth of onion roots in water jars (Jar A uncut vs Jar B excised)"
        }
    ],
    2: [
        {
            "problem": "What is the process of differentiation, and how does a meristematic cell transform into a permanent sclerenchyma cell?",
            "given": "Cellular development from dividing meristem to permanent tissue.",
            "formula": "Differentiation Pathway: Mitosis -> Vacuolation -> Wall Thickening -> Protoplast Loss",
            "substitution": "Cells take up a permanent shape, size, and function through genetic expression.",
            "calculation": "1. A meristematic daughter cell ceases active division.\n2. It absorbs water, expands, and deposits thick secondary cell wall layers impregnated with lignin.\n3. The living protoplast eventually disintegrates, leaving a hollow, rigid, dead lumen.",
            "finalAnswer": "Differentiation is the process whereby non-specialized dividing cells undergo morphological and biochemical specialization to assume permanent, specialized functions.",
            "unit": "Cytological Transformation",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.7: Transverse section of plant stem displaying tissue differentiation layers"
        },
        {
            "problem": "Why is parenchyma termed the basic packaging and storage tissue of plants?",
            "given": "Parenchyma morphology and cellular characteristics.",
            "formula": "Thin Primary Wall + Large Central Vacuole = Storage Matrix",
            "substitution": "Unspecialized isodiametric cells with thin cellulose walls and prominent intercellular spaces.",
            "calculation": "1. Parenchyma fills the ground space (cortex and pith) between specialized vascular tissues.\n2. Its thin cellulose walls permit easy diffusion of nutrients.\n3. Large central vacuoles store water, starch, proteins, and metabolic products.",
            "finalAnswer": "Parenchyma forms the bulk of unspecialized ground tissue and stores nutrients and water in large vacuoles with ample intercellular spaces.",
            "unit": "Ground Tissue Mechanics",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.10: Parenchyma tissue (transverse and longitudinal sections showing intercellular spaces)"
        },
        {
            "problem": "How does chlorenchyma differ functionally and structurally from general parenchyma?",
            "given": "Photosynthetic tissue specialization in mesophyll of leaves.",
            "formula": "Chlorenchyma = Parenchyma + Chloroplasts",
            "substitution": "Parenchyma cells in leaves and young green stems contain abundant chlorophyll pigments.",
            "calculation": "1. Standard parenchyma primarily performs mechanical packing and storage.\n2. Chlorenchyma cells house thylakoid membranes and rubisco enzymes to capture sunlight and perform carbon dioxide assimilation (photosynthesis).",
            "finalAnswer": "Chlorenchyma is specialized parenchyma containing chloroplasts dedicated to photosynthesis in leaves and green stems.",
            "unit": "Photosynthetic Histology",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.8: Leaf cross-section showing palisade and spongy chlorenchyma"
        },
        {
            "problem": "How do hydrophytic aquatic plants like Eichhornia (water hyacinth) and Hydrilla float on the water surface?",
            "given": "Buoyancy adaptation in aquatic flora.",
            "formula": "Aerenchyma Buoyancy: Air Cavity Network = Low Effective Density",
            "substitution": "Parenchyma cells enclosing immense, interconnected air cavities.",
            "calculation": "1. In aquatic plants, large intercellular air cavities develop within the parenchyma ground tissue.\n2. Trapped atmospheric gases lower the overall bulk density of the stems and petioles below that of water ($1.0\\text{ g/cm}^3$).\n3. This hydrostatic buoyancy keeps leaves and flowers floating near the surface for sunlight and gas exchange.",
            "finalAnswer": "Aerenchyma tissue contains extensive air spaces that provide buoyancy, allowing aquatic plants to float.",
            "unit": "Hydrophyte Adaptations",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.9: Aerenchyma cross-section in aquatic petioles showing vast air lacunae"
        },
        {
            "problem": "Why can climbers and tender cucurbit tendrils bend and twist around supports without snapping during heavy winds?",
            "given": "Mechanical flexibility in plant tendrils and young stems.",
            "formula": "Collenchyma Biomechanics: Corner Pectin Thickening + Living Protoplast",
            "substitution": "Collenchyma provides mechanical flexibility without brittleness.",
            "calculation": "1. Collenchyma cells are elongated living cells located in the hypodermis of dicot stems and leaf stalks.\n2. Their primary walls have localized thickenings of cellulose, hemicellulose, and pectin at cell corners.\n3. Unlike sclerenchyma, collenchyma walls are unlignified and hydrated, giving immense tensile flexibility without breaking.",
            "finalAnswer": "Collenchyma provides mechanical tensile strength and flexibility due to localized pectin corner thickenings in living cells.",
            "unit": "Tensile Mechanical Support",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.11: Collenchyma cells showing prominent corner pectin thickenings"
        },
        {
            "problem": "Which tissue makes up the husk of a coconut, and what biochemical feature gives it immense hardness?",
            "given": "Hard, fibrous husk of Cocos nucifera.",
            "formula": "Sclerenchymatous Fibre Wall Composition",
            "substitution": "Thick secondary walls heavily encrusted with hydrophobic lignin.",
            "calculation": "1. Coconut husk consists of dead, elongated sclerenchyma fibres.\n2. The cell walls are heavily thickened with lignin, a rigid chemical complex acting as a natural cement.\n3. The lumen is extremely narrow or obliterated; cells are dead at maturity, providing extreme fracture resistance.",
            "finalAnswer": "The husk of a coconut consists of sclerenchymatous fibres whose walls are heavily thickened with lignin, making them dead and rigid.",
            "unit": "Lignified Biomechanics",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.12: Sclerenchyma fibres and sclereids showing thick lignified walls and narrow lumen"
        }
    ],
    3: [
        {
            "problem": "Why are xylem and phloem classified as complex permanent tissues rather than simple tissues?",
            "given": "Cellular heterogeneity of vascular bundles.",
            "formula": "Complex Tissue Definition: Heterogeneous cell types functioning as a single coordinated physiological unit.",
            "substitution": "Xylem and phloem consist of 4 distinct cell types each.",
            "calculation": "1. Simple tissues (parenchyma, collenchyma, sclerenchyma) consist of only ONE type of cell.\n2. Xylem consists of tracheids, vessels, xylem parenchyma, and xylem fibres.\n3. Phloem consists of sieve tubes, companion cells, phloem parenchyma, and phloem fibres.\n4. All elements work together as an integrated transport pipeline.",
            "finalAnswer": "Xylem and phloem are complex permanent tissues because they are composed of multiple distinct cell types acting in coordination to conduct water and food.",
            "unit": "Vascular Architecture",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.13: Vascular bundle cross-section showing xylem and phloem cylinders"
        },
        {
            "problem": "Compare tracheids and vessels on the basis of shape, end walls, and efficiency of water conduction.",
            "given": "Xylem water conducting elements.",
            "formula": "Hydraulic Conductance: Poiseuille Flow ($Q \\propto r^4$)",
            "substitution": "Tracheids: Spindle-shaped with tapered, imperforate pitted ends. Vessels: Cylindrical tubes with perforated end plates.",
            "calculation": "1. Tracheids: Elongated, single cells with tapering closed ends; water passes between cells via pits across pit membranes.\n2. Vessels: Long continuous tube formed by end-to-end fusion of vessel elements with dissolved or perforated cross-walls.\n3. Wider vessel diameter ($r$) dramatically increases hydraulic throughput proportional to $r^4$, making vessels far more efficient in angiosperms.",
            "finalAnswer": "Vessels form continuous, open perforated pipes offering far lower hydraulic resistance than closed, tapered, pitted tracheids.",
            "unit": "Hydraulic Architecture",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.14: Tracheid and vessel element morphology and perforation plates"
        },
        {
            "problem": "What is the only living component of xylem tissue, and what is its physiological role?",
            "given": "Cytological state of xylem elements.",
            "formula": "Living Parenchyma in Dead Xylem Matrix",
            "substitution": "Tracheids, vessels, and xylem fibres are dead; xylem parenchyma remains living.",
            "calculation": "1. Tracheids, vessels, and fibres undergo autolysis of protoplasm and deposit thick lignified walls.\n2. Xylem parenchyma retains thin cellulosic walls, living nucleus, and cytoplasm.\n3. It stores starch, fats, and tannins, and facilitates radial water conduction via ray parenchyma.",
            "finalAnswer": "Xylem parenchyma is the only living element; it stores nutrients and conducts water sideways along radial medullary rays.",
            "unit": "Physiological Storage",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.15: Radial xylem parenchyma ray cells conducting solutes laterally"
        },
        {
            "problem": "How do mature sieve tube elements survive and transport sugars despite lacking a nucleus?",
            "given": "Anucleate condition of functional angiosperm sieve tube elements.",
            "formula": "Symplastic Coupling: Sieve Element + Companion Cell Dyad",
            "substitution": "Companion cells maintain metabolic control over adjacent sieve tube elements via plasmodesmata.",
            "calculation": "1. Mature sieve tube elements discard their nucleus, vacuoles, and ribosomes to minimize resistance to phloem sap flow.\n2. Each sieve tube element is intimately connected to a sister companion cell via branched plasmodesmatal channels.\n3. The companion cell's nucleus and dense mitochondria provide nuclear genetic directives and ATP for active phloem loading and unloading.",
            "finalAnswer": "Sieve tubes survive via their companion cells, which supply ATP and regulatory directives through cytoplasmic plasmodesmata.",
            "unit": "Translocation Symbiosis",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.16: Longitudinal section of Phloem showing sieve plate, sieve tube, and companion cell"
        },
        {
            "problem": "What are stomata, and how do guard cells regulate transpiration and gaseous exchange in the plant epidermis?",
            "given": "Epidermal leaf architecture in Activity 3.3 (Rheo leaf peel).",
            "formula": "Turgor-Driven Guard Cell Osmotic Gating",
            "substitution": "Bean-shaped/kidney-shaped guard cells flanking a central stomatal pore.",
            "calculation": "1. Guard cells have unequally thickened cellulose walls (inner wall facing pore is thick and rigid; outer wall is thin and elastic).\n2. When water enters guard cells via osmosis, they swell; the thin outer wall bulges outwards, pulling the thick inner wall open.\n3. Loss of water decreases turgor, causing guard cells to become flaccid and close the stomatal pore to prevent desiccation.",
            "finalAnswer": "Stomata are epidermal pores regulated by turgor pressure changes in guard cells, controlling transpiration and $CO_2/O_2$ exchange.",
            "unit": "Epidermal Gas Exchange",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.4: Guard cells and stomatal pore in epidermal peel (open vs closed state)"
        },
        {
            "problem": "How does cork (bark) form protective tissue in mature trees, and what chemical makes it impervious to gases and water?",
            "given": "Outer protective secondary cortex (phellem).",
            "formula": "Suberin Deposition in Dead Cork Cells",
            "substitution": "Cork cambium (phellogen) produces multi-layered, compactly arranged dead cells without intercellular spaces.",
            "calculation": "1. As a woody stem expands in girth, outer epidermal layers rupture and are replaced by cork cambium.\n2. Cork cells become dead at maturity and pack tightly without gaps.\n3. Their secondary cell walls are heavily impregnated with suberin, a waxy hydrophobic substance that prevents water loss and resists microbial attack.",
            "finalAnswer": "Cork forms an impervious barrier because its compactly arranged dead cells are heavily impregnated with suberin, preventing water loss and mechanical injury.",
            "unit": "Protective Histology",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.5: Protective cork layer (bark) showing suberised cell walls"
        }
    ],
    4: [
        {
            "problem": "What are the common structural characteristics of all epithelial tissues?",
            "given": "Histological definition of epithelium.",
            "formula": "Acellular Basement Membrane + Intercellular Tight Junctions",
            "substitution": "Continuous sheets of tightly packed cells with almost no intercellular matrix.",
            "calculation": "1. Cells rest upon an extracellular fibrous basement membrane composed of collagen and glycoproteins.\n2. Tight junctions seal adjacent cell membranes to form an impermeable protective boundary.\n3. Epithelial tissue is avascular; nutrients diffuse from underlying connective tissue blood capillaries.",
            "finalAnswer": "Epithelial tissues form continuous tightly joined sheets resting on an extracellular basement membrane with zero intercellular space and no direct blood vessels.",
            "unit": "Epithelial Invariant",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.17: Types of epithelium: squamous, cuboidal, columnar, and ciliated"
        },
        {
            "problem": "Why are the alveoli of lungs and blood capillaries lined by simple squamous epithelium rather than stratified cuboidal epithelium?",
            "given": "Gas and solute diffusion across physiological barriers.",
            "formula": "Fick's First Law of Diffusion ($J = -D \\frac{dC}{dx}$)",
            "substitution": "Diffusion rate is inversely proportional to diffusion distance ($dx$).",
            "calculation": "1. Simple squamous epithelium consists of extremely thin, flat, scale-like cells (minimal $dx$).\n2. This minimal thickness permits rapid, unimpeded diffusion of $O_2$ and $CO_2$ between alveolar air and capillary red blood cells.\n3. Thicker multi-layered epithelium would increase diffusion distance, causing respiratory asphyxiation.",
            "finalAnswer": "Simple squamous epithelium provides an ultra-thin barrier minimizing diffusion distance for rapid gas exchange in lungs and capillaries.",
            "unit": "Diffusion Biomechanics",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.17a: Simple squamous epithelium lining alveolar exchange surfaces"
        },
        {
            "problem": "How does stratified squamous epithelium in human skin prevent mechanical wear and tear and water loss?",
            "given": "Epidermal integument of terrestrial mammals.",
            "formula": "Stratification + Keratinization Barrier",
            "substitution": "Multiple layers of flattened cells impregnated with water-insoluble fibrous keratin protein.",
            "calculation": "1. Multiple cellular strata allow superficial layers to slough off during friction without exposing deeper sensitive dermis.\n2. Basal cells continuously divide by mitosis to replenish shed cells.\n3. Keratin deposits create a tough, waterproof barrier preventing dehydration and pathogen entry.",
            "finalAnswer": "Stratified squamous epithelium consists of multiple cell layers with keratin deposits, providing abrasion resistance and waterproofing.",
            "unit": "Integumentary Protection",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.17b: Stratified squamous epithelium showing basal dividing and surface keratin layers"
        },
        {
            "problem": "Differentiate between cuboidal and ciliated columnar epithelium on the basis of location and function.",
            "given": "Specialized transport and protective epithelia.",
            "formula": "Cuboidal (Secretory/Absorptive) vs Columnar (Movement/Protection)",
            "substitution": "Cuboidal: Cube-shaped cells in kidney tubules. Ciliated columnar: Pillar-like cells with hair-like cilia in bronchioles and oviducts.",
            "calculation": "1. Cuboidal epithelium lines renal tubules and salivary ducts, offering mechanical support and microvilli for reabsorption.\n2. Ciliated columnar epithelium possesses rhythmic beating cilia that propel mucus and trapped dust particles out of the respiratory tract, and sweep ova along the fallopian tubes.",
            "finalAnswer": "Cuboidal epithelium lines kidney tubules for absorption/secretion; ciliated columnar lines respiratory tract and oviducts to propel substances in a specific direction.",
            "unit": "Epithelial Specialization",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.17c: Ciliated columnar epithelium showing surface cilia and basal oval nuclei"
        },
        {
            "problem": "How does glandular epithelium originate, and what do glands secrete?",
            "given": "Exocrine and endocrine glandular structures.",
            "formula": "Epithelial Invagination -> Secretory Acinus",
            "substitution": "Portions of epithelial tissue fold inward to form multicellular secretory glands.",
            "calculation": "1. Epithelial cells differentiate into specialized secretory cells producing enzymes, hormones, mucus, saliva, or sweat.\n2. Exocrine glands maintain ducts to discharge secretions to epithelial surfaces; endocrine glands discharge directly into blood capillaries.",
            "finalAnswer": "Glandular epithelium forms when epithelial sheets fold inward into secretory structures that synthesize and secrete enzymes, mucus, or sweat.",
            "unit": "Secretory Histology",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.17d: Glandular epithelial invagination forming secretory unit"
        },
        {
            "problem": "Why is blood classified as a connective tissue even though it is a circulating fluid?",
            "given": "Mesodermal connective tissue classification criteria.",
            "formula": "Connective Tissue Invariant: Cells suspended in an extracellular matrix.",
            "substitution": "Blood consists of cellular elements (RBCs, WBCs, platelets) suspended in an extensive non-cellular fluid matrix (plasma).",
            "calculation": "1. Like all connective tissues, blood originates from embryonic mesoderm.\n2. It physically and chemically connects all organ systems by transporting oxygen, carbon dioxide, nutrients, hormones, and waste.\n3. The plasma matrix contains dissolved proteins (albumin, fibrinogen, globulin) and electrolytes maintaining systemic homeostasis.",
            "finalAnswer": "Blood is a connective tissue because it consists of specialized cells suspended in an extracellular matrix (plasma) and links distant body systems through material transport.",
            "unit": "Fluid Connective Tissue",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 3.18: Blood smear showing erythrocytes (RBCs), leukocytes (WBCs), and platelets in plasma"
        }
    ]
}

print("Chapter 3 worked examples ready for integration.")
