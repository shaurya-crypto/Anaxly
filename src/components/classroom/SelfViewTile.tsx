'use client'

import React, { useEffect, useRef } from 'react'
import { MicOff } from 'lucide-react'

export function SelfViewTile({
  stream,
  isMuted,
  name = 'You',
  error,
  className = '',
}: {
  stream: MediaStream | null
  isMuted: boolean
  name?: string
  error?: string | null
  className?: string
}) {
  const videoRef = useRef<HTMLVideoElement | null>(null)

  useEffect(() => {
    if (videoRef.current) videoRef.current.srcObject = stream
  }, [stream])

  const initial = name.trim().charAt(0).toUpperCase() || 'Y'

  return (
    <div className={`relative overflow-hidden rounded-xl bg-[#3C4043] ${className}`}>
      {stream ? (
        <video
          ref={videoRef}
          autoPlay
          playsInline
          muted
          className="absolute inset-0 h-full w-full -scale-x-100 object-cover"
        />
      ) : (
        <div className="absolute inset-0 flex flex-col items-center justify-center gap-2">
          <div className="flex h-14 w-14 items-center justify-center rounded-full bg-[#5F6368] text-xl font-medium text-white sm:h-16 sm:w-16">
            {initial}
          </div>
          {error && <p className="px-2 text-center text-[11px] text-[#F28B82]">{error}</p>}
        </div>
      )}
      <div className="absolute bottom-2 left-2 flex items-center gap-1.5 rounded-md bg-black/50 px-2 py-0.5 text-xs text-white">
        {isMuted && <MicOff className="h-3.5 w-3.5 text-[#F28B82]" />}
        {name}
      </div>
    </div>
  )
}
