import json
import os

DIR_10 = "scripts/science_class10_modules"

# Chapter 6: Control and Coordination
ch6_solver = [
    {
        "problem": "In-Text Question (Section 6.1 & 6.2, p. 6 & p. 9): (a) What is the difference between a reflex action and walking? (b) What happens at the synapse between two neurons?",
        "given": "Somatic voluntary locomotion vs involuntary spinal reflex arcs; Neurotransmitter synaptic transmission.",
        "formula": "Reflex Arc: Receptor -> Sensory Neuron -> Spinal Relay Neuron -> Motor Neuron -> Effector. Synaptic transmission: Chemical neurotransmitters (acetylcholine) diffuse across synaptic cleft.",
        "substitution": "Involuntary spinal arc vs cerebral cortical motor planning.",
        "calculation": "(a) Reflex Action vs Walking:\n1. Reflex action: Rapid, involuntary, automatic motor response to an immediate external hazard (e.g. withdrawing hand from hot flame). Coordinated primarily by the SPINAL CORD without prior conscious brain intervention.\n2. Walking: Voluntary, intentional, learned locomotor action coordinated and controlled consciously by the FOREBRAIN (cerebral motor cortex and cerebellum for balance).\n(b) Events at the Synapse:\nWhen an electrical nerve impulse reaches the axon terminal of the pre-synaptic neuron, it triggers synaptic vesicles to release chemical neurotransmitters (e.g. acetylcholine) into the microscopic gap (synaptic cleft). The neurotransmitters diffuse across the cleft and bind to specific receptor sites on the dendrite membrane of the post-synaptic neuron, initiating a new electrical impulse. This chemical bridge ensures strictly UNIDIRECTIONAL signal transmission.",
        "finalAnswer": "(a) Reflex action is an automatic involuntary spinal response; walking is a conscious voluntary action controlled by the forebrain; (b) Electrical impulse releases chemical neurotransmitters across the synaptic cleft to initiate a new impulse in the next neuron.",
        "unit": "Neurobiology",
        "has_diagram": True,
        "diagram_source": "image_search",
        "figure_caption": "Synaptic transmission between axon terminal and dendrite",
        "image_search_query": "chemical synapse neurotransmitter axon dendrite diagram class 10",
        "page": 6,
        "section": "Section 6.1"
    },
    {
        "problem": "In-Text Question & Exercise (Section 6.3 & p. 13): (a) What are plant hormones (phytohormones)? Give examples of growth promoters and growth inhibitors. (b) How does phototropism occur in plant shoots?",
        "given": "Plant hormonal signaling; Shoot phototropism mechanism.",
        "formula": "Auxin differential elongation on shaded side: Stem bends toward light ($L_{\\text{shaded}} > L_{\\text{illuminated}}$).",
        "substitution": "Auxin redistribution away from unilateral light source.",
        "calculation": "(a) Plant hormones are chemical coordination substances synthesized in minute quantities at shoot/root tips that regulate cell division, elongation, and differentiation.\n- Growth Promoters: Auxins (cell elongation, apical dominance), Gibberellins (stem elongation, seed germination), Cytokinins (active cell division, stomatal opening).\n- Growth Inhibitor: Abscisic Acid / ABA (induces dormancy, leaf wilting/fall, stomatal closure under drought stress).\n(b) Mechanism of Phototropism: When unilateral sunlight shines on one side of a plant shoot, auxin synthesized at the shoot tip diffuses toward the SHADED SIDE of the stem. The higher concentration of auxin stimulates the cells on the shaded side to grow and elongate faster than cells on the illuminated side. This asymmetric elongation causes the shoot stem to curve and bend toward the light source (positive phototropism).",
        "finalAnswer": "(a) Promoters: Auxin, Gibberellin, Cytokinin; Inhibitor: Abscisic acid (ABA); (b) Auxin migrates to the shaded side, stimulating faster elongation and causing the shoot to bend towards light.",
        "unit": "Plant Physiology",
        "has_diagram": True,
        "diagram_source": "image_search",
        "figure_caption": "Auxin redistribution and phototropic bending of shoot toward unilateral light",
        "image_search_query": "phototropism auxin shaded side shoot bending experiment",
        "page": 9,
        "section": "Section 6.3"
    }
]

