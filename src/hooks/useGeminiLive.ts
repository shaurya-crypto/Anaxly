"use client";

import { useState, useRef, useCallback, useEffect } from "react";
import { ConnectionState, TranscriptItem, GeminiVoice } from "@/types/liveSession";
import { AudioPlayer } from "@/services/audioPlayer";
import { AudioStreamer } from "@/services/audioStreamer";
import { GeminiLiveClient, LiveAvatarConfig } from "@/services/geminiWebSocket";
import { PedagogicalStateManager } from "@/services/pedagogicalStateManager";
import { SessionController } from "@/services/sessionController";

export function useGeminiLive() {
  const [connectionState, setConnectionState] = useState<ConnectionState>("IDLE");
  const pedagogicalStateManager = useRef(new PedagogicalStateManager());
  const sessionController = useRef(SessionController.getInstance());
  const [isMuted, setIsMuted] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [transcripts, setTranscripts] = useState<TranscriptItem[]>([]);
  const teacherVolumeRef = useRef(0);
  const userVolumeRef = useRef(0);
  const [selectedVoice, setSelectedVoice] = useState<GeminiVoice>("Leda");
  const [latestVideoFrame, setLatestVideoFrame] = useState<string | null>(null);
  const [videoMimeType, setVideoMimeType] = useState<string>("image/jpeg");
  const [studentProfile, setStudentProfile] = useState<any>(null);
  const [activeHighlight, setActiveHighlight] = useState<{ text: string; color?: string; timestamp: number } | null>(null);
  const highlightTimeoutRef = useRef<NodeJS.Timeout | null>(null);

  const audioPlayerRef = useRef<AudioPlayer | null>(null);
  const audioStreamerRef = useRef<AudioStreamer | null>(null);
  const geminiClientRef = useRef<GeminiLiveClient | null>(null);
  const animationFrameRef = useRef<number | null>(null);
  const sharedAudioCtxRef = useRef<AudioContext | null>(null);
  const isMutedRef = useRef(false);
  const transcriptsRef = useRef<TranscriptItem[]>([]);
  const connectionStateRef = useRef<ConnectionState>("IDLE");
  const lockedVoiceRef = useRef<GeminiVoice | null>(null);
  const resumptionHandleRef = useRef<string | null>(null);
  const tokenCacheRef = useRef<{
    token: string;
    config: any;
    mintedAt: number;
    consumed: boolean;
  } | null>(null);
  const isManualEndRef = useRef<boolean>(false);
  const endCallRef = useRef<() => void>(() => {});
  const transparentReconnectAttemptsRef = useRef<number>(0);
  const transparentReconnectTimerRef = useRef<NodeJS.Timeout | null>(null);
  const isTransparentReconnectingRef = useRef<boolean>(false);
  const activeSessionOptionsRef = useRef<{
    voiceOverride?: GeminiVoice;
    systemInstructionOverride?: string;
    kickoffPrompt?: string;
    onChalkboardToolCall?: (action: string, content: any, color?: string) => any;
    onVisualAction?: (action: string, params: Record<string, any>) => void;
    avatarConfig?: LiveAvatarConfig;
    onAudioOutputChunk?: (pcm16: Int16Array, sampleRate: number) => void;
    onSpeechInterrupted?: () => void;
    languageOptions?: {
      preferredLanguage?: string;
      supportedLanguages?: string[];
      languageCode?: string;
    };
    onGetBoardContent?: () => string;
    onHighlightText?: (text: string, target?: string, color?: string) => void;
    onPlanTeachingMove?: (args: {
      questionOrTopic: string;
      studentMessage: string;
      struggleCount?: number;
    }) => Promise<any>;
  } | null>(null);

  useEffect(() => {
    isMutedRef.current = isMuted;
    geminiClientRef.current?.setStudentMicMuted(isMuted);
  }, [isMuted]);

  useEffect(() => {
    transcriptsRef.current = transcripts;
    geminiClientRef.current?.setRecentTranscriptHistory(transcripts.slice(-6));
  }, [transcripts]);

  useEffect(() => {
    connectionStateRef.current = connectionState;
  }, [connectionState]);

  // Volume visualizer loop writing directly to refs to eliminate 60-120fps component re-render thrashing
  const startVolumeLoop = useCallback(() => {
    const loop = () => {
      if (audioPlayerRef.current) {
        teacherVolumeRef.current = audioPlayerRef.current.getVolumeLevel();
      } else {
        teacherVolumeRef.current = 0;
      }
      if (audioStreamerRef.current && !isMutedRef.current) {
        userVolumeRef.current = audioStreamerRef.current.getMicVolume();
      } else {
        userVolumeRef.current = 0;
      }
      animationFrameRef.current = requestAnimationFrame(loop);
    };
    animationFrameRef.current = requestAnimationFrame(loop);
  }, []);

  const stopVolumeLoop = useCallback(() => {
    if (animationFrameRef.current !== null) {
      cancelAnimationFrame(animationFrameRef.current);
      animationFrameRef.current = null;
    }
    teacherVolumeRef.current = 0;
    userVolumeRef.current = 0;
  }, []);

  const pendingTranscriptsRef = useRef<{ text: string; sender: "user" | "teacher" }[]>([]);
  const transcriptFlushTimerRef = useRef<NodeJS.Timeout | null>(null);

  const flushTranscripts = useCallback(() => {
    if (transcriptFlushTimerRef.current) {
      clearTimeout(transcriptFlushTimerRef.current);
      transcriptFlushTimerRef.current = null;
    }
    const queue = pendingTranscriptsRef.current;
    if (queue.length === 0) return;
    pendingTranscriptsRef.current = [];

    setTranscripts((prev) => {
      let updated = [...prev];
      for (const item of queue) {
        const last = updated[updated.length - 1];
        if (last && last.sender === item.sender && Date.now() - last.timestamp < 3500) {
          updated[updated.length - 1] = {
            ...last,
            text: `${last.text} ${item.text.trim()}`,
            id: `${last.id.split('_')[0]}_${Date.now()}`,
          };
        } else {
          updated = [
            ...updated.slice(-8),
            { id: `${Math.random().toString(36).substring(7)}_${Date.now()}`, sender: item.sender, text: item.text.trim(), timestamp: Date.now() },
          ];
        }
      }
      return updated;
    });
  }, []);

  const addTranscript = useCallback((text: string, sender: "user" | "teacher") => {
    pendingTranscriptsRef.current.push({ text, sender });
    if (!transcriptFlushTimerRef.current) {
      transcriptFlushTimerRef.current = setTimeout(flushTranscripts, 150);
    }
  }, [flushTranscripts]);

  const fetchSessionConfig = useCallback(async (forceFresh = false) => {
    const cached = tokenCacheRef.current;
    if (
      !forceFresh &&
      cached &&
      !cached.consumed &&
      Date.now() - cached.mintedAt < 45000
    ) {
      return cached.config;
    }
    const res = await fetch("/api/session");
    if (!res.ok) {
      const errJson = await res.json().catch(() => ({}));
      throw new Error(errJson.error || "Failed to initialize live session configuration");
    }
    const config = await res.json();
    tokenCacheRef.current = {
      token: config.token || config.apiKey,
      config,
      mintedAt: Date.now(),
      consumed: false,
    };
    return config;
  }, []);

  const connectClientInstance = useCallback(
    async (
      config: any,
      opts: NonNullable<typeof activeSessionOptionsRef.current>,
      isResuming: boolean
    ) => {
      if (config.studentProfile) {
        setStudentProfile(config.studentProfile);
      }

      const activeVoice = (lockedVoiceRef.current ||
        opts.voiceOverride ||
        selectedVoice ||
        config.voiceName ||
        "Charon") as GeminiVoice;
      lockedVoiceRef.current = activeVoice;
      if (activeVoice !== selectedVoice) {
        setSelectedVoice(activeVoice);
      }
      console.log("[useGeminiLive] Locked active voice for live session:", activeVoice);

      const triggerTransparentReconnect = (reasonLabel: string) => {
        if (isManualEndRef.current || isTransparentReconnectingRef.current) return;
        if (transparentReconnectAttemptsRef.current >= 3) {
          console.warn(`[useGeminiLive] Max transparent reconnect attempts reached after ${reasonLabel}. Falling back to clean disconnect.`);
          setConnectionState("DISCONNECTED");
          endCallRef.current();
          return;
        }
        isTransparentReconnectingRef.current = true;
        transparentReconnectAttemptsRef.current += 1;
        const attemptNum = transparentReconnectAttemptsRef.current;
        const delayMs = attemptNum === 1 ? 350 : attemptNum === 2 ? 1200 : 2400;
        console.log(`[useGeminiLive] Transparent reconnect scheduled (${reasonLabel}, attempt ${attemptNum}/3) keeping AudioStreamer alive...`);

        if (geminiClientRef.current) {
          geminiClientRef.current.disconnect({ preserveResumption: true });
          geminiClientRef.current = null;
        }

        if (transparentReconnectTimerRef.current) {
          clearTimeout(transparentReconnectTimerRef.current);
        }
        transparentReconnectTimerRef.current = setTimeout(async () => {
          if (isManualEndRef.current) {
            isTransparentReconnectingRef.current = false;
            return;
          }
          try {
            const freshConfig = await fetchSessionConfig();
            const savedOpts = activeSessionOptionsRef.current;
            if (!savedOpts || isManualEndRef.current) {
              isTransparentReconnectingRef.current = false;
              return;
            }
            // Clear reconnecting lock before connect so onError/onClose from this attempt can schedule the next retry instead of deadlocking
            isTransparentReconnectingRef.current = false;
            await connectClientInstance(freshConfig, savedOpts, true);
          } catch (reconnErr) {
            console.warn("[useGeminiLive] Transparent reconnect attempt failed:", reconnErr);
            isTransparentReconnectingRef.current = false;
            if (transparentReconnectAttemptsRef.current < 3 && !isManualEndRef.current) {
              triggerTransparentReconnect("retry");
            } else {
              setConnectionState("DISCONNECTED");
              endCallRef.current();
            }
          }
        }, delayMs);
      };

      if (tokenCacheRef.current) {
        tokenCacheRef.current.consumed = true;
      }

      const client = new GeminiLiveClient(
        config.token || config.apiKey,
        {
          onSetupComplete: () => {
            isTransparentReconnectingRef.current = false;
            transparentReconnectAttemptsRef.current = 0;
            setConnectionState("CONNECTED");
            const shouldKickoff = (!isResuming || !resumptionHandleRef.current) && !resumptionHandleRef.current && opts.kickoffPrompt;
            if (shouldKickoff && opts.kickoffPrompt) {
              audioStreamerRef.current?.setTeacherSpeaking(true);
              const resumePrompt = isResuming
                ? `[SESSION RECONNECTED]: Continue teaching smoothly from where we paused on the current chalkboard without repeating already-written notes.`
                : opts.kickoffPrompt;
              client.sendKickoff(resumePrompt);
              setTimeout(() => {
                setConnectionState((current) => {
                  if (current === "CONNECTED") {
                    audioStreamerRef.current?.setTeacherSpeaking(false);
                    return isMutedRef.current ? "MUTED" : "LISTENING";
                  }
                  return current;
                });
              }, 3500);
            } else {
              setConnectionState((current) =>
                current === "CONNECTED" ? (isMutedRef.current ? "MUTED" : "LISTENING") : current
              );
            }
          },
          onSessionResumptionUpdate: (handle, resumable) => {
            if (resumable && handle) {
              resumptionHandleRef.current = handle;
            }
          },
          onGoAway: () => {
            triggerTransparentReconnect("goAway");
          },
          onAudioData: (pcm16, sampleRate) => {
            if (audioPlayerRef.current) {
              audioPlayerRef.current.playChunk(pcm16, sampleRate);
            }
            opts.onAudioOutputChunk?.(pcm16, sampleRate);
          },
          onVideoData: (data, mimeType) => {
            setLatestVideoFrame(data);
            if (mimeType) {
              setVideoMimeType(mimeType);
            }
          },
          onUserSpeechStart: () => {
            console.log("[useGeminiLive] onUserSpeechStart: Server detected voice activity");
            setConnectionState((prev) =>
              prev !== "MUTED" && prev !== "TEACHER_SPEAKING" ? "LISTENING" : prev
            );
          },
          onInterrupted: () => {
            console.log("[useGeminiLive] onInterrupted: Server confirmed barge-in");
            if (audioPlayerRef.current) {
              audioPlayerRef.current.stopAndClear();
            }
            opts.onSpeechInterrupted?.();
            audioStreamerRef.current?.setTeacherSpeaking(false);
            setConnectionState((prev) => (prev !== "MUTED" ? "LISTENING" : "MUTED"));
          },
          onTurnComplete: () => {
            console.log("[useGeminiLive] onTurnComplete: Model finished generation");
            if (audioPlayerRef.current) {
              audioPlayerRef.current.onTurnComplete();
            }
          },
          onTranscript: (text, sender) => {
            if (sender === "user") {
              pedagogicalStateManager.current.handleUserCommand(text);
            }
            addTranscript(text, sender);
          },
          onChalkboardToolCall: (action, content, color) => {
            return opts.onChalkboardToolCall?.(action, content, color);
          },
          onVisualAction: (action, params) => {
            opts.onVisualAction?.(action, params);
          },
          onHighlightText: (text, target, color) => {
            if (target === "subtitles" || target === "both" || !target) {
              setActiveHighlight({ text, color, timestamp: Date.now() });
              if (highlightTimeoutRef.current) clearTimeout(highlightTimeoutRef.current);
              highlightTimeoutRef.current = setTimeout(() => {
                setActiveHighlight(null);
              }, 4500);
            }
            opts.onHighlightText?.(text, target, color);
          },
          onGetBoardContent: () => {
            return opts.onGetBoardContent?.() || "";
          },
          onPlanTeachingMove: async (args) => {
            if (opts.onPlanTeachingMove) {
              return opts.onPlanTeachingMove(args);
            }
            return { result: "skipped", reason: "no_think_handler" };
          },
          onError: (err) => {
            console.error("[useGeminiLive] Connection error:", err);
            if (!isManualEndRef.current && transparentReconnectAttemptsRef.current < 3 && audioStreamerRef.current) {
              triggerTransparentReconnect("error");
              return;
            }
            setErrorMessage("Connection to Gemini Live was interrupted. Please check your network and try again.");
            setConnectionState("ERROR");
            endCallRef.current();
          },
          onClose: (event) => {
            console.log("[useGeminiLive] onClose callback triggered, event:", event);
            if (!isManualEndRef.current && audioStreamerRef.current && transparentReconnectAttemptsRef.current < 3) {
              triggerTransparentReconnect(`close_${event?.code || "unknown"}`);
              return;
            }
            setConnectionState((prev) => (prev === "ERROR" ? "ERROR" : "DISCONNECTED"));
            endCallRef.current();
          },
        },
        {
          model: config.model,
          voiceName: activeVoice,
          systemInstruction: opts.systemInstructionOverride,
          enableFunctionCalling: true,
          avatarConfig: opts.avatarConfig,
          pedagogicalStateManager: pedagogicalStateManager.current,
          preferredLanguage: opts.languageOptions?.preferredLanguage || config.preferredLanguage,
          supportedLanguages: opts.languageOptions?.supportedLanguages || config.supportedLanguages || ["en-IN", "hi-IN"],
          languageCode: opts.languageOptions?.languageCode || config.languageCode || "en-IN",
          thinkingLevel: config.thinkingLevel,
          resumptionHandle: resumptionHandleRef.current,
        }
      );

      geminiClientRef.current = client;
      client.setStudentMicMuted(isMutedRef.current);
      client.setRecentTranscriptHistory(transcriptsRef.current.slice(-6));
      sessionController.current.initSession(client);
      await client.connect(isResuming ? undefined : opts.kickoffPrompt);
    },
    [addTranscript, fetchSessionConfig, selectedVoice]
  );

  // Start Live Tutoring Session
  const startClass = useCallback(async (
    voiceOverride?: GeminiVoice,
    systemInstructionOverride?: string,
    kickoffPrompt?: string,
    onChalkboardToolCall?: (action: string, content: any, color?: string) => any,
    onVisualAction?: (action: string, params: Record<string, any>) => void,
    avatarConfig?: LiveAvatarConfig,
    onAudioOutputChunk?: (pcm16: Int16Array, sampleRate: number) => void,
    onSpeechInterrupted?: () => void,
    languageOptions?: {
      preferredLanguage?: string;
      supportedLanguages?: string[];
      languageCode?: string;
    },
    onGetBoardContent?: () => string,
    onHighlightText?: (text: string, target?: string, color?: string) => void,
    onPlanTeachingMove?: (args: {
      questionOrTopic: string;
      studentMessage: string;
      struggleCount?: number;
    }) => Promise<any>
  ) => {
    setErrorMessage(null);
    setConnectionState("CONNECTING");
    isManualEndRef.current = false;
    transparentReconnectAttemptsRef.current = 0;
    isTransparentReconnectingRef.current = false;

    const opts = {
      voiceOverride,
      systemInstructionOverride,
      kickoffPrompt,
      onChalkboardToolCall,
      onVisualAction,
      avatarConfig,
      onAudioOutputChunk,
      onSpeechInterrupted,
      languageOptions,
      onGetBoardContent,
      onHighlightText,
      onPlanTeachingMove,
    };
    activeSessionOptionsRef.current = opts;

    try {
      // 1. Fetch live session config from backend
      const config = await fetchSessionConfig(true);

      // 2. Initialize AudioPlayer with Web Audio API (reuse if already alive)
      let player = audioPlayerRef.current;
      let audioCtx = sharedAudioCtxRef.current;
      if (!player || !audioCtx || audioCtx.state === "closed") {
        player = new AudioPlayer((isPlaying) => {
          setConnectionState((prev) => {
            if (prev === "DISCONNECTED" || prev === "ERROR" || prev === "IDLE") return prev;
            if (isPlaying) {
              audioStreamerRef.current?.setTeacherSpeaking(true);
              return "TEACHER_SPEAKING";
            } else {
              audioStreamerRef.current?.setTeacherSpeaking(false);
              return isMutedRef.current ? "MUTED" : "LISTENING";
            }
          });
        });

        audioCtx = await player.init(undefined, 24000);
        if (typeof window !== "undefined") {
          const savedSpeed = localStorage.getItem("anaxly_tutor_speed");
          if (savedSpeed) {
            const parsed = parseFloat(savedSpeed);
            if (!isNaN(parsed) && parsed >= 0.75 && parsed <= 1.3) {
              player.setPlaybackSpeed(parsed);
            }
          }
        }
        audioPlayerRef.current = player;
        sharedAudioCtxRef.current = audioCtx;
      }

      // 3. Initialize AudioStreamer using the SAME AudioContext for hardware echo cancellation
      if (!audioStreamerRef.current) {
        const streamer = new AudioStreamer(
          (base64Chunk) => {
            if (geminiClientRef.current) {
              geminiClientRef.current.sendAudioChunk(base64Chunk);
            }
          },
          () => {
            console.log("[useGeminiLive] Client barge-in detected: stopping teacher playback immediately");
            if (audioPlayerRef.current) {
              audioPlayerRef.current.stopAndClear();
            }
            activeSessionOptionsRef.current?.onSpeechInterrupted?.();
            setConnectionState((prev) => (prev !== "MUTED" ? "LISTENING" : "MUTED"));
          },
          () => {
            console.log("[useGeminiLive] Student started speaking");
            // Non-destructive: suppress LISTENING clobber while TEACHER_SPEAKING; deliberate barge-in is handled above.
            setConnectionState((prev) =>
              prev !== "MUTED" && prev !== "TEACHER_SPEAKING" ? "LISTENING" : prev
            );
          },
          () => {
            // Server VAD continuously monitors incoming audio stream and detects turn completion.
          }
        );
        await streamer.start(audioCtx);
        audioStreamerRef.current = streamer;
      }

      await connectClientInstance(config, opts, false);

      // 5. Start Volume Visualizer loop
      startVolumeLoop();
    } catch (err: unknown) {
      const error = err as Error;
      console.error("[useGeminiLive] Start error:", error);
      setErrorMessage(error.message || "Failed to start live class.");
      setConnectionState("ERROR");
      endCall();
    }
  }, [connectClientInstance, fetchSessionConfig, startVolumeLoop]);

  const toggleMute = useCallback(() => {
    if (!audioStreamerRef.current) return;
    const nextMuted = !isMuted;
    audioStreamerRef.current.setMuted(nextMuted);
    isMutedRef.current = nextMuted;
    setIsMuted(nextMuted);
    geminiClientRef.current?.setStudentMicMuted(nextMuted);
    
    // Flush only if the student was mid-speech when clicking mute; never send synthetic turn endings when already silent
    if (nextMuted && geminiClientRef.current && userVolumeRef.current > 0.015) {
      geminiClientRef.current.sendAudioStreamEnd();
    }

    setConnectionState((prev) => {
      if (prev === "TEACHER_SPEAKING") return prev;
      return nextMuted ? "MUTED" : "LISTENING";
    });
  }, [isMuted]);

  // End Live Call
  const endCall = useCallback(() => {
    isManualEndRef.current = true;
    isTransparentReconnectingRef.current = false;
    transparentReconnectAttemptsRef.current = 0;
    if (transparentReconnectTimerRef.current) {
      clearTimeout(transparentReconnectTimerRef.current);
      transparentReconnectTimerRef.current = null;
    }
    resumptionHandleRef.current = null;
    tokenCacheRef.current = null;
    activeSessionOptionsRef.current = null;

    stopVolumeLoop();

    if (audioStreamerRef.current) {
      audioStreamerRef.current.stop();
      audioStreamerRef.current = null;
    }

    if (audioPlayerRef.current) {
      audioPlayerRef.current.stopAndClear();
      audioPlayerRef.current.close().catch(() => {});
      audioPlayerRef.current = null;
    }

    if (sharedAudioCtxRef.current && sharedAudioCtxRef.current.state !== "closed") {
      try {
        sharedAudioCtxRef.current.close().catch(() => {});
      } catch {
        // Ignore close error
      }
      sharedAudioCtxRef.current = null;
    }

    if (geminiClientRef.current) {
      sessionController.current.terminateSession();
      geminiClientRef.current = null;
    }

    setLatestVideoFrame(null);
    setIsMuted(false);
    setActiveHighlight(null);
    if (highlightTimeoutRef.current) clearTimeout(highlightTimeoutRef.current);
    setConnectionState((prev) => (prev === "ERROR" ? "ERROR" : "DISCONNECTED"));
  }, [stopVolumeLoop]);

  useEffect(() => {
    endCallRef.current = endCall;
  }, [endCall]);

  // Reset to Idle
  const resetToIdle = useCallback(() => {
    endCall();
    setErrorMessage(null);
    setConnectionState("IDLE");
    setTranscripts([]);
    setLatestVideoFrame(null);
  }, [endCall]);

  const setTeacherAudioMuted = useCallback((muted: boolean) => {
    if (audioPlayerRef.current) {
      audioPlayerRef.current.setOutputMuted(muted);
    }
  }, []);

  const pauseClass = useCallback(async () => {
    if (audioPlayerRef.current) {
      await audioPlayerRef.current.pause();
    }
  }, []);

  const resumeClass = useCallback(async () => {
    if (audioPlayerRef.current) {
      await audioPlayerRef.current.resume();
    }
  }, []);

  const setPlaybackSpeed = useCallback((speed: number) => {
    if (audioPlayerRef.current) {
      audioPlayerRef.current.setPlaybackSpeed(speed);
    }
  }, []);

  const sendBoardContext = useCallback((summary: string) => {
    if (geminiClientRef.current) {
      geminiClientRef.current.sendBoardContext(summary);
    }
  }, []);

  const sendTextMessage = useCallback((text: string, displayText?: string) => {
    if (geminiClientRef.current && text?.trim()) {
      if (audioPlayerRef.current) {
        audioPlayerRef.current.stopAndClear();
      }
      geminiClientRef.current.sendTextMessage(text.trim());
      const visibleText = displayText !== undefined ? displayText.trim() : (text.trim().startsWith('[') ? '' : text.trim());
      if (visibleText) {
        addTranscript(visibleText, "user");
      }
    }
  }, [addTranscript]);

  useEffect(() => {
    return () => {
      endCall();
    };
  }, [endCall]);

  return {
    connectionState,
    isMuted,
    errorMessage,
    transcripts,
    teacherVolume: 0,
    userVolume: 0,
    teacherVolumeRef,
    userVolumeRef,
    getTeacherVolume: () => teacherVolumeRef.current,
    getUserVolume: () => userVolumeRef.current,
    audioPlayerRef,
    audioStreamerRef,
    selectedVoice,
    setSelectedVoice,
    latestVideoFrame,
    videoMimeType,
    studentProfile,
    activeHighlight,
    setActiveHighlight,
    startClass,
    toggleMute,
    setTeacherAudioMuted,
    pauseClass,
    resumeClass,
    setPlaybackSpeed,
    endCall,
    resetToIdle,
    sendBoardContext,
    sendTextMessage,
    setAwaitingStudentAnswer: (awaiting: boolean) => geminiClientRef.current?.setAwaitingStudentAnswer(awaiting),
    pedagogicalStateManager: pedagogicalStateManager.current,
  };
}
