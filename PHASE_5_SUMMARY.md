# Phase 5 Architecture & Handover Specification
## Generative Visual Engine, 20-Minute Exam-Topper Capsule Ingestion & Socratic Progression Gating

---

## 1. Executive Summary & Milestone Sign-Off
- **Milestone Identification**: **Phase 5** (Verified via Git history: Phase 1 & 2 signed off; Phase 3 Visual Engine merged in commit `80355ea`; Phase 4 Onboarding & Security Hardening signed off in commit `77bbf99`).
- **Core Objective**: Elevate chalkboard vector visuals to the **Aristotle & Gauth Benchmark Standard**, overhaul capsule ingestion into **super-detailed 20-minute masterclasses** with **4 to 6 authentic board-exam questions per concept**, implement **strict Socratic progression gating**, and enable **multi-curve interactive function plotting** without canned or hardcoded shortcuts.

---

## 2. Root Cause Analysis of Previous Rendering & Ingestion Issues

| Symptom / Defect | Exact Code Location | Root Cause | Phase 5 Resolution |
| :--- | :--- | :--- | :--- |
| **"Single Visual Hijack"** across entire module | `src/app/dashboard/[id]/class/[moduleId]/page.tsx` (L2228-L2235) | If `conceptVisuals.length === 1`, any diagram tool call for *any* concept in that module was hijacked by that single visual. | Removed length check. Implemented concept-specific index matching (`currentConceptIndexRef.current`) and query matching. |
| **Optics Lens Rendered for Kinematics** | `src/services/universalScientificSvg.ts` (L770-L835) | Keyword matching previously matched "point" to optics ray tracing when teaching "Position and Reference Point". | Re-routed "position", "reference point", "displacement", "1d motion" strictly to `generateDynamic1DMotionSvg`. |
| **Crude 4-Bar Stripes & Flat Ellipses for Biology** | Live WebSocket Inline Generation & Chalkboard Fallback | Gemini Live WebSocket has strict latency and token limits for audio; lacked biology vector generators in `universalScientificSvg.ts`. | Added `generateDynamicPlantCellWallSvg` (layered microfibrils, lamella, phospholipid bilayer) and `generateDynamicCellStructureSvg`, plus on-demand `/api/diagram/generate`. |
| **Bypassed Visual Plan on Chalkboard Directives** | `src/components/whiteboard/GreenChalkboard.tsx` (L3793) | Directive `[DIAGRAM: ...]` was called with empty SVG string, bypassing pre-rendered capsule SVGs. | Unified all diagram directives (`draw_diagram`, `render_svg_diagram`, `draw_image`) through a single resolver. |
| **15-Min Truncated Capsules without Exam Questions** | `src/app/api/curriculum/ingest/route.ts` | Modules defaulted to `estimated_minutes: 15` with single-question examples and no concept-level question arrays. | Updated duration to `estimated_minutes: 20`, added 4–6 authentic exam questions per concept, and indexed all textbook exercises. |

---

## 3. Subsystem Architecture

### A. Dedicated On-Demand Generative Diagram API (`/api/diagram/generate`)
- **Engine**: Powered by `gemini-2.5-flash` with a specialized textbook vector illustrator system instruction.
- **Specifications**:
  - ViewBox `0 0 540 280` with dark scholastic chalkboard backdrop (`#13211B`, `#0F1A15`, `#233930`).
  - Strict palette: Ice Blue (`#7EC8E3`), Royal Blue (`#4A90E2`), Sage Green (`#68B084`), Warm Amber (`#FBBF24`), Coral Red (`#F87171`), Crisp White (`#FFFFFF`).
  - Informational density: Labeled callouts with circular pins, measurement units, coordinate scales, and force/ray vectors.
  - Zero fake corporate blueprint cards (`"CONCEPTUAL BLUEPRINT"`, `"ANAXLY VECTOR ENGINE"`).
  - In-memory LRU caching to eliminate token waste on repeated views.

### B. High-Fidelity Deterministic Vector Generators (`universalScientificSvg.ts`)
- **`generateDynamicPlantCellWallSvg`**:
  - Middle Lamella with calcium/magnesium pectate matrix.
  - Primary Cell Wall with interwoven criss-cross cellulose microfibrils.
  - Secondary Cell Wall with S1, S2, S3 dense lamellae and angle patterns.
  - Plasma Membrane phospholipid bilayer with polar hydrophilic heads, hydrophobic tails, and transmembrane transport channel.
  - Plasmodesmata intercellular cytoplasmic channel with callout leader lines.
- **`generateDynamicCellStructureSvg`**:
  - Eukaryotic compartmentalized cytoplasm, double nuclear envelope with pores, dark nucleolus, and chromatin network.
  - Mitochondria with folded cristae labyrinth, chloroplasts with stacked grana discs, central vacuole with tonoplast, and endoplasmic reticulum.
- **`generateDynamic1DMotionSvg`**:
  - Horizontal coordinate axis with origin O(0m), positions A and B, forward dashed vector, return vector, and net displacement vector banner.

### C. Multi-Curve Graphing Canvas (`MafsGraphCanvas.tsx`)
- Supports simultaneous multi-function plotting (e.g. `2x + 1; x^2; 2`) separated by semicolon, pipe, or newline.
- Plots distinct curve colors (Ice Blue `#7EC8E3`, Coral `#E87D65`, Sage `#68B084`, Amber `#F3B455`).
- Footer bar with colored curve legend indicators and coordinate bounds matching Aristotle and Desmos standards.
- Moveable floating window, right-docked pane, or maximized full-board viewports.

### D. 20-Minute Capsule Ingestion Pipeline (`curriculum/ingest/route.ts`)
- **Duration**: `estimated_minutes: 20` across all database records and visual lesson plans.
- **4 to 6 Exam Questions per Concept**:
  - 1-mark MCQ (concept recognition)
  - 2-mark Short Answer (verbatim definition, SI unit, or assertion-reason)
  - 3-mark Conceptual / Derivation / Short Numerical
  - 5-mark Structured Board Question / Numerical with step-by-step scratchpad
  - Board Exam Past Year Question (PYQ)
  - NEP 2020 Competency-Based Real-World Application
- **Mathematics Specialization**:
  - All textbook exercises (e.g. Exercise 1.1, Exercise 1.2) fully indexed.
  - Line-by-line step-by-step scratchpad calculations (Given -> Formula -> Substitution -> Calculation -> Boxed Answer).

### E. Socratic Progression Gating & Live Session Cadence (`page.tsx`)
- **Max 2–3 Sentences per Spoken Turn**: Anti-teleprompter rule prevents continuous lecturing.
- **Strict Progression Gating**:
  - After each concept, tutor poses at least one prepared exam question from the concept's micro-dossier using `write_chalkboard(action="draw_question", content="Q: ...")`.
  - **Hard Stop**: Tutor stops speaking and strictly waits for the student's answer or question.
  - Advance to next concept is blocked until the student attempts or asks for the solution.
  - Writes `[STUDENT_ANSWER]` and `[VERDICT]` to chalkboard before co-solving and asking confirmation to advance.

---

## 4. Verification & Compilation Sign-Off
- `npx tsc --noEmit`: Clean compilation across all modified files.
- `npm run build`: Production build verified with zero errors.
- Zero raw API key exposure invariant strictly maintained.
- Classes 6 to 12 target audience scope strictly preserved.
