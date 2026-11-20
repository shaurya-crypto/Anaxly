import json
import os

CURRICULUM_IDS = {
    2: "c0d6c12e-5576-434d-b541-5142fe09f03b", # Cell: The Building Block of Life
    3: "1053ed93-7167-423b-bdf0-0c73f2b179ff", # Tissues in Action
    4: "b1a05ff2-8ca8-4d59-b7c7-cc0e1304c3ae", # Describing Motion Around Us
    5: "8d01a5f5-bf82-49c2-9fab-253d26b086f4", # Exploring Mixtures and their Separation
    6: "7e1d5438-1174-4577-8599-5f05a6642093", # How Forces Affect Motion
    7: "da5625a5-7071-4533-8667-13da4c28abda", # Work, Energy, and Simple Machines
    8: "8be782c9-c0d3-425e-bb81-c18c298dc4a7", # Journey Inside the Atom
    9: "9a32d68b-ea7e-4860-99c1-0152d3dd6fcd", # Atomic Foundations of Matter
    10: "1908699a-60c6-4a5e-9f27-05f9111fe142", # Sound Waves: Characteristics and Applications
    11: "ba28b0f0-bc67-4638-8c25-092fd7604db4", # Reproduction: How Life Continues
    12: "f0fa824b-38af-44dc-bb2e-e7f5519bad6f", # Patterns in Life: Diversity and Classification
    13: "136b112f-1d39-41ed-9d1b-14236bc5fe52"  # Earth as a System: Energy, Matter, and Life
}

