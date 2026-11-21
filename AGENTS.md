# AI Tutor Project Invariants & Behavioral Guidelines

@[pedagogical_and_architecture_rules](.agents/rules/pedagogical_and_architecture_rules.md)

# AI Tutor Pedagogical, Scope & Security Invariants (1–20)

## 1. Target Audience Scope (Classes 6–12 Only)
- The platform is strictly for school students in **Classes 6 to 12** under **CBSE, ICSE, and IB** boards.
- Do NOT include competitive entrance exams (JEE, NEET, CUET) or Undergraduate college curriculum in platform copy, curriculum generation, or pricing tiers unless explicitly instructed.

## 2. Socratic Exam-Topper Teaching Cadence
Whenever designing, prompting, or updating the AI tutor voice instruction:
- **Complete Explanation First (5–6 Sentences per Turn)**: The tutor must never stop after speaking something half or deliver fragmented, cut-off thoughts. In each pedagogical explanation turn, speak properly with rich depth for 5 to 6 well-formed, articulate sentences covering physical intuition, underlying mechanism, and real-world clarity.
- **Explain -> Ask Question -> Continue**: Complete the full 5–6 sentence explanation thoroughly first. ONLY AFTER completing the explanation, ask ONE engaging checkpoint question to verify the student's understanding. When they answer or confirm, continue smoothly with the next stage.
- **Immediate Stop on Student Inquiry**: The moment the student speaks, asks a question, interrupts, or raises a doubt at any time, the tutor must immediately STOP speaking, yield the floor, listen with complete diagnostic attentiveness, address their query directly with clarity and kindness, and only then proceed.
- **Strict 6-Stage Cadence**:
  1. *Real-Life Intuition*: Everyday physical hook/analogy (5–6 complete sentences, proactive visual).
  2. *Concept Formulation*: Precise scientific law, definition, and SI units.
  3. *Precise Example*: Concrete illustration addressing common pitfalls.
  4. *Board Numerical*: Step-by-step layout on the whiteboard (Given -> Formula -> Substitution -> Calculation -> Boxed Answer with Units).
  5. *Check for Understanding*: Ask if the student understood.
     - If NO / hesitant: Break down with visual analogy and co-solve on board.
     - If YES: Advance to Stage 6.
  6. *Board-Exam Numerical*: Poses an authentic board-exam level question matching the student's exact board pattern (CBSE/ICSE/IB).

## 3. Whiteboard is Single Source of Truth for Notes
- Do NOT call a separate post-class note optimization LLM API (`/api/class/optimize-notes`).
- The AI Tutor writes topper-ready, structured notes directly to the chalkboard during class via tool calls.
- These live chalkboard notes are directly saved as the final Master Notes for the student.

## 4. Pinned Identity Context Guard
- When applying `contextWindowCompression` in Gemini Live WebSockets, the student's identity dossier (Name, Class, Board, Pacing, Weak Areas) must be permanently pinned in `systemInstruction`.
- Sliding window context compression must NEVER evict or dilute the student's identity or curriculum context.

## 5. Security & Zero Key Leakage Invariant
- NEVER return raw API keys (such as `process.env.GEMINI_API_KEY`) to the client browser in plaintext JSON or HTML.
- All Gemini Live WebSocket connections and external LLM calls must be proxied or brokered through authenticated server-side endpoints.

## 6. Multi-Board Classroom & Ingestion Standards
- **CBSE**: Follows NCERT standard structure, derivation-centric, 50% NEP 2020 Competency-Based Questions, zero calculators.
- **ICSE**: Exact verbatim definitions (penalize missing clauses), dual-column chalkboard with `[ROUGH_WORK]` margin on the right, Selina Concise / Morning Star publisher alignment, no calculators in Class 10.
- **IB (MYP & DP)**: Statement of Inquiry (SOI), official IB command terms, measurement uncertainty ($\pm \Delta x$), GDC keystroke notes, and toggleable Formula Booklet HUD.

