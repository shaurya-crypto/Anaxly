'use client'

import React from 'react'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import { ArrowLeft, Home, LogIn } from 'lucide-react'

export default function NotFound() {
  const router = useRouter()

  return (
    <div className="min-h-screen bg-[var(--canvas-base)] flex flex-col items-center justify-center p-6 text-center">
      <div className="w-16 h-16 rounded-2xl bg-[var(--accent-sage-soft)] border border-[var(--accent-sage)]/20 flex items-center justify-center text-[var(--accent-sage)] mb-4 shadow-xs">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
          <path d="M12 2C6.5 2 2 6.5 2 12c0 5 3.5 9 8.5 9.8" />
          <path d="M12 2c5.5 0 10 4.5 10 10 0 5.5-4.5 10-10 10-1.5 0-3-.5-4-1" />
          <path d="M12 2v20" />
        </svg>
      </div>
      <h2 className="font-serif text-3xl text-[var(--ink-primary)] mb-2">Page Not Found</h2>
      <p className="text-sm text-[var(--ink-secondary)] max-w-sm mb-6">
        The classroom or module you are looking for does not exist or has been relocated.
      </p>

      <div className="flex flex-col sm:flex-row items-center gap-3">
        <button
          onClick={() => {
            if (typeof window !== 'undefined' && window.history.length > 1) {
              window.history.back()
            } else {
              router.push('/dashboard')
            }
          }}
          className="inline-flex items-center justify-center gap-2 rounded-xl bg-white hover:bg-stone-50 border border-[var(--border-subtle)] text-[var(--ink-primary)] px-4 py-2.5 text-sm font-medium transition-colors shadow-2xs cursor-pointer"
        >
          <ArrowLeft className="w-4 h-4" />
          Go Back
        </button>

        <Link
          href="/dashboard"
          className="inline-flex items-center justify-center gap-2 rounded-xl bg-[var(--accent-warm)] hover:bg-[var(--accent-warm-hover)] text-white px-5 py-2.5 text-sm font-medium transition-colors shadow-xs"
        >
          <Home className="w-4 h-4" />
          Return to Dashboard
        </Link>
      </div>

      <div className="mt-6 text-xs text-[var(--ink-muted)]">
        Need to sign in again?{' '}
        <Link href="/login" className="text-[var(--accent-warm)] hover:underline inline-flex items-center gap-1 font-medium">
          <LogIn className="w-3 h-3 inline" />
          Portal Login
        </Link>
      </div>
    </div>
  )
}
