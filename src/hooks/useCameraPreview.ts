'use client'

import { useCallback, useEffect, useRef, useState } from 'react'

/**
 * Local-only camera preview for the classroom self-view tile.
 * The stream is never sent to the tutor; it only feeds a <video> element.
 */
export function useCameraPreview() {
  const [stream, setStream] = useState<MediaStream | null>(null)
  const [error, setError] = useState<string | null>(null)
  const streamRef = useRef<MediaStream | null>(null)

  const stop = useCallback(() => {
    streamRef.current?.getTracks().forEach((t) => t.stop())
    streamRef.current = null
    setStream(null)
  }, [])

  const start = useCallback(async () => {
    setError(null)
    try {
      const s = await navigator.mediaDevices.getUserMedia({
        video: { width: { ideal: 640 }, height: { ideal: 360 }, facingMode: 'user' },
        audio: false,
      })
      streamRef.current = s
      setStream(s)
    } catch (e) {
      const name = (e as DOMException)?.name
      setError(
        name === 'NotAllowedError'
          ? 'Camera permission was blocked'
          : name === 'NotFoundError'
          ? 'No camera found'
          : 'Camera unavailable'
      )
    }
  }, [])

  const toggle = useCallback(() => {
    if (streamRef.current) stop()
    else void start()
  }, [start, stop])

  useEffect(() => stop, [stop])

  return { stream, isOn: !!stream, error, toggle, stop }
}