## 7. Zero Hardcoded Fake Diagrams Invariant
- The digital chalkboard must NEVER render static, canned diagrams with hardcoded numbers or fixed problem values (e.g., a fixed 5kg block or fixed refractive index).
- All visual graphs, curves, and kinematic diagrams must be dynamically plotted using **Mafs.dev** pure React/SVG vector math based on the student's actual lesson and equations.
- Diagram elements (forces, rays, circuits) must be drawn dynamically with user-provided parameters via geometry primitives (`draw_shape`).

## 8. Universal Topic-Adaptive Flowcharts
- Whiteboard flowcharts must NEVER be restricted to a single-line or rigid 4-step derivation pattern (`Given -> Formula -> Substitution -> Boxed Answer`).
- The flowchart engine must support:
  1. Multi-row wrapping with downward connecting return arrows.
  2. Branching decision trees (`A -> B | C`).
  3. Cyclical loops (`cycle: Step 1 -> Step 2 -> Step 3 -> Step 1`) for biological and chemical processes.
  4. Adaptive node widths to prevent horizontal or vertical text overflow.

## 9. Lean Tool Calling & Zero Alias Duplication
- Keep Gemini Live WebSocket tool declarations canonical and lean (at most 12 distinct chalkboard actions).
- NEVER introduce duplicate action aliases (e.g., `table` vs `draw_table`, `graph` vs `draw_graph`, or 5 separate `clear` actions).
- Avoid registering heavy 3D simulation scene enums unless they provide genuine 3D spatial rotation value (e.g. 3D geometry solids).

## 10. Exhaustive Curriculum Module Decomposition & Problem Solving Mandate
- **Module Count**: Every chapter must synthesize a **minimum of 5 to 8 dedicated modules** (never fewer than 5).
- **Universal Problem & Theorem Invariant (Maths & Science)**:
  * Zero omissions: EVERY exercise question (all parts) and EVERY worked example from the textbook must be captured and solved.
  * Every theorem, lemma, corollary, and axiom in Maths must be stated verbatim and proved step-by-step.
  * Every scientific law, definition, and in-text laboratory activity/experiment in Science must be documented with Apparatus, Method, Observation, and Inference.
- **Mathematics Architecture**:
  * All abstract theory and core theorems MUST conclude strictly within **Modules 1 to 2**.
  * **Modules 3 to 8**: Dedicated exercise solvers (one module per exercise/section) where question solving and step-by-step explanations heavily outweigh dry theory.
- **Science Architecture**:
  * Foundational modules prioritize deep, intuitive scientific explanations, physical mechanisms, and laboratory experiments.
  * Chapter-end questions and in-text questions are resolved in dedicated solver modules at the end of the chapter.
  * Every explanatory module MUST STILL retain its 4 to 6 prepared concept questions (`concept_questions`) for active Socratic dialogue during class.

## 11. Secondary & Senior Secondary Multi-Term Syllabus Architecture (Classes 9–12)
- **Mid-Term & Final-Term Partitioning**: Every subject curriculum must partition chapters according to the official board syllabus into **Mid-Term** (Part 1 textbook) and **Final-Term / Annual Exam** (Part 2 textbook). Every module must clearly carry its syllabus term tag (`Mid-Term` vs. `Final-Term`).
  * **Class 9 Mathematics**: Part 1 (*Ganita Prakash / Manjari* Part 1, Chapters 1–8) tagged strictly as `[CBSE Mid-Term Examination Syllabus]`. Part 2 (*Ganita Manjari* Part 2, Chapters 9–14) tagged strictly as `[CBSE Final-Term Examination Syllabus]`.
  * **Class 10 Mathematics**: Partitioned strictly per DoE / CBSE official syllabus bifurcation: Mid-Term (Ch 1, 3, 5, 6, 7, 8) vs Final-Term (Ch 2, 4, 9, 10, 11, 12, 13, 14).
  * **Class 9 Science**: Mid-Term (Ch 2, 3, 4, 5, 6) vs Final-Term (Ch 7, 8, 9, 10, 11, 12, 13).
  * **Class 10 Science**: Mid-Term (Ch 1, 2, 3, 5, 6, 9, 10) vs Final-Term (Ch 4, 7, 8, 11, 12, 13).
  * **Class 11 Physics**: Part 1 (Ch 1–7) tagged `Mid-Term`; Part 2 (Ch 8–14) tagged `Final-Term`.
