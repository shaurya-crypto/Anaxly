export type TeachingStage = 
  | 'REAL_LIFE_INTUITION' 
  | 'CONCEPT_FORMULATION' 
  | 'PRECISE_EXAMPLE' 
  | 'BOARD_NUMERICAL' 
  | 'CHECK_UNDERSTANDING' 
  | 'BOARD_EXAM_NUMERICAL';

export class PedagogicalStateManager {
  private currentStage: TeachingStage = 'REAL_LIFE_INTUITION';
  private stageOrder: TeachingStage[] = [
    'REAL_LIFE_INTUITION',
    'CONCEPT_FORMULATION',
    'PRECISE_EXAMPLE',
    'BOARD_NUMERICAL',
    'CHECK_UNDERSTANDING',
    'BOARD_EXAM_NUMERICAL'
  ];

  public getStage(): TeachingStage {
    return this.currentStage;
  }

  public getStageIndex(): number {
    return this.stageOrder.indexOf(this.currentStage);
  }

  public setStage(stage: TeachingStage): void {
    if (this.stageOrder.includes(stage)) {
      this.currentStage = stage;
      console.log(`[PedagogicalStateManager] Explicit stage set: ${this.currentStage}`);
    }
  }

  // Advance stage based on explicit user command
  public handleUserCommand(command: string): boolean {
    if (/next concept|aage badho|next page|move to next concept|agla concept/i.test(command)) {
      // Force allow advancement on explicit user command
      this.currentStage = 'BOARD_EXAM_NUMERICAL';
      return true;
    }
    return false;
  }

  // Handle and track pedagogical progression based on tool call
  public handleToolCall(action: string, content?: any): boolean {
    let act = (action || '').toLowerCase();
    let effectiveContent = content;

    // Unwrap write_chalkboard calls if action was passed inside content/args
    if (['write_chalkboard', 'write_chalkboardd', 'write_board', 'chalkboard', 'whiteboard'].includes(act) && typeof content === 'object' && content !== null) {
      if (content.action) {
        act = String(content.action).toLowerCase();
      }
      effectiveContent = content.content ?? content.text ?? content;
    }

    const contentStr = typeof effectiveContent === 'string' ? effectiveContent : JSON.stringify(effectiveContent || '');

    // 1. Concept advancement gating
    if (['concept_completed', 'concept_done', 'next_concept', 'advance_concept'].includes(act)) {
      const currentIndex = this.stageOrder.indexOf(this.currentStage);
      // Allow advancement if we reached Stage 5 (CHECK_UNDERSTANDING) or Stage 6 (BOARD_EXAM_NUMERICAL)
      if (currentIndex >= 4) {
        console.log(`[PedagogicalStateManager] Concept completion permitted at stage: ${this.currentStage}`);
        return true;
      }
      
      console.log(`[PedagogicalStateManager] Blocked premature advancement from stage: ${this.currentStage}`);
      return false;
    }

    // 2. Dynamic stage advancement based on chalkboard tools (never advance stage on draw_title alone)
    if (act === 'draw_title' || act === 'title' || act === 'board_title') {
      return true;
    }

    if (act === 'draw_highlight_box' || /\b(?:theorem|property|axiom|corollary|definition)\b|law:|formula:|concept\s*:/i.test(contentStr)) {
      if (this.getStageIndex() < 1) {
        this.currentStage = 'CONCEPT_FORMULATION';
        console.log(`[PedagogicalStateManager] Tool triggered stage -> CONCEPT_FORMULATION`);
      }
    } else if (act === 'draw_note' && /example|application|pitfall/i.test(contentStr)) {
      if (this.getStageIndex() < 2) {
        this.currentStage = 'PRECISE_EXAMPLE';
        console.log(`[PedagogicalStateManager] Tool triggered stage -> PRECISE_EXAMPLE`);
      }
    } else if (act === 'draw_numerical' || act === 'draw_step' || act === 'draw_rough_work' || act === 'numerical') {
      if (this.getStageIndex() < 3) {
        this.currentStage = 'BOARD_NUMERICAL';
        console.log(`[PedagogicalStateManager] Tool triggered stage -> BOARD_NUMERICAL`);
      }
    } else if (act === 'draw_question' || act === 'draw_exam_question' || /checkpoint|question|q:/i.test(contentStr)) {
      this.currentStage = 'CHECK_UNDERSTANDING';
      console.log(`[PedagogicalStateManager] Tool triggered stage -> CHECK_UNDERSTANDING`);
    } else if (act === 'draw_answer_verdict' || /verdict:/i.test(contentStr)) {
      this.currentStage = 'BOARD_EXAM_NUMERICAL';
      console.log(`[PedagogicalStateManager] Tool triggered stage -> BOARD_EXAM_NUMERICAL`);
    }

    return true; // Allow non-advancement tools
  }

  public advanceStage(): boolean {
    const currentIndex = this.stageOrder.indexOf(this.currentStage);
    if (currentIndex < this.stageOrder.length - 1) {
      this.currentStage = this.stageOrder[currentIndex + 1];
      console.log(`[PedagogicalStateManager] Advanced to stage: ${this.currentStage}`);
      return true;
    }
    return false;
  }

  public canCompleteConcept(): boolean {
    return this.getStageIndex() >= 4;
  }

  public resetStages(): void {
    this.currentStage = 'REAL_LIFE_INTUITION';
    console.log(`[PedagogicalStateManager] Reset to stage: ${this.currentStage}`);
  }
}
