/**
 * AudioStreamer captures the browser microphone using modern AudioWorkletNode
 * with hardware AEC (Acoustic Echo Cancellation), speech bandpass DSP,
 * and adaptive noise-gating to ignore ambient room noise and catch only human voice.
 */
export class AudioStreamer {
  private audioCtx: AudioContext | null = null;
  private mediaStream: MediaStream | null = null;
  private workletNode: AudioWorkletNode | null = null;
  private scriptProcessor: ScriptProcessorNode | null = null;
  private sourceNode: MediaStreamAudioSourceNode | null = null;
  private highpassFilter: BiquadFilterNode | null = null;
  private lowpassFilter: BiquadFilterNode | null = null;
  private analyser: AnalyserNode | null = null;
  private isMuted: boolean = false;
  private isTeacherSpeaking: boolean = false;
  private teacherSpeakingHangoverTimer: NodeJS.Timeout | null = null;
  private teacherSpeechStartTime: number = 0;
  private lastSpeechTime: number = 0;
  private consecutiveBargeInFrames: number = 0;
  private wasSpeechActive: boolean = false;
  private pendingOnsetFrame: Float32Array | null = null;
  private noiseFloor: number = 0.015;
  private consecutiveSpeechFrames: number = 0;
  private speechStartTime: number = 0;
  private speechEndTime: number = 0;
  private onAudioChunk?: (base64Chunk: string) => void;
  private onBargeIn?: () => void;
  private onSpeechStart?: () => void;
  private onSpeechEnd?: () => void;

  constructor(
    onAudioChunk?: (base64Chunk: string) => void,
    onBargeIn?: () => void,
    onSpeechStart?: () => void,
    onSpeechEnd?: () => void
  ) {
    this.onAudioChunk = onAudioChunk;
    this.onBargeIn = onBargeIn;
    this.onSpeechStart = onSpeechStart;
    this.onSpeechEnd = onSpeechEnd;
  }

