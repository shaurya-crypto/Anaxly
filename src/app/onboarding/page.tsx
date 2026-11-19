'use client'

import React, { useState, useEffect, useRef } from 'react'
import { useRouter } from 'next/navigation'
import { motion, AnimatePresence } from 'motion/react'
import { createClient } from '@/utils/supabase/client'
import { SobiVectorBot } from '@/components/mascot/SobiVectorBot'
import { completeOnboardingAction, Phase4OnboardingData } from './actions'
import { getLanguageVoiceConfig } from '@/lib/voiceAndLanguageConfig'
import {
  ArrowLeft,
  ArrowRight,
  Volume2,
  VolumeX,
  Loader2,
  Info,
  Mic,
  Square,
  Check,
  Sparkles,
} from 'lucide-react'

// Sparkle Icon matching Aristotle's selection option styling
function SparkleStar({ className = 'w-5 h-5' }: { className?: string }) {
  return (
    <svg
      viewBox="0 0 24 24"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      className={className}
    >
      <defs>
        <linearGradient id="sparkle-grad" x1="2" y1="2" x2="22" y2="22" gradientUnits="userSpaceOnUse">
          <stop offset="0%" stopColor="#3B82F6" />
          <stop offset="60%" stopColor="#255D88" />
          <stop offset="100%" stopColor="#1F3852" />
        </linearGradient>
      </defs>
      <path
        d="M12 2C12 7.5 16.5 12 22 12C16.5 12 12 16.5 12 22C12 16.5 7.5 12 2 12C7.5 12 12 7.5 12 2Z"
        fill="url(#sparkle-grad)"
      />
      <circle cx="18" cy="6" r="1.5" fill="#60A5FA" />
      <circle cx="6" cy="18" r="1.2" fill="#93C5FD" />
    </svg>
  )
}

interface QuestionConfig {
  id: string
  title: string
  subtitle?: string
  sobiExpression: string
  type: 'text' | 'select' | 'voice_selection'
  placeholder?: string
  options?: { value: string; label: string; disabled?: boolean; badge?: string }[]
  audioFile: string
}

// Streamlined 6-step curriculum onboarding questions
const QUESTIONS: QuestionConfig[] = [
  {
    id: 'fullName',
    title: "What's your name?",
    subtitle: 'Let Sobi know who they are pair-learning with',
    sobiExpression: 'joyful-wide',
    type: 'text',
    placeholder: 'Type your name...',
    audioFile: '/q2_name.wav',
  },
  {
    id: 'classLevel',
    title: 'What grade are you in?',
    subtitle: 'Loads your authentic board syllabus from Classes 6 to 12',
    sobiExpression: 'small-attentive',
    type: 'select',
    audioFile: '/q4_class.wav',
    options: [
      { value: 'Class 6', label: '6th grade' },
      { value: 'Class 7', label: '7th grade' },
      { value: 'Class 8', label: '8th grade' },
      { value: 'Class 9', label: '9th grade' },
      { value: 'Class 10', label: '10th grade' },
      { value: 'Class 11', label: '11th grade' },
      { value: 'Class 12', label: '12th grade' },
    ],
  },
  {
    id: 'targetBoard',
    title: 'Which educational board are you studying under?',
    subtitle: 'Selects authentic curriculum format, definitions, and grading rubrics',
    sobiExpression: 'attentive-left',
    type: 'select',
    audioFile: '/q5_board.wav',
    options: [
      { value: 'CBSE', label: 'CBSE (NCERT & Competency-Based Application)' },
      { value: 'ICSE', label: 'ICSE / ISC (Concise Formulations & Deep Precision)' },
      { value: 'IB', label: 'IB (International Baccalaureate)' },
    ],
  },
  {
    id: 'preferredLanguage',
    title: 'Which language do you prefer for your AI tutor?',
    subtitle: 'Language of talking & spoken conversation during class',
    sobiExpression: 'attentive-left',
    type: 'select',
    audioFile: '/q0_language.wav',
    options: [
      { value: 'English', label: 'English (Academic & Conversational English)' },
      { value: 'Hinglish', label: 'Hinglish (Conversational English + Hindi)' },
      { value: 'Hindi', label: 'Hindi (हिंदी — Conversational Hindi)' },
      { value: 'Spanish', label: 'Spanish (Español)' },
      { value: 'French', label: 'French (Français)' },
      { value: 'German', label: 'German (Deutsch)' },
    ],
  },
  {
    id: 'learningPace',
    title: 'How fast do you usually understand new concepts?',
    subtitle: 'Determines pause frequencies and question checkpoints',
    sobiExpression: 'curious-left',
    type: 'select',
    audioFile: '/q7_pace.wav',
    options: [
      { value: 'fast_and_curious', label: 'Fast & curious — give me challenging problems quickly' },
      { value: 'steady_and_balanced', label: 'Steady & balanced — balance concepts with step-by-step examples' },
      { value: 'slow_deep_intuitive', label: 'Deep & intuitive — slow down with real-world analogies first' },
    ],
  },
  {
    id: 'preferredVoice',
    title: "Pick your AI tutor's voice persona",
    subtitle: 'Choose a studio voice persona or clone a parent voice',
    sobiExpression: 'attentive-left',
    type: 'voice_selection',
    audioFile: '/q10_voice.wav',
    options: [
      { value: 'Charon', label: 'Charon — Realistic, calm, authoritative male mentor (Recommended Default)' },
      { value: 'Puck', label: 'Puck — Upbeat, lively, energetic male voice' },
      { value: 'Fenrir', label: 'Fenrir — Confident, energetic, and direct male voice' },
      { value: 'Leda', label: 'Leda — Warm, youthful, natural tone' },
      { value: 'Aoede', label: 'Aoede — Breezy, relaxed, and methodical mentor' },
      { value: 'Kore', label: 'Kore — Crisp, attentive, and academically clear' },
    ],
  },
]

