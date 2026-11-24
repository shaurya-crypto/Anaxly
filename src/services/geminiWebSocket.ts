import { GoogleGenAI, Type, Behavior, FunctionResponseScheduling, StartSensitivity, EndSensitivity } from '@google/genai';
import { cleanChalkboardTypography } from '../components/whiteboard/chalkboardTypography';
import { PedagogicalStateManager } from './pedagogicalStateManager';

export interface CustomizedAvatarConfig {
  imageData?: string;
  imageMimeType?: string;
}

export interface LiveAvatarConfig {
  avatarName?: string;
  customizedAvatar?: CustomizedAvatarConfig;
  audioBitrateBps?: number;
  videoBitrateBps?: number;
}

export interface GeminiLiveCallbacks {
  onSetupComplete: () => void;
  onAudioData: (pcmData: Int16Array, sampleRate: number) => void;
  onVideoData?: (data: string, mimeType: string) => void;
  onInterrupted: () => void;
  onTurnComplete: () => void;
  onTranscript: (text: string, sender: "user" | "teacher") => void;
  onError: (error: Error) => void;
  onClose: (event: CloseEvent) => void;
  onUserSpeechStart?: () => void;
  onChalkboardToolCall?: (action: string, content: any, color?: string) => void;
  onVisualAction?: (action: string, params: Record<string, any>) => void;
  onGetBoardContent?: () => string;
  onHighlightText?: (text: string, target?: string, color?: string) => void;
}

export class GeminiLiveClient {
  private ai: GoogleGenAI;
  private session: any | null = null;
  private pedagogicalStateManager: PedagogicalStateManager;
  private apiKey: string;
  private model: string;
  private voiceName: string;
  private supportedLanguages: string[];
  private languageCode: string;
  private thinkingLevel: string;
  private systemInstruction: string;
  private callbacks: GeminiLiveCallbacks;
  private isManuallyClosed: boolean = false;
  private isConnected: boolean = false;
  private hasSentKickoff: boolean = false;
  private pendingKickoffText: string | null = null;
  private enableFunctionCalling: boolean = false;
  private avatarConfig?: LiveAvatarConfig;
  private executedToolCallIds = new Set<string>();
  private lastExecutedToolCalls = new Map<string, number>();
  private pendingBoardContext: string | null = null;
  private isModelGenerating: boolean = false;
  private turnToolCallsExecuted: number = 0;
  private turnEmittedAudio: boolean = false;
  private lastExecutedToolAction: string | null = null;
  private silentTurnNudgeCount: number = 0;

  constructor(
    authTokenOrApiKey: string,
    callbacks: GeminiLiveCallbacks,
    options?: {
      model?: string;
      voiceName?: string;
      systemInstruction?: string;
      enableFunctionCalling?: boolean;
      avatarConfig?: LiveAvatarConfig;
      supportedLanguages?: string[];
      languageCode?: string;
      preferredLanguage?: string;
      thinkingLevel?: string;
      pedagogicalStateManager?: PedagogicalStateManager;
    }
  ) {
    this.apiKey = authTokenOrApiKey;
    this.callbacks = callbacks;
    this.pedagogicalStateManager = options?.pedagogicalStateManager || new PedagogicalStateManager();
    let model = options?.model || "gemini-3.8-live";
    if (model.startsWith("models/")) {
      model = model.replace("models/", "");
    }
    // Low latency invariant: Do NOT use gemini-3.8-live-extended; strictly keep gemini-3.8-live
    if (model.includes("extended-thinking")) {
      model = "gemini-3.8-live";
    }
    this.model = model;
    
    this.supportedLanguages =
      options?.supportedLanguages && options.supportedLanguages.length > 0
        ? options.supportedLanguages
        : ["en-IN", "hi-IN"];
    this.languageCode =
      options?.languageCode ||
      (options?.preferredLanguage?.toLowerCase().includes("hindi") ? "hi-IN" : "en-IN");
    
    // Dynamic voice adaptation
    this.voiceName = options?.voiceName || (this.languageCode === "hi-IN" ? "Fenrir" : "Leda");
    
    this.thinkingLevel = options?.thinkingLevel || "";
    this.enableFunctionCalling = options?.enableFunctionCalling ?? false;
    this.avatarConfig = options?.avatarConfig;
    this.systemInstruction = options?.systemInstruction || `You are an inspiring, charismatic senior academic faculty mentor standing at a live chalkboard for Classes 6-12 (CBSE, ICSE, IB).
    1. Language Style & Charismatic Teacher Voice: Radiate calm confidence, intellectual clarity, and genuine warmth. ALWAYS speak simple, colloquial Hinglish, Hindi, or English as requested. Talk like a beloved faculty mentor or exam-topper elder sibling (Bhaiya/Didi); use natural conversational phrases like "samjhe," "dekho," "bilkul," "chalo" to make concepts crystal clear.
    2. Complete Explanation First (5-6 Rich Sentences Per Turn): In each explanation turn, speak properly with rich pedagogical depth for 5 to 6 well-formed, articulate sentences covering physical intuition, living mechanisms, and real-world clarity. Never deliver fragmented, cut-off thoughts or stop halfway.
    3. Natural Chapter-Adaptive Pedagogy: Teach naturally according to the subject and chapter without rigid robotic stage announcements:
       - Science / Physics / Chemistry / Biology: Everyday sensory intuition hook -> living physical/cellular mechanism -> exact scientific law, definition, and SI units -> concrete everyday/industrial applications -> interactive checkpoint questions -> step-by-step board numericals.
       - Mathematics: Real-world dilemma/anchor -> theorem/formula formulation with proofs -> model exemplar solved on chalkboard -> full spectrum of board-exam practice questions (MCQs, short answer, multi-step proofs, case-based).
       - Chemistry: Reaction mechanisms with electron flow, 3D molecular geometry, periodic trends (Z_eff, shielding), Given + Formula + Units first discipline.
    4. Seamless Voice & Live Chalkboard Synchronization:
       - Speak aloud what you are writing simultaneously as you write it. Synchronize your voice with the board in real-time. NEVER write in silence, and never dump text on the board without vocalizing it.
       - At the START of introducing each concept or new page, YOU MUST write the topic title cleanly on the chalkboard: write_chalkboard(action="draw_title", content="<Topic Title>", color="cream").
       - Follow authentic Topper Layout for derivations, numericals, and worked examples (one or max 2 concise steps per line):
         * Given line: write_chalkboard(action="draw_step", content="Given: m = 2 kg, a = 5 m/s²", color="amber")
         * Formula line: write_chalkboard(action="draw_step", content="Formula: F = m × a", color="blue")
         * Substitution line: write_chalkboard(action="draw_step", content="Step 1: F = 2 kg × 5 m/s²", color="white")
         * Calculation line: write_chalkboard(action="draw_step", content="Step 2: F = 10 N", color="white")
         * Boxed Answer line: write_chalkboard(action="draw_step", content="Boxed Answer: [ F = 10 N ]", color="botanical")
         * Scratchpad arithmetic: write_chalkboard(action="draw_rough_work", content="Rough: 2 × 5 = 10")
       - Pure Mathematical Typography: Use standard textbook notation and Unicode superscripts/symbols (x², v², 10⁸, θ, α, ×, ÷, √, ±). NEVER output raw programming syntax (*, **, ^, //).
    5. Proactive Complex Tables & Flowcharts (Real Master Teacher Invariant):
       - Teach visually with ultra-rich chalkboard diagrams like an iconic faculty mentor. Do NOT wait for the student to ask for a table or flowchart! Sketch them proactively whenever useful.
       - Comparison & Difference Tables (action="draw_table"): Whenever explaining differences, distinctions, comparisons, or properties of two or more entities (e.g. Plant vs Animal Cell, Xylem vs Phloem, Distance vs Displacement, Speed vs Velocity, Mitosis vs Meiosis, Real vs Virtual Images, Acids vs Bases, Metals vs Non-metals), PROACTIVELY DRAW A STRUCTURED COMPARISON TABLE:
         * write_chalkboard(action="draw_table", content="Parameter | Entity A | Entity B\nFeature 1 | Detail A1 | Detail B1\nFeature 2 | Detail A2 | Detail B2\nFeature 3 | Detail A3 | Detail B3")
       - Hierarchical Flow Trees & Classifications (action="draw_flowchart"): Whenever breaking down a concept into groups, taxonomies, or decision trees (e.g. Classification of Matter, Plant/Animal Tissues, Real Number System, Organic Reaction Pathways, Types of Sets), PROACTIVELY DRAW A BRANCHING FLOW TREE:
         * write_chalkboard(action="draw_flowchart", content="Root -> Group 1 | Group 2; Group 1 -> Sub 1 | Sub 2; Group 2 -> Sub 3 | Sub 4")
       - Cyclical Mechanisms & Process Pathways (action="draw_flowchart"): For biological or geochemical cycles (Nitrogen cycle, Carbon cycle, Cardiac cycle, Calvin cycle, Water cycle), prefix with 'cycle:':
         * write_chalkboard(action="draw_flowchart", content="cycle: Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 1")
       - Multi-Step Physiological / Reaction Pathways (action="draw_flowchart"):
         * write_chalkboard(action="draw_flowchart", content="Stimulus -> Sensory Receptor -> Sensory Neuron -> Spinal Cord -> Motor Neuron -> Effector Muscle -> Action")
    6. Visual Tools & Flexible Diagram Presentation:
       - Mandatory Concept Visuals: At the START of a visual concept, show an authentic diagram via search_and_show_image(...) and/or an animated demonstration video via search_and_show_video(...).
       - Flexible Diagram Mandate: Start with 1 clear diagram so the board stays clean and uncluttered. If the student asks for additional diagrams, comparisons (e.g. plant vs animal cell, xylem vs phloem, different ray positions), or if a follow-up diagram helps explain a doubt, call search_and_show_image freely! Everything is flexible, natural, and responsive like a real master faculty tutor.
       - Side Book Viewer: Reference standard textbook figures directly in the open NCERT page: "Look at Figure X on page N in your textbook in the side viewer". Do NOT redraw or extract book figures onto the digital chalkboard.
       - Mathematical Graph Engine: Proactively call plot_mathematical_graph(...) whenever plotting functions, curves, kinematics (v-t, s-t), Ohm's law (V-I), coordinate geometry, line segments, vectors, or statistical bar graphs.
    7. Active Questioning, Diagnostic Listening & The Hard Stop:
       - Complete your 5-6 sentence explanation thoroughly first -> THEN ask ONE engaging checkpoint question to verify the student's understanding.
       - THE HARD STOP: Once you ask a question, IMMEDIATELY STOP SPEAKING. Wait silently for the student's response. Do NOT answer your own question! Do NOT guess what they might say!
       - Immediate Stop on Student Inquiry: The moment the student speaks, asks a question, interrupts, or raises a doubt at any time, STOP speaking immediately! Listen with complete diagnostic attentiveness, address their query with clarity and kindness, and only then proceed.
       - Zero Auto-Solving: Never jump to solving without asking the student for given values or approach first. Co-solve together line-by-line.
    8. Strict Doubt & Re-explanation Lock:
       - If the student asks any question, raises a doubt ('doubt', 'douth', 'confused'), says they don't understand ('samajh nahi aaya'), or asks to explain again ('explain again', 'phir se samjhao', 'dobara samjhao', 'pura concept samjhao'):
       - You are STRICTLY FORBIDDEN from calling concept_completed or switching pages.
       - Stay on the current concept, write clear clarifying notes/examples on the current chalkboard, and re-explain thoroughly with fresh intuition until the student is 100% confident. Advance only after the student confirms understanding or explicitly commands "next concept."`;
    this.ai = new GoogleGenAI({
      apiKey: this.apiKey,
      httpOptions: { apiVersion: "v1alpha" },
    });
  }