  public async start(existingContext?: AudioContext): Promise<AudioContext> {
    // 1. Request microphone with browser-native Echo Cancellation, Noise Suppression, and AGC
    try {
      this.mediaStream = await navigator.mediaDevices.getUserMedia({
        audio: {
          channelCount: 1,
          sampleRate: { ideal: 16000 },
          echoCancellation: true,
          noiseSuppression: true,
          autoGainControl: true,
        },
      });
    } catch (err: unknown) {
      const error = err as Error;
      if (error.name === "NotAllowedError" || error.name === "PermissionDeniedError") {
        throw new Error("Microphone permission denied. Please allow microphone access to talk to the AI tutor.");
      }
      if (error.name === "NotFoundError" || error.name === "DevicesNotFoundError") {
        throw new Error("No microphone found. Please connect a microphone and try again.");
      }
      throw new Error(`Microphone error: ${error.message || "Failed to access microphone"}`);
    }

    // 2. Use existing AudioContext or create one
    if (existingContext && existingContext.state !== "closed") {
      this.audioCtx = existingContext;
    } else {
      const AudioCtxClass =
        window.AudioContext ||
        (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
      this.audioCtx = new AudioCtxClass();
    }

    if (this.audioCtx.state === "suspended") {
      await this.audioCtx.resume();
    }

    const inputSampleRate = this.audioCtx.sampleRate;
    const targetSampleRate = 16000;

    // 3. Audio Graph with Voice-Band Filtering (120 Hz highpass, 4000 Hz lowpass)
    // Cuts out laptop fan drone, desk bump rumbles, AC hum, and electrical hiss while preserving human vocal formants
    this.sourceNode = this.audioCtx.createMediaStreamSource(this.mediaStream);

    this.highpassFilter = this.audioCtx.createBiquadFilter();
    this.highpassFilter.type = "highpass";
    this.highpassFilter.frequency.value = 120; // eliminate low-frequency rumble & fan hum

    this.lowpassFilter = this.audioCtx.createBiquadFilter();
    this.lowpassFilter.type = "lowpass";
    this.lowpassFilter.frequency.value = 4000; // eliminate high-frequency static & hiss

    this.analyser = this.audioCtx.createAnalyser();
    this.analyser.fftSize = 256;
    this.analyser.smoothingTimeConstant = 0.2;

    this.sourceNode.connect(this.highpassFilter);
    this.highpassFilter.connect(this.lowpassFilter);
    this.lowpassFilter.connect(this.analyser);

    // 4. Connect AudioWorkletNode
    let useWorklet = false;
    if (this.audioCtx.audioWorklet) {
      try {
        await this.audioCtx.audioWorklet.addModule("/worklets/pcm-recorder-processor.js");
        this.workletNode = new AudioWorkletNode(this.audioCtx, "pcm-recorder-processor");

        this.workletNode.port.onmessage = (event: MessageEvent<Float32Array>) => {
          this.processAudioFrame(event.data, inputSampleRate, targetSampleRate);
        };

        this.lowpassFilter.connect(this.workletNode);
        const muteGain = this.audioCtx.createGain();
        muteGain.gain.value = 0;
        this.workletNode.connect(muteGain);
        muteGain.connect(this.audioCtx.destination);

        useWorklet = true;
      } catch (workletErr) {
        console.warn("[AudioStreamer] AudioWorklet init failed, falling back to ScriptProcessor:", workletErr);
      }
    }

    if (!useWorklet) {
      const bufferSize = 4096;
      this.scriptProcessor = this.audioCtx.createScriptProcessor(bufferSize, 1, 1);
      this.scriptProcessor.onaudioprocess = (e) => {
        const inputChannelData = e.inputBuffer.getChannelData(0);
        this.processAudioFrame(inputChannelData, inputSampleRate, targetSampleRate);
      };

      this.lowpassFilter.connect(this.scriptProcessor);
      const muteGain = this.audioCtx.createGain();
      muteGain.gain.value = 0;
      this.scriptProcessor.connect(muteGain);
      muteGain.connect(this.audioCtx.destination);
    }

    return this.audioCtx;
  }

  /**
   * Processes a chunk of audio, performs barge-in detection,
   * downsamples to 16kHz, and streams base64 PCM continuously to Gemini Live.
   * Continuous streaming lets Gemini Live's built-in server-side VAD manage turn boundaries accurately.
   */
  private processAudioFrame(inputData: Float32Array, inputRate: number, targetRate: number): void {
    if (this.isMuted) {
      return;
    }

    // Calculate RMS energy of voice-filtered audio
    let sum = 0;
    for (let i = 0; i < inputData.length; i++) {
      sum += inputData[i] * inputData[i];
    }
    const rms = Math.sqrt(sum / inputData.length);
    const now = Date.now();
    const SILENCE_TAIL_MS = 950;
    const SPEECH_HANGOVER_MS = 900;

    let allowUpstreamAudio = false;
    let emitDigitalSilence = false;

    // 1. TEACHER SPEAKING & CLIENT-SIDE STRICT BARGE-IN GATE:
    // Require sustained higher-amplitude speech (5 consecutive frames) before interrupting the teacher,
    // and withhold raw mic audio while teacher is speaking so room hum / speaker bleed never triggers
    // false server-side VAD interruptions.
    if (this.isTeacherSpeaking) {
      const bargeInThreshold = Math.max(0.085, this.noiseFloor * 4.8);
      if (rms >= bargeInThreshold) {
        this.consecutiveBargeInFrames++;
        if (this.consecutiveBargeInFrames >= 5) {
          console.log(`[AudioStreamer] Sustained student speech detected during teacher speech (RMS: ${rms.toFixed(4)}). Triggering barge-in.`);
          this.isTeacherSpeaking = false;
          this.consecutiveBargeInFrames = 0;
          this.consecutiveSpeechFrames = 2;
          this.lastSpeechTime = now;
          this.wasSpeechActive = true;
          this.speechStartTime = now;
          this.onBargeIn?.();
          this.onSpeechStart?.();
          allowUpstreamAudio = true;
        }
      } else {
        this.consecutiveBargeInFrames = 0;
      }
      if (!allowUpstreamAudio) {
        this.wasSpeechActive = false;
        this.pendingOnsetFrame = null;
        return;
      }
    } else {
      this.consecutiveBargeInFrames = 0;

      // 2. ADAPTIVE NOISE FLOOR & SPEECH ONSET GATE (IDLE / LISTENING):
      const onsetThreshold = Math.max(0.028, this.noiseFloor * 2.8);
      const sustainThreshold = Math.max(0.020, this.noiseFloor * 2.1);

      if (rms >= (this.wasSpeechActive ? sustainThreshold : onsetThreshold)) {
        this.consecutiveSpeechFrames++;
        if (this.wasSpeechActive) {
          this.lastSpeechTime = now;
          allowUpstreamAudio = true;
        } else if (this.consecutiveSpeechFrames >= 2) {
          this.wasSpeechActive = true;
          this.lastSpeechTime = now;
          this.speechStartTime = now;
          this.onSpeechStart?.();
          allowUpstreamAudio = true;
        } else {
          // Buffer 1 onset frame so the first syllable is preserved once frame 2 confirms speech
          this.pendingOnsetFrame = new Float32Array(inputData);
          return;
        }
      } else {
        this.consecutiveSpeechFrames = 0;
        if (!this.wasSpeechActive) {
          this.pendingOnsetFrame = null;
          // Track ambient noise floor smoothly during non-speech frames
          if (rms < 0.045) {
            this.noiseFloor = Math.min(0.032, Math.max(0.008, this.noiseFloor * 0.96 + rms * 0.04));
          }
          // Send clean digital silence only briefly after speech ended so server VAD finishes the turn cleanly
          if (this.speechEndTime > 0 && now - this.speechEndTime <= SILENCE_TAIL_MS) {
            emitDigitalSilence = true;
          } else {
            return;
          }
        } else if (now - this.lastSpeechTime <= SPEECH_HANGOVER_MS) {
          // Short hangover keeps mid-word pauses smooth
          allowUpstreamAudio = true;
        } else {
          this.wasSpeechActive = false;
          this.speechEndTime = now;
          this.onSpeechEnd?.();
          emitDigitalSilence = true;
        }
      }
    }

    // 3. GATED AUDIO STREAMING TO SERVER VAD:
    // Flush onset pre-roll frame if present so words never clip at start
    if (allowUpstreamAudio && this.pendingOnsetFrame) {
      const preRoll = this.resampleAudio(this.pendingOnsetFrame, inputRate, targetRate);
      this.pendingOnsetFrame = null;
      const prePcm = this.floatTo16BitPCM(preRoll);
      this.onAudioChunk?.(this.arrayBufferToBase64(prePcm.buffer));
    }

    if (emitDigitalSilence) {
      const silentLen = Math.max(1, Math.round(inputData.length * (targetRate / inputRate)));
      const zeroPcm = new Int16Array(silentLen);
      this.onAudioChunk?.(this.arrayBufferToBase64(zeroPcm.buffer));
      return;
    }

    const resampledData = this.resampleAudio(inputData, inputRate, targetRate);
    const pcm16 = this.floatTo16BitPCM(resampledData);
    const base64 = this.arrayBufferToBase64(pcm16.buffer);

    this.onAudioChunk?.(base64);
  }

  public setTeacherSpeaking(speaking: boolean, isSimliActive: boolean = false): void {
    if (this.teacherSpeakingHangoverTimer) {
      clearTimeout(this.teacherSpeakingHangoverTimer);
      this.teacherSpeakingHangoverTimer = null;
    }
    if (speaking) {
      this.isTeacherSpeaking = true;
      this.teacherSpeechStartTime = Date.now();
      this.consecutiveBargeInFrames = 0;
    } else {
      const delayMs = isSimliActive ? 650 : 280;
      this.teacherSpeakingHangoverTimer = setTimeout(() => {
        this.isTeacherSpeaking = false;
        this.consecutiveBargeInFrames = 0;
        this.teacherSpeakingHangoverTimer = null;
      }, delayMs);
    }
  }

  public setMuted(muted: boolean): void {
    this.isMuted = muted;
    this.pendingOnsetFrame = null;
    if (!muted) {
      this.wasSpeechActive = false;
      this.consecutiveSpeechFrames = 0;
      this.consecutiveBargeInFrames = 0;
      this.lastSpeechTime = Date.now();
      if (this.audioCtx && this.audioCtx.state === 'suspended') {
        this.audioCtx.resume().catch(() => {});
      }
    }
  }

  public getIsMuted(): boolean {
    return this.isMuted;
  }

  public getMicVolume(): number {
    if (!this.analyser || this.isMuted) return 0;
    const dataArray = new Uint8Array(this.analyser.frequencyBinCount);
    this.analyser.getByteFrequencyData(dataArray);

    let sum = 0;
    for (let i = 0; i < dataArray.length; i++) {
      sum += dataArray[i];
    }
    const avg = sum / dataArray.length;
    return Math.min(1.0, avg / 128.0);
  }

  public stop(): void {
    this.pendingOnsetFrame = null;
    if (this.workletNode) {
      this.workletNode.disconnect();
      this.workletNode.port.onmessage = null;
      this.workletNode = null;
    }

    if (this.scriptProcessor) {
      this.scriptProcessor.disconnect();
      this.scriptProcessor.onaudioprocess = null;
      this.scriptProcessor = null;
    }

    if (this.highpassFilter) {
      this.highpassFilter.disconnect();
      this.highpassFilter = null;
    }

    if (this.lowpassFilter) {
      this.lowpassFilter.disconnect();
      this.lowpassFilter = null;
    }

    if (this.sourceNode) {
      this.sourceNode.disconnect();
      this.sourceNode = null;
    }

    if (this.mediaStream) {
      this.mediaStream.getTracks().forEach((track) => track.stop());
      this.mediaStream = null;
    }

    if (this.audioCtx && this.audioCtx.state !== "closed") {
      try {
        this.audioCtx.close().catch(() => {});
      } catch {
        // Ignore close error
      }
      this.audioCtx = null;
    }
  }

  private resampleAudio(audioData: Float32Array, inputRate: number, outputRate: number): Float32Array {
    if (inputRate === outputRate) return audioData;
    const ratio = inputRate / outputRate;
    const newLength = Math.round(audioData.length / ratio);
    const result = new Float32Array(newLength);
    for (let i = 0; i < newLength; i++) {
      const originalIndex = i * ratio;
      const index = Math.floor(originalIndex);
      const nextIndex = Math.min(index + 1, audioData.length - 1);
      const weight = originalIndex - index;
      result[i] = audioData[index] * (1 - weight) + audioData[nextIndex] * weight;
    }
    return result;
  }

  private floatTo16BitPCM(input: Float32Array): Int16Array {
    const output = new Int16Array(input.length);
    for (let i = 0; i < input.length; i++) {
      const s = Math.max(-1, Math.min(1, input[i]));
      output[i] = s < 0 ? s * 0x8000 : s * 0x7fff;
    }
    return output;
  }

  private arrayBufferToBase64(buffer: ArrayBufferLike): string {
    let binary = "";
    const bytes = new Uint8Array(buffer);
    const len = bytes.byteLength;
    for (let i = 0; i < len; i++) {
      binary += String.fromCharCode(bytes[i]);
    }
    return window.btoa(binary);
  }
}