- **No Artificial Module Length Limits**: Module content must scale to full textbook chapter depth. Senior secondary modules (Classes 11–12) and secondary milestone modules (Classes 9–10) require rigorous physical intuition, formal mathematical derivations, geometric proofs, physical mechanisms, and real-world applications.
- **Exact Textbook Topic Headings**: Every module must preserve the verbatim topic titles, section numbers, theorems, lab experiments, and worked examples from the standard textbook with zero omissions.

## 12. Dynamic Live Visuals & Question-Only Diagram Invariant
- **Zero Static Hardcoded Image URLs in Theory**: Modules must NEVER store hardcoded or brittle external image links for theory concepts in database tables or module JSONs.
- **Search Engine First for Concepts**: Concept visuals must query Search Engines (Bing Images with strict SafeSearch) FIRST for exact topic diagrams, Wikipedia PageImages SECOND for authoritative encyclopedic figures, and Wikimedia Commons THIRD.
- **Authentic Book Figures Strictly For Questions**: High-resolution diagrams extracted directly from textbook PDFs (`public/extracted_diagrams/`) are preserved and bound EXCLUSIVELY to questions (worked examples and practice/quiz problems) that explicitly cite a figure (e.g., "In Fig. 12.10...", "refer to the figure below"). The digital chalkboard automatically renders these figures via `draw_image` when the tutor presents that specific problem.
- **Strict Content Safety Filter**: Every visual query must pass through `isSafeEducationalImage` and `isSafeEducationalVideo` filters with strict SafeSearch (`&adlt=strict` / SafeSearch=Strict) to permanently block adult, violent, harmful, or non-educational content.
- **YouTube Classroom Video Demonstrations**: Scientific and mathematical videos must play seamlessly inside the whiteboard modal via responsive, secure YouTube embedded iframes (`video/youtube`), with native HTML5 fallback for direct media streams.

## 13. Socratic Cadence Gating & Anti-Premature Page Turn Guard
- **No Premature Page Flips on Affirmations**: Casual conversational affirmations (`"yes"`, `"ok"`, `"haan"`, `"sure"`, `"understood"`) in voice or text MUST NEVER advance the concept or turn the chalkboard page.
- **Strict Stage 1–4 Lock**: The AI tutor is strictly forbidden from calling `concept_completed` or `concept_done` during Stages 1 to 4 (Intuition, Formulation, Worked Application, Board Numerical). When the student affirms understanding during initial stages, the tutor must simply continue to the next stage of the same concept.
- **Advancement Exclusively on Stage 6 or Explicit Command**: The chalkboard page advances ONLY after the student attempts and resolves the Stage 5/6 checkpoint question, OR if the student explicitly commands advancement (`"next concept"`, `"next page"`, `"move to next concept"`, `"aage badho"`).

## 14. Pure Chalkboard Mathematical Typography
- **Zero Raw Programming Operators**: The chalkboard must NEVER render raw code syntax: no raw asterisks (`*`, `**`, `***`), no raw carets (`^`), and no raw double slashes (`//`).
- **Authentic Unicode Mathematics**: All mathematical expressions must format as standard textbook mathematics with superscripts ($x², v², 10⁻¹¹$), subscripts ($v₀, F_{\text{net}}$), Greek letters ($\theta, \alpha, \beta, \gamma, \Delta, \lambda, \mu, \pi, \rho, \sigma, \tau, \omega, \Omega$), calculus symbols ($\int, \iint, \oint, \sum, \prod, \partial, \nabla$), and standard arithmetic operators ($\times, \cdot, \div, \pm, \le, \ge, \ne, \approx, \to, \Rightarrow, \rightleftharpoons$).

