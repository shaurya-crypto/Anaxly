# AI Tutor Pedagogical, Scope & Security Invariants

## 1. Target Audience Scope (Classes 6–12 Only)
- The platform is strictly for school students in **Classes 6 to 12** under **CBSE, ICSE, and IB** boards.
- Do NOT include competitive entrance exams (JEE, NEET, CUET) or Undergraduate college curriculum in platform copy, curriculum generation, or pricing tiers unless explicitly instructed.

## 2. Socratic Exam-Topper Teaching Cadence
Whenever designing, prompting, or updating the AI tutor voice instruction:
- **Never lecture continuously**: The tutor must never speak more than 2–3 sentences without engaging the student or checking understanding.
- **Strict 6-Stage Cadence**:
  1. *Real-Life Intuition*: Everyday physical hook/analogy.
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

## 11. Senior Secondary & Multi-Term Syllabus Architecture (Classes 11 & 12)
- **Mid-Term & Final-Term Partitioning**: Every subject curriculum must partition chapters according to the official board syllabus into **Mid-Term** (Part 1 textbook) and **Final-Term / Annual Exam** (Part 2 textbook). Every module must clearly carry its syllabus term tag (`Mid-Term` vs. `Final-Term`).
- **No Artificial Module Length Limits**: Module content must scale to full textbook chapter depth. Senior secondary modules (Classes 11–12) require rigorous physical intuition, formal mathematical derivations with calculus, physical mechanisms, boundary conditions, and engineering applications.
- **Exact Textbook Topic Headings**: Every module must preserve the verbatim topic titles, section numbers, theorems, lab experiments, and worked examples from the standard textbook with zero omissions.

## 12. Dynamic Live Visuals & Content Safety Invariant
- **Zero Static Hardcoded Image URLs**: Modules must NEVER store hardcoded or brittle external image links in database tables or module JSONs. 
- **Search Engine First**: Visual search must query Search Engines (Bing Images with strict SafeSearch) FIRST for exact topic diagrams, Wikipedia PageImages SECOND for authoritative encyclopedic figures, and Wikimedia Commons THIRD.
- **Strict Content Safety Filter**: Every visual query must pass through `isSafeEducationalImage` and `isSafeEducationalVideo` filters with strict SafeSearch (`&adlt=strict` / SafeSearch=Strict) to permanently block adult, violent, harmful, or non-educational content.
- **YouTube Classroom Video Demonstrations**: Scientific videos must play seamlessly inside the whiteboard modal via responsive, secure YouTube embedded iframes (`video/youtube`), with native HTML5 fallback for direct media streams.

## 13. Socratic Cadence Gating & Anti-Premature Page Turn Guard
- **No Premature Page Flips on Affirmations**: Casual conversational affirmations (`"yes"`, `"ok"`, `"haan"`, `"sure"`, `"understood"`) in voice or text MUST NEVER advance the concept or turn the chalkboard page.
- **Strict Stage 1–4 Lock**: The AI tutor is strictly forbidden from calling `concept_completed` or `concept_done` during Stages 1 to 4 (Intuition, Formulation, Worked Application, Board Numerical). When the student affirms understanding during initial stages, the tutor must simply continue to the next stage of the same concept.
- **Advancement Exclusively on Stage 6 or Explicit Command**: The chalkboard page advances ONLY after the student attempts and resolves the Stage 5/6 checkpoint question, OR if the student explicitly commands advancement (`"next concept"`, `"next page"`, `"move to next concept"`, `"aage badho"`).

## 14. Pure Chalkboard Mathematical Typography
- **Zero Raw Programming Operators**: The chalkboard must NEVER render raw code syntax: no raw asterisks (`*`, `**`, `***`), no raw carets (`^`), and no raw double slashes (`//`).
- **Authentic Unicode Mathematics**: All mathematical expressions must format as standard textbook mathematics with superscripts ($x², v², 10⁻¹¹$), subscripts ($v₀, F_{\text{net}}$), Greek letters ($\theta, \alpha, \beta, \gamma, \Delta, \lambda, \mu, \pi, \rho, \sigma, \tau, \omega, \Omega$), calculus symbols ($\int, \iint, \oint, \sum, \prod, \partial, \nabla$), and standard arithmetic operators ($\times, \cdot, \div, \pm, \le, \ge, \ne, \approx, \to, \Rightarrow, \rightleftharpoons$).