# Chapter 7: How do Organisms Reproduce?
ch7_solver = [
    {
        "problem": "In-Text Question & Exercise (Section 7.1, 7.2 & p. 15): (a) What is the importance of DNA copying in reproduction? (b) Why is variation beneficial to a species even if it is not advantageous for the individual?",
        "given": "Cellular reproduction, genetic replication fidelity, and natural selection.",
        "formula": "DNA replication produces structural blueprints; Genetic variation enables evolutionary resilience under environmental niche shifts.",
        "substitution": "Biochemical replication errors generating natural phenotypic variation.",
        "calculation": "(a) Importance of DNA copying: DNA contains hereditary instructions for synthesizing body proteins and structures. Copying DNA ensures that daughter cells receive identical structural blueprints to maintain tissue functioning and species fidelity.\n(b) Evolutionary Benefit of Variation: If an entire population of organisms were genetically identical and inhabited a specific ecological niche, a catastrophic environmental change (e.g. sharp temperature spike, novel viral pathogen, drying of pond) could kill all individuals, causing species extinction. If genetic variants exist within the population (e.g. heat-resistant bacteria in a hot spring), those variants will survive the catastrophe and propagate, preventing the species from dying out.",
        "finalAnswer": "(a) DNA copying preserves structural blueprints across generations; (b) Genetic variation allows populations to survive unpredictable environmental disasters, preventing extinction.",
        "unit": "Genetics & Evolution",
        "has_diagram": False,
        "diagram_source": "image_search",
        "figure_caption": "",
        "image_search_query": "dna replication importance reproduction variation natural selection",
        "page": 2,
        "section": "Section 7.1"
    },
    {
        "problem": "In-Text Question & Exercise (Section 7.4 & p. 15): (a) What are the functions of the placenta during human gestation? (b) List three different methods of contraception and explain their working mechanisms.",
        "given": "Maternal-fetal uterine physiology; Reproductive health and family planning.",
        "formula": "Placenta villi countercurrent exchange; Barrier, chemical, and surgical contraceptive mechanisms.",
        "substitution": "Nutrient/gas exchange across maternal blood spaces.",
        "calculation": "(a) Functions of Placenta: A specialized disc-shaped vascular organ embedded in the uterine wall. Chorionic villi on the fetal side provide huge surface area in maternal blood pools. Functions: 1. Delivers glucose, amino acids, and oxygen from mother to embryo. 2. Transports metabolic wastes (urea, uric acid, CO2) from embryo to maternal blood for excretion. 3. Endocrine gland secreting progesterone and human chorionic gonadotropin (hCG) to maintain pregnancy.\n(b) Contraceptive Methods:\n1. Barrier Methods (Condoms, diaphragms): Physically prevent sperm from entering the female cervix/uterus, while shielding against Sexually Transmitted Infections (STIs).\n2. Hormonal / Chemical Methods (Oral contraceptive pills): Ingested hormones alter estrogen-progesterone balance, preventing ovulation from ovaries.\n3. Surgical Methods (Vasectomy in males, Tubectomy in females): Tying and cutting the vas deferens or fallopian tubes permanently blocks gamete transit.",
        "finalAnswer": "(a) Placenta delivers nutrients/oxygen to embryo, removes metabolic wastes, and secretes hormones; (b) Barrier blocks sperm transit, hormonal stops ovulation, surgical cuts/ties gamete conduits.",
        "unit": "Reproductive Health & Physiology",
        "has_diagram": True,
        "diagram_source": "image_search",
        "figure_caption": "Cross-section of human uterus showing placenta, umbilical cord, and embryo",
        "image_search_query": "placenta human embryo uterine wall umbilical cord diagram",
        "page": 14,
        "section": "Section 7.4"
    }
]