## 15. Exhaustive Problem Solving & Step-by-Step Pedagogical Layout
- **Zero Omission Invariant**: Every single textbook exercise question (all parts (i), (ii), (iii)...), worked example, and "Think and Reflect" / "Try These" problem must be fully solved in the curriculum modules.
- **Step-by-Step Topper Layout**: All problem solutions must adhere to the standard board topper layout:
  * **Given**: Stating all given quantities with symbols and standard units.
  * **To Prove / To Find**: Clear mathematical objective.
  * **Formula / Theorem Used**: Explicit naming of theorems, axioms, or algebraic identities.
  * **Construction (for Geometry)**: Precise construction lines/points.
  * **Step-by-Step Proof / Calculation**: Clear logical transitions without skipping steps.
  * **Rough Work Margin**: Secondary scratch calculations.
  * **Boxed Final Answer**: Explicit final answer with correct units or "Hence Proved!".

## 16. Search-Engine-First Visual Execution & LLM Diagram Fallback Guard
- **Zero Premature LLM Generation during Live Instruction**: When visual diagrams are requested by the tutor (`render_svg_diagram`, `draw_diagram`, `draw_image`, or graph gating fallbacks), the classroom must query the online search engine pipeline (`/api/diagram/search-image`) FIRST.
- **Concise Topic Keywords**: Queries sent to the image search engine must be distilled into concise 2–5 word academic topic keywords (`extractConciseSearchKeyword`), permanently stripping lengthy definitions, subclauses, or descriptive sentences.
- **Search Engine First, Wikipedia Second**: Online image searches prioritize Bing Images web search engine candidates first, authoritative Wikipedia encyclopedic figures second, and Wikimedia Commons third.
- **Harmful & Political Result Blocking**: Political ballot propositions, election results, party campaigns, and watermarked stock photos are permanently filtered and blocked from educational search candidates.
- **Last Resort Fallback Only**: Live bespoke LLM SVG generation (`/api/diagram/generate`) serves strictly as a last resort when online search finds zero accessible educational diagrams or encounters a network failure, protected by a strict 15-second abort controller.

## 17. Side Book Viewer Dynamic NCERT Auto-Scroll & Synchronization
- **Direct Official NCERT PDF Streaming**: All textbook links resolve directly to official NCERT URLs (`https://ncert.nic.in/textbook/pdf/<bookcode>.pdf`) across all classes (9–12) and subjects (Maths, Science, Physics, Chemistry, Biology). This completely avoids bundling hundreds of megabytes of PDF binaries in Git or Vercel serverless functions (bypassing the 250 MB deployment limit and `.gitignore` restrictions).
- **Exact Concept-to-Page Indexing**: `src/lib/textbookPageMap.json` maps all 102+ chapters and concepts to exact PDF page numbers. When unindexed chapters are loaded, `constructNcertPdfUrl` in `src/lib/textbookResolver.ts` dynamically synthesizes canonical URLs based on class level, subject, and chapter number.
- **Synchronized Auto-Scrolling**: The side book viewer (`SideBookViewer.tsx`) automatically jumps to the exact topic page via `#page=<N>&view=FitH` when the tutor advances concepts or introduces a problem citing a textbook page.
- **Minimalist UI & Mobile Compatibility**: The viewer top bar stays strictly minimal (`[Title] [ < ] Page [ N ] / [Total] [ > ] [ExternalLink] [ ✕ ]`) with zero useless sync pills or bloat. An `ExternalLink` icon provides 1-tap full-tab access for mobile iOS Safari where cross-origin iframes may be restricted.

