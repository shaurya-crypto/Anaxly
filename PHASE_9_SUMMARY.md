# Phase 9: Side Book Viewer Dynamic NCERT Synchronization & PDF Streaming Architecture

## 1. Executive Summary
Phase 9 eliminates PDF delivery failures (such as Vercel 404s and the 250 MB serverless deployment file-size limits) by transitioning the entire platform to stream authentic, official **National Council of Educational Research and Training (NCERT)** textbook PDFs directly from the official NCERT digital repository (`https://ncert.nic.in/textbook/pdf/<filename>.pdf`).

In tandem with this migration, Phase 9 delivers the **Synchronized Side Book Viewer**, an integrated textbook reader embedded inside the digital chalkboard workspace that automatically jumps and auto-scrolls to the exact page of the textbook matching the concept or problem currently being taught by the AI tutor.

---

## 2. Root Problems Diagnosed & Solved

### 2.1 The Vercel 404 & 250 MB Deployment Limit
- **Previous Failure**: Attempting to host complete textbook PDFs locally under `public/<class>/<subject>/...` caused deployment failures on Vercel due to serverless bundle size ceilings (250 MB limit). Files were missing or 404ing in production.
- **Root Cause**: Storing hundreds of high-resolution school textbook PDF binaries in Git or static Next.js assets is unscalable and violates deployment best practices.
- **Resolution**: Implemented dynamic streaming from official NCERT URLs (`https://ncert.nic.in/textbook/pdf/<bookcode><chapternum>.pdf`).

### 2.2 The Supabase Memory 400 Bad Request
- **Previous Failure**: The dashboard client received a `400 Bad Request` from Supabase PostgREST when querying `ai_user_memories`:
  ```
  /rest/v1/ai_user_memories?select=memory_text,content,category,importance_score...
  ```
- **Root Cause**: Schema drift: `ai_user_memories` stores records with columns `memory_type` and `content` (along with `id, user_id, importance_score, metadata, created_at`), but the client requested non-existent columns `memory_text` and `category`.
- **Resolution**: Aligned query to select `*` and gracefully extract content and memory types with fallbacks across both schemas.

---

## 3. Subsystem Architecture & Implementation

### 3.1 NCERT Canonical Code Schema (`textbookResolver.ts`)
The resolver translates any class level, subject, and chapter into the official NCERT textbook filename standard:

| Subject & Class | NCERT Book Prefix | Part 1 Prefix | Part 2 Prefix | Example URL |
| :--- | :--- | :--- | :--- | :--- |
| **Class 9 Mathematics** | `iemh1` (Part 1), `iemh2` (Part 2) | Ch 1–8 (`iemh101`..`08`) | Ch 9–14 (`iemh201`..`06`) | `https://ncert.nic.in/textbook/pdf/iemh101.pdf` |
| **Class 10 Mathematics** | `jemh1` | Ch 1–14 (`jemh101`..`14`) | N/A | `https://ncert.nic.in/textbook/pdf/jemh101.pdf` |
| **Class 11 Mathematics** | `kemh1` | Ch 1–14 (`kemh101`..`14`) | N/A | `https://ncert.nic.in/textbook/pdf/kemh101.pdf` |
| **Class 12 Mathematics** | `lemh1` (Part 1), `lemh2` (Part 2) | Ch 1–6 (`lemh101`..`06`) | Ch 7–13 (`lemh201`..`07`) | `https://ncert.nic.in/textbook/pdf/lemh101.pdf` |
| **Class 9 Science** | `iesc1` | Ch 1–12 (`iesc101`..`12`) | N/A | `https://ncert.nic.in/textbook/pdf/iesc101.pdf` |
| **Class 10 Science** | `jesc1` | Ch 1–13 (`jesc101`..`13`) | N/A | `https://ncert.nic.in/textbook/pdf/jesc101.pdf` |
| **Class 11 Physics** | `keph1` (Part 1), `keph2` (Part 2) | Ch 1–7 (`keph101`..`07`) | Ch 8–14 (`keph201`..`07`) | `https://ncert.nic.in/textbook/pdf/keph101.pdf` |
| **Class 11 Chemistry** | `kech1` (Part 1), `kech2` (Part 2) | Ch 1–6 (`kech101`..`06`) | Ch 7–12 (`kech201`..`06`) | `https://ncert.nic.in/textbook/pdf/kech101.pdf` |
| **Class 11 Biology** | `kebo1` | Ch 1–19 (`kebo101`..`19`) | N/A | `https://ncert.nic.in/textbook/pdf/kebo101.pdf` |
| **Class 12 Physics** | `leph1` (Part 1), `leph2` (Part 2) | Ch 1–8 (`leph101`..`08`) | Ch 9–14 (`leph201`..`06`) | `https://ncert.nic.in/textbook/pdf/leph101.pdf` |
| **Class 12 Chemistry** | `lech1` (Part 1), `lech2` (Part 2) | Ch 1–5 (`lech101`..`05`) | Ch 6–10 (`lech201`..`05`) | `https://ncert.nic.in/textbook/pdf/lech101.pdf` |
| **Class 12 Biology** | `lebo1` | Ch 1–13 (`lebo101`..`13`) | N/A | `https://ncert.nic.in/textbook/pdf/lebo101.pdf` |

### 3.2 102-Chapter Dynamic Indexing (`textbookPageMap.json`)
All 102 chapters across Class 9, 10, and 11 Mathematics and Science are fully indexed with:
- Canonical official NCERT PDF URL
- Total chapter page count
- Concept-by-concept starting page numbers
- Work-example and exercise page anchors

### 3.3 Synchronized Side Book Viewer (`SideBookViewer.tsx`)
- **Docked Beside Chalkboard**: Renders as an interactive split pane next to the digital chalkboard.
- **Concept Page Auto-Scroll**: When the tutor introduces a concept or exercise, the viewer automatically updates its hash fragment `#page=<pageNumber>&view=FitH`, jumping directly to the corresponding textbook section.
- **Mobile Safari Compatibility**: On iOS Safari where cross-origin iframes may restrict internal PDF scroll events, a minimalist top bar provides a direct 1-tap external viewer button (`ExternalLink`) opening the exact official NCERT page in a native PDF view.
- **Clean Minimalist Header**: Stripped of bloat, displaying only:
  ```
  [Book Title]  [ < ] Page [ N ] / [Total] [ > ]  [ExternalLink]  [ ✕ ]
  ```

---

## 4. Verification & Testing

- `npx tsc --noEmit`: **0 errors**.
- Official NCERT URL construction verified across all 12 class/subject variants.
- Dynamic page hash switching verified on concept transitions.
- Signed off and committed to `main`.
