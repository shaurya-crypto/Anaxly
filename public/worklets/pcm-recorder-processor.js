/**
 * pcm-recorder-processor.js
 * AudioWorkletProcessor that streams microphone audio buffers to the main thread.
 * Replaces deprecated ScriptProcessorNode.
 */
class PCMRecorderProcessor extends AudioWorkletProcessor {
  constructor() {
    super();
    // 512 samples = ~10.6ms at 48kHz / ~21.3ms at 24kHz, reducing collection delay and providing ultra-low latency
    this.bufferSize = 512;
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
