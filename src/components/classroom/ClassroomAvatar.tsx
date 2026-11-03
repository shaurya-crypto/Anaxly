'use client'

import React, { useState, useEffect, useRef } from 'react'
import { ConnectionState, TranscriptItem } from '@/types/liveSession'
import { LiveAvatarConfig } from '@/services/geminiWebSocket'
import { SimliAvatarController, SimliStatus } from '@/services/simliAvatarService'

export type AvatarProvider = 'simli' | 'google'

interface ClassroomAvatarProps {
  state: ConnectionState
  teacherVolume: number
  userVolume?: number
  isMuted: boolean
  latestTranscript?: TranscriptItem | null
  latestVideoFrame?: string | null
  videoMimeType?: string
  onCustomAvatarChange?: (avatarConfig: LiveAvatarConfig | null) => void
  onSimliControllerReady?: (controller: SimliAvatarController | null) => void
  onSimliActiveChange?: (isActive: boolean) => void
  preferredProvider?: AvatarProvider
  isAvatarEnabled?: boolean
  /** Tailwind size classes for the avatar circle, e.g. 'w-12 h-12 md:w-40 md:h-40' */
  className?: string
}

export const ClassroomAvatar: React.FC<ClassroomAvatarProps> = ({
  state,
  teacherVolume,
  userVolume = 0,
  isMuted,
  latestTranscript,
  onSimliControllerReady,
  onSimliActiveChange,
  isAvatarEnabled = true,
  className = 'w-16 h-16',
}) => {

  // Selected Face ID: default to 80459b57-2d66-4ca7-8682-59e1c649bc53
  const [selectedFaceId, setSelectedFaceId] = useState<string>('80459b57-2d66-4ca7-8682-59e1c649bc53')
  const [simliStatus, setSimliStatus] = useState<SimliStatus>('idle')
  const [isMounted, setIsMounted] = useState(false)

  const simliVideoRef = useRef<HTMLVideoElement | null>(null)
  const simliAudioRef = useRef<HTMLAudioElement | null>(null)
  const simliControllerRef = useRef<SimliAvatarController | null>(null)

  const isSpeaking = state === 'TEACHER_SPEAKING'
  const isCallActive = state !== 'IDLE' && state !== 'DISCONNECTED' && state !== 'ERROR'
  const isUserTalking = !isSpeaking && !isMuted && userVolume > 0.04
  const isSimliActive = simliStatus === 'connected'

  const onSimliActiveChangeRef = useRef(onSimliActiveChange)
  onSimliActiveChangeRef.current = onSimliActiveChange

  const onSimliControllerReadyRef = useRef(onSimliControllerReady)
  onSimliControllerReadyRef.current = onSimliControllerReady

  const prevSimliActiveRef = useRef<boolean | null>(null)

  // Notify parent of Simli active status to manage audio routing and eliminate echo
  useEffect(() => {
    if (prevSimliActiveRef.current !== isSimliActive) {
      prevSimliActiveRef.current = isSimliActive
      onSimliActiveChangeRef.current?.(isSimliActive)
    }
  }, [isSimliActive])

  // Restore saved faceId from localStorage on mount and sync on storage events
  useEffect(() => {
    setIsMounted(true)
    if (typeof window !== 'undefined') {
      try {
        const storedFaceId = localStorage.getItem('ai_tutor_selected_face_id')
        if (storedFaceId && storedFaceId.length > 5) {
          setSelectedFaceId(storedFaceId)
        }
      } catch {}
    }

    const handleStorageUpdate = () => {
      try {
        const storedFaceId = localStorage.getItem('ai_tutor_selected_face_id')
        if (storedFaceId && storedFaceId.length > 5) {
          setSelectedFaceId(storedFaceId)
        }
      } catch {}
    }
    window.addEventListener('storage', handleStorageUpdate)
    return () => window.removeEventListener('storage', handleStorageUpdate)
  }, [])

  // Initialize controller once
  useEffect(() => {
    const controller = new SimliAvatarController((status) => {
      setSimliStatus(status)
    })

    simliControllerRef.current = controller
    onSimliControllerReadyRef.current?.(controller)

    return () => {
      controller.stop()
      simliControllerRef.current = null
      onSimliControllerReadyRef.current?.(null)
      onSimliActiveChangeRef.current?.(false)
    }
  }, [])

  // Manage Simli WebRTC connection lifecycle based on classroom call state
  useEffect(() => {
    if (!isMounted) return

    if (!isAvatarEnabled || !isCallActive) {
      simliControllerRef.current?.stop()
      return
    }

    if (!simliVideoRef.current || !simliAudioRef.current) return

    const controller = simliControllerRef.current
    if (!controller) return

    controller.start({
      videoElement: simliVideoRef.current,
      audioElement: simliAudioRef.current,
      faceId: selectedFaceId,
    })
  }, [isMounted, isCallActive, isAvatarEnabled, selectedFaceId])

  // Subtle audio-reactive ring; no per-frame layout work, just a transform
  const level = isSpeaking ? teacherVolume : isUserTalking ? userVolume : 0
  const ringScale = 1 + Math.min(level, 1) * 0.12
  const ringColor = isSpeaking ? 'ring-amber-500/60' : isUserTalking ? 'ring-emerald-500/60' : 'ring-stone-200'

  const avatarImageUrl = `/avatars/${selectedFaceId}.jpg`

  return (
    <div
      className={`relative shrink-0 rounded-full bg-stone-100 ring-2 ring-offset-2 ring-offset-[#F8F6F0] overflow-hidden select-none transition-[transform,box-shadow] duration-150 ease-out ${ringColor} ${className}`}
      style={{ transform: `scale(${ringScale})` }}
    >
      {isAvatarEnabled ? (
        <>
          <video
            ref={simliVideoRef}
            autoPlay
            playsInline
            muted
            className={`absolute inset-0 w-full h-full object-cover bg-stone-900 transition-opacity duration-300 ${
              isSimliActive ? 'opacity-100 z-10' : 'opacity-0 pointer-events-none z-0'
            }`}
          />
          <audio ref={simliAudioRef} autoPlay />
          <img
            src={avatarImageUrl}
            alt="Tutor"
            className={`absolute inset-0 w-full h-full object-cover transition-opacity duration-300 ${
              isSimliActive ? 'opacity-0' : 'opacity-100'
            }`}
            onError={(e) => {
              ;(e.currentTarget as HTMLImageElement).src = `https://app.simli.com/characters/trinity2/${selectedFaceId}.jpg`
            }}
          />
        </>
      ) : (
        <div className="absolute inset-0 flex items-center justify-center text-[10px] text-stone-500">Tutor</div>
      )}
    </div>
  )
}