# Chapter 8: Heredity
ch8_solver = [
    {
        "problem": "In-Text Question & Exercise (Section 8.1, 8.2 & p. 6): (a) A Mendelian cross between tall pea plants (TT) and short pea plants (tt) produced all tall plants in the F1 generation. When F1 plants were self-pollinated, what was the ratio of tall to short plants in the F2 generation? (b) How is the sex of a human child determined genetically?",
        "given": "Mendelian monohybrid cross; Human chromosomal sex determination.",
        "formula": "Monohybrid phenotypic ratio 3 : 1, genotypic ratio 1 : 2 : 1. Sex determination: Female XX, Male XY. Probability of male vs female = 50% each.",
        "substitution": "Punnett square analysis: F1 (Tt) x F1 (Tt) -> TT, Tt, Tt, tt.",
        "calculation": "(a) Mendelian Monohybrid Cross:\n1. Parents: TT (pure tall) x tt (pure dwarf).\n2. Gametes: T and t -> F1 Generation: All Tt (heterozygous tall; 'T' is dominant over recessive 't').\n3. Selfing F1 (Tt x Tt):\n   Gametes: T, t from both parents.\n   F2 Genotypes: 1 TT : 2 Tt : 1 tt (Genotypic ratio 1 : 2 : 1).\n   F2 Phenotypes: 3 Tall : 1 Short (Phenotypic ratio 3 : 1, i.e. 75% tall, 25% dwarf).\n(b) Sex Determination in Humans:\nHuman females have two homologous X chromosomes (XX), producing only one type of ovum carrying an X chromosome. Human males have heteromorphic sex chromosomes (XY), producing two types of sperm: 50% carry an X chromosome, and 50% carry a Y chromosome.\n- If an X-sperm fertilises the ovum: Zygote is XX -> Female child.\n- If a Y-sperm fertilises the ovum: Zygote is XY -> Male child.\nSince fertilization by X or Y sperm is an equal random probability (50%), the child's genetic sex is determined strictly by the father's fertilising sperm.",
        "finalAnswer": "(a) F2 phenotypic ratio is 3 Tall : 1 Short (75% tall, 25% short); (b) Sex is determined by the sperm: X-sperm produces a girl (XX), Y-sperm produces a boy (XY) with 50% probability.",
        "unit": "Mendelian Genetics",
        "has_diagram": True,
        "diagram_source": "image_search",
        "figure_caption": "Mendelian monohybrid cross and human sex determination chart",
        "image_search_query": "mendel monohybrid cross punnett square sex determination xx xy",
        "page": 2,
        "section": "Section 8.1"
    }
]

