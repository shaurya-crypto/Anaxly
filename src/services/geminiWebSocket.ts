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
  onChalkboardToolCall?: (action: string, content: any, color?: string) => any;
  onVisualAction?: (action: string, params: Record<string, any>) => void;
  onGetBoardContent?: () => string;
  onHighlightText?: (text: string, target?: string, color?: string) => void;
  onGoAway?: (timeLeftMs?: number) => void;
  onSessionResumptionUpdate?: (handle: string, resumable: boolean) => void;
  onPlanTeachingMove?: (args: {
    questionOrTopic: string;
    studentMessage: string;
    struggleCount?: number;
  }) => Promise<any>;
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
  private turnTeacherTranscriptText: string = "";
  private lastExecutedToolAction: string | null = null;
  private lastTurnHadBlockedToolCall: boolean = false;
  private suppressedSilenceNudgeTurnAt: number = 0;
  private silentTurnNudgeCount: number = 0;
  private silentBoardNudgeCount: number = 0;
  private resumptionHandle: string | null = null;
  private goAwayTriggered: boolean = false;
  private isStudentMicMuted: boolean = false;
  private awaitingStudentAnswer: boolean = false;
  private recentTranscriptHistory: Array<{ sender: "user" | "teacher"; text: string }> = [];

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
      resumptionHandle?: string | null;
    }
  ) {
    this.apiKey = authTokenOrApiKey;
    this.callbacks = callbacks;
    this.pedagogicalStateManager = options?.pedagogicalStateManager || new PedagogicalStateManager();
    this.resumptionHandle = options?.resumptionHandle ?? null;
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
    this.systemInstruction = options?.systemInstruction || `You are a warm, sharp 1-on-1 faculty mentor at a live chalkboard for Classes 9 to 12 (CBSE, ICSE, IB).
1. Human Voice & Short Turns: Speak simply and naturally in Hinglish, Hindi, or English as requested. Keep each spoken turn to 2 or 3 plain sentences while writing or plotting on the board. Skip textbook monologues.
2. Everyday Examples First: Ground abstract ideas in things students know, such as cricket throws, bike braking, mobile data, or kitchen habits.
3. Subject Style:
   - Mathematics: Never recite dictionary definitions or ask "did you understand the definition?". Teach the intuition, theorem, or method, solve ONLY the active chapter's textbook exercises clearly with matching chapter/question numbers (never invent other chapters' exercises), and ask "Did you follow that concept?".
   - Science (Physics, Chemistry, Biology): Start with an everyday observation, explain the mechanism, state the exact law with SI units, then solve step-by-step numericals.
4. Write As You Talk: Write 1 or 2 crisp lines per spoken micro-turn instead of dumping a full solution at once. Start each concept with draw_title, progress step-by-step (Given -> Formula -> Substitution -> Step-by-Step Calculation -> Boxed Answer), and use Unicode math (x², x₁, y₁, θ, ×, ÷, √, ±) with no raw *, **, ^, or //. For 2D distance, always write d = √[(x₂ - x₁)² + (y₂ - y₁)²].
5. Visual Escalation: Begin each visual concept with 1 clean diagram via search_and_show_image or plot_mathematical_graph. If the student is confused, asks again, or wants a video, call plan_teaching_move for a verified analogy/graph move and unlock search_and_show_video, draw_shape, draw_table, or draw_flowchart. Reference NCERT pages in the Side Book Viewer when citing textbook figures.
6. Hard Stop & Doubt Lock: Write every checkpoint question via draw_question, then stop speaking and wait silently for the student. Never solve your own question or evaluate it unless the student replies or asks you to solve it. Whenever the student speaks or raises a doubt, stop immediately, address their question in the simplest words with board visuals, and never call concept_completed until they confirm.`;
    this.ai = new GoogleGenAI({
      apiKey: this.apiKey,
      httpOptions: { apiVersion: "v1alpha" },
    });
  }

  public getResumptionHandle(): string | null {
    return this.resumptionHandle;
  }

  public setResumptionHandle(handle: string | null): void {
    this.resumptionHandle = handle;
  }

  public setStudentMicMuted(muted: boolean): void {
    this.isStudentMicMuted = Boolean(muted);
  }

  public setAwaitingStudentAnswer(awaiting: boolean): void {
    this.awaitingStudentAnswer = Boolean(awaiting);
  }

  public isAwaitingStudentAnswer(): boolean {
    return this.awaitingStudentAnswer;
  }

  public setRecentTranscriptHistory(turns: Array<{ sender: "user" | "teacher"; text: string }>): void {
    this.recentTranscriptHistory = Array.isArray(turns) ? turns.slice(-6) : [];
  }

  private isSocketOpen(): boolean {
    if (!this.session || !this.isConnected || this.isManuallyClosed) {
      return false;
    }
    const wsReadyState = (this.session as any)?.conn?.ws?.readyState;
    if (typeof wsReadyState === "number" && wsReadyState !== 1) {
      return false;
    }
    return true;
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

  private async handleSingleToolCall(name: string, args: any, callId?: string): Promise<any> {
    const isBoardWrite = ['write_chalkboard', 'write_chalkboardd', 'write_board', 'chalkboard', 'whiteboard', 'draw_chalkboard', 'draw_board'].includes(name);
    const effectiveAction = isBoardWrite && args?.action ? String(args.action).toLowerCase() : name.toLowerCase();
    const rawContentText = typeof args === 'string'
      ? args
      : String(args?.content ?? args?.text ?? args?.answer ?? args?.step ?? '');

    if (effectiveAction === 'draw_question' || effectiveAction === 'question' || effectiveAction === 'draw_exam_question' || effectiveAction === 'exam_question') {
      if (
        this.awaitingStudentAnswer &&
        (effectiveAction === 'draw_exam_question' || effectiveAction === 'exam_question')
      ) {
        console.warn(`[GeminiLive] Answer Gate blocked stacked ${effectiveAction} while awaiting student response (muted=${this.isStudentMicMuted}).`);
        return {
          result: "blocked",
          status: "blocked_waiting_for_student",
          reason: "STOP! Wait for the student to answer the current question before posting another question.",
        };
      }
      this.awaitingStudentAnswer = true;
    } else if (this.awaitingStudentAnswer) {
      const isPrematureSelfSolve =
        [
          'draw_step', 'step', 'board_step',
          'draw_answer_verdict', 'answer_verdict', 'verdict',
          'draw_numerical', 'numerical', 'worked_example', 'solve', 'solve_step_by_step_numerical',
          'concept_completed', 'concept_done', 'next_concept', 'advance_concept', 'conclude_and_open_quiz',
        ].includes(effectiveAction) ||
        (['draw_highlight_box', 'highlight_box', 'box'].includes(effectiveAction) && /\b(?:answer|result|hence\s*proved|solution)\b/i.test(rawContentText));
      if (isPrematureSelfSolve) {
        console.warn(`[GeminiLive] Answer Gate blocked premature ${effectiveAction} while awaiting student response (muted=${this.isStudentMicMuted}).`);
        return {
          result: "blocked",
          status: "blocked_waiting_for_student",
          reason: "STOP! You posed a question on the board and the student has NOT responded yet. Do NOT write solution steps (Given/Formula/Substitution/Answer), evaluate it, or advance concepts. Wait silently until the student replies or asks you to solve it.",
        };
      }
    }

    if (!this.pedagogicalStateManager.handleToolCall(name, args)) {
      return { result: "Progression blocked: finish current stage first" };
    }
    if (callId) {
      if (this.executedToolCallIds.has(callId)) {
        return { result: "duplicate_ignored" };
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
      return { result: "ok", deduplicated: true };
    }
    this.lastExecutedToolCalls.set(callSignature, now);
    if (this.lastExecutedToolCalls.size > 200) {
      for (const [k, t] of this.lastExecutedToolCalls.entries()) {
        if (now - t > 60000) this.lastExecutedToolCalls.delete(k);
      }
    }
    this.lastExecutedToolAction = name;
    this.silentBoardNudgeCount = 0;

    if (name === "get_board_content" || name === "read_board_content" || name === "get_board_state") {
      const boardState = this.callbacks.onGetBoardContent?.() || "";
      return {
        result: "ok",
        chalkboard_content: boardState || "Digital chalkboard is active. No notes written yet.",
      };
    }

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
        const res = this.callbacks.onChalkboardToolCall?.("draw_numerical", numericalPayload);
        return (res && typeof res === 'object') ? res : { result: "ok" };
      } else if (action === "highlight_text" || action === "highlight_word" || action === "highlight_sentence") {
        this.callbacks.onHighlightText?.(textContent, "both", color || "amber");
        return { result: "ok" };
      } else {
        const res = this.callbacks.onChalkboardToolCall?.(action, textContent, color);
        return (res && typeof res === 'object') ? res : { result: "ok" };
      }
    } else if (name === "highlight_text" || name === "highlight_word" || name === "highlight_sentence") {
      const textToHighlight = args.text || args.content || args.word || args.sentence || (typeof args === "string" ? args : "");
      const target = args.target || "both";
      const color = args.color || "amber";
      this.callbacks.onHighlightText?.(textToHighlight, target, color);
      return { result: "ok" };
    } else if (name === "execute_visual_action") {
      const action = args.action || "";
      const parameters = args.parameters || {};
      this.callbacks.onVisualAction?.(action, parameters);
      return { result: "ok" };
    } else if (name === "plot_mathematical_graph") {
      const res = this.callbacks.onChalkboardToolCall?.("draw_graph", args);
      if (res && typeof (res as any).then === "function") {
        return await res;
      }
      return (res && typeof res === 'object') ? res : { result: "ok" };
    } else if (name === "open_interactive_simulation") {
      const sceneType = args.sceneType || "geometry";
      const parameters = args.parameters || {};
      const title = args.title || parameters.title;
      this.callbacks.onVisualAction?.("SHOW_SCENE", { sceneType, title, ...parameters });
      return { result: "ok" };
    } else if (name === "update_interactive_simulation") {
      const parameters = args.parameters || args;
      const title = args.title || parameters.title;
      this.callbacks.onVisualAction?.("UPDATE_SCENE", { title, ...parameters });
      return { result: "ok" };
    } else if (name === "draw_shape") {
      const res = this.callbacks.onChalkboardToolCall?.("draw_shape", args, args.color);
      return (res && typeof res === 'object') ? res : { result: "ok" };
    } else if (name === "solve_step_by_step_numerical") {
      const res = this.callbacks.onChalkboardToolCall?.("draw_numerical", args);
      return (res && typeof res === 'object') ? res : { result: "ok" };
    } else if (name === "render_svg_diagram") {
      const title = args.title || "Educational Diagram";
      const svg = args.svg || "";
      const caption = args.caption || "";
      const what = args.what || "";
      this.callbacks.onChalkboardToolCall?.("render_svg_diagram", { title, svg, caption, what });
      return { result: "ok", title };
    } else if (name === "search_and_show_image") {
      const query = args.query || args.searchQuery || args.q || "";
      const title = args.title || query || "Scientific Diagram";
      const caption = args.caption || "";
      if (query && typeof window !== "undefined") {
        const controller = new AbortController();
        const timer = setTimeout(() => controller.abort(), 10500);
        try {
          const res = await fetch("/api/diagram/search-image", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            signal: controller.signal,
            body: JSON.stringify({ query }),
          });
          const data = await res.json();
          const candidateImages = data.images || [];
          let displayed = false;
          let skippedReason: string | null = null;
          for (const img of candidateImages) {
            if (!img?.url) continue;
            try {
              const check = await fetch(`/api/diagram/proxy?dataUrl=true&url=${encodeURIComponent(img.url)}`, {
                signal: controller.signal,
              });
              if (check.ok) {
                const pData = await check.json();
                if (pData.success && pData.dataURL) {
                  const drawRes = this.callbacks.onChalkboardToolCall?.("draw_image", {
                    url: pData.dataURL,
                    title: title || img.title,
                    caption: caption || img.description || "",
                  });
                  if (drawRes && typeof drawRes === "object" && drawRes.status === "skipped") {
                    skippedReason = drawRes.reason || "Image already displayed on chalkboard.";
                    break;
                  }
                  displayed = true;
                  break;
                }
              }
            } catch {
              // Failover to next candidate image
            }
          }
          clearTimeout(timer);
          if (skippedReason) {
            return { result: "skipped", status: "skipped", reason: skippedReason, title };
          }
          if (displayed) {
            return { result: "ok", status: "displayed", title };
          }
          this.callbacks.onChalkboardToolCall?.("render_svg_diagram", { title, caption });
          return { result: "ok", status: "fallback_used", fallback_used: "render_svg_diagram", title };
        } catch (err) {
          clearTimeout(timer);
          console.warn("[GeminiLive] search_and_show_image error:", err);
          this.callbacks.onChalkboardToolCall?.("render_svg_diagram", { title, caption });
          return { result: "fallback", status: "fallback_used", fallback_used: "render_svg_diagram", title };
        }
      }
      return { result: "skipped", reason: "missing_query" };
    } else if (name === "search_and_show_video") {
      const query = args.query || args.searchQuery || args.q || "";
      const title = args.title || query || "Demonstration Video";
      const description = args.description || args.caption || "";
      if (query && typeof window !== "undefined") {
        const controller = new AbortController();
        const timer = setTimeout(() => controller.abort(), 5000);
        try {
          const res = await fetch("/api/diagram/search-video", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            signal: controller.signal,
            body: JSON.stringify({ query }),
          });
          const data = await res.json();
          clearTimeout(timer);
          const firstVid = data.videos?.[0];
          if (firstVid?.url) {
            this.callbacks.onChalkboardToolCall?.("draw_video", {
              url: firstVid.url,
              title: title || firstVid.title,
              description: description || firstVid.description || "",
              mimeType: firstVid.mimeType || "video/mp4",
            });
            return { result: "ok", status: "displayed", title: title || firstVid.title };
          } else {
            this.callbacks.onChalkboardToolCall?.("draw_video", { url: "", title, description });
            return { result: "fallback", status: "no_direct_video_found", title };
          }
        } catch (err) {
          clearTimeout(timer);
          console.warn("[GeminiLive] search_and_show_video error:", err);
          this.callbacks.onChalkboardToolCall?.("draw_video", { url: "", title, description });
          return { result: "fallback", status: "video_search_error", title };
        }
      }
      return { result: "skipped", reason: "missing_query" };
    } else if (name === "plan_teaching_move") {
      const questionOrTopic = String(args.questionOrTopic || args.topic || args.concept || "").trim();
      const studentMessage = String(args.studentMessage || args.doubt || args.attempt || "").trim();
      const struggleCount = typeof args.struggleCount === "number" ? args.struggleCount : undefined;
      if (this.callbacks.onPlanTeachingMove) {
        try {
          const moveResult = await this.callbacks.onPlanTeachingMove({
            questionOrTopic: questionOrTopic || "Current concept",
            studentMessage: studentMessage || "Student needs a clearer intuitive explanation",
            struggleCount,
          });
          return moveResult && typeof moveResult === "object"
            ? { result: "ok", ...moveResult }
            : { result: "ok", plan: moveResult };
        } catch (err: any) {
          console.warn("[GeminiLive] plan_teaching_move error:", err);
          return { result: "fallback", error: err?.message || "Think co-pilot unavailable" };
        }
      }
      return { result: "skipped", reason: "no_think_handler" };
    } else if (name === "conclude_and_open_quiz") {
      if (args.summary) {
        this.callbacks.onChalkboardToolCall?.("chapter_summary", args.summary);
      }
      this.callbacks.onChalkboardToolCall?.("open_quiz", args.summary || "10-MCQ Diagnostic Evaluation");
      return { result: "ok" };
    } else if (name === "close_graph" || ((name === "write_chalkboard" || name === "write_chalkboardd") && args?.action === "close_graph")) {
      this.callbacks.onChalkboardToolCall?.("close_graph", "");
      return { result: "ok" };
    } else if (name === "concept_completed" || name === "next_concept" || name === "advance_concept") {
      const cName = args.conceptName || args.concept || (typeof args === "string" ? args : "");
      const res = this.callbacks.onChalkboardToolCall?.("concept_done", cName);
      return (res && typeof res === 'object') ? res : { result: "ok" };
    } else if (name === "concept_focus" || name === "focus_concept") {
      const cName = args.conceptName || args.concept || (typeof args === "string" ? args : "");
      this.callbacks.onChalkboardToolCall?.("concept_focus", cName);
      return { result: "ok" };
    } else {
      const res = this.callbacks.onChalkboardToolCall?.(name, typeof args === 'string' ? args : JSON.stringify(args));
      return (res && typeof res === 'object') ? res : { result: "ok" };
    }
  }

  public async connect(kickoffPrompt?: string): Promise<void> {
    if (this.session) return;
    this.isManuallyClosed = false;
    this.hasSentKickoff = false;
    this.goAwayTriggered = false;
    if (kickoffPrompt) {
      this.pendingKickoffText = kickoffPrompt;
    }

    try {
      console.log(`[GeminiLive] Connecting session with model: ${this.model}, voice: ${this.voiceName}, enableFunctionCalling: ${this.enableFunctionCalling}, resuming: ${Boolean(this.resumptionHandle)}`);

      const responseModalities =
        this.model === "gemini-3.8-live" || !this.avatarConfig
          ? ["AUDIO" as any]
          : ["VIDEO" as any, "AUDIO" as any];

      const liveConfig: any = {
        responseModalities,
        systemInstruction: { parts: [{ text: this.systemInstruction }] },
        sessionResumption: this.resumptionHandle
          ? { handle: this.resumptionHandle }
          : {},
        realtimeInputConfig: {
          automaticActivityDetection: {
            disabled: false,
            startOfSpeechSensitivity: StartSensitivity.START_SENSITIVITY_LOW,
            endOfSpeechSensitivity: EndSensitivity.END_SENSITIVITY_LOW,
            prefixPaddingMs: 200,
            silenceDurationMs: 1100,
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
        outputAudioTranscription: {},
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
                description: "CRITICAL MULTI-TYPE GRAPH ENGINE (MATHS, PHYSICS, SCIENCE & STATISTICS): Plot interactive mathematical functions, kinematics curves (v-t, s-t, a-t), Ohm's law (V-I), thermodynamics (P-V), statistical bar graphs & histograms, pie charts, multi-point line graphs, shaded color regions, physics vectors, geometric constructions (circles, triangles, polygons, segments), and custom coordinate texts directly on the whiteboard canvas. Call this tool whenever a question asks to plot or solve graphically, whenever teaching coordinate geometry, circles passing through points, triangles, distances, statistics, or whenever ANY visual line, curve, chart, or shape on a grid helps explain a concept! Supports: (1) functions formula/formulas; (2) bounded line segments with explicit lengths and stopping points; (3) critical coordinate points with labels; (4) statistical bar graphs & histograms via 'bars' with custom fillColor/fillOpacity; (5) physics vectors via 'vectors'; (6) geometric figures on Cartesian plane via 'polygons' and 'circles' with fillColor/fillOpacity; (7) multiple freeform text annotations via 'texts'; (8) pie/donut charts via 'pies'; (9) discrete multi-point line graphs with optional area color fill via 'lineSeries'; (10) shaded color regions under or between curves via 'shadedRegions'. MANDATE: When plotting lines/curves, ALWAYS provide actual points (intercepts, intersection, roots, vertex, endpoints) and segments if bounded. Use render_svg_diagram or search_and_show_image only for physical lab apparatus, ray optics mirrors/lenses, or biological anatomy. STRICT ZERO MEANINGLESS GRAPH INVARIANT: NEVER output a meaningless default line y = x without points, segments, or purpose. DEDUPLICATION RULE: The graph engine automatically displays coordinates for all items in points. Do NOT repeat coordinate labels in texts.",
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
                      description: "Statistical bar graph or histogram items with optional custom colors, e.g. ['{\"label\": \"Maths\", \"height\": 85, \"color\": \"#2563EB\", \"fillColor\": \"#60A5FA\", \"fillOpacity\": 0.7}'] or simple delimited string 'Maths: 85 | Science: 92'.",
                    },
                    vectors: {
                      type: Type.ARRAY,
                      items: { type: Type.STRING },
                      description: "Physics vectors and directional arrows, e.g. ['{\"tail\": [0, 0], \"tip\": [4, 3], \"label\": \"F1 = 5 N\"}'] or transition strings '(0,0) -> (4,3) [F1]'.",
                    },
                    polygons: {
                      type: Type.ARRAY,
                      items: { type: Type.STRING },
                      description: "Cartesian polygons like triangles or quadrilaterals with custom color filling, e.g. ['{\"points\": [[1,1],[5,1],[3,5]], \"label\": \"Triangle ABC\", \"color\": \"#7C3AED\", \"fillColor\": \"#DDD6FE\", \"fillOpacity\": 0.4}'].",
                    },
                    circles: {
                      type: Type.ARRAY,
                      items: { type: Type.STRING },
                      description: "Circles in Cartesian space with custom fill colors, e.g. ['{\"center\": [0, 0], \"radius\": 4, \"label\": \"Circle r=4\", \"color\": \"#2563EB\", \"fillColor\": \"#BFDBFE\", \"fillOpacity\": 0.3}'].",
                    },
                    texts: {
                      type: Type.ARRAY,
                      items: { type: Type.STRING },
                      description: "Multiple custom text annotations placed anywhere on the graph, e.g. ['{\"x\": 2, \"y\": 5, \"text\": \"Maximum Altitude\"}'].",
                    },
                    pies: {
                      type: Type.ARRAY,
                      items: { type: Type.STRING },
                      description: "Pie / Donut chart slices with custom colors, e.g. ['{\"label\": \"Science\", \"value\": 40, \"color\": \"#2563EB\"}', '{\"label\": \"Maths\", \"value\": 35, \"color\": \"#16A34A\"}', '{\"label\": \"English\", \"value\": 25, \"color\": \"#D97706\"}'].",
                    },
                    lineSeries: {
                      type: Type.ARRAY,
                      items: { type: Type.STRING },
                      description: "Discrete multi-point line graph series with optional area color filling, e.g. ['{\"label\": \"Velocity\", \"points\": [[0,0],[2,10],[4,20]], \"color\": \"#2563EB\", \"fillColor\": \"#93C5FD\", \"fillOpacity\": 0.25, \"filled\": true}'].",
                    },
                    shadedRegions: {
                      type: Type.ARRAY,
                      items: { type: Type.STRING },
                      description: "Shaded color regions under a curve or between two curves over a domain, e.g. ['{\"upperFormula\": \"x^2\", \"lowerFormula\": \"0\", \"domain\": [0, 3], \"fillColor\": \"#16A34A\", \"fillOpacity\": 0.25, \"label\": \"Area\"}'].",
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
                description: "Draw custom 2D or 3D geometric shapes (rectangle, square, circle, ellipse, triangle, right_triangle, parallelogram, trapezium, cylinder, cone, sphere, hemisphere, prism, pyramid, cube, cuboid, polygon, number_line, angle_arc, line, arrow) on the whiteboard with complete control over width, height, radius, labels, and colors.",
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
                        "parallelogram",
                        "trapezium",
                        "cylinder",
                        "cone",
                        "sphere",
                        "hemisphere",
                        "prism",
                        "pyramid",
                        "cube",
                        "cuboid",
                        "polygon",
                        "number_line",
                        "angle_arc",
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
              {
                name: "plan_teaching_move",
                description: "DIAGNOSTIC CO-PILOT: Call whenever the student is confused, gives a wrong answer, asks a doubt, or studies Class 10-12 multi-step proofs/numericals. Consults textbook RAG, prerequisite links, and mathjs verification to return an adaptive Teaching Move (INTUITION_ANALOGY, TINY_NUMBER_TEST, ANIMATED_VISUAL_GRAPH, PREREQUISITE_REPAIR, or STEP_BY_STEP_COACH) with verified numbers, chalkboard steps, and optional graph coordinates.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    questionOrTopic: {
                      type: Type.STRING,
                      description: "The current concept, theorem, or exercise question being taught.",
                    },
                    studentMessage: {
                      type: Type.STRING,
                      description: "What the student just said, asked, or answered.",
                    },
                    struggleCount: {
                      type: Type.NUMBER,
                      description: "How many times the student has been stuck on this concept (0, 1, 2...).",
                    },
                  },
                  required: ["questionOrTopic", "studentMessage"],
                },
              },
            ],
          },
        ];
      }

      const dispatchToolCalls = async (calls: any[]) => {
        const responses: any[] = [];
        const isExtendedThinking = this.model.includes("extended-thinking");
        for (const call of calls) {
          if (!call.id || this.executedToolCallIds.has(call.id)) {
            continue;
          }
          this.turnToolCallsExecuted++;
          const toolResult = await this.handleSingleToolCall(call.name, call.args || {}, call.id);
          const responsePayload = (toolResult && typeof toolResult === 'object') ? toolResult : { result: "ok" };
          if (String(responsePayload?.status || '').startsWith('blocked')) {
            this.lastTurnHadBlockedToolCall = true;
          }
          const isQuestionTool = (
            (call.name === 'write_chalkboard' || call.name === 'write_chalkboardd') &&
            (call.args?.action === 'draw_question' || call.args?.action === 'draw_exam_question')
          ) || call.name === 'draw_question' || call.name === 'draw_exam_question';
          const isSilentBoardOrVisualTool = [
            'write_chalkboard',
            'write_chalkboardd',
            'write_board',
            'chalkboard',
            'whiteboard',
            'draw_chalkboard',
            'draw_board',
            'plot_mathematical_graph',
            'draw_shape',
            'highlight_text',
            'render_svg_diagram',
            'search_and_show_image',
            'search_and_show_video',
            'open_interactive_simulation',
            'update_interactive_simulation',
            'concept_completed',
            'close_graph',
          ].includes(call.name);
          const shouldRespondSilently =
            isQuestionTool ||
            isSilentBoardOrVisualTool ||
            String(responsePayload?.status || '').startsWith('blocked') ||
            this.isStudentMicMuted ||
            this.awaitingStudentAnswer;

          responses.push({
            id: call.id,
            name: call.name,
            response: {
              ...responsePayload,
              scheduling: shouldRespondSilently
                ? FunctionResponseScheduling.SILENT
                : (!isExtendedThinking ? FunctionResponseScheduling.WHEN_IDLE : undefined),
            },
          });
        }
        if (responses.length > 0 && this.isSocketOpen()) {
          try {
            this.session.sendToolResponse({ functionResponses: responses });
          } catch (e) {
            console.warn("[GeminiLive] Failed to send tool response:", e);
          }
        }
      };

      const sessionCallbacks = {
        onopen: () => {
          console.log("[GeminiLive] WebSocket TCP connection open; awaiting setupComplete...");
        },
        onmessage: (msg: any) => {
           // Session resumption token updates & GoAway pre-emptive disconnect notice
           if (msg.sessionResumptionUpdate) {
             const update = msg.sessionResumptionUpdate;
             if (update.resumable && update.newHandle) {
               this.resumptionHandle = update.newHandle;
               this.callbacks.onSessionResumptionUpdate?.(update.newHandle, true);
             }
           }
           if (msg.goAway && !this.goAwayTriggered) {
             this.goAwayTriggered = true;
             const timeLeftStr = String(msg.goAway.timeLeft || "");
             const secMatch = timeLeftStr.match(/([\d.]+)s/);
             const timeLeftMs = secMatch ? Math.round(parseFloat(secMatch[1]) * 1000) : 10000;
             console.warn(`[GeminiLive] Server sent goAway (timeLeft=${timeLeftStr || 'unknown'}). Triggering pre-emptive transparent reconnect...`);
             this.callbacks.onGoAway?.(timeLeftMs);
           }

           const content = msg.serverContent;
           
           // Server Voice Activity Detection (VAD) events
           const isVoiceActivityStart = msg.voiceActivity?.voiceActivityType === "ACTIVITY_START" || msg.voiceActivity?.type === "ACTIVITY_START";
           if (isVoiceActivityStart) {
              this.callbacks.onUserSpeechStart?.();
           }

           // Handle root tool calls for chalkboard writing, visual stage, and dedicated tools
           if (msg.toolCall && msg.toolCall.functionCalls) {
             void dispatchToolCalls(msg.toolCall.functionCalls);
           }

           if (!content) return;

           if (content.interrupted) {
             this.isModelGenerating = false;
             this.turnToolCallsExecuted = 0;
             this.turnEmittedAudio = false;
             this.lastTurnHadBlockedToolCall = false;
             this.turnTeacherTranscriptText = "";
             this.silentTurnNudgeCount = 0;
             this.pendingBoardContext = null;
             this.callbacks.onInterrupted();
             return;
           }
           
           // Transcripts extraction
           const isSubstantiveSpeech = (txt: string) => /[a-zA-Z0-9\u0900-\u097F]{2,}|\d/.test(txt.trim());
           if (content.inputTranscription && content.inputTranscription.text) {
             const userSpoken = content.inputTranscription.text;
             if (isSubstantiveSpeech(userSpoken)) {
               this.awaitingStudentAnswer = false;
               this.recentTranscriptHistory = [...this.recentTranscriptHistory.slice(-5), { sender: "user", text: userSpoken.trim() }];
               this.callbacks.onTranscript(userSpoken, "user");
             }
           }
           if (content.inputTranscription && content.inputTranscription.parts) {
             for (const part of content.inputTranscription.parts) {
                 if (part.text && isSubstantiveSpeech(part.text)) {
                     this.awaitingStudentAnswer = false;
                     this.recentTranscriptHistory = [...this.recentTranscriptHistory.slice(-5), { sender: "user", text: part.text.trim() }];
                     this.callbacks.onTranscript(part.text, "user");
                 }
             }
           }
           
           let hasTeacherTranscript = false;
           if (content.outputTranscription && content.outputTranscription.text) {
             const cleaned = this.extractAndExecuteEmbeddedToolCalls(content.outputTranscription.text);
             if (cleaned) {
               this.turnTeacherTranscriptText += ` ${cleaned}`;
               this.callbacks.onTranscript(cleaned, "teacher");
             }
             hasTeacherTranscript = true;
           } else if (content.outputTranscription && content.outputTranscription.parts) {
             for (const part of content.outputTranscription.parts) {
               if (part.text) {
                 const cleaned = this.extractAndExecuteEmbeddedToolCalls(part.text);
                 if (cleaned) {
                   this.turnTeacherTranscriptText += ` ${cleaned}`;
                   this.callbacks.onTranscript(cleaned, "teacher");
                   hasTeacherTranscript = true;
                 }
               }
             }
           }

           // Incoming audio, video frames, or text model turns
           if (content.modelTurn && content.modelTurn.parts) {
             this.isModelGenerating = true;
             const partFunctionCalls: any[] = [];
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
                   this.turnTeacherTranscriptText += ` ${cleaned}`;
                   this.callbacks.onTranscript(cleaned, "teacher");
                 }
               }
               if (part.functionCall) {
                 partFunctionCalls.push(part.functionCall);
               }
             }
             if (partFunctionCalls.length > 0) {
               void dispatchToolCalls(partFunctionCalls);
             }
           }

           const currentStatus = content.interactionStatus || msg.interactionStatus;
           const isTurnDone = Boolean(content.turnComplete || currentStatus === "IDLE");
           if (isTurnDone && currentStatus !== "IN_PROGRESS") {
             this.isModelGenerating = false;
             if (this.turnTeacherTranscriptText.trim()) {
               this.recentTranscriptHistory = [...this.recentTranscriptHistory.slice(-5), { sender: "teacher", text: this.turnTeacherTranscriptText.trim() }];
             }
             const spokenWordCount = this.turnTeacherTranscriptText.trim().split(/\s+/).filter(Boolean).length;
             const isSilentStateTransition = [
               "concept_completed",
               "concept_done",
               "next_concept",
               "advance_concept",
               "concept_focus",
               "close_graph",
               "clear_board",
               "start_quiz",
               "open_quiz",
             ].includes(this.lastExecutedToolAction || "");
             const suppressSilenceNudge =
               this.lastTurnHadBlockedToolCall ||
               isSilentStateTransition ||
               Date.now() - this.suppressedSilenceNudgeTurnAt < 2500;
             if (
               this.turnToolCallsExecuted > 0 &&
               !this.turnEmittedAudio &&
               !suppressSilenceNudge &&
               this.isSocketOpen() &&
               this.silentTurnNudgeCount < 2 &&
               !this.isStudentMicMuted &&
               !this.awaitingStudentAnswer
             ) {
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
             } else if (
               this.turnEmittedAudio &&
               this.turnToolCallsExecuted === 0 &&
               spokenWordCount >= 18 &&
               !suppressSilenceNudge &&
               this.isSocketOpen() &&
               this.silentBoardNudgeCount < 2 &&
               !this.isStudentMicMuted &&
               !this.awaitingStudentAnswer
             ) {
               this.silentBoardNudgeCount++;
               console.log(`[GeminiLive] Substantive verbal turn (${spokenWordCount} words) ended with 0 board/visual tool calls. Triggering board sync reminder...`);
               try {
                 this.session?.sendClientContent({
                   turns: [
                     {
                       role: "user",
                       parts: [
                         {
                           text: "[BOARD SYNC REMINDER]: You just explained verbally without writing or visualizing on the board. Immediately write concise key points or steps on the chalkboard via write_chalkboard (and call plot_mathematical_graph or search_and_show_image if visual), then ask a quick check question.",
                         },
                       ],
                     },
                   ],
                   turnComplete: true,
                 });
               } catch {}
             }
             this.turnToolCallsExecuted = 0;
             this.turnEmittedAudio = false;
             this.lastTurnHadBlockedToolCall = false;
             this.turnTeacherTranscriptText = "";
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
          this.session = null;
          console.log(`[GeminiLive] WebSocket closed: code=${event?.code}, reason=${event?.reason || '(none)'}, wasClean=${event?.wasClean}`);
          if (event?.reason?.toLowerCase().includes("thinking") || (event?.code === 1007 && event?.reason?.includes("Thinking"))) {
            console.warn(`[GeminiLive] WebSocket closed due to unsupported thinking config (${event?.reason}). Permanently clearing thinkingLevel for all reconnects.`);
            this.thinkingLevel = "";
          }
          if (!this.isManuallyClosed) {
             this.callbacks.onClose(event as CloseEvent);
          }
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

      if (this.pendingKickoffText && !this.hasSentKickoff && !this.resumptionHandle) {
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
    // Note: GreenChalkboard.goToPage already manages the clean concept page title.
    // Never write internal kickoff control headers onto the chalkboard.

    // Use sendClientContent with a user-role turn to trigger the model to respond with audio speech.
    // If reconnecting after a dropped handle, inject compact recent conversation + board state so tutor never forgets context.
    let kickoffInstruction = (text.includes('[SESSION START') || text.includes('[SESSION RECONNECTED]') || text.includes('Speak FIRST'))
      ? text
      : `The student has just joined the class. The topic is: ${text}. Begin the class NOW by warmly greeting the student and immediately starting to teach. You MUST speak your greeting and explanation aloud (produce audio) AND write key points on the chalkboard simultaneously. Start speaking immediately.`;

    if (text.includes('[SESSION RECONNECTED]')) {
      const historyBlock = this.recentTranscriptHistory.length > 0
        ? `\n[RECENT CONVERSATION BEFORE RECONNECT]:\n${this.recentTranscriptHistory.map(t => `${t.sender === 'user' ? 'Student' : 'Tutor'}: ${t.text}`).join('\n')}`
        : '';
      const boardBlock = this.latestBoardState ? `\n[CURRENT_BOARD_STATE]:\n${this.latestBoardState}` : '';
      const muteNote = this.isStudentMicMuted || this.awaitingStudentAnswer
        ? `\nIMPORTANT: The student is currently thinking/muted or solving an active question. Give a tiny 1-sentence encouraging reassurance or stay ready without solving their question or advancing concepts.`
        : '';
      kickoffInstruction = `${text}${historyBlock}${boardBlock}${muteNote}`;
    }

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
    if (!this.isSocketOpen() || !text?.trim()) return;
    const rawTrimmed = text.trim();
    const isInternalDirective = rawTrimmed.startsWith('[');
    if (!isInternalDirective) {
      this.awaitingStudentAnswer = false;
      this.recentTranscriptHistory = [...this.recentTranscriptHistory.slice(-5), { sender: "user", text: rawTrimmed }];
    } else if (
      (this.isStudentMicMuted || this.awaitingStudentAnswer) &&
      /^\[(?:PEDAGOGICAL|EXERCISE|BOARD SYNC)/i.test(rawTrimmed)
    ) {
      console.log("[GeminiLive] Suppressed background guard directive while student is muted or solving active question.");
      return;
    } else if (/^\[(?:PEDAGOGICAL|TRANSITION|STUDENT QUESTION|STUDENT REQUEST|EXERCISE|CURRENT_BOARD)/i.test(rawTrimmed)) {
      this.suppressedSilenceNudgeTurnAt = Date.now();
    }
    try {
      let messageToSend = rawTrimmed;
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
      if (!this.isSocketOpen()) return;
      try {
        this.session.sendRealtimeInput({ text: text.trim() });
      } catch (fallbackErr) {
        console.warn("[GeminiLive] Failed to send text fallback:", fallbackErr);
      }
    }
  }

  public sendAudioChunk(base64Chunk: string): void {
    if (!this.isSocketOpen()) return;
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
    if (!this.isSocketOpen()) return;
    try {
      this.session.sendRealtimeInput({ audioStreamEnd: true });
    } catch (err) {
      console.warn("Failed to send audioStreamEnd", err);
    }
  }

  public sendTurnComplete(): void {
    if (!this.isSocketOpen()) return;
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

  public disconnect(options?: { preserveResumption?: boolean }): void {
    this.isManuallyClosed = true;
    this.isConnected = false;
    this.hasSentKickoff = false;
    this.pendingKickoffText = null;
    if (!options?.preserveResumption) {
      this.resumptionHandle = null;
    }
    if (this.session) {
      try {
        this.session.close();
      } catch (err) {}
      this.session = null;
    }
  }
}
