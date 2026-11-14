"""
Complete Module Synthesis for Class 9 Science:
Chapter 11: Reproduction: How Life Continues (Curriculum ID: ba28b0f0-bc67-4638-8c25-092fd7604db4)
"""

import json

def get_ch11_modules():
    # Module 1: Cellular Foundations: DNA Replication, Chromosomes & Variations
    m1 = {
        "order_index": 1,
        "title": "Cellular Foundations of Reproduction: DNA Replication, Chromosomes & Biological Variation",
        "description": "Analyze why reproduction is essential for species continuity, explore DNA replication fidelity and biochemical copying mechanisms in the cell nucleus, and evaluate how genetic variations drive natural selection and population survival.",
        "subtopics": [
            "Biological Purpose of Reproduction: Continuity of species vs individual organism survival",
            "The Cellular Blueprint: Chromosomes and DNA (Deoxyribonucleic Acid) in the cell nucleus",
            "DNA Replication Mechanics: Biochemical synthesis of identical genetic copies prior to cell division",
            "Origins of Biological Variation: Biochemical inaccuracies during DNA replication",
            "Evolutionary Value of Variations: Thermophilic bacteria surviving heat waves; natural selection",
            "Insect Metamorphosis: Complete metamorphosis in the life cycle of butterflies (egg, larva, pupa, adult)"
        ],
        "key_concepts": [
            "Biological Continuity of Species: Reproduction is the biological process by which existing organisms produce new individuals of their own kind, ensuring the continuation of life and preventing species extinction across generations.",
            "Chromosomes & DNA Blueprint: The cell nucleus contains chromosomes which carry information for the inheritance of features from parents to offspring in the form of DNA (Deoxyribonucleic Acid) molecules; DNA is the master blueprint for protein synthesis.",
            "DNA Replication Invariant: A dividing cell must replicate its DNA so each daughter cell receives an identical copy of the genetic blueprint; replication is accompanied by the creation of an additional cellular apparatus so each daughter cell is viable.",
            "Biochemical Error & Variation: No biochemical copying mechanism is 100% reliable; subtle copying errors during DNA replication introduce genetic variations, making offspring subtly distinct from parents.",
            "Survival Value of Variations: Variations are not necessarily beneficial to an individual, but they are vital for the survival of the species over time under severe environmental changes (e.g., global warming, drought, epidemics).",
            "Metamorphosis & Developmental Plasticity: In holometabolous insects like butterflies, reproduction initiates an embryonic and larval life cycle (egg -> larva/caterpillar -> pupa/chrysalis -> adult butterfly) where distinct body plans adapt to different ecological niches."
        ],
        "success_criteria": "Student can explain the role of DNA replication in cell division, explain why variation is beneficial for species survival, and describe complete metamorphosis in butterflies.",
        "chapter_notes": """### 11.1 The Biological Necessity of Reproduction
Reproduction is not essential to maintain the life of an individual organism (unlike nutrition, respiration, or excretion). However, it is **vital for the continuation and survival of a species** on Earth. If organisms ceased reproducing, their species would go extinct upon the death of the existing generation.

### 11.2 The Genetic Blueprint: DNA and Chromosomes
- In the cell nucleus, **chromosomes** consist of **DNA (Deoxyribonucleic Acid)** and histones.
- DNA contains coded nucleotide sequences (genes) that dictate the structure of enzymes and structural proteins. If the genetic information changes, different proteins are synthesized, altering the organism's body design.

### 11.3 DNA Replication & The Mechanism of Variation
- When a cell divides, it must create **two copies of its DNA**:
  1. DNA polymerases synthesize complementary strands.
  2. The cell creates an additional cellular apparatus (organelles, cytoplasm).
  3. The DNA copies separate, each taking its own cellular machinery to form two daughter cells.
- **Inaccuracies in DNA Copying**:
  - Biochemical reactions have a statistical error rate.
  - Minor variations result in subtle physical differences among siblings.
  - Drastic variations produce non-viable cellular apparatus, leading to cell death.

### 11.4 The Importance of Variation in Evolution
- Organisms occupy specific ecological niches in an ecosystem based on their body design.
- If an environmental niche undergoes drastic changes (e.g., sudden temperature surge, water scarcity, meteor strike), a uniform population lacking variation could be wiped out entirely.
- If some variants possess heat-resistant or drought-resistant traits, those individuals survive, reproduce, and propagate the resilient population.
- Thus, **variation is the raw fuel for natural selection and evolution**.

### 11.5 Life Cycles & Metamorphosis (The Butterfly)
- Sexual reproduction produces a zygote that undergoes specialized ontogenetic development:
  1. **Egg**: Laid on host plant leaves.
  2. **Larva (Caterpillar)**: Voracious feeding stage focused on nutrient accumulation.
  3. **Pupa (Chrysalis)**: Non-feeding stage of radical tissue histolysis and organ remodeling.
  4. **Adult (Imago)**: Winged reproductive adult adapted for dispersal and mating.""",
        "worked_examples": [
            {
                "problem": "What is the importance of DNA copying in reproduction?",
                "given": "Cellular division and inheritance of genetic traits.",
                "formula": "Genetic Information Conservation: DNA_parent -> 2 * DNA_daughter",
                "substitution": "DNA carries coded instructions for synthesizing structural proteins and enzymes.",
                "calculation": "1. DNA carries the master genetic blueprint that determines the body design, metabolic pathways, and physical characteristics of the organism.\n2. DNA replication ensures that each resulting daughter cell receives a complete and identical complement of chromosomes.\n3. Along with DNA replication, new cellular apparatus (cytoplasm, organelles) is generated to keep daughter cells functionally viable.\n4. Subtle replication errors generate variations essential for evolution.",
                "finalAnswer": "DNA copying ensures the accurate transmission of body design and functional traits to offspring, while generating variations vital for species evolution.",
                "unit": "Molecular Genetics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.16: Cellular DNA inheritance and reproductive continuity"
            },
            {
                "problem": "Why is variation beneficial to the species, even if it may not necessarily benefit the individual organism?",
                "given": "Environmental niche stability vs sudden catastrophic climate shifts.",
                "formula": "Population Survival Probability under Ecological Stress",
                "substitution": "A population of temperate bacteria subjected to global warming.",
                "calculation": "1. Consider a colony of bacteria living in temperate water. If water temperature suddenly rises due to thermal pollution or climate warming, the majority of standard bacteria will die.\n2. If a small fraction of the population carried a genetic variation granting heat resistance, those few individuals will survive the thermal shock.\n3. The surviving heat-resistant bacteria will multiply and prevent the entire species from becoming extinct.\n4. Therefore, variations safeguard species survival over geological time.",
                "finalAnswer": "Variations ensure that when severe environmental catastrophes strike, adapted variants survive and preserve the species from total extinction.",
                "unit": "Evolutionary Ecology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.17: Environmental adaptation across life cycles"
            },
            {
                "problem": "Describe the four distinct stages in the complete metamorphosis of a butterfly (Fig. 11.17). How does this life cycle optimize survival?",
                "given": "Holometabolous development in Lepidoptera.",
                "formula": "Complete Metamorphosis: Egg -> Larva -> Pupa -> Adult",
                "substitution": "Specialization of feeding vs reproductive stages.",
                "calculation": "1. Stage 1: Egg - Protected embryo laid on specific host plant leaves.\n2. Stage 2: Larva (Caterpillar) - Voracious feeding stage equipped with chewing mouthparts to accumulate mass and energy.\n3. Stage 3: Pupa (Chrysalis) - Enclosed resting stage where larval tissues break down and adult structures (wings, antennae, reproductive organs) differentiate.\n4. Stage 4: Adult Butterfly - Winged stage specialized for flight, nectar feeding, and sexual reproduction.\n5. Survival advantage: Larvae and adults occupy different ecological niches and eat different foods (leaves vs nectar), eliminating intraspecific competition.",
                "finalAnswer": "Egg -> Larva -> Pupa -> Adult; eliminates food competition between young and adults, maximizing survival across life stages.",
                "unit": "Developmental Biology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.17: Life cycle of a butterfly showing complete metamorphosis"
            },
            {
                "problem": "Why does sexual reproduction produce much greater variation than asexual reproduction?",
                "given": "Asexual cloning vs sexual amphimixis (gamete fusion).",
                "formula": "Meiotic Crossing Over + Independent Assortment + Syngamy",
                "substitution": "One parent vs two parents combining distinct genomes.",
                "calculation": "1. In asexual reproduction, offspring are produced by a single parent through mitotic cell division; variations arise solely from rare accidental DNA copying errors.\n2. In sexual reproduction, two distinct parents contribute gametes (sperm and egg).\n3. During gametogenesis (meiosis), homologous chromosomes undergo crossing-over and independent assortment, shuffling millions of gene combinations.\n4. The fusion of two genetically unique gametes (syngamy) creates a unique combination of traits in every offspring.",
                "finalAnswer": "Sexual reproduction shuffles genes from two distinct parental genomes through meiotic crossing over and random fertilization, generating vast genetic diversity.",
                "unit": "Genetic Variation",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.16: Genetic recombination in sexual reproduction"
            },
            {
                "problem": "Can a cell divide simply by duplicating its DNA without creating new cellular machinery? Explain what would happen.",
                "given": "Cellular division requirements: Genetic material + Cytoplasmic apparatus.",
                "formula": "Cell Viability = Functional Genome + Metabolic Machinery",
                "substitution": "DNA alone vs functional cytoplasm, enzymes, and membranes.",
                "calculation": "1. No, a cell cannot divide solely by copying DNA.\n2. Naked DNA cannot metabolize, synthesize ATP, or maintain structural boundaries on its own.\n3. For a daughter cell to survive, the parent cell must duplicate its cytoplasmic contents, mitochondria, ribosomes, and synthesize new cell membranes and walls.\n4. If a DNA copy were isolated without cellular machinery, it would simply degrade and die.",
                "finalAnswer": "No; DNA cannot function without cytoplasm and organelles; replication must be paired with cellular apparatus synthesis to produce living daughter cells.",
                "unit": "Cell Physiology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.16: Cytoplasmic division alongside nuclear division"
            },
            {
                "problem": "What is the difference between an individual organism's survival need and species survival need regarding reproduction?",
                "given": "Vital life processes (circulation, respiration, excretion) vs reproduction.",
                "formula": "Individual Homeostasis vs Lineage Continuity",
                "substitution": "An animal that fails to reproduce lives a full natural lifespan; a species that fails to reproduce vanishes.",
                "calculation": "1. Individual survival processes (digestion, respiration, excretion, neural coordination) maintain homeostasis within an organism's lifetime; failure of any of these results in immediate individual death.\n2. An individual organism can live a completely healthy, full lifespan without ever reproducing.\n3. However, reproduction is strictly mandatory for the species; without it, when the current living generation dies of old age, the entire species is extinguished permanently.",
                "finalAnswer": "Reproduction is non-essential for an individual's personal survival, but strictly indispensable for the collective persistence of the species.",
                "unit": "Evolutionary Principles",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.17: Generational succession in life cycles"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Reproduction is necessary for an individual animal or human to stay alive.",
                "correction": "Reproduction is NOT necessary for an individual's personal survival. If an organism never reproduces, its heart still beats, lungs still breathe, and it lives a normal lifespan. Reproduction is necessary only for the CONTINUITY OF THE SPECIES.",
                "why_it_matters": "Distinguishes individual metabolic maintenance from generational lineage survival."
            }
        ],
        "visual_lesson_plan": {
            "title": "Cellular Foundations & Variations Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Biological Continuity of Species: Reproduction is the biological process by which existing organisms produce new individuals of their own kind, ensuring the continuation of life and preventing species extinction across generations.",
                    "diagram_title": "Generational Succession in Living Systems",
                    "diagram_type": "image",
                    "image_query": "biological reproduction continuity of life species diagram",
                    "video_query": "why reproduction is essential for life continuity",
                    "image_url": "/extracted_diagrams/ch11/fig_11_16.webp",
                    "what_to_make": "Textbook diagram illustrating biological inheritance and cellular continuity.",
                    "timing_and_cue": "Mount biological continuity on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_16.webp | Biological Continuity | Generational inheritance safeguarding species from extinction\")"
                },
                {
                    "concept_title": "Chromosomes & DNA Blueprint: The cell nucleus contains chromosomes which carry information for the inheritance of features from parents to offspring in the form of DNA (Deoxyribonucleic Acid) molecules; DNA is the master blueprint for protein synthesis.",
                    "diagram_title": "DNA Replication & Chromosome Duplication",
                    "diagram_type": "image",
                    "image_query": "DNA replication chromosomes nucleus cell division diagram",
                    "video_query": "DNA copying during cell division class 10 9",
                    "image_url": "/extracted_diagrams/ch11/fig_11_16.webp",
                    "what_to_make": "Textbook diagram showing DNA duplication and chromosome allocation to daughter cells.",
                    "timing_and_cue": "Mount DNA blueprint on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_16.webp | DNA Replication Blueprint | Nucleotide copying synthesizing protein blueprints for daughter cells\")"
                },
                {
                    "concept_title": "DNA Replication Invariant: A dividing cell must replicate its DNA so each daughter cell receives an identical copy of the genetic blueprint; replication is accompanied by the creation of an additional cellular apparatus so each daughter cell is viable.",
                    "diagram_title": "Cellular Apparatus Synthesis During Division",
                    "diagram_type": "image",
                    "image_query": "cellular division organelle replication cytokinesis diagram",
                    "video_query": "cell division DNA and cellular apparatus duplication",
                    "image_url": "/extracted_diagrams/ch11/fig_11_16.webp",
                    "what_to_make": "Textbook diagram illustrating cytoplasmic apparatus generation alongside genome copying.",
                    "timing_and_cue": "Mount cellular apparatus on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_16.webp | Complete Cell Duplication | Creating cellular organelles and membranes to support replicated DNA\")"
                },
                {
                    "concept_title": "Biochemical Error & Variation: No biochemical copying mechanism is 100% reliable; subtle copying errors during DNA replication introduce genetic variations, making offspring subtly distinct from parents.",
                    "diagram_title": "Genetic Variation & Morphological Diversity",
                    "diagram_type": "image",
                    "image_query": "genetic variation DNA copying errors diversity diagram",
                    "video_query": "how DNA copying leads to variation",
                    "image_url": "/extracted_diagrams/ch11/fig_11_17.webp",
                    "what_to_make": "Textbook diagram showing distinct developmental phenotypes across insect life stages.",
                    "timing_and_cue": "Mount replication variation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_17.webp | Replication Inaccuracies | Inherent biochemical variations producing phenotypic diversity\")"
                },
                {
                    "concept_title": "Survival Value of Variations: Variations are not necessarily beneficial to an individual, but they are vital for the survival of the species over time under severe environmental changes (e.g., global warming, drought, epidemics).",
                    "diagram_title": "Ecological Adaptation & Natural Selection",
                    "diagram_type": "image",
                    "image_query": "importance of variation natural selection species survival diagram",
                    "video_query": "importance of variation in organisms class 10",
                    "image_url": "/extracted_diagrams/ch11/fig_11_17.webp",
                    "what_to_make": "Textbook diagram illustrating adaptive survival across environmental transformations.",
                    "timing_and_cue": "Mount survival variation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_17.webp | Survival Value of Variation | Genetic plasticity protecting populations during climatic catastrophes\")"
                },
                {
                    "concept_title": "Metamorphosis & Developmental Plasticity: In holometabolous insects like butterflies, reproduction initiates an embryonic and larval life cycle (egg -> larva/caterpillar -> pupa/chrysalis -> adult butterfly) where distinct body plans adapt to different ecological niches.",
                    "diagram_title": "Complete Metamorphosis of Butterfly",
                    "diagram_type": "image",
                    "image_query": "life cycle of butterfly egg larva caterpillar pupa chrysalis adult diagram",
                    "video_query": "butterfly metamorphosis life cycle animation",
                    "image_url": "/extracted_diagrams/ch11/fig_11_17.webp",
                    "what_to_make": "Textbook diagram of the four developmental stages of the butterfly life cycle.",
                    "timing_and_cue": "Mount butterfly metamorphosis on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_17.webp | Butterfly Metamorphosis | Four-stage holometabolous development: Egg, Larva, Pupa, Adult\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "If an animal never reproduces in its entire life, will it drop dead? If not, why is reproduction considered a fundamental characteristic of life?"
   - Law: Detail DNA copying fidelity, chromosomes, and the survival value of variations.
   - Socratic check: "Why is an exact, 100% photocopy of parental DNA actually dangerous for the long-term survival of a species?" HARD STOP: Wait for student answer!"""
    }

    # Module 2: Modes of Asexual Reproduction: Fission, Budding, Spores, Fragmentation & Regeneration
    m2 = {
        "order_index": 2,
        "title": "Asexual Reproduction Strategies: Fission, Budding, Spores, Fragmentation & Regeneration",
        "description": "Examine uniparental asexual reproduction across unicellular and simple multicellular organisms: binary vs multiple fission, budding in Hydra/Yeast, spore formation in Rhizopus, fragmentation in Spirogyra, and regeneration in Planaria.",
        "subtopics": [
            "Asexual vs Sexual Reproduction: Single parent, zero gametic fusion, mitotic cloning",
            "Binary Fission: Non-directional in Amoeba vs longitudinal along flagellum in Leishmania",
            "Multiple Fission: Cyst formation and simultaneous multiple daughter cells in Plasmodium",
            "Budding in Hydra and Yeast: Outgrowth developing into miniature clone through repetitive mitosis",
            "Spore Formation in Rhizopus: Aerial sporangia containing thick-walled desiccation-resistant spores",
            "Fragmentation vs Regeneration: Natural reproductive splitting in Spirogyra vs tissue repair in Planaria"
        ],
        "key_concepts": [
            "Asexual Reproduction Definition: A mode of reproduction involving a single parent without the production or fusion of gametes, producing genetically identical clones of the parent organism.",
            "Binary Fission (Amoeba & Leishmania): In Amoeba, cell division occurs across any plane; in Leishmania (the pathogen causing Kala-azar / visceral leishmaniasis), binary fission occurs in a definite longitudinal orientation relative to the whip-like flagellum at one end.",
            "Multiple Fission (Plasmodium): Under adverse conditions, the malarial parasite Plasmodium forms a protective cyst around itself; the nucleus divides repeatedly by mitosis into numerous nuclei, which synchronously hatch into hundreds of daughter cells upon cyst rupture.",
            "Budding Mechanics (Hydra & Yeast): A small regenerative outgrowth or 'bud' forms on the parent body through repeated localized mitotic cell divisions; the bud grows, develops mouth and tentacles (in Hydra), and detaches to live independently.",
            "Spore Formation (Rhizopus): In bread mould (Rhizopus), thread-like non-reproductive hyphae give rise to erect bloblike structures called sporangia; sporangia contain hundreds of spores protected by thick walls that resist harsh heat and drought until landing on moist food.",
            "Fragmentation vs Regeneration: Fragmentation is a natural reproductive method in simple multicellular organisms like Spirogyra, which simply break into smaller fragments upon maturity; Regeneration (in Planaria and Hydra) is the specialized ability of damaged organisms to regrow lost body parts, which is not purely a reproductive strategy."
        ],
        "success_criteria": "Student can contrast binary fission in Amoeba vs Leishmania, detail multiple fission in Plasmodium, describe budding, spore formation, and distinguish fragmentation from regeneration.",
        "chapter_notes": """### 11.6 Asexual Reproduction
In **asexual reproduction**, a single parent gives rise to new offspring without gamete fusion. Offspring are genetic clones.

### 11.7 The Five Primary Asexual Strategies

#### 1. Fission
- **Binary Fission**: A single unicellular organism divides into two identical daughter cells.
  - *Amoeba*: Division of nucleus (karyokinesis) followed by cytoplasm (cytokinesis) occurs across **any plane**.
  - *Leishmania* (causes Kala-azar): Possesses a whip-like flagellum; binary fission occurs strictly in a **fixed longitudinal orientation** relative to the flagellum.
- **Multiple Fission**:
  - *Plasmodium* (malarial parasite): Encysts during stress; nucleus divides repeatedly into hundreds of nuclei. Upon favorable conditions, the cyst wall bursts, releasing hundreds of daughter individuals simultaneously.

#### 2. Fragmentation
- Occurs in simple multicellular organisms with unspecialized tissue (e.g., green filamentous alga ***Spirogyra***).
- Upon reaching maturity, the long filament simply breaks into two or more smaller fragments, each of which elongates via mitosis into a complete new filament.

#### 3. Regeneration
- Demonstrated by ***Planaria*** (flatworm) and ***Hydra***.
- If cut into several pieces, specialized regenerative cells proliferate and differentiate into all missing body tissues, forming complete organisms.
- *Crucial Note*: Regeneration is a repair/healing mechanism and is **NOT synonymous with reproduction**, because normal organisms do not depend on being chopped to pieces to multiply!

#### 4. Budding
- ***Hydra***: Uses specialized regenerative cells. A localized bulge forms on the side wall due to repeated mitotic division. It develops a mouth and tentacles, and when fully mature, pinches off to lead an independent life.
- ***Yeast*** (unicellular fungus): Small buds pinch off the parent cell, sometimes forming chains of buds before separating.

#### 5. Spore Formation
- Typical of common bread mould (***Rhizopus***).
- Aerial vertical stalks terminate in swollen bulbous sacs called **sporangia**.
- Sporangia contain hundreds of microscopic **spores** covered with tough, thick protective coats that resist drying and extreme temperatures.
- When the sporangium matures and ruptures, spores disperse through air; landing on moist bread, they germinate into hyphae.""",
        "worked_examples": [
            {
                "problem": "How does binary fission in Amoeba differ fundamentally from binary fission in Leishmania?",
                "given": "Cellular morphology and division planes of Amoeba vs Leishmania.",
                "formula": "Plane of Cytokinesis Symmetry",
                "substitution": "Amorphous shape of Amoeba vs whip-like flagellar polarity of Leishmania.",
                "calculation": "1. In Amoeba, the cell has no fixed shape (amorphous); nuclear and cytoplasmic division can take place along ANY plane.\n2. In Leishmania (the causative agent of kala-azar), the cell has a definite whip-like flagellum at one end.\n3. Binary fission in Leishmania occurs in a strictly definite, fixed longitudinal plane in relation to this flagellar structure.",
                "finalAnswer": "Amoeba divides along any plane, whereas Leishmania divides strictly in a fixed longitudinal plane relative to its whip-like flagellum.",
                "unit": "Protozoan Fission",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.16: Cellular division plane in protozoans"
            },
            {
                "problem": "Why cannot complex multicellular organisms like humans, dogs, or birds reproduce by fragmentation or regeneration as Spirogyra and Planaria do?",
                "given": "Simple tissue-level organization vs complex organ-system architecture.",
                "formula": "Cellular Specialization & Organ System Hierarchy",
                "substitution": "Spirogyra: simple chain of identical cells; Mammals: deeply specialized tissues.",
                "calculation": "1. Simple organisms like Spirogyra are merely chains of identical, unspecialized cells; any fragment contains all necessary cell types to survive.\n2. Complex multicellular organisms exhibit advanced cellular differentiation into specialized tissues, organs, and organ systems placed at definite locations.\n3. Highly differentiated cells (like nerve cells, heart muscle cells) lose the totipotent ability to de-differentiate and regenerate entire organ systems.\n4. Hence, cell-by-cell or fragment division is impossible in complex organisms.",
                "finalAnswer": "Complex organisms have specialized cells organized into intricate organ systems that cannot regenerate an entire body from a fragment.",
                "unit": "Tissue Complexity",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.17: Complex multicellular organ differentiation"
            },
            {
                "problem": "How will an organism be benefited if it reproduces through spores? Explain using Rhizopus (bread mould).",
                "given": "Spore formation in Rhizopus.",
                "formula": "Dormancy and Protective Spore Coat Kinetics",
                "substitution": "Thick-walled spores surviving adverse environmental conditions.",
                "calculation": "1. Spores are encased in thick, durable protective cell walls that protect the internal protoplasm from desiccation, extreme heat, and lack of moisture.\n2. Spores are extraordinarily lightweight and produced in massive numbers, allowing vast dispersal by air currents.\n3. They remain dormant for months until they settle on a suitable nutrient substrate (like moist bread), germinating immediately when moisture and temperature are favorable.",
                "finalAnswer": "Spores have thick protective coats that resist harsh weather, are easily dispersed by wind in vast numbers, and remain viable until favorable conditions return.",
                "unit": "Spore Survival",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.1: Spore and vegetative propagation structures"
            },
            {
                "problem": "Why is regeneration not considered the same as reproduction? Explain using Planaria.",
                "given": "Regeneration in Planaria after injury.",
                "formula": "Accidental Tissue Repair vs Programmed Life-Cycle Propagation",
                "substitution": "Planaria cut into pieces vs normal developmental reproduction.",
                "calculation": "1. Reproduction is a natural, programmed physiological process by which organisms actively multiply their numbers as part of their regular life cycle.\n2. Regeneration is essentially an accidental wound healing and tissue repair mechanism mediated by localized stem cells when an organism is damaged or severed.\n3. Most organisms cannot rely on being cut or mutilated to reproduce; many organisms (like lizards regenerating tails) exhibit regeneration without producing new individuals.",
                "finalAnswer": "Regeneration is an accidental tissue repair mechanism after trauma, not a natural, programmed reproductive strategy.",
                "unit": "Regenerative Biology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.16: Cellular proliferation in regenerative repair"
            },
            {
                "problem": "Describe how multiple fission in Plasmodium provides an adaptive advantage inside the human host.",
                "given": "Malarial parasite Plasmodium infecting human erythrocytes and hepatocytes.",
                "formula": "Exponential Daughter Progeny Production via Cyst Bursting",
                "substitution": "Single infection resulting in hundreds of synchronous merozoites.",
                "calculation": "1. Inside a protective cyst or red blood cell, Plasmodium undergoes repeated nuclear mitosis without immediate cytokinesis.\n2. When the cell membrane finally ruptures, hundreds of active daughter merozoites are released simultaneously into the bloodstream.\n3. This synchronous release overwhelms the host's immune defense mechanisms and ensures rapid, widespread infection of new red blood cells.",
                "finalAnswer": "Multiple fission produces hundreds of daughter parasites simultaneously, overwhelming host immune defenses and ensuring rapid systemic propagation.",
                "unit": "Parasitology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.16: Multiple fission within protective cyst"
            },
            {
                "problem": "Compare budding in Hydra with budding in Yeast in terms of cellular organization and detachment.",
                "given": "Multicellular Hydra vs unicellular Yeast.",
                "formula": "Multicellular Outgrowth vs Unicellular Cytoplasmic Budding",
                "substitution": "Hydra develops mouth/tentacles; Yeast forms cellular chains.",
                "calculation": "1. In multicellular Hydra, the bud is composed of thousands of organized ectodermal and endodermal cells that develop into a miniature animal with mouth and tentacles before detaching.\n2. In unicellular Yeast, the bud is a small cytoplasmic protrusion receiving a daughter nucleus.\n3. Yeast buds often do not detach immediately, forming long branched chains of cells, whereas Hydra buds strictly detach upon maturity.",
                "finalAnswer": "Hydra budding involves multicellular differentiation into a miniature animal with tentacles; Yeast budding is unicellular and can form chained colonies.",
                "unit": "Comparative Budding",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.1: Budding mechanisms in lower organisms"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Planaria cuts itself into pieces whenever it wants to reproduce.",
                "correction": "Planaria does not cut itself up to reproduce. Regeneration is an emergency repair mechanism that enables it to regrow into complete worms if accidentally sliced by a predator. For normal reproduction, Planaria reproduces sexually or by transverse constriction.",
                "why_it_matters": "Distinguishes physiological reproduction from accidental injury healing."
            }
        ],
        "visual_lesson_plan": {
            "title": "Asexual Reproduction Strategies Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Asexual Reproduction Definition: A mode of reproduction involving a single parent without the production or fusion of gametes, producing genetically identical clones of the parent organism.",
                    "diagram_title": "Asexual Mitotic Cloning Framework",
                    "diagram_type": "image",
                    "image_query": "asexual reproduction single parent cloning diagram",
                    "video_query": "asexual reproduction methods overview",
                    "image_url": "/extracted_diagrams/ch11/fig_11_1.webp",
                    "what_to_make": "Textbook diagram showing vegetative asexual propagation generating identical clonal plantlets.",
                    "timing_and_cue": "Mount asexual framework on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_1.webp | Asexual Reproduction Overview | Single-parent mitotic proliferation producing identical genetic clones\")"
                },
                {
                    "concept_title": "Binary Fission (Amoeba & Leishmania): In Amoeba, cell division occurs across any plane; in Leishmania (the pathogen causing Kala-azar / visceral leishmaniasis), binary fission occurs in a definite longitudinal orientation relative to the whip-like flagellum at one end.",
                    "diagram_title": "Binary Fission in Amoeba & Leishmania",
                    "diagram_type": "image",
                    "image_query": "binary fission amoeba leishmania longitudinal division diagram",
                    "video_query": "binary fission in amoeba and leishmania",
                    "image_url": "/extracted_diagrams/ch11/fig_11_16.webp",
                    "what_to_make": "Textbook diagram showing nuclear elongation, division plane, and cytokinesis.",
                    "timing_and_cue": "Mount binary fission on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_16.webp | Binary Fission Planes | Any plane in Amoeba versus longitudinal plane in flagellated Leishmania\")"
                },
                {
                    "concept_title": "Multiple Fission (Plasmodium): Under adverse conditions, the malarial parasite Plasmodium forms a protective cyst around itself; the nucleus divides repeatedly by mitosis into numerous nuclei, which synchronously hatch into hundreds of daughter cells upon cyst rupture.",
                    "diagram_title": "Multiple Fission in Encysted Plasmodium",
                    "diagram_type": "image",
                    "image_query": "multiple fission plasmodium cyst daughter cells diagram",
                    "video_query": "multiple fission in plasmodium animation",
                    "image_url": "/extracted_diagrams/ch11/fig_11_16.webp",
                    "what_to_make": "Textbook diagram showing encysted cell with repeated nuclear division bursting into daughter cells.",
                    "timing_and_cue": "Mount multiple fission on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_16.webp | Multiple Fission | Synchronous release of hundreds of daughter cells upon cyst rupture\")"
                },
                {
                    "concept_title": "Budding Mechanics (Hydra & Yeast): A small regenerative outgrowth or 'bud' forms on the parent body through repeated localized mitotic cell divisions; the bud grows, develops mouth and tentacles (in Hydra), and detaches to live independently.",
                    "diagram_title": "Budding in Hydra & Miniature Detachment",
                    "diagram_type": "image",
                    "image_query": "budding in hydra tentacles yeast bud diagram",
                    "video_query": "budding in hydra under microscope",
                    "image_url": "/extracted_diagrams/ch11/fig_11_1.webp",
                    "what_to_make": "Textbook diagram illustrating localized cellular proliferation forming miniature independent offspring.",
                    "timing_and_cue": "Mount budding on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_1.webp | Budding in Hydra | Localized mitotic outgrowth developing tentacles and detaching\")"
                },
                {
                    "concept_title": "Spore Formation (Rhizopus): In bread mould (Rhizopus), thread-like non-reproductive hyphae give rise to erect bloblike structures called sporangia; sporangia contain hundreds of spores protected by thick walls that resist harsh heat and drought until landing on moist food.",
                    "diagram_title": "Spore Formation in Bread Mould Rhizopus",
                    "diagram_type": "image",
                    "image_query": "spore formation rhizopus bread mould sporangium hyphae diagram",
                    "video_query": "spore formation in rhizopus bread mould",
                    "image_url": "/extracted_diagrams/ch11/fig_11_1.webp",
                    "what_to_make": "Textbook diagram of Rhizopus showing hyphae, erect sporangiophores, and sporangia releasing spores.",
                    "timing_and_cue": "Mount spore formation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_1.webp | Spore Formation in Rhizopus | Thick-walled protective spores released from aerial sporangia\")"
                },
                {
                    "concept_title": "Fragmentation vs Regeneration: Fragmentation is a natural reproductive method in simple multicellular organisms like Spirogyra, which simply break into smaller fragments upon maturity; Regeneration (in Planaria and Hydra) is the specialized ability of damaged organisms to regrow lost body parts, which is not purely a reproductive strategy.",
                    "diagram_title": "Spirogyra Fragmentation vs Planaria Regeneration",
                    "diagram_type": "image",
                    "image_query": "fragmentation spirogyra regeneration planaria diagram",
                    "video_query": "fragmentation in spirogyra vs regeneration in planaria",
                    "image_url": "/extracted_diagrams/ch11/fig_11_16.webp",
                    "what_to_make": "Textbook diagram comparing simple filament fragmentation with complex stem-cell regeneration.",
                    "timing_and_cue": "Mount fragmentation vs regeneration on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_16.webp | Fragmentation vs Regeneration | Natural filament division in Spirogyra versus wound-healing regeneration in Planaria\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "If you cut a lizard's tail off, it grows a new tail, but the severed tail doesn't grow a new lizard. Is that reproduction or regeneration?"
   - Law: Define binary/multiple fission, budding, spores, fragmentation, and regeneration.
   - Socratic check: "Why does Leishmania divide only along a strict longitudinal line, whereas Amoeba can divide in any direction?" HARD STOP: Wait for student answer!"""
    }

    # Module 3: Vegetative Propagation: Natural & Artificial Techniques
    m3 = {
        "order_index": 3,
        "title": "Vegetative Propagation in Plants: Natural Adaptations & Agronomic Innovations",
        "description": "Analyze natural vegetative propagation via roots, stems (tubers, rhizomes, runners), and leaves (Bryophyllum), evaluate artificial horticultural techniques (cutting, layering, grafting), and examine tissue culture micropropagation.",
        "subtopics": [
            "What is Vegetative Propagation: Formation of new plants from vegetative parts (roots, stems, leaves)",
            "Natural Vegetative Propagation: Bryophyllum leaf margin buds, potato tuber eyes, ginger rhizomes",
            "Artificial Propagation - Cutting: Stem cuttings in rose, sugarcane, and bougainvillea",
            "Artificial Propagation - Layering: Simple and mound layering in jasmine and strawberry",
            "Artificial Propagation - Grafting: Combining rootstock (stock) and shoot scion in mango and apple",
            "Micropropagation & Plant Tissue Culture: Growing clones on sterile nutrient agar with phytohormones"
        ],
        "key_concepts": [
            "Vegetative Propagation Principle: A form of asexual reproduction in plants where new individuals develop from vegetative structures such as roots, stems, or leaves, without the production of seeds or spores.",
            "Leaf Propagation in Bryophyllum: The leaves of Bryophyllum produce adventitious buds in the notches along their margins; when mature leaves detach and fall on moist soil, each bud develops roots and shoots into a viable independent plant.",
            "Stem Adaptations (Tubers & Rhizomes): Potato tubers possess modified vegetative buds called 'eyes' capable of sprouting; ginger and turmeric reproduce through underground creeping stems called rhizomes; onions reproduce via modified bulbs.",
            "Artificial Horticultural Techniques: Cutting (planting a severed stem with nodes in moist soil, e.g., rose), Layering (bending a lower branch into moist soil to develop adventitious roots before cutting from parent, e.g., jasmine), Grafting (joining the shoot scion of a high-yield plant onto the rooted stock of a hardy plant).",
            "Tissue Culture (Micropropagation): Cells or small tissue explants from the growing shoot tip of a plant are placed on a sterile nutrient medium containing vitamins and hormones to form an undifferentiated cellular mass called a callus; hormones induce differentiation into plantlets, producing thousands of disease-free clones.",
            "Agronomic Advantages: Vegetative propagation enables propagation of seedless fruit varieties (banana, seedless grapes, oranges), yields earlier flowering and fruiting compared to seed-grown plants, and produces genetically identical crops with uniform yield and taste."
        ],
        "success_criteria": "Student can describe Bryophyllum leaf propagation, explain cutting, layering, and grafting, outline tissue culture steps, and list advantages of vegetative propagation.",
        "chapter_notes": """### 11.8 Natural Vegetative Propagation
In many angiosperms, vegetative organs develop adventitious buds that generate complete new plants:
1. **By Roots**: *Sweet potato (Ipomoea batatas)*, *Dahlia*, and *Guava* develop adventitious root tubers that sprout new leafy shoots.
2. **By Stems**:
   - **Tuber**: *Potato* tubers are swollen underground stems bearing 'eyes' (nodes with dormant buds). Planting a potato piece containing at least one eye produces a new plant.
   - **Rhizome**: Underground horizontal stems in *Ginger* and *Turmeric* bearing nodes and scale leaves.
   - **Bulb**: Compressed underground stems in *Onion* and *Garlic*.
   - **Runners / Stolons**: Horizontal creeping stems in *Mint* and *Grass*.
3. **By Leaves**:
   - ***Bryophyllum*** (*Kalanchoe*): Distinct notches along the fleshy leaf margins contain dormant buds. When a leaf detaches and falls on damp earth, these buds rapidly develop adventitious roots and leafy shoots, forming miniature plantlets.

### 11.9 Artificial Methods of Vegetative Propagation
Used extensively in agriculture and horticulture:
- **1. Cutting**: A severed portion of a stem bearing active axillary nodes is planted in moist soil (e.g., *Rose, Sugarcane, Bougainvillea, Grapes*). Adventitious roots develop at the base.
- **2. Layering**: A lower flexible branch is bent downward, pegged into moist soil with its growing tip left exposed above ground (Activity 11.4). After roots sprout at the buried node, the branch is severed from the mother plant (e.g., *Jasmine, Strawberry, Hibiscus*).
- **3. Grafting**: Two distinct plant stems are cut at an angle and bound together with cambial layers aligned:
  - **Stock**: The rooted, disease-resistant plant portion.
  - **Scion**: The upper stem cutting of a high-quality fruiting/flowering variety (e.g., *Mango, Apple, Rose*).

### 11.10 Plant Tissue Culture (Micropropagation)
1. A tiny explant (group of cells from shoot apical meristem) is excised under strictly sterile conditions.
2. Cultured on nutrient agar containing inorganic salts, sucrose, vitamins, and growth hormones (auxins and cytokinins).
3. The cells divide rapidly into an unorganized cellular mass called a **Callus**.
4. The callus is transferred to hormone-adjusted media to stimulate shoot and root morphogenesis into **Plantlets**.
5. *Benefits*: Thousands of disease-free, identical plants can be grown from a single plant in a small laboratory area throughout the year.""",
        "worked_examples": [
            {
                "problem": "How does vegetative propagation take place in the leaves of Bryophyllum? Detail the role of leaf notches.",
                "given": "Fleshy leaf anatomy of Bryophyllum with margin notches.",
                "formula": "Adventitious Folia Bud Development Kinetics",
                "substitution": "Dormant buds in notches stimulated by contact with damp soil.",
                "calculation": "1. The margins of Bryophyllum leaves feature distinct serrated notches.\n2. In these notches lie specialized clusters of dormant adventitious vegetative buds.\n3. As long as the leaf is attached to the parent plant, apical dominance and hydration keep the buds dormant.\n4. When a mature leaf falls onto moist soil, moisture and ground contact trigger rapid cell division.\n5. The buds sprout roots downward into the soil and miniature leafy shoots upward, developing into viable independent plantlets.",
                "finalAnswer": "Adventitious buds in leaf margin notches sprout roots and shoots upon falling on moist soil, growing into new independent plants.",
                "unit": "Foliar Propagation",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.1: Bryophyllum leaf showing plantlets sprouting in margin notches"
            },
            {
                "problem": "Explain the horticultural process of grafting. What are the 'stock' and 'scion', and what biological condition is essential for a successful graft union?",
                "given": "Grafting technique in commercial fruit orchards.",
                "formula": "Vascular Cambium Coalescence",
                "substitution": "Stock (rooted base) joined to Scion (fruiting stem).",
                "calculation": "1. Grafting joins two plant stems so they grow as a single unified plant.\n2. **Stock**: The lower plant portion rooted in the soil, selected for deep root vigor and disease resistance.\n3. **Scion**: The upper severed stem cutting from a superior donor plant, selected for sweet fruit or fragrant flowers.\n4. **Essential Biological Invariant**: The **vascular cambium** layers of both stock and scion must be placed in direct, intimate contact and tied tightly with waterproof tape to enable vascular reconnection of xylem and phloem.",
                "finalAnswer": "Stock is the rooted base; scion is the superior shoot; vascular cambium layers must align perfectly for continuous xylem/phloem flow.",
                "unit": "Horticultural Grafting",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.2: Artificial vegetative propagation techniques"
            },
            {
                "problem": "Describe an activity to demonstrate layering in a jasmine plant (Activity 11.4).",
                "given": "Activity 11.4: Layering in flexible-stem plants.",
                "formula": "Soil-Induced Adventitious Rooting at Intact Node",
                "substitution": "Bending low branch of jasmine into soil without severing.",
                "calculation": "1. Select a healthy, flexible lower branch of a mature jasmine plant growing close to the ground.\n2. Defoliate the middle portion of this branch and scrape off a thin ring of outer bark to expose cambium.\n3. Bend the branch downward, bury the scraped node under 5-8 cm of moist soil, and secure it with a wooden peg or stone, leaving the branch tip upright above ground.\n4. Water the buried area regularly for 3 to 4 weeks.\n5. Adventitious roots sprout profusely from the buried node.\n6. Cut the branch away from the mother plant; it now grows as an independent jasmine plant.",
                "finalAnswer": "A low branch is bent, scraped at a node, buried in moist soil until roots sprout, and then severed from the parent plant.",
                "unit": "Activity 11.4 Lab Analysis",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.4: Technique of layering in plants"
            },
            {
                "problem": "State four distinct agronomic and commercial advantages of vegetative propagation over growing crops from seeds.",
                "given": "Agricultural economics of vegetative propagation vs seed germination.",
                "formula": "Clonal Uniformity & Reproductive Acceleration",
                "substitution": "Fruit trees, seedless cultivars, and disease management.",
                "calculation": "1. **Seedless Crop Cultivation**: Allows propagation of economically valuable crops that have lost the ability to produce viable seeds (e.g., commercial bananas, seedless grapes, oranges, jasmine, rose).\n2. **Clonal Genetic Uniformity**: All offspring are exact genetic clones of the parent, ensuring uniform fruit size, sweetness, flavor, and harvest timing.\n3. **Accelerated Fruiting**: Plants raised by vegetative propagation bear flowers and fruits much earlier than plants grown from seeds.\n4. **Propagation of Clones from Single Parent**: Only one parent plant is needed; beneficial genetic traits are never lost or diluted by genetic recombination.",
                "finalAnswer": "1. Enables seedless crop cultivation, 2. Preserves exact desirable traits (clones), 3. Flowers and fruits earlier, 4. Requires only one parent.",
                "unit": "Agronomy",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.1: Vegetative propagation agronomic applications"
            },
            {
                "problem": "Explain the biological principle of plant tissue culture (micropropagation). Why is it conducted in strictly sterile conditions?",
                "given": "Totipotency of plant meristematic explants.",
                "formula": "Explant -> Callus (Nutrient Agar + Auxins/Cytokinins) -> Plantlets",
                "substitution": "Sterile nutrient medium preventing bacterial and fungal overgrowth.",
                "calculation": "1. Principle: Plant apical cells possess **totipotency** (the biological ability of a single vegetative cell to regenerate an entire multicellular plant).\n2. A tiny explant from the shoot tip is placed on an agar medium containing sucrose, amino acids, and balanced ratios of auxins and cytokinins to form an undifferentiated callus.\n3. Modulating hormone concentrations triggers organogenesis (root and shoot differentiation).\n4. Sterile conditions are mandatory because the rich sugary nutrient agar is an ideal breeding ground for airborne bacteria and mold, which would quickly smother and destroy the delicate plant tissues.",
                "finalAnswer": "Relies on cellular totipotency to grow thousands of disease-free plantlets from an explant; sterile conditions prevent lethal bacterial/mold contamination.",
                "unit": "Biotechnology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.2: Micropropagation and artificial propagation methods"
            },
            {
                "problem": "If a farmer cuts a potato into four pieces and plants them in soil, why will some pieces grow into healthy potato plants while others rot away?",
                "given": "Potato tuber anatomy with localized 'eyes' (nodes).",
                "formula": "Presence of Vegetative Meristematic Buds ('Eyes')",
                "substitution": "Pieces with eyes contain axillary buds; pieces without eyes contain only starchy storage parenchyma.",
                "calculation": "1. A potato is a modified underground storage stem. Its 'eyes' are actually stem nodes containing dormant axillary vegetative buds.\n2. A potato piece that includes at least one intact eye has the meristematic tissue required to initiate cellular division, sprout roots, and develop leafy green shoots.\n3. A potato piece that lacks an eye consists purely of starch-storing parenchyma cells without any meristematic buds.\n4. Lacking growing points, it cannot sprout and simply decomposes in the moist soil.",
                "finalAnswer": "Only potato pieces containing an 'eye' possess meristematic buds capable of sprouting roots and shoots; pieces without eyes simply decompose.",
                "unit": "Tuber Morphogenesis",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.1: Tuber buds and foliar plantlet sprouting"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "You can bury any random slice of a potato tuber and it will always grow into a new plant.",
                "correction": "Only potato pieces that contain at least one 'eye' (the nodal dormant bud) can sprout into a new plant. A piece cut entirely from the eye-less center consists only of dead starch storage tissue and will simply rot in the dirt.",
                "why_it_matters": "Fundamental rule of plant meristematic tissue presence in vegetative reproduction."
            }
        ],
        "visual_lesson_plan": {
            "title": "Vegetative Propagation Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Vegetative Propagation Principle: A form of asexual reproduction in plants where new individuals develop from vegetative structures such as roots, stems, or leaves, without the production of seeds or spores.",
                    "diagram_title": "Bryophyllum Leaf Notch Propagation",
                    "diagram_type": "image",
                    "image_query": "bryophyllum leaf vegetative propagation adventitious buds diagram",
                    "video_query": "bryophyllum leaf propagation under microscope",
                    "image_url": "/extracted_diagrams/ch11/fig_11_1.webp",
                    "what_to_make": "Textbook diagram of Bryophyllum leaf showing adventitious buds sprouting roots and shoots in margin notches.",
                    "timing_and_cue": "Mount Bryophyllum on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_1.webp | Bryophyllum Foliar Propagation | Adventitious buds sprouting roots and shoots in leaf margin notches\")"
                },
                {
                    "concept_title": "Leaf Propagation in Bryophyllum: The leaves of Bryophyllum produce adventitious buds in the notches along their margins; when mature leaves detach and fall on moist soil, each bud develops roots and shoots into a viable independent plant.",
                    "diagram_title": "Stem Cutting Technique in Horticulture",
                    "diagram_type": "image",
                    "image_query": "stem cutting vegetative propagation rose sugarcane diagram",
                    "video_query": "how to propagate plants from stem cuttings",
                    "image_url": "/extracted_diagrams/ch11/fig_11_2.webp",
                    "what_to_make": "Textbook diagram showing severed stem cuttings planted in moist soil producing adventitious roots.",
                    "timing_and_cue": "Mount stem cutting on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_2.webp | Stem Cutting Technique | Inserting severed node in soil to induce adventitious root growth\")"
                },
                {
                    "concept_title": "Stem Adaptations (Tubers & Rhizomes): Potato tubers possess modified vegetative buds called 'eyes' capable of sprouting; ginger and turmeric reproduce through underground creeping stems called rhizomes; onions reproduce via modified bulbs.",
                    "diagram_title": "Underground Stem Morphologies",
                    "diagram_type": "image",
                    "image_query": "potato tuber eyes ginger rhizome onion bulb vegetative propagation diagram",
                    "video_query": "vegetative propagation from underground stems",
                    "image_url": "/extracted_diagrams/ch11/fig_11_1.webp",
                    "what_to_make": "Textbook diagram of modified underground storage organs bearing active nodal buds.",
                    "timing_and_cue": "Mount underground stems on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_1.webp | Underground Stem Organs | Potato eyes, ginger rhizomes, and onion bulbs sprouting shoots\")"
                },
                {
                    "concept_title": "Artificial Horticultural Techniques: Cutting (planting a severed stem with nodes in moist soil, e.g., rose), Layering (bending a lower branch into moist soil to develop adventitious roots before cutting from parent, e.g., jasmine), Grafting (joining the shoot scion of a high-yield plant onto the rooted stock of a hardy plant).",
                    "diagram_title": "Layering Technique in Jasmine Plants",
                    "diagram_type": "image",
                    "image_query": "layering plant propagation jasmine branch bent soil roots diagram",
                    "video_query": "layering technique in plants animation",
                    "image_url": "/extracted_diagrams/ch11/fig_11_4.webp",
                    "what_to_make": "Textbook diagram of a jasmine branch pegged beneath the soil to develop adventitious roots.",
                    "timing_and_cue": "Mount layering on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_4.webp | Plant Layering Method | Bending flexible low branch into soil to establish roots before detachment\")"
                },
                {
                    "concept_title": "Tissue Culture (Micropropagation): Cells or small tissue explants from the growing shoot tip of a plant are placed on a sterile nutrient medium containing vitamins and hormones to form an undifferentiated cellular mass called a callus; hormones induce differentiation into plantlets, producing thousands of disease-free clones.",
                    "diagram_title": "Plant Tissue Culture Callus Differentiation",
                    "diagram_type": "image",
                    "image_query": "plant tissue culture micropropagation callus test tube plantlets diagram",
                    "video_query": "plant tissue culture technique step by step",
                    "image_url": "/extracted_diagrams/ch11/fig_11_2.webp",
                    "what_to_make": "Textbook diagram illustrating explant culture on sterile nutrient agar developing into plantlets.",
                    "timing_and_cue": "Mount tissue culture on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_2.webp | Micropropagation Laboratory | Culturing meristematic explants on nutrient agar to produce disease-free clones\")"
                },
                {
                    "concept_title": "Agronomic Advantages: Vegetative propagation enables propagation of seedless fruit varieties (banana, seedless grapes, oranges), yields earlier flowering and fruiting compared to seed-grown plants, and produces genetically identical crops with uniform yield and taste.",
                    "diagram_title": "Commercial Clonal Orchard Architecture",
                    "diagram_type": "image",
                    "image_query": "seedless banana orange vegetative propagation advantages diagram",
                    "video_query": "advantages of vegetative propagation in agriculture",
                    "image_url": "/extracted_diagrams/ch11/fig_11_1.webp",
                    "what_to_make": "Textbook diagram showing clonal crop uniformity and earlier agricultural fruiting cycles.",
                    "timing_and_cue": "Mount agronomic advantages on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_1.webp | Commercial Orchard Benefits | Propagating seedless bananas and oranges with uniform high-yield harvests\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "Commercial bananas don't have any seeds inside them. If there are no seeds, how on earth do farmers plant millions of new banana trees every year?"
   - Law: Detail natural vegetative propagation (Bryophyllum leaf notches, potato eyes) and artificial techniques (cutting, layering, grafting, tissue culture).
   - Socratic check: "In grafting, why must the cambium layer of the scion touch the cambium layer of the stock?" HARD STOP: Wait for student answer!"""
    }

    # Module 4: Sexual Reproduction in Flowering Plants: Floral Anatomy, Pollination & Fertilization
    m4 = {
        "order_index": 4,
        "title": "Sexual Reproduction in Flowering Plants: Floral Anatomy, Pollination & Double Fertilization",
        "description": "Analyze angiosperm floral whorls (sepals, petals, stamen, pistil), contrast unisexual vs bisexual flowers, trace self vs cross-pollination vectors, examine pollen tube chemotropism, and map post-fertilization seed/fruit transformation.",
        "subtopics": [
            "Floral Anatomy: Calyx (sepals), Corolla (petals), Androecium (stamens), Gynoecium/Pistil (carpels)",
            "Unisexual vs Bisexual Flowers: Papaya/Watermelon (unisexual) vs Hibiscus/Mustard (bisexual)",
            "The Stamen: Filament and anther producing male haploid pollen grains",
            "The Pistil / Carpel: Receptive stigma, elongated style, and swollen basal ovary housing ovules",
            "Pollination Vectors: Self-pollination vs cross-pollination via wind, water, insects, birds",
            "Pollen Germination & Fertilization: Pollen tube chemotropism down style, syngamy, ovary -> fruit, ovule -> seed"
        ],
        "key_concepts": [
            "Angiosperm Flower Structure: The flower is the specialized reproductive organ of angiosperms consisting of four concentric whorls: calyx (protective green sepals), corolla (attractive petals), androecium (male stamens), and gynoecium (female carpel/pistil).",
            "Unisexual vs Bisexual Flowers: Unisexual flowers contain either stamens or carpels but not both (e.g., papaya, watermelon); bisexual flowers contain both stamens and carpels in the same flower (e.g., hibiscus, mustard).",
            "Pistil (Carpel) Architecture: The central female organ composed of three parts: the sticky terminal stigma which receives pollen grains, the elongated slender style through which the pollen tube grows, and the swollen basal ovary which houses one or more ovules containing the female egg cell.",
            "Pollination Mechanisms: Pollination is the transfer of pollen grains from the anther to the stigma; Self-pollination occurs when pollen settles on the stigma of the same flower or another flower on the same plant; Cross-pollination occurs when pollen is transferred to a flower on a different plant of the same species by wind, water, or animal pollinators.",
            "Pollen Tube Chemotropism: After landing on a compatible stigma, the pollen grain absorbs sugary exudates and germinates, producing a long pollen tube that grows down through the style guided chemotropically toward the ovule micropyle.",
            "Post-Fertilization Transformations: Following fertilization (syngamy of male gamete with egg cell): the zygote divides into an embryo, the ovule develops a tough protective coat and becomes the seed, and the ovary ripens and enlarges into the fruit; sepals, petals, and stamens typically shrivel and fall off."
        ],
        "success_criteria": "Student can sketch and label a flower, differentiate unisexual vs bisexual flowers, explain self vs cross-pollination, trace pollen tube germination, and map flower parts to fruit/seed.",
        "chapter_notes": """### 11.11 Anatomy of a Flower
The flower is the reproductive shoot of angiosperms, organized into four concentric whorls:
1. **Calyx (Sepals)**: Outermost green leaf-like structures that enclose and protect the flower in its bud stage.
2. **Corolla (Petals)**: Brightly colored, scented petals that attract insect and bird pollinators.
3. **Androecium (Male Reproductive Organ)**: Composed of **Stamens**.
   - **Filament**: Slender stalk supporting the anther.
   - **Anther**: Bilobed terminal sac containing pollen sacs that produce haploid **pollen grains** (male gametophytes).
4. **Gynoecium / Pistil (Female Reproductive Organ)**: Composed of one or more **Carpels**.
   - **Stigma**: Sticky, receptive landing platform that captures pollen grains.
   - **Style**: Slender neck connecting stigma to ovary.
   - **Ovary**: Swollen basal chamber containing one or more **ovules** (each containing a female egg cell).

### 11.12 Classification of Flowers
- **Unisexual Flowers**: Contain either stamens or carpels (e.g., *Papaya, Watermelon*). Cross-pollination is mandatory.
- **Bisexual Flowers**: Contain both male stamens and female carpels in the same flower (e.g., *Hibiscus, Mustard, Pea*).

### 11.13 Pollination
- **Self-Pollination (Autogamy & Geitonogamy)**: Transfer of pollen from anther to stigma of the same flower or another flower on the same plant.
- **Cross-Pollination (Allogamy / Xenogamy)**: Transfer of pollen from anther of one flower to the stigma of a flower on a completely different plant of the same species. Agents: Wind (anemophily), Insects/Bees (entomophily), Water (hydrophily), Birds (ornithophily). Cross-pollination creates novel genetic combinations.

### 11.14 Pollen Germination & Fertilization (Syngamy)
1. Compatible pollen grains land on the sticky, sugary stigma.
2. The pollen grain germinates, pushing out a **pollen tube** (Activity 11.14).
3. Guided by chemical attractants (**chemotropism**), the pollen tube grows through the style tissues into the ovary and enters the ovule through the **micropyle**.
4. The pollen tube releases two male gametes. One male gamete fuses with the female egg cell (**Syngamy**), producing a diploid **Zygote**.
5. *Post-Fertilization Fate*:
   - Zygote $\\to$ Multicellular **Embryo** (consisting of plumule, radicle, and cotyledons).
   - Ovule $\\to$ **Seed** (encased in a tough seed coat / testa).
   - Ovary $\\to$ **Fruit** (fleshy like mango/tomato or dry like pea pod).
   - Sepals, petals, stamens, style, and stigma dry up and drop off.""",
        "worked_examples": [
            {
                "problem": "Describe the structure of a pistil (carpel) with the help of a labeled diagram (Fig. 11.11). Name the function of each part.",
                "given": "Pistil / Gynoecium anatomy of angiosperm flower.",
                "formula": "Tri-Partite Female Floral Architecture",
                "substitution": "Stigma (reception) + Style (transmission) + Ovary (gametogenesis).",
                "calculation": "1. **Stigma**: The sticky, expanded terminal surface that catches and holds landing pollen grains and secretes sugary fluids to stimulate pollen germination.\n2. **Style**: The long, slender tubular neck that elevates the stigma to catch wind/pollinators and provides a conduit for pollen tube growth.\n3. **Ovary**: The swollen basal chamber that protects ovules; each ovule contains the female gamete (egg cell). Following fertilization, the ovary matures into the fruit.",
                "finalAnswer": "Stigma catches pollen, style guides the pollen tube, and ovary houses ovules and develops into the fruit.",
                "unit": "Floral Morphology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.11: Detailed structure of a pistil (stigma, style, ovary, ovule)"
            },
            {
                "problem": "What is the difference between self-pollination and cross-pollination (Fig. 11.13)? Which produces greater genetic variation in offspring?",
                "given": "Pollen transfer modes in angiosperms.",
                "formula": "Autogamy vs Xenogamy Genetic Recombination",
                "substitution": "Pollen within same plant vs pollen between distinct individuals.",
                "calculation": "1. Self-pollination: Pollen grains are transferred from the anther to the stigma of the same flower or another flower on the same individual plant.\n2. Cross-pollination: Pollen grains are transferred from the anther of one plant to the stigma of a flower on a different plant of the same species.\n3. Cross-pollination mixes genetic material from two distinct parental genomes, generating vastly greater genetic variation, vigor, and disease resistance in offspring.",
                "finalAnswer": "Self-pollination occurs within the same plant; cross-pollination occurs between different plants, generating significantly greater genetic variation.",
                "unit": "Pollination Dynamics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.13: Self-pollination versus cross-pollination mechanisms"
            },
            {
                "problem": "Explain the step-by-step process of pollen germination on the stigma and the growth of the pollen tube leading to fertilization (Fig. 11.14).",
                "given": "Pollen-pistil interaction and siphonogamous fertilization.",
                "formula": "Chemotropic Pollen Tube Growth Cascade",
                "substitution": "Stigmatic exudate -> Pollen tube -> Style -> Micropyle -> Syngamy.",
                "calculation": "1. A viable pollen grain adheres to the moist, sugary stigma and hydrates.\n2. The intine emerges through a germ pore to form a tubular outgrowth called the pollen tube.\n3. The pollen tube secretes pectinases and cellulases to digest a path through the style tissues, guided chemotropically by calcium-sugar gradients.\n4. Two male gamete nuclei travel down the tube.\n5. The tube enters the ovule through the micropylar opening and discharges the male gametes into the embryo sac.\n6. One male gamete fuses with the egg cell nucleus to form the diploid zygote (syngamy).",
                "finalAnswer": "Pollen germinates on stigma, extends a pollen tube down the style via chemotropism, enters the ovule micropyle, and discharges male gametes to fertilize the egg.",
                "unit": "Embryology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.14: Germination of pollen on stigma and pollen tube growth"
            },
            {
                "problem": "What are the post-fertilization changes that occur in a flower to transform it into a fruit and seed (Fig. 11.15)?",
                "given": "Post-fertilization morphogenesis in angiosperms.",
                "formula": "Floral Organ Fate Mapping: Zygote -> Embryo; Ovule -> Seed; Ovary -> Fruit",
                "substitution": "Hormonal shifts triggering ovary wall enlargement into pericarp.",
                "calculation": "1. Zygote undergoes mitotic divisions to develop into an **Embryo** (containing radicle, plumule, cotyledons).\n2. Ovule integuments harden into a tough, protective seed coat (testa) to form the **Seed**.\n3. Ovary wall thickens, swells, and matures under auxin and ethylene influence to become the **Fruit** (pericarp).\n4. Petals, sepals, stamens, style, and stigma wither, senesce, and drop off.",
                "finalAnswer": "Zygote becomes embryo, ovule becomes seed with tough coat, ovary ripens into fruit, and other floral whorls wither and shed.",
                "unit": "Carpology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.15: Transformation of a fertilized ovary into fruit and ovule into seed"
            },
            {
                "problem": "Distinguish between unisexual and bisexual flowers. Give two examples of each.",
                "given": "Distribution of sexual reproductive whorls in flowers.",
                "formula": "Floral Sexuality Classification",
                "substitution": "Monoecious/dioecious unisexual vs hermaphroditic bisexual flowers.",
                "calculation": "1. Unisexual Flower: Possesses either only male stamens (staminate flower) or only female carpels (pistillate flower), but never both. Examples: **Papaya**, **Watermelon**, Cucumber, Maize.\n2. Bisexual Flower: Possesses both male stamens and female carpels within the exact same flower. Examples: **Hibiscus**, **Mustard**, Pea, Rose.",
                "finalAnswer": "Unisexual flowers have only male or only female organs (Papaya, Watermelon); bisexual flowers have both in one flower (Hibiscus, Mustard).",
                "unit": "Floral Classification",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.11: Bisexual flower showing both stamens and pistil"
            },
            {
                "problem": "What will happen if pollination does not take place in a flowering plant? Will fruits and seeds be formed?",
                "given": "Requirement of pollination for fertilization in angiosperms.",
                "formula": "Syngamy Dependency on Pollen Vector",
                "substitution": "No pollination -> no pollen tube -> no syngamy -> ovary fails to set fruit.",
                "calculation": "1. Without pollination, pollen grains never reach the stigma.\n2. Without pollen on the stigma, no pollen tube can germinate, and male gametes cannot reach the female egg cell inside the ovule.\n3. Because fertilization does not occur, the zygote and endosperm are not formed, so **no seeds can develop**.\n4. In natural conditions, the unfertilized ovary produces no growth hormones, withering and dropping off without forming fruit (except in rare artificial parthenocarpic varieties).",
                "finalAnswer": "If pollination fails, fertilization cannot occur; the ovule cannot become a seed, and the ovary withers without forming natural fruit.",
                "unit": "Reproductive Ecology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.13: Pollination as indispensable prerequisite for seed setting"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Pollination and fertilization are the same event.",
                "correction": "Pollination is merely the PHYSICAL TRANSFER of pollen grains from an anther to a stigma (by wind or insects). Fertilization is the subsequent BIOCHEMICAL FUSION of male and female gamete nuclei inside the ovule to form a zygote, occurring hours or days after pollination.",
                "why_it_matters": "Fundamental chronological and biological distinction in plant reproduction."
            }
        ],
        "visual_lesson_plan": {
            "title": "Sexual Reproduction in Flowering Plants Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Angiosperm Flower Structure: The flower is the specialized reproductive organ of angiosperms consisting of four concentric whorls: calyx (protective green sepals), corolla (attractive petals), androecium (male stamens), and gynoecium (female carpel/pistil).",
                    "diagram_title": "Complete Flower Longitudinal Anatomy",
                    "diagram_type": "image",
                    "image_query": "flower anatomy longitudinal section sepals petals stamen carpel diagram",
                    "video_query": "flower anatomy and reproductive parts 3d animation",
                    "image_url": "/extracted_diagrams/ch11/fig_11_11.webp",
                    "what_to_make": "Textbook diagram showing longitudinal section of flower displaying all four whorls.",
                    "timing_and_cue": "Mount floral anatomy on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_11.webp | Anatomy of Angiosperm Flower | Calyx, corolla, male stamens, and female pistil whorls\")"
                },
                {
                    "concept_title": "Unisexual vs Bisexual Flowers: Unisexual flowers contain either stamens or carpels but not both (e.g., papaya, watermelon); bisexual flowers contain both stamens and carpels in the same flower (e.g., hibiscus, mustard).",
                    "diagram_title": "Pistil Structure & Floral Sexuality",
                    "diagram_type": "image",
                    "image_query": "unisexual vs bisexual flower papaya hibiscus diagram",
                    "video_query": "unisexual and bisexual flowers explained",
                    "image_url": "/extracted_diagrams/ch11/fig_11_11.webp",
                    "what_to_make": "Textbook diagram of pistil showing structural components in bisexual flower.",
                    "timing_and_cue": "Mount floral sexuality on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_11.webp | Floral Sexuality | Bisexual flower containing both stamen and pistil on single receptacle\")"
                },
                {
                    "concept_title": "Pistil (Carpel) Architecture: The central female organ composed of three parts: the sticky terminal stigma which receives pollen grains, the elongated slender style through which the pollen tube grows, and the swollen basal ovary which houses one or more ovules containing the female egg cell.",
                    "diagram_title": "Pistil Tri-Partite Anatomy Schema",
                    "diagram_type": "image",
                    "image_query": "pistil carpel stigma style ovary ovule diagram",
                    "video_query": "structure of carpel or pistil in flower",
                    "image_url": "/extracted_diagrams/ch11/fig_11_11.webp",
                    "what_to_make": "Textbook diagram detailing sticky stigma, conducting style, and basal ovary with internal ovule.",
                    "timing_and_cue": "Mount pistil architecture on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_11.webp | Pistil Anatomy | Stigma for pollen landing, style for tube passage, and ovary housing ovules\")"
                },
                {
                    "concept_title": "Pollination Mechanisms: Pollination is the transfer of pollen grains from the anther to the stigma; Self-pollination occurs when pollen settles on the stigma of the same flower or another flower on the same plant; Cross-pollination occurs when pollen is transferred to a flower on a different plant of the same species by wind, water, or animal pollinators.",
                    "diagram_title": "Self vs Cross-Pollination Pathways",
                    "diagram_type": "image",
                    "image_query": "self pollination cross pollination anther stigma insect wind diagram",
                    "video_query": "pollination self vs cross pollination class 10 9",
                    "image_url": "/extracted_diagrams/ch11/fig_11_13.webp",
                    "what_to_make": "Textbook diagram showing pollen transfer vectors for self-pollination and insect cross-pollination.",
                    "timing_and_cue": "Mount pollination on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_13.webp | Pollination Mechanics | Self-pollination within same plant versus cross-pollination between plants\")"
                },
                {
                    "concept_title": "Pollen Tube Chemotropism: After landing on a compatible stigma, the pollen grain absorbs sugary exudates and germinates, producing a long pollen tube that grows down through the style guided chemotropically toward the ovule micropyle.",
                    "diagram_title": "Pollen Germination & Siphonogamy Pathway",
                    "diagram_type": "image",
                    "image_query": "pollen germination stigma pollen tube growth female gametophyte diagram",
                    "video_query": "pollen tube growth and fertilization in plants",
                    "image_url": "/extracted_diagrams/ch11/fig_11_14.webp",
                    "what_to_make": "Textbook diagram of pollen grains germinating on stigma, pushing pollen tube down through style into ovary.",
                    "timing_and_cue": "Mount pollen tube on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_14.webp | Pollen Tube Chemotropism | Pollen tube growing through style to deliver male gametes to ovule\")"
                },
                {
                    "concept_title": "Post-Fertilization Transformations: Following fertilization (syngamy of male gamete with egg cell): the zygote divides into an embryo, the ovule develops a tough protective coat and becomes the seed, and the ovary ripens and enlarges into the fruit; sepals, petals, and stamens typically shrivel and fall off.",
                    "diagram_title": "Ovary to Fruit & Ovule to Seed Metamorphosis",
                    "diagram_type": "image",
                    "image_query": "transformation of ovary into fruit ovule into seed diagram",
                    "video_query": "how flowers turn into fruits post fertilization changes",
                    "image_url": "/extracted_diagrams/ch11/fig_11_15.webp",
                    "what_to_make": "Textbook diagram showing fertilized floral ovary expanding and transforming into a fruit with internal seeds.",
                    "timing_and_cue": "Mount fruit metamorphosis on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_15.webp | Fruit & Seed Development | Swollen ovary transforming into fruit and fertilized ovule into seed\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "When you eat a juicy mango or sweet apple, which exact part of the original flower are you chewing on?"
   - Law: Detail floral anatomy, distinguish unisexual/bisexual, and explain pollination and syngamy.
   - Socratic check: "What happens to the ovule and the ovary after fertilization takes place?" HARD STOP: Wait for student answer!"""
    }

    # Module 5: Human Reproductive Systems: Male Anatomy, Female Anatomy & Gametogenesis
    m5 = {
        "order_index": 5,
        "title": "Human Reproductive Systems: Male Anatomy, Female Anatomy & Pubertal Gametogenesis",
        "description": "Analyze puberty and endocrine regulation (testosterone, estrogen), detail the male reproductive system (scrotal thermoregulation, testes, vas deferens, prostate), and examine the female reproductive system (ovaries, fallopian tubes, uterus).",
        "subtopics": [
            "Puberty & Secondary Sexual Characteristics: Hormonal activation by pituitary gonadotropins",
            "Male Reproductive System: Testes, scrotum thermoregulation ($2-2.5^\\circ\\text{C}$ lower), epididymis",
            "Male Duct System & Accessory Glands: Vas deferens, seminal vesicles, prostate gland, urethra, semen",
            "Female Reproductive System: Ovaries (oogenesis, ovulation), fallopian tubes / oviducts, ampulla",
            "The Uterus & Birth Canal: Muscular myometrium, vascular endometrium, cervix, vagina",
            "Spermatogenesis vs Oogenesis: Millions of motile sperm vs single monthly non-motile ovum"
        ],
        "key_concepts": [
            "Puberty & Endocrine Activation: Puberty is the developmental phase during adolescence when reproductive organs mature and secondary sexual characteristics develop, driven by testosterone in males and estrogen/progesterone in females.",
            "Scrotal Thermoregulation Axiom: The testes are located outside the abdominal cavity in a pouch of skin called the scrotum because normal human body temperature ($37^\\circ\\text{C}$) is too high for viable spermatogenesis; the scrotum maintains a temperature $2\\text{ to }2.5^\\circ\\text{C}$ lower than body core temperature.",
            "Male Accessory Gland Secretions: The seminal vesicles and prostate gland secrete alkaline fluids containing fructose, mucus, and clotting enzymes into the vas deferens; this fluid nourishes sperm, provides a fluid transport medium, and neutralizes vaginal acidity, forming semen.",
            "Female Ovarian Function & Ovulation: Human females are born with thousands of immature oocytes in both ovaries; starting at puberty, one mature ovum is released alternately by one of the ovaries roughly every 28 days (ovulation).",
            "Fallopian Tube (Oviduct) as Site of Fertilization: The fallopian tube captures the released ovum with its ciliated fimbriae; fertilization of the ovum by sperm takes place strictly within the ampulla of the fallopian tube.",
            "The Uterus (Womb) Architecture: The uterus is an elastic, pear-shaped muscular organ designed to nurture a developing fetus; its inner lining (endometrium) thickens with blood vessels every month to prepare for embryonic implantation."
        ],
        "success_criteria": "Student can sketch and label male and female reproductive systems, explain scrotal temperature regulation, describe accessory gland functions, and state the site of fertilization.",
        "chapter_notes": """### 11.15 Puberty & Secondary Sexual Characteristics
**Puberty** is the period of sexual maturation during adolescence:
- **Males**: Deepening of voice (enlarged larynx / Adam's apple), facial/body hair, muscular broadening of shoulders, nocturnal emissions. Regulated by **Testosterone** from testicular Leydig cells.
- **Females**: Breast enlargement, widening of hips/pelvis, onset of menstruation (menarche). Regulated by **Estrogen** and **Progesterone** from ovarian follicles.

### 11.16 Male Reproductive System
1. **Testes (Primary Sex Organs)**:
   - Paired oval organs located outside the abdominal cavity in the **Scrotum**.
   - *Thermoregulation*: Scrotum maintains temperature **$2 - 2.5^\\circ\\text{C}$ lower** than core body temperature ($37^\\circ\\text{C}$), which is an absolute requirement for healthy **spermatogenesis**.
   - Dual function: (a) Production of male gametes (**sperm**), (b) Secretion of male hormone (**testosterone**).
2. **Epididymis**: Tightly coiled tube on testicular posterior where sperm mature and gain motility.
3. **Vas Deferens (Sperm Duct)**: Carries sperm upward from testes into the abdominal cavity, looping over the urinary bladder.
4. **Accessory Glands**:
   - **Seminal Vesicles**: Secrete alkaline fluid rich in fructose (nutrient for sperm).
   - **Prostate Gland**: Secretes thin milky alkaline fluid that activates sperm motility and neutralizes acidity in female vagina.
   - **Semen**: Combined fluid containing sperm (~10%) and glandular secretions (~90%).
5. **Urethra & Penis**: Urethra serves as a common passageway for both urine and semen (never simultaneously). The penis is the erectile copulatory organ delivering sperm into the vagina.

### 11.17 Female Reproductive System
1. **Ovaries (Primary Sex Organs)**:
   - Paired almond-shaped organs in the lower abdominal cavity.
   - Functions: (a) Production of female gametes (**ova / eggs**), (b) Secretion of **estrogen** and **progesterone**.
   - At birth, ovaries contain thousands of immature eggs. Starting at puberty, **one mature egg is released every month** alternately.
2. **Fallopian Tubes (Oviducts)**:
   - Funnel-shaped fimbriated ends pick up the ovum released from the ovary.
   - **Site of Fertilization**: Fusion of sperm and egg occurs strictly in the **ampulla of the fallopian tube**.
3. **Uterus (Womb)**:
   - Inverted pear-shaped, hollow, highly muscular organ.
   - **Endometrium**: Highly vascular inner lining that thickens every month to receive the fertilized blastocyst for **implantation** and nourishment.
4. **Cervix & Vagina**:
   - The cervix is the narrow neck connecting uterus to vagina.
   - The **Vagina** is the elastic muscular tube receiving the penis during intercourse and serving as the birth canal during parturition.""",
        "worked_examples": [
            {
                "problem": "Why are the human testes situated outside the abdominal cavity within the scrotum? What would happen if they failed to descend?",
                "given": "Anatomical position of human testes in scrotal sac.",
                "formula": "Thermoregulatory Spermatogenesis Invariant: T_scrotum = T_core - 2.5 deg C",
                "substitution": "Core body temperature 37 deg C vs viable spermatogenesis temperature ~34.5 deg C.",
                "calculation": "1. Spermatogenesis (the formation of viable sperm) requires a temperature 2 to 2.5 deg C lower than standard human core body temperature (37 deg C).\n2. The scrotum hangs outside the pelvic cavity, dissipating heat and regulating testicular temperature through cremaster and dartos muscle contraction and relaxation.\n3. If testes fail to descend into the scrotum (a clinical condition called cryptorchidism), the higher internal body temperature halts spermatogenesis, leading to permanent sterility, even though testosterone production may persist.",
                "finalAnswer": "Testes lie in the scrotum because sperm production requires a temperature 2-2.5 deg C cooler than core body temperature; failure to descend causes sterility.",
                "unit": "Thermoregulatory Physiology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.18: Anatomical layout of male reproductive system and scrotum"
            },
            {
                "problem": "What are the specific functions performed by the seminal vesicles and prostate gland in the male reproductive system?",
                "given": "Male accessory reproductive glands.",
                "formula": "Semen Alkalinity, Nutrition & Motility Cascade",
                "substitution": "Fructose from seminal vesicles + Alkaline fluid from prostate gland.",
                "calculation": "1. **Seminal Vesicles**: Secrete a thick, viscous alkaline fluid rich in fructose, prostaglandins, and clotting proteins. Fructose provides the metabolic ATP fuel for active sperm flagellar propulsion.\n2. **Prostate Gland**: Secretes a thin, alkaline fluid that neutralizes the natural acidic environment of both the male urethra and female vagina, protecting sperm from acid denaturation and enhancing their swimming motility.\n3. Together, these secretions form the bulk of semen, facilitating fluid transport and viability.",
                "finalAnswer": "Seminal vesicles supply fructose for sperm energy; prostate gland secretes alkaline fluid to neutralize acidity and enhance motility.",
                "unit": "Accessory Endocrinology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.18: Seminal vesicles and prostate gland along vas deferens"
            },
            {
                "problem": "Name the exact anatomical site where fertilization takes place in the human female body. What happens to the ovum if it is not fertilized?",
                "given": "Human female reproductive tract.",
                "formula": "Ampullary-Isthmic Fertilization Locus",
                "substitution": "Fallopian tube (oviduct) lumen.",
                "calculation": "1. Fertilization (the syngamy of sperm with ovum) takes place strictly in the **Fallopian tube (oviduct)**, specifically in the ampullary region.\n2. If the ovum is not fertilized by a sperm within 24 hours of ovulation, it degenerates.\n3. The thickened uterine endometrial lining, built up to receive an embryo, breaks down along with its ruptured blood vessels and the unfertilized egg, exiting the body as **menstruation**.",
                "finalAnswer": "Fertilization occurs in the Fallopian tube (oviduct); if unfertilized, the ovum degenerates and is shed with uterine lining during menstruation.",
                "unit": "Gynaecological Physiology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.19: Female reproductive system showing ovaries, fallopian tubes, uterus"
            },
            {
                "problem": "Trace the path of a sperm cell from its origin in the seminiferous tubules of the testis until it fertilizes an egg cell in the female body.",
                "given": "Sperm transit pathway through male and female reproductive tracts.",
                "formula": "Sperm Transit Anatomical Cascade",
                "substitution": "Testis -> Epididymis -> Vas Deferens -> Urethra -> Vagina -> Cervix -> Uterus -> Fallopian Tube.",
                "calculation": "1. Origin: Seminiferous tubules inside the **Testis**.\n2. Storage/Maturation: Enters the **Epididymis**.\n3. Transport: Travels through the **Vas Deferens**, receives secretions from seminal vesicles and prostate gland.\n4. Ejaculation: Passes through the **Urethra** and is deposited in the **Vagina** during copulation.\n5. Female Transit: Swims upward through the **Cervix** into the **Uterus**.\n6. Destination: Swims into the **Fallopian Tube (Oviduct)** to meet and penetrate the ovum.",
                "finalAnswer": "Testis -> Epididymis -> Vas Deferens -> Urethra -> Vagina -> Cervix -> Uterus -> Fallopian Tube.",
                "unit": "Transit Trajectory",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.18: Male duct system connecting to female tract"
            },
            {
                "problem": "Compare sperm and ovum in terms of: (a) Relative size, (b) Motility, (c) Number produced per cycle.",
                "given": "Male gamete (sperm) vs Female gamete (ovum).",
                "formula": "Anisogamy Dimorphism Ledger",
                "substitution": "Microscopic motile sperm vs large nutrient-laden stationary ovum.",
                "calculation": "| Feature | Sperm (Male Gamete) | Ovum (Female Gamete) |\n| :--- | :--- | :--- |\n| **Size** | Microscopic (~0.05 mm), stripped of cytoplasm | Large (~0.1 mm), abundant nutrient yolk/cytoplasm |\n| **Motility** | Actively motile with flagellar tail | Non-motile, moved passively by ciliated tube epithelium |\n| **Production** | Millions (200-300 million per ejaculation) | Strictly one mature ovum per 28-day menstrual cycle |",
                "finalAnswer": "Sperm is tiny, actively motile, and produced in millions; ovum is large, non-motile, and released one per month.",
                "unit": "Gametology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.19: Ovarian release of single ovum"
            },
            {
                "problem": "Why is the urethra in males called a urinogenital duct, while in females the urinary and reproductive tracts are completely separate?",
                "given": "Anatomical comparison of urinary and reproductive ducts in males vs females.",
                "formula": "Urinogenital Convergence vs Divergence",
                "substitution": "Male: common urethral canal; Female: distinct urethral orifice and vaginal opening.",
                "calculation": "1. In males, the urethra passes through the penis and conveys both urine from the bladder and semen from the vas deferens to the outside (though neuro-muscular sphincters prevent simultaneous discharge). Hence it is called a **urinogenital canal**.\n2. In human females, the urinary system and reproductive system are completely separate anatomical passages: urine exits via the separate urethral orifice, while reproductive intercourse, menstruation, and childbirth occur through the distinct vaginal canal.",
                "finalAnswer": "In males, the urethra serves as a shared canal for both urine and semen; in females, the urinary orifice and reproductive vagina are entirely separate.",
                "unit": "Comparative Anatomy",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.18: Male urinogenital canal pathway"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Fertilization takes place inside the uterus (womb).",
                "correction": "Fertilization does NOT happen in the uterus. Fertilization occurs strictly in the FALLOPIAN TUBE (oviduct). The fertilized egg divides into a blastocyst as it travels down the tube and only enters the uterus 5-7 days later for IMPLANTATION.",
                "why_it_matters": "A primary board exam question where thousands of students mistakenly write 'uterus'."
            }
        ],
        "visual_lesson_plan": {
            "title": "Human Reproductive Systems Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Puberty & Endocrine Activation: Puberty is the developmental phase during adolescence when reproductive organs mature and secondary sexual characteristics develop, driven by testosterone in males and estrogen/progesterone in females.",
                    "diagram_title": "Pubertal Endocrine Cascade & Maturation",
                    "diagram_type": "image",
                    "image_query": "puberty secondary sexual characteristics endocrine male female diagram",
                    "video_query": "puberty changes in boys and girls class 10 8",
                    "image_url": "/extracted_diagrams/ch11/fig_11_18.webp",
                    "what_to_make": "Textbook diagram showing male reproductive organ system and hormonal maturation.",
                    "timing_and_cue": "Mount pubertal endocrine on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_18.webp | Pubertal Maturation | Endocrine activation of secondary sexual characteristics and gametogenesis\")"
                },
                {
                    "concept_title": "Scrotal Thermoregulation Axiom: The testes are located outside the abdominal cavity in a pouch of skin called the scrotum because normal human body temperature ($37^\\circ\\text{C}$) is too high for viable spermatogenesis; the scrotum maintains a temperature $2\\text{ to }2.5^\\circ\\text{C}$ lower than body core temperature.",
                    "diagram_title": "Male Reproductive System & Scrotum Schema",
                    "diagram_type": "image",
                    "image_query": "male reproductive system testes scrotum vas deferens prostate diagram",
                    "video_query": "male reproductive system 3d animation",
                    "image_url": "/extracted_diagrams/ch11/fig_11_18.webp",
                    "what_to_make": "Textbook diagram detailing testes in scrotum, epididymis, vas deferens, and penile urethra.",
                    "timing_and_cue": "Mount male system on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_18.webp | Male Reproductive System | Scrotum thermoregulation maintaining 2-2.5°C lower temperature for spermatogenesis\")"
                },
                {
                    "concept_title": "Male Accessory Gland Secretions: The seminal vesicles and prostate gland secrete alkaline fluids containing fructose, mucus, and clotting enzymes into the vas deferens; this fluid nourishes sperm, provides a fluid transport medium, and neutralizes vaginal acidity, forming semen.",
                    "diagram_title": "Accessory Gland Duct Convergence",
                    "diagram_type": "image",
                    "image_query": "seminal vesicles prostate gland semen formation diagram",
                    "video_query": "functions of prostate and seminal vesicles",
                    "image_url": "/extracted_diagrams/ch11/fig_11_18.webp",
                    "what_to_make": "Textbook diagram showing seminal vesicles and prostate gland emptying into urethra.",
                    "timing_and_cue": "Mount accessory glands on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_18.webp | Accessory Glands | Seminal vesicles providing fructose and prostate neutralizing acidity\")"
                },
                {
                    "concept_title": "Female Ovarian Function & Ovulation: Human females are born with thousands of immature oocytes in both ovaries; starting at puberty, one mature ovum is released alternately by one of the ovaries roughly every 28 days (ovulation).",
                    "diagram_title": "Female Reproductive System Schema",
                    "diagram_type": "image",
                    "image_query": "female reproductive system ovary fallopian tube uterus cervix vagina diagram",
                    "video_query": "female reproductive system 3d animation",
                    "image_url": "/extracted_diagrams/ch11/fig_11_19.webp",
                    "what_to_make": "Textbook diagram detailing bilateral ovaries, fallopian tubes, uterus, cervix, and vagina.",
                    "timing_and_cue": "Mount female system on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_19.webp | Female Reproductive System | Ovaries releasing mature ovum alternately every 28 days\")"
                },
                {
                    "concept_title": "Fallopian Tube (Oviduct) as Site of Fertilization: The fallopian tube captures the released ovum with its ciliated fimbriae; fertilization of the ovum by sperm takes place strictly within the ampulla of the fallopian tube.",
                    "diagram_title": "Fallopian Tube Ampullary Fertilization Locus",
                    "diagram_type": "image",
                    "image_query": "fallopian tube oviduct fertilization site sperm egg diagram",
                    "video_query": "fertilization in fallopian tube animation",
                    "image_url": "/extracted_diagrams/ch11/fig_11_19.webp",
                    "what_to_make": "Textbook diagram showing ovum pathway into the fallopian tube ampulla where fertilization occurs.",
                    "timing_and_cue": "Mount fertilization site on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_19.webp | Site of Fertilization | Fallopian tube (oviduct) capturing ovum for syngamy with sperm\")"
                },
                {
                    "concept_title": "The Uterus (Womb) Architecture: The uterus is an elastic, pear-shaped muscular organ designed to nurture a developing fetus; its inner lining (endometrium) thickens with blood vessels every month to prepare for embryonic implantation.",
                    "diagram_title": "Uterine Muscular Wall & Endometrial Architecture",
                    "diagram_type": "image",
                    "image_query": "uterus endometrium myometrium implantation diagram",
                    "video_query": "uterus structure and endometrial cycle",
                    "image_url": "/extracted_diagrams/ch11/fig_11_19.webp",
                    "what_to_make": "Textbook diagram showing hollow pear-shaped muscular uterus with vascular lining.",
                    "timing_and_cue": "Mount uterus architecture on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_19.webp | Uterine Architecture | Muscular womb with vascular endometrium prepared for embryonic implantation\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "Why are the male testes suspended outside the body in a pouch, rather than safely protected inside the abdominal cavity like the ovaries?"
   - Law: Detail male anatomy, scrotal temperature regulation, female anatomy, and oviductal fertilization site.
   - Socratic check: "Where does the sperm meet and fertilize the egg: inside the uterus or inside the fallopian tube?" HARD STOP: Wait for student answer!"""
    }

    # Module 6: Menstrual Cycle, Embryonic Development, Reproductive Health & Master NCERT Solver
    m6 = {
        "order_index": 6,
        "title": "The Menstrual Cycle, Embryonic Gestation, Reproductive Health & Master NCERT Solver",
        "description": "Analyze the 28-day menstrual cycle timeline, explore placental maternal-fetal exchange, evaluate contraceptive strategies (barrier, chemical, IUD, surgical), examine STI prevention, and solve all NCERT chapter exercises.",
        "subtopics": [
            "The 28-Day Menstrual Cycle: Menstruation (days 1-5), Follicular phase, Ovulation (day 14), Luteal phase",
            "Implantation & Gestation: Blastocyst embedding into uterine endometrium; 9-month gestation",
            "The Placenta: Vascular disc tissue with chorionic villi for oxygen, nutrient, and waste exchange",
            "Contraceptive Strategies: Barrier (condoms preventing STIs), Chemical (oral pills), IUDs (Copper-T), Surgical",
            "Sexually Transmitted Infections: Bacterial (gonorrhoea, syphilis) vs viral (warts, HIV/AIDS)",
            "Comprehensive NCERT Chapter-End Problem Solver: In-text and terminal exercises solved step-by-step"
        ],
        "key_concepts": [
            "The 28-Day Menstrual Cycle: In human females, if the released egg is not fertilized, the thickened vascular lining of the uterus (endometrium) along with its blood vessels sloughs off and exits through the vagina as menstrual flow lasting 3 to 5 days; ovulation occurs roughly midway on Day 14.",
            "Implantation: Following fertilization in the fallopian tube, the zygote divides repeatedly to form an embryo (blastocyst) that travels into the uterus and embeds itself into the vascular endometrial lining, establishing pregnancy.",
            "The Placenta as Maternal-Fetal Conduit: The placenta is a specialized disc-shaped organ embedded in the uterine wall containing embryonic chorionic villi surrounded by maternal blood spaces; it provides a vast surface area for glucose and oxygen to diffuse from mother to embryo, and metabolic wastes (CO2, urea) to pass from embryo to mother.",
            "Contraceptive Methodologies: Contraceptive methods prevent unwanted pregnancy: Mechanical barriers (condoms) prevent sperm entry and protect against STIs; Hormonal pills alter endocrine balance to prevent ovulation; Intrauterine Devices (Copper-T / IUDs) prevent implantation; Surgical sterilisation (Vasectomy in males, Tubectomy in females) permanently blocks gamete transit.",
            "STI Prevention & Reproductive Health: Sexually Transmitted Infections are transmitted via sexual contact; bacterial STIs (Gonorrhoea, Syphilis) can be cured with antibiotics, whereas viral STIs (Genital Warts, HIV/AIDS) have no cure; barrier methods (latex condoms) provide effective dual protection.",
            "PCPNDT Act & Female Foeticide Prohibition: Prenatal sex determination using ultrasound is strictly illegal under Indian law (Pre-Conception and Pre-Natal Diagnostic Techniques Act) to prevent female foeticide and restore balanced child sex ratios."
        ],
        "success_criteria": "Student can explain the 28-day menstrual timeline, describe placental exchange, compare contraceptive methods, explain STI transmission, and solve all NCERT exercises.",
        "chapter_notes": """### 11.18 The 28-Day Menstrual Cycle
The female reproductive cycle repeats approximately every **28 days**:
1. **Menstruation Phase (Days 1 to 5)**: If fertilization does not occur, the corpus luteum degenerates, progesterone levels drop, and the vascular uterine endometrium breaks down, discharging blood and tissue through the vagina.
2. **Follicular / Proliferative Phase (Days 6 to 13)**: Pituitary FSH stimulates an ovarian follicle to mature. Estrogen stimulates endometrial thickening.
3. **Ovulation (Day 14)**: A surge of LH triggers the rupture of the Graafian follicle, releasing the secondary oocyte into the fallopian tube.
4. **Luteal / Secretory Phase (Days 15 to 28)**: Ruptured follicle becomes the **corpus luteum**, secreting high levels of **progesterone** to maintain the glandular, nutrient-rich endometrium for potential implantation.

### 11.19 Embryonic Development & The Placenta
1. **Implantation**: The zygote undergoes cleavage, forming a hollow ball of cells called a **blastocyst**, which embeds in the uterine wall ~6-8 days after fertilization.
2. **The Placenta**:
   - A specialized disc-shaped tissue embedded in the uterine wall, connected to the fetus via the **umbilical cord**.
   - Contains microscopic finger-like **chorionic villi** on the fetal side projecting into maternal blood spaces.
   - *Vital Functions*:
     - **Nutrient & Gas Delivery**: Oxygen, glucose, amino acids, and antibodies diffuse from maternal blood into fetal blood.
     - **Waste Elimination**: Carbon dioxide and nitrogenous wastes (urea) diffuse from fetal blood into maternal blood for excretion by the mother's kidneys.
3. **Gestation Period**: In humans, gestation lasts approximately **9 months (38 to 40 weeks / ~280 days)**, culminating in rhythmic uterine contractions (**parturition / labor**) to deliver the baby.

### 11.20 Reproductive Health & Contraception
Contraception prevents unwanted pregnancy, spacing births and protecting health:
- **1. Barrier Methods**: Condoms (on penis) or diaphragms (in vagina). Prevent sperm from reaching ovum. *Condoms provide the ONLY effective protection against Sexually Transmitted Infections (STIs)*.
- **2. Chemical / Hormonal Methods**: Oral contraceptive pills containing synthetic estrogen/progesterone that inhibit pituitary FSH/LH, preventing ovulation. Can cause minor hormonal side effects.
- **3. Intrauterine Devices (IUDs)**: Devices like the **Copper-T** inserted into the uterus by a doctor (Fig. 11.23). Copper ions impair sperm motility and prevent implantation.
- **4. Surgical Methods (Permanent Sterilization)**:
  - **Vasectomy (Males)**: Small portion of vas deferens is cut and ligated; sperm cannot enter semen.
  - **Tubectomy (Females)**: Fallopian tubes are cut and tied; ovum cannot meet sperm.

### 11.21 Sexually Transmitted Infections (STIs)
- **Bacterial**: *Gonorrhoea* (Neisseria gonorrhoeae), *Syphilis* (Treponema pallidum). Treatable with antibiotics.
- **Viral**: *Genital Warts* (Human Papillomavirus - HPV), *HIV/AIDS* (Human Immunodeficiency Virus). Incurable; managed with antivirals.
- **Legal Protection**: Prenatal sex determination using ultrasound is strictly banned by the **PCPNDT Act** to prevent female foeticide.""",
        "worked_examples": [
            {
                "problem": "What happens when the human egg is not fertilized? Explain the 28-day menstrual cycle phases (Fig. 11.21).",
                "given": "Ovarian and uterine cycle without fertilization.",
                "formula": "Menstrual Cycle Timeline: Menstruation -> Follicular -> Ovulation -> Luteal",
                "substitution": "Progesterone withdrawal leading to endometrial shedding.",
                "calculation": "1. If fertilization does not occur within 24 hours of ovulation, the egg degenerates.\n2. The corpus luteum in the ovary ceases progesterone production.\n3. The thick, spongy uterine endometrium, rich in blood vessels and glands built to support an embryo, is no longer needed.\n4. The lining breaks down and is shed along with blood, mucous, and the unfertilized egg through the vagina.\n5. This bleeding phase is menstruation, lasting 3 to 5 days, resetting the cycle.",
                "finalAnswer": "The unfertilized egg degenerates, progesterone levels plunge, and the vascular uterine endometrium is shed as menstrual bleeding lasting 3-5 days.",
                "unit": "Menstrual Physiology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.21: Key stages of the 28-day menstrual cycle"
            },
            {
                "problem": "What is the role of the placenta during pregnancy (Fig. 11.22)? Explain its structural adaptations for exchange.",
                "given": "Maternal-fetal interface during gestation.",
                "formula": "Counter-Current Chorionic Villi Diffusion",
                "substitution": "Maternal blood sinuses surrounding fetal chorionic villi.",
                "calculation": "1. The placenta is a temporary disc-shaped organ formed jointly by embryonic and maternal tissues embedded in the uterine wall.\n2. **Structure**: On the fetal side, millions of microscopic finger-like projections called chorionic villi extend into large pools of maternal blood.\n3. This provides an enormous surface area for efficient diffusion.\n4. **Function**: Oxygen, glucose, amino acids, and maternal antibodies diffuse across the thin membrane into fetal capillaries; metabolic wastes (carbon dioxide, urea) diffuse in reverse from fetus to mother for excretion.",
                "finalAnswer": "Placenta's chorionic villi provide vast surface area for maternal-fetal exchange of oxygen, glucose, antibodies, and elimination of fetal waste.",
                "unit": "Placental Physiology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.22: Stages of pregnancy and placental fetal exchange"
            },
            {
                "problem": "What are the different methods of contraception? How do they prevent pregnancy, and which method protects against STIs?",
                "given": "Classification of contraceptive techniques.",
                "formula": "Contraceptive Mechanism Mapping: Barrier, Chemical, IUD, Surgical",
                "substitution": "Physical blocking vs ovulation inhibition vs implantation prevention vs gamete transit block.",
                "calculation": "1. **Barrier Methods**: Condoms, diaphragms. Physically block sperm entry. Latex condoms uniquely protect against Sexually Transmitted Infections (HIV, syphilis).\n2. **Chemical/Hormonal Methods**: Oral pills. Alter female hormone balance to prevent ovulation.\n3. **Intrauterine Devices (IUDs)**: Copper-T inserted into uterus. Suppresses sperm motility and prevents implantation.\n4. **Surgical Methods**: Vasectomy (vas deferens tied in males) and Tubectomy (fallopian tubes tied in females). Permanently blocks gamete transit.",
                "finalAnswer": "Barrier (condoms, also prevents STIs), Chemical (pills stop ovulation), IUD (Copper-T stops implantation), Surgical (vasectomy/tubectomy permanent blocks).",
                "unit": "Reproductive Health",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.23: Intra-Uterine Device (Copper-T) contraception"
            },
            {
                "problem": "Why is female foeticide a grave social crime, and which Indian legal act strictly prohibits prenatal sex determination?",
                "given": "Misuse of prenatal diagnostic ultrasonography in India.",
                "formula": "PCPNDT Act & Child Sex Ratio Balance",
                "substitution": "Ultrasound sex determination leading to selective abortion of female fetuses.",
                "calculation": "1. Female foeticide is the illegal aborting of female fetuses following prenatal sex determination, driven by social gender bias.\n2. This practice creates severe distortions in the child sex ratio (skewed male-to-female proportions), leading to demographic crises and social instability.\n3. In India, prenatal sex determination using ultrasound or genetic testing is strictly prohibited by law under the **PCPNDT Act (Pre-Conception and Pre-Natal Diagnostic Techniques Act, 1994)**, making disclosure of fetal sex punishable by imprisonment and heavy fines.",
                "finalAnswer": "Female foeticide skews the sex ratio; prenatal sex determination is strictly prohibited and penalized under India's PCPNDT Act.",
                "unit": "Bioethics & Law",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.23: Reproductive health regulations and clinical contraception"
            },
            {
                "problem": "Can a woman become pregnant if copulation occurs on Day 25 of her 28-day menstrual cycle? Explain based on ovulation timing.",
                "given": "Ovulation timing in standard 28-day menstrual cycle.",
                "formula": "Fertile Window Calculation: Day 14 +/- 2 days",
                "substitution": "Day 25 is deep in the post-ovulatory luteal phase.",
                "calculation": "1. In a regular 28-day cycle, ovulation occurs roughly on Day 14.\n2. The released ovum survives in the fallopian tube for only 12 to 24 hours.\n3. By Day 16, the unfertilized ovum has already degenerated, and the corpus luteum is secreting progesterone.\n4. On Day 25, there is no viable egg in the reproductive tract, and the endometrium is preparing to shed.\n5. Therefore, pregnancy cannot occur on Day 25 of a regular cycle.",
                "finalAnswer": "No; ovulation occurs around Day 14 and the ovum survives only 24 hours; by Day 25 no viable egg exists.",
                "unit": "Fertility Window",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.21: Fertile window on 28-day menstrual cycle timeline"
            },
            {
                "problem": "How does the Copper-T intrauterine device prevent pregnancy? Does it protect against sexually transmitted infections?",
                "given": "Mechanism of Copper-T IUD.",
                "formula": "Copper Ion Spermicidal & Implantation Prevention Action",
                "substitution": "In situ uterine foreign-body response and copper ion release.",
                "calculation": "1. Copper-T is a T-shaped plastic device wrapped in fine copper wire, placed inside the uterine cavity by a doctor.\n2. It continuously releases trace copper ions into uterine fluid.\n3. Copper ions are toxic to sperm: they suppress sperm motility, impair their fertilizing capacity, and induce a mild endometrial reaction that prevents blastocyst implantation.\n4. **STI Protection**: It does NOT protect against STIs because it does not create a physical barrier preventing microbial contact between mucous membranes during intercourse.",
                "finalAnswer": "Copper-T releases copper ions suppressing sperm motility and preventing implantation; it provides ZERO protection against STIs.",
                "unit": "Contraceptive Science",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 11.23: Copper-T intrauterine contraceptive device"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Oral contraceptive pills or Copper-T protect against HIV/AIDS and other STIs.",
                "correction": "Oral pills and Copper-T protect ONLY against pregnancy. They provide ZERO protection against Sexually Transmitted Infections (HIV, Gonorrhoea, Syphilis). Only physical barrier methods (latex condoms) prevent transmission of STIs.",
                "why_it_matters": "A life-critical health distinction taught universally in school curricula."
            }
        ],
        "visual_lesson_plan": {
            "title": "Menstrual Cycle, Gestation & Contraception Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "The 28-Day Menstrual Cycle: In human females, if the released egg is not fertilized, the thickened vascular lining of the uterus (endometrium) along with its blood vessels sloughs off and exits through the vagina as menstrual flow lasting 3 to 5 days; ovulation occurs roughly midway on Day 14.",
                    "diagram_title": "28-Day Menstrual Cycle Timeline",
                    "diagram_type": "image",
                    "image_query": "menstrual cycle 28 days phases menstruation ovulation luteal diagram",
                    "video_query": "menstrual cycle animation class 10 3d",
                    "image_url": "/extracted_diagrams/ch11/fig_11_21.webp",
                    "what_to_make": "Textbook diagram showing 28-day menstrual cycle timeline and uterine endometrial thickness curve.",
                    "timing_and_cue": "Mount menstrual cycle on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_21.webp | Menstrual Cycle Timeline | 28-day cycle: Days 1-5 menstruation, Day 14 ovulation, Days 15-28 luteal phase\")"
                },
                {
                    "concept_title": "Implantation: Following fertilization in the fallopian tube, the zygote divides repeatedly to form an embryo (blastocyst) that travels into the uterus and embeds itself into the vascular endometrial lining, establishing pregnancy.",
                    "diagram_title": "Blastocyst Implantation in Endometrium",
                    "diagram_type": "image",
                    "image_query": "blastocyst implantation uterine wall endometrium diagram",
                    "video_query": "fertilization to implantation animation 3d",
                    "image_url": "/extracted_diagrams/ch11/fig_11_22.webp",
                    "what_to_make": "Textbook diagram showing early embryonic cleavage stages and uterine implantation.",
                    "timing_and_cue": "Mount implantation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_22.webp | Blastocyst Implantation | Embryo embedding into vascular endometrium establishing pregnancy\")"
                },
                {
                    "concept_title": "The Placenta as Maternal-Fetal Conduit: The placenta is a specialized disc-shaped organ embedded in the uterine wall containing embryonic chorionic villi surrounded by maternal blood spaces; it provides a vast surface area for glucose and oxygen to diffuse from mother to embryo, and metabolic wastes (CO2, urea) to pass from embryo to mother.",
                    "diagram_title": "Placental Villi Maternal-Fetal Exchange",
                    "diagram_type": "image",
                    "image_query": "placenta structure chorionic villi umbilical cord exchange diagram",
                    "video_query": "how the placenta works 3d animation",
                    "image_url": "/extracted_diagrams/ch11/fig_11_22.webp",
                    "what_to_make": "Textbook diagram detailing placenta, umbilical cord, chorionic villi, and maternal blood pools.",
                    "timing_and_cue": "Mount placenta on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_22.webp | Placental Architecture | Chorionic villi delivering oxygen and nutrients while clearing fetal metabolic wastes\")"
                },
                {
                    "concept_title": "Contraceptive Methodologies: Contraceptive methods prevent unwanted pregnancy: Mechanical barriers (condoms) prevent sperm entry and protect against STIs; Hormonal pills alter endocrine balance to prevent ovulation; Intrauterine Devices (Copper-T / IUDs) prevent implantation; Surgical sterilisation (Vasectomy in males, Tubectomy in females) permanently blocks gamete transit.",
                    "diagram_title": "Intrauterine Contraceptive Device (Copper-T)",
                    "diagram_type": "image",
                    "image_query": "copper T intrauterine device contraception diagram",
                    "video_query": "contraception methods copper T vasectomy tubectomy",
                    "image_url": "/extracted_diagrams/ch11/fig_11_23.webp",
                    "what_to_make": "Textbook diagram showing Copper-T IUD positioned inside uterine cavity.",
                    "timing_and_cue": "Mount Copper-T on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_23.webp | Intra-Uterine Device (Copper-T) | Releasing copper ions to suppress sperm motility and prevent implantation\")"
                },
                {
                    "concept_title": "STI Prevention & Reproductive Health: Sexually Transmitted Infections are transmitted via sexual contact; bacterial STIs (Gonorrhoea, Syphilis) can be cured with antibiotics, whereas viral STIs (Genital Warts, HIV/AIDS) have no cure; barrier methods (latex condoms) provide effective dual protection.",
                    "diagram_title": "Reproductive Health & Barrier Protection",
                    "diagram_type": "image",
                    "image_query": "barrier contraception condom sexually transmitted infection prevention diagram",
                    "video_query": "reproductive health and sexually transmitted diseases class 10",
                    "image_url": "/extracted_diagrams/ch11/fig_11_23.webp",
                    "what_to_make": "Textbook diagram illustrating clinical contraception and STI barrier defense.",
                    "timing_and_cue": "Mount STI prevention on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_23.webp | Reproductive Health & STI Defense | Barrier methods providing indispensable protection against viral and bacterial STIs\")"
                },
                {
                    "concept_title": "PCPNDT Act & Female Foeticide Prohibition: Prenatal sex determination using ultrasound is strictly illegal under Indian law (Pre-Conception and Pre-Natal Diagnostic Techniques Act) to prevent female foeticide and restore balanced child sex ratios.",
                    "diagram_title": "PCPNDT Act Legal Protection Framework",
                    "diagram_type": "image",
                    "image_query": "PCPNDT act female foeticide child sex ratio legal protection diagram",
                    "video_query": "PCPNDT act female foeticide prohibition",
                    "image_url": "/extracted_diagrams/ch11/fig_11_23.webp",
                    "what_to_make": "Textbook statutory advisory prohibiting prenatal fetal sex determination under Indian law.",
                    "timing_and_cue": "Mount PCPNDT Act on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch11/fig_11_23.webp | Statutory PCPNDT Prohibition | Absolute legal ban on prenatal sex determination to eliminate female foeticide\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "Does the blood of a mother mix directly with the blood of her developing baby inside the womb? If not, how does the fetus breathe and eat?"
   - Law: Detail the 28-day menstrual cycle, the placenta, contraceptive categories, and the PCPNDT Act.
   - Socratic check: "Why do birth control pills protect against pregnancy, but fail to protect against HIV/AIDS?" HARD STOP: Wait for student answer!"""
    }

    return [m1, m2, m3, m4, m5, m6]

if __name__ == "__main__":
    modules = get_ch11_modules()
    with open("scripts/science_modules_ch11.json", "w", encoding="utf-8") as f:
        json.dump(modules, f, indent=2, ensure_ascii=False)
    print(f"Chapter 11 complete: {len(modules)} modules synthesized with 1:1 visuals and worked examples.")
