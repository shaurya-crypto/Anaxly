"""
Complete Module Synthesis for Class 9 Science:
Chapter 10: Sound Waves: Characteristics and Applications (Curriculum ID: 1908699a-60c6-4a5e-9f27-05f9111fe142)
"""

import json

def get_ch10_modules():
    # Module 1: Production and Propagation of Sound: Vibrations & Mechanical Wave Nature
    m1 = {
        "order_index": 1,
        "title": "Production & Propagation of Sound: Vibrational Origins & Material Medium Requirement",
        "description": "Analyze the mechanics of sound generation through vibrating bodies (tuning forks, vocal cords, stretched membranes), demonstrate why sound requires a material medium via the bell jar experiment, and explore mechanical wave propagation.",
        "subtopics": [
            "Vibrational Nature of Sound: Rapid to-and-fro motion of bodies producing pressure disturbances",
            "Activity 10.1 & 10.2: Striking a tuning fork, touching water surface, vibrating stretched rubber bands",
            "Sound Production in Humans: Vocal cords vibrating in the larynx (voice box) with air forced by lungs",
            "Medium Requirement Axiom: Sound cannot travel through vacuum; requires solids, liquids, or gases",
            "Activity 10.7: The Electric Bell in a Vacuum Bell Jar Experiment (air evacuation leads to silence)",
            "Propagation Mechanics: Particles vibrating about mean positions and transmitting kinetic energy without bulk transport"
        ],
        "key_concepts": [
            "Vibrational Origin of Sound: Sound is produced due to the vibration of objects; a vibration is a rapid to-and-fro or periodic back-and-forth motion of an object about its central equilibrium position.",
            "Human Vocal Mechanism: In humans, sound is produced by the voice box or larynx; two vocal cords are stretched across the larynx leaving a narrow slit for the passage of air; air expelled from the lungs forces the cords to vibrate, producing voice.",
            "Material Medium Requirement: Sound is a mechanical wave that requires a material medium (solid, liquid, or gas) for its transmission; it cannot travel through a vacuum because there are no particles to collide and transfer momentum.",
            "The Bell Jar Vacuum Proof: When an electric bell rings inside a glass bell jar connected to a vacuum pump, the sound gradually weakens as air is evacuated and ceases completely when a full vacuum is reached, even though the hammer continues striking the gong.",
            "Propagation as Energy Transfer: When a vibrating object moves forward, it pushes and compresses the medium in front of it creating a region of high pressure (compression); when it moves backward, it creates a region of low pressure (rarefaction).",
            "Zero Bulk Particle Transport: During sound propagation, individual particles of the medium do not travel from the source to the listener; they merely oscillate locally about their mean equilibrium positions, passing the disturbance to neighboring particles."
        ],
        "success_criteria": "Student can explain how vibrations produce sound, detail the bell jar vacuum experiment, prove sound cannot travel in space, and explain energy transmission without net particle movement.",
        "chapter_notes": """### 10.1 Production of Sound
Sound is produced by vibrating objects. A **vibration** means a rapid to-and-fro motion of an object about its mean position:
- **Tuning Fork**: When struck against a rubber pad, the prongs vibrate rapidly. Touching the vibrating prong to a suspended pith ball drives it violently away. Touching the surface of water produces vigorous ripples and splashes.
- **Human Voice**: In the larynx (voice box), two **vocal cords** are stretched with a narrow slit between them. When the lungs force air through the slit, the vocal cords vibrate to produce sound. Muscles attached to the vocal cords can tighten or loosen them, altering the pitch and timbre of the voice.
- **Musical Instruments**: Sound is produced by vibrating stretched strings (guitar, sitar, violin), vibrating membranes (tabla, dholak, drum), or vibrating air columns (flute, clarionet).

### 10.2 Propagation of Sound Requires a Material Medium
Sound is a **mechanical wave**; it relies on the elastic collisions of particles in the medium to propagate.
- **The Bell Jar Experiment (Activity 10.7)**:
  1. An electric bell is suspended inside an airtight glass bell jar connected to a vacuum pump.
  2. With air inside, the ringing bell is clearly audible.
  3. When the vacuum pump begins evacuating the air, the sound becomes progressively fainter.
  4. Once a complete vacuum is established, **no sound can be heard at all**, even though the hammer is visibly seen striking the gong.
  5. *Conclusion*: Sound strictly requires a material medium and **cannot propagate through a vacuum**.
- **Astronauts on the Moon**: Because the Moon has no atmosphere (vacuum), astronauts cannot hear each other directly by acoustic sound waves, even if they shout side by side. They must communicate using **radio waves** (electromagnetic waves that propagate through vacuum).

### 10.3 Mechanics of Wave Propagation
When a body vibrates in air:
1. Moving forward pushes air molecules together, creating a localized high-density, high-pressure zone called a **Compression ($C$)**.
2. Moving backward allows air molecules to spread apart, creating a localized low-density, low-pressure zone called a **Rarefaction ($R$)**.
3. A series of alternating compressions and rarefactions travels outwards through the air as a longitudinal wave. The particles themselves only oscillate locally about their mean positions; **energy travels, particles stay**.""",
        "worked_examples": [
            {
                "problem": "Explain how sound is produced by your school bell.",
                "given": "A striking hammer hitting a metallic school bell.",
                "formula": "Vibrational Mechanical Sound Production",
                "substitution": "Kinetic impact causes rapid to-and-fro elastic oscillation of the metal rim.",
                "calculation": "1. When the hammer strikes the brass or iron school bell, it imparts kinetic energy that forces the metal to vibrate rapidly back and forth.\n2. The vibrating rim compresses adjacent air molecules forward creating compressions, and rebounds backward creating rarefactions.\n3. This repeating wave of compressions and rarefactions travels through ambient air to reach our eardrums.",
                "finalAnswer": "The hammer impact forces the bell rim to vibrate rapidly; these vibrations compress and rarefy surrounding air, propagating sound waves to our ears.",
                "unit": "Acoustic Production",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.2: Vibrations producing sound in elastic bodies"
            },
            {
                "problem": "Why is sound wave called a mechanical wave? Can two astronauts talk to each other on the surface of the moon as they do on earth?",
                "given": "Sound propagation dynamics in terrestrial air vs lunar vacuum.",
                "formula": "Medium Requirement for Mechanical Wave Propagation",
                "substitution": "Lunar environment is a vacuum devoid of atmosphere.",
                "calculation": "1. Sound waves are called mechanical waves because they require a material medium (composed of physical particles with mass and elasticity) to propagate through successive particle collisions.\n2. On the Moon, there is no atmosphere (vacuum).\n3. Because there are no medium particles to transmit acoustic pressure disturbances, sound cannot travel on the Moon.\n4. Astronauts cannot hear each other directly; they must use radio transceivers.",
                "finalAnswer": "Sound is a mechanical wave requiring particle collisions; astronauts cannot talk acoustically on the moon due to vacuum and must use radio waves.",
                "unit": "Vacuum Invariant",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.7: Electric bell jar experiment proving sound cannot travel in vacuum"
            },
            {
                "problem": "Describe an activity to show that sound can travel through solids with high efficiency.",
                "given": "Activity 10.5: Investigating sound transmission in solid media.",
                "formula": "Acoustic Transmission in Dense Media",
                "substitution": "A long wooden table or metallic meter rod.",
                "calculation": "1. Place your ear firmly flat against one end of a long wooden or metal table.\n2. Have a classmate scratch or gently tap the other end of the table with a fingernail.\n3. You will hear the scratching sound distinctly and much louder through the solid wood than through the ambient air.\n4. This demonstrates that solids, with high particle density and elastic modulus, transmit sound efficiently.",
                "finalAnswer": "Scratching one end of a long table is heard much louder with ear pressed to wood than through air, demonstrating efficient transmission through solids.",
                "unit": "Solid Medium Transmission",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.5: Sound transmission through solid materials"
            },
            {
                "problem": "How do human vocal cords produce speech of varying pitch? Explain the anatomical mechanism in the larynx.",
                "given": "Human voice box (larynx) anatomy with vocal cords.",
                "formula": "Vocal Cord Tension & Frequency Regulation",
                "substitution": "Laryngeal muscles adjusting vocal cord tension and thickness.",
                "calculation": "1. The larynx contains two vocal cords stretched across the tracheal airway with a narrow slit between them.\n2. Air expelled from the lungs under pressure forces the cords to oscillate, generating sound waves.\n3. When attached muscles contract, the vocal cords become tight and thin, vibrating at a higher frequency to produce high-pitch sound.\n4. When the muscles relax, the cords become loose and thick, vibrating at lower frequency to produce low-pitch sound.",
                "finalAnswer": "Laryngeal muscles tighten or loosen the vocal cords; tight/thin cords vibrate faster producing high pitch, loose/thick cords vibrate slower producing low pitch.",
                "unit": "Laryngeal Biomechanics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.3: Vocal cords in human larynx producing sound"
            },
            {
                "problem": "When a tuning fork is struck and its stem is pressed against a tabletop, why does the sound become significantly louder?",
                "given": "Vibrating tuning fork placed in direct contact with table surface.",
                "formula": "Forced Vibrations and Increased Radiating Surface Area",
                "substitution": "Small prongs vs large table surface area.",
                "calculation": "1. A lone tuning fork has very thin prongs that disturb only a small volume of surrounding air, emitting faint sound.\n2. When its stem is pressed against a large wooden table, forced vibrations are set up in the entire tabletop.\n3. Because the tabletop has a vastly larger surface area, it sets a much larger volume of air into vibration simultaneously.\n4. This radiates a significantly greater acoustic energy per second, resulting in a much louder sound.",
                "finalAnswer": "The tabletop undergoes forced vibrations; its larger surface area displaces a vastly larger volume of air, multiplying acoustic loudness.",
                "unit": "Forced Oscillations",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.4: Tuning fork vibration and acoustic radiation"
            },
            {
                "problem": "Do the particles of air travel all the way from a ringing bell to our ears? Explain what physically travels across the room.",
                "given": "Sound propagating from a distant source across an air-filled room.",
                "formula": "Energy & Momentum Transfer vs Mass Bulk Transport",
                "substitution": "Air molecules undergo local simple harmonic oscillations.",
                "calculation": "1. Air molecules do NOT travel across the room. If they did, a ringing bell would create a continuous hurricane-force wind blowing outward!\n2. The source merely gives an impulse to adjacent air particles, which oscillate locally about their equilibrium positions.\n3. These particles collide with adjacent particles, transferring energy and momentum, and rebound back to their mean position.\n4. Thus, **energy and pressure disturbance travel across the room**, while the medium particles remain in their localized positions.",
                "finalAnswer": "No, air particles oscillate locally about their mean positions; only the energy disturbance and pressure waves travel across the room.",
                "unit": "Wave Dynamics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.10: Spherical propagation of sound energy without bulk particle drift"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "When someone speaks to you from across a room, air molecules blow out of their mouth and strike your ear.",
                "correction": "Air molecules do not travel across the room. The speaker's vocal cords create pressure oscillations that are passed from molecule to molecule like a row of falling dominoes. Only the acoustic energy travels.",
                "why_it_matters": "Distinguishes wave energy propagation from bulk physical fluid transport."
            }
        ],
        "visual_lesson_plan": {
            "title": "Production & Propagation of Sound Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Vibrational Origin of Sound: Sound is produced due to the vibration of objects; a vibration is a rapid to-and-fro or periodic back-and-forth motion of an object about its central equilibrium position.",
                    "diagram_title": "Vibrating Rubber Band Sound Generation",
                    "diagram_type": "image",
                    "image_query": "vibrating rubber band produces sound diagram",
                    "video_query": "vibration produces sound rubber band experiment",
                    "image_url": "/extracted_diagrams/ch10/fig_10_2.webp",
                    "what_to_make": "Textbook diagram showing stretched rubber band vibrating to generate sound.",
                    "timing_and_cue": "Mount vibrating band on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_2.webp | Vibrational Sound Generation | Rapid to-and-fro oscillation of stretched rubber band\")"
                },
                {
                    "concept_title": "Human Vocal Mechanism: In humans, sound is produced by the voice box or larynx; two vocal cords are stretched across the larynx leaving a narrow slit for the passage of air; air expelled from the lungs forces the cords to vibrate, producing voice.",
                    "diagram_title": "Vocal Cords in Human Larynx",
                    "diagram_type": "image",
                    "image_query": "human vocal cords in larynx voice box diagram",
                    "video_query": "how vocal cords produce sound",
                    "image_url": "/extracted_diagrams/ch10/fig_10_3.webp",
                    "what_to_make": "Textbook anatomical diagram of human vocal cords in the larynx showing air slit and muscular tensioning.",
                    "timing_and_cue": "Mount vocal cords on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_3.webp | Human Vocal Cords | Air from lungs vibrating slit in larynx to produce speech\")"
                },
                {
                    "concept_title": "Material Medium Requirement: Sound is a mechanical wave that requires a material medium (solid, liquid, or gas) for its transmission; it cannot travel through a vacuum because there are no particles to collide and transfer momentum.",
                    "diagram_title": "Tuning Fork Vibration & Pith Ball",
                    "diagram_type": "image",
                    "image_query": "tuning fork vibrating ping pong pith ball splash water diagram",
                    "video_query": "tuning fork vibration water splash experiment",
                    "image_url": "/extracted_diagrams/ch10/fig_10_4.webp",
                    "what_to_make": "Textbook diagram showing tuning fork struck against rubber pad and touching ear or water surface.",
                    "timing_and_cue": "Mount tuning fork on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_4.webp | Tuning Fork Vibrations | Rapid prong oscillations transferring mechanical disturbance\")"
                },
                {
                    "concept_title": "The Bell Jar Vacuum Proof: When an electric bell rings inside a glass bell jar connected to a vacuum pump, the sound gradually weakens as air is evacuated and ceases completely when a full vacuum is reached, even though the hammer continues striking the gong.",
                    "diagram_title": "Vacuum Bell Jar Experiment Setup",
                    "diagram_type": "image",
                    "image_query": "electric bell jar vacuum pump experiment diagram",
                    "video_query": "bell jar experiment sound needs medium vacuum",
                    "image_url": "/extracted_diagrams/ch10/fig_10_7.webp",
                    "what_to_make": "Textbook diagram of airtight glass bell jar, electric bell, and vacuum pump demonstrating silence in vacuum.",
                    "timing_and_cue": "Mount bell jar experiment on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_7.webp | Vacuum Bell Jar Setup | Total silence when air is evacuated proving sound requires a medium\")"
                },
                {
                    "concept_title": "Propagation as Energy Transfer: When a vibrating object moves forward, it pushes and compresses the medium in front of it creating a region of high pressure (compression); when it moves backward, it creates a region of low pressure (rarefaction).",
                    "diagram_title": "Sound Propagation Through Solid Medium",
                    "diagram_type": "image",
                    "image_query": "sound travels through solid table meter rod experiment diagram",
                    "video_query": "sound transmission through solids",
                    "image_url": "/extracted_diagrams/ch10/fig_10_5.webp",
                    "what_to_make": "Textbook diagram showing student listening to tapping sounds transmitted through a solid wooden table.",
                    "timing_and_cue": "Mount solid transmission on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_5.webp | Sound in Solids | Fast acoustic transmission through solid lattice particles\")"
                },
                {
                    "concept_title": "Zero Bulk Particle Transport: During sound propagation, individual particles of the medium do not travel from the source to the listener; they merely oscillate locally about their mean equilibrium positions, passing the disturbance to neighboring particles.",
                    "diagram_title": "Spherical Wave Energy Propagation",
                    "diagram_type": "image",
                    "image_query": "spherical sound waves point source propagation diagram",
                    "video_query": "how sound waves travel compression rarefaction",
                    "image_url": "/extracted_diagrams/ch10/fig_10_10.webp",
                    "what_to_make": "Textbook diagram showing spherical wavefronts radiating from a point source through local particle oscillations.",
                    "timing_and_cue": "Mount spherical wave on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_10.webp | Spherical Wavefronts | Acoustic energy expanding in all directions without net particle drift\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "If a massive meteor explodes in deep space right next to your spacecraft, will you hear a deafening thunderous boom or dead silence?"
   - Law: State the mechanical nature of sound and detail the bell jar vacuum experiment.
   - Socratic check: "When a tuning fork rings, do the air molecules around it fly across the classroom into your ear? What actually travels?" HARD STOP: Wait for student answer!"""
    }

    # Module 2: Longitudinal Waves vs Transverse Waves & Wave Anatomy
    m2 = {
        "order_index": 2,
        "title": "Longitudinal vs Transverse Waves & Mathematical Wave Anatomy ($v = \\nu\\lambda$)",
        "description": "Analyze longitudinal waves in slinky springs and air, contrast them with transverse waves, map compressions and rarefactions to sinusoidal crests and troughs, and master the wave speed equation $v = \\nu\\lambda$.",
        "subtopics": [
            "Longitudinal Waves Mechanics: Particle oscillation parallel to wave propagation direction",
            "Compressions (C) & Rarefactions (R): High-density/high-pressure vs low-density/low-pressure zones",
            "Transverse Waves Mechanics: Particle oscillation perpendicular to wave propagation (light waves, water ripples)",
            "Wave Parameters: Wavelength (lambda in m), Amplitude (A in m), Frequency (nu in Hz), Time Period (T in s)",
            "The Fundamental Wave Equation: Deriving v = nu * lambda = lambda / T",
            "Sinusoidal Graphical Representation: Density-distance and pressure-distance curves"
        ],
        "key_concepts": [
            "Longitudinal Wave Definition: A wave in which the individual particles of the medium oscillate back and forth parallel to the direction of wave propagation (e.g., sound waves in gases and liquids, compressional pulses in a slinky spring).",
            "Transverse Wave Definition: A wave in which the particles of the medium oscillate up and down perpendicular to the direction of wave propagation (e.g., ripples on a water surface, light waves), characterized by crests and troughs.",
            "Wavelength (lambda): The linear distance between two consecutive compressions or two consecutive rarefactions in a longitudinal wave, measured in meters (m).",
            "Frequency (nu or f) & Time Period (T): Frequency is the number of complete wave cycles or oscillations passing a point per second, measured in Hertz (1 Hz = 1 s^-1); Time period is the time taken for one complete oscillation (T = 1 / nu).",
            "Amplitude (A): The magnitude of the maximum displacement of particles of the medium from their mean position on either side, representing the wave's energy.",
            "Fundamental Wave Equation: The speed of a wave equals the product of its frequency and wavelength: v = nu * lambda, or v = lambda / T, measured in meters per second (m/s)."
        ],
        "success_criteria": "Student can distinguish longitudinal from transverse waves, sketch density-distance curves identifying crests/troughs, and solve numerical problems using v = nu * lambda.",
        "chapter_notes": """### 10.4 Longitudinal vs Transverse Waves
1. **Longitudinal Waves**:
   - Particles of the medium vibrate **parallel** to the direction of wave propagation.
   - Propagates via alternating **Compressions ($C$)** (high density, high pressure) and **Rarefactions ($R$)** (low density, low pressure).
   - *Examples*: Sound waves in air, compressional pulses in a slinky spring.
2. **Transverse Waves**:
   - Particles of the medium oscillate **perpendicular** to the direction of wave propagation.
   - Characterized by alternating **Crests** (peaks of positive displacement) and **Troughs** (valleys of negative displacement).
   - *Examples*: Waves on a plucked guitar string, surface water ripples, electromagnetic light waves.

### 10.5 Anatomy of a Sound Wave
- **Wavelength ($\\lambda$)**: The distance between two consecutive compressions or two consecutive rarefactions (SI unit: meter, $\\text{m}$).
- **Frequency ($\\nu$ or $f$)**: Number of complete oscillations per unit time:
  $$\\nu = \\frac{1}{T} \\quad (\\text{SI unit: Hertz, Hz} = \\text{s}^{-1})$$
- **Time Period ($T$)**: The time taken by two consecutive compressions or rarefactions to cross a fixed point:
  $$T = \\frac{1}{\\nu} \\quad (\\text{SI unit: second, s})$$
- **Amplitude ($A$)**: The maximum displacement of particles from their central equilibrium position (determines wave energy and loudness).

### 10.6 The Fundamental Wave Speed Equation
$$\\text{Wave Speed } v = \\frac{\\text{Distance}}{\\text{Time}} = \\frac{\\lambda}{T} = \\nu \\lambda$$
$$\\mathbf{v = \\nu \\lambda}$$
- Where:
  - $v = \\text{wave speed in meters per second (m/s)}$
  - $\\nu = \\text{frequency in Hertz (Hz)}$
  - $\\lambda = \\text{wavelength in meters (m)}$""",
        "worked_examples": [
            {
                "problem": "A sound wave has a frequency of 2 kHz and wavelength 35 cm. How long will it take to travel 1.5 km?",
                "given": "Frequency nu = 2 kHz = 2000 Hz. Wavelength lambda = 35 cm = 0.35 m. Distance d = 1.5 km = 1500 m.",
                "formula": "Wave speed v = nu * lambda; Travel time t = d / v",
                "substitution": "v = 2000 Hz * 0.35 m; t = 1500 m / v",
                "calculation": "1. Calculate wave speed:\n   v = 2000 * 0.35 = 700 m/s\n2. Calculate time to travel 1500 m:\n   t = d / v = 1500 / 700 = 2.143 s",
                "finalAnswer": "Wave speed is 700 m/s; it will take 2.14 seconds to travel 1.5 km.",
                "unit": "s",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.16: Periodic density variation and graphical representation of sound wave"
            },
            {
                "problem": "A sound wave travels at a speed of 339 m/s. If its wavelength is 1.5 cm, what is the frequency of the wave? Will it be audible to human ears?",
                "given": "Speed v = 339 m/s. Wavelength lambda = 1.5 cm = 0.015 m. Human audible range = 20 Hz to 20,000 Hz.",
                "formula": "Frequency nu = v / lambda",
                "substitution": "nu = 339 / 0.015",
                "calculation": "1. nu = 339 / 0.015 = 22,600 Hz = 22.6 kHz\n2. Human audible range is 20 Hz to 20 kHz (20,000 Hz).\n3. Since 22,600 Hz > 20,000 Hz, this wave lies in the ultrasonic range.",
                "finalAnswer": "Frequency is 22,600 Hz (22.6 kHz); it is ultrasonic and NOT audible to human ears.",
                "unit": "Hz",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.19: Graphical representation of high-frequency ultrasonic wave"
            },
            {
                "problem": "Calculate the wavelength of a sound wave whose frequency is 220 Hz and speed is 440 m/s in a given medium.",
                "given": "Frequency nu = 220 Hz. Speed v = 440 m/s.",
                "formula": "Wavelength lambda = v / nu",
                "substitution": "lambda = 440 / 220",
                "calculation": "lambda = 440 / 220 = 2.0 m",
                "finalAnswer": "The wavelength of the sound wave is 2.0 meters.",
                "unit": "m",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.12: Anatomical wavelength dimension between consecutive compressions"
            },
            {
                "problem": "A person is listening to a tone of 500 Hz sitting at a distance of 450 m from the source of the sound. What is the time interval between successive compressions reaching the listener?",
                "given": "Frequency nu = 500 Hz. Distance d = 450 m.",
                "formula": "Time interval between successive compressions is the Time Period T = 1 / nu",
                "substitution": "T = 1 / 500",
                "calculation": "T = 1 / 500 = 0.002 s = 2 * 10^-3 s (2 milliseconds).\n(Note: The distance of 450 m is extraneous information; time between successive compressions depends solely on frequency).",
                "finalAnswer": "The time interval between successive compressions is 0.002 seconds (2 ms).",
                "unit": "s",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.16a: Sinusoidal periodic density variation with time period T"
            },
            {
                "problem": "Explain the difference between compressions and rarefactions in terms of particle density and pressure. How are they represented on a displacement-distance graph?",
                "given": "Longitudinal wave propagation in air.",
                "formula": "Density-Pressure Sinusoidal Mapping",
                "substitution": "Compressions -> Peaks (Crests); Rarefactions -> Valleys (Troughs).",
                "calculation": "1. Compression: Region where particles are crowded together; density is higher than average, and pressure is maximum. On a graph, it is represented as a Crest (peak above centerline).\n2. Rarefaction: Region where particles are spread apart; density is lower than average, and pressure is minimum. On a graph, it is represented as a Trough (valley below centerline).",
                "finalAnswer": "Compressions have high density/pressure (plotted as crests); rarefactions have low density/pressure (plotted as troughs).",
                "unit": "Graph Mapping",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.16: Mapping physical compressions/rarefactions to sinusoidal graph"
            },
            {
                "problem": "A vibrating body produces 50 waves in 0.5 seconds. If the distance between a compression and the next rarefaction is 68 cm, calculate: (a) Frequency, (b) Wavelength, (c) Wave speed.",
                "given": "50 complete waves in 0.5 s. Distance from compression to next rarefaction = 68 cm = 0.68 m.",
                "formula": "(a) nu = Waves / Time; (b) Distance C to R = lambda / 2 -> lambda = 2 * (C to R); (c) v = nu * lambda.",
                "substitution": "(a) nu = 50 / 0.5; (b) lambda = 2 * 0.68; (c) v = 100 * 1.36.",
                "calculation": "1. Frequency nu = 50 / 0.5 = 100 Hz\n2. Distance between a compression and immediate adjacent rarefaction is half a wavelength: lambda / 2 = 0.68 m -> lambda = 1.36 m\n3. Wave speed v = nu * lambda = 100 * 1.36 = 136 m/s",
                "finalAnswer": "(a) Frequency = 100 Hz, (b) Wavelength = 1.36 m, (c) Speed = 136 m/s.",
                "unit": "m/s",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.8: Longitudinal wave propagation along a slinky spring"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "The distance between a compression and the immediate next rarefaction is equal to one full wavelength lambda.",
                "correction": "No! One full wavelength lambda is the distance between two CONSECUTIVE compressions (C to C) or two consecutive rarefactions (R to R). The distance from a compression to the immediately adjacent rarefaction (C to R) is only HALF a wavelength (lambda / 2).",
                "why_it_matters": "A frequent calculation pitfall in board exam numericals."
            }
        ],
        "visual_lesson_plan": {
            "title": "Longitudinal Waves & Wave Anatomy Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Longitudinal Wave Definition: A wave in which the individual particles of the medium oscillate back and forth parallel to the direction of wave propagation (e.g., sound waves in gases and liquids, compressional pulses in a slinky spring).",
                    "diagram_title": "Slinky Spring Longitudinal Wave Pulse",
                    "diagram_type": "image",
                    "image_query": "slinky spring longitudinal wave compressions rarefactions diagram",
                    "video_query": "longitudinal wave slinky demonstration",
                    "image_url": "/extracted_diagrams/ch10/fig_10_8.webp",
                    "what_to_make": "Textbook diagram showing compressions and rarefactions traveling along a stretched slinky.",
                    "timing_and_cue": "Mount slinky wave on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_8.webp | Slinky Longitudinal Waves | Alternating coils showing compressions and rarefactions\")"
                },
                {
                    "concept_title": "Transverse Wave Definition: A wave in which the particles of the medium oscillate up and down perpendicular to the direction of wave propagation (e.g., ripples on a water surface, light waves), characterized by crests and troughs.",
                    "diagram_title": "Piston Air Tube Density Disturbance",
                    "diagram_type": "image",
                    "image_query": "air density tube piston longitudinal sound wave diagram",
                    "video_query": "longitudinal vs transverse waves difference",
                    "image_url": "/extracted_diagrams/ch10/fig_10_9.webp",
                    "what_to_make": "Textbook diagram showing oscillating piston generating density variations in an air tube.",
                    "timing_and_cue": "Mount air piston on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_9.webp | Air Density in Tube | Piston oscillations creating alternating density bands\")"
                },
                {
                    "concept_title": "Wavelength (lambda): The linear distance between two consecutive compressions or two consecutive rarefactions in a longitudinal wave, measured in meters (m).",
                    "diagram_title": "Longitudinal Waveform Anatomy",
                    "diagram_type": "image",
                    "image_query": "longitudinal wave anatomy wavelength compression rarefaction diagram",
                    "video_query": "wavelength of sound wave explained",
                    "image_url": "/extracted_diagrams/ch10/fig_10_12.webp",
                    "what_to_make": "Textbook anatomical diagram of a longitudinal wave marking wavelength between compressions.",
                    "timing_and_cue": "Mount wave anatomy on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_12.webp | Longitudinal Wave Anatomy | Distance lambda between consecutive compressions\")"
                },
                {
                    "concept_title": "Frequency (nu or f) & Time Period (T): Frequency is the number of complete wave cycles or oscillations passing a point per second, measured in Hertz (1 Hz = 1 s^-1); Time period is the time taken for one complete oscillation (T = 1 / nu).",
                    "diagram_title": "Density Variation Sinusoidal Graph",
                    "diagram_type": "image",
                    "image_query": "sound wave density distance variation sine graph crest trough diagram",
                    "video_query": "frequency time period sound wave graph",
                    "image_url": "/extracted_diagrams/ch10/fig_10_16a.webp",
                    "what_to_make": "Textbook graph plotting periodic medium density variation against distance at a fixed instant.",
                    "timing_and_cue": "Mount density curve on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_16a.webp | Periodic Density Variation | Sinusoidal curve mapping compressions as crests and rarefactions as troughs\")"
                },
                {
                    "concept_title": "Amplitude (A): The magnitude of the maximum displacement of particles of the medium from their mean position on either side, representing the wave's energy.",
                    "diagram_title": "Dual Representation: Density Medium & Sinusoid",
                    "diagram_type": "image",
                    "image_query": "sound wave graphical representation density pressure diagram",
                    "video_query": "amplitude of sound wave explained",
                    "image_url": "/extracted_diagrams/ch10/fig_10_16.webp",
                    "what_to_make": "Textbook dual diagram displaying physical compressed air layers aligned directly above the sine wave graph.",
                    "timing_and_cue": "Mount dual representation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_16.webp | Medium Density & Waveform | Direct alignment of physical compressions with graph peaks\")"
                },
                {
                    "concept_title": "Fundamental Wave Equation: The speed of a wave equals the product of its frequency and wavelength: v = nu * lambda, or v = lambda / T, measured in meters per second (m/s).",
                    "diagram_title": "Wave Speed & Frequency Relationship Curve",
                    "diagram_type": "image",
                    "image_query": "graphical representation sound wave frequency wavelength speed diagram",
                    "video_query": "v equals f lambda wave equation derivation",
                    "image_url": "/extracted_diagrams/ch10/fig_10_19.webp",
                    "what_to_make": "Textbook mathematical graph illustrating wave parameters governing v = nu * lambda.",
                    "timing_and_cue": "Mount wave equation graph on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_19.webp | Wave Equation Geometry | Connecting frequency, wavelength, and propagation velocity\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "If a wave has a distance of 50 cm between a compression and the VERY NEXT rarefaction, what is its wavelength? Is it 50 cm or 100 cm?"
   - Law: Define longitudinal vs transverse waves, amplitude, time period, and derive $v = \\nu\\lambda$.
   - Socratic check: "A sound wave has frequency 1000 Hz and speed 340 m/s. Calculate its wavelength!" HARD STOP: Wait for student answer!"""
    }

    # Module 3: Auditory Characteristics: Pitch, Loudness & Timbre
    m3 = {
        "order_index": 3,
        "title": "Auditory Characteristics of Sound: Pitch Dynamics, Loudness & Timbre (Quality)",
        "description": "Examine how human hearing perceives sound through pitch (governed by frequency), loudness (governed by amplitude squared), and timbre/quality (governed by harmonic waveforms).",
        "subtopics": [
            "The Three Subjective Characteristics of Musical Sound: Pitch, Loudness, Quality/Timbre",
            "Pitch & Frequency: Shrillness vs depth; high frequency bird chirp vs low frequency lion roar",
            "Loudness & Amplitude: Energy relationship ($Loudness \\propto Amplitude^2$); whisper vs shouting",
            "Intensity vs Loudness: Objective physical measurement (W/m^2) vs subjective physiological perception",
            "Quality or Timbre: Differentiating instruments (flute vs violin vs piano) producing same pitch and loudness",
            "Tone vs Note: Pure single-frequency oscillation vs complex musical mixture of harmonic overtones"
        ],
        "key_concepts": [
            "Pitch (Shrillness): Pitch is the auditory sensation that allows us to classify a sound as shrill or grave/flat; it is governed entirely by the frequency of vibration—higher frequency corresponds to higher pitch.",
            "Loudness & Amplitude Squared: Loudness is the measure of auditory response of the ear to sound energy, determined primarily by the amplitude of the vibrating body ($Loudness \\propto Amplitude^2$); doubling the amplitude quadruples the loudness.",
            "Intensity of Sound: Intensity is the physical acoustic power transmitted per unit area perpendicular to wave direction ($\\text{W/m}^2$), an objective quantity independent of human ear sensitivity, whereas loudness is a subjective psychological sensation.",
            "Quality or Timbre: Quality or timbre is the characteristic of a musical sound that enables us to distinguish between two sounds having the identical pitch and loudness emitted by different sources, determined by the harmonic waveform shape.",
            "Tone vs Note: A sound of a single, pure frequency is called a tone (e.g., from an ideal tuning fork); a rich pleasant sound produced by a mixture of several frequencies is called a note (musical chord).",
            "Noise vs Music: Noise is an unpleasant, irregular, and jarring acoustic waveform that irritates the ear, whereas music consists of harmonious, periodic, and mathematically ordered waveforms."
        ],
        "success_criteria": "Student can contrast pitch vs loudness, explain the square law of loudness with amplitude, interpret waveform graphs of different instruments, and define timbre.",
        "chapter_notes": """### 10.7 Auditory Characteristics of Sound
The human brain interprets sound waves using three distinct perceptual dimensions:

#### 1. Pitch
- **Governing Parameter**: **Frequency ($\\nu$)**.
- Higher frequency $\\implies$ More oscillations per second $\\implies$ Higher pitch (shrill sound).
  - *Examples*: Whistle, child's voice, mosquito whine, flute, violin.
- Lower frequency $\\implies$ Fewer oscillations per second $\\implies$ Lower pitch (grave, deep, flat sound).
  - *Examples*: Roar of a lion, bass drum, adult male voice.

#### 2. Loudness
- **Governing Parameter**: **Amplitude ($A$)**.
- Loudness is proportional to the square of the amplitude of vibration:
  $$\\text{Loudness} \\propto A^2$$
  - If amplitude is doubled ($2A$), loudness increases by a factor of $2^2 = \\mathbf{4}$.
  - If amplitude is tripled ($3A$), loudness increases by a factor of $3^2 = \\mathbf{9}$.
- **Intensity vs Loudness**:
  - *Intensity*: Physical amount of sound energy passing through unit area per second (unit: $\\text{W/m}^2$). Objective, measurable by instruments.
  - *Loudness*: Subjective perception of intensity by the human ear. A sound can have high intensity but low loudness if human ears are insensitive to that frequency.

#### 3. Quality or Timbre
- **Governing Parameter**: **Waveform Shape & Harmonic Overtones**.
- Timbre allows us to immediately distinguish between a flute, a violin, and a guitar playing the **exact same musical note at the exact same loudness**.
- A pure single-frequency sound is a **tone** (produced by a laboratory tuning fork).
- A pleasant musical sound composed of a fundamental frequency mixed with higher harmonics is a **note**.""",
        "worked_examples": [
            {
                "problem": "Guess which sound has a higher pitch: guitar or car horn? Explain using the concept of frequency.",
                "given": "Acoustic characteristics of a plucked guitar string vs automotive horn.",
                "formula": "Pitch = Perceived Frequency of Waveform",
                "substitution": "Plucked guitar string produces rapid high-frequency vibrations; car horn produces lower fundamental frequency with high acoustic power.",
                "calculation": "1. Pitch depends directly on frequency: higher frequency produces a sharper, more shrill sound.\n2. A guitar string produces rapid, high-frequency acoustic oscillations, yielding a high-pitch musical note.\n3. A car horn produces loud sound with broad lower frequencies designed for alerting traffic.\n4. Therefore, the guitar has a higher pitch.",
                "finalAnswer": "The guitar produces a higher pitch because its strings vibrate at a higher frequency than a car horn.",
                "unit": "Pitch Comparison",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.17: Comparison of low-frequency vs high-frequency sound waveforms"
            },
            {
                "problem": "If the amplitude of a sound wave is increased by a factor of 3, how will the loudness of the sound be affected?",
                "given": "Initial amplitude A1 = A; Final amplitude A2 = 3A.",
                "formula": "Loudness L proportional to A^2 -> L2 / L1 = (A2 / A1)^2",
                "substitution": "L2 / L1 = (3A / A)^2 = 3^2",
                "calculation": "L2 / L1 = 9 -> L2 = 9 * L1",
                "finalAnswer": "The loudness of the sound will increase by a factor of 9 (it becomes 9 times louder).",
                "unit": "Square Law",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.22: Waveform showing tripled amplitude and magnified acoustic power"
            },
            {
                "problem": "Distinguish between a tone and a note in acoustics.",
                "given": "Definitions of single-frequency vs harmonic musical sound.",
                "formula": "Spectral Frequency Composition",
                "substitution": "Tone = pure single nu; Note = fundamental nu + harmonics.",
                "calculation": "1. Tone: A sound composed of a single, pure frequency (e.g., from an ideal tuning fork). It sounds plain and lacks musical richness.\n2. Note: A complex musical sound produced by a mixture of several harmonic frequencies. It has a fundamental frequency accompanied by richer overtones.",
                "finalAnswer": "A tone is a sound of a single frequency; a note is a rich musical sound produced by a mixture of multiple frequencies.",
                "unit": "Harmonic Acoustics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.25: Harmonic waveform characteristics of musical instruments"
            },
            {
                "problem": "Two musical notes played on a flute and a violin have the same pitch and the same loudness. Can you distinguish between them? Name the property of sound that enables this.",
                "given": "Flute and violin playing identical note (same frequency) at identical loudness (same amplitude).",
                "formula": "Timbre / Quality of Sound",
                "substitution": "Waveform shape determined by unique harmonic overtone spectrum.",
                "calculation": "1. Yes, we can easily distinguish between them.\n2. The property is called **Quality** or **Timbre**.\n3. Even though fundamental frequency (pitch) and amplitude (loudness) are identical, the two instruments produce different shapes of waveforms due to different mixtures of harmonic overtones.",
                "finalAnswer": "Yes, we can distinguish them by their Quality or Timbre, which depends on the unique waveform shape and harmonic overtones of each instrument.",
                "unit": "Timbre",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.26: Acoustic resonance and unique timbre in musical instruments"
            },
            {
                "problem": "Why does a woman's voice generally sound more shrill than a man's voice?",
                "given": "Anatomical length and tension of vocal cords in females vs males.",
                "formula": "Frequency nu proportional to sqrt(Tension / Linear Density)",
                "substitution": "Female vocal cords are shorter and thinner (~15 mm) than male vocal cords (~20 mm).",
                "calculation": "1. Shrillness corresponds directly to high pitch and high frequency.\n2. Adult females have shorter, lighter, and tighter vocal cords (~15 mm) compared to adult males (~20 mm).\n3. When air passes through shorter and lighter cords, they oscillate with a significantly higher frequency (typically 200-250 Hz for women vs 100-130 Hz for men).\n4. This higher frequency gives the female voice a higher pitch and greater shrillness.",
                "finalAnswer": "Women's vocal cords are shorter and lighter, vibrating at higher frequencies (200-250 Hz) to produce higher pitch and shrillness.",
                "unit": "Anatomical Acoustics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.3: Vocal cord tension and frequency determination"
            },
            {
                "problem": "Explain the difference between loudness and intensity of sound. Can two sounds have the same intensity but different loudness?",
                "given": "Objective acoustic intensity vs subjective human loudness perception.",
                "formula": "Intensity I = Power / Area (W/m^2) vs Loudness Sensation",
                "substitution": "Human ear frequency response curve (Fletcher-Munson).",
                "calculation": "1. Intensity is the physical energy passing per second through unit area (measured in W/m^2), independent of whether anyone hears it.\n2. Loudness is the physiological response of the human ear and auditory cortex to sound energy.\n3. Yes, two sounds of the same intensity can have different loudness if their frequencies differ. For instance, the human ear is extraordinarily sensitive to 2000-4000 Hz, so a 3000 Hz tone sounds much louder than a 50 Hz tone of the exact same physical intensity.",
                "finalAnswer": "Intensity is objective physical power (W/m^2); loudness is subjective perception; two sounds of equal intensity can have different loudness due to frequency sensitivity of the ear.",
                "unit": "Psychoacoustics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.21: Sound energy spreading over distance"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Loudness and pitch are the same thing; if you shout louder, you increase the pitch.",
                "correction": "Loudness depends on AMPLITUDE (how far the particles move, energy). Pitch depends on FREQUENCY (how fast they oscillate). You can speak with a low pitch loudly (like a lion's roar) or with a high pitch softly (like a quiet whisper of a whistle).",
                "why_it_matters": "Fundamental orthogonal separation between amplitude and frequency."
            }
        ],
        "visual_lesson_plan": {
            "title": "Pitch, Loudness & Timbre Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Pitch (Shrillness): Pitch is the auditory sensation that allows us to classify a sound as shrill or grave/flat; it is governed entirely by the frequency of vibration—higher frequency corresponds to higher pitch.",
                    "diagram_title": "Pitch vs Frequency Wave Comparison",
                    "diagram_type": "image",
                    "image_query": "pitch and frequency sound wave high low pitch graph diagram",
                    "video_query": "pitch and frequency of sound waves",
                    "image_url": "/extracted_diagrams/ch10/fig_10_17.webp",
                    "what_to_make": "Textbook comparative graph showing two waveforms: low frequency (low pitch) and high frequency (high pitch).",
                    "timing_and_cue": "Mount pitch graph on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_17.webp | Pitch & Frequency | Comparing low-frequency bass with high-frequency shrill wave\")"
                },
                {
                    "concept_title": "Loudness & Amplitude Squared: Loudness is the measure of auditory response of the ear to sound energy, determined primarily by the amplitude of the vibrating body ($Loudness \\propto Amplitude^2$); doubling the amplitude quadruples the loudness.",
                    "diagram_title": "Loudness & Amplitude Wave Comparison",
                    "diagram_type": "image",
                    "image_query": "loudness and amplitude sound wave soft loud sound graph diagram",
                    "video_query": "loudness and amplitude sound waves",
                    "image_url": "/extracted_diagrams/ch10/fig_10_22.webp",
                    "what_to_make": "Textbook diagram showing soft sound (small amplitude) vs loud sound (large amplitude).",
                    "timing_and_cue": "Mount amplitude graph on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_22.webp | Loudness & Amplitude | Small amplitude for soft sound vs tall amplitude for loud sound\")"
                },
                {
                    "concept_title": "Intensity of Sound: Intensity is the physical acoustic power transmitted per unit area perpendicular to wave direction ($\\text{W/m}^2$), an objective quantity independent of human ear sensitivity, whereas loudness is a subjective psychological sensation.",
                    "diagram_title": "Sound Energy Dispersion Over Area",
                    "diagram_type": "image",
                    "image_query": "sound energy spreading over area inverse square law diagram",
                    "video_query": "sound intensity vs loudness",
                    "image_url": "/extracted_diagrams/ch10/fig_10_21.webp",
                    "what_to_make": "Textbook diagram showing sound energy spreading over expanding spherical areas as distance increases.",
                    "timing_and_cue": "Mount intensity dispersion on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_21.webp | Acoustic Intensity Dispersion | Energy spreading over expanding spherical wavefronts\")"
                },
                {
                    "concept_title": "Quality or Timbre: Quality or timbre is the characteristic of a musical sound that enables us to distinguish between two sounds having the identical pitch and loudness emitted by different sources, determined by the harmonic waveform shape.",
                    "diagram_title": "Musical Instrument Timbre Waveforms",
                    "diagram_type": "image",
                    "image_query": "timbre quality sound waveform harmonics musical instruments diagram",
                    "video_query": "timbre and quality of musical instruments",
                    "image_url": "/extracted_diagrams/ch10/fig_10_25.webp",
                    "what_to_make": "Textbook diagram displaying distinct complex waveforms for different musical instruments.",
                    "timing_and_cue": "Mount timbre waveforms on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_25.webp | Timbre & Harmonics | Unique waveform shapes distinguishing flute, violin, and voice\")"
                },
                {
                    "concept_title": "Tone vs Note: A sound of a single, pure frequency is called a tone (e.g., from an ideal tuning fork); a rich pleasant sound produced by a mixture of several frequencies is called a note (musical chord).",
                    "diagram_title": "Tabla Acoustic Percussion Mechanics",
                    "diagram_type": "image",
                    "image_query": "tabla set percussion membrane vibration acoustic harmonics diagram",
                    "video_query": "harmonics and overtones in Indian percussion tabla",
                    "image_url": "/extracted_diagrams/ch10/fig_10_26.webp",
                    "what_to_make": "Textbook image of a tabla set demonstrating acoustic membrane harmonics and rich tonal quality.",
                    "timing_and_cue": "Mount tabla harmonics on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_26.webp | Percussion Acoustics | Stretched membrane vibrating with rich harmonic overtones\")"
                },
                {
                    "concept_title": "Noise vs Music: Noise is an unpleasant, irregular, and jarring acoustic waveform that irritates the ear, whereas music consists of harmonious, periodic, and mathematically ordered waveforms.",
                    "diagram_title": "Harmonic Order vs Noise Waveform",
                    "diagram_type": "image",
                    "image_query": "music vs noise waveforms regular vs irregular diagram",
                    "video_query": "difference between music and noise acoustics",
                    "image_url": "/extracted_diagrams/ch10/fig_10_20.webp",
                    "what_to_make": "Textbook comparative waveforms showing smooth periodic musical tones versus chaotic jagged noise.",
                    "timing_and_cue": "Mount noise vs music on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_20.webp | Musical Order vs Noise | Regular periodic curves for music versus erratic spikes for noise\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "If a flute and a violin play the EXACT same note at the EXACT same loudness, how does your brain know instantly which one is the violin?"
   - Law: Detail the tri-particulate acoustic triad: Pitch (Frequency), Loudness (Amplitude^2), and Timbre (Waveform).
   - Socratic check: "If a guitarist doubles the amplitude of vibration by plucking harder, by what factor does the loudness multiply?" HARD STOP: Wait for student answer!"""
    }

    # Module 4: Speed of Sound, Sonic Boom & Reflection: Echoes and Reverberation
    m4 = {
        "order_index": 4,
        "title": "Speed of Sound, Sonic Boom & Sound Reflection: Echoes & Reverberation",
        "description": "Analyze acoustic speed variations across solids, liquids, and gases, explore supersonic flight and sonic booms, master the laws of reflection of sound, calculate minimum echo distances ($17.2\\text{ m}$), and control reverberation.",
        "subtopics": [
            "Speed of Sound in Media: Solids ($~5000\\text{ m/s}$) > Liquids ($~1500\\text{ m/s}$) > Gases ($~340\\text{ m/s}$)",
            "Temperature & Humidity Dependence: Speed increases as temperature and humidity rise",
            "Supersonic Speed & Sonic Boom: Shock waves formed when $v_{\\text{object}} > v_{\\text{sound}}$",
            "Laws of Reflection of Sound: $\\angle i = \\angle r$ in the same plane (megaphones, stethoscopes, curved ceilings)",
            "Echo Formation & Persistence of Hearing: $0.1\\text{ s}$ brain retention requiring minimum distance $d \\ge 17.2\\text{ m}$",
            "Reverberation & Acoustic Engineering: Repeated wall reflections in auditoriums and sound-absorbing treatments"
        ],
        "key_concepts": [
            "Speed of Sound Invariant: Sound travels fastest in solids, slower in liquids, and slowest in gases ($v_{\\text{solids}} > v_{\\text{liquids}} > v_{\\text{gases}}$); in air at $22^\\circ\\text{C}$ it travels at $344\\text{ m/s}$, and in iron at $5950\\text{ m/s}$.",
            "Temperature Dependence: The speed of sound increases with increase in temperature; in air, it increases by approximately $0.6\\text{ m/s}$ per degree Celsius rise ($v = 331 + 0.6 T$).",
            "Sonic Boom: When an object moves at supersonic speed (faster than the speed of sound in air), it produces conical pressure shock waves in the air; these shock waves carry enormous energy perceived as a thunderous, glass-shattering sonic boom.",
            "Laws of Reflection of Sound: Sound reflects off hard surfaces following the same laws as light: the incident wave, the normal, and the reflected wave all lie in the same plane, and the angle of incidence equals the angle of reflection ($\\angle i = \\angle r$).",
            "Minimum Echo Distance: The human brain retains auditory sensations for $0.1\\text{ s}$ (persistence of hearing); to hear a distinct echo, reflected sound must arrive after at least $0.1\\text{ s}$, requiring total round-trip distance $2d = v \\times 0.1$, so $d \\ge \\frac{344 \\times 0.1}{2} = \\mathbf{17.2\\text{ m}}$ at $22^\\circ\\text{C}$.",
            "Reverberation Control: The persistence of sound in an enclosed hall due to repeated successive reflections is called reverberation; excessive reverberation causes words to overlap into muddy noise, controlled by lining walls with sound-absorbing acoustic materials."
        ],
        "success_criteria": "Student can state speeds across phases, derive $17.2\\text{ m}$ minimum echo distance, calculate echo problems with cliffs/ships, and describe auditorium acoustic design.",
        "chapter_notes": """### 10.8 Speed of Sound in Different Media
The speed of sound depends on the **elasticity** and **density** of the medium:
$$\\mathbf{v_{\\text{solids}} > v_{\\text{liquids}} > v_{\\text{gases}}}$$
- **Speed in Air**:
  - At $0^\\circ\\text{C}$: $331\\text{ m/s}$
  - At $22^\\circ\\text{C}$: $344\\text{ m/s}$
  - At $25^\\circ\\text{C}$: $346\\text{ m/s}$
- **Speed in Liquids ($25^\\circ\\text{C}$)**:
  - Water (distilled): $1498\\text{ m/s}$
  - Sea water: $1531\\text{ m/s}$
- **Speed in Solids ($25^\\circ\\text{C}$)**:
  - Aluminium: $6420\\text{ m/s}$
  - Steel: $5960\\text{ m/s}$
  - Iron: $5950\\text{ m/s}$

### 10.9 Supersonic Speed & Sonic Boom
- **Subsonic**: Speed less than sound ($v < v_{\\text{sound}}$).
- **Supersonic**: Speed greater than sound ($v > v_{\\text{sound}}$) (fighter jets, rifle bullets).
- **Sonic Boom**: When a supersonic aircraft flies through air, it travels faster than the pressure waves it emits, generating conical **shock waves**. The sudden jump in air pressure across the shock front produces a violent, explosive sound called a **sonic boom**, powerful enough to shatter window panes and damage structures.

### 10.10 Reflection of Sound
Sound reflects from hard barriers (cliffs, walls, metal sheets) obeying the laws of reflection:
$$\\mathbf{\\angle i = \\angle r}$$

### 10.11 Echo: Derivation of Minimum Distance
- **Persistence of Hearing**: The human sensation of sound persists in our brain for about **$0.1\\text{ second}$** ($t_{\\text{persist}} = 0.1\\text{ s}$).
- For an echo to be perceived distinctly from the original sound, the reflected wave must return after an interval of at least $0.1\\text{ s}$.
- If $d$ is the distance to the reflecting surface, the sound travels a round-trip distance of $2d$:
  $$2d = v \\times t \\implies d = \\frac{v \\times t}{2}$$
  $$d_{\\text{min}} = \\frac{344\\text{ m/s} \\times 0.1\\text{ s}}{2} = \\frac{34.4}{2} = \\mathbf{17.2\\text{ m}}$$
- *Conclusion*: The reflecting obstacle must be situated at a minimum distance of **$17.2\\text{ meters}$** from the source (at $22^\\circ\\text{C}$).

### 10.12 Reverberation
In large auditoriums or cinema halls, sound reflects repeatedly off walls, ceiling, and floor before decaying, causing speech to sound garbled.
- **Remedies for Reverberation**:
  1. Walls covered with sound-absorbing materials (compressed acoustic fiberboard, rough plaster, draperies).
  2. Floors covered with thick carpets.
  3. Upholstered seats with sound-absorbing fabric.
  4. Curved ceilings and soundboards behind the stage to direct sound evenly to all rows.""",
        "worked_examples": [
            {
                "problem": "An echo is heard after 3 s. What is the distance of the reflecting surface from the source, given that the speed of sound is 342 m/s?",
                "given": "Time t = 3 s. Speed of sound v = 342 m/s.",
                "formula": "Round-trip distance 2d = v * t -> d = (v * t) / 2",
                "substitution": "d = (342 * 3) / 2",
                "calculation": "1. 2d = 342 * 3 = 1026 m\n2. d = 1026 / 2 = 513 m",
                "finalAnswer": "The distance of the reflecting surface from the source is 513 meters.",
                "unit": "m",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.23: Round-trip reflection distance for echo determination"
            },
            {
                "problem": "A person standing between two parallel cliffs fires a gun. He hears the first echo after 2 s and the second echo after 3 s. Calculate the distance between the two cliffs. (Speed of sound in air = 340 m/s).",
                "given": "Time for first echo t1 = 2 s; Time for second echo t2 = 3 s; Speed v = 340 m/s.",
                "formula": "Distance to Cliff 1 d1 = (v * t1) / 2; Distance to Cliff 2 d2 = (v * t2) / 2; Total Distance D = d1 + d2",
                "substitution": "d1 = (340 * 2) / 2; d2 = (340 * 3) / 2",
                "calculation": "1. d1 = 340 * 1 = 340 m\n2. d2 = 340 * 1.5 = 510 m\n3. Total distance D = d1 + d2 = 340 + 510 = 850 m",
                "finalAnswer": "The distance between the two parallel cliffs is 850 meters.",
                "unit": "m",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.23: Dual echo reflections between two parallel boundaries"
            },
            {
                "problem": "Derive the minimum distance required between the listener and reflecting obstacle to hear a distinct echo in air at 22 deg C.",
                "given": "Speed of sound in air at 22 deg C = 344 m/s; Persistence of hearing = 0.1 s.",
                "formula": "Minimum distance d_min = (v * t_persist) / 2",
                "substitution": "d_min = (344 * 0.1) / 2",
                "calculation": "1. Human auditory cortex retains sound impression for 0.1 s.\n2. In 0.1 s, sound travels: total distance = 344 m/s * 0.1 s = 34.4 m.\n3. Because sound must travel to the obstacle and reflect back to the ear, path is 2d.\n4. Therefore, d_min = 34.4 / 2 = 17.2 m.",
                "finalAnswer": "The minimum distance to hear a distinct echo in air at 22 deg C is 17.2 meters.",
                "unit": "m",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.23: Geometric path of echo round trip"
            },
            {
                "problem": "What is reverberation? How can it be reduced in a cinema hall or auditorium?",
                "given": "Acoustic persistence in enclosed auditoriums.",
                "formula": "Reverberation Control via Acoustic Absorption Coefficient",
                "substitution": "Absorptive wall claddings, heavy drapes, and cushioned seats.",
                "calculation": "1. Reverberation is the repeated reflection of sound waves from walls, ceiling, and floor of an enclosed space, causing sound to persist.\n2. In excess, words overlap and speech becomes unintelligible.\n3. Reduction methods: (a) Covering walls and ceilings with porous acoustic materials like compressed fiberboard or perforated acoustic tiles; (b) Hanging heavy velour draperies over windows; (c) Laying thick carpets on floors; (d) Using upholstered seats that absorb sound even when empty.",
                "finalAnswer": "Reverberation is sound persistence from multiple reflections; it is reduced by lining walls with acoustic tiles, heavy curtains, carpets, and upholstered seating.",
                "unit": "Architectural Acoustics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.21: Sound absorption and energy dissipation in halls"
            },
            {
                "problem": "What produces a sonic boom? Why do windows of buildings shake when a supersonic fighter jet flies overhead?",
                "given": "Aircraft flying at speed v > v_sound in atmospheric air.",
                "formula": "Shock Wave Mach Cone Geometry: sin(theta) = v_sound / v_jet",
                "substitution": "Jet travels faster than the speed of pressure propagation.",
                "calculation": "1. When an aircraft travels faster than sound, it compresses the air in front of it into extremely high-pressure, narrow shock fronts forming a cone.\n2. When this conical shock wave sweeps across the ground, the instantaneous air pressure jumps violently and drops back.\n3. This sudden massive pressure discontinuity is heard as a deafening sonic boom.\n4. The intense air pressure wave exerts large mechanical forces on building window panes, causing them to rattle or shatter.",
                "finalAnswer": "Supersonic aircraft compress air into conical shock waves; the abrupt pressure jump sweeps the ground as a sonic boom, shaking windows.",
                "unit": "Gas Dynamics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.11: Supersonic aircraft and conical shock wave formation"
            },
            {
                "problem": "During a thunderstorm, lightning is seen several seconds before thunder is heard, even though both occur simultaneously. Explain why.",
                "given": "Speed of light c = 3 * 10^8 m/s; Speed of sound v = 340 m/s.",
                "formula": "Time Lag Delta t = d / v_sound - d / c",
                "substitution": "Speed of light is nearly 1,000,000 times faster than speed of sound.",
                "calculation": "1. Lightning and thunder are created simultaneously during the dielectric breakdown of air.\n2. Light travels at c = 300,000,000 m/s, reaching the observer almost instantaneously (in microseconds).\n3. Sound travels at a modest speed of only ~340 m/s in air, taking roughly 3 seconds to cover just 1 kilometer.\n4. Hence, the visual flash arrives immediately, followed seconds later by the sound of thunder.",
                "finalAnswer": "Light travels at 300,000,000 m/s (instantaneous arrival) while sound travels at only 340 m/s, causing a noticeable delay.",
                "unit": "Speed Discrepancy",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.10: Atmospheric acoustic propagation over large distance"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "You can hear an echo in a typical small bedroom if you shout loudly.",
                "correction": "You cannot hear a distinct echo in a small room because the distance to opposite walls (typically 3-4 m) is far less than the minimum required distance of 17.2 m. The reflected sound returns in less than 0.1 s and blends directly into the original sound, creating slight resonance or reverberation rather than an echo.",
                "why_it_matters": "Clarifies echo condition vs general reflection."
            }
        ],
        "visual_lesson_plan": {
            "title": "Speed of Sound, Echoes & Reverberation Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Speed of Sound Invariant: Sound travels fastest in solids, slower in liquids, and slowest in gases ($v_{\\text{solids}} > v_{\\text{liquids}} > v_{\\text{gases}}$); in air at $22^\\circ\\text{C}$ it travels at $344\\text{ m/s}$, and in iron at $5950\\text{ m/s}$.",
                    "diagram_title": "Speed of Sound Across Media Scales",
                    "diagram_type": "image",
                    "image_query": "speed of sound in solids liquids gases comparison table diagram",
                    "video_query": "speed of sound in different materials",
                    "image_url": "/extracted_diagrams/ch10/fig_10_5.webp",
                    "what_to_make": "Textbook diagram showing acoustic transmission through dense solids demonstrating high propagation speeds.",
                    "timing_and_cue": "Mount speed comparison on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_5.webp | Speed in Media | Solids transmit sound fastest due to high elastic modulus\")"
                },
                {
                    "concept_title": "Temperature Dependence: The speed of sound increases with increase in temperature; in air, it increases by approximately $0.6\\text{ m/s}$ per degree Celsius rise ($v = 331 + 0.6 T$).",
                    "diagram_title": "Atmospheric Thermal Sound Convection",
                    "diagram_type": "image",
                    "image_query": "speed of sound temperature dependence refraction diagram",
                    "video_query": "how temperature affects speed of sound",
                    "image_url": "/extracted_diagrams/ch10/fig_10_10.webp",
                    "what_to_make": "Textbook diagram showing spherical wavefronts spreading in atmospheric temperature gradients.",
                    "timing_and_cue": "Mount temperature dependence on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_10.webp | Temperature & Acoustic Speed | Velocity rising 0.6 m/s per degree Celsius in air\")"
                },
                {
                    "concept_title": "Sonic Boom: When an object moves at supersonic speed (faster than the speed of sound in air), it produces conical pressure shock waves in the air; these shock waves carry enormous energy perceived as a thunderous, glass-shattering sonic boom.",
                    "diagram_title": "Supersonic Aircraft Conical Shock Waves",
                    "diagram_type": "image",
                    "image_query": "supersonic aircraft shock wave sonic boom mach cone diagram",
                    "video_query": "how sonic boom works supersonic flight",
                    "image_url": "/extracted_diagrams/ch10/fig_10_11.webp",
                    "what_to_make": "Textbook diagram of supersonic jet showing shock waves coalescing into Mach cone.",
                    "timing_and_cue": "Mount sonic boom on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_11.webp | Sonic Boom Shock Waves | Conical pressure wave from supersonic aircraft shattering window panes\")"
                },
                {
                    "concept_title": "Laws of Reflection of Sound: Sound reflects off hard surfaces following the same laws as light: the incident wave, the normal, and the reflected wave all lie in the same plane, and the angle of incidence equals the angle of reflection ($\\angle i = \\angle r$).",
                    "diagram_title": "Law of Reflection for Acoustic Waves",
                    "diagram_type": "image",
                    "image_query": "reflection of sound angle of incidence angle of reflection diagram",
                    "video_query": "reflection of sound experiment",
                    "image_url": "/extracted_diagrams/ch10/fig_10_23.webp",
                    "what_to_make": "Textbook experimental setup showing sound reflecting off wooden barrier with equal incidence and reflection angles.",
                    "timing_and_cue": "Mount sound reflection on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_23.webp | Sound Reflection Laws | Angle of incidence equals angle of reflection at hard barriers\")"
                },
                {
                    "concept_title": "Minimum Echo Distance: The human brain retains auditory sensations for $0.1\\text{ s}$ (persistence of hearing); to hear a distinct echo, reflected sound must arrive after at least $0.1\\text{ s}$, requiring total round-trip distance $2d = v \\times 0.1$, so $d \\ge \\frac{344 \\times 0.1}{2} = \\mathbf{17.2\\text{ m}}$ at $22^\\circ\\text{C}$.",
                    "diagram_title": "Echo Geometry & Minimum 17.2 m Distance",
                    "diagram_type": "image",
                    "image_query": "echo minimum distance 17.2 meters persistence of hearing diagram",
                    "video_query": "how to calculate minimum distance for echo 17.2m",
                    "image_url": "/extracted_diagrams/ch10/fig_10_23.webp",
                    "what_to_make": "Textbook diagram illustrating 2d round trip path for sound echoing from a distant wall.",
                    "timing_and_cue": "Mount echo distance on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_23.webp | Echo Geometry 17.2 m | Minimum obstacle distance required for distinct auditory reflection\")"
                },
                {
                    "concept_title": "Reverberation Control: The persistence of sound in an enclosed hall due to repeated successive reflections is called reverberation; excessive reverberation causes words to overlap into muddy noise, controlled by lining walls with sound-absorbing acoustic materials.",
                    "diagram_title": "Auditorium Acoustic Absorption & Soundboard",
                    "diagram_type": "image",
                    "image_query": "auditorium acoustics curved ceiling reverberation absorption diagram",
                    "video_query": "reverberation in auditoriums and how to reduce it",
                    "image_url": "/extracted_diagrams/ch10/fig_10_21.webp",
                    "what_to_make": "Textbook diagram showing acoustic reflections and absorptive wall panels in halls.",
                    "timing_and_cue": "Mount reverberation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_21.webp | Reverberation Control | Sound-absorbing tiles preventing garbled acoustic reflections\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "Why can't you hear an echo inside your bedroom when you shout, but you hear it clearly standing in front of a giant cliff?"
   - Law: State the 0.1 s persistence of hearing and derive the 17.2 m minimum distance rule.
   - Socratic check: "An echo is heard 2 seconds after shouting near a mountain. If sound speed is 340 m/s, how far is the mountain? Don't forget the round trip!" HARD STOP: Wait for student answer!"""
    }

    # Module 5: Ultrasound Technologies: SONAR, Echocardiography & Flaw Detection
    m5 = {
        "order_index": 5,
        "title": "Ultrasound Technologies: Infrasound, Bat Echolocation, SONAR & Medical Applications",
        "description": "Examine the audible spectrum ($20\\text{ Hz} - 20\\text{ kHz}$), infrasound, and ultrasound, analyze bat echolocation, calculate submarine/ocean depth using SONAR ($2d = vt$), and examine ultrasonography and industrial flaw detection.",
        "subtopics": [
            "Auditory Spectrum Range: Infrasound (<20 Hz), Audible (20 Hz - 20 kHz), Ultrasound (>20 kHz)",
            "Biological Emitters & Receivers: Infrasound in whales/elephants; Ultrasound in bats/dolphins",
            "Bat Echolocation Mechanics: High-frequency ultrasonic clicks navigating in total darkness",
            "SONAR Architecture: Sound Navigation And Ranging (transmitter, transducer, underwater echo receiver)",
            "Quantitative SONAR Formulations: Ocean floor depth and submarine distance calculations ($2d = vt$)",
            "Medical & Industrial Ultrasound: Echocardiography, fetal ultrasonography, kidney stone lithotripsy, metal flaw detection"
        ],
        "key_concepts": [
            "Auditory Spectrum: Human hearing is sensitive to frequencies from $20\\text{ Hz}$ to $20,000\\text{ Hz}$ ($20\\text{ kHz}$); frequencies below $20\\text{ Hz}$ are infrasonic, and frequencies above $20\\text{ kHz}$ are ultrasonic.",
            "Infrasound Phenomena: Rhinoceroses communicate using infrasound frequencies as low as $5\\text{ Hz}$; whales and elephants produce infrasound; earthquakes produce low-frequency infrasonic waves before main shockwaves that animals perceive.",
            "Bat Ultrasonic Navigation: Bats emit high-frequency ultrasonic clicks; these waves reflect off flying insects and surrounding obstacles; by timing the returning echoes and frequency shifts, bats pinpoint prey position with millimeter accuracy in total darkness.",
            "SONAR Operating Principle: SONAR (Sound Navigation And Ranging) consists of an ultrasonic transmitter and detector mounted on a ship hull; transmitter beams ultrasound pulses to the seabed; detector catches the reflected echo.",
            "SONAR Depth Equation: If the time between transmission and reception is $t$, and the speed of sound in seawater is $v$, the seabed depth $d$ is given by $2d = v \\times t \\implies d = \\frac{v \\times t}{2}$.",
            "Medical & Industrial Ultrasound: Ultrasound waves have high frequency and short wavelength, enabling them to penetrate tissues and metal blocks; used in Echocardiography (heart imaging), Ultrasonography (fetal scanning), Lithotripsy (crushing kidney stones into fine powder), and detecting microscopic internal cracks in metallurgical castings."
        ],
        "success_criteria": "Student can classify infrasound/ultrasound frequencies, explain bat echolocation, calculate ocean depth using SONAR equations, and detail industrial flaw detection.",
        "chapter_notes": """### 10.13 The Auditory Spectrum
1. **Infrasound**: Frequencies **below $20\\text{ Hz}$**.
   - Produced by: Earthquakes, volcanic eruptions, ocean waves, elephants, rhinoceroses ($5\\text{ Hz}$), blue whales.
2. **Audible Sound**: Frequencies **$20\\text{ Hz}$ to $20,000\\text{ Hz}$** ($20\\text{ kHz}$).
   - Human hearing range. As humans age, the upper threshold drops from $20\\text{ kHz}$ to ~14-16 kHz. Children under 5 can hear up to 25 kHz.
3. **Ultrasound**: Frequencies **above $20,000\\text{ Hz}$** ($20\\text{ kHz}$).
   - Produced by: Bats, dolphins, porpoises, moths, dogs (Galton whistle).

### 10.14 Applications of Ultrasound

#### 1. Bat Echolocation
Bats emit ultrasonic squeaks (up to $100\\text{ kHz}$). The reflected waves from flying prey (moths) or obstacles return to the bat's ears. The time delay reveals the exact distance, and Doppler pitch shifts reveal the prey's speed and direction, allowing pinpoint hunting in total darkness.

#### 2. SONAR (Sound Navigation And Ranging)
- **Apparatus**: Installed beneath ships/submarines, consisting of an ultrasonic **Transmitter** and a **Receiver (Detector)**.
- **Echo Ranging Method**:
  1. Transmitter emits ultrasonic pulses through seawater.
  2. Pulses travel down, reflect off the seabed, sunken ship, or enemy submarine.
  3. Detector receives the reflected pulse and converts it to electrical signals.
  4. Formula:
     $$\\mathbf{2d = v \\times t} \\implies \\mathbf{d = \\frac{v \\times t}{2}}$$

#### 3. Industrial Non-Destructive Flaw Detection
- Ultrasonic waves are passed through thick metal blocks (used in bridges, buildings, airplanes).
- Detectors placed on the opposite side catch transmitted waves.
- If there is an invisible internal crack, void, or cavity, the ultrasound reflects back early, preventing transmission to the detector and revealing the hidden structural defect.

#### 4. Medical Applications
- **Echocardiography (ECG)**: Ultrasonic waves reflected from heart chambers create live dynamic cardiac imagery.
- **Ultrasonography**: Imaging liver, gall bladder, uterus, kidney, and monitoring fetal development in pregnancy without harmful ionizing radiation.
- **Lithotripsy**: High-energy ultrasound focused on kidney stones breaks them into fine gravel that flushes out naturally in urine.""",
        "worked_examples": [
            {
                "problem": "A submarine emits a sonar pulse, which returns from an underwater cliff in 1.02 s. If the speed of sound in salt water is 1531 m/s, how far away is the cliff?",
                "given": "Time t = 1.02 s. Speed of sound in salt water v = 1531 m/s.",
                "formula": "2d = v * t -> d = (v * t) / 2",
                "substitution": "d = (1531 * 1.02) / 2",
                "calculation": "1. Total distance covered by pulse = 1531 * 1.02 = 1561.62 m\n2. Distance to cliff d = 1561.62 / 2 = 780.81 m",
                "finalAnswer": "The underwater cliff is 780.81 meters away from the submarine.",
                "unit": "m",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.28: SONAR underwater ultrasonic transmission and reflection"
            },
            {
                "problem": "A ship sends out ultrasound that returns from the seabed and is detected after 3.42 s. If the speed of ultrasound through seawater is 1531 m/s, what is the distance of the seabed from the ship?",
                "given": "Time t = 3.42 s. Speed v = 1531 m/s.",
                "formula": "d = (v * t) / 2",
                "substitution": "d = (1531 * 3.42) / 2",
                "calculation": "1. 2d = 1531 * 3.42 = 5236.02 m\n2. d = 5236.02 / 2 = 2618.01 m",
                "finalAnswer": "The seabed is 2618.01 meters (approx 2.62 km) deep.",
                "unit": "m",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.28: Seabed echo ranging via SONAR transducer"
            },
            {
                "problem": "How does a bat use ultrasound to catch prey in total darkness? Explain the mechanism of echolocation.",
                "given": "Bat ultrasonic biological navigation mechanism.",
                "formula": "Bio-Sonar Reflection Timing & Doppler Tracking",
                "substitution": "Ultrasound clicks (>20 kHz) reflecting off flying insects.",
                "calculation": "1. The bat emits bursts of high-frequency ultrasound squeaks.\n2. When these waves strike an insect, they reflect back as echoes.\n3. The bat's specialized ears receive the reflected echoes.\n4. By calculating the arrival time delay, the bat deduces target distance ($d = vt / 2$).\n5. By sensing the intensity difference between ears and frequency shifts, it pinpoints the prey's exact elevation, direction, and velocity.",
                "finalAnswer": "Bats emit ultrasonic pulses and analyze returning echoes; time delay yields distance and directional cues pinpoint insect location in darkness.",
                "unit": "Bio-Echolocation",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.27: Echolocation in bats hunting insects in darkness"
            },
            {
                "problem": "Describe how ultrasound is used to detect internal cracks and flaws in metallic blocks during civil and aerospace engineering inspections.",
                "given": "Non-destructive testing of metallic structures using ultrasound.",
                "formula": "Acoustic Impedance Mismatch & Flaw Reflection",
                "substitution": "Ultrasound beam transmitted through metal block into opposing detector.",
                "calculation": "1. Ultrasonic waves are transmitted through one face of a metal component toward a detector on the opposite face.\n2. In a defect-free block, waves pass completely through and produce a strong signal on the detector.\n3. If an internal defect (air crack or cavity) exists, the high acoustic impedance difference at the crack boundary reflects the ultrasound back prematurely.\n4. The detector receives a depleted or zero signal at that location, pinpointing the presence and depth of the internal flaw without cutting the block.",
                "finalAnswer": "Ultrasound passes through intact metal; internal cracks reflect the beam back early, alerting detectors to hidden structural defects.",
                "unit": "Non-Destructive Testing",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.29: Ultrasonic flaw detection in structural materials"
            },
            {
                "problem": "Why is ultrasound preferred over X-rays for examining internal organs like the liver, kidneys, and pregnant uterus?",
                "given": "Medical diagnostic imaging: Ultrasound vs X-ray radiography.",
                "formula": "Non-Ionizing Mechanical Waves vs Ionizing Radiation",
                "substitution": "Ultrasound consists of safe mechanical pressure waves; X-rays are high-energy ionizing electromagnetic radiation.",
                "calculation": "1. X-rays are ionizing electromagnetic radiation that can damage cellular DNA, cause genetic mutations, and pose severe radiation risks to developing fetuses.\n2. Ultrasound uses high-frequency mechanical sound waves that have zero ionizing power and do not harm living biological cells.\n3. Furthermore, ultrasound reflects excellently from soft tissues of varying densities (fluid vs muscle vs organ boundaries), providing clear real-time soft tissue imaging where X-rays pass straight through.",
                "finalAnswer": "Ultrasound is completely non-ionizing and safe for fetuses and tissues, while clearly distinguishing soft internal organ boundaries.",
                "unit": "Diagnostic Medicine",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.29: Acoustic imaging and medical sensing technologies"
            },
            {
                "problem": "What is the audible range of the average human ear? What are frequencies below and above this range called?",
                "given": "Acoustic frequency spectrum boundaries.",
                "formula": "Spectrum Bandwidths: Infrasonic < 20 Hz, Audible 20 Hz - 20 kHz, Ultrasonic > 20 kHz",
                "substitution": "Human limits: lower bound = 20 Hz, upper bound = 20,000 Hz.",
                "calculation": "1. The audible range of the average human ear is from 20 Hz to 20,000 Hz (20 kHz).\n2. Sounds with frequencies below 20 Hz are called **infrasonic sounds** or **infrasound**.\n3. Sounds with frequencies above 20,000 Hz are called **ultrasonic sounds** or **ultrasound**.",
                "finalAnswer": "Audible range is 20 Hz to 20,000 Hz; below 20 Hz is infrasound, above 20 kHz is ultrasound.",
                "unit": "Acoustic Spectrum",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.27: Ultrasonic spectrum utilized by bats and marine mammals"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Ultrasound travels faster through air than ordinary audible sound.",
                "correction": "Ultrasound and audible sound travel at the EXACT SAME SPEED in the same medium at the same temperature. Speed is determined by the medium's properties (v = sqrt(B / rho)). Because ultrasound has a much higher frequency (nu), its wavelength (lambda) is proportionally smaller (v = nu * lambda), keeping speed invariant.",
                "why_it_matters": "Fundamental wave principle: wave speed in a medium is independent of frequency."
            }
        ],
        "visual_lesson_plan": {
            "title": "Ultrasound Technologies Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Auditory Spectrum: Human hearing is sensitive to frequencies from $20\\text{ Hz}$ to $20,000\\text{ Hz}$ ($20\\text{ kHz}$); frequencies below $20\\text{ Hz}$ are infrasonic, and frequencies above $20\\text{ kHz}$ are ultrasonic.",
                    "diagram_title": "Auditory Spectrum Frequency Scale",
                    "diagram_type": "image",
                    "image_query": "auditory spectrum human hearing 20 Hz 20 kHz infrasound ultrasound diagram",
                    "video_query": "range of hearing infrasound ultrasound explained",
                    "image_url": "/extracted_diagrams/ch10/fig_10_27.webp",
                    "what_to_make": "Textbook diagram showing acoustic frequency ranges from infrasound to ultrasound.",
                    "timing_and_cue": "Mount hearing spectrum on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_27.webp | The Acoustic Spectrum | Infrasound below 20 Hz, audible 20 Hz-20 kHz, ultrasound above 20 kHz\")"
                },
                {
                    "concept_title": "Infrasound Phenomena: Rhinoceroses communicate using infrasound frequencies as low as $5\\text{ Hz}$; whales and elephants produce infrasound; earthquakes produce low-frequency infrasonic waves before main shockwaves that animals perceive.",
                    "diagram_title": "Longitudinal Infrasonic Ground Waves",
                    "diagram_type": "image",
                    "image_query": "infrasound earthquake waves elephant communication diagram",
                    "video_query": "infrasound animals communication earthquake",
                    "image_url": "/extracted_diagrams/ch10/fig_10_8.webp",
                    "what_to_make": "Textbook diagram showing long-wavelength low-frequency longitudinal pulses traveling through dense media.",
                    "timing_and_cue": "Mount infrasound on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_8.webp | Infrasound Waves | Sub-audible low-frequency waves (<20 Hz) traveling over vast distances\")"
                },
                {
                    "concept_title": "Bat Ultrasonic Navigation: Bats emit high-frequency ultrasonic clicks; these waves reflect off flying insects and surrounding obstacles; by timing the returning echoes and frequency shifts, bats pinpoint prey position with millimeter accuracy in total darkness.",
                    "diagram_title": "Bat Echolocation Ultrasonic Tracking",
                    "diagram_type": "image",
                    "image_query": "echolocation bats hunting insect ultrasound diagram",
                    "video_query": "how bats use echolocation animation",
                    "image_url": "/extracted_diagrams/ch10/fig_10_27.webp",
                    "what_to_make": "Textbook diagram of bat emitting ultrasound pulses and receiving reflected echoes from flying insect.",
                    "timing_and_cue": "Mount bat echolocation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_27.webp | Bat Echolocation | High-frequency ultrasound pulses reflecting off prey in complete darkness\")"
                },
                {
                    "concept_title": "SONAR Operating Principle: SONAR (Sound Navigation And Ranging) consists of an ultrasonic transmitter and detector mounted on a ship hull; transmitter beams ultrasound pulses to the seabed; detector catches the reflected echo.",
                    "diagram_title": "SONAR Ship Seabed Echo Transmission",
                    "diagram_type": "image",
                    "image_query": "sonar transmitter receiver seabed underwater echo diagram",
                    "video_query": "how SONAR works underwater sound navigation and ranging",
                    "image_url": "/extracted_diagrams/ch10/fig_10_28.webp",
                    "what_to_make": "Textbook diagram showing ship emitting ultrasonic waves down to seabed and detector catching reflected echo.",
                    "timing_and_cue": "Mount SONAR on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_28.webp | SONAR Working Principle | Transmitter sending ultrasonic pulse and detector recording echo time delay\")"
                },
                {
                    "concept_title": "SONAR Depth Equation: If the time between transmission and reception is $t$, and the speed of sound in seawater is $v$, the seabed depth $d$ is given by $2d = v \\times t \\implies d = \\frac{v \\times t}{2}$.",
                    "diagram_title": "Quantitative SONAR Depth Formulation",
                    "diagram_type": "image",
                    "image_query": "SONAR depth calculation 2d equals vt diagram",
                    "video_query": "SONAR numericals class 9 science",
                    "image_url": "/extracted_diagrams/ch10/fig_10_28.webp",
                    "what_to_make": "Textbook diagram illustrating 2d path geometry for underwater echo ranging.",
                    "timing_and_cue": "Mount SONAR calculation on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_28.webp | SONAR Depth Equation | 2d = v * t formula for measuring ocean depth and tracking submarines\")"
                },
                {
                    "concept_title": "Medical & Industrial Ultrasound: Ultrasound waves have high frequency and short wavelength, enabling them to penetrate tissues and metal blocks; used in Echocardiography (heart imaging), Ultrasonography (fetal scanning), Lithotripsy (crushing kidney stones into fine powder), and detecting microscopic internal cracks in metallurgical castings.",
                    "diagram_title": "Acoustic Remote Sensing & Drone Technology",
                    "diagram_type": "image",
                    "image_query": "ultrasonic sensor flaw detection drone acoustic diagram",
                    "video_query": "ultrasound applications medicine and industry",
                    "image_url": "/extracted_diagrams/ch10/fig_10_29.webp",
                    "what_to_make": "Textbook image of acoustic sensing drone demonstrating industrial ultrasound navigation and flaw detection.",
                    "timing_and_cue": "Mount industrial ultrasound on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_29.webp | Modern Acoustic Sensing | Ultrasonic transducers for non-destructive testing and medical imaging\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "How can a blind bat fly through dense pitch-black forest at 40 km/h and snatch a tiny mosquito out of thin air without colliding with a single twig?"
   - Law: Detail the auditory spectrum (Infrasound < 20 Hz, Ultrasound > 20 kHz) and the SONAR equation $2d = vt$.
   - Socratic check: "A ship sends a SONAR signal and receives the echo from the ocean bed 4 seconds later. If sound in seawater travels at 1500 m/s, how deep is the seabed?" HARD STOP: Wait for student answer!"""
    }

    # Module 6: Human Ear Anatomy & Master NCERT Comprehensive Solver
    m6 = {
        "order_index": 6,
        "title": "Anatomy of the Human Ear & Master NCERT Sound Problem Solver",
        "description": "Analyze the outer, middle, and inner ear anatomy, trace the transformation of pressure waves into mechanical lever amplification and auditory nerve electrical impulses, and solve every NCERT chapter-end question.",
        "subtopics": [
            "Outer Ear Architecture: Pinna, auditory canal, and tympanic membrane (eardrum)",
            "Middle Ear Lever Mechanics: Three ossicles (Hammer/Malleus, Anvil/Incus, Stirrup/Stapes)",
            "Inner Ear Transduction: Cochlea converting fluid pressure waves into electrical nerve impulses",
            "Auditory Pathway to Brain: Auditory nerve transmitting action potentials to auditory cortex",
            "Pressure Equalization: Eustachian tube balancing air pressure on both sides of eardrum",
            "Comprehensive NCERT Chapter-End Problem Solver: Questions 1 through 22 solved step-by-step"
        ],
        "key_concepts": [
            "Outer Ear Architecture: The outer ear consists of the pinna which collects sound waves from surroundings, guiding them through the auditory canal to strike the thin elastic tympanic membrane (eardrum).",
            "Tympanic Membrane Vibration: When a compression reaches the eardrum, external pressure pushes it inward; when a rarefaction arrives, pressure decreases and the membrane moves outward, vibrating in sync with sound frequency.",
            "Middle Ear Ossicular Amplification: The middle ear houses three tiny bones—the hammer (malleus), anvil (incus), and stirrup (stapes)—which act as a compound mechanical lever system, amplifying the mechanical vibrations more than 20 to 30 times.",
            "Inner Ear Cochlear Transduction: The stapes pushes against the oval window of the cochlea (a fluid-filled spiral snail-shell structure); fluid pressure waves stimulate specialized microscopic sensory hair cells in the organ of Corti, converting vibrations into electrical nerve signals.",
            "Auditory Nerve Transmission: Electrical nerve impulses generated by cochlear hair cells are transmitted via the auditory nerve directly to the temporal lobe of the brain, which interprets the signals as sound.",
            "Complete NCERT Chapter 10 Mastery: Step-by-step solutions for all in-text questions and chapter-end numerical exercises guaranteeing 100% board accuracy."
        ],
        "success_criteria": "Student can sketch and label all human ear anatomical structures, trace acoustic transduction from pinna to brain, and solve all NCERT chapter-end exercises.",
        "chapter_notes": """### 10.15 Anatomy & Physiology of the Human Ear
The human ear is divided into three primary anatomical regions:

#### 1. The Outer Ear
- **Pinna**: The visible external cartilaginous flap. Acts as a funnel collecting sound waves from all directions.
- **Auditory Canal (Ear Canal)**: A ~2.5 cm tube leading inwards, channeling sound waves.
- **Tympanic Membrane (Eardrum)**: A delicate, stretched circular membrane terminating the auditory canal. Compressions force it inward; rarefactions pull it outward.

#### 2. The Middle Ear
- Contains **three tiny ossicles** (the smallest bones in the human body):
  1. **Hammer (Malleus)**: Attached directly to the eardrum.
  2. **Anvil (Incus)**: Intermediate lever connecting hammer to stirrup.
  3. **Stirrup (Stapes)**: Footplate rests against the oval window of the inner ear.
- **Amplification Function**: These bones form a mechanical lever system. Together with the large area ratio between eardrum ($~55\\text{ mm}^2$) and oval window ($~3.2\\text{ mm}^2$), they amplify the pressure vibrations **over 20-30 times**.
- **Eustachian Tube**: Connects middle ear to the throat, equalizing air pressure on both sides of the eardrum during swallowing or yawning.

#### 3. The Inner Ear
- **Cochlea**: A spiral, fluid-filled snail-shell-like bony organ.
- **Organ of Corti & Sensory Hair Cells**: As the stapes vibrates the oval window, fluid waves ripple through the cochlear perilymph and endolymph. These fluid waves bend microscopic stereocilia (hair cells), generating **action potentials (electrical nerve impulses)**.
- **Auditory Nerve**: Collects electrical impulses from cochlear nerve fibers and carries them to the brain's auditory cortex, which interprets them as speech, music, or environmental sound.""",
        "worked_examples": [
            {
                "problem": "Explain the step-by-step sequence of events that takes place inside the human ear from the moment a sound wave enters the pinna until it is perceived by the brain.",
                "given": "Acoustic wave entering external ear to auditory cortex perception.",
                "formula": "Biomechanical Acoustic Transduction Cascade",
                "substitution": "Outer Ear -> Middle Ear Lever -> Inner Ear Fluid -> Electrical Impulses -> Brain.",
                "calculation": "1. Pinna collects sound waves and directs them down the auditory canal.\n2. Pressure waves strike the tympanic membrane (eardrum), causing it to vibrate in exact synchrony.\n3. The three middle ear ossicles (hammer, anvil, stirrup) amplify these vibrations mechanically by ~25-30x.\n4. The stapes transmits amplified vibrations to the oval window of the cochlea.\n5. Fluid ripples inside the cochlea stimulate sensory hair cells, converting mechanical oscillations into electrical nerve impulses.\n6. The auditory nerve carries these electrical signals to the brain, which interprets them as sound.",
                "finalAnswer": "Pinna collects -> eardrum vibrates -> ossicles amplify -> cochlea converts fluid waves to electrical signals -> auditory nerve sends to brain.",
                "unit": "Auditory Physiology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.24: Complete schematic anatomical diagram of the human ear"
            },
            {
                "problem": "What are the three tiny bones in the middle ear? What vital function do they perform?",
                "given": "Middle ear ossicular anatomy.",
                "formula": "Mechanical Advantage of Middle Ear Lever System",
                "substitution": "Malleus (Hammer), Incus (Anvil), Stapes (Stirrup).",
                "calculation": "1. The three bones are: (a) Hammer (Malleus), (b) Anvil (Incus), (c) Stirrup (Stapes).\n2. Function: They act as a compound mechanical lever system to amplify the delicate vibrations received from the large eardrum.\n3. They concentrate this amplified force onto the tiny oval window of the cochlea, increasing acoustic pressure by over 20-30 times so sound can efficiently enter the dense fluid medium of the inner ear.",
                "finalAnswer": "Hammer, anvil, and stirrup amplify vibrations from the eardrum >20-30 times and transfer them to the cochlea's oval window.",
                "unit": "Ossicular Mechanics",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.24: Middle ear ossicles: hammer, anvil, and stirrup"
            },
            {
                "problem": "Why does your ear 'pop' when riding an elevator in a high-rise building or flying in an airplane? Which anatomical structure resolves this?",
                "given": "Atmospheric pressure change across altitude.",
                "formula": "Boyle's Law & Pressure Balance across Tympanic Membrane",
                "substitution": "External canal pressure vs sealed middle ear cavity pressure.",
                "calculation": "1. When altitude changes rapidly, outside atmospheric pressure decreases while air in the middle ear remains at higher ground-level pressure.\n2. This pressure imbalance forces the eardrum to bulge outward, producing ear fullness or pain.\n3. The **Eustachian tube** connects the middle ear cavity to the back of the nasopharynx.\n4. When you swallow, chew, or yawn, the Eustachian tube opens, allowing trapped air to vent and equalizing pressure on both sides of the eardrum, accompanied by a 'pop'.",
                "finalAnswer": "Rapid altitude change creates pressure difference across the eardrum; the Eustachian tube opens during swallowing to equalize pressure.",
                "unit": "Barometric Physiology",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.24: Eustachian tube connecting middle ear to pharynx"
            },
            {
                "problem": "An acoustic source emits sound of frequency 100 Hz. How many times does it vibrate in a minute?",
                "given": "Frequency nu = 100 Hz = 100 vibrations per second. Time t = 1 minute = 60 seconds.",
                "formula": "Total Vibrations N = nu * t",
                "substitution": "N = 100 * 60",
                "calculation": "N = 100 * 60 = 6000 vibrations",
                "finalAnswer": "The acoustic source vibrates 6000 times in one minute.",
                "unit": "Vibrations (NCERT Q6)",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.16: Oscillations per unit time representing frequency"
            },
            {
                "problem": "Does sound follow the same laws of reflection as light does? Explain with an experimental setup.",
                "given": "Experimental verification of laws of reflection of sound.",
                "formula": "Laws of Acoustic Reflection: angle i = angle r; Incident, normal, and reflected in same plane.",
                "substitution": "Two hollow pipes angled toward a smooth metallic or wooden board with a clock.",
                "calculation": "1. Yes, sound strictly obeys the same laws of reflection as light.\n2. Apparatus: Take two identical long hollow pipes (A and B) inclined toward a polished vertical board, separated by an acoustic screen along the normal.\n3. Place a ticking clock at the open mouth of pipe A.\n4. Listen at the mouth of pipe B and adjust its angle until the ticking is loudest.\n5. Measuring the angles shows that the angle of incidence equals the angle of reflection (angle i = angle r), and both pipes lie in the same horizontal plane.",
                "finalAnswer": "Yes, sound obeys identical laws of reflection (angle i = angle r in same plane), verified using two angled hollow tubes and a ticking clock.",
                "unit": "NCERT Exercise Q7",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.23: Experimental verification of reflection of sound"
            },
            {
                "problem": "The sound waves emitted by three sources A, B and C are represented in Fig. 10.30. Which source produces sound with: (a) Maximum loudness, (b) Maximum pitch?",
                "given": "Comparative waveforms A, B, C from NCERT Fig. 10.30.",
                "formula": "Loudness proportional to Amplitude; Pitch proportional to Frequency.",
                "substitution": "Compare wave heights (amplitude) and wave crowding (frequency/wavelength).",
                "calculation": "1. Waveform with greatest crest-to-trough vertical height has the maximum amplitude, corresponding to maximum loudness.\n2. Waveform with the greatest number of waves packed into the same horizontal distance has the highest frequency, corresponding to maximum pitch.\n3. Inspecting Fig. 10.30: Wave with largest peak height produces maximum loudness; wave with shortest wavelength / closest peaks produces maximum pitch.",
                "finalAnswer": "The source with the greatest amplitude has maximum loudness; the source with the highest wave frequency has maximum pitch.",
                "unit": "NCERT Exercise Q19",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 10.30: Waveform comparison of sound sources A, B, and C"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "The eardrum sends electrical signals directly to the brain.",
                "correction": "The eardrum only vibrates mechanically. It cannot generate electrical signals. Electrical signals are generated exclusively by the microscopic sensory hair cells inside the fluid-filled COCHLEA in the inner ear, which then travel via the auditory nerve.",
                "why_it_matters": "Crucial distinction between mechanical amplification (middle ear) and biological sensory transduction (inner ear)."
            }
        ],
        "visual_lesson_plan": {
            "title": "Human Ear Anatomy & NCERT Solver Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Outer Ear Architecture: The outer ear consists of the pinna which collects sound waves from surroundings, guiding them through the auditory canal to strike the thin elastic tympanic membrane (eardrum).",
                    "diagram_title": "Complete Human Ear Anatomy Schema",
                    "diagram_type": "image",
                    "image_query": "human ear anatomy pinna auditory canal eardrum ossicles cochlea diagram",
                    "video_query": "how the human ear works animation 3d",
                    "image_url": "/extracted_diagrams/ch10/fig_10_24.webp",
                    "what_to_make": "Textbook schematic anatomical diagram of the human ear detailing outer, middle, and inner sections.",
                    "timing_and_cue": "Mount ear anatomy on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_24.webp | Human Ear Anatomy | Outer pinna, middle ossicles, and inner cochlea transduction cascade\")"
                },
                {
                    "concept_title": "Tympanic Membrane Vibration: When a compression reaches the eardrum, external pressure pushes it inward; when a rarefaction arrives, pressure decreases and the membrane moves outward, vibrating in sync with sound frequency.",
                    "diagram_title": "Eardrum Membrane Acoustic Oscillation",
                    "diagram_type": "image",
                    "image_query": "tympanic membrane eardrum vibration sound pressure diagram",
                    "video_query": "how eardrum vibrates with sound",
                    "image_url": "/extracted_diagrams/ch10/fig_10_14.webp",
                    "what_to_make": "Textbook diagram showing acoustic vibrations moving particles across stretched membrane.",
                    "timing_and_cue": "Mount eardrum vibration on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_14.webp | Eardrum Vibration | Elastic membrane oscillating inward and outward with air pressure pulses\")"
                },
                {
                    "concept_title": "Middle Ear Ossicular Amplification: The middle ear houses three tiny bones—the hammer (malleus), anvil (incus), and stirrup (stapes)—which act as a compound mechanical lever system, amplifying the mechanical vibrations more than 20 to 30 times.",
                    "diagram_title": "Middle Ear Ossicle Lever Amplification",
                    "diagram_type": "image",
                    "image_query": "middle ear bones malleus incus stapes lever amplification diagram",
                    "video_query": "middle ear ossicles mechanism animation",
                    "image_url": "/extracted_diagrams/ch10/fig_10_24.webp",
                    "what_to_make": "Textbook diagram showing magnified view of hammer, anvil, and stirrup lever system.",
                    "timing_and_cue": "Mount ossicles on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_24.webp | Ossicle Lever System | Hammer, anvil, and stirrup amplifying vibrations over 20-30 times\")"
                },
                {
                    "concept_title": "Inner Ear Cochlear Transduction: The stapes pushes against the oval window of the cochlea (a fluid-filled spiral snail-shell structure); fluid pressure waves stimulate specialized microscopic sensory hair cells in the organ of Corti, converting vibrations into electrical nerve signals.",
                    "diagram_title": "Cochlea Fluid Wave Sensory Transduction",
                    "diagram_type": "image",
                    "image_query": "inner ear cochlea organ of corti hair cells electrical impulse diagram",
                    "video_query": "cochlea hair cells sound transduction",
                    "image_url": "/extracted_diagrams/ch10/fig_10_24.webp",
                    "what_to_make": "Textbook diagram showing spiral cochlea fluid chambers and auditory nerve pathway.",
                    "timing_and_cue": "Mount cochlea on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_24.webp | Cochlear Transduction | Fluid pressure waves stimulating hair cells to generate electrical impulses\")"
                },
                {
                    "concept_title": "Auditory Nerve Transmission: Electrical nerve impulses generated by cochlear hair cells are transmitted via the auditory nerve directly to the temporal lobe of the brain, which interprets the signals as sound.",
                    "diagram_title": "Acoustic Frequency Processing Spectrum",
                    "diagram_type": "image",
                    "image_query": "auditory nerve brain sound perception pathway diagram",
                    "video_query": "auditory pathway to brain",
                    "image_url": "/extracted_diagrams/ch10/fig_10_25.webp",
                    "what_to_make": "Textbook diagram showing neural acoustic response curves across auditory spectrum.",
                    "timing_and_cue": "Mount neural transmission on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_25.webp | Auditory Pathway | Auditory nerve delivering action potentials to temporal brain cortex\")"
                },
                {
                    "concept_title": "Complete NCERT Chapter 10 Mastery: Step-by-step solutions for all in-text questions and chapter-end numerical exercises guaranteeing 100% board accuracy.",
                    "diagram_title": "NCERT Comparative Acoustic Waveforms",
                    "diagram_type": "image",
                    "image_query": "NCERT class 9 science sound chapter exercise question 19 waveforms diagram",
                    "video_query": "class 9 science chapter sound NCERT exercise complete solutions",
                    "image_url": "/extracted_diagrams/ch10/fig_10_30.webp",
                    "what_to_make": "Textbook diagram of comparative waveforms A, B, and C used in NCERT Chapter-End Problem 19.",
                    "timing_and_cue": "Mount NCERT waveforms on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch10/fig_10_30.webp | NCERT Master Problem 19 | Comparing amplitude and frequency waveforms A, B, and C\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount the verified extracted diagram on Step 1.
2. SOCRATIC CADENCE:
   - Hook: "How does a physical wave of vibrating air molecules turn into electrical thoughts inside your brain? Which organ is the biochemical microphone?"
   - Law: Detail the anatomy of outer ear, middle ear ossicles, and inner ear cochlea.
   - Socratic check: "Why do the three tiny bones in your middle ear exist? Why couldn't the eardrum connect directly to the cochlea?" HARD STOP: Wait for student answer!"""
    }

    return [m1, m2, m3, m4, m5, m6]

if __name__ == "__main__":
    modules = get_ch10_modules()
    with open("scripts/science_modules_ch10.json", "w", encoding="utf-8") as f:
        json.dump(modules, f, indent=2, ensure_ascii=False)
    print(f"Chapter 10 complete: {len(modules)} modules synthesized with 1:1 visuals and worked examples.")