## 18. Mandatory Dual Visuals (Image + Video) on Every Concept & Module Start
- **Universal Dual Visual Mandate**: On Step 1 (Stage 1 Intuition) of EVERY module and EVERY single concept, the AI tutor MUST dispatch BOTH `search_and_show_image(...)` for an authentic, high-resolution scientific educational diagram AND `search_and_show_video(...)` for a real playable demonstration video.
- **Proactive Frontend Pre-fetching**: The classroom client (`ensureConceptVisualSynthesized` in `page.tsx`) automatically pre-fetches and primes both the image and the video card from `/api/diagram/search-image` and `/api/diagram/search-video`, guaranteeing that both visual modalities are ready on the board.
- **Zero Vague Search Queries**: Queries must be rich, concise academic topic descriptions (10–25 words for images, concise demonstration phrases for videos) specifying exact apparatus, anatomical structures, or phenomena.

## 19. Universal Multi-Type Graph Engine & Micro-Visual Calling Mandate
- **Seven Core Graph Modalities Supported**: The digital chalkboard graph engine (`MafsGraphCanvas.tsx`, `graphGating.ts`) supports seven distinct graphing modalities:
  1. *Function Curves*: Single and comparative curves ($y = f(x)$) for polynomials, quadratics, trigonometric functions, $s-t, v-t, a-t$ kinematics, Ohm's law ($V-I$), thermodynamics ($P-V$), and chemical kinetics, with automatic intersection detection.
  2. *Bounded Line Segments & Explicit Lengths*: Line segments (`segments`) with start and end stopping points, midpoint labels, and explicit lengths (e.g. `label: "AB = 5 cm"`).
  3. *Critical Coordinate Points*: Key coordinates (`points`) with labels, coordinates, and educational callouts (roots, intercepts, vertex, local extrema).
  4. *Statistical Bar Graphs & Histograms*: Discrete categories and frequencies or continuous class intervals (`bars`) rendered as rectangular polygons with values on top and labels below the x-axis.
  5. *Physics Vectors*: Force, velocity, displacement, and ray vectors (`vectors`) with directional arrowheads, tail coordinates, and magnitude labels.
  6. *Geometric Figures on Cartesian Plane*: Triangles, quadrilaterals, shaded regions under curves (`polygons`), and circles (`circles`) with center point marker and radius annotation.
  7. *Multiple Freeform Text Annotations*: Arbitrary text labels (`texts`) positioned at custom $(x, y)$ coordinates across the graph canvas.
- **Auto-Fitting Viewport Bounding**: `autoBounds` dynamically calculates the bounding box over all elements with a 20% margin, ensuring all figures fit without clipping.
- **Problem Solving & Micro-Visual Mandate**: The AI tutor is strictly required to call `plot_mathematical_graph` whenever a question involves coordinate geometry, plotting, solving graphically, finding intercepts, kinematics ($v-t, s-t, a-t$), Ohm's law ($V-I$), thermodynamics ($P-V$), or statistical bar graphs. Furthermore, the tutor must proactively call graphs for small visual explanations (e.g. line segment lengths, vectors, coordinates) to aid student understanding.
- **Zero Meaningless Graph Invariant**: The tutor is strictly forbidden from outputting an empty graph, placeholder `formula="x"`, or line through origin without actual points, segments, figures, or purpose.

## 20. Supabase Schema Alignment & Memory Invariant
- **Column Mapping Invariant**: The `ai_user_memories` table stores memory records using `memory_type` and `content` (with `id, user_id, importance_score, metadata, created_at`). Client queries must select `*` and fall back between `content`/`memory_text` and `memory_type`/`category` to prevent PostgREST 400 Bad Request errors.
- **Chalkboard Notes Persistence**: Master notes and whiteboard pages are saved directly to `user_progress.chapter_notes` and `visual_progress.whiteboard_pages`, serving as the single source of truth for student revision.

