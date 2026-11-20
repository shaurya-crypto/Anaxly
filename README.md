# Anaxly: 1-on-1 Socratic AI Classroom & Chalkboard Engine

[![Next.js 14](https://img.shields.io/badge/Next.js-14.2-black?logo=next.js)](https://nextjs.org/)
[![Google Gemini Live API](https://img.shields.io/badge/Google_Gemini-3.8_Live-4285F4?logo=google)](https://ai.google.dev/)
[![Mafs Vector Math](https://img.shields.io/badge/Mafs-Pure_React_Vector_SVG-6366F1)](https://mafs.dev/)
[![Supabase](https://img.shields.io/badge/Supabase-Auth_%26_Postgres-3ECF8E?logo=supabase)](https://supabase.com/)
[![Razorpay](https://img.shields.io/badge/Razorpay-Production_Billing-0C2340?logo=razorpay)](https://razorpay.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?logo=typescript)](https://www.typescriptlang.org/)

**Anaxly** is a production-grade 1-on-1 Socratic AI classroom platform designed exclusively for school students in **Classes 6 to 12** under **CBSE, ICSE, and IB** boards. Powered by the **Google Gemini Multimodal Live API** (`models/gemini-3.8-live`), Anaxly couples sub-second, full-duplex conversational voice tutoring with an interactive digital chalkboard, dynamic official NCERT textbook synchronization, an authentic 7-modality Cartesian vector graphing engine, and search-engine-first dual visual aids.

---

## 🌟 Architectural Pillars & Core Capabilities

### 1. Real-Time Socratic Voice Engine with Instant Barge-In
- **Native Full-Duplex WebSockets**: Persistent bidirectional connection to Google Gemini Live API via `BidiGenerateContent`.
- **Acoustic Streaming Pipeline**: Captures student microphone input, downsamples to 16kHz 16-bit Mono Linear PCM, and streams to Gemini. Audio responses are received as 24kHz PCM chunks played gaplessly via Web Audio API.
- **Sub-Second Barge-In Interruption**: The instant the student speaks, interrupts, or asks a doubt, Gemini detects speech energy (`interrupted: true`), immediately terminating client-side audio buffers and yielding the floor to the student.
- **Strict 6-Stage Exam-Topper Cadence**:
  1. *Real-Life Intuition*: 5–6 complete sentences delivering everyday physical analogies and mental hooks.
  2. *Concept Formulation*: Precise scientific definitions, laws, and standard SI units.
  3. *Worked Application*: Concrete illustration addressing common student pitfalls.
  4. *Board Numerical*: Step-by-step topper layout on the chalkboard (`Given -> Formula -> Substitution -> Calculation -> Boxed Answer`).
  5. *Understanding Check*: Verifies understanding; co-solves with visual breakdown if hesitant.
  6. *Authentic Board-Exam Numerical*: Poses genuine board-level questions matching the student's exact board pattern (CBSE/ICSE/IB).
- **Anti-Premature Page Turn Guard**: Casual affirmations (`"yes"`, `"ok"`, `"understood"`) are strictly locked from advancing the concept; progression occurs exclusively upon resolving Stage 6 checkpoint questions or explicit verbal commands (`"next concept"`).

### 2. Live Digital Chalkboard (Single Source of Truth)
- **Zero Post-Class LLM API Waste**: The tutor writes topper-ready structured notes, steps, and rough calculations directly to the chalkboard during class via tool directives (`write_chalkboard`). These notes are saved directly as the student's final Master Revision Notes (`user_progress.chapter_notes`).
- **Pure Unicode Mathematical Typography**: Zero raw code syntax (no raw asterisks `*`, carets `^`, or double slashes `//`). Formats as authentic textbook mathematics with superscripts ($x², 10⁻¹¹$), subscripts ($v₀, F_{\text{net}}$), Greek letters ($\theta, \alpha, \lambda, \Omega$), calculus operators ($\int, \sum$), and standard arithmetic operators ($\times, \div, \pm, \approx, \le, \ge$).
- **Universal Topic-Adaptive Flowcharts**: Multi-row wrapping, branching decision trees (`A -> B | C`), and cyclical biological/chemical loops (`cycle: Step 1 -> Step 2 -> Step 3 -> Step 1`).

### 3. Universal 7-Modality Cartesian Graph Engine (Mafs.dev)
- **Zero Meaningless / Fake Lines**: Eliminates placeholder diagonal lines passing through the origin. Every graph is constructed with explicit coordinates, parameters, and educational purpose.
- **Seven Core Graph Modalities**:
  1. *Function Curves*: Single and comparative functions ($y = f(x)$) with automatic intersection finding (polynomials, quadratics, $s-t, v-t, a-t$ kinematics, Ohm's law $V-I$, thermodynamics $P-V$).
  2. *Bounded Line Segments & Explicit Lengths*: Segments (`segments`) with start and end stopping points, midpoint labels, and explicit lengths (e.g. `AB = 5 cm`).
  3. *Critical Coordinate Points*: Marked coordinates (`points`) with labels, roots, vertices, and pedagogical callouts.
  4. *Statistical Bar Graphs & Histograms*: Discrete categories and continuous class frequency intervals (`bars`) rendered as rectangular polygons with values stamped on top and labels below the x-axis.
  5. *Physics Vectors*: 2D force, velocity, displacement, and ray vectors (`vectors`) with directional arrowheads, tail markers, and magnitude/angle labels.
  6. *Geometric Figures on Coordinate Plane*: Triangles, quadrilaterals, shaded areas (`polygons`), and coordinate circles (`circles`) with center point marker and radius annotation.
  7. *Multiple Coordinate Text Annotations*: Arbitrary pedagogical callouts (`texts`) placed at custom $(x, y)$ coordinates.
- **Dynamic AutoBounds**: Automatically calculates the bounding box over all elements with a 20% margin to prevent visual clipping.
- **Micro-Visual & Question Solving Mandate**: The tutor proactively summons graphs whenever solving textbook numericals or providing small visual intuitions (e.g. line lengths, vector directions, coordinates).

### 4. Search-Engine-First Dual Visual Engine
- **Turn 1 Mandatory Dual Visual Pair**: On Step 1 (Intuition) of every module and concept, the AI tutor dispatches BOTH `search_and_show_image` for an authoritative diagram AND `search_and_show_video` for a real demonstration video.
- **Proactive Frontend Pre-fetching**: The classroom client (`ensureConceptVisualSynthesized`) pre-fetches and primes both visual cards before speech commences.
- **Strict SafeSearch & Quality Guard**:
  * Bing Images web search engine runs FIRST with `&adlt=strict` (SafeSearch=Strict).
  * Wikipedia PageImages runs SECOND for encyclopedic accuracy.
  * Wikimedia Commons runs THIRD.
  * Political elections, ballot campaigns, watermarked stock photos, and non-educational images are permanently filtered.
- **YouTube Classroom Player**: Educational demonstration videos stream directly inside the chalkboard interface via responsive `video/youtube` iframe players.
- **Last-Resort Bespoke LLM Fallback**: If zero online candidates exist, `/api/diagram/generate` provides vector SVG diagrams protected by a strict 15-second abort controller.

### 5. Synchronized Side Book Viewer (Official NCERT Streaming)
- **Direct Official NCERT Streaming**: Textbook links stream directly from official NCERT servers (`https://ncert.nic.in/textbook/pdf/<filename>.pdf`), completely bypassing Vercel's 250 MB serverless deployment limits and eliminating local binary storage in Git.
- **Dynamic Canonical URL Resolver (`textbookResolver.ts`)**: Resolves official NCERT book codes across Classes 9–12 for Mathematics, Science, Physics, Chemistry, and Biology (e.g. `iemh101` for Class 9 Maths Ch 1, `keph103` for Class 11 Physics Ch 3).
- **Synchronized Auto-Scrolling**: Embedded alongside the chalkboard; automatically jumps to the exact topic page using `#page=<N>&view=FitH` when the tutor advances concepts or introduces textbook problems.
- **Mobile Safari Compatibility**: Minimalist top bar includes a discrete 1-tap external viewer link (`ExternalLink`) opening the exact official NCERT page in a native PDF view for mobile devices.

### 6. Classroom Avatars & Expressive Presence
- **Circular Audio-Reactive Avatar**: Minimalist top avatar with live audio-reactive pulse rings reflecting volume and speaking state.
- **Sobi Mascot Companion**: Interactive companion character with animated expressions and mood states.
- **Simli WebRTC Photorealistic Video Avatar**: Real-time face-to-face video avatar streaming for Topper and Mastery subscription tiers.

### 7. Multi-Board Curriculum Synthesis (Zero Omissions)
- **CBSE, ICSE, and IB Standards**: Strict alignment with NCERT, Selina Concise, Morning Star, and Cambridge IB curricula.
- **Exhaustive Problem Coverage**: Zero omissions. Every single textbook exercise question (all parts), worked example, and "Think and Reflect" problem is captured and solved step-by-step.
- **Multi-Term Partitioning**: Structured into Mid-Term and Final-Term syllabi across Classes 9–12.

### 8. Enterprise Subscriptions & Production Security
- **4-Tier Pricing Model**: Free, Scholar, Topper, and Mastery tiers engineered to guarantee $\ge 75\%$ gross profit margin.
- **Production Razorpay Integration**: Zero key leakage architecture with server-side HMAC-SHA256 signature verification and automated entitlement provisioning.
- **Supabase Memory Schema Alignment**: Resilient student profile and memory retrieval (`ai_user_memories`) syncing mastery across sessions.

---

## 📁 Repository Architecture & Directory Map

```
AI_tutor/
├── .agents/
│   └── rules/
│       └── pedagogical_and_architecture_rules.md  # Definitive 20 Architecture Invariants
├── public/
│   ├── extracted_diagrams/                        # High-resolution textbook PDF diagrams for questions
│   └── icons/                                     # UI icons and visual assets
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   ├── class/                             # Classroom session & note endpoints
│   │   │   ├── diagram/
│   │   │   │   ├── generate/                      # Bespoke LLM SVG generator (last-resort fallback)
│   │   │   │   ├── search-image/                  # Bing & Wikipedia SafeSearch image search engine
│   │   │   │   └── search-video/                  # Educational demonstration video resolver
│   │   │   ├── razorpay/                          # Razorpay order creation & webhook verification
│   │   │   └── session/                           # Gemini Live session & token configuration
│   │   ├── dashboard/[id]/
│   │   │   ├── class/[moduleId]/                  # Master 1-on-1 Live Classroom Workspace
│   │   │   └── page.tsx                           # Student dashboard, syllabus browser, progress
│   │   ├── pricing/                               # 4-tier subscription billing page
│   │   ├── globals.css                            # Apple/Linear dark canvas, typography, tokens
│   │   └── layout.tsx                             # Root layout, analytics, fonts
│   ├── components/
│   │   ├── classroom/                             # Classroom controls, speech meters, transcripts
│   │   ├── whiteboard/
│   │   │   ├── MafsGraphCanvas.tsx                # Universal 7-modality Cartesian vector graph engine
│   │   │   ├── SideBookViewer.tsx                 # Official NCERT textbook sync & auto-scroll viewer
│   │   │   ├── WhiteboardWorkspace.tsx            # Master chalkboard coordinator (canvas, split view)
│   │   │   └── SVGViewerModal.tsx                 # Modal diagram & YouTube demonstration player
│   │   ├── avatar/                                # Audio-reactive Teacher Avatar & Simli WebRTC
│   │   └── navigation/                            # Top bars, breadcrumbs, modals
│   ├── hooks/
│   │   ├── useGeminiLive.ts                       # Master hook managing WebSocket, audio, barge-in
│   │   └── useRazorpayCheckout.ts                 # Razorpay payment checkout hook
│   ├── lib/
│   │   ├── chalkboardTypography.ts                # Pure Unicode mathematical typography engine
│   │   ├── graphGating.ts                         # Graph payload validation, parsing, and topic gating
│   │   ├── searchSafeEducationalImage.ts          # SafeSearch image search pipeline
│   │   ├── searchSafeEducationalVideo.ts          # YouTube classroom video search pipeline
│   │   ├── textbookRegistry.ts                    # Chapter registry & metadata
│   │   ├── textbookResolver.ts                    # Dynamic official NCERT PDF URL synthesis
│   │   ├── textbookPageMap.json                   # 102-chapter concept-to-page indexing
│   │   └── supabaseClient.ts                      # Supabase client singleton
│   ├── services/
│   │   ├── audioPlayer.ts                         # 24kHz PCM gapless streaming player with barge-in reset
│   │   ├── audioStreamer.ts                       # Microphone capture & 16kHz PCM downsampler
│   │   └── geminiWebSocket.ts                     # Gemini Live WebSocket protocol client & tools
│   ├── tests/
│   │   ├── enhancedGraphUIAndGatingVerification.ts # 46-point graph UI & gating test suite
│   │   └── multiTypeGraphAndDualVisualVerification.ts # 24-point multi-modality & dual visual test suite
│   └── types/
│       ├── chalkboard.ts                          # Whiteboard actions, cards, and graph contracts
│       └── liveSession.ts                         # Live session state contracts
├── AGENTS.md                                      # Developer & AI Agent Invariants and Phase Handovers
├── GRAPH_DIAGRAM_SPEC.md                          # Version 2.0 Graph & Diagram Specification
├── PHASE_1_SUMMARY.md                             # Phase 1 Handover: Foundation & WebSockets
├── PHASE_2_SUMMARY.md                             # Phase 2 Handover: Sobi, Chalkboard Wrap & Landing
├── PHASE_5_SUMMARY.md                             # Phase 5 Handover: Aristotle Benchmark & Pricing
├── PHASE_6_SUMMARY.md                             # Phase 6 Handover: Razorpay & Class 11 Physics
├── PHASE_9_SUMMARY.md                             # Phase 9 Handover: NCERT Sync & Side Book Viewer
├── PHASE_10_SUMMARY.md                            # Phase 10 Handover: Multi-Type Graphs & Dual Visuals
└── package.json
```

---

## 🚀 Getting Started & Local Development

### 1. Prerequisites
- **Node.js**: v18.0.0 or later (tested on Node v20+ and v24+)
- **npm**: v9.0.0 or later
- **Modern Browser**: Chromium (Google Chrome, Microsoft Edge, Brave) or Firefox with microphone permissions.

### 2. Environment Setup
Create a `.env.local` file at the root of the project:
```bash
cp .env.example .env.local
```

Configure your environment variables:
```env
# Google Gemini API
GEMINI_API_KEY=your_gemini_api_key_here
NEXT_PUBLIC_GEMINI_MODEL=models/gemini-3.8-live

# Supabase
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key_here
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key_here

# Razorpay (Leave dummy values for test mode)
NEXT_PUBLIC_RAZORPAY_KEY_ID=rzp_test_your_key_id
RAZORPAY_KEY_SECRET=your_key_secret

# Visual Search (Optional: falls back to Wikipedia & direct video search)
BING_SEARCH_API_KEY=your_bing_search_api_key_here
```

### 3. Install Dependencies
```bash
npm install
```

### 4. Run Development Server
```bash
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

### 5. Production Build
```bash
npm run build
npm run start
```

---

## 🧪 Verification & Testing Suite

Run type checking:
```bash
npx tsc --noEmit
```

Run automated verification scripts:
```bash
# Verify Enhanced Graph UI & Topic Gating (46 tests)
npx tsx src/tests/enhancedGraphUIAndGatingVerification.ts

# Verify Multi-Type Graph Modalities & Mandatory Dual Visuals (24 tests)
npx tsx src/tests/multiTypeGraphAndDualVisualVerification.ts
```

---

## 📋 The 20 Core Invariants Summary

Every AI agent, developer, and automated pipeline operating in this repository must strictly adhere to the 20 Invariants defined in [`.agents/rules/pedagogical_and_architecture_rules.md`](file:///e:/AI_tutor/.agents/rules/pedagogical_and_architecture_rules.md):

1. **Target Audience Scope**: Classes 6–12 only under CBSE, ICSE, and IB. No competitive exams or college curricula.
2. **Socratic Exam-Topper Cadence**: 5–6 sentence explanations, followed by a checkpoint question. Immediate stop on student interruption.
3. **Whiteboard is Single Source of Truth**: Live chalkboard tool notes are saved as final master notes. No post-class LLM optimization.
4. **Pinned Identity Context Guard**: Student identity and curriculum context are permanently pinned in system instructions.
5. **Zero Key Leakage Invariant**: Never leak raw API keys to browser JSON or HTML.
6. **Multi-Board Standards**: Board-specific derivations, definitions, and formatting for CBSE, ICSE, and IB.
7. **Zero Hardcoded Fake Diagrams**: All quantitative and geometric plots must be drawn dynamically using Mafs.dev vector math.
8. **Universal Topic-Adaptive Flowcharts**: Multi-row wrapping, branching decision trees, and cyclical loops.
9. **Lean Tool Calling**: At most 12 distinct canonical actions; zero duplicate aliases.
10. **Exhaustive Module Decomposition**: 5–8 modules per chapter; 100% textbook questions and worked examples solved.
11. **Multi-Term Syllabus Partitioning**: Mid-Term vs Final-Term separation for Classes 9–12.
12. **Dynamic Live Visuals & Book Figures**: Search engine first for concepts; authentic book diagrams bound exclusively to figure questions.
13. **Anti-Premature Page Turn Guard**: Affirmations never flip pages; advancement occurs strictly on Stage 6 mastery or explicit student command.
14. **Pure Mathematical Typography**: Zero raw code syntax (`*`, `^`, `//`); authentic Unicode superscripts, subscripts, and Greek symbols.
15. **Topper Problem Layout**: Given -> To Prove -> Formula -> Construction -> Proof -> Rough Work -> Boxed Answer.
16. **Search-Engine-First Visual Execution**: Bing Images SafeSearch=Strict first, Wikipedia second, LLM SVG strictly as last-resort fallback.
17. **Side Book Viewer NCERT Sync**: Stream official NCERT PDFs directly, dynamic `#page=N&view=FitH` auto-scroll, 1-tap mobile popout.
18. **Mandatory Dual Visuals**: Turn 1 of every module and concept dispatches both `search_and_show_image` and `search_and_show_video`.
19. **Universal Multi-Type Graph Engine**: Seven coordinate modalities, dynamic autoBounds, proactive micro-visual calling.
20. **Supabase Schema Alignment & Memory**: Canonical column mapping (`memory_type` and `content`), persistent notes in `user_progress`.

---

## 📜 Documentation Index
- [AGENTS.md](file:///e:/AI_tutor/AGENTS.md): Complete architecture handovers (Phases 1–10) and agent guidelines.
- [GRAPH_DIAGRAM_SPEC.md](file:///e:/AI_tutor/GRAPH_DIAGRAM_SPEC.md): Version 2.0 Graph & Diagram Specification.
- [FUTURE_PLANS.md](file:///e:/AI_tutor/FUTURE_PLANS.md): Strategic roadmap (parent voice cloning, code sandboxes, robotics).
- [PHASE_1_SUMMARY.md](file:///e:/AI_tutor/PHASE_1_SUMMARY.md) to [PHASE_10_SUMMARY.md](file:///e:/AI_tutor/PHASE_10_SUMMARY.md): Phase handovers.

---
*Anaxly AI Tutor • Engineering & Pedagogical Excellence for School Education.*
