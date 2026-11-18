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

  // Advance stage based on explicit user command
  public handleUserCommand(command: string): boolean {
    if (/next concept|aage badho|next page|move to next concept/i.test(command)) {
      return this.advanceStage();
    }
    return false;
  }

  // Advance stage based on tool call (e.g., tutor finished a stage)
  public handleToolCall(action: string): boolean {
    // Stage 1-4 lock: forbidden from calling concept_completed/done automatically
    if (['concept_completed', 'concept_done', 'next_concept', 'advance_concept'].includes(action)) {
      const currentIndex = this.stageOrder.indexOf(this.currentStage);
      
      // Allow advancement if we are at Stage 5 (CHECK_UNDERSTANDING) 
      // or if it's an explicit "next concept" tool call
      if (currentIndex >= 4) {
        return this.advanceStage();
      }
      
      console.log(`[PedagogicalStateManager] Blocked premature advancement from stage: ${this.currentStage}`);
      return false;
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

  public resetStages() {
    this.currentStage = 'REAL_LIFE_INTUITION';
  }
}