## 21. Strict Doubt & Re-explanation Lock & Anti-Premature Page Turn Invariant
- **Doubt & Re-explanation Lock (Zero Advancement on Doubts)**:
  * Whenever the student asks a question, raises a doubt (including typos: `douth`, `douts`, `dought`, `daoubt`, `shanka`), says they don't understand (`samajh nahi aaya`), or asks to explain the whole concept again (`explain whole concept again`, `explain again`, `dobara samjhao`, `phir se samjhao`, `pura concept samjhao`):
    1. The tutor is STRICTLY FORBIDDEN from calling `concept_completed`, `concept_done`, or creating a new page.
    2. `studentHasActiveDoubtRef.current = true`, `hasConfirmedUnderstandingRef.current = false`, `lastVerdictStatusRef.current = 'neutral'`.
    3. `handleConceptDone` strictly aborts with `PEDAGOGICAL DOUBT GUARD` if an active doubt or re-explanation request exists.
    4. The tutor MUST re-explain the concept thoroughly from the very beginning with fresh everyday intuition and write step-by-step notes on the CURRENT chalkboard page.
- **Sequential Concept Progression & Non-Zero Progress Percent Guarantee**:
  * Advancing to concept $K$ (`nextIdx`) GUARANTEES that all prior concepts (`keyConcepts.slice(0, nextIdx)`) are permanently preserved in `completedConcepts`.
  * `progressPercent` reflects true completed percentage ($> 0\%$) and previous concepts are permanently marked in the sidebar with checkmarks.
- **Dedicated 1-Concept-Per-Page Layout**:
  * Unilateral AI `new_page` actions are completely ignored by the client; the chalkboard page switches ONLY when transitioning concepts via `advanceToNextConcept` or explicit user navigation.

## 22. Animated Short Video Search & High-Precision Image Relevance Invariant
- **Animated Short Video Mandate Across All Classes & Subjects**:
  * All video search queries must explicitly request an `animated short video showing animation to understand <concept>` across all classes (6–12) and subjects (Maths, Physics, Chemistry, Biology).
  * Video search ranking prioritizes candidates matching `animat`, `3d`, `simulation`, and `how it works` in titles/descriptions.
- **High-Precision Image Relevance Gate & Scoring**:
  * `isImageRelevantToQuery` enforces a minimum 2-token match threshold for queries with $\ge 2$ substantive words, eliminating single generic word false matches.
  * `scoreEducationalImage` awards up to +80 points for exact token match ratio, +50 for Wikipedia PageImages, +30 for labeled diagrams/schematics, and penalizes generic stock/lifestyle images (-40 points).

---

# Architecture Handover Summaries (Phases 1–11)

