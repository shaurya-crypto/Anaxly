/**
 * pcm-recorder-processor.js
 * AudioWorkletProcessor that streams microphone audio buffers to the main thread.
 * Replaces deprecated ScriptProcessorNode.
 */
class PCMRecorderProcessor extends AudioWorkletProcessor {
  constructor() {
    super();
    // Aggregate audio chunks to ~100ms (e.g. 2400 samples at 24kHz, 4800 at 48kHz, 1600 at 16kHz)
    // Eliminates micro-chunk flooding to the main thread and Gemini WebSocket
    const rate = typeof sampleRate !== 'undefined' ? sampleRate : 24000;
    this.bufferSize = Math.max(1024, Math.round(rate * 0.1));
    this.buffer = new Float32Array(this.bufferSize);
    this.bufferIndex = 0;
  }

  process(inputs, outputs, parameters) {
    const input = inputs[0];
    if (!input || !input[0]) {
      return true;
    }

    const channelData = input[0];
    const len = channelData.length;

    for (let i = 0; i < len; i++) {
      this.buffer[this.bufferIndex++] = channelData[i];
      if (this.bufferIndex >= this.bufferSize) {
        // Post the collected float chunk to main thread
        const chunk = new Float32Array(this.buffer);
        this.port.postMessage(chunk, [chunk.buffer]);
        this.bufferIndex = 0;
      }
    }

    return true;
  }
}

registerProcessor("pcm-recorder-processor", PCMRecorderProcessor);