  private extractAndExecuteEmbeddedToolCalls(rawText: string): string {
    if (!rawText) return rawText;

    // 1. Match pseudo-code: write_chalkboard(...) or write_board(action="...", content="...", color="...")
    const chalkboardRegex = /(?:write_chalkboard|write_chalkboardd|write_board|draw_board|chalkboard)\s*\(\s*(?:action\s*=\s*)?["']?([a-zA-Z0-9_\-]+)["']?\s*(?:,\s*(?:content\s*=\s*)?(?:["']([^"']*)["']|([^"',\)]*)))?(?:\s*,\s*(?:color\s*=\s*)?["']?([a-zA-Z0-9_#]+)["']?)?\s*\)/gi;
    let m;
    while ((m = chalkboardRegex.exec(rawText)) !== null) {
      const action = m[1]?.trim() || "";
      const content = (m[2] ?? m[3] ?? "").trim();
      const color = m[4]?.trim() || undefined;
      if (action) {
        this.handleSingleToolCall("write_chalkboard", { action, content, color });
      }
    }

    // 1a2. Match pseudo-code: highlight_text(...) or highlight_word(...)
    const highlightRegex = /(?:highlight_text|highlight_word|highlight_sentence)\s*\(\s*(?:(?:text|targetText|content)\s*=\s*)?(?:["']([^"']*)["']|([^"',\)]*))(?:\s*,\s*(?:target\s*=\s*)?["']?([a-zA-Z0-9_\-]+)["']?)?(?:\s*,\s*(?:color\s*=\s*)?["']?([a-zA-Z0-9_#]+)["']?)?\s*\)/gi;
    let hm;
    while ((hm = highlightRegex.exec(rawText)) !== null) {
      const text = (hm[1] ?? hm[2] ?? "").trim();
      const target = hm[3]?.trim() || "both";
      const color = hm[4]?.trim() || "amber";
      if (text) {
        this.handleSingleToolCall("highlight_text", { text, target, color });
      }
    }

    // 1b. Match bracket directives: [NOTE: ...], [STEP: ...], [DEFINITION: ...], [HIGHLIGHT: ...], etc.
    const bracketRegex = /\[(NOTE|INTUITION|INSIGHT|DEFINITION|LAW|FORMULA|HIGHLIGHT|HIGHLIGHT_WORD|HIGHLIGHT_SENTENCE|FOCUS_WORD|FOCUS_PHRASE|EXAMPLE|ILLUSTRATION|STEP|DERIVATION|CALCULATION|QUESTION|CHECKPOINT_QUESTION|BOARD_QUESTION|STUDENT_ANSWER|STUDENT|VERDICT|ANSWER_VERDICT|CORRECTION|CONCEPT_FOCUS|NUMERICAL|BOARD_NUMERICAL|WORKED_EXAMPLE|SOLVE|MATH_SOLVE):\s*([^\]]+)\]/gi;
    let bm;
    while ((bm = bracketRegex.exec(rawText)) !== null) {
      const type = bm[1]?.toUpperCase() || "";
      const content = bm[2]?.trim() || "";
      if (!content) continue;
      if (type === "NOTE" || type === "INTUITION" || type === "INSIGHT") {
        this.handleSingleToolCall("write_chalkboardd", { action: "draw_note", content: type === "INTUITION" ? `Intuition: ${content}` : content, color: "botanical" });
      } else if (type === "HIGHLIGHT_WORD" || type === "HIGHLIGHT_SENTENCE" || type === "FOCUS_WORD" || type === "FOCUS_PHRASE") {
        this.handleSingleToolCall("highlight_text", { text: content, target: "both", color: "amber" });
      } else if (type === "HIGHLIGHT") {
        if (content.length <= 45) {
          this.handleSingleToolCall("highlight_text", { text: content, target: "both", color: "amber" });
        } else {
          this.handleSingleToolCall("write_chalkboardd", { action: "draw_highlight_box", content: content, color: "coral" });
        }
      } else if (type === "DEFINITION" || type === "LAW" || type === "FORMULA") {
        this.handleSingleToolCall("write_chalkboardd", { action: "draw_highlight_box", content: content, color: "coral" });
      } else if (type === "EXAMPLE" || type === "ILLUSTRATION") {
        this.handleSingleToolCall("write_chalkboardd", { action: "draw_note", content: `Example: ${content}`, color: "blue" });
      } else if (type === "STEP" || type === "DERIVATION" || type === "CALCULATION") {
        this.handleSingleToolCall("write_chalkboardd", { action: "draw_step", content: content, color: "amber" });
      } else if (type === "QUESTION" || type === "CHECKPOINT_QUESTION" || type === "BOARD_QUESTION") {
        this.handleSingleToolCall("write_chalkboardd", { action: "draw_question", content: content, color: "amber" });
      } else if (type === "STUDENT_ANSWER" || type === "STUDENT") {
        this.handleSingleToolCall("write_chalkboardd", { action: "draw_student_answer", content: content, color: "blue" });
      } else if (type === "VERDICT" || type === "ANSWER_VERDICT" || type === "CORRECTION") {
        this.handleSingleToolCall("write_chalkboardd", { action: "draw_answer_verdict", content: content, color: "botanical" });
      } else if (type === "NUMERICAL" || type === "BOARD_NUMERICAL" || type === "WORKED_EXAMPLE" || type === "SOLVE" || type === "MATH_SOLVE") {
        this.handleSingleToolCall("write_chalkboardd", { action: "draw_numerical", content: content });
      } else if (type === "CONCEPT_FOCUS") {
        this.handleSingleToolCall("concept_focus", { conceptName: content });
      }
    }

    // 2. Match execute_visual_action(action="...", parameters={...})
    const visualRegex = /execute_visual_action\s*\(\s*(?:action\s*=\s*)?["']?([a-zA-Z0-9_\-]+)["']?\s*(?:,\s*(?:parameters\s*=\s*)?(\{.*?\})|\s*,\s*([^,\)]+))?\s*\)/gi;
    let vm;
    while ((vm = visualRegex.exec(rawText)) !== null) {
      const action = vm[1]?.trim() || "";
      let parameters: Record<string, any> = {};
      const rawParams = vm[2] || vm[3];
      if (rawParams) {
        try {
          parameters = JSON.parse(rawParams);
        } catch {
          // ignore parsing error
        }
      }
      if (action) {
        this.handleSingleToolCall("execute_visual_action", { action, parameters });
      }
    }

    // 3. Match draw_shape(...)
    const shapeRegex = /draw_shape\s*\(\s*([^()]+)\)/gi;
    let sm;
    while ((sm = shapeRegex.exec(rawText)) !== null) {
      const argStr = sm[1];
      try {
        if (argStr.trim().startsWith('{')) {
          this.handleSingleToolCall("draw_shape", JSON.parse(argStr.trim()));
        } else {
          this.handleSingleToolCall("draw_shape", { shape: argStr.trim() });
        }
      } catch {}
    }

    // 3b. Match plot_mathematical_graph(...)
    const graphRegex = /plot_mathematical_graph\s*\(([\s\S]*?)\)/gi;
    let gm;
    while ((gm = graphRegex.exec(rawText)) !== null) {
      const body = gm[1]?.trim() || "";
      if (!body) continue;
      if (body.startsWith("{")) {
        try {
          const parsed = JSON.parse(body);
          this.handleSingleToolCall("plot_mathematical_graph", parsed);
        } catch {}
      } else {
        const extractBalancedBracket = (src: string, key: string): string | null => {
          const idx = src.search(new RegExp(`\\b${key}\\s*=\\s*\\[`, 'i'));
          if (idx === -1) return null;
          const startBracket = src.indexOf('[', idx);
          if (startBracket === -1) return null;
          let depth = 0;
          for (let i = startBracket; i < src.length; i++) {
            if (src[i] === '[') depth++;
            else if (src[i] === ']') {
              depth--;
              if (depth === 0) return src.substring(startBracket, i + 1);
            }
          }
          return null;
        };

        const explicitFormula = body.match(/\bformula\s*=\s*["']([^"']*)["']/i);
        const explicitTitle = body.match(/\btitle\s*=\s*["']([^"']*)["']/i);
        const explicitDomain = body.match(/\bdomain\s*=\s*["']([^"']*)["']/i);
        const explicitRange = body.match(/\brange\s*=\s*["']([^"']*)["']/i);
        const explicitCallout = body.match(/\bcallout\s*=\s*["']([^"']*)["']/i);

        let points: any = undefined;
        const balancedPoints = extractBalancedBracket(body, 'points');
        if (balancedPoints) {
          try { points = JSON.parse(balancedPoints); } catch { points = balancedPoints; }
        } else {
          const explicitPoints = body.match(/\bpoints\s*=\s*(?:["']([^"']*)["']|(\[[^\]]*\])|([^\s,\)]+))/i);
          if (explicitPoints) {
            points = explicitPoints[1] || explicitPoints[2] || explicitPoints[3];
          }
        }

        let formulas: any = undefined;
        const balancedFormulas = extractBalancedBracket(body, 'formulas');
        if (balancedFormulas) {
          try { formulas = JSON.parse(balancedFormulas); } catch { formulas = balancedFormulas; }
        } else {
          const explicitFormulasStr = body.match(/\bformulas\s*=\s*["']([^"']*)["']/i);
          if (explicitFormulasStr) formulas = explicitFormulasStr[1];
        }

        let segments: any = undefined;
        const balancedSegments = extractBalancedBracket(body, 'segments');
        if (balancedSegments) {
          try { segments = JSON.parse(balancedSegments); } catch { segments = balancedSegments; }
        } else {
          const explicitSegmentsStr = body.match(/\bsegments\s*=\s*["']([^"']*)["']/i);
          if (explicitSegmentsStr) segments = explicitSegmentsStr[1];
        }

        const formula = explicitFormula ? explicitFormula[1] : body.split(',')[0]?.replace(/^["']|["']$/g, '').trim() || undefined;

        this.handleSingleToolCall("plot_mathematical_graph", {
          formula,
          formulas,
          segments,
          title: explicitTitle ? explicitTitle[1] : undefined,
          domain: explicitDomain ? explicitDomain[1] : undefined,
          range: explicitRange ? explicitRange[1] : undefined,
          callout: explicitCallout ? explicitCallout[1] : undefined,
          points,
        });
      }
    }

    // 4. Match render_svg_diagram(...)
    const svgRegex = /render_svg_diagram\s*\(([\s\S]*?)\)/gi;
    let svgm;
    while ((svgm = svgRegex.exec(rawText)) !== null) {
      const body = svgm[1]?.trim() || "";
      if (!body) continue;
      if (body.startsWith("{")) {
        try {
          const parsed = JSON.parse(body);
          if (parsed.title || parsed.svg || parsed.what) {
            this.handleSingleToolCall("render_svg_diagram", {
              title: parsed.title || "Educational Diagram",
              svg: parsed.svg || "",
              caption: parsed.caption || "",
              what: parsed.what || "",
            });
          }
        } catch {}
      } else {
        const explicitTitle = body.match(/\btitle\s*=\s*["']([^"']*)["']/i);
        const explicitSvg = body.match(/\bsvg\s*=\s*["']([\s\S]*?)["'](?:\s*,\s*[a-zA-Z_]+\s*=|\s*$)/i);
        const explicitCaption = body.match(/\bcaption\s*=\s*["']([^"']*)["']/i);
        const explicitWhat = body.match(/\bwhat\s*=\s*["']([^"']*)["']/i);
        if (explicitTitle || explicitSvg || explicitWhat) {
          const title = explicitTitle ? explicitTitle[1] : "Educational Diagram";
          const svg = explicitSvg ? explicitSvg[1] : "";
          const caption = explicitCaption ? explicitCaption[1] : "";
          const what = explicitWhat ? explicitWhat[1] : "";
          this.handleSingleToolCall("render_svg_diagram", { title, svg, caption, what });
        } else {
          const posMatch = body.match(/["']([^"']*)["'](?:\s*,\s*["']([\s\S]*?)["'])?(?:\s*,\s*["']([^"']*)["'])?/);
          if (posMatch && posMatch[1]) {
            this.handleSingleToolCall("render_svg_diagram", {
              title: posMatch[1],
              svg: posMatch[2] || "",
              caption: posMatch[3] || "",
            });
          }
        }
      }
    }

    // 4a2. Match search_and_show_image(...)
    const searchImgRegex = /search_and_show_image\s*\(([\s\S]*?)\)/gi;
    let sim;
    while ((sim = searchImgRegex.exec(rawText)) !== null) {
      const body = sim[1]?.trim() || "";
      if (!body) continue;
      if (body.startsWith("{")) {
        try {
          const parsed = JSON.parse(body);
          this.handleSingleToolCall("search_and_show_image", parsed);
        } catch {}
      } else {
        const explicitQuery = body.match(/\bquery\s*=\s*["']([^"']*)["']/i);
        const explicitTitle = body.match(/\btitle\s*=\s*["']([^"']*)["']/i);
        const explicitCaption = body.match(/\bcaption\s*=\s*["']([^"']*)["']/i);
        const query = explicitQuery ? explicitQuery[1] : body.split(',')[0]?.replace(/^["']|["']$/g, '').trim() || '';
        const title = explicitTitle ? explicitTitle[1] : body.split(',')[1]?.replace(/^["']|["']$/g, '').trim() || query;
        const caption = explicitCaption ? explicitCaption[1] : body.split(',')[2]?.replace(/^["']|["']$/g, '').trim() || '';
        if (query) {
          this.handleSingleToolCall("search_and_show_image", { query, title, caption });
        }
      }
    }

    // 4a3. Match search_and_show_video(...)
    const searchVidRegex = /search_and_show_video\s*\(([\s\S]*?)\)/gi;
    let svm;
    while ((svm = searchVidRegex.exec(rawText)) !== null) {
      const body = svm[1]?.trim() || "";
      if (!body) continue;
      if (body.startsWith("{")) {
        try {
          const parsed = JSON.parse(body);
          this.handleSingleToolCall("search_and_show_video", parsed);
        } catch {}
      } else {
        const explicitQuery = body.match(/\bquery\s*=\s*["']([^"']*)["']/i);
        const explicitTitle = body.match(/\btitle\s*=\s*["']([^"']*)["']/i);
        const explicitDesc = body.match(/\b(?:description|caption)\s*=\s*["']([^"']*)["']/i);
        const query = explicitQuery ? explicitQuery[1] : body.split(',')[0]?.replace(/^["']|["']$/g, '').trim() || '';
        const title = explicitTitle ? explicitTitle[1] : body.split(',')[1]?.replace(/^["']|["']$/g, '').trim() || query;
        const description = explicitDesc ? explicitDesc[1] : body.split(',')[2]?.replace(/^["']|["']$/g, '').trim() || '';
        if (query) {
          this.handleSingleToolCall("search_and_show_video", { query, title, description });
        }
      }
    }


    // 4c. Match concept_focus(...)
    const conceptFocusRegex = /(?:concept_focus|focus_concept)\s*\(\s*(?:(?:conceptName|concept)\s*=\s*)?["']?([^"'\)]*)["']?\s*\)/gi;
    let cfm;
    while ((cfm = conceptFocusRegex.exec(rawText)) !== null) {
      const cName = cfm[1]?.trim() || "";
      this.handleSingleToolCall("concept_focus", { conceptName: cName });
    }

    // 5. Strip any leaked tool calls and bracket directives from spoken transcript text
    const stripCall = (name: string) => new RegExp(`${name}\\s*\\((?:'[^']*'|"[^"]*"|[^()]*|\\([^()]*\\))*\\)`, "gi");
    return rawText
      .replace(stripCall("write_chalkboard"), "")
      .replace(stripCall("write_chalkboardd"), "")
      .replace(stripCall("write_board"), "")
      .replace(stripCall("draw_board"), "")
      .replace(stripCall("chalkboard"), "")
      .replace(stripCall("execute_visual_action"), "")
      .replace(stripCall("plot_mathematical_graph"), "")
      .replace(stripCall("open_interactive_simulation"), "")
      .replace(stripCall("update_interactive_simulation"), "")
      .replace(stripCall("draw_shape"), "")
      .replace(stripCall("solve_step_by_step_numerical"), "")
      .replace(stripCall("conclude_and_open_quiz"), "")
      .replace(stripCall("concept_completed"), "")
      .replace(stripCall("concept_done"), "")
      .replace(stripCall("next_concept"), "")
      .replace(stripCall("advance_concept"), "")
      .replace(stripCall("concept_focus"), "")
      .replace(stripCall("focus_concept"), "")
      .replace(stripCall("highlight_text"), "")
      .replace(stripCall("highlight_word"), "")
      .replace(stripCall("highlight_sentence"), "")
      .replace(stripCall("render_svg_diagram"), "")
      .replace(/render_svg_diagram\s*\([\s\S]*?\)/gi, "")
      .replace(stripCall("search_and_show_image"), "")
      .replace(/search_and_show_image\s*\([\s\S]*?\)/gi, "")
      .replace(stripCall("search_and_show_video"), "")
      .replace(/search_and_show_video\s*\([\s\S]*?\)/gi, "")
      .replace(/\[(?:STAGE|PHASE|NOTE|STEP|DEFINITION|LAW|FORMULA|HIGHLIGHT|QUESTION|CHECKPOINT|VERDICT|NUMERICAL|CONCEPT)[^\]]*\]/gi, "")
      .replace(/\[[A-Z_]+(?::\s*[^\]]*)?\]/gi, "")
      .replace(/(?:^|\n|\.\s+)(?:Now\s+(?:in|entering|moving\s+to)\s+)?(?:Stage|Phase)\s*\d+\s*[:\-–—]\s*/gi, "$1")
      .replace(/\b(?:Executing|Calling|Triggering|Running)\s+(?:tool\s+|function\s+)?(?:write_chalkboard|write_chalkboardd|write_board|draw_board|draw_step|draw_note|draw_question|draw_answer_verdict|draw_numerical|plot_mathematical_graph|search_and_show_image|search_and_show_video|render_svg_diagram|concept_completed|highlight_text)\b(?:\([^)]*\))?[:\-–—.]?\s*/gi, "")
      .replace(/\s+/g, " ")
      .trim();
  }

  private handleSingleToolCall(name: string, args: any, callId?: string): any {
    if (!this.pedagogicalStateManager.handleToolCall(name)) {
      return { result: "Progression blocked: finish current stage first" };
    }
    if (callId) {
      if (this.executedToolCallIds.has(callId)) {
        return;
      }
      this.executedToolCallIds.add(callId);
      if (this.executedToolCallIds.size > 200) {
        const first = this.executedToolCallIds.values().next().value;
        if (first) this.executedToolCallIds.delete(first);
      }
    }

    const argKey = typeof args === 'string' ? args : JSON.stringify(args);
    const callSignature = `${name}:${argKey}`;
    const now = Date.now();
    const lastTime = this.lastExecutedToolCalls.get(callSignature);
    if (lastTime && (now - lastTime) < 2500) {
      return;
    }
    this.lastExecutedToolCalls.set(callSignature, now);
    if (this.lastExecutedToolCalls.size > 200) {
      for (const [k, t] of this.lastExecutedToolCalls.entries()) {
        if (now - t > 60000) this.lastExecutedToolCalls.delete(k);
      }
    }
    this.lastExecutedToolAction = name;
    // Wrap callback execution in a microtask or setTimeout to ensure it's non-blocking
    setTimeout(() => {
        if (
          name === "write_chalkboard" ||
          name === "write_chalkboardd" ||
          name === "write_board" ||
          name === "chalkboard" ||
          name === "whiteboard" ||
          name === "draw_chalkboard" ||
          name === "draw_board"
        ) {
          let action = args.action || "";
          let textContent = args.content ?? args.text ?? args.note ?? args.step ?? args.title ?? args.question ?? "";
          let color = args.color || "";
    
          if (!action) {
            if (args.note) action = "draw_note";
            else if (args.step) action = "draw_step";
            else if (args.title) action = "draw_title";
            else if (args.question) { action = "draw_question"; textContent = args.question; }
            else if (args.highlight) { action = "draw_highlight_box"; textContent = args.highlight; }
            else if (args.formula) { action = "draw_step"; textContent = args.formula; }
            else {
              action = "draw_note";
              if (typeof args === "string") textContent = args;
            }
          }
          this.lastExecutedToolAction = action;
    
          if (typeof textContent === "string") {
            textContent = cleanChalkboardTypography(textContent);
          }
    
          if (action === "draw_numerical" || action === "numerical") {
            let numericalPayload: any = args.content !== undefined ? args.content : args;
            if (typeof numericalPayload === 'string') {
              try {
                const parsed = JSON.parse(numericalPayload);
                if (parsed && typeof parsed === 'object') {
                  numericalPayload = parsed;
                }
              } catch {
                // Keep as raw string (pipe-separated)
              }
            }
            this.callbacks.onChalkboardToolCall?.("draw_numerical", numericalPayload);
          } else if (action === "highlight_text" || action === "highlight_word" || action === "highlight_sentence") {
            this.callbacks.onHighlightText?.(textContent, "both", color || "amber");
          } else {
            this.callbacks.onChalkboardToolCall?.(action, textContent, color);
          }
        } else if (name === "highlight_text" || name === "highlight_word" || name === "highlight_sentence") {
          const textToHighlight = args.text || args.content || args.word || args.sentence || (typeof args === "string" ? args : "");
          const target = args.target || "both";
          const color = args.color || "amber";
          this.callbacks.onHighlightText?.(textToHighlight, target, color);
        } else if (name === "execute_visual_action") {
          const action = args.action || "";
          const parameters = args.parameters || {};
          this.callbacks.onVisualAction?.(action, parameters);
        } else if (name === "plot_mathematical_graph") {
          this.callbacks.onChalkboardToolCall?.("draw_graph", args);
        } else if (name === "open_interactive_simulation") {
          const sceneType = args.sceneType || "geometry";
          const parameters = args.parameters || {};
          const title = args.title || parameters.title;
          this.callbacks.onVisualAction?.("SHOW_SCENE", { sceneType, title, ...parameters });
        } else if (name === "update_interactive_simulation") {
          const parameters = args.parameters || args;
          const title = args.title || parameters.title;
          this.callbacks.onVisualAction?.("UPDATE_SCENE", { title, ...parameters });
        } else if (name === "draw_shape") {
          this.callbacks.onChalkboardToolCall?.("draw_shape", args, args.color);
        } else if (name === "solve_step_by_step_numerical") {
          this.callbacks.onChalkboardToolCall?.("draw_numerical", args);
        } else if (name === "render_svg_diagram") {
          const title = args.title || "Educational Diagram";
          const svg = args.svg || "";
          const caption = args.caption || "";
          const what = args.what || "";
          this.callbacks.onChalkboardToolCall?.("render_svg_diagram", { title, svg, caption, what });
        } else if (name === "search_and_show_image") {
          const query = args.query || args.searchQuery || args.q || "";
          const title = args.title || query || "Scientific Diagram";
          const caption = args.caption || "";
          if (query && typeof window !== "undefined") {
            fetch("/api/diagram/search-image", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ query }),
            })
              .then((res) => res.json())
              .then(async (data) => {
                const candidateImages = data.images || [];
                let displayed = false;
                for (const img of candidateImages) {
                  if (!img?.url) continue;
                  try {
                    const check = await fetch(`/api/diagram/proxy?dataUrl=true&url=${encodeURIComponent(img.url)}`);
                    if (check.ok) {
                      const pData = await check.json();
                      if (pData.success && pData.dataURL) {
                        this.callbacks.onChalkboardToolCall?.("draw_image", {
                          url: pData.dataURL,
                          title: title || img.title,
                          caption: caption || img.description || "",
                        });
                        displayed = true;
                        break;
                      }
                    }
                  } catch {
                    // Failover to next candidate image
                  }
                }
                if (!displayed) {
                  // Only fall back to SVG diagram if all online image search candidates fail
                  this.callbacks.onChalkboardToolCall?.("render_svg_diagram", {
                    title,
                    caption,
                  });
                }
              })
              .catch((err) => {
                console.warn("[GeminiLive] search_and_show_image error:", err);
                this.callbacks.onChalkboardToolCall?.("render_svg_diagram", {
                  title,
                  caption,
                });
              });
          }
        } else if (name === "search_and_show_video") {
          const query = args.query || args.searchQuery || args.q || "";
          const title = args.title || query || "Demonstration Video";
          const description = args.description || args.caption || "";
          if (query && typeof window !== "undefined") {
            fetch("/api/diagram/search-video", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ query }),
            })
              .then((res) => res.json())
              .then((data) => {
                const firstVid = data.videos?.[0];
                if (firstVid?.url) {
                  this.callbacks.onChalkboardToolCall?.("draw_video", {
                    url: firstVid.url,
                    title: title || firstVid.title,
                    description: description || firstVid.description || "",
                    mimeType: firstVid.mimeType || "video/mp4",
                  });
                } else {
                  this.callbacks.onChalkboardToolCall?.("draw_video", {
                    url: "",
                    title,
                    description,
                  });
                }
              })
              .catch((err) => {
                console.warn("[GeminiLive] search_and_show_video error:", err);
                this.callbacks.onChalkboardToolCall?.("draw_video", {
                  url: "",
                  title,
                  description,
                });
              });
          }
        } else if (name === "conclude_and_open_quiz") {
          if (args.summary) {
            this.callbacks.onChalkboardToolCall?.("chapter_summary", args.summary);
          }
          this.callbacks.onChalkboardToolCall?.("open_quiz", args.summary || "10-MCQ Diagnostic Evaluation");
        } else if (name === "get_board_content" || name === "read_board_content" || name === "get_board_state") {
          const boardState = this.callbacks.onGetBoardContent?.() || "";
          return {
            result: "ok",
            chalkboard_content: boardState || "Digital chalkboard is active. No notes written yet.",
          };
        } else if (name === "close_graph" || ((name === "write_chalkboard" || name === "write_chalkboardd") && args?.action === "close_graph")) {
          this.callbacks.onChalkboardToolCall?.("close_graph", "");
        } else if (name === "concept_completed" || name === "next_concept" || name === "advance_concept") {
          const cName = args.conceptName || args.concept || (typeof args === "string" ? args : "");
          this.callbacks.onChalkboardToolCall?.("concept_done", cName);
        } else if (name === "concept_focus" || name === "focus_concept") {
          const cName = args.conceptName || args.concept || (typeof args === "string" ? args : "");
          this.callbacks.onChalkboardToolCall?.("concept_focus", cName);
        } else {
          this.callbacks.onChalkboardToolCall?.(name, typeof args === 'string' ? args : JSON.stringify(args));
        }
    }, 0);
  }

  public async connect(kickoffPrompt?: string): Promise<void> {
    if (this.session) return;
    this.isManuallyClosed = false;
    this.hasSentKickoff = false;
    if (kickoffPrompt) {
      this.pendingKickoffText = kickoffPrompt;
    }

    try {
      console.log(`[GeminiLive] Connecting session with model: ${this.model}, voice: ${this.voiceName}, enableFunctionCalling: ${this.enableFunctionCalling}`);

      const responseModalities = this.avatarConfig
        ? ["VIDEO" as any, "AUDIO" as any]
        : ["AUDIO" as any];

      const liveConfig: any = {
        responseModalities,
        systemInstruction: { parts: [{ text: this.systemInstruction }] },
        realtimeInputConfig: {
          automaticActivityDetection: {
            disabled: false,
            startOfSpeechSensitivity: StartSensitivity.START_SENSITIVITY_LOW,
            endOfSpeechSensitivity: EndSensitivity.END_SENSITIVITY_HIGH,
            prefixPaddingMs: 40,
            silenceDurationMs: 350,
          },
        },
        contextWindowCompression: {
          slidingWindow: {},
        },
        speechConfig: {
          voiceConfig: {
            prebuiltVoiceConfig: {
              voiceName: this.voiceName,
            },
          },
        },
        inputAudioTranscription: {
          languageCodes: this.supportedLanguages,
        },
        outputAudioTranscription: {
          languageCodes: this.supportedLanguages,
        },
      };

      if (this.avatarConfig) {
        liveConfig.avatarConfig = this.avatarConfig;
      }

      // Zero Latency Degradation & Unsupported Model Guard:
      // Thinking level is strictly unsupported for standard Gemini Live audio models (gemini-3.8-live, gemini-2.5-live).
      // Passing thinkingConfig causes Google Live WebSockets to immediately close with code 1007.
      const isThinkingSupported =
        this.model.includes("extended-thinking") ||
        (this.model.includes("thinking") && !this.model.includes("live"));

      if (isThinkingSupported && this.thinkingLevel && this.thinkingLevel !== "minimal" && this.thinkingLevel !== "none") {
        const safeThinkingLevel =
          this.thinkingLevel === "high" || this.thinkingLevel === "medium"
            ? "low"
            : this.thinkingLevel || "low";
        liveConfig.thinkingConfig = {
          thinkingLevel: safeThinkingLevel,
        };
      }

      if (this.enableFunctionCalling) {
        liveConfig.tools = [
          {
            functionDeclarations: [
              {
                name: "write_chalkboard",
                description: "MANDATORY CHALKBOARD TOOL: You MUST invoke this tool in EVERY spoken turn to write notes, definitions, steps, formulas, worked examples, questions, comparison tables, or flowcharts on the student's live chalkboard. Speaking without calling this tool is strictly prohibited. PROACTIVE VISUAL MASTERY: Whenever comparing, contrasting, or listing differences between concepts, ALWAYS call action='draw_table' with a rich comparison table. Whenever explaining groups, hierarchies, taxonomies, decision trees, or process cycles, ALWAYS call action='draw_flowchart'. For problem solving, write cleanly with 1 or at most 2 steps per line in standard topper layout (Given -> Formula -> Substitution -> Calculation -> Boxed Answer).",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    action: {
                      type: Type.STRING,
                      enum: [
                        "draw_title",
                        "draw_note",
                        "draw_step",
                        "draw_highlight_box",
                        "draw_question",
                        "draw_answer_verdict",
                        "draw_exam_question",
                        "draw_flowchart",
                        "draw_table",
                        "draw_numerical",
                        "concept_focus",
                        "concept_done",
                        "close_graph",
                        "set_color",
                      ],
                      description: "The chalkboard action to perform (e.g. draw_note, draw_step, draw_highlight_box, draw_question, draw_answer_verdict, draw_exam_question, draw_flowchart, draw_table, draw_numerical, close_graph, concept_focus, concept_done, set_color)",
                    },
                    content: {
                      type: Type.STRING,
                      description: "The text to write, equation, table markup, flowchart text, or color name to apply to the chalkboard. For comparison tables (action='draw_table'), format as markdown table: 'Parameter | Entity A | Entity B\nRow 1 | Val A1 | Val B1\nRow 2 | Val A2 | Val B2'. For flowcharts (action='draw_flowchart'), format as branching trees ('Root -> Branch A | Branch B; Branch A -> Sub 1 | Sub 2'), cyclical loops ('cycle: Step 1 -> Step 2 -> Step 3 -> Step 1'), or sequential pathways ('Step 1 -> Step 2 -> Step 3'). For problem solving or derivations, format with 1 or max 2 steps per line in standard topper layout (Given -> Formula -> Substitution -> Calculation -> Boxed Answer).",
                    },
                    color: {
                      type: Type.STRING,
                      enum: [
                        "white",
                        "primary",
                        "botanical",
                        "green",
                        "coral",
                        "red",
                        "amber",
                        "yellow",
                        "blue",
                        "cyan",
                        "purple",
                        "lavender",
                        "rose",
                      ],
                      description: "Optional chalk color to write with (botanical, coral, amber, blue, purple, white). Use botanical/green for biology/definitions, coral/red for laws & boxed formulas, blue for physics/derivations, amber/yellow for SI units/highlights, purple for terms, white for standard text.",
                    },
                  },
                  required: ["action"],
                },
              },
              {
                name: "close_graph",
                description: "Dismiss or close the currently active interactive mathematical or physics graph on the student's whiteboard.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {},
                },
              },
              {
                name: "highlight_text",
                description: "LIVE AI HIGHLIGHTER: Temporarily highlight key words, terms, laws, formulas, or sentences on the student's chalkboard notes and/or live spoken subtitle streamer with an animated golden/amber glow pill marker. Call this dynamically while speaking to direct the student's visual focus to critical terms, exam keywords, or specific derivations.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    text: {
                      type: Type.STRING,
                      description: "The specific word, phrase, key term, or sentence to highlight (e.g. 'Photosynthesis', 'F = ma', 'Cellulose microfibrils', 'SI unit: Newton').",
                    },
                    target: {
                      type: Type.STRING,
                      enum: ["both", "chalkboard", "subtitles"],
                      description: "Where to render the highlight: 'both' (default), 'chalkboard' (marks text on the digital board), or 'subtitles' (glows in the live speech streamer).",
                    },
                    color: {
                      type: Type.STRING,
                      enum: ["amber", "yellow", "cyan", "botanical", "coral"],
                      description: "Chalk marker color: 'amber' (default golden marker), 'yellow', 'cyan', 'botanical', 'coral'.",
                    },
                  },
                  required: ["text"],
                },
              },
              {
                name: "plot_mathematical_graph",
                description: "CRITICAL MULTI-TYPE GRAPH ENGINE (MATHS, PHYSICS, SCIENCE & STATISTICS): Plot interactive mathematical functions, kinematics curves (v-t, s-t, a-t), Ohm's law (V-I), thermodynamics (P-V), statistical bar graphs & histograms, physics vectors, geometric figures, and custom coordinate texts directly on the whiteboard canvas. Call this tool whenever a question asks to plot or solve graphically, whenever drawing an exact graph from a question or question's answer, and whenever ANY small graphical aid or visual line helps explain a concept to the student! Supports: (1) functions formula/formulas; (2) bounded line segments with explicit lengths and stopping points; (3) critical coordinate points with labels; (4) statistical bar graphs & histograms via 'bars'; (5) physics vectors via 'vectors'; (6) geometric figures on Cartesian plane via 'polygons' and 'circles'; (7) multiple freeform text annotations placed anywhere on the graph via 'texts'. MANDATE: When plotting lines/curves, ALWAYS provide actual points (intercepts, intersection, roots, vertex, endpoints) and segments if bounded (with start and end points). If a geometric diagram (e.g. triangles, circles, angles) or physical apparatus is needed, use render_svg_diagram or search_and_show_image — NEVER use plot_mathematical_graph. STRICT ZERO MEANINGLESS GRAPH INVARIANT: NEVER output a meaningless default line y = x without points, segments, or purpose.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    formula: {
                      type: Type.STRING,
                      description: "The primary mathematical formula to plot, e.g. 'x^2 - 4' or '2x + 1' or 'sin(x)'. Never pass meaningless placeholder 'x'.",
                    },
                    formulas: {
                      type: Type.ARRAY,
                      items: { type: Type.STRING },
                      description: "Optional list of 2-3 simultaneous formulas for comparative multi-curve graphs, e.g. ['2x + 1', '-x + 4'] or JSON formula objects.",
                    },
                    segments: {
                      type: Type.ARRAY,
                      items: { type: Type.STRING },
                      description: "Optional bounded line segments with stopping start and end points, e.g. ['{\"start\": [0, 0], \"end\": [4, 8], \"label\": \"OA\"}']. Always specify when lines have endpoints.",
                    },
                    points: {
                      type: Type.STRING,
                      description: "Critical coordinate points to highlight with coordinates and labels, e.g. '(0, -4), (2, 0), (-2, 0)' or JSON array of points with callouts.",
                    },
                    domain: {
                      type: Type.STRING,
                      description: "Domain range for x-axis, e.g. '[-5, 5]'",
                    },
                    range: {
                      type: Type.STRING,
                      description: "Range for y-axis, e.g. '[-10, 10]'",
                    },
                    title: {
                      type: Type.STRING,
                      description: "Graph title, e.g. 'Quadratic Parabola: y = x^2 - 4'",
                    },
                    callout: {
                      type: Type.STRING,
                      description: "Key features or annotations, e.g. 'Roots at x = -2, 2 | Minimum at (0, -4)'",
                    },
                    bars: {
                      type: Type.ARRAY,
                      items: { type: Type.STRING },
                      description: "Statistical bar graph or histogram items, e.g. ['{\"label\": \"Maths\", \"height\": 85}', '{\"label\": \"Science\", \"height\": 92}'] or simple delimited string 'Maths: 85 | Science: 92'.",
                    },
                    vectors: {
                      type: Type.ARRAY,
                      items: { type: Type.STRING },
                      description: "Physics vectors and directional arrows, e.g. ['{\"tail\": [0, 0], \"tip\": [4, 3], \"label\": \"F1 = 5 N\"}'] or transition strings '(0,0) -> (4,3) [F1]'.",
                    },
                    polygons: {
                      type: Type.ARRAY,
                      items: { type: Type.STRING },
                      description: "Cartesian polygons like triangles or quadrilaterals, e.g. ['{\"points\": [[1,1],[5,1],[3,5]], \"label\": \"Triangle ABC\"}'].",
                    },
                    circles: {
                      type: Type.ARRAY,
                      items: { type: Type.STRING },
                      description: "Circles in Cartesian space, e.g. ['{\"center\": [0, 0], \"radius\": 4, \"label\": \"Circle r=4\"}'].",
                    },
                    texts: {
                      type: Type.ARRAY,
                      items: { type: Type.STRING },
                      description: "Multiple custom text annotations placed anywhere on the graph, e.g. ['{\"x\": 2, \"y\": 5, \"text\": \"Maximum Altitude\"}'].",
                    },
                    slope: {
                      type: Type.BOOLEAN,
                      description: "Whether to render a slope triangle (Delta y / Delta x) displaying rate of change or velocity.",
                    },
                    overwrite: {
                      type: Type.BOOLEAN,
                      description: "Set to true to overwrite/update the existing graph on the current page instead of adding another.",
                    },
                  },
                },
              },
              {
                name: "render_svg_diagram",
                description: "MANDATORY PROACTIVE CHALKBOARD DIAGRAM TOOL: Call this tool proactively on Step 1 of EACH concept to render a clean, high-precision 3D axonometric Hairline vector SVG educational diagram directly on the chalkboard. For all physical apparatus, optics, circuits, and 3D geometry, render 30Â° isometric projection with rounded wireframe solids, leader callouts, and clean white background. The student will NOT ask you for a diagram â€” you MUST draw it automatically on cue. Provide concise title (e.g. 'Plant Cell Wall', 'Reflection of Light', 'Simple Circuit'). You may optionally supply svg markup; if omitted, the high-precision vector diagram is rendered automatically.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    title: {
                      type: Type.STRING,
                      description: "Concise academic title of the diagram (e.g. 'Plant Cell Wall & Cellulose Microfibrils', 'Reflection of Light at Plane Mirror', 'Simple Resistor-Battery Circuit')",
                    },
                    what: {
                      type: Type.STRING,
                      description: "Detailed specification of anatomical parts, components, arrows, coordinate axes, and labels to draw.",
                    },
                    svg: {
                      type: Type.STRING,
                      description: "Optional complete, well-formed XML <svg> element with xmlns='http://www.w3.org/2000/svg'. If omitted, an authentic vector diagram is automatically generated and rendered.",
                    },
                    caption: {
                      type: Type.STRING,
                      description: "1-2 sentence pedagogical explanation or key takeaway highlighting the governing law or anatomical feature.",
                    },
                  },
                  required: ["title"],
                },
              },
              {
                name: "draw_shape",
                description: "Draw custom 2D or 3D geometric shapes (rectangle, square, circle, ellipse, triangle, right_triangle, cylinder, cube, polygon, line, arrow) on the whiteboard with complete control over width, height, radius, labels, and colors.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    shape: {
                      type: Type.STRING,
                      enum: [
                        "rectangle",
                        "square",
                        "circle",
                        "ellipse",
                        "triangle",
                        "right_triangle",
                        "cylinder",
                        "cube",
                        "cuboid",
                        "polygon",
                        "line",
                        "arrow",
                      ],
                      description: "The geometric shape to draw",
                    },
                    width: {
                      type: Type.NUMBER,
                      description: "Width in pixels (e.g. 80 to 720)",
                    },
                    height: {
                      type: Type.NUMBER,
                      description: "Height in pixels (e.g. 40 to 450)",
                    },
                    radius: {
                      type: Type.NUMBER,
                      description: "Radius in pixels for circle or cylinder (e.g. 30 to 200)",
                    },
                    label: {
                      type: Type.STRING,
                      description: "Educational formula, dimension callout, or label (e.g. 'Length = 30cm, Breadth = 15cm | Area = 450cmÂ²')",
                    },
                    values: {
                      type: Type.OBJECT,
                      description: "Custom dimension and angle values to display on the figure (e.g. { length: '12 cm', breadth: '5 cm', hypotenuse: '13 cm', angleA: '60Â°' }). Use standard school units (cm, m, Â°), NEVER pixels.",
                    },
                    overwrite: {
                      type: Type.BOOLEAN,
                      description: "Set to true to overwrite and update the existing shape on the current page instead of adding a new one below.",
                    },
                    color: {
                      type: Type.STRING,
                      enum: [
                        "botanical",
                        "coral",
                        "blue",
                        "amber",
                        "purple",
                        "white",
                      ],
                      description: "Chalk stroke color",
                    },
                    fillColor: {
                      type: Type.STRING,
                      description: "Optional background fill color",
                    },
                  },
                  required: ["shape"],
                },
              },
              {
                name: "open_interactive_simulation",
                description: "Summon an interactive 3D WebGL geometry solid or cross-section model directly on the whiteboard stage with full control over title, shape, and dimensions.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    sceneType: {
                      type: Type.STRING,
                      enum: [
                        "geometry_3d",
                        "geometry_cross_section",
                      ],
                      description: "The 3D geometric simulation scene to open ('geometry_3d' for 3D solids or 'geometry_cross_section' for cutting plane slices)",
                    },
                    title: {
                      type: Type.STRING,
                      description: "Custom title for the 3D model simulation",
                    },
                    parameters: {
                      type: Type.OBJECT,
                      description: "Dynamic simulation parameters and values (e.g. { shape: 'cylinder', radius: 4, height: 8 })",
                    },
                  },
                  required: ["sceneType"],
                },
              },
              {
                name: "update_interactive_simulation",
                description: "Update values, variables, sliders, or title of the currently active 3D simulation scene in real time (e.g. adjust shape, change radius or height, alter slice angle).",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    title: {
                      type: Type.STRING,
                      description: "Updated title for the simulation",
                    },
                    parameters: {
                      type: Type.OBJECT,
                      description: "Updated parameters and values to apply to the 3D model",
                    },
                  },
                },
              },
              {
                name: "conclude_and_open_quiz",
                description: "Conclude the teaching capsule, write the comprehensive chapter synthesis summary on the whiteboard, and prompt the student to open the 10-MCQ evaluation quiz. Call ONLY when ALL concepts in the capsule key concepts roadmap have been fully taught and mastered. NEVER call mid-lesson.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    summary: {
                      type: Type.STRING,
                      description: "The chapter synthesis summary covering all key definitions, formulas, and laws taught",
                    },
                  },
                  required: ["summary"],
                },
              },
              {
                name: "concept_completed",
                description: "CONCEPT ADVANCEMENT TOOL: Call this tool when the student has understood the current concept or solved the checkpoint question, or when the student asks to move to the next concept. NEVER call this tool when the student asks a question, raises a doubt, says they don't understand, or asks to explain again. Stay on the current concept and address doubts thoroughly.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    conceptName: {
                      type: Type.STRING,
                      description: "The name of the concept that was just mastered.",
                    },
                  },
                  required: ["conceptName"],
                },
              },
              {
                name: "search_and_show_image",
                description: "Display an authentic, high-resolution scientific educational diagram, anatomical structure, or textbook figure on the student's digital chalkboard. Mandatory when introducing a visual concept. If the student asks for additional diagrams, comparisons, or different angles, call freely to show more! Flexible and responsive like a real tutor.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    query: {
                      type: Type.STRING,
                      description: "Detailed, specific educational textbook diagram search query (e.g. 'Class 10 Physics concave mirror ray diagram labeled' or 'Class 9 Science plant cell vs animal cell ultrastructure labeled diagram').",
                    },
                    title: {
                      type: Type.STRING,
                      description: "Title for the chalkboard image card",
                    },
                    caption: {
                      type: Type.STRING,
                      description: "Key educational note or legend",
                    },
                  },
                  required: ["query", "title"],
                },
              },
              {
                name: "search_and_show_video",
                description: "Display an animated educational demonstration video on the student's chalkboard. Call when demonstrating a dynamic physical process, laboratory experiment, or biological motion.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    query: {
                      type: Type.STRING,
                      description: "Educational animated video search query requesting an animated short video to understand the concept (e.g. 'animated short video showing animation to understand concave mirror ray diagram').",
                    },
                    title: {
                      type: Type.STRING,
                      description: "Title for the demonstration video card",
                    },
                    description: {
                      type: Type.STRING,
                      description: "Brief 1-line educational description of what the video demonstrates",
                    },
                  },
                  required: ["query", "title"],
                },
              },
              {
                name: "get_board_content",
                description: "Inspect and read the current digital chalkboard contents, including all notes, definitions, formulas, student responses, answer verdicts, and rough work scratchpad currently visible on the board. Call this whenever the student asks about what is on the board, refers to board content, or before writing new notes to avoid duplication.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {},
                },
              },
            ],
          },
        ];
      }

      const sessionCallbacks = {
        onopen: () => {
          console.log("[GeminiLive] WebSocket TCP connection open; awaiting setupComplete...");
        },
        onmessage: (msg: any) => {
           const content = msg.serverContent;
           
           // Server Voice Activity Detection (VAD) events
           const isVoiceActivityStart = msg.voiceActivity?.voiceActivityType === "ACTIVITY_START" || msg.voiceActivity?.type === "ACTIVITY_START";
           if (isVoiceActivityStart) {
              this.callbacks.onUserSpeechStart?.();
           }

           // Handle root tool calls for chalkboard writing, visual stage, and dedicated tools
           if (msg.toolCall && msg.toolCall.functionCalls) {
             const responses: any[] = [];
             const isExtendedThinking = this.model.includes("extended-thinking");
             for (const call of msg.toolCall.functionCalls) {
               if (!call.id || this.executedToolCallIds.has(call.id)) {
                 continue;
               }
               const allowed = this.pedagogicalStateManager.handleToolCall(call.name, call.args);
               let toolResult: any;
               if (!allowed) {
                 toolResult = { result: "Progression blocked: complete checkpoint first" };
               } else {
                 toolResult = this.handleSingleToolCall(call.name, call.args || {}, call.id);
               }
               const responsePayload = (toolResult && typeof toolResult === 'object') ? toolResult : { result: "ok" };
               const isQuestionTool = (
                 (call.name === 'write_chalkboard' || call.name === 'write_chalkboardd') &&
                 (call.args?.action === 'draw_question' || call.args?.action === 'draw_exam_question')
               ) || call.name === 'draw_question' || call.name === 'draw_exam_question';

               const fnResponse: any = {
                  id: call.id,
                  name: call.name,
                  response: {
                    ...responsePayload,
                    scheduling: isQuestionTool
                      ? FunctionResponseScheduling.SILENT
                      : (!isExtendedThinking ? FunctionResponseScheduling.WHEN_IDLE : undefined)
                  },
               };
               responses.push(fnResponse);
             }
             if (responses.length > 0 && this.session) {
               try {
                 this.session.sendToolResponse({ functionResponses: responses });
               } catch (e) {
                 console.warn("[GeminiLive] Failed to send tool response:", e);
               }
             }
           }

           if (!content) return;

           if (content.interrupted) {
             this.isModelGenerating = false;
             this.turnToolCallsExecuted = 0;
             this.turnEmittedAudio = false;
             this.silentTurnNudgeCount = 0;
             this.pendingBoardContext = null;
             this.callbacks.onInterrupted();
             return;
           }
           
           // Transcripts extraction
           if (content.inputTranscription && content.inputTranscription.text) {
             this.callbacks.onTranscript(content.inputTranscription.text, "user");
           }
           if (content.inputTranscription && content.inputTranscription.parts) {
             for (const part of content.inputTranscription.parts) {
                 if (part.text) {
                     this.callbacks.onTranscript(part.text, "user");
                 }
             }
           }
           
           let hasTeacherTranscript = false;
           if (content.outputTranscription && content.outputTranscription.text) {
             const cleaned = this.extractAndExecuteEmbeddedToolCalls(content.outputTranscription.text);
              if (cleaned) this.callbacks.onTranscript(cleaned, "teacher");
             hasTeacherTranscript = true;
           } else if (content.outputTranscription && content.outputTranscription.parts) {
             for (const part of content.outputTranscription.parts) {
               if (part.text) {
                 const cleaned = this.extractAndExecuteEmbeddedToolCalls(part.text);
                 if (cleaned) {
                   this.callbacks.onTranscript(cleaned, "teacher");
                   hasTeacherTranscript = true;
                 }
               }
             }
           }

           // Incoming audio, video frames, or text model turns
           if (content.modelTurn && content.modelTurn.parts) {
             this.isModelGenerating = true;
             for (const part of content.modelTurn.parts) {
               if (part.inlineData && part.inlineData.data) {
                 this.turnEmittedAudio = true;
                 this.silentTurnNudgeCount = 0;
                 const mime = part.inlineData.mimeType || "audio/pcm;rate=24000";
                 if (mime.startsWith("video/") || mime.startsWith("image/")) {
                   // Native Gemini 3.8 Live Avatar video frame streaming
                   this.callbacks.onVideoData?.(part.inlineData.data, mime);
                 } else {
                   const pcm16 = this.base64ToInt16(part.inlineData.data);
                   this.callbacks.onAudioData(pcm16, 24000); // SDK returns 24kHz
                 }
               }
               // Deliver model turn text if it contains chalkboard bracket tags or if no audio transcript was emitted
               if (part.text) {
                 const cleaned = this.extractAndExecuteEmbeddedToolCalls(part.text);
                 if (cleaned && (part.text.includes("[") || part.text.includes("write_chalkboard") || part.text.includes("write_chalkboardd") || !hasTeacherTranscript)) {
                   this.callbacks.onTranscript(cleaned, "teacher");
                 }
               }
               if (part.functionCall) {
                 const call = part.functionCall;
                 if (call.id && !this.executedToolCallIds.has(call.id)) {
                   this.turnToolCallsExecuted++;
                   const allowed = this.pedagogicalStateManager.handleToolCall(call.name, call.args);
                   let toolResult: any;
                   if (!allowed) {
                     toolResult = { result: "Progression blocked: complete checkpoint first" };
                   } else {
                     toolResult = this.handleSingleToolCall(call.name, call.args || {}, call.id);
                   }
                   const isExtendedThinking = this.model.includes("extended-thinking");
                   const responsePayload = (toolResult && typeof toolResult === 'object') ? toolResult : { result: "ok" };
                   const isQuestionTool = (
                     (call.name === 'write_chalkboard' || call.name === 'write_chalkboardd') &&
                     (call.args?.action === 'draw_question' || call.args?.action === 'draw_exam_question')
                   ) || call.name === 'draw_question' || call.name === 'draw_exam_question';

                   const fnResponse: any = {
                     id: call.id,
                     name: call.name,
                     response: {
                       ...responsePayload,
                       scheduling: isQuestionTool
                         ? FunctionResponseScheduling.SILENT
                         : (!isExtendedThinking ? FunctionResponseScheduling.WHEN_IDLE : undefined)
                     },
                   };

                   try {
                     this.session?.sendToolResponse({
                       functionResponses: [fnResponse],
                     });
                   } catch (e) {
                     console.warn(`[GeminiLive] Failed to send tool response for ${call.name}:`, e);
                   }
                 }
               }
             }
           }

           const currentStatus = content.interactionStatus || msg.interactionStatus;
           const isTurnDone = Boolean(content.turnComplete || currentStatus === "IDLE");
           if (isTurnDone && currentStatus !== "IN_PROGRESS") {
             this.isModelGenerating = false;
             if (this.turnToolCallsExecuted > 0 && !this.turnEmittedAudio && this.isConnected && !this.isManuallyClosed && this.silentTurnNudgeCount < 2) {
               this.silentTurnNudgeCount++;
               const isQuestionTool = this.lastExecutedToolAction === "draw_question" || this.lastExecutedToolAction === "draw_exam_question";
               const nudgePrompt = isQuestionTool
                 ? "Please read the question out loud to the student, then stop speaking and wait silently for their answer. Do NOT reveal or solve the question!"
                 : "Please continue speaking and explaining out loud now.";
               console.log(`[GeminiLive] Turn ended with chalkboard tool calls (${this.lastExecutedToolAction}) but zero audio. Prompting spoken delivery automatically...`);
               try {
                 this.session?.sendClientContent({
                   turns: [{ role: "user", parts: [{ text: nudgePrompt }] }],
                   turnComplete: true,
                 });
               } catch {}
             }
             this.turnToolCallsExecuted = 0;
             this.turnEmittedAudio = false;
             this.callbacks.onTurnComplete();
             this.pendingBoardContext = null;
           }
        },
        onerror: (err: any) => {
          if (!this.isManuallyClosed) {
            console.error("[GeminiLive] Connection error:", err);
            this.callbacks.onError(new Error(err.message || "Connection to Gemini Live was interrupted."));
          }
        },
        onclose: (event: any) => {
          this.isConnected = false;
          this.hasSentKickoff = false;
          console.log(`[GeminiLive] WebSocket closed: code=${event?.code}, reason=${event?.reason || '(none)'}, wasClean=${event?.wasClean}`);
          if (event?.reason?.toLowerCase().includes("thinking") || (event?.code === 1007 && event?.reason?.includes("Thinking"))) {
            console.warn(`[GeminiLive] WebSocket closed due to unsupported thinking config (${event?.reason}). Permanently clearing thinkingLevel for all reconnects.`);
            this.thinkingLevel = "";
          }
          if (!this.isManuallyClosed) {
             this.callbacks.onClose(event as CloseEvent);
          }
          this.session = null;
        }
      };

      try {
        this.session = await this.ai.live.connect({
          model: this.model,
          config: liveConfig,
          callbacks: sessionCallbacks,
        });
        // Generic kickoff removed. The session will now await the user-provided dynamic kickoff.
        if (!this.hasSentKickoff) {
          // No hardcoded greeting.
        }
      } catch (connectError: any) {
        if (liveConfig.thinkingConfig && !this.model.includes("extended-thinking")) {
          console.warn("[GeminiLive] Thinking config rejected by endpoint. Instant fallback without thinkingConfig for zero-latency audio streaming:", connectError);
          delete liveConfig.thinkingConfig;
          try {
            this.session = await this.ai.live.connect({
              model: this.model,
              config: liveConfig,
              callbacks: sessionCallbacks,
            });
            return;
          } catch (noThinkingErr) {
            console.warn("[GeminiLive] Standard connection retry with thinking disabled failed, cascading to next fallback:", noThinkingErr);
          }
        }
        if (this.model.includes("extended-thinking")) {
          console.warn("[GeminiLive] Extended thinking live model unavailable or rejected. Self-healing fallback to standard gemini-3.8-live:", connectError);
          this.model = "gemini-3.8-live";
          delete liveConfig.thinkingConfig;
          try {
            this.session = await this.ai.live.connect({
              model: this.model,
              config: liveConfig,
              callbacks: sessionCallbacks,
            });
          } catch (retryError: any) {
            if (this.avatarConfig) {
              console.warn("[GeminiLive] Native video avatar modality rejected. Fallback to audio stream:", retryError);
              this.avatarConfig = undefined;
              liveConfig.responseModalities = ["AUDIO" as any];
              delete liveConfig.avatarConfig;
              this.session = await this.ai.live.connect({
                model: this.model,
                config: liveConfig,
                callbacks: sessionCallbacks,
              });
            } else {
              throw retryError;
            }
          }
        } else if (this.avatarConfig) {
          console.warn("[GeminiLive] Native video avatar modality rejected or unsupported by current endpoint/credentials. Self-healing fallback to high-fidelity audio stream:", connectError);
          this.avatarConfig = undefined;
          liveConfig.responseModalities = ["AUDIO" as any];
          delete liveConfig.avatarConfig;
          this.session = await this.ai.live.connect({
            model: this.model,
            config: liveConfig,
            callbacks: sessionCallbacks,
          });
        } else {
          throw connectError;
        }
      }

      this.isConnected = true;
      console.log("[GeminiLive] Handshake verified and session ready.");
      this.callbacks.onSetupComplete();

      if (this.pendingKickoffText && !this.hasSentKickoff) {
        setTimeout(() => this.sendKickoff(this.pendingKickoffText!), 500);
      }
    } catch (err: any) {
      console.error("[GeminiLive] Connection error during setup:", err);
      this.callbacks.onError(new Error(`Connection failed: ${err.message}`));
    }
  }

  public sendKickoff(text: string): void {
    if (this.hasSentKickoff) {
      console.log("[GeminiLive] Kickoff already dispatched, ignoring repeat.");
      return;
    }
    if (!this.session) {
      console.log("[GeminiLive] Queued kickoff prompt while session connects.");
      this.pendingKickoffText = text;
      return;
    }
    // Proactive Greeting and Topic Writing
    const topicHeading = text.includes('Topic:')
      ? text.split('Topic:')[1]?.split('\n')[0]?.trim()
      : text.split(':')[0]?.replace(/^\[.*?\]/, '').trim() || 'Learning Session';
    this.handleSingleToolCall("write_chalkboard", { action: "draw_title", content: `Topic: ${topicHeading}` });

    // Use sendClientContent with a user-role turn to trigger the model to respond with audio speech.
    // If text already contains full kickoff instructions (from page.tsx), use it directly.
    const kickoffInstruction = (text.includes('[SESSION START') || text.includes('Speak FIRST'))
      ? text
      : `The student has just joined the class. The topic is: ${text}. Begin the class NOW by warmly greeting the student and immediately starting to teach. You MUST speak your greeting and explanation aloud (produce audio) AND write key points on the chalkboard simultaneously. Start speaking immediately.`;

    try {
      this.session.sendClientContent({
        turns: [{ role: "user", parts: [{ text: kickoffInstruction }] }],
        turnComplete: true,
      });
      console.log("[GeminiLive] Kickoff instruction dispatched via sendClientContent.");
    } catch (err) {
      console.error("[GeminiLive] Failed to send kickoff via sendClientContent:", err);
      // Fallback: try sendRealtimeInput with text
      try {
        this.session.sendRealtimeInput({ text: kickoffInstruction });
        console.log("[GeminiLive] Kickoff fallback dispatched via sendRealtimeInput.");
      } catch (fallbackErr) {
        console.error("[GeminiLive] Failed to send kickoff via sendRealtimeInput:", fallbackErr);
      }
    }
    this.hasSentKickoff = true;
  }

  private lastSentBoardContextHash: string = '';
  private latestBoardState: string = '';

  public sendTextMessage(text: string): void {
    if (!this.session || !text?.trim()) return;
    try {
      let messageToSend = text.trim();
      const currentStage = this.pedagogicalStateManager?.getStage?.() || 'REAL_LIFE_INTUITION';
      if (!messageToSend.includes('[TEACHING STATE') && !messageToSend.includes('[SESSION START')) {
        messageToSend = `[TEACHING STATE: Stage = ${currentStage}]\n${messageToSend}`;
      }
      if (
        this.latestBoardState &&
        !messageToSend.includes('[CURRENT_BOARD_STATE]') &&
        this.lastSentBoardContextHash !== this.latestBoardState
      ) {
        this.lastSentBoardContextHash = this.latestBoardState;
        messageToSend = `[CURRENT_BOARD_STATE]\n${this.latestBoardState}\n[CONTINUATION MANDATE: The notes and diagrams above are ALREADY VISIBLE on the student's chalkboard. Continue teaching directly without duplicating.]\n\n${messageToSend}`;
      }

      console.log("[GeminiLive] Dispatching text turn to model:", messageToSend.slice(0, 100));
      this.session.sendClientContent({
        turns: [
          {
            role: "user",
            parts: [{ text: messageToSend }],
          },
        ],
        turnComplete: true,
      });
    } catch (err) {
      console.warn("[GeminiLive] Failed to send text message via sendClientContent, trying sendRealtimeInput fallback:", err);
      try {
        this.session.sendRealtimeInput({ text: text.trim() });
      } catch (fallbackErr) {
        console.warn("[GeminiLive] Failed to send text fallback:", fallbackErr);
      }
    }
  }

  public sendAudioChunk(base64Chunk: string): void {
    if (!this.session) return;
    try {
      this.session.sendRealtimeInput({
        audio: {
          mimeType: "audio/pcm;rate=16000",
          data: base64Chunk,
        }
      });
    } catch (err) {
      console.warn("Failed to send audio chunk", err);
    }
  }

  public sendAudioStreamEnd(): void {
    if (!this.session) return;
    try {
      this.session.sendRealtimeInput({ audioStreamEnd: true });
    } catch (err) {
      console.warn("Failed to send audioStreamEnd", err);
    }
  }

  public sendTurnComplete(): void {
    if (!this.session) return;
    try {
      this.session.sendClientContent({ turnComplete: true });
    } catch (err) {
      console.warn("Failed to send turnComplete", err);
    }
  }

  public sendBoardContext(summaryText: string): void {
    if (!summaryText?.trim()) return;
    // Block disruptive system notices from being injected as user turns
    if (summaryText.includes('[SYSTEM NOTICE:') || summaryText.includes('SYSTEM NOTICE')) {
      return;
    }
    const trimmed = summaryText.trim();
    this.latestBoardState = trimmed;
  }

  private base64ToInt16(base64: string): Int16Array {
    const binary = window.atob(base64);
    const bytes = new Uint8Array(binary.length);
    for (let i = 0; i < binary.length; i++) {
      bytes[i] = binary.charCodeAt(i);
    }
    return new Int16Array(bytes.buffer);
  }

  public disconnect(): void {
    this.isManuallyClosed = true;
    this.isConnected = false;
    this.hasSentKickoff = false;
    this.pendingKickoffText = null;
    if (this.session) {
      try {
        this.session.close();
      } catch (err) {}
      this.session = null;
    }
  }
}