def get_ch2_solver_full():
    return [
        {
            "problem": "Textbook Revise, Reflect, Refine Q1 (Section 2.1, p. 17): Differentiate between the following pairs of terms based on the clues given in parentheses: (i) Cell membrane and cell wall (permeability), (ii) RER and SER (structure), (iii) Chloroplasts and chromoplasts (pigments).",
            "given": "Three cytological pairs with distinguishing criteria: permeability, organelle structure, and pigment chemistry.",
            "formula": "Permeability: Selective vs completely permeable; Reticulum: Ribosome-studded vs smooth tubules; Plastids: Chlorophyll vs carotenoids/xanthophylls.",
            "substitution": "(i) Membrane vs Wall; (ii) RER vs SER; (iii) Chloroplast vs Chromoplast.",
            "calculation": "(i) Cell membrane is selectively permeable, regulating specific solute entry and exit, whereas plant cell wall is completely permeable (freely porous) to water and solutes.\n(ii) Rough Endoplasmic Reticulum (RER) has ribosomes bound to its cytosolic surface giving it a rough granulated appearance, whereas Smooth Endoplasmic Reticulum (SER) is devoid of ribosomes and composed of interconnected smooth tubular networks.\n(iii) Chloroplasts contain green photosynthetic pigments (chlorophyll a and b), whereas chromoplasts contain non-photosynthetic yellow, orange, or red carotenoid and xanthophyll pigments.",
            "finalAnswer": "(i) Membrane is selectively permeable; wall is freely permeable. (ii) RER possesses ribosomes; SER lacks ribosomes. (iii) Chloroplasts contain chlorophyll; chromoplasts contain carotenoids.",
            "unit": "Cytological differentiation",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Comparative cytology: Cell membrane vs cell wall and ER ultrastructure",
            "image_search_query": "endoplasmic reticulum rer ser ribosome diagram",
            "page": 17,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q2 (Section 2.2, p. 17-18): Two similar animal cells are placed in two different solutions: Cell X is placed in pure water, and Cell Y is placed in a concentrated salt solution. Cells are observed after some time. Cell X swells, and Cell Y shrinks. Which statement provides the correct explanation? (i) Salt molecules moved into Cell Y, causing it to shrink. (ii) Water moved into Cell X and more water moved out of Cell Y than the salt solution entered in it. (iii) Water moved into Cell X and moved out of Cell Y through the cell membrane. (iv) Solute movement caused osmosis in both cells.",
            "given": "Animal Cell X in pure water (hypotonic); Animal Cell Y in concentrated salt solution (hypertonic).",
            "formula": "Osmosis: Net diffusion of water solvent molecules across a selectively permeable membrane from higher water potential (lower solute conc.) to lower water potential (higher solute conc.).",
            "substitution": "Cell X: Water moves in (endosmosis); Cell Y: Water moves out (exosmosis).",
            "calculation": "1. Pure water is hypotonic relative to cell cytosol, causing net water inflow into Cell X via endosmosis, making it swell.\n2. Concentrated salt solution is hypertonic relative to cytosol, causing net water outflow from Cell Y via exosmosis into the exterior, causing cell shrinkage (crenation).\n3. Osmosis is mediated exclusively by water solvent transit across the membrane, not solute transit.",
            "finalAnswer": "Correct Option is (iii): Water moved into Cell X and moved out of Cell Y through the cell membrane.",
            "unit": "Tonicity & Osmosis",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Osmotic behavior of animal cells in hypotonic, isotonic, and hypertonic media",
            "image_search_query": "animal cell osmosis hypotonic hypertonic swelling shrinking",
            "page": 18,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q3 (Section 2.3, p. 18): Look at the diagram of a cell in Fig. 2.20. Identify the parts labelled from (a) to (g) and correctly match them with their functions: (i) Controlling all the activities of a cell, (ii) Site of cellular respiration, (iii) Storage organelle providing turgidity/rigidity, (iv) Packaging and secretion, (v) Protein synthesis, (vi) Site of photosynthesis, (vii) Boundary regulating transport.",
            "given": "Cell diagram Fig. 2.20 with organelles (a) to (g) and cellular physiological functions (i) to (vii).",
            "formula": "Organelle Function Mapping: Nucleus -> Master control; Mitochondria -> ATP respiration; Central Vacuole -> Turgidity; Golgi -> Packaging; Ribosomes/RER -> Protein synthesis; Chloroplast -> Photosynthesis; Cell Membrane -> Selective transport.",
            "substitution": "Matching organelle labels to physiological roles.",
            "calculation": "1. Nucleus (a) contains chromosomes/DNA and directs all metabolic and reproductive cell activities -> (i).\n2. Mitochondrion (b) generates ATP via the Krebs cycle and oxidative phosphorylation -> (ii).\n3. Large central vacuole (c) stores cell sap and sustains hydrostatic turgor pressure -> (iii).\n4. Golgi apparatus (d) modifies, sorts, and packages glycoproteins into secretory vesicles -> (iv).\n5. Rough ER / Ribosomes (e) translate mRNA into polypeptide protein chains -> (v).\n6. Chloroplast (f) captures radiant solar energy for photosynthetic sugar production -> (vi).\n7. Plasma membrane (g) maintains ionic homeostasis and selective permeability -> (vii).",
            "finalAnswer": "(a)-(i) Nucleus, (b)-(ii) Mitochondrion, (c)-(iii) Vacuole, (d)-(iv) Golgi apparatus, (e)-(v) RER/Ribosomes, (f)-(vi) Chloroplast, (g)-(vii) Plasma membrane.",
            "unit": "Organelle morphology & function",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 2.20: Schematic diagram of plant and animal cell ultrastructure",
            "image_search_query": "plant cell ultrastructure labelled diagram organelles",
            "page": 18,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q4 (Section 2.3, p. 18): Which of the following option(s) of the pairs of cell organelles and their functions is/are correct? (a) Mitochondria – ATP synthesis, (b) Chloroplast – Starch synthesis and photosynthesis, (c) Lysosomes – Secretory vesicle packaging, (d) Ribosomes – Protein synthesis.",
            "given": "Four organelle-function pairs: (a) Mitochondria, (b) Chloroplast, (c) Lysosomes, (d) Ribosomes.",
            "formula": "Organelle functions: Mitochondria produce ATP; Chloroplasts synthesize carbohydrates via photosynthesis; Lysosomes are hydrolytic digestive organelles (Golgi handles secretory packaging); Ribosomes synthesize proteins.",
            "substitution": "Evaluate validity of pairs (a), (b), (c), (d).",
            "calculation": "1. Pair (a) is correct: Mitochondria are the 'powerhouses of the cell' generating ATP.\n2. Pair (b) is correct: Chloroplasts perform photosynthesis and store starch.\n3. Pair (c) is INCORRECT: Secretory packaging is performed by Golgi apparatus; lysosomes perform intracellular digestion and autolysis.\n4. Pair (d) is correct: Ribosomes assemble amino acids into proteins during translation.",
            "finalAnswer": "Correct pairs are (a), (b), and (d). Pair (c) is incorrect because lysosomes are digestive/suicidal bags, not secretory packaging bodies.",
            "unit": "Organelle functions",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "cell organelles functions mitochondria chloroplast ribosomes",
            "page": 18,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q5 (Section 2.3, p. 18): Two students, Renu and Rohit, were having a discussion on plastids. Renu stated that all plastids contain pigments, whereas Rohit argued that some plastids are colourless and store starch, oils, or proteins. Who is correct? Justify with scientific classifications.",
            "given": "Renu's claim (all plastids have pigments) vs Rohit's claim (some plastids are colourless storage bodies).",
            "formula": "Plastid Classification: Chromoplasts & Chloroplasts (pigmented) vs Leucoplasts (colourless storage plastids: amyloplasts, elaioplasts, aleuroplasts).",
            "substitution": "Compare claims against plastid morphology and biochemical function.",
            "calculation": "1. Rohit is scientifically correct.\n2. Plastids are classified into: (a) Chromoplasts (coloured, containing carotenoids/xanthophylls), (b) Chloroplasts (green, containing chlorophyll), and (c) Leucoplasts (non-pigmented, colourless plastids).\n3. Leucoplasts occur in non-photosynthetic storage tissues (tubers, roots, seeds) and specialize into amyloplasts (store starch), elaioplasts (store lipids/oils), and aleuroplasts (store proteins).\n4. Therefore, Renu's statement that all plastids contain pigments is erroneous.",
            "finalAnswer": "Rohit is correct. Leucoplasts are colourless plastids that store starch, oils, and proteins without pigments.",
            "unit": "Plastid classification",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Classification of plastids: Chloroplasts, Chromoplasts, and Leucoplasts",
            "image_search_query": "plastids classification chloroplast chromoplast leucoplast diagram",
            "page": 18,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q6 (Section 2.3, p. 18): Mitochondria and chloroplasts are two important organelles in a plant cell. Explain two unique structural features they share that distinguish them from all other cytoplasmic organelles.",
            "given": "Mitochondria and chloroplasts in eukaryotic cells.",
            "formula": "Endosymbiotic Theory: Double membrane envelope, circular double-stranded prokaryotic-like DNA, and 70S ribosomes enabling semi-autonomous protein synthesis.",
            "substitution": "Structural features common to mitochondria and chloroplasts.",
            "calculation": "1. Feature 1: Presence of Own Genetic Material (DNA) and 70S Ribosomes: Both mitochondria and chloroplasts contain circular DNA molecules and their own ribosomes, enabling them to synthesize some of their own structural enzymes and proteins independently (semi-autonomous organelles).\n2. Feature 2: Double-Membrane Envelope: Both organelles are enclosed by two distinct lipid bilayer membranes (an outer membrane and a folded or thylakoid-containing inner membrane) reflecting their endosymbiotic prokaryotic origin.",
            "finalAnswer": "They both possess: 1. Their own circular DNA and 70S ribosomes (semi-autonomous); 2. A distinct double-membrane bounding envelope.",
            "unit": "Semi-autonomous organelles",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Ultrastructure of semi-autonomous organelles: Mitochondria and Chloroplast",
            "image_search_query": "mitochondria and chloroplast ultrastructure comparison diagram",
            "page": 18,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q7 (Section 2.3, p. 18): Which of the following pairs of cell organelles contains DNA? (i) Mitochondria and Lysosomes, (ii) Chloroplasts and Vacuoles, (iii) Mitochondria and Chloroplasts, (iv) Golgi apparatus and Endoplasmic Reticulum.",
            "given": "Organelle pairs for extranuclear DNA presence.",
            "formula": "Organellar genome localization: Mitochondria (mtDNA) and Chloroplasts (cpDNA).",
            "substitution": "Examine organelle genomes.",
            "calculation": "1. Lysosomes, vacuoles, Golgi bodies, and ER contain zero DNA.\n2. The nucleus houses nuclear genomic DNA.\n3. Outside the nucleus, only mitochondria and chloroplasts retain vestigial circular double-stranded DNA genomes from ancestral bacterial endosymbionts.",
            "finalAnswer": "Correct Option is (iii): Mitochondria and Chloroplasts contain DNA.",
            "unit": "Extranuclear genetics",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "mitochondrial dna chloroplast dna circular genome",
            "page": 18,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q8 (Section 2.2, p. 19): A researcher carried out an experiment in which she took two carrots of equal size and mass (Carrot A and Carrot B). Carrot A was immersed in pure water and Carrot B was immersed in a concentrated sodium chloride (salt) solution. After 24 hours: (a) Predict the change in mass and firmness of Carrot A and Carrot B. (b) Name and explain the cellular processes responsible.",
            "given": "Carrot A in pure water (hypotonic); Carrot B in concentrated NaCl solution (hypertonic).",
            "formula": "Osmosis: $\\Delta m > 0$ for endosmosis; $\\Delta m < 0$ for exosmosis and cellular plasmolysis.",
            "substitution": "Evaluate cell turgor and water flux for both carrots.",
            "calculation": "1. Carrot A (in pure water): Water moves into root cells via endosmosis because the external water potential is higher than the cell sap. The cells become fully turgid. Carrot A shows an increase in mass and becomes firm, stiff, and crisp.\n2. Carrot B (in concentrated salt solution): Water moves out of root cells into the external concentrated solution via exosmosis because cell sap has higher water potential. The cells lose turgor pressure and undergo plasmolysis (cytoplasm pulls away from cell wall). Carrot B loses mass and becomes soft, flaccid, and limp.",
            "finalAnswer": "(a) Carrot A gains mass and becomes firm/crisp; Carrot B loses mass and becomes soft/flaccid. (b) Endosmosis causes turgor in A; exosmosis causes flaccidity/plasmolysis in B.",
            "unit": "Plant cell osmosis & plasmolysis",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Experimental demonstration of endosmosis and exosmosis in plant tissues",
            "image_search_query": "carrot osmosis salt water vs tap water experiment",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q9 (Section 2.1 & 2.3, p. 19): Indicate the presence (+) or absence (-) of the following structures in bacterial cells, plant cells, and animal cells: 1. Cell membrane, 2. Cell wall, 3. Well-defined nucleus with membrane, 4. Membrane-bound organelles (Mitochondria, Chloroplasts), 5. Ribosomes.",
            "given": "Comparative cytological table for Prokaryotic (bacterial) vs Eukaryotic (plant and animal) cell plans.",
            "formula": "Prokaryote vs Eukaryote cytology: Prokaryotes lack membrane-bound nucleus and organelles but have 70S ribosomes and peptidoglycan wall. Plant cells have cellulose wall, chloroplasts, and large vacuole. Animal cells lack cell wall and chloroplasts.",
            "substitution": "Tabulate morphological features.",
            "calculation": "1. Cell membrane: Present in all three (+, +, +).\n2. Cell wall: Present in bacterial cell (peptidoglycan, +) and plant cell (cellulose, +); Absent in animal cell (-).\n3. Well-defined nucleus: Absent in bacterial cell (-); Present in plant cell (+) and animal cell (+).\n4. Membrane-bound organelles: Absent in bacterial cell (-); Present in plant cell (+) and animal cell (+).\n5. Ribosomes: Present in all three (+) (70S in bacteria; 80S in eukaryotic cytosol).",
            "finalAnswer": "Bacterial: Wall (+), Membrane (+), Nucleus (-), Organelles (-), Ribosomes (+).\nPlant: Wall (+), Membrane (+), Nucleus (+), Organelles (+), Ribosomes (+).\nAnimal: Wall (-), Membrane (+), Nucleus (+), Organelles (+), Ribosomes (+).",
            "unit": "Cytological comparative taxonomy",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Comparative cytological table: Prokaryotic vs Plant vs Animal cell structure",
            "image_search_query": "prokaryotic vs eukaryotic plant animal cell comparison table",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q10 (Section 2.2, p. 19-20): Carry out the following experiment using four peeled potato halves (Cups A, B, C, D): Cup A is kept empty; Cup B has 1 teaspoon of sugar; Cup C has 1 teaspoon of salt; Cup D is made from a boiled potato and has 1 teaspoon of sugar. Each cup is placed in a trough of water: (a) Explain why water gathers in the hollowed portions of B and C. (b) Why is Cup A necessary? (c) Explain why water does not gather in Cup D.",
            "given": "Four hollowed potato osmometers: A (empty raw), B (raw + sugar), C (raw + salt), D (boiled + sugar).",
            "formula": "Osmosis across living semi-permeable membrane: Dead/boiled cells lose membrane semi-permeability ($k_d \\to 0$).",
            "substitution": "Analyze membrane integrity and solute gradients across cups A, B, C, D.",
            "calculation": "1. Water gathers in B and C: The sugar in B and salt in C create hypertonic solute solutions inside the hollows. Surrounding water enters potato cells by endosmosis and flows down the water potential gradient through living plasma membranes into the cavity.\n2. Cup A is the experimental CONTROL: It has no solute inside the cavity. It proves that water does not accumulate spontaneously without an osmotic concentration gradient.\n3. No water gathers in Cup D: Boiling denatures cellular membrane proteins and destroys the selectively permeable plasma membranes of potato cells. Without an intact semi-permeable membrane, osmosis cannot take place.",
            "finalAnswer": "(a) Endosmosis drives water into hypertonic sugar/salt cavities of B and C. (b) Cup A serves as the negative control. (c) Boiling kills potato cells and destroys semi-permeability in D.",
            "unit": "Potato Osmometer Experiment",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Four-cup potato osmometer experimental setup (Cups A, B, C, D)",
            "image_search_query": "potato osmometer experiment four cups sugar salt boiled water",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q11 (Section 2.3, p. 19): Identify the pair that incorrectly matches the cell organelle with its structural feature or function: (i) Golgi apparatus – Cisternae and secretory vesicles, (ii) Lysosome – Oxidative ATP synthesis, (iii) Vacuole – Tonoplast membrane and cell sap, (iv) Centrosome – Microtubule organization during cell division.",
            "given": "Four organelle structure/function assertions.",
            "formula": "Lysosome: Hydrolytic acidic enzymes for autolysis/digestion; Mitochondria: Oxidative phosphorylation and ATP synthesis.",
            "substitution": "Examine pair (ii).",
            "calculation": "1. Pair (i) correctly describes Golgi apparatus stacked flattened cisternae and vesicles.\n2. Pair (ii) is INCORRECT: Lysosomes do NOT perform ATP synthesis; they contain acid hydrolases that digest cellular debris and foreign pathogens. ATP synthesis is the unique function of mitochondria.\n3. Pair (iii) correctly describes plant vacuoles bounded by the tonoplast membrane.\n4. Pair (iv) correctly describes animal centrosomes organizing spindle fibers.",
            "finalAnswer": "Incorrect pair is (ii): Lysosome – Oxidative ATP synthesis (ATP synthesis is carried out by mitochondria).",
            "unit": "Cell organelle diagnostics",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "lysosome structure hydrolytic enzymes diagram",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q12 (Section 2.3, p. 19): What outcome do you expect if all the mitochondria are removed from a living animal cell? Explain the metabolic consequences.",
            "given": "Complete removal of mitochondria from an animal cell.",
            "formula": "Aerobic respiration in mitochondria: 1 Glucose -> 36-38 ATP; Cytosolic glycolysis only yields 2 net ATP.",
            "substitution": "Evaluate cell bioenergetics without Krebs cycle and oxidative phosphorylation.",
            "calculation": "1. Mitochondria are responsible for aerobic cellular respiration, carrying out the Krebs cycle, electron transport chain, and ATP synthesis.\n2. In their absence, the cell cannot utilize pyruvate aerobically and is forced to rely solely on anaerobic cytosolic glycolysis, yielding only 2 ATP molecules per glucose molecule.\n3. This 95% reduction in ATP yield is insufficient to power energy-intensive active transport pumps (Na+/K+ ATPase), macromolecule synthesis, and metabolic homeostasis. The cell undergoes osmotic lysis and rapid necrosis.",
            "finalAnswer": "The cell will suffer severe ATP deprivation, active transport failure, inability to maintain osmotic equilibrium, and cell death.",
            "unit": "Cellular energetics & ATP synthesis",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "mitochondria atp synthesis cellular respiration diagram",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q13 (Section 2.4, p. 19): Which phenomenon inhibits the formation of tumors and cancerous growth in human tissue under normal cellular conditions? Explain the mechanism of contact inhibition and regulated cell division.",
            "given": "Normal tissue growth control vs neoplastic tumor formation.",
            "formula": "Cell Cycle Control: Contact inhibition and apoptotic tumor suppressor pathways (p53).",
            "substitution": "Mechanism preventing aberrant proliferation in normal cells.",
            "calculation": "1. Normal animal cells exhibit Contact Inhibition: when cells grow and touch neighboring cells, surface cadherin-mediated cell-cell signals halt further mitotic division.\n2. In addition, internal cell cycle checkpoints (G1/S and G2/M) regulated by tumor suppressor genes inspect DNA integrity. If DNA damage cannot be repaired, programmed cell death (apoptosis) is triggered.\n3. Cancer cells lose contact inhibition and bypass cycle checkpoints, dividing uncontrollably into malignant tumors.",
            "finalAnswer": "Contact inhibition and apoptotic cell cycle checkpoints halt mitosis when cells touch, preventing tumor formation.",
            "unit": "Cell division regulation & oncology",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Contact inhibition in normal cells vs uncontrolled proliferation in cancer cells",
            "image_search_query": "contact inhibition normal vs cancer cells diagram",
            "page": 19,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q14 (Section 2.3, p. 20): The cell membrane of a cell is made up of proteins and lipids. Which specific cell organelles synthesize these lipids and proteins required for membrane biogenesis?",
            "given": "Cell membrane biochemical composition: Phospholipids, sterols, and integral/peripheral proteins.",
            "formula": "Membrane Biogenesis: Rough Endoplasmic Reticulum (RER) synthesizes membrane proteins; Smooth Endoplasmic Reticulum (SER) synthesizes membrane lipids.",
            "substitution": "Synthesized components transported to Golgi apparatus for processing and vesicle fusion with the plasma membrane.",
            "calculation": "1. Membrane Lipids (phospholipids and cholesterol) are synthesized on the cytoplasmic face of the Smooth Endoplasmic Reticulum (SER).\n2. Membrane Proteins are synthesized by ribosomes docked on the Rough Endoplasmic Reticulum (RER) and translocated directly into the ER membrane.\n3. These lipids and proteins are transported via transition vesicles to the Golgi apparatus for glycosylation and sorting, then delivered by secretory vesicles to replenish and build the plasma membrane (membrane biogenesis).",
            "finalAnswer": "Proteins are synthesized by RER; lipids are synthesized by SER. Together with Golgi processing, this constitutes membrane biogenesis.",
            "unit": "Membrane biogenesis",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Membrane biogenesis: Cooperation between RER, SER, and Golgi apparatus",
            "image_search_query": "membrane biogenesis rer ser golgi apparatus diagram",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q15 (Section 2.4, p. 20): What would happen if gametes (sperm and ovum) were formed by mitotic cell divisions instead of meiotic divisions? Explain the genetic consequence across generations.",
            "given": "Diploid parental chromosome count 2n = 46 in humans; Gamete formation via mitosis vs meiosis.",
            "formula": "Chromosome number across generations: Meiosis: $2n \\to n$; Syngamy: $n + n = 2n$. Mitosis hypothetical: $2n \\to 2n$; Syngamy: $2n + 2n = 4n$.",
            "substitution": "Trace chromosomal ploidy over successive generations.",
            "calculation": "1. In normal sexual reproduction, meiosis is a reductional division that halves the chromosome number from diploid (2n = 46) to haploid (n = 23) in gametes. Fertilisation restores the species-specific diploid number (23 + 23 = 46).\n2. If gametes were produced by equational mitosis, each sperm and ovum would carry a diploid set (2n = 46).\n3. Fertilisation would fuse two diploid gametes, producing a tetraploid zygote (4n = 92 chromosomes). In the next generation, this would double again to octoploid (8n = 184 chromosomes).\n4. This geometric chromosomal doubling leads to massive genetic instability, lethal developmental abnormalities, and loss of species identity.",
            "finalAnswer": "Chromosome number would double every generation (2n -> 4n -> 8n), causing extreme polyploidy, developmental arrest, and loss of species stability.",
            "unit": "Meiosis & Ploidy dynamics",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "meiosis vs mitosis chromosome number reduction division",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q16 (Section 2.2, p. 20): A farmer, Deepa, was very happy with the harvest of amla (Indian gooseberry) from her farm. She decided to prepare sweet amla preserve (murabba) and salty amla pickle. When she added salt and concentrated sugar syrup to amla pieces, she observed that liquid was released from the pieces. (a) Name the biological phenomenon responsible for this observation. (b) Why is this step essential in food preservation against microbial spoilage?",
            "given": "Amla pieces soaked in concentrated salt and sugar syrups releasing aqueous fluid.",
            "formula": "Exosmosis and Plasmolysis: High hypertonic external osmotic pressure ($C_{\\text{ext}} \\gg C_{\\text{cell}}$).",
            "substitution": "Water flow from amla tissue and microbes into hypertonic brine/sugar syrup.",
            "calculation": "(a) Biological Phenomenon: Exosmosis. Concentrated sugar syrup and salt solution are strongly hypertonic relative to the amla cell sap. Water diffuses out of amla cells across their semi-permeable membranes into the surrounding medium down its water potential gradient, releasing liquid.\n(b) Food Preservation Mechanism: The high concentration of sugar or salt creates a hypertonic environment for bacteria, yeasts, and fungal spores. When microbes land on the pickle or preserve, water is drawn out of microbial cells by exosmosis, causing microbial plasmolysis, dehydration, and inhibition of metabolic enzymes, permanently preventing microbial spoilage.",
            "finalAnswer": "(a) Exosmosis; (b) The hypertonic environment draws water out of microbial cells by exosmosis (plasmolysis), killing microbes and preserving food.",
            "unit": "Food preservation & applied osmosis",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Mechanism of food preservation via hypertonic plasmolysis of bacterial cells",
            "image_search_query": "bacterial plasmolysis salt sugar food preservation osmosis",
            "page": 20,
            "section": "Revise, Reflect, Refine"
        }
    ]