# Chapter 10: The Human Eye and the Colourful World
ch10_solver = [
    {
        "problem": "In-Text Question & Exercise (Section 10.2 & p. 10): (a) A person with a myopic eye cannot see objects beyond 1.2 m distinctly. What should be the type and power of the corrective lens to restore proper vision? (b) Why do stars twinkle in the night sky while planets do not?",
        "given": "(a) Far point of myopic eye d = 1.2 m; Target: View distant objects at infinity (u = -infinity, v = -1.2 m).\n(b) Atmospheric refraction and point vs extended light sources.",
        "formula": "Lens Formula: $\\frac{1}{f} = \\frac{1}{v} - \\frac{1}{u}$; Power $P = \\frac{1}{f\\text{ (m)}}$.",
        "substitution": "$\\frac{1}{f} = \\frac{1}{-1.2} - \\frac{1}{-\\infty} = -\\frac{1}{1.2} - 0 = -\\frac{1}{1.2}$.",
        "calculation": "1. Focal length: $f = -1.2\\text{ m}$ (Concave/diverging lens).\n2. Power of lens:\n   $P = \\frac{1}{-1.2} = -\\frac{10}{12} = -0.83\\text{ Dioptres (D)}$.\n(b) Why Stars Twinkle:\nStars are situated billions of kilometers away and act as point sources of light. Starlight enters Earth's atmosphere, which consists of air layers with constantly fluctuating temperatures, densities, and refractive indices. The path of starlight refracts continuously (atmospheric refraction), causing the apparent position of the star and the quantity of light entering the eye to flicker rapidly (twinkling).\nPlanets are much closer to Earth and act as extended disc sources of light (collections of billions of point sources). The twinkling fluctuations from different points average out to zero, so planets shine with steady light without twinkling.",
        "finalAnswer": "(a) A concave lens of power -0.83 D is required; (b) Stars twinkle due to atmospheric refraction of point light sources; planets do not twinkle because they are extended sources whose fluctuations cancel out.",
        "unit": "Dioptres and Atmospheric Optics",
        "has_diagram": True,
        "diagram_source": "image_search",
        "figure_caption": "Myopia eye defect correction with concave lens and atmospheric refraction",
        "image_search_query": "myopia eye defect concave lens correction twinkling stars optics",
        "page": 4,
        "section": "Section 10.2"
    },
    {
        "problem": "End-of-Chapter Exercise Q10, Q11, Q12 (p. 10): (a) Explain the dispersion of white light through a triangular glass prism. Which color bends the most and why? (b) Why does the clear sky appear blue during the day, and why does the sun appear reddish at sunrise and sunset?",
        "given": "Prismatic dispersion; Rayleigh scattering in atmosphere.",
        "formula": "Snell's Law: $n = \\frac{c}{v}$; Cauchy's relation: $n \\propto \\frac{1}{\\lambda^2}$. Rayleigh scattering: Intensity $I \\propto \\frac{1}{\\lambda^4}$.",
        "substitution": "Wavelength order: $\\lambda_{\\text{red}} \\approx 700\\text{ nm} > \\lambda_{\\text{violet}} \\approx 400\\text{ nm}$.",
        "calculation": "1. Prismatic Dispersion: Glass has a wavelength-dependent refractive index ($n_{\\text{violet}} > n_{\\text{red}}$). Violet light has the shortest wavelength and slows down the most in glass, refracting through the largest angle of deviation. Red light has the longest wavelength and refracts the least, splitting white light into the VIBGYOR spectrum.\n2. Blue Sky: Nitrogen and oxygen molecules in the upper atmosphere have sizes smaller than visible light wavelengths, scattering blue/violet light ~16 times more effectively than red light ($I \\propto 1/\\lambda^4$). Scattered blue photons illuminate the sky.\n3. Reddish Sunrise/Sunset: At sunrise/sunset, sunlight traverses a much thicker atmospheric path. Shorter blue and violet wavelengths are completely scattered away before reaching the observer; only longer, less-scattered red and orange rays reach the eye.",
        "finalAnswer": "(a) Violet light bends the most because it has the shortest wavelength and highest refractive index in glass; (b) Sky is blue due to Rayleigh scattering ($1/\\lambda^4$); sunset is red because only long red waves penetrate thick atmospheric paths.",
        "unit": "Wave Optics & Atmospheric Scattering",
        "has_diagram": True,
        "diagram_source": "image_search",
        "figure_caption": "Dispersion of white light through prism and Rayleigh scattering of sunlight",
        "image_search_query": "dispersion white light prism spectrum rayleigh scattering sunset",
        "page": 10,
        "section": "Exercises"
    }
]

solvers = {
    "chapter_6_control_and_coordination.json": ch6_solver,
    "chapter_7_how_do_organisms_reproduce.json": ch7_solver,
    "chapter_8_heredity.json": ch8_solver,
    "chapter_10_the_human_eye_and_the_colourful_world.json": ch10_solver
}

for fname, examples in solvers.items():
    fpath = os.path.join(DIR_10, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        mods = json.load(f)
    
    m_solver = mods[-1]
    m_solver["worked_examples"] = examples
    m_solver["title"] = "NCERT In-Text & Chapter-End Exercises Master Solver"
    
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(mods, f, indent=2)
    print(f"Updated {fname} with {len(examples)} exhaustive solver questions!")
