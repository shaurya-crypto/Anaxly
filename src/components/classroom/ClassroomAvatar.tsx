'use client'

import React, { useState, useEffect, useRef } from 'react'
import Link from 'next/link'
import { useParams } from 'next/navigation'
import { ConnectionState, TranscriptItem } from '@/types/liveSession'
import { LiveAvatarConfig } from '@/services/geminiWebSocket'
import { SimliAvatarController, SimliStatus } from '@/services/simliAvatarService'

export type AvatarProvider = 'simli' | 'google'

interface ClassroomAvatarProps {
  state: ConnectionState
  teacherVolume?: number
  userVolume?: number
  teacherVolumeRef?: React.RefObject<number>
  userVolumeRef?: React.RefObject<number>
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
  teacherVolume = 0,
  userVolume = 0,
  teacherVolumeRef,
  userVolumeRef,
  isMuted,
  latestTranscript,
  latestVideoFrame,
  videoMimeType,
  onCustomAvatarChange,
  onSimliControllerReady,
  onSimliActiveChange,
  preferredProvider = 'simli',
  isAvatarEnabled = true,
  className = 'w-16 h-16',
}) => {

  const params = useParams()
  const studentId = (params?.id as string) || ''

  // Selected Face ID: default to 80459b57-2d66-4ca7-8682-59e1c649bc53
  const [selectedFaceId, setSelectedFaceId] = useState<string>('80459b57-2d66-4ca7-8682-59e1c649bc53')
  const [activeProvider, setActiveProvider] = useState<AvatarProvider>(preferredProvider)
  const [simliStatus, setSimliStatus] = useState<SimliStatus>('idle')
  const [isMounted, setIsMounted] = useState(false)

  const simliVideoRef = useRef<HTMLVideoElement | null>(null)
  const simliAudioRef = useRef<HTMLAudioElement | null>(null)
  const simliControllerRef = useRef<SimliAvatarController | null>(null)
  const canvasRef = useRef<HTMLCanvasElement | null>(null)

  const isSpeaking = state === 'TEACHER_SPEAKING'
  const isCallActive = state !== 'IDLE' && state !== 'DISCONNECTED' && state !== 'ERROR'
  const isUserTalking = !isSpeaking && !isMuted && userVolume > 0.04
  const isSimliActive = activeProvider === 'simli' && simliStatus === 'connected'

  const onSimliActiveChangeRef = useRef(onSimliActiveChange)
  onSimliActiveChangeRef.current = onSimliActiveChange

  const onSimliControllerReadyRef = useRef(onSimliControllerReady)
  onSimliControllerReadyRef.current = onSimliControllerReady

  const onCustomAvatarChangeRef = useRef(onCustomAvatarChange)
  onCustomAvatarChangeRef.current = onCustomAvatarChange

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
      if (status === 'error' || status === 'fallback') {
        setActiveProvider('google')
      }
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
  const simliEntitlementRef = useRef<boolean | null>(null)
  useEffect(() => {
    if (!isMounted) return

    if (!isAvatarEnabled || !isCallActive) {
      simliControllerRef.current?.stop()
      return
    }

    if (!simliVideoRef.current || !simliAudioRef.current) return

    const controller = simliControllerRef.current
    if (!controller) return

    let cancelled = false
    const startIfEntitled = async () => {
      if (simliEntitlementRef.current === null) {
        try {
          const checkRes = await fetch('/api/avatar/simli', { method: 'GET' })
          if (checkRes.ok) {
            const checkData = await checkRes.json().catch(() => ({}))
            simliEntitlementRef.current = Boolean(checkData?.available)
          } else {
            simliEntitlementRef.current = false
          }
        } catch {
          simliEntitlementRef.current = false
        }
      }

      if (cancelled) return

      if (!simliEntitlementRef.current) {
        setActiveProvider('google')
        setSimliStatus('fallback')
        return
      }

      if (!simliVideoRef.current || !simliAudioRef.current) return
      controller.start({
        videoElement: simliVideoRef.current,
        audioElement: simliAudioRef.current,
        faceId: selectedFaceId,
      })
    }

    startIfEntitled()
    return () => {
      cancelled = true
    }
  }, [isMounted, isCallActive, isAvatarEnabled, selectedFaceId])

  const ringContainerRef = useRef<HTMLDivElement | null>(null)

  // Local decoupled animation loop reading volume levels directly without parent re-renders
  useEffect(() => {
    let animId: number
    const animate = () => {
      const tVol = teacherVolumeRef?.current ?? teacherVolume ?? 0
      const uVol = userVolumeRef?.current ?? userVolume ?? 0
      const isSpeakingNow = state === 'TEACHER_SPEAKING'
      const isUserTalkingNow = !isSpeakingNow && !isMuted && uVol > 0.04
      const level = isSpeakingNow ? tVol : isUserTalkingNow ? uVol : 0
      const scale = 1 + Math.min(level, 1) * 0.12

      if (ringContainerRef.current) {
        ringContainerRef.current.style.transform = `scale(${scale})`
        if (isSpeakingNow) {
          ringContainerRef.current.classList.add('ring-amber-500/60')
          ringContainerRef.current.classList.remove('ring-emerald-500/60', 'ring-stone-200')
        } else if (isUserTalkingNow) {
          ringContainerRef.current.classList.add('ring-emerald-500/60')
          ringContainerRef.current.classList.remove('ring-amber-500/60', 'ring-stone-200')
        } else {
          ringContainerRef.current.classList.add('ring-stone-200')
          ringContainerRef.current.classList.remove('ring-amber-500/60', 'ring-emerald-500/60')
        }
      }
      animId = requestAnimationFrame(animate)
    }
    animId = requestAnimationFrame(animate)
    return () => cancelAnimationFrame(animId)
  }, [state, isMuted, teacherVolumeRef, userVolumeRef, teacherVolume, userVolume])

  const ringColor = isSpeaking ? 'ring-amber-500/60' : 'ring-stone-200'

  const avatarImageUrl = `/avatars/${selectedFaceId}.jpg`

  return (
    <div
      ref={ringContainerRef}
      className={`relative shrink-0 rounded-full bg-stone-100 ring-2 ring-offset-2 ring-offset-[#F8F6F0] overflow-hidden select-none transition-[box-shadow] duration-150 ease-out ${ringColor} ${className}`}
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
          <canvas ref={canvasRef} className="hidden" />
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
        <div className="absolute inset-0 flex items-center justify-center text-xs text-stone-500">Tutor</div>
      )}
      {studentId ? (
        <Link
          href={`/dashboard/${studentId}/settings?tab=avatars`}
          className="sr-only"
          title="Configure Classroom Avatars & Settings"
        >
          <span>Avatars</span>
        </Link>
      ) : null}
    </div>
  )
}