## Phase 1 Documentation & Handover
- Refer to [PHASE_1_SUMMARY.md](file:///e:/AI_tutor/PHASE_1_SUMMARY.md) for the complete architecture breakdown, database schema, subsystem specifications, and the catalog of all bugs identified and resolved in Phase 1.

## Phase 2 Documentation & Handover
- Refer to [PHASE_2_SUMMARY.md](file:///e:/AI_tutor/PHASE_2_SUMMARY.md) for the complete breakdown of Phase 2 achievements: Sobi Companion, whiteboard text wrapping and page guard, audio streamer mic collision fix, classical cinematic landing page (video scrubber, Lenis smooth scroll, glowing typography), and Mascot hook order resolution.

## Phase 3 Documentation & Handover
- Integrated the Visual Engine, Simli WebRTC real-time avatar, student settings hub, audio accumulator buffer, and chalkboard deduplication.

## Phase 4 Documentation & Handover
- Implemented production security hardening, paper-grid onboarding, expressive Sobi avatar, Indian voice inflection, and Playwright verification suite.

## Phase 5 Documentation & Handover
- Refer to [PHASE_5_SUMMARY.md](file:///e:/AI_tutor/PHASE_5_SUMMARY.md) for the complete breakdown of Phase 5 achievements: Generative Visual Engine (`/api/diagram/generate`), Aristotle & Gauth benchmark vector SVG generators, multi-curve interactive function plotting, 20-minute capsule ingestion overhaul with 4–6 authentic board-exam questions per concept, strict Socratic progression gating, mass-market startup pricing architecture guaranteeing $\ge 75\%$ gross profit margin, standalone `/pricing` route with 4-tier model, 100% Face-to-Face AI Video Avatar for Tiers 2 & 3, complete removal of modal overlays, Hairline axonometric illustrations, and Razorpay payment gateway integration.

## Phase 6 Documentation & Handover
- Refer to [PHASE_6_SUMMARY.md](file:///e:/AI_tutor/PHASE_6_SUMMARY.md) for the complete breakdown of Phase 6 achievements: Comprehensive Class 11 Physics Part 1 (Mid-Term) and Part 2 (Final-Term) curriculum synthesis: 14 chapters, 88 modules, 432 concepts, zero omissions. Enterprise student subscriptions, entitlements, and production Razorpay integration.

## Phase 7 Documentation & Handover
- Comprehensive Class 9 Mathematics Part 2 (Final-Term) curriculum synthesis: 6 chapters (Ch 9 to 14), 33 publication-grade modules, completing the full 14-chapter Class 9 Mathematics curriculum (80 total modules).
- Exhaustive step-by-step problem-solving for all textbook exercises, worked examples, and activities with zero omissions.
- Secondary & Senior Secondary Multi-Term Syllabus Architecture (Classes 9–12) codified in `.agents/rules/pedagogical_and_architecture_rules.md`.
- Dynamic Search Engine First visual cues for concepts; authentic book diagrams bound exclusively to question problems citing figures (66 diagrams bound across 36 modules).
- Pure mathematical typography enforced across all modules (zero raw programming operators `*`, `**`, `//`, `^`).

## Phase 8 Documentation & Handover
- Search-Engine-First visual retrieval pipeline permanently integrated into classroom live directives (`render_svg_diagram`, `draw_diagram`, `draw_image`, and graph gating fallbacks).
- Ranking algorithm updated: Search Engine (Bing Images) prioritized FIRST, Wikipedia PageImages SECOND, Wikimedia Commons THIRD.
- Political ballot propositions, election results, and non-educational matches permanently filtered and blocked.
- Dynamic query extraction (`extractConciseSearchKeyword`) distillations prevent sentence-length search misses.
- Live LLM SVG generator (`/api/diagram/generate`) strictly gated as last-resort fallback with 15-second abort controller.

## Phase 9 Documentation & Handover
- Refer to [PHASE_9_SUMMARY.md](file:///e:/AI_tutor/PHASE_9_SUMMARY.md) for the complete breakdown of Phase 9 achievements:
  - **Side Book Viewer Chapter Sync & Auto-Scroll Engine**: Integrated `SideBookViewer.tsx` inside `WhiteboardWorkspace.tsx` to automatically display and scroll the authentic textbook chapter PDF to the exact page matching the concept or problem being taught.
  - **Official NCERT PDF Dynamic Resolution Architecture**:
    * Migrated all 102 indexed chapters in `textbookPageMap.json` to stream authentic official NCERT PDFs (`https://ncert.nic.in/textbook/pdf/<filename>.pdf`), bypassing Vercel 404s and the 250 MB serverless deployment limits.
    * Implemented `constructNcertPdfUrl()` and `toNcertPdfUrl()` in `textbookResolver.ts` supporting all classes (9–12) and subjects (Maths, Science, Physics, Chemistry, Biology) with automatic fallback for unindexed chapters.
    * Clean filename matching in `textbookRegistry.ts` (`getChapterByPdf`).
    * Minimalist top bar with discrete 1-tap external viewer link for mobile iOS Safari.
  - **Supabase Memory Schema Alignment**: Resolved PostgREST 400 Bad Request error by aligning queries to `ai_user_memories` columns (`memory_type` and `content`).

## Phase 10 Documentation & Handover
- Refer to [PHASE_10_SUMMARY.md](file:///e:/AI_tutor/PHASE_10_SUMMARY.md) for the complete breakdown of Phase 10 achievements:
  - **Mandatory Dual Visuals (Image + Video) on Every Concept & Module Start**:
    * Live directives mandate calling BOTH `search_and_show_image` AND `search_and_show_video` on turn 1 of every module and concept.
    * Client-side pre-fetching automatically primes both cards from `/api/diagram/search-image` and `/api/diagram/search-video`.
  - **Universal Multi-Type Graph Engine**:
    * Expanded `MafsGraphCanvas.tsx` and `graphGating.ts` to support seven distinct graphing modalities:
      1. Single and comparative functions ($y = f(x)$) with automatic intersection finding
      2. Bounded line segments with explicit stopping points and defined lengths
      3. Critical coordinate points with labels and callouts
      4. Statistical bar graphs and histograms (`bars`) with values on top and labels below
      5. Physics vectors (`vectors`) with directional arrowheads, tail coordinates, and magnitude labels
      6. Geometric figures on Cartesian space (triangles, quadrilaterals via `polygons`, circles via `circles`)
      7. Multiple freeform text annotations placed anywhere on the graph (`texts`)
    * Dynamic `autoBounds` automatically calculates domain and range to prevent visual clipping.
    * Props spread (`{...activeGraph}`) across docked, floating, and maximized display modes in `WhiteboardWorkspace.tsx`.
  - **Micro-Visual & Question Solving Graph Mandate**:
    * Instructed AI tutor to call `plot_mathematical_graph` whenever solving graph questions or whenever even a small visual line, vector, coordinate, or figure helps explain a concept.

## Phase 11 Documentation & Handover
- Refer to [PHASE_11_SUMMARY.md](file:///e:/AI_tutor/PHASE_11_SUMMARY.md) for the complete breakdown of Phase 11 achievements:
  - **Pedagogical Doubt & Re-explanation Lock (Zero Premature Advancement on Doubts)**:
    * Synchronous doubt tracking via `studentHasActiveDoubtRef` immediately halts any concept completion when the student asks a question, raises a doubt (including common typos like `douth`), expresses confusion, or requests to explain the concept again (`explain whole concept again`, `dobara samjhao`, `phir se samjhao`).
    * Active doubt guard in `handleConceptDone` blocks calls and directs the tutor to remain on the current chalkboard page and re-explain thoroughly.
    * Gated `isConfirmationOrNextIntent` to immediately return `false` whenever any question or doubt token is present.
  - **Sequential Concept Progression & Non-Zero Progress Percent Guarantee**:
    * `advanceToNextConcept` permanently merges all concepts prior to `nextIdx` (`keyConcepts.slice(0, nextIdx)`) into `completedConcepts`.
    * Ensures `progressPercent` reflects true completed percentage ($> 0\%$) and previous concepts are properly marked in the sidebar with checkmarks.
    * Unilateral AI `new_page` actions in `write_chalkboard` are removed from the tool schema and safely ignored in the client, preserving the 1-concept-per-page vertically scrollable chalkboard layout.
  - **Animated Short Video Mandate Across All Classes & Subjects**:
    * `search_and_show_video` prompts and tool declarations mandate queries explicitly requesting `animated short video showing animation to understand <concept>`.
    * Online video search pipeline (`/api/diagram/search-video`) sorts and prioritizes videos with `animat`, `3d`, `simulation`, and `how it works`.
  - **High-Precision Image Relevance Gate & Scoring**:
    * `isImageRelevantToQuery` enforces a minimum 2-token match threshold for multi-word queries.
    * Upgraded `scoreEducationalImage` awards up to +80 points for exact query token match ratio, +50 for Wikipedia PageImages, +30 for labeled diagram keywords, and penalizes generic stock/lifestyle images (-40 points).

