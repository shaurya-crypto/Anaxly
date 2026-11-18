
import { GeminiLiveClient } from './geminiWebSocket';

export class SessionController {
  private static instance: SessionController;
  private geminiClient: GeminiLiveClient | null = null;
  private sessionStartTime: number = 0;

  private constructor() {}

  public static getInstance(): SessionController {
    if (!SessionController.instance) {
      SessionController.instance = new SessionController();
    }
    return SessionController.instance;
  }

  public initSession(client: GeminiLiveClient) {
    this.geminiClient = client;
    this.sessionStartTime = Date.now();
    console.log("[SessionController] Session initialized");
  }

  public terminateSession() {
    if (this.geminiClient) {
      this.geminiClient.disconnect();
      this.geminiClient = null;
      console.log("[SessionController] Session terminated");
    }
  }

  public checkAutoTermination() {
    // Logic for auto-termination (e.g. time limit or completion of curriculum)
    const sessionDuration = (Date.now() - this.sessionStartTime) / 1000 / 60;
    if (sessionDuration > 60) { // e.g. 60 minute limit
      this.terminateSession();
    }
  }
}
