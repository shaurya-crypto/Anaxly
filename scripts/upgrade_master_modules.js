const { supabase } = require('./db_helper');

const CH2_ID = 'c0d6c12e-5576-434d-b541-5142fe09f03b';
const CH3_ID = '1053ed93-7167-423b-bdf0-0c73f2b179ff';
const CH4_ID = 'b1a05ff2-8ca8-4d59-b7c7-cc0e1304c3ae';

// ============================================================================
// CHAPTER 2: Cell: The Building Block of Life (Class 9 CBSE Science)
// ============================================================================
const ch2Updates = [
  {
    order_index: 1,
    title: 'The Microscopic Frontier: Cell Discovery, Staining & Onion vs Cheek Cell Labs',
    concept_visuals: [
      {
        concept_title: 'Historical Milestones: Robert Hooke (1665), Antonie van Leeuwenhoek (1674), Robert Brown (1831), J.E. Purkinje (1839)',
        diagram_title: 'Robert Hooke Cork Cells Micrographia 1665',
        diagram_type: 'image',
        image_search_query: 'Robert Hooke Micrographia cork cells 1665',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/f/fe/RobertHookeMicrographia1665.jpg',
        what_to_make: 'Historic 1665 plate from Micrographia showing porous honey-comb cork cells (cella) examined under compound microscope.',
        timing_and_cue: 'Mount historical plate on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/f/fe/RobertHookeMicrographia1665.jpg | Robert Hooke Micrographia 1665 | Original 1665 drawing of honeycomb porous dead cork cells")'
      },
      {
        concept_title: 'Activity 2.1 (Onion Peel Mount): Epidermal peel of Allium cepa, safranin staining, brickwork lattice',
        diagram_title: 'Allium Cepa Epidermal Cells Under Light Microscope',
        diagram_type: 'image',
        image_search_query: 'Onion peel cells under microscope',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/b/b7/Onion_peel_under_a_microscope%28normal%29.jpg',
        what_to_make: 'High-res light micrograph of Allium cepa epidermal cells showing rectangular brickwork lattice, prominent peripheral nuclei, distinct cellulose cell walls, and clear central vacuoles.',
        timing_and_cue: 'Mount authentic micrograph on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/b/b7/Onion_peel_under_a_microscope%28normal%29.jpg | Allium Cepa Onion Peel Micrograph | Regular hexagonal/rectangular brickwork lattice with safranin-stained cellulose walls")'
      },
      {
        concept_title: 'Activity 2.2 (Human Cheek Cell Mount): Buccal mucosa scraping, methylene blue staining, irregular polygonal cells',
        diagram_title: 'Human Buccal Mucosa Cheek Cells Under Microscope',
        diagram_type: 'image',
        image_search_query: 'Human cheek cells methylene blue',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/2/25/Human_Cheek_Cells_%28Methylene_Blue_Stain%29.jpg',
        what_to_make: 'Methylene blue stained squamous epithelial cheek cells displaying irregular polygonal contours, centrally placed spherical nuclei, dense cytoplasm, and complete absence of cell walls.',
        timing_and_cue: 'Mount authentic cheek cell micrograph on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/2/25/Human_Cheek_Cells_%28Methylene_Blue_Stain%29.jpg | Human Cheek Epithelial Cells | Flat squamous polygonal cells with central spherical nuclei and no rigid cell wall")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1 of Concept 1, call write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/f/fe/RobertHookeMicrographia1665.jpg | Robert Hooke Micrographia 1665 | Original 1665 drawing of honeycomb cork cells") AND write_chalkboard(action="draw_flowchart", content="Hooke (1665: Cork) -> Leeuwenhoek (1674: Free pond life) -> Brown (1831: Nucleus) -> Purkinje (1839: Protoplasm) -> Virchow (1855: Omnis cellula e cellula)"). On Step 1 of Concept 2 (Onion Peel), immediately call write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/b/b7/Onion_peel_under_a_microscope%28normal%29.jpg | Onion Peel Micrograph | Brickwork lattice with safranin red walls"). On Step 1 of Concept 3 (Cheek Cells), immediately call write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/2/25/Human_Cheek_Cells_%28Methylene_Blue_Stain%29.jpg | Cheek Epithelial Cells | Polygonal cells with central blue nucleus").
2. PROACTIVE HESITATION RECOVERY: If the student is confused, hesitates, or asks to see another view, immediately call search_and_show_image(query="onion peel epidermal cells microscope", title="High Magnification Onion Peel") or search_and_show_image(query="methylene blue cheek cells", title="Human Cheek Cells Methylene Blue").
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Real-life physical hook (peeling transparent onion skin / inner cheek scraping).
   Stage 2: Strict definition of cell theory, safranin vs methylene blue affinities, and glycerine mounting purpose (prevents desiccation & bubble entrapment at 45 degree angle).
   Stage 3: Common pitfall: Why onion cells have rigid borders (cellulose cell wall) while animal cells do not.
   Stage 4: Chalkboard tabular comparison between Plant (Onion) vs Animal (Cheek) cells.
   Stage 5: Socratic check: "Why do we lower the coverslip at a 45-degree angle with a needle instead of dropping it flat?" HARD STOP: Wait for student response!
   Stage 6: Authentic CBSE Exam Question on staining chemistry and magnification.`
  },
  {
    order_index: 2,
    title: 'Plasma Membrane Dynamics: Fluid Mosaic Architecture, Diffusion & Osmosis Mechanics',
    concept_visuals: [
      {
        concept_title: 'Fluid Mosaic Architecture (Singer & Nicolson 1972): Phospholipid bilayer, hydrophobic tails, hydrophilic heads',
        diagram_title: 'Fluid Mosaic Model of Plasma Membrane',
        diagram_type: 'image',
        image_search_query: 'Fluid mosaic model cell membrane',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/1/10/Fluid_Mosaic.svg',
        what_to_make: 'Bilayer diagram showing hydrophilic polar phosphate heads facing aqueous exterior/interior, hydrophobic fatty acid tails sequestered inside, integral transport proteins, and peripheral glycoprotein receptors.',
        timing_and_cue: 'Mount fluid mosaic diagram on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/1/10/Fluid_Mosaic.svg | Fluid Mosaic Plasma Membrane | Phospholipid bilayer with hydrophobic core and embedded transmembrane transport channels")'
      },
      {
        concept_title: 'Osmosis & Tonicity Mechanics: Hypotonic (turgidity/lysis), Isotonic (dynamic equilibrium), Hypertonic (plasmolysis)',
        diagram_title: 'Osmotic Effects on Animal vs Plant Cells',
        diagram_type: 'image',
        image_search_query: 'Osmosis hypotonic hypertonic isotonic red blood cell plant cell',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/7/76/Osmotic_pressure_on_blood_cells_diagram.svg',
        what_to_make: 'Osmotic tonicity comparison: Hypotonic (Water enters -> Turgid in plants / Swells & Lyses in RBC) -> Isotonic (Net zero flux -> Flaccid/Normal) -> Hypertonic (Water leaves -> Plasmolysed in plants / Crenated in RBC)',
        timing_and_cue: 'Mount tonicity comparison on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/7/76/Osmotic_pressure_on_blood_cells_diagram.svg | Osmotic Pressure on Blood Cells | Hypotonic lysis vs Isotonic equilibrium vs Hypertonic crenation")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount the fluid mosaic membrane diagram: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/1/10/Fluid_Mosaic.svg | Fluid Mosaic Model | Phospholipid bilayer with integral proteins"). When discussing osmosis and tonicity, immediately call write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/7/76/Osmotic_pressure_on_blood_cells_diagram.svg | Osmotic Pressure Diagram | Tonicity behaviors") AND write_chalkboard(action="draw_flowchart", content="Hypotonic: Endosmosis (Turgidity in plants, Hemolysis in RBC) | Isotonic: Equal flux | Hypertonic: Exosmosis (Plasmolysis)").
2. PROACTIVE HESITATION RECOVERY: If the student struggles with water movement or raisin experiment, call search_and_show_image(query="plasmolysis plant cell microscope", title="Plasmolysed Plant Cells") to show shrinking of protoplast away from cell wall.
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Soak dried raisins in water vs concentrated salt solution: "Why do dried raisins swell in pure water but shrink back in sugar syrup?"
   Stage 2: Net solvent movement from high water potential (dilute solution) to low water potential (concentrated solution) across selectively permeable membrane.
   Stage 3: Pitfall: Difference between selectively permeable (plasma membrane) vs freely permeable (cellulose cell wall).
   Stage 4: Lay out the Trio Combo for Activity 2.3 (de-shelled egg in pure water vs concentrated brine solution).
   Stage 5: Check: "If a freshwater protozoan is placed in marine water, will it swell or shrivel?" HARD STOP: Wait for student answer!
   Stage 6: Authentic board exam numerical on osmotic equilibrium and plasmolysis recovery.`
  },
  {
    order_index: 3,
    title: 'The Cell Wall & The Cytoplasmic Operating Engine: Prokaryote vs Eukaryote Architecture',
    concept_visuals: [
      {
        concept_title: 'Plant Cell Wall Ultrastructure: Cellulose microfibrils, hemicellulose, pectin middle lamella',
        diagram_title: 'Plant Cell Wall & Middle Lamella Ultrastructure',
        diagram_type: 'image',
        image_search_query: 'Plant cell wall ultrastructure diagram',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/8/87/Plant_cell_wall_diagram-en.svg',
        what_to_make: 'Layered diagram of plant cell wall: Calcium pectate middle lamella cement, primary cellulose microfibril wall, secondary wall with lignin, and plasmodesmata cytoplasmic bridges.',
        timing_and_cue: 'Mount cell wall ultrastructure on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/8/87/Plant_cell_wall_diagram-en.svg | Plant Cell Wall Ultrastructure | Layered cellulose microfibrils, pectin middle lamella, and plasmodesmata bridges")'
      },
      {
        concept_title: 'Prokaryotic vs Eukaryotic Cellular Architecture: Nucleoid, plasmids, 70S vs 80S ribosomes',
        diagram_title: 'Prokaryotic Bacterium vs Eukaryotic Cell Anatomy',
        diagram_type: 'image',
        image_search_query: 'Prokaryote cell diagram bacterium anatomy',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/9/99/Prokaryote_cell_diagram.svg',
        what_to_make: 'Detailed anatomical comparison: Non-membrane bound nucleoid region, circular naked DNA, capsule, flagella, and 70S ribosomes vs membrane-bound organelle compartmentalization.',
        timing_and_cue: 'Mount prokaryotic architecture on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/9/99/Prokaryote_cell_diagram.svg | Prokaryotic Cellular Architecture | Capsule, flagellum, peptidoglycan wall, 70S ribosomes, and naked circular nucleoid")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount plant cell wall ultrastructure: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/8/87/Plant_cell_wall_diagram-en.svg | Plant Cell Wall Ultrastructure | Primary wall, middle lamella, secondary wall"). For prokaryotes vs eukaryotes, call write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/9/99/Prokaryote_cell_diagram.svg | Bacterial Cell Ultrastructure | Nucleoid, flagella, capsule").
2. PROACTIVE HESITATION RECOVERY: If the student confuses cell wall and cell membrane, immediately call search_and_show_image(query="plant cell wall plasmodesmata transmission electron micrograph", title="Cell Wall TEM Micrograph").
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Everyday hook: "Why can trees stand tall in strong monsoons and high winds without a skeletal backbone, while human bodies would collapse without bones?"
   Stage 2: Strict definition of cellulose fibrils, tensile strength, and turgor pressure resistance preventing bursting during endosmosis.
   Stage 3: Deep dive: The biochemical difference between bacterial peptidoglycan wall vs fungal chitin wall vs plant cellulose wall.
   Stage 4: Whiteboard comparative matrix: Prokaryote (Size 1-10 um, Nucleoid, Single chromosome, No membrane-bound organelles) vs Eukaryote (Size 5-100 um, Nuclear envelope, Multiple chromosomes, Membrane-bound organelles).
   Stage 5: Check: "If an animal cell is placed in hypotonic distilled water, it bursts. Why doesn't an onion peel cell burst?" HARD STOP: Wait for student answer!
   Stage 6: Authentic Class 9 CBSE Board Question on prokaryotic nucleoid vs eukaryotic nucleus.`
  },
  {
    order_index: 4,
    title: 'The Genetic Control Center & The Protein Factory: Nucleus & Endomembrane System',
    concept_visuals: [
      {
        concept_title: 'The Nucleus: Double nuclear envelope, nuclear pore complexes, nucleolus, and chromatin-chromosome condensation',
        diagram_title: 'Cell Nucleus & Nuclear Pore Complex TEM',
        diagram_type: 'image',
        image_search_query: 'Diagram human cell nucleus',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/3/38/Diagram_human_cell_nucleus.svg',
        what_to_make: 'Diagram of nuclear anatomy: Outer and inner membranes, perinuclear cisterna, nuclear pore octagonal complexes, dense fibrillar nucleolus, euchromatin, and heterochromatin fibers.',
        timing_and_cue: 'Mount nucleus architecture on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/3/38/Diagram_human_cell_nucleus.svg | Cell Nucleus Ultrastructure | Double nuclear envelope with octagonal pore complexes, nucleolus, and chromatin thread network")'
      },
      {
        concept_title: 'The Endomembrane Assembly Line: Rough ER (ribosomes, protein synthesis), Smooth ER (lipid synthesis, detoxification), and Golgi Apparatus (glycosylation, packaging, cis/trans polarity)',
        diagram_title: 'Endomembrane Secretory Pathway (Nucleus -> ER -> Golgi -> Vesicle)',
        diagram_type: 'image',
        image_search_query: 'Endomembrane system diagram Golgi ER secretory pathway',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/b/b8/Endomembrane_system_diagram_en.svg',
        what_to_make: 'Secretory transport pipeline: Nuclear envelope continuous with Rough ER, transport vesicles budding from ER, fusing with cis-Golgi cisternae, maturing through medial Golgi, and exiting trans-Golgi to secretory vesicles or lysosomes.',
        timing_and_cue: 'Mount secretory pathway on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/b/b8/Endomembrane_system_diagram_en.svg | Endomembrane Secretory Pathway | Continuous transport from RER to cis-Golgi, trans-Golgi packaging, and secretory vesicles")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount the cell nucleus diagram: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/3/38/Diagram_human_cell_nucleus.svg | Nucleus Anatomy | Nuclear envelope, pores, and nucleolus"). On Concept 2, mount the Endomembrane pipeline: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/b/b8/Endomembrane_system_diagram_en.svg | Endomembrane Assembly Line | RER -> SER -> Golgi Apparatus -> Secretory Vesicles").
2. PROACTIVE HESITATION RECOVERY: If the student confuses chromatin vs chromosomes or cis vs trans faces of Golgi, call search_and_show_image(query="Golgi apparatus transmission electron microscope", title="Golgi Apparatus TEM View").
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Everyday analogy: The cell as a smart mega-factory (Nucleus = CEO office with master blueprint; ER = assembly lines; Golgi = Amazon packaging & logistics hub).
   Stage 2: Strict definition of chromatin (DNA + histone proteins) condensing into rod-shaped chromosomes only during cell division; SER liver detoxification role.
   Stage 3: Common pitfall: Why Camillo Golgi's black reaction (silver nitrate staining) was crucial for discovering the reticular apparatus.
   Stage 4: Lay out the molecular workflow on the chalkboard: DNA -> mRNA transcription -> Ribosome translation on RER -> Vesicle dispatch -> Golgi modification & sorting.
   Stage 5: Socratic check: "What would happen to the life of a cell if there was no Golgi apparatus?" HARD STOP: Wait for student response!
   Stage 6: Authentic board exam numerical & diagram labeling questions.`
  },
  {
    order_index: 5,
    title: 'Powerhouses, Cellular Recycling & Storage Reservoirs: Mitochondria, Plastids, Lysosomes & Vacuoles',
    concept_visuals: [
      {
        concept_title: 'Mitochondria: Double membrane, cristae surface folding, matrix, autonomous 70S ribosomes & circular DNA',
        diagram_title: 'Mitochondrion Cristae & Matrix Ultrastructure',
        diagram_type: 'image',
        image_search_query: 'Animal mitochondrion diagram',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/3/3b/Animal_mitochondrion_diagram_en.svg',
        what_to_make: 'Mitochondrial ultrastructure showing porous outer membrane, deeply folded inner membrane creating cristae sheets, intermembrane space, and central matrix containing F1-ATP synthase particles.',
        timing_and_cue: 'Mount mitochondrion ultrastructure on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/3/3b/Animal_mitochondrion_diagram_en.svg | Mitochondrion Ultrastructure | Folded cristae, matrix, circular DNA, and ATP synthase particles")'
      },
      {
        concept_title: 'Plastids: Chloroplasts (thylakoids, grana, stroma), Chromoplasts (carotenoids/xanthophylls), Leucoplasts (amyloplasts, elaioplasts, aleuroplasts)',
        diagram_title: 'Chloroplast Ultrastructure & Plastid Functional Types',
        diagram_type: 'image',
        image_search_query: 'Chloroplast diagram',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/0/09/Chloroplast_%28standalone_version%29-en.svg',
        what_to_make: 'Chloroplast anatomy with stroma, thylakoid disks stacked into grana columns, intergranal lamellae, and comparison matrix of Leucoplast storage roles.',
        timing_and_cue: 'Mount chloroplast diagram on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/0/09/Chloroplast_%28standalone_version%29-en.svg | Chloroplast Anatomy | Stroma fluid, stacked thylakoid grana, and plastid DNA")'
      },
      {
        concept_title: 'Lysosomes (Suicide Bags, hydrolytic digestive enzymes) & Vacuoles (tonoplast, cell sap turgor pressure)',
        diagram_title: 'Lysosome Autophagy & Cellular Waste Degradation',
        diagram_type: 'image',
        image_search_query: 'Lysosome phagocytosis autophagy diagram',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/e/e6/Phagocytosis2.png',
        what_to_make: 'Phagocytosis and lysosomal degradation showing primary lysosome fusing with damaged organelles or phagocytic vacuoles to form secondary digestive vacuoles.',
        timing_and_cue: 'Mount lysosome phagocytosis on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/e/e6/Phagocytosis2.png | Lysosome Degradation & Phagocytosis | Hydrolytic enzymes digesting cellular debris")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount the mitochondrion diagram: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/3/3b/Animal_mitochondrion_diagram_en.svg | Mitochondrion Anatomy | Cristae, matrix, autonomous DNA"). On Concept 2, mount chloroplast ultrastructure: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/0/09/Chloroplast_%28standalone_version%29-en.svg | Chloroplast Structure | Grana, stroma, thylakoids"). On Concept 3, mount lysosome degradation: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/e/e6/Phagocytosis2.png | Lysosome Degradation | Hydrolytic enzyme action").
2. PROACTIVE HESITATION RECOVERY: If the student asks why mitochondria and chloroplasts are called semi-autonomous, call search_and_show_image(query="endosymbiotic theory mitochondria chloroplast", title="Endosymbiotic Evolution") and explain their own 70S ribosomes and circular DNA.
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Everyday hook: "Why is ATP called the energy currency of the cell, just like rupees in a marketplace?"
   Stage 2: Strict definition of cellular respiration, ATP release, and tonoplast membrane in plant vacuoles maintaining turgidity.
   Stage 3: Why lysosomes are called 'suicide bags' (rupture releases acid hydrolases that digest the host cell when damaged).
   Stage 4: Chalkboard derivation of plastid functional classes: Chromoplast (pigments), Chloroplast (photosynthesis), Leucoplast (starch, oil, protein storage).
   Stage 5: Socratic check: "Which two organelles have their own genetic material and ribosomes?" HARD STOP: Wait for student response!
   Stage 6: Authentic board exam questions on organelle semiautonomy and vacuolar function.`
  },
  {
    order_index: 6,
    title: 'Cell Division Mechanics: Mitosis for Growth and Repair vs Meiosis for Gametogenesis',
    concept_visuals: [
      {
        concept_title: 'Mitosis (Equational Division): Prophase (chromatid condensation, spindle formation), Metaphase (equatorial plate alignment), Anaphase (centromere split, sister chromatid separation), Telophase (nuclear reformation, cytokinesis)',
        diagram_title: 'Mitosis Stages: Prophase, Metaphase, Anaphase, Telophase',
        diagram_type: 'image',
        image_search_query: 'Mitosis Stages diagram',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/c/c9/Mitosis_Stages.svg',
        what_to_make: 'Sequential vector illustration of 4 stages of mitosis: Interphase -> Prophase (chromosomes condense) -> Metaphase (metaphase plate) -> Anaphase (sister chromatids pull to opposite poles) -> Telophase & Cytokinesis (2 identical 2n diploid daughter cells).',
        timing_and_cue: 'Mount mitosis stages on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/c/c9/Mitosis_Stages.svg | Mitosis Equational Division Stages | Prophase -> Metaphase -> Anaphase -> Telophase producing 2 identical 2n daughter cells")'
      },
      {
        concept_title: 'Meiosis (Reductional Division): Meiosis I (homologous chromosome pairing, crossing over, chromosome halving) and Meiosis II (separation of sister chromatids resulting in 4 genetically distinct haploid gametes)',
        diagram_title: 'Meiosis I & II Reductional Division to Haploid Gametes',
        diagram_type: 'image',
        image_search_query: 'Meiosis Stages diagram',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/7/74/Meiosis_Stages.svg',
        what_to_make: 'Two-step reductional division schema: Diploid germ cell (2n) undergoing crossing over in Prophase I, halving to two haploid cells (n) in Meiosis I, then dividing without DNA replication to yield 4 non-identical haploid gametes (n).',
        timing_and_cue: 'Mount meiosis stages on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/7/74/Meiosis_Stages.svg | Meiosis Reductional Division | Meiosis I (2n -> n) and Meiosis II producing 4 diverse haploid gametes")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount the mitosis stages: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/c/c9/Mitosis_Stages.svg | Mitosis Stages | Prophase -> Metaphase -> Anaphase -> Telophase"). On Concept 2, mount meiosis: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/7/74/Meiosis_Stages.svg | Meiosis Stages | Reductional division producing 4 haploid gametes").
2. PROACTIVE HESITATION RECOVERY: If the student confuses diploid (2n) vs haploid (n) chromosome numbers, call write_chalkboard(action="draw_flowchart", content="Mitosis: Parent (2n=46) -> 2 Daughters (2n=46 each) || Meiosis: Parent (2n=46) -> Meiosis I (n=23) -> 4 Gametes (n=23 each)").
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Everyday hook: "When you skin your knee, how do new skin cells appear with the exact same genetic code, while sperms and eggs have half the chromosome count?"
   Stage 2: Strict definition of equational division (mitosis: identical 2n daughter cells) vs reductional division (meiosis: halving chromosome count to n).
   Stage 3: Common pitfall: Why cytokinesis in plant cells requires a cell plate from Golgi vesicles, whereas animal cells form a cleavage furrow.
   Stage 4: Chalkboard comparative matrix: Mitosis (Growth, repair, 1 division, 2 identical diploid cells) vs Meiosis (Gametogenesis, crossing over, 2 divisions, 4 diverse haploid cells).
   Stage 5: Socratic check: "If a human skin cell with 46 chromosomes divides by mitosis, how many chromosomes will each daughter cell have?" HARD STOP: Wait for student response!
   Stage 6: Authentic board exam numerical & stage identification questions.`
  },
  {
    order_index: 7,
    title: 'Master Problem Solver & Comprehensive Chapter Review: High-Yield NCERT Solutions & Diagnostic Evaluation',
    concept_visuals: [
      {
        concept_title: 'Complete Cell Architecture Synthesis: From Molecular Ingestion to Cellular Reproduction',
        diagram_title: 'Cell Biology Master Synthesis Flowchart',
        diagram_type: 'flowchart',
        image_search_query: 'Cell biology master flowchart',
        what_to_make: 'Complete classification tree: Cell -> Cell Wall / Plasma Membrane | Nucleus (Chromatin/Pores) | Cytoplasm -> Organelles [Double Membrane: Mitochondria, Chloroplast | Single Membrane: ER, Golgi, Lysosome, Vacuole | Non-membrane: Ribosomes]',
        timing_and_cue: 'Mount master synthesis tree on Step 1: write_chalkboard(action="draw_flowchart", content="CELL ARCHITECTURE: Membrane/Wall | Nucleus (DNA/Pores) | Organelles: Double Membrane (Mitochondria, Chloroplast) | Single Membrane (ER, Golgi, Lysosome) | Non-Membrane (Ribosomes)")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount the Master Synthesis Tree: write_chalkboard(action="draw_flowchart", content="CELL MASTER TAXONOMY: Boundary (Wall, Membrane) || Nucleus (DNA, Chromatin) || Endomembrane (ER, Golgi, Lysosome) || Energetics (Mitochondria, Plastid) || Division (Mitosis, Meiosis)").
2. TEXTBOOK EXERCISE RESOLUTION: Solve all 10 NCERT textbook exercise questions step-by-step:
   - Q1: Comparison between plant cell and animal cell.
   - Q2: How does a prokaryotic cell differ from a eukaryotic cell?
   - Q3: What would happen if the plasma membrane ruptures or breaks down?
   - Q4: What would happen to the life of a cell if there was no Golgi apparatus?
   - Q5: Which organelle is known as the powerhouse of the cell and why?
   - Q6: Where do the lipids and proteins constituting the cell membrane get synthesised?
   - Q7: How does an Amoeba obtain its food? (Endocytosis/phagocytosis).
   - Q8: What is osmosis?
   - Q9: Potato Osmometer Experiment with boiled and unboiled potatoes.
   - Q10: Which type of cell division is required for growth and repair, and which for gamete formation?
3. HARD STOP after each problem to confirm student understanding before concluding.`
  }
];

// ============================================================================
// CHAPTER 3: Tissues in Action (Class 9 CBSE Science)
// ============================================================================
const ch3Updates = [
  {
    order_index: 1,
    title: 'Architectural Divergence & The Dividing Engines: Plant vs Animal Histology & Meristematic Tissues',
    concept_visuals: [
      {
        concept_title: 'Architectural Divergence: Stationary plant demands (dead mechanical support, localized continuous meristems) vs Motile animal demands (living flexible tissues, uniform systemic growth)',
        diagram_title: 'Plant vs Animal Histology Master Divergence Flowchart',
        diagram_type: 'flowchart',
        image_search_query: 'Plant tissue types classification',
        what_to_make: 'Flowchart: Plant Histology (Stationary -> Dead supportive tissues, localized meristematic growth) vs Animal Histology (Active locomotion -> Living tissues, uniform systemic growth).',
        timing_and_cue: 'Mount divergence flowchart on Step 1: write_chalkboard(action="draw_flowchart", content="TISSUE DIVERGENCE: Plants (Stationary -> Dead mechanical support, Localized growth) vs Animals (Motile -> Uniform living tissues, Systemic growth)")'
      },
      {
        concept_title: 'Meristematic Tissues: Apical meristem (root/shoot apex length), Intercalary meristem (internodal elongation in monocots), and Lateral meristem / Cambium (secondary radial girth increase)',
        diagram_title: 'Root & Shoot Apical Meristem Microscopic View',
        diagram_type: 'image',
        image_search_query: 'Root Apical Meristem cell light microscope',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/7/7f/Root_Apical_Meristem_cell.jpg',
        what_to_make: 'High-res light micrograph of root/stem apical meristem showing dense cytoplasm, prominent spherical nuclei, thin cellulose walls, and complete absence of vacuoles due to rapid division.',
        timing_and_cue: 'Mount apical meristem micrograph on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/7/7f/Root_Apical_Meristem_cell.jpg | Root Apical Meristem Micrograph | Actively dividing isodiametric cells with dense protoplasm and no central vacuoles")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, call write_chalkboard(action="draw_flowchart", content="TISSUE DIVERGENCE: Plants (Stationary -> Dead mechanical support, Localized growth) vs Animals (Motile -> Uniform living tissues, Systemic growth)"). For Meristems, immediately mount write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/7/7f/Root_Apical_Meristem_cell.jpg | Root Apical Meristem | Active isodiametric division zone").
2. PROACTIVE HESITATION RECOVERY: If the student asks why meristematic cells lack vacuoles, immediately call search_and_show_image(query="apical meristem shoot tip coleus", title="Shoot Apical Meristem L.S.") and explain that active division requires no nutrient storage space.
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Everyday hook: "Why does grass keep growing taller after being cut by a lawnmower, while an animal limb cannot regenerate if trimmed?"
   Stage 2: Strict definition of differentiation: Loss of division capacity to assume specific permanent shape, size, and function.
   Stage 3: Location and role of Apical (length), Intercalary (internode), and Lateral (cambium/girth) meristems.
   Stage 4: Chalkboard derivation of the 3 Meristems with their growth vectors.
   Stage 5: Check: "Why do meristematic cells have thin cellulose walls and lack vacuoles?" HARD STOP: Wait for student answer!
   Stage 6: Authentic board exam question on onion root tip experiment (Activity 3.1).`
  },
  {
    order_index: 2,
    title: 'Simple Permanent Plant Tissues: Parenchyma, Chlorenchyma, Aerenchyma, Collenchyma & Sclerenchyma',
    concept_visuals: [
      {
        concept_title: 'Parenchyma & Modifications: Thin primary cellulose walls, intercellular spaces, storage; Chlorenchyma (mesophyll chloroplasts); Aerenchyma (air cavities in hydrophytes)',
        diagram_title: 'Plant Cell Types: Parenchyma, Collenchyma, Sclerenchyma',
        diagram_type: 'image',
        image_search_query: 'Plant cell types diagram',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/e/e7/Plant_cell_types.svg',
        what_to_make: 'Vector diagram illustrating thin-walled parenchyma with intercellular spaces, angular-thickened collenchyma, and thick lignified sclerenchyma.',
        timing_and_cue: 'Mount plant cell types on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/e/e7/Plant_cell_types.svg | Plant Simple Permanent Tissues | Parenchyma vs Collenchyma vs Sclerenchyma")'
      },
      {
        concept_title: 'Collenchyma: Living mechanical tissue, localized pectin-cellulose corner thickenings, flexibility without breakage in petioles and climbers',
        diagram_title: 'Collenchyma Corner Thickenings in Petiole Cross Section',
        diagram_type: 'image',
        image_search_query: 'Plant cell type collenchyma',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/9/97/Plant_cell_type_collenchyma.png',
        what_to_make: 'Transverse section showing living elongated collenchyma cells with characteristic pectin thickening at corners, lack of intercellular spaces, and tensile elasticity.',
        timing_and_cue: 'Mount collenchyma micrograph on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/9/97/Plant_cell_type_collenchyma.png | Collenchyma Cross Section | Pectin-cellulose corner wall thickenings conferring tensile elasticity to stems and petioles")'
      },
      {
        concept_title: 'Sclerenchyma: Dead mechanical tissue, uniformly thickened lignified secondary walls, narrow obliterated lumens; Fibres vs Sclereids/Stone cells',
        diagram_title: 'Sclerenchyma Lignified Fibres and Sclereids',
        diagram_type: 'image',
        image_search_query: 'Plant cell type sclerenchyma fibers',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/0/07/Plant_cell_type_sclerenchyma_fibers.png',
        what_to_make: 'Microscopic section showing dead sclerenchyma fibers with lignified secondary walls, pits, and obliterated lumens (coconut husk / pear stone cells).',
        timing_and_cue: 'Mount sclerenchyma micrograph on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/0/07/Plant_cell_type_sclerenchyma_fibers.png | Sclerenchyma Lignified Fibres | Dead cells with thick secondary walls and narrow lumen")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount the overview: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/e/e7/Plant_cell_types.svg | Simple Permanent Plant Tissues | Parenchyma, Collenchyma, Sclerenchyma"). On Concept 2 (Collenchyma), mount write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/9/97/Plant_cell_type_collenchyma.png | Collenchyma | Pectin corner thickenings"). On Concept 3 (Sclerenchyma), mount write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/0/07/Plant_cell_type_sclerenchyma_fibers.png | Sclerenchyma Fibres | Thick lignified dead walls").
2. PROACTIVE HESITATION RECOVERY: If the student confuses collenchyma with chlorenchyma or sclerenchyma, call search_and_show_image(query="coconut husk sclerenchyma fibers microscope", title="Coconut Husk Sclerenchyma").
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Everyday hook: "Why can you bend a green tree twig without snapping it, but pulling dry coconut husk feels like unravelling tough metallic rope?"
   Stage 2: Strict definition of primary vs secondary wall, lignin chemical cement, and pectin plasticity.
   Stage 3: Anatomical comparison: Parenchyma (living, thin, unspecialized) vs Collenchyma (living, pectin corners, flexible) vs Sclerenchyma (dead, lignified, rigid).
   Stage 4: Chalkboard 3-column table comparing Living Status, Wall Composition, Intercellular Spaces, and Biological Function.
   Stage 5: Socratic check: "Why do aquatic plants like lotus float effortlessly on the water surface?" (Aerenchyma buoyancy). HARD STOP: Wait for student response!
   Stage 6: Authentic board exam numerical & identification questions.`
  },
  {
    order_index: 3,
    title: 'Vascular Transport Pipelines: Complex Permanent Tissues (Xylem vs Phloem)',
    concept_visuals: [
      {
        concept_title: 'Xylem Transport Engine: Tracheids (primitive spindle conducting cells), Vessels (perforated continuous conduits), Xylem Parenchyma (radial living storage), and Xylem Fibres (lignified mechanical support)',
        diagram_title: 'Xylem Tracheids & Vessel Elements Longitudinal Section',
        diagram_type: 'image',
        image_search_query: 'Xylem cells diagram',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/c/ce/Xylem_cells.svg',
        what_to_make: 'Vector diagram of xylem: Spindle-shaped tracheids with bordered pits, cylindrical perforated vessel elements forming continuous pipelines, and living xylem parenchyma.',
        timing_and_cue: 'Mount xylem pipeline on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/c/ce/Xylem_cells.svg | Xylem Vascular Pipeline | Tracheids with bordered pits and vessel conduits for unidirectional water and mineral sap ascent")'
      },
      {
        concept_title: 'Phloem Translocation Engine: Sieve Tubes (enucleated living conducting cells with porous sieve plates), Companion Cells (nucleated metabolic drivers with plasmodesmata), Phloem Parenchyma, and Phloem Fibres (Bast fibres)',
        diagram_title: 'Phloem Sieve Tubes & Companion Cells Microscopic View',
        diagram_type: 'image',
        image_search_query: 'Phloem cells diagram',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/e/e2/Phloem_cells.svg',
        what_to_make: 'Detailed phloem diagram: Sieve tube elements with perforated sieve plates, nucleated companion cells, and plasmodesmata cytoplasmic bridges.',
        timing_and_cue: 'Mount phloem translocation on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/e/e2/Phloem_cells.svg | Phloem Translocation Architecture | Sieve tube conduits with perforated sieve plates driven by nucleated companion cells")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount the Xylem pipeline: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/c/ce/Xylem_cells.svg | Xylem Elements | Tracheids, vessels, parenchyma, fibres"). On Concept 2, mount Phloem: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/e/e2/Phloem_cells.svg | Phloem Elements | Sieve tubes, companion cells, sieve plates").
2. PROACTIVE HESITATION RECOVERY: If the student confuses living vs dead elements, call write_chalkboard(action="draw_flowchart", content="XYLEM: 3 Dead (Tracheids, Vessels, Fibres) + 1 Living (Parenchyma) || PHLOEM: 3 Living (Sieve Tubes, Companion, Parenchyma) + 1 Dead (Bast Fibres)").
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Everyday hook: "How does a 100-meter-tall Redwood tree pump tons of water up to its crown leaves without an electric heart pump?"
   Stage 2: Strict definition of xylem unidirectional sap ascent (transpiration pull + capillary suction) vs phloem bidirectional translocation (sucrose mass flow driven by ATP).
   Stage 3: Deep dive: Why sieve tube elements lose their nucleus at maturity yet remain metabolically alive (driven by adjacent companion cells via plasmodesmata).
   Stage 4: Chalkboard master comparative table: Xylem (Water/minerals, Unidirectional, Dead at maturity, Lignin) vs Phloem (Photosynthetic sugars/amino acids, Bidirectional, Living, Cellulose).
   Stage 5: Socratic check: "Which is the only living element in xylem, and which is the only dead element in phloem?" HARD STOP: Wait for student answer!
   Stage 6: Authentic board exam questions on girdling experiments and vascular bundle anatomy.`
  },
  {
    order_index: 4,
    title: 'Animal Boundary Protectors & Fluid Connective Transport: Epithelia & Blood Histology',
    concept_visuals: [
      {
        concept_title: 'Epithelial Tissue Morphologies: Simple Squamous (diffusion barrier), Stratified Squamous (keratinized wear/tear), Cuboidal (glandular secretion/absorption), Columnar (brush border microvilli), and Ciliated (mucus wave)',
        diagram_title: 'Epithelial Tissue Morphologies & Basement Membrane',
        diagram_type: 'image',
        image_search_query: 'Summary of Epithelial Tissue Cells',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/6/64/423_Table_04_02_Summary_of_Epithelial_Tissue_CellsN.jpg',
        what_to_make: 'Histological classification of epithelia: Squamous pavement tiles, cuboidal cubes with central spherical nuclei, tall columnar pillars, ciliated columnar lining, and stratified layers over basement membrane.',
        timing_and_cue: 'Mount epithelial morphologies on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/6/64/423_Table_04_02_Summary_of_Epithelial_Tissue_CellsN.jpg | Epithelial Tissue Morphologies | Squamous, cuboidal, columnar, and ciliated types on non-cellular basement membrane")'
      },
      {
        concept_title: 'Fluid Connective Tissue: Blood (liquid plasma matrix, biconcave enucleated RBCs/erythrocytes, phagocytic/antibody WBCs/leukocytes, thrombocyte platelets) and Lymph (interstitial fluid filtration)',
        diagram_title: 'Human Peripheral Blood Smear Microscopic View',
        diagram_type: 'image',
        image_search_query: 'Human blood smear peripheral blood film microscope',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/c/c6/Blood_film_01.jpg',
        what_to_make: 'High-res light micrograph of human peripheral blood smear: Biconcave pink erythrocytes, multilobed neutrophils, lymphocytes, and tiny thrombocyte platelets suspended in fluid matrix.',
        timing_and_cue: 'Mount blood smear micrograph on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/c/c6/Blood_film_01.jpg | Human Blood Smear Micrograph | Biconcave enucleated RBCs, polymorphonuclear WBCs, and platelets in fluid plasma")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount epithelial morphologies: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/6/64/423_Table_04_02_Summary_of_Epithelial_Tissue_CellsN.jpg | Epithelial Tissues | Squamous, Cuboidal, Columnar, Ciliated"). On Concept 2, mount the blood smear: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/c/c6/Blood_film_01.jpg | Blood Smear Micrograph | Erythrocytes, Leukocytes, Platelets in Plasma").
2. PROACTIVE HESITATION RECOVERY: If the student confuses squamous epithelium with cuboidal or questions why blood is classified as a connective tissue, call search_and_show_image(query="blood smear neutrophils erythrocytes platelets", title="Blood Cells High Magnification") and explain its mesodermal embryonic origin and living cells dispersed in an extracellular matrix.
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Everyday hook: "Why does rubbing your hands together peel off microscopic dead skin layers without causing bleeding, while a shallow needle prick immediately bleeds?"
   Stage 2: Strict definition of epithelial avascularity, basement membrane (collagen + glycoproteins), and connective tissue definition (cells widely spaced in an intercellular matrix).
   Stage 3: Specific locations: Squamous (alveoli, mouth lining), Cuboidal (kidney tubules, salivary glands), Columnar (stomach, intestines), Ciliated (respiratory bronchioles, fallopian tubes).
   Stage 4: Chalkboard tabular breakdown of Blood composition: Fluid Matrix (55% Plasma: Water, albumin, fibrinogen, mineral ions) + Formed Elements (45%: RBCs 5-5.5M/uL, WBCs 6000-8000/uL, Platelets 1.5-3.5L/uL).
   Stage 5: Socratic check: "Why is blood classified as a connective tissue even though it is liquid?" HARD STOP: Wait for student response!
   Stage 6: Authentic board exam questions on epithelial lining matching and blood function.`
  },
  {
    order_index: 5,
    title: 'Supportive Framework & Musculoskeletal Ties: Bone, Cartilage, Ligaments, Tendons, Areolar & Adipose Histology',
    concept_visuals: [
      {
        concept_title: 'Skeletal Connective Tissues: Bone (rigid calcium-phosphate matrix, osteocytes in concentric Haversian canal osteons) vs Cartilage (chondrocytes in lacunae, solid flexible chondroitin-sulphate matrix)',
        diagram_title: 'Compact Bone Osteon vs Hyaline Cartilage Histology',
        diagram_type: 'image',
        image_search_query: 'Compact bone histology osteon',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/5/5d/Compact_bone_histology_2014.jpg',
        what_to_make: 'Histological micrograph showing concentric Haversian lamellae with osteocytes inside lacunae, central neurovascular canal, and contrasting hyaline cartilage with chondrocyte clusters.',
        timing_and_cue: 'Mount bone osteon histology on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/5/5d/Compact_bone_histology_2014.jpg | Compact Bone Osteon Histology | Concentric Haversian lamellae with osteocyte lacunae and central canal")'
      },
      {
        concept_title: 'Dense Regular & Packaging Connective Tissues: Tendons (muscle-to-bone, tough inextensible collagen cords) vs Ligaments (bone-to-bone, elastic flexible yellow elastin bands); Areolar & Adipose tissues',
        diagram_title: 'Tendon vs Ligament Molecular Architecture',
        diagram_type: 'image',
        image_search_query: 'Comparison of molecular structure tendon ligament',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Comparison_of_molecular_structure%2C_fibers_organization_and_composition_of_tendon_and_ligament.png',
        what_to_make: 'Structural diagram illustrating dense parallel collagen bundles in inelastic tendons vs intersecting elastic fibres in flexible ligaments.',
        timing_and_cue: 'Mount tendon vs ligament on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/8/8f/Comparison_of_molecular_structure%2C_fibers_organization_and_composition_of_tendon_and_ligament.png | Tendon vs Ligament Architecture | Inelastic parallel collagen cords vs flexible elastin bands")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount bone osteon histology: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/5/5d/Compact_bone_histology_2014.jpg | Bone Osteon Histology | Haversian canals and osteocytes"). On Concept 2, mount tendon vs ligament: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/8/8f/Comparison_of_molecular_structure%2C_fibers_organization_and_composition_of_tendon_and_ligament.png | Tendon vs Ligament | Collagen vs Elastin architecture").
2. PROACTIVE HESITATION RECOVERY: If the student confuses Tendon vs Ligament, call write_chalkboard(action="draw_flowchart", content="TENDON: Muscle to Bone | Inelastic Collagen | Great tensile strength || LIGAMENT: Bone to Bone | Flexible Elastin | Prevents dislocation").
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Everyday hook: "Why can you bend the tip of your ear and nose without snapping, but your forearm bones are completely rigid?"
   Stage 2: Strict definition of hydroxyapatite calcium-phosphate mineralized matrix in bone vs chondroitin-protein flexible matrix in cartilage.
   Stage 3: Pitfall: Difference between sprain (ligament overstretching) vs strain (tendon/muscle tear).
   Stage 4: Lay out the Connective Tissue Family on chalkboard: Fluid (Blood, Lymph), Skeletal (Bone, Cartilage), Dense Regular (Tendon, Ligament), Loose Packaging (Areolar, Adipose).
   Stage 5: Socratic check: "Why do obese individuals feel warmer in winter compared to thin individuals?" (Adipose subcutaneous fat thermal insulation). HARD STOP: Wait for student response!
   Stage 6: Authentic CBSE Board Exam Questions on joint histology and matrix composition.`
  },
  {
    order_index: 6,
    title: 'Contractile Machinery & Neural Signaling Networks: Muscular & Nervous Histology',
    concept_visuals: [
      {
        concept_title: 'Muscular Tissue Morphologies: Striated/Skeletal (voluntary, syncytial multinucleated, unbranched, alternating dark/light striations), Smooth/Visceral (involuntary, spindle uninucleate, unstriated), and Cardiac (involuntary, branched, intercalated discs)',
        diagram_title: 'Skeletal, Smooth & Cardiac Muscle Histology Comparison',
        diagram_type: 'image',
        image_search_query: 'Muscle Tissue types diagram histology',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/f/f9/Muscle_Tissue_%281%29.svg',
        what_to_make: 'Tri-panel comparative vector diagram: Striated cylindrical fibers with peripheral nuclei, smooth fusiform spindle cells with central oval nucleus, and cardiac branched fibers with intercalated discs.',
        timing_and_cue: 'Mount muscle histology on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/f/f9/Muscle_Tissue_%281%29.svg | Muscle Tissue Comparison | Striated (voluntary) vs Smooth (visceral) vs Cardiac (intercalated discs)")'
      },
      {
        concept_title: 'Nervous Tissue Architecture: Multipolar neuron anatomy (cyton/cell body, Nissl granules, dendrites, axon with myelin sheath, nodes of Ranvier, synaptic terminal boutons) and neuromuscular junction',
        diagram_title: 'Neuron Anatomy & Synaptic Transmission Pathway',
        diagram_type: 'image',
        image_search_query: 'Anatomy and physiology of animals Motor neuron',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/5/5f/Anatomy_and_physiology_of_animals_Motor_neuron_jp.png',
        what_to_make: 'Detailed motor neuron diagram: Dendrites receiving chemical signals, cyton processing, axon hillock action potential triggering, myelin sheath insulation, nodes of Ranvier, and terminal synaptic bulbs.',
        timing_and_cue: 'Mount neuron anatomy on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/5/5f/Anatomy_and_physiology_of_animals_Motor_neuron_jp.png | Motor Neuron Anatomy | Dendrites, soma with Nissl granules, myelinated axon with nodes of Ranvier, and synaptic terminals")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount the muscle comparison: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/f/f9/Muscle_Tissue_%281%29.svg | Muscle Histology | Striated vs Smooth vs Cardiac"). On Concept 2, mount neuron anatomy: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/5/5f/Anatomy_and_physiology_of_animals_Motor_neuron_jp.png | Motor Neuron Architecture | Dendrite -> Soma -> Axon -> Synapse").
2. PROACTIVE HESITATION RECOVERY: If the student confuses striated vs cardiac muscle or impulse transmission across synapses, call search_and_show_image(query="intercalated discs cardiac muscle histology microscope", title="Cardiac Intercalated Discs").
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Everyday hook: "How can your heart beat continuously for 80 years without fatigue, while your arm muscles cramp up after holding a heavy bag for 10 minutes?"
   Stage 2: Strict definition of contractile proteins (actin and myosin sliding filament mechanism) and action potential transmission across neurotransmitter synapses.
   Stage 3: Morphological comparison: Skeletal (cylindrical, unbranched, multinucleate), Smooth (spindle, unbranched, uninucleate), Cardiac (cylindrical, branched, uninucleate, intercalated discs for synchronized contraction).
   Stage 4: Chalkboard diagrammatic breakdown of Neuron impulse conduction: Stimulus -> Dendrite -> Cyton -> Axon -> Axon Terminal -> Synaptic Cleft (Neurotransmitter) -> Next Dendrite.
   Stage 5: Socratic check: "Which specific muscle tissue never rests or fatigues throughout an organism's lifetime, and what feature enables its rhythmic synchronous contraction?" HARD STOP: Wait for student response!
   Stage 6: Authentic board exam questions on neuron labeling and muscle tissue distinction.`
  },
  {
    order_index: 7,
    title: 'Master Problem Solver & Comprehensive Histology Taxonomy: Complete NCERT Solutions & Diagnostic Assessment',
    concept_visuals: [
      {
        concept_title: 'Comprehensive Histology Taxonomy: Unified Plant and Animal Tissue Hierarchy',
        diagram_title: 'Plant and Animal Histology Master Classification Tree',
        diagram_type: 'flowchart',
        image_search_query: 'Histology master classification flowchart',
        what_to_make: 'Comprehensive branching flowchart unifying all 14 tissue classes taught across the chapter.',
        timing_and_cue: 'Mount master histology taxonomy on Step 1: write_chalkboard(action="draw_flowchart", content="HISTOLOGY MASTER TAXONOMY: Plant [Meristematic (Apical, Lateral, Intercalary) | Permanent (Simple: Parenchyma, Collenchyma, Sclerenchyma; Complex: Xylem, Phloem)] || Animal [Epithelial | Connective (Fluid, Skeletal, Proper) | Muscular (Striated, Smooth, Cardiac) | Nervous]")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount the Master Histology Taxonomy: write_chalkboard(action="draw_flowchart", content="HISTOLOGY MASTER TAXONOMY: Plant [Meristematic | Permanent: Simple & Complex] || Animal [Epithelial | Connective: Blood, Bone, Cartilage, Tendon | Muscular: Striated, Smooth, Cardiac | Nervous]").
2. TEXTBOOK EXERCISE RESOLUTION: Solve all 15 textbook questions step-by-step:
   - Q1: Define the term tissue.
   - Q2: How many types of elements together make up the xylem tissue? Name them.
   - Q3: How are simple tissues different from complex tissues in plants?
   - Q4: Differentiate between parenchyma, collenchyma and sclerenchyma on the basis of their cell wall.
   - Q5: What are the functions of the stomata?
   - Q6: Diagrammatically show the difference between the three types of muscle fibres.
   - Q7: What is the specific function of the cardiac muscle?
   - Q8: Differentiate between striated, unstriated and cardiac muscles on the basis of their structure and site/location in the body.
   - Q9: Draw a labelled diagram of a neuron.
   - Q10: Name the following: tissue forming the inner lining of mouth, tissue connecting muscle to bone, tissue transporting food in plants, tissue storing fat, connective tissue with fluid matrix, tissue in brain.
   - Q11: Identify the type of tissue in: skin, bark of tree, bone, lining of kidney tubule, vascular bundle.
   - Q12: Name the regions in which parenchyma tissue is present.
   - Q13: What is the role of epidermis in plants?
   - Q14: How does the cork act as a protective tissue?
   - Q15: Complete the summary flowchart of plant tissues.
3. HARD STOP after each problem to confirm student understanding before concluding.`
  }
];

// ============================================================================
// CHAPTER 4: Describing Motion Around Us (Class 9 CBSE Science - Kinematics)
// ============================================================================
const ch4Updates = [
  {
    order_index: 1,
    title: 'Frame of Reference, Relative Motion & The 1D Coordinate Line: Distance vs Displacement',
    concept_visuals: [
      {
        concept_title: 'Reference Frame & Origin: Coordinate axes, observer state of rest or motion, one-dimensional spatial line',
        diagram_title: '1D Reference Coordinate Axis with Origin O',
        diagram_type: 'graph',
        interactive_math_formula: '0',
        what_to_make: 'Linear coordinate axis showing origin O (x=0), positive direction to the right (+x), negative to the left (-x), and spatial position coordinates of a moving particle.',
        timing_and_cue: 'Mount coordinate line: plot_mathematical_graph(formula="0", domain="[-10, 10]", title="1D Reference Coordinate Axis with Origin O")'
      },
      {
        concept_title: 'Distance (Scalar Total Path Length) vs Displacement (Vector Shortest Distance Chord with Direction)',
        diagram_title: 'Distance vs Net Displacement Function',
        diagram_type: 'graph',
        interactive_math_formula: 'abs(x)',
        what_to_make: 'Mathematical graph showing absolute distance path length abs(x) vs signed displacement coordinate x demonstrating that Distance >= |Displacement| always.',
        timing_and_cue: 'Mount distance vs displacement graph: plot_mathematical_graph(formula="abs(x)", domain="[-6, 6]", title="Distance vs Net Displacement Function")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount the 1D Coordinate Axis using plot_mathematical_graph(formula="0", domain="[-10, 10]", title="1D Reference Coordinate Axis with Origin O"). On Concept 2, plot the scalar vs vector distance graph: plot_mathematical_graph(formula="abs(x)", domain="[-6, 6]", title="Distance vs Displacement Function").
2. TEXTBOOK IN-TEXT ACTIVITY RESOLUTION: Co-solve Activity 4.1 (Passenger in moving bus: Fellow passengers at rest relative to bus frame, but trees moving backward relative to road frame) and Activity 4.2 (Farmer walking along the boundary of a square field of side 10m in 40s. Calculate displacement at 2m20s = 140s).
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Everyday hook: "If you walk 5 meters east and then 5 meters west, how far have your feet walked, and how far have you actually displaced from where you started?"
   Stage 2: Strict definition of Scalar (magnitude only: Distance in meters) vs Vector (magnitude + direction: Displacement in meters with unit vector/sign).
   Stage 3: Fundamental Invariant: Distance >= |Displacement|; Displacement can be positive, negative, or zero, but distance traveled can NEVER be negative or zero for moving bodies.
   Stage 4: Whiteboard derivation: Farmer problem step-by-step (Total time = 140s; Rounds = 140/40 = 3.5 rounds; Position = opposite corner; Displacement = sqrt(10^2 + 10^2) = 10*sqrt(2) = 14.14 m).
   Stage 5: Socratic check: "Can an object have zero displacement even after covering a massive distance of 500 kilometers?" HARD STOP: Wait for student response!
   Stage 6: Authentic board exam numerical on circular track diameter and displacement.`
  },
  {
    order_index: 2,
    title: 'Rate of Motion: Speed, Velocity & The Calculus of Acceleration',
    concept_visuals: [
      {
        concept_title: 'Speed (Scalar Rate) vs Velocity (Vector Rate) & Average Metrics (Total Distance / Total Time vs Net Displacement / Total Time)',
        diagram_title: 'Linear Velocity Curve v = 2t',
        diagram_type: 'graph',
        interactive_math_formula: '2*x',
        what_to_make: 'Linear velocity graph plotting v = 2t showing instantaneous rate of change of position with respect to time.',
        timing_and_cue: 'Mount velocity graph: plot_mathematical_graph(formula="2*x", domain="[0, 10]", title="Linear Velocity Curve v = 2t")'
      },
      {
        concept_title: 'Acceleration (Rate of Change of Velocity: a = (v - u) / t): Positive acceleration, negative acceleration (retardation/deceleration), and zero acceleration in uniform motion',
        diagram_title: 'Accelerating Position-Time Parabola s = 0.5 a t^2',
        diagram_type: 'graph',
        interactive_math_formula: '0.5*x^2',
        what_to_make: 'Parabolic curve plotting position s = 0.5 * 1 * t^2 representing constant positive acceleration a = 1 m/s^2.',
        timing_and_cue: 'Mount acceleration parabola: plot_mathematical_graph(formula="0.5*x^2", domain="[0, 8]", title="Accelerating Position-Time Parabola s = 0.5 a t^2")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount the linear velocity graph: plot_mathematical_graph(formula="2*x", domain="[0, 10]", title="Linear Velocity Curve v = 2t"). On Concept 2, plot the acceleration parabola: plot_mathematical_graph(formula="0.5*x^2", domain="[0, 8]", title="Accelerating Position-Time Parabola s = 0.5 a t^2").
2. PROACTIVE HESITATION RECOVERY: If the student confuses average speed with average velocity, call write_chalkboard(action="draw_flowchart", content="Average Speed = Total Distance / Total Time (Scalar, always > 0) || Average Velocity = Net Displacement / Total Time (Vector, can be zero or negative)").
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Everyday hook: Look at your car dashboard: "What does the speedometer measure (instantaneous speed) vs what does the odometer count (total odometer distance)?"
   Stage 2: Mathematical definition of acceleration: a = (v - u) / t in SI units of m/s^2. Sign convention: +a along direction of motion (speeding up), -a opposite to motion (retardation).
   Stage 3: Common pitfall: Why uniform speed in a circle is STILL accelerated motion (because velocity vector changes direction continuously).
   Stage 4: Chalkboard worked numerical for Abdul driving to school: v1 = 20 km/h, v2 = 30 km/h; Average speed = 2*v1*v2 / (v1 + v2) = 2*20*30 / 50 = 24 km/h (Harmonic mean, NOT arithmetic mean 25 km/h!).
   Stage 5: Socratic check: "Why is average speed 24 km/h and NOT 25 km/h?" HARD STOP: Wait for student response!
   Stage 6: Authentic CBSE numerical on bus slowing down from 80 km/h to 60 km/h in 5 seconds.`
  },
  {
    order_index: 3,
    title: 'The Visual Language of Kinematics: Distance-Time & Velocity-Time Graphs',
    concept_visuals: [
      {
        concept_title: 'Distance-Time (s-t) Graphs: Slope represents instantaneous speed (Delta s / Delta t); Straight line = uniform motion; Curved line = accelerated motion',
        diagram_title: 'Position-Time (s-t) Uniform Motion Line',
        diagram_type: 'graph',
        interactive_math_formula: '3*x',
        what_to_make: 'Linear position-time graph with slope m = 3 m/s illustrating constant speed with zero acceleration.',
        timing_and_cue: 'Mount s-t graph: plot_mathematical_graph(formula="3*x", domain="[0, 10]", title="Position-Time (s-t) Uniform Motion Line")'
      },
      {
        concept_title: 'Velocity-Time (v-t) Graphs: Slope represents acceleration (Delta v / Delta t); Area under the curve represents distance/displacement covered',
        diagram_title: 'Velocity-Time (v-t) Graph with Slope=Acceleration & Area=Displacement',
        diagram_type: 'graph',
        interactive_math_formula: '2*x + 4',
        what_to_make: 'Velocity-time curve v = 4 + 2t starting from initial velocity u = 4 m/s with slope a = 2 m/s^2 and shaded trapezium area under curve.',
        timing_and_cue: 'Mount v-t graph: plot_mathematical_graph(formula="2*x + 4", domain="[0, 8]", title="Velocity-Time (v-t) Graph with Slope=Acceleration & Area=Displacement")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount the s-t graph: plot_mathematical_graph(formula="3*x", domain="[0, 10]", title="Position-Time (s-t) Graph"). On Concept 2, mount the v-t graph: plot_mathematical_graph(formula="2*x + 4", domain="[0, 8]", title="Velocity-Time (v-t) Graph with Area=Displacement").
2. PROACTIVE HESITATION RECOVERY: If the student struggles to understand why Area under v-t graph = Distance, call write_chalkboard(action="draw_note", content="Dimension check: Area = Height * Base = (Velocity in m/s) * (Time in s) = meters (Displacement)!", color="botanical").
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Everyday hook: Look at an ECG or heart monitor graph: "Just as a flat line means no heart contraction, what does a flat horizontal line on an s-t graph mean (rest) vs on a v-t graph (constant velocity)?"
   Stage 2: Strict definition of slope: tan(theta) = Delta y / Delta x. For s-t graph, slope = Delta s / Delta t = Speed. For v-t graph, slope = Delta v / Delta t = Acceleration.
   Stage 3: Geometric integration: Area under v-t curve between t1 and t2 equals total displacement.
   Stage 4: Chalkboard analysis of 3 objects A, B, and C moving along s-t curves (CBSE Chapter 4 Exercise Q6).
   Stage 5: Socratic check: "If a v-t graph is a horizontal line parallel to the time axis, what is the acceleration of the object?" HARD STOP: Wait for student response!
   Stage 6: Authentic board exam problem calculating area of rectangle + triangle under v-t curve.`
  },
  {
    order_index: 4,
    title: 'Derivation & Architectural Calculus of Equations of Motion: Graphical Proofs',
    concept_visuals: [
      {
        concept_title: 'First Equation of Motion (v = u + at): Graphical proof from slope of velocity-time curve (BC / AC = (v - u) / t = a)',
        diagram_title: 'Graphical Derivation of v = u + at from Slope of v-t Graph',
        diagram_type: 'graph',
        interactive_math_formula: '2 + 1.5*x',
        what_to_make: 'Velocity-time graph with initial velocity u = 2 m/s, accelerating at a = 1.5 m/s^2, highlighting slope triangle ABC.',
        timing_and_cue: 'Mount v-t derivation line: plot_mathematical_graph(formula="2 + 1.5*x", domain="[0, 6]", title="Graphical Derivation of v = u + at from Slope of v-t Graph")'
      },
      {
        concept_title: 'Second & Third Equations: Displacement by Area decomposition (s = Area of OABD = Area of Rectangle OACD + Area of Triangle ABC = ut + 0.5at^2) and Trapezium Formula (s = (u + v)*t / 2 -> v^2 - u^2 = 2as)',
        diagram_title: 'Displacement Curve from Trapezium Area Decomposition',
        diagram_type: 'graph',
        interactive_math_formula: '2*x + 0.75*x^2',
        what_to_make: 'Quadratic displacement curve s = 2t + 0.75t^2 corresponding to the area decomposition of the v-t trapezium.',
        timing_and_cue: 'Mount quadratic displacement curve: plot_mathematical_graph(formula="2*x + 0.75*x^2", domain="[0, 6]", title="Displacement Curve from Trapezium Area Decomposition")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount the graphical derivation line: plot_mathematical_graph(formula="2 + 1.5*x", domain="[0, 6]", title="Graphical Derivation of v = u + at from Slope"). On Concept 2, plot the quadratic displacement curve: plot_mathematical_graph(formula="2*x + 0.75*x^2", domain="[0, 6]", title="Displacement Curve s = ut + 0.5at^2").
2. TEXTBOOK PROOFS VERBATIM:
   - Derivation 1: Slope a = (v - u) / t => at = v - u => v = u + at.
   - Derivation 2: Area s = Area(Rectangle OADC) + Area(Triangle ABD) = u*t + 0.5*(t)*(v-u) = ut + 0.5*a*t^2.
   - Derivation 3: Area of trapezium s = 0.5 * (Sum of parallel sides) * (Perpendicular distance) = 0.5 * (u + v) * t. Substitute t = (v - u) / a => s = (v^2 - u^2) / (2a) => v^2 - u^2 = 2as.
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Everyday hook: "How can rocket engineers predict exactly when a spacecraft reaches escape velocity before launching it into space?"
   Stage 2: Strict condition of validity: These 3 equations hold ONLY for CONSTANT (uniform) acceleration in a straight line!
   Stage 3: Pitfall: Forgetting to convert km/h to m/s by multiplying by 5/18!
   Stage 4: Chalkboard derivation layout with boxed answers.
   Stage 5: Socratic check: "Can you use v = u + at if the acceleration of a car is continuously increasing every second?" HARD STOP: Wait for student response!
   Stage 6: Authentic board exam numerical on a train starting from rest and attaining 72 km/h in 5 minutes.`
  },
  {
    order_index: 5,
    title: 'Braking Dynamics, Reaction Time & Stopping Distance: Vertical Kinematics & Real-World Safety Physics',
    concept_visuals: [
      {
        concept_title: 'Braking Deceleration & Stopping Distance: Final velocity v = 0; Stopping distance s = u^2 / (2a) grows quadratically with initial speed',
        diagram_title: 'Stopping Distance vs Speed Quadratic Curve (d proportional to v^2)',
        diagram_type: 'graph',
        interactive_math_formula: 'x^2 / 12',
        what_to_make: 'Quadratic stopping distance curve d = v^2 / (2*6) illustrating that doubling velocity quadruples stopping distance.',
        timing_and_cue: 'Mount stopping distance curve: plot_mathematical_graph(formula="x^2 / 12", domain="[0, 25]", title="Stopping Distance vs Speed Quadratic Curve (d proportional to v^2)")'
      },
      {
        concept_title: 'Two-Phase Stopping Distance: Thinking Distance (Reaction Time * Speed) + Braking Distance (Deceleration Stage)',
        diagram_title: 'Two-Phase Stopping Distance Formula Ledger',
        diagram_type: 'flowchart',
        image_search_query: 'Two phase stopping distance thinking distance braking distance',
        what_to_make: 'Flowchart: Driver perceives hazard -> Thinking Distance d1 = u * t_reaction -> Brakes applied -> Braking Distance d2 = u^2 / 2a -> Total Stopping Distance = d1 + d2.',
        timing_and_cue: 'Mount stopping distance ledger: write_chalkboard(action="draw_flowchart", content="TOTAL STOPPING DISTANCE: Thinking Distance (u * t_reaction) + Braking Distance (u^2 / 2a)")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount the stopping distance curve: plot_mathematical_graph(formula="x^2 / 12", domain="[0, 25]", title="Stopping Distance vs Speed Quadratic Curve"). On Concept 2, mount the two-phase stopping flowchart: write_chalkboard(action="draw_flowchart", content="Total Stopping Distance = Thinking Distance (u * t_reaction) + Braking Distance (u^2 / 2a)").
2. PROACTIVE HESITATION RECOVERY: If the student struggles with vertical gravity problems, call write_chalkboard(action="draw_note", content="Vertical Free Fall Rules: Dropped from rest -> u = 0, a = +g (+9.8 m/s^2). Thrown upward -> at highest point v = 0, a = -g (-9.8 m/s^2).", color="botanical").
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Everyday hook: "Why does driving at 60 km/h require much more than double the stopping space of driving at 30 km/h?"
   Stage 2: Mathematical proof that braking distance is proportional to velocity squared (v^2). Doubling speed means FOUR times the braking distance!
   Stage 3: Vertical kinematics: Sign conventions for objects dropped from height vs thrown vertically upward.
   Stage 4: Chalkboard worked solution for Class 9 NCERT Chapter 4 Exercise Q7 (Ball dropped from height 20m, a = 10 m/s^2. Find final velocity v and time t: v^2 = u^2 + 2as = 0 + 2*10*20 = 400 => v = 20 m/s; t = v/a = 20/10 = 2 seconds).
   Stage 5: Socratic check: "If a car speed doubles from 40 km/h to 80 km/h, by what factor does its braking distance multiply?" HARD STOP: Wait for student answer!
   Stage 6: Authentic board exam numerical on car braking with reaction time.`
  },
  {
    order_index: 6,
    title: 'Motion in a Plane: Uniform Circular Motion (UCM) & Radial Acceleration Mechanics',
    concept_visuals: [
      {
        concept_title: 'Tangential Velocity & Radial Centripetal Acceleration Vectors: Constant speed with continuously changing direction',
        diagram_title: 'Uniform Circular Motion Vectors',
        diagram_type: 'image',
        image_search_query: 'Circular motion vectors',
        image_url: 'https://upload.wikimedia.org/wikipedia/commons/3/38/Circular_motion_vectors.svg',
        what_to_make: 'Circular orbit illustrating tangential velocity vectors v perpendicular to inward radial acceleration vectors a_c = v^2 / r at every point along the perimeter.',
        timing_and_cue: 'Mount circular motion vector diagram on Step 1: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/3/38/Circular_motion_vectors.svg | Uniform Circular Motion Vectors | Tangential velocity perpendicular to centripetal radial acceleration")'
      },
      {
        concept_title: 'Circular Orbit Circumference & Orbital Speed Geometry: v = 2*pi*r / T',
        diagram_title: 'Circular Orbit Circumference & Orbital Speed Geometry',
        diagram_type: 'flowchart',
        image_search_query: 'Uniform circular motion derivation',
        what_to_make: 'Derivation flowchart: Distance in 1 revolution = Circumference 2*pi*r -> Time period = T -> Linear Speed v = 2*pi*r / T -> Inward acceleration a = v^2/r.',
        timing_and_cue: 'Mount circular orbit derivation: write_chalkboard(action="draw_flowchart", content="UCM DERIVATION: Perimeter Distance = 2*pi*r || Period = T || Tangential Speed v = 2*pi*r / T || Inward Acceleration a = v^2/r")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount the circular motion vectors diagram: write_chalkboard(action="draw_image", content="https://upload.wikimedia.org/wikipedia/commons/3/38/Circular_motion_vectors.svg | Uniform Circular Motion Vectors | Tangential velocity perpendicular to radial acceleration"). On Concept 2, mount the derivation: write_chalkboard(action="draw_flowchart", content="UCM DERIVATION: Perimeter = 2*pi*r || Period = T || Tangential Speed v = 2*pi*r / T || Inward Acceleration a = v^2/r").
2. PROACTIVE HESITATION RECOVERY: If the student asks why circular motion at constant speed is called accelerated motion, call write_chalkboard(action="draw_note", content="Velocity is a vector having both Magnitude and Direction. In a circle, speed is constant but direction changes at every millisecond. Therefore velocity changes, meaning it is an ACCELERATED MOTION!", color="coral").
3. 6-STAGE SOCRATIC CADENCE:
   Stage 1: Everyday hook: Whirl a stone tied to a string in a circle and suddenly let go: "Does the stone fly straight outward radially, or does it fly tangentially in a straight line?"
   Stage 2: Strict definition of Uniform Circular Motion: Motion of an object along a circular path with constant speed.
   Stage 3: Direction of velocity at any instant is along the tangent to the circular path at that point.
   Stage 4: Chalkboard worked solution for Class 9 NCERT Exercise Q10: Artificial satellite moving in circular orbit of radius 42,250 km taking 24 hours. Speed v = 2 * pi * r / T = 2 * 3.1416 * 42250 km / (24 * 3600 s) = 265,465 km / 86,400 s = 3.07 km/s (or 11,061 km/h!).
   Stage 5: Socratic check: "In which direction does an athlete throw a hammer in the hammer throw event?" (Along the tangent). HARD STOP: Wait for student response!
   Stage 6: Authentic board exam numerical on circular tracks and angular speed.`
  },
  {
    order_index: 7,
    title: 'Master Problem Solver & Comprehensive Chapter Review: NCERT Exercises & Board Numerical Mastery',
    concept_visuals: [
      {
        concept_title: 'Kinematics Master Synthesis Architecture & Formula Ledger',
        diagram_title: 'Kinematics Master Synthesis Architecture & Formula Ledger',
        diagram_type: 'flowchart',
        image_search_query: 'Kinematics master equations summary',
        what_to_make: 'Complete master formula ledger summarizing all 6 governing equations and graphical rules of Class 9 Motion.',
        timing_and_cue: 'Mount Kinematics Master Ledger on Step 1: write_chalkboard(action="draw_flowchart", content="KINEMATICS MASTER LEDGER: v = u + at || s = ut + 0.5*a*t^2 || v^2 = u^2 + 2as || v_avg = (u+v)/2 || v_circle = (2*pi*r) / T")'
      }
    ],
    ai_directives: `MANDATORY LIVE CHALKBOARD INVARIANTS:
1. STEP 1 VISUAL MOUNTING: On Step 1, mount the Kinematics Master Formula Ledger: write_chalkboard(action="draw_flowchart", content="KINEMATICS MASTER LEDGER: v = u + at || s = ut + 1/2*a*t^2 || v^2 = u^2 + 2as || v_avg = Delta x / Delta t || v_circle = (2*pi*r) / T").
2. TEXTBOOK EXERCISE RESOLUTION: Solve all 10 chapter-end and in-text questions step-by-step:
   - Q1: Athlete completing circular track of diameter 200m in 40s. Distance & displacement at 2 min 20s.
   - Q2: Joseph jogs from A to B (300m in 2m30s) and turns around to C (100m in 1m). Average speeds and velocities.
   - Q3: Abdul driving to school at 20 km/h and returning at 30 km/h. Average speed calculation (24 km/h).
   - Q4: Motorboat accelerating from rest at 3.0 m/s^2 for 8.0 s. Distance calculation (s = 0.5 * 3 * 64 = 96 m).
   - Q5: Driver of car at 52 km/h braking to stop in 5s vs driver at 3 km/h braking to stop in 10s. Graph plotting.
   - Q6: Interpretation of s-t curves for objects A, B, and C.
   - Q7: Ball dropped from height 20m with acceleration 10 m/s^2. Velocity and time (v = 20 m/s, t = 2s).
   - Q8: Speed-time graph of a car. Finding distance in first 4s and uniform motion part.
   - Q9: State which situations are possible: (a) Constant acceleration with zero velocity, (b) Acceleration perpendicular to velocity.
   - Q10: Artificial satellite of radius 42250 km in 24 hours (v = 3.07 km/s).
3. HARD STOP after each problem to confirm student understanding before concluding.`
  }
];

async function updateChapter(chapterId, chapterTitle, updates) {
  console.log(`\n============================================================`);
  console.log(`Upgrading Chapter: ${chapterTitle} (${chapterId})`);
  console.log(`============================================================`);

  for (const u of updates) {
    // 1. Fetch current module
    const { data: currentMod, error: fetchErr } = await supabase
      .from('syllabus_modules')
      .select('id, title, visual_lesson_plan')
      .eq('curriculum_id', chapterId)
      .eq('order_index', u.order_index)
      .single();

    if (fetchErr || !currentMod) {
      console.error(`Error fetching Module ${u.order_index}:`, fetchErr);
      continue;
    }

    // 2. Prepare merged visual lesson plan
    const existingVPlan = currentMod.visual_lesson_plan || {};
    const updatedVPlan = {
      ...existingVPlan,
      title: u.title,
      concept_visuals: u.concept_visuals
    };

    // 3. Update syllabus_modules
    const { error: updateErr } = await supabase
      .from('syllabus_modules')
      .update({
        visual_lesson_plan: updatedVPlan,
        ai_system_prompt_context: u.ai_directives
      })
      .eq('id', currentMod.id);

    if (updateErr) {
      console.error(`Error updating Module ${u.order_index} (${currentMod.id}):`, updateErr);
    } else {
      console.log(`[SUCCESS] Module ${u.order_index}: "${currentMod.title}" updated.`);
      console.log(`  - Concept visuals: ${u.concept_visuals.length} high-res assets configured`);
      console.log(`  - AI directives length: ${u.ai_directives.length} characters`);
    }
  }
}

async function run() {
  try {
    await updateChapter(CH2_ID, 'Chapter 2: Cell: The Building Block of Life', ch2Updates);
    await updateChapter(CH3_ID, 'Chapter 3: Tissues in Action', ch3Updates);
    await updateChapter(CH4_ID, 'Chapter 4: Describing Motion Around Us', ch4Updates);
    console.log('\n>>> ALL 21 MODULES ACROSS CHAPTERS 2, 3, AND 4 SUCCESSFULLY UPGRADED IN SUPABASE! <<<');
  } catch (err) {
    console.error('Fatal upgrade error:', err);
    process.exit(1);
  }
}

run();