export default function OnboardingPage() {
  const router = useRouter()
  const supabase = createClient()

  // Form State
  const [currentStep, setCurrentStep] = useState(0)
  const [answers, setAnswers] = useState<Record<string, any>>({
    fullName: '',
    classLevel: 'Class 10',
    targetBoard: 'CBSE',
    preferredLanguage: 'English',
    learningPace: 'steady_and_balanced',
    preferredVoice: 'Charon',
    customVoiceKey: null,
  })

  const [reactionExpression, setReactionExpression] = useState<string | undefined>(undefined)
  const [hoverExpression, setHoverExpression] = useState<string | undefined>(undefined)
  const [textInputValue, setTextInputValue] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [isMuted, setIsMuted] = useState(false)
  const [ingestedClasses, setIngestedClasses] = useState<string[]>(['Class 9', 'Class 10', 'Class 11'])
  const [classWarningMessage, setClassWarningMessage] = useState<string | null>(null)
  const textInputRef = useRef<HTMLInputElement | null>(null)

  // Parent Voice Cloning State
  const [isRecording, setIsRecording] = useState(false)
  const [recordedAudioUrl, setRecordedAudioUrl] = useState<string | null>(null)
  const [recordedBase64, setRecordedBase64] = useState<string | null>(null)
  const [recordingSeconds, setRecordingSeconds] = useState(0)
  const [parentConsent, setParentConsent] = useState(false)
  const [isCloningVoice, setIsCloningVoice] = useState(false)
  const [clonedVoiceKey, setClonedVoiceKey] = useState<string | null>(null)
  const mediaRecorderRef = useRef<MediaRecorder | null>(null)
  const audioChunksRef = useRef<Blob[]>([])
  const recordingTimerRef = useRef<any>(null)

  const currentQ = QUESTIONS[currentStep]
  const progressPercent = Math.round(((currentStep + 1) / QUESTIONS.length) * 100)

  // Query database for authentic ingested classes
  useEffect(() => {
    async function loadIngestedClasses() {
      try {
        const { data, error } = await supabase
          .from('curriculums')
          .select('class_level')
          .not('class_level', 'is', null)

        if (!error && data && data.length > 0) {
          const unique = Array.from(
            new Set(data.map((d: any) => d.class_level).filter(Boolean))
          ) as string[]

          unique.sort((a, b) => {
            const numA = parseInt(a.replace(/\D/g, ''), 10) || 0
            const numB = parseInt(b.replace(/\D/g, ''), 10) || 0
            return numA - numB
          })

          if (unique.length > 0) {
            setIngestedClasses(unique)
            setAnswers((prev) => {
              if (!unique.includes(prev.classLevel)) {
                return { ...prev, classLevel: unique[0] }
              }
              return prev
            })
          }
        }
      } catch (err) {
        console.warn('Could not load ingested classes:', err)
      }
    }
    loadIngestedClasses()
  }, [supabase])

  // Pre-populate name if user metadata exists
  useEffect(() => {
    supabase.auth.getUser().then(({ data: { user } }) => {
      if (user?.user_metadata?.full_name && !answers.fullName) {
        setAnswers((prev) => ({
          ...prev,
          fullName: user.user_metadata.full_name,
        }))
        setTextInputValue(user.user_metadata.full_name)
      }
    })
  }, [supabase])

  // Sync text input value on step change
  useEffect(() => {
    if (currentQ.type === 'text') {
      setTextInputValue(answers[currentQ.id] !== undefined ? String(answers[currentQ.id]) : '')
      setTimeout(() => {
        textInputRef.current?.focus()
      }, 150)
    }
  }, [currentStep, currentQ])

  // Clean up recording timer on unmount
  useEffect(() => {
    return () => {
      if (recordingTimerRef.current) clearInterval(recordingTimerRef.current)
    }
  }, [])

  // Start parent voice recording
  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
      audioChunksRef.current = []
      const recorder = new MediaRecorder(stream)
      mediaRecorderRef.current = recorder

      recorder.ondataavailable = (e) => {
        if (e.data.size > 0) audioChunksRef.current.push(e.data)
      }

      recorder.onstop = () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/wav' })
        const url = URL.createObjectURL(audioBlob)
        setRecordedAudioUrl(url)

        const reader = new FileReader()
        reader.onloadend = () => {
          const base64 = reader.result as string
          setRecordedBase64(base64)
        }
        reader.readAsDataURL(audioBlob)

        stream.getTracks().forEach((track) => track.stop())
      }

      recorder.start()
      setIsRecording(true)
      setRecordingSeconds(0)
      recordingTimerRef.current = setInterval(() => {
        setRecordingSeconds((prev) => {
          if (prev >= 20) {
            stopRecording()
            return prev
          }
          return prev + 1
        })
      }, 1000)
    } catch {
      alert('Microphone access is required to record a voice sample.')
    }
  }

  // Stop parent voice recording
  const stopRecording = () => {
    if (mediaRecorderRef.current && mediaRecorderRef.current.state !== 'inactive') {
      mediaRecorderRef.current.stop()
    }
    setIsRecording(false)
    if (recordingTimerRef.current) clearInterval(recordingTimerRef.current)
  }

  // Submit voice clone request
  const handleCloneVoice = async () => {
    if (!recordedBase64 || !parentConsent) return
    setIsCloningVoice(true)
    try {
      const res = await fetch('/api/voice/replicate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ audioSample: recordedBase64 }),
      })
      const data = await res.json()
      if (data.voiceKey) {
        setClonedVoiceKey(data.voiceKey)
        setAnswers((prev) => ({ ...prev, customVoiceKey: data.voiceKey, preferredVoice: 'Charon' }))
      }
    } catch (err) {
      console.warn('Voice replication fallback:', err)
    } finally {
      setIsCloningVoice(false)
    }
  }

  // Advance to next question or submit
  const handleNext = async (customValue?: any) => {
    const valueToSave = customValue !== undefined ? customValue : textInputValue

    if (currentQ.id === 'classLevel' && typeof valueToSave === 'string') {
      const isIngested = ingestedClasses.includes(valueToSave)
      if (!isIngested) {
        const formattedClasses = ingestedClasses.join(', ')
        setClassWarningMessage(
          `This is in prototype. We have only ingested ${formattedClasses}. Please select that.`
        )
        setReactionExpression('gentle-downward-gaze')
        return
      }
      setClassWarningMessage(null)
    }

    setReactionExpression('joyful-wide')
    setTimeout(() => {
      setReactionExpression(undefined)
    }, 700)

    const updatedAnswers = {
      ...answers,
      [currentQ.id]: valueToSave,
    }

    if (currentQ.id === 'preferredLanguage' && typeof valueToSave === 'string') {
      const langConfig = getLanguageVoiceConfig(valueToSave)
      updatedAnswers.preferredVoice = langConfig.defaultVoice || 'Charon'
    }

    setAnswers(updatedAnswers)

    if (currentStep < QUESTIONS.length - 1) {
      setCurrentStep((prev) => prev + 1)
    } else {
      await submitOnboarding(updatedAnswers)
    }
  }

  const handleBack = () => {
    setClassWarningMessage(null)
    if (currentStep > 0) {
      setCurrentStep((prev) => prev - 1)
    }
  }

  const handleSkip = () => {
    setClassWarningMessage(null)
    if (currentStep < QUESTIONS.length - 1) {
      setCurrentStep((prev) => prev + 1)
    } else {
      // Default to Charon on skip
      const finalAnswers = { ...answers, preferredVoice: 'Charon' }
      submitOnboarding(finalAnswers)
    }
  }

  const handleSkipToDefaultMaleVoice = async () => {
    const finalAnswers = { ...answers, preferredVoice: 'Charon', customVoiceKey: null }
    setAnswers(finalAnswers)
    await submitOnboarding(finalAnswers)
  }

  const submitOnboarding = async (dataToSubmit: Record<string, any>) => {
    setIsSubmitting(true)
    const payload: Phase4OnboardingData = {
      fullName: dataToSubmit.fullName || 'Student',
      classLevel: dataToSubmit.classLevel || 'Class 10',
      targetBoard: dataToSubmit.targetBoard || 'CBSE',
      preferredLanguage: dataToSubmit.preferredLanguage || 'English',
      learningPace: dataToSubmit.learningPace || 'steady_and_balanced',
      preferredVoice: dataToSubmit.preferredVoice || 'Charon',
      customVoiceKey: dataToSubmit.customVoiceKey || clonedVoiceKey || undefined,
    }

    const res = await completeOnboardingAction(payload)
    if (res?.error) {
      if (res.error.includes('Authentication required')) {
        if (typeof window !== 'undefined') {
          localStorage.setItem('pending_onboarding', JSON.stringify(payload))
        }
        router.push('/login')
        return
      }
      alert(res.error)
      setIsSubmitting(false)
    }
  }

  const handleTextFormSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (!textInputValue.trim() || isSubmitting) return
    handleNext(textInputValue.trim())
  }

  const activeSobiExpression =
    reactionExpression ||
    hoverExpression ||
    (textInputValue.trim().length > 0 ? 'downward-gaze' : currentQ.sobiExpression)

  return (
    <div className="relative min-h-screen w-full bg-[var(--canvas-base)] text-[var(--ink-primary)] overflow-hidden flex flex-col font-sans select-none">
      {/* Paper Grid Canvas Background */}
      <div
        className="pointer-events-none absolute inset-0 z-0 opacity-40"
        style={{
          backgroundImage: `
            linear-gradient(to right, var(--border-subtle) 1px, transparent 1px),
            linear-gradient(to bottom, var(--border-subtle) 1px, transparent 1px)
          `,
          backgroundSize: '24px 24px',
        }}
      />

      {/* 1. Header Toolbar */}
      <header className="relative z-20 flex h-16 w-full items-center justify-between px-6 sm:px-10">
        <div className="flex items-center gap-3">
          {currentStep > 0 && (
            <button
              type="button"
              onClick={handleBack}
              disabled={isSubmitting}
              className="flex h-9 w-9 items-center justify-center rounded-xl border border-[var(--border-subtle)] bg-white/80 text-[var(--ink-secondary)] shadow-xs transition-all hover:bg-white hover:text-[var(--ink-primary)] active:scale-95 disabled:opacity-50 cursor-pointer"
              aria-label="Previous question"
            >
              <ArrowLeft className="h-4 w-4" />
            </button>
          )}
        </div>

        {/* Minimal Progress Bar (Top Center) */}
        <div className="w-48 sm:w-64">
          <div className="h-1.5 w-full overflow-hidden rounded-full bg-[var(--border-subtle)]">
            <motion.div
              className="h-full bg-[var(--accent-primary)] rounded-full"
              initial={{ width: 0 }}
              animate={{ width: `${progressPercent}%` }}
              transition={{ duration: 0.35, ease: 'easeOut' }}
            />
          </div>
        </div>

        <div className="flex items-center gap-2">
          <button
            type="button"
            onClick={() => setIsMuted(!isMuted)}
            className="flex h-9 w-9 items-center justify-center rounded-xl border border-[var(--border-subtle)] bg-white/80 text-[var(--ink-secondary)] shadow-xs transition-all hover:bg-white hover:text-[var(--ink-primary)] active:scale-95 cursor-pointer"
            title={isMuted ? 'Unmute voice questions' : 'Mute voice questions'}
            aria-label="Toggle voice"
          >
            {isMuted ? <VolumeX className="h-4 w-4" /> : <Volume2 className="h-4 w-4" />}
          </button>
          <button
            type="button"
            onClick={handleSkip}
            disabled={isSubmitting}
            className="text-sm font-medium text-[var(--ink-muted)] transition-colors hover:text-[var(--ink-primary)] cursor-pointer"
          >
            Skip
          </button>
        </div>
      </header>

      {/* 2. Main Question Area */}
      <main className="relative z-10 flex flex-1 flex-col items-center justify-center px-4 pb-28 pt-2">
        <AnimatePresence mode="wait">
          {/* A. TEXT INPUT MODE */}
          {currentQ.type === 'text' && (
            <motion.div
              key={`q-text-${currentQ.id}`}
              initial={{ opacity: 0, y: 14 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -14 }}
              transition={{ duration: 0.25 }}
              className="flex flex-col items-center justify-center"
            >
              <SobiVectorBot
                message={currentQ.title}
                subtitle={currentQ.subtitle}
                bubblePosition="top"
                audioSrc={currentQ.audioFile}
                isMuted={isMuted}
                onToggleMute={() => setIsMuted(!isMuted)}
                size={140}
                lookAt="input"
                expression={activeSobiExpression}
                isTyping={textInputValue.trim().length > 0}
              />
            </motion.div>
          )}

          {/* B. OPTION SELECTION MODE */}
          {currentQ.type === 'select' && (
            <motion.div
              key={`q-select-${currentQ.id}`}
              initial={{ opacity: 0, y: 14 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -14 }}
              transition={{ duration: 0.25 }}
              className="flex w-full max-w-[560px] flex-col items-center"
            >
              <div className="mb-6 flex w-full items-center justify-start pl-2">
                <SobiVectorBot
                  message={currentQ.title}
                  subtitle={currentQ.subtitle}
                  bubblePosition="right"
                  audioSrc={currentQ.audioFile}
                  isMuted={isMuted}
                  onToggleMute={() => setIsMuted(!isMuted)}
                  size={105}
                  lookAt="cursor"
                  expression={activeSobiExpression}
                />
              </div>

              <div className="w-full rounded-2xl border border-[var(--border-subtle)] bg-white/95 p-3.5 shadow-xs backdrop-blur-sm max-h-[58vh] overflow-y-auto">
                {classWarningMessage && currentQ.id === 'classLevel' && (
                  <motion.div
                    initial={{ opacity: 0, y: -6 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="mb-3.5 flex items-start gap-2.5 rounded-xl border border-[var(--accent-warm-border)] bg-[var(--accent-warm-soft)] px-3.5 py-3 text-xs text-[var(--accent-warm)] shadow-xs"
                  >
                    <Info className="h-4 w-4 shrink-0 mt-0.5" />
                    <span className="font-medium leading-relaxed">{classWarningMessage}</span>
                  </motion.div>
                )}

                <div className="flex flex-col gap-2.5">
                  {currentQ.options?.map((opt) => {
                    const isSelected = answers[currentQ.id] === opt.value
                    const isDisabled = !!opt.disabled
                    const isClassQuestion = currentQ.id === 'classLevel'
                    const isClassIngested = isClassQuestion ? ingestedClasses.includes(opt.value) : true
                    const displayBadge =
                      opt.badge ||
                      (isClassQuestion ? (isClassIngested ? 'Ready' : 'Prototype') : undefined)

                    return (
                      <button
                        key={opt.value}
                        type="button"
                        disabled={isDisabled}
                        onClick={() => {
                          if (!isDisabled) handleNext(opt.value)
                        }}
                        onMouseEnter={() => !isDisabled && setHoverExpression('attentive-left')}
                        onMouseLeave={() => !isDisabled && setHoverExpression(undefined)}
                        className={`group flex w-full items-center justify-between gap-3.5 rounded-xl border px-4 py-3.5 text-left transition-all cursor-pointer ${
                          isDisabled
                            ? 'cursor-not-allowed border-[var(--border-subtle)] bg-[var(--canvas-soft)] opacity-60'
                            : isSelected
                            ? 'border-[var(--accent-primary)] bg-[var(--accent-primary-soft)] shadow-xs'
                            : 'border-[var(--border-subtle)] bg-white hover:border-[var(--border-strong)] hover:bg-[var(--canvas-soft)]'
                        }`}
                      >
                        <div className="flex items-center gap-3.5">
                          <SparkleStar className="h-5 w-5 shrink-0 transition-transform group-hover:scale-110" />
                          <span className="text-[15px] font-medium text-[var(--ink-primary)]">
                            {opt.label}
                          </span>
                        </div>
                        {displayBadge && (
                          <span className="shrink-0 rounded-full border border-[var(--accent-warm-border)] bg-[var(--accent-warm-soft)] px-2.5 py-0.5 text-xs font-semibold text-[var(--accent-warm)]">
                            {displayBadge}
                          </span>
                        )}
                      </button>
                    )
                  })}
                </div>
              </div>
            </motion.div>
          )}

          {/* C. STEP 6: VOICE PERSONA + PARENT VOICE CLONING CARD */}
          {currentQ.type === 'voice_selection' && (
            <motion.div
              key="q-voice-persona"
              initial={{ opacity: 0, y: 14 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -14 }}
              transition={{ duration: 0.25 }}
              className="flex w-full max-w-[620px] flex-col items-center gap-4 max-h-[72vh] overflow-y-auto pr-1"
            >
              <div className="flex w-full items-center justify-start pl-2">
                <SobiVectorBot
                  message="Pick your teacher's voice persona"
                  subtitle="Default realistic male voice (Charon), or optionally clone parent's voice"
                  bubblePosition="right"
                  audioSrc={currentQ.audioFile}
                  isMuted={isMuted}
                  onToggleMute={() => setIsMuted(!isMuted)}
                  size={105}
                  lookAt="cursor"
                  expression={activeSobiExpression}
                />
              </div>

              {/* Fast-track: One-Click Skip to Default Male Voice */}
              <div className="w-full flex items-center justify-between p-3.5 rounded-2xl bg-white border border-[var(--border-subtle)] shadow-xs">
                <div>
                  <h4 className="text-sm font-semibold text-[var(--ink-primary)]">
                    Default Realistic Male Voice (Charon)
                  </h4>
                  <p className="text-xs text-[var(--ink-secondary)]">
                    Calm, patient, authoritative master mentor. No setup required.
                  </p>
                </div>
                <button
                  type="button"
                  onClick={handleSkipToDefaultMaleVoice}
                  disabled={isSubmitting}
                  className="px-4 py-2 rounded-xl bg-[var(--accent-primary)] hover:bg-[var(--accent-primary-hover)] text-white text-xs font-semibold shadow-xs transition-all cursor-pointer whitespace-nowrap"
                >
                  Use Charon (Default)
                </button>
              </div>

              {/* Optional Parent Voice Cloning Feature Card */}
              <div className="w-full rounded-2xl border border-[var(--accent-warm-border)] bg-[var(--accent-warm-soft)]/50 p-4 sm:p-5 shadow-xs space-y-3.5">
                <div className="flex items-center gap-2 text-[var(--accent-warm)]">
                  <Sparkles className="w-4 h-4" />
                  <h3 className="text-sm font-bold tracking-tight">
                    Optional: Clone Parent Voice for Teacher
                  </h3>
                </div>
                <p className="text-xs text-[var(--ink-secondary)] leading-relaxed">
                  Record a 10–20 second audio sample of parent reading any textbook sentence. The AI tutor can synthesize lessons in this familiar parental voice.
                </p>

                {/* Recorder Controls */}
                <div className="flex flex-wrap items-center gap-3 pt-1">
                  {!isRecording ? (
                    <button
                      type="button"
                      onClick={startRecording}
                      className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-white border border-[var(--border-strong)] text-xs font-semibold text-[var(--ink-primary)] hover:bg-[var(--canvas-soft)] transition-colors cursor-pointer"
                    >
                      <Mic className="w-4 h-4 text-[var(--accent-warm)]" />
                      <span>{recordedAudioUrl ? 'Record Again' : 'Record Voice Sample (10-20s)'}</span>
                    </button>
                  ) : (
                    <button
                      type="button"
                      onClick={stopRecording}
                      className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-red-600 text-white text-xs font-semibold hover:bg-red-700 transition-colors cursor-pointer animate-pulse"
                    >
                      <Square className="w-4 h-4 fill-current" />
                      <span>Stop Recording ({recordingSeconds}s)</span>
                    </button>
                  )}

                  {recordedAudioUrl && !isRecording && (
                    <audio src={recordedAudioUrl} controls className="h-8 max-w-[200px]" />
                  )}
                </div>

                {/* Parent Consent Checkbox */}
                {recordedAudioUrl && (
                  <div className="space-y-2 pt-2 border-t border-[var(--border-subtle)]">
                    <label className="flex items-start gap-2.5 cursor-pointer text-xs text-[var(--ink-secondary)]">
                      <input
                        type="checkbox"
                        checked={parentConsent}
                        onChange={(e) => setParentConsent(e.target.checked)}
                        className="mt-0.5 rounded border-[var(--border-strong)] text-[var(--accent-primary)] focus:ring-[var(--accent-primary)]"
                      />
                      <span>
                        I confirm that I am the parent/guardian and I give consent to replicate this voice for personalized tutoring.
                      </span>
                    </label>

                    <button
                      type="button"
                      disabled={!parentConsent || isCloningVoice || !!clonedVoiceKey}
                      onClick={handleCloneVoice}
                      className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-[var(--accent-warm)] hover:bg-[var(--accent-warm-hover)] text-white text-xs font-semibold disabled:opacity-50 transition-colors cursor-pointer"
                    >
                      {isCloningVoice ? (
                        <>
                          <Loader2 className="w-3.5 h-3.5 animate-spin" />
                          <span>Generating Voice Model...</span>
                        </>
                      ) : clonedVoiceKey ? (
                        <>
                          <Check className="w-3.5 h-3.5" />
                          <span>Voice Model Ready & Bound</span>
                        </>
                      ) : (
                        <span>Generate & Bind Parent Voice</span>
                      )}
                    </button>

                    {clonedVoiceKey && (
                      <p className="text-xs font-medium text-[var(--accent-warm)] flex items-center gap-1.5">
                        <Check className="w-3.5 h-3.5" />
                        Parent voice key minted: <span className="font-mono text-xs">{clonedVoiceKey.slice(0, 18)}...</span>
                      </p>
                    )}
                  </div>
                )}
              </div>

              {/* Or Select Prebuilt Studio Voice */}
              <div className="w-full rounded-2xl border border-[var(--border-subtle)] bg-white/95 p-3.5 shadow-xs space-y-2">
                <span className="text-xs font-bold text-[var(--ink-muted)]">
                  Or select a studio persona:
                </span>
                <div className="flex flex-col gap-2">
                  {currentQ.options?.map((opt) => {
                    const isSelected = answers.preferredVoice === opt.value
                    return (
                      <button
                        key={opt.value}
                        type="button"
                        onClick={() => {
                          setAnswers((prev) => ({ ...prev, preferredVoice: opt.value }))
                        }}
                        className={`flex w-full items-center justify-between p-3 rounded-xl border text-left text-xs font-medium transition-all cursor-pointer ${
                          isSelected
                            ? 'border-[var(--accent-primary)] bg-[var(--accent-primary-soft)] text-[var(--ink-primary)] font-semibold'
                            : 'border-[var(--border-subtle)] bg-white hover:bg-[var(--canvas-soft)] text-[var(--ink-secondary)]'
                        }`}
                      >
                        <span>{opt.label}</span>
                        {isSelected && <Check className="w-4 h-4 text-[var(--accent-primary)]" />}
                      </button>
                    )
                  })}
                </div>
              </div>

              {/* Final Submit Button */}
              <button
                type="button"
                onClick={() => submitOnboarding(answers)}
                disabled={isSubmitting}
                className="w-full py-3.5 px-6 rounded-2xl bg-[var(--accent-primary)] hover:bg-[var(--accent-primary-hover)] text-white text-sm font-semibold shadow-xs transition-all active:scale-[0.99] cursor-pointer flex items-center justify-center gap-2"
              >
                {isSubmitting ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    <span>Finalizing Classroom...</span>
                  </>
                ) : (
                  <>
                    <span>Go to my classroom</span>
                    <ArrowRight className="w-4 h-4" />
                  </>
                )}
              </button>
            </motion.div>
          )}
        </AnimatePresence>
      </main>

      {/* 3. Bottom Pill Input (For Text Questions) */}
      {currentQ.type === 'text' && (
        <footer className="fixed bottom-10 left-1/2 z-30 w-full max-w-[480px] -translate-x-1/2 px-4">
          <form
            onSubmit={handleTextFormSubmit}
            className="flex items-center rounded-2xl border-2 border-[var(--accent-primary)] bg-white px-4 py-2.5 shadow-md transition-all focus-within:ring-2 focus-within:ring-[var(--accent-primary)]/20"
          >
            <input
              ref={textInputRef}
              type="text"
              value={textInputValue}
              onChange={(e) => setTextInputValue(e.target.value)}
              placeholder={currentQ.placeholder}
              className="flex-1 bg-transparent text-[15px] text-[var(--ink-primary)] placeholder:text-[var(--ink-muted)] focus:outline-none"
            />
            <button
              type="submit"
              disabled={!textInputValue.trim() || isSubmitting}
              className="ml-2 flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-[var(--accent-primary)] text-white transition-all hover:bg-[var(--accent-primary-hover)] active:scale-95 disabled:opacity-30 disabled:pointer-events-none cursor-pointer"
              aria-label="Submit answer"
            >
              {isSubmitting ? (
                <Loader2 className="h-4 w-4 animate-spin text-white" />
              ) : (
                <ArrowRight className="h-4 w-4" />
              )}
            </button>
          </form>
        </footer>
      )}

      {/* Global submission overlay if submitting */}
      {isSubmitting && (
        <div className="fixed inset-0 z-50 flex flex-col items-center justify-center bg-white/70 backdrop-blur-sm">
          <Loader2 className="h-8 w-8 animate-spin text-[var(--accent-primary)] mb-3" />
          <p className="text-sm font-medium text-[var(--ink-secondary)]">
            Setting up your personalized classroom...
          </p>
        </div>
      )}
    </div>
  )
}
