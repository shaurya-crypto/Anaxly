'use client'

import React, { useState } from 'react'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import Script from 'next/script'
import {
  Check,
  ArrowRight,
  HelpCircle,
  Star,
  Users,
  Tv,
  Clock,
  CreditCard,
  X,
} from 'lucide-react'
import { LandingNav } from '@/components/landing/LandingNav'
import { LandingFooter } from '@/components/landing/LandingFooter'
import {
  HairlineHeroIllustration,
  HairlineFreeCrest,
  HairlineScholarCrest,
  HairlineTopperCrest,
  HairlineMasteryCrest,
} from '@/components/pricing/HairlinePricingIllustration'

interface PricingPlan {
  id: string
  name: string
  badge?: string
  popular?: boolean
  description: string
  monthlyPrice: number
  annualPrice: number
  priceSuffix: string
  annualSavings: string
  crest: React.ReactNode
  featuresHeader: string
  features: {
    text: string
    highlight?: boolean
    freeHighlight?: boolean
  }[]
  ctaText: string
  ctaHref: string
  ctaVariant: 'secondary' | 'primary' | 'outline'
}

interface ComparisonFeature {
  title: string
  free: string | boolean
  scholar: string | boolean
  topper: string | boolean
  mastery: string | boolean
}

function loadRazorpaySdk(): Promise<boolean> {
  return new Promise((resolve) => {
    if (typeof window !== 'undefined' && (window as any).Razorpay) {
      resolve(true)
      return
    }
    const existing = document.querySelector('script[src*="checkout.razorpay.com"]')
    if (existing) {
      existing.addEventListener('load', () => resolve(true))
      existing.addEventListener('error', () => resolve(false))
      setTimeout(() => {
        resolve(typeof window !== 'undefined' && !!(window as any).Razorpay)
      }, 1500)
      return
    }
    const script = document.createElement('script')
    script.src = 'https://checkout.razorpay.com/v1/checkout.js'
    script.async = true
    script.onload = () => resolve(true)
    script.onerror = () => resolve(false)
    document.body.appendChild(script)
  })
}

export default function PricingPage() {
  const [billingCycle, setBillingCycle] = useState<'monthly' | 'annual'>('annual')
  const [openFaqIndex, setOpenFaqIndex] = useState<number | null>(null)

  const plans: PricingPlan[] = [
    {
      id: 'free',
      name: 'Chalkboard Free',
      description: 'The ultimate visual discovery engine. Interactive digital chalkboard and dynamic science diagrams forever.',
      monthlyPrice: 0,
      annualPrice: 0,
      priceSuffix: 'forever',
      annualSavings: '',
      crest: <HairlineFreeCrest />,
      featuresHeader: 'TOP 5 HIGHLIGHTS:',
      features: [
        {
          text: 'Interactive Digital Chalkboard & Derivations (100% Free)',
          freeHighlight: true,
        },
        {
          text: 'Dynamic Science Diagrams & Math Graphs (100% Free)',
          freeHighlight: true,
        },
        {
          text: '3 Live Socratic Classes / month (~1 hour total)',
        },
        {
          text: '3 Quick Last-Minute Summaries / month',
        },
        {
          text: 'CBSE, ICSE & IB Core Curriculum standards',
        },
      ],
      ctaText: 'Get Started Free',
      ctaHref: '/onboarding',
      ctaVariant: 'outline',
    },
    {
      id: 'scholar',
      name: 'Scholar',
      badge: 'Syllabus Completion',
      description: '1-on-1 Socratic Audio Tutor guaranteeing complete school syllabus coverage if taken properly.',
      monthlyPrice: 499,
      annualPrice: 399,
      priceSuffix: '/ month',
      annualSavings: '₹4,788 billed annually (Save 20%)',
      crest: <HairlineScholarCrest />,
      featuresHeader: 'TOP 5 HIGHLIGHTS:',
      features: [
        {
          text: 'Interactive Chalkboard & Math Graphs (100% Free)',
          freeHighlight: true,
        },
        {
          text: '8 Live Socratic Classes / month (80 classes over term)',
          highlight: true,
        },
        {
          text: 'Guaranteed School Syllabus Coverage (Maths & Science)',
          highlight: true,
        },
        {
          text: 'Unlimited Quick Last-Minute Summaries & Flashcards',
        },
        {
          text: 'Downloadable Unwatermarked Clean PDF Master Notes',
        },
      ],
      ctaText: 'Start Scholar Plan',
      ctaHref: '/onboarding?plan=scholar',
      ctaVariant: 'secondary',
    },
    {
      id: 'topper',
      name: 'Topper Pro',
      badge: 'Most Popular',
      popular: true,
      description: 'Face-to-face live video tutoring for 100% of your classes, past exam solver & exam blitz.',
      monthlyPrice: 1099,
      annualPrice: 899,
      priceSuffix: '/ month',
      annualSavings: '₹10,788 billed annually (Save 18%)',
      crest: <HairlineTopperCrest />,
      featuresHeader: 'TOP 5 HIGHLIGHTS:',
      features: [
        {
          text: '15 Live Classes / month — ALL with Face-to-Face Video Teacher',
          highlight: true,
        },
        {
          text: '150 Live Face-to-Face Video Classes across the school academic year',
          highlight: true,
        },
        {
          text: 'Full 10-Year Board PYQ Solver with Step-by-Step Marking Keys',
          highlight: true,
        },
        {
          text: '10-Minute Morning High-Yield Exam Blitz Mode',
          highlight: true,
        },
        {
          text: 'Interactive Chalkboard & Visual Diagrams (100% Free)',
          freeHighlight: true,
        },
      ],
      ctaText: 'Start Topper Pro',
      ctaHref: '/onboarding?plan=topper',
      ctaVariant: 'primary',
    },
    {
      id: 'elite',
      name: 'Mastery Infinity',
      badge: 'Ultimate Academic Shield',
      description: 'Nearly daily 1-on-1 live video tutoring, notebook camera homework diagnostics & parent WhatsApp reports.',
      monthlyPrice: 1999,
      annualPrice: 1499,
      priceSuffix: '/ month',
      annualSavings: '₹17,988 billed annually (Save 25%)',
      crest: <HairlineMasteryCrest />,
      featuresHeader: 'TOP 5 HIGHLIGHTS:',
      features: [
        {
          text: '24 Live Classes / month — ALL with Face-to-Face Video Teacher',
          highlight: true,
        },
        {
          text: '240 Live Face-to-Face Video Classes across the school academic year',
          highlight: true,
        },
        {
          text: 'Notebook Camera Step-by-Step Homework Error Check',
          highlight: true,
        },
        {
          text: 'Timed Board Mock Exam Simulator with Automated Grading',
          highlight: true,
        },
        {
          text: 'Parent WhatsApp Weekly Progress Card & All Boards Prep',
        },
      ],
      ctaText: 'Join Mastery Infinity',
      ctaHref: '/onboarding?plan=elite',
      ctaVariant: 'secondary',
    },
  ]

  // Continuous Granular Features List (Dividing category rows removed per user request)
  const allGranularFeatures: ComparisonFeature[] = [
    {
      title: 'Interactive Digital Chalkboard & Derivations',
      free: '100% Free',
      scholar: '100% Free',
      topper: '100% Free',
      mastery: '100% Free',
    },
    {
      title: 'Dynamic Coordinate & Math Function Graphs',
      free: '100% Free',
      scholar: '100% Free',
      topper: '100% Free',
      mastery: '100% Free',
    },
    {
      title: 'Animated Science Diagrams & Experiments',
      free: '100% Free',
      scholar: '100% Free',
      topper: '100% Free',
      mastery: '100% Free',
    },
    {
      title: 'Monthly Live Socratic Classes',
      free: '3 Classes / mo',
      scholar: '8 Classes / mo',
      topper: '15 Classes / mo',
      mastery: '24 Classes / mo',
    },
    {
      title: 'Total Classes Over School Academic Term',
      free: '30 Classes',
      scholar: '80 Classes',
      topper: '150 Classes',
      mastery: '240 Classes',
    },
    {
      title: 'Face-to-Face Live AI Video Teacher',
      free: false,
      scholar: false,
      topper: '100% of All Classes',
      mastery: '100% of All Classes',
    },
    {
      title: 'Guaranteed School Syllabus Completion',
      free: false,
      scholar: true,
      topper: true,
      mastery: true,
    },
    {
      title: 'Instant Speech Barge-in & Conversational Interruption',
      free: true,
      scholar: true,
      topper: true,
      mastery: true,
    },
    {
      title: '60-Second Last-Minute Revision Summaries',
      free: '3 / month',
      scholar: 'Unlimited',
      topper: 'Unlimited',
      mastery: 'Unlimited',
    },
    {
      title: 'Smart Memory Revision Flashcards',
      free: '1 Demo Deck',
      scholar: 'Unlimited',
      topper: 'Unlimited',
      mastery: 'Unlimited',
    },
    {
      title: 'Authentic Past Year Question (PYQ) Solver',
      free: '5 Previews',
      scholar: '30 / chapter',
      topper: '10-Year Bank',
      mastery: '10-Year + Predicted',
    },
    {
      title: '10-Minute Morning Exam Blitz Sprint Mode',
      free: false,
      scholar: false,
      topper: true,
      mastery: true,
    },
    {
      title: 'Timed Board Mock Exam with Handwriting Grading',
      free: false,
      scholar: false,
      topper: false,
      mastery: true,
    },
    {
      title: 'Notebook Camera Step-by-Step Error Check',
      free: false,
      scholar: false,
      topper: false,
      mastery: true,
    },
    {
      title: 'CBSE NCERT Textbook Curriculum Standards',
      free: true,
      scholar: true,
      topper: true,
      mastery: true,
    },
    {
      title: 'ICSE Selina Concise & Dual-Column Rough Work',
      free: false,
      scholar: 'Single Board',
      topper: 'Single Board',
      mastery: 'All Boards',
    },
    {
      title: 'IB Curriculum Alignment & Formula Guides',
      free: false,
      scholar: 'Single Board',
      topper: 'Single Board',
      mastery: 'All Boards',
    },
    {
      title: 'Clean Unwatermarked Master Notes PDF Export',
      free: false,
      scholar: true,
      topper: true,
      mastery: true,
    },
    {
      title: 'Parent WhatsApp Weekly Academic Progress Card',
      free: false,
      scholar: false,
      topper: false,
      mastery: true,
    },
  ]

  const alternativesComparison = [
    {
      dimension: 'Teaching Format',
      youtube: '1 Teacher to Millions (Passive Video)',
      pw: '1 Teacher to 5,000–50,000 (Chat Stream)',
      tutor: '1 Private Offline Home Tutor',
      anaxly: 'True 1-on-1 Socratic Dialogue (Teacher speaks directly to your child)',
    },
    {
      dimension: 'Student Attention & Doubt Resolution',
      youtube: 'Zero interaction. Distracted by recommendations & shorts.',
      pw: 'Impossible in live class. Comments move too fast to read.',
      tutor: 'Depends on tutor patience. Often repeats without visual intuition.',
      anaxly: 'Tutor pauses every 2 mins to check understanding on the chalkboard.',
    },
    {
      dimension: 'Derivation & Step-by-Step Method',
      youtube: 'Passive screen watching with pre-written slides.',
      pw: 'Rapid slide progression; child falls behind copying notes.',
      tutor: 'Handwritten on paper, lacks interactive graphs.',
      anaxly: 'Trio Combo (Given -> Formula -> Substitution -> Boxed Answer with SI units).',
    },
    {
      dimension: 'School Syllabus Completion',
      youtube: 'Unstructured, leaves critical textbook exercise questions unworked.',
      pw: 'Paced for competitive JEE/NEET, skips school textbook nuances.',
      tutor: 'Slow and inconsistent pacing before school term examinations.',
      anaxly: 'Systematic 10-month schedule covering all textbook chapters & exercises.',
    },
    {
      dimension: 'Interactive Visual Chalkboard',
      youtube: 'Static video frames.',
      pw: 'Static smartboard recording.',
      tutor: 'Standard notebook paper.',
      anaxly: '100% Free Forever interactive chalkboard with dynamic coordinate graphs.',
    },
    {
      dimension: 'Parent Visibility',
      youtube: 'Zero visibility into child screen time.',
      pw: 'Generic portal logins rarely opened by parents.',
      tutor: 'Occasional informal parent updates.',
      anaxly: 'Automated weekly WhatsApp report with attendance & concept mastery.',
    },
    {
      dimension: 'Monthly Cost (INR)',
      youtube: 'Free (Costly in lost focus & bad study habits)',
      pw: '₹3,500 – ₹5,000 / year (Passive group broadcast)',
      tutor: '₹6,000 – ₹12,000 / month (High expense & travel)',
      anaxly: '₹399 – ₹899 / month (Private 1-on-1 Socratic quality at 1/4th the cost)',
    },
  ]

  const faqs = [
    {
      q: 'Why are the Digital Whiteboard and Visualizations 100% free on every plan?',
      a: 'We believe genuine understanding happens through visual proof and active problem-solving, not passive video lectures. Our interactive chalkboard, animated science diagrams, and coordinate math graph tools are 100% free forever to every student in India.',
    },
    {
      q: 'How does the Live AI Avatar video tutoring work in Topper Pro & Mastery?',
      a: 'In Topper Pro and Mastery Infinity, every live class features a face-to-face visual teacher. The teacher looks directly at your child, speaks with natural educator cadence, listens and responds in real time, and dynamically writes notes and step-by-step derivations on the chalkboard.',
    },
    {
      q: 'How does the Scholar plan guarantee school syllabus completion?',
      a: 'The Scholar plan provides 8 live Socratic classes every month (80 classes over the 10-month school academic term). This covers all 27–30 chapters in school Maths and Science with dedicated sessions for challenging concepts and textbook exercise problem solving.',
    },
    {
      q: 'Why is 1-on-1 Socratic tutoring better than PhysicsWallah or YouTube?',
      a: 'In YouTube or mass coaching streams (where 5,000 to 50,000 students watch one teacher), students easily get distracted, browse other tabs, and cannot ask questions. Anaxly is strictly 1-on-1: it addresses the student by name, stops every 2-3 sentences to ask check-for-understanding questions, and will not move forward until the student demonstrates comprehension on the chalkboard.',
    },
    {
      q: 'Which boards and classes are covered?',
      a: 'We exclusively serve school students in Classes 6 to 12 under CBSE (NCERT syllabus), ICSE (Selina Concise & Morning Star standards), and IB (MYP and DP criterion rubrics). We do not distract students with college entrance exams—every explanation matches your exact school board marking scheme.',
    },
    {
      q: 'Can I cancel or switch plans at any time?',
      a: 'Yes. You can upgrade, downgrade, or cancel your subscription at any time with a single click. When upgrading, your remaining days are automatically credited toward your new tier.',
    },
    {
      q: 'What payment methods do you accept?',
      a: 'We support all major Indian payment methods via 1-click UPI (Google Pay, PhonePe, Paytm, BHIM), Net Banking across 50+ banks, Credit/Debit Cards (Visa, MasterCard, RuPay), and international cards for IB students.',
    },
  ]

  // Clean, high-visibility cell content renderer: NO badges, NO useless icons
  const renderCellContent = (val: string | boolean) => {
    if (typeof val === 'boolean') {
      return val ? (
        <Check className="w-5 h-5 text-[var(--accent-warm)] stroke-[2.75] mx-auto" />
      ) : (
        <span className="text-[var(--border-strong)] font-bold text-lg select-none">—</span>
      )
    }
    if (val === '100% Free') {
      return (
        <span className="font-extrabold text-[var(--accent-warm)] text-sm sm:text-base">
          100% Free
        </span>
      )
    }
    if (val.includes('100% of All Classes')) {
      return (
        <span className="font-extrabold text-[var(--accent-warm-hover)] text-sm sm:text-base">
          100% of All Classes
        </span>
      )
    }
    return <span className="font-bold text-[var(--ink-primary)] text-sm sm:text-base">{val}</span>
  }

  const handleScrollToCompare = (e: React.MouseEvent) => {
    e.preventDefault()
    const el = document.getElementById('compare')
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' })
    }
  }

  const router = useRouter()
  const [processingPlanId, setProcessingPlanId] = useState<string | null>(null)
  const [testModalOrder, setTestModalOrder] = useState<{
    orderId: string
    amount: number
    currency: string
    planId: string
    billingCycle: string
    keyId: string
  } | null>(null)
  const [isVerifying, setIsVerifying] = useState(false)

  const handleVerifyPayment = async (
    orderId: string,
    paymentId: string,
    signature: string
  ) => {
    setIsVerifying(true)
    try {
      const verifyRes = await fetch('/api/payment/verify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          razorpay_order_id: orderId,
          razorpay_payment_id: paymentId,
          razorpay_signature: signature,
        }),
      })
      const verifyData = await verifyRes.json()
      if (verifyData.success) {
        setTestModalOrder(null)
        window.location.href = '/dashboard?payment_success=true'
      } else {
        alert(verifyData.error || 'Payment verification failed')
      }
    } catch (err: any) {
      alert('Network error verifying payment: ' + (err.message || 'Unknown error'))
    } finally {
      setIsVerifying(false)
      setProcessingPlanId(null)
    }
  }

  const handlePlanCheckout = async (e: React.MouseEvent, planId: string, defaultHref: string) => {
    e.preventDefault()

    if (planId === 'free') {
      try {
        const res = await fetch('/api/subscription', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ planTier: 'free' }),
        })
        if (res.ok) {
          window.location.href = '/dashboard'
          return
        }
      } catch {
        // Fallback
      }
      window.location.href = defaultHref
      return
    }

    setProcessingPlanId(planId)

    try {
      const res = await fetch('/api/payment/create-order', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ planTier: planId, billingCycle }),
      })

      if (res.status === 401) {
        window.location.href = `/login?next=${encodeURIComponent('/pricing')}`
        return
      }

      const order = await res.json()
      if (order.error) {
        alert(order.error)
        setProcessingPlanId(null)
        return
      }

      // 1. Attempt to load Razorpay checkout script
      const isLoaded = await loadRazorpaySdk()

      if (isLoaded && typeof window !== 'undefined' && (window as any).Razorpay) {
        const options = {
          key: order.keyId,
          amount: order.amount,
          currency: order.currency,
          name: 'Anaxly',
          description: `${planId.toUpperCase()} Subscription (${billingCycle})`,
          order_id: order.orderId,
          handler: async function (response: any) {
            await handleVerifyPayment(
              response.razorpay_order_id,
              response.razorpay_payment_id,
              response.razorpay_signature
            )
          },
          modal: {
            ondismiss: function () {
              setProcessingPlanId(null)
            },
          },
          theme: {
            color: '#1F3852',
          },
        }

        try {
          const rzp = new (window as any).Razorpay(options)
          rzp.on('payment.failed', function (resp: any) {
            console.warn('Payment failed:', resp.error)
            setProcessingPlanId(null)
            if (order.keyId.startsWith('rzp_test_')) {
              setTestModalOrder({
                orderId: order.orderId,
                amount: order.amount,
                currency: order.currency,
                planId,
                billingCycle,
                keyId: order.keyId,
              })
            } else {
              alert(resp.error?.description || 'Payment was unsuccessful')
            }
          })
          rzp.open()
          return
        } catch (openErr) {
          console.warn('Failed to open Razorpay modal:', openErr)
        }
      }

      // 2. Fallback to interactive Test Payment Simulator in test mode
      setTestModalOrder({
        orderId: order.orderId,
        amount: order.amount,
        currency: order.currency,
        planId,
        billingCycle,
        keyId: order.keyId,
      })
    } catch (err: any) {
      console.error('Checkout error:', err)
      alert('Unable to initialize payment: ' + (err.message || 'Network error'))
    } finally {
      setProcessingPlanId(null)
    }
  }

  return (
    <div className="min-h-screen bg-[var(--canvas-base)] text-[var(--ink-primary)] antialiased selection:bg-[var(--accent-warm-soft)] selection:text-[var(--ink-primary)] font-sans">
      <Script src="https://checkout.razorpay.com/v1/checkout.js" strategy="afterInteractive" />
      <LandingNav />

      {/* Main Page Content - Expanded Container for Wider Cards */}
      <main className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-10 pt-28 sm:pt-32 pb-24">
        
        {/* Header Hero Section */}
        <section className="text-center max-w-4xl mx-auto space-y-4">
          <h1 className="font-sans text-3xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight text-[var(--ink-primary)] leading-[1.14] sm:leading-[1.12] lg:leading-[1.1]">
            World-Class <span className="text-[var(--accent-warm)]">1-on-1 Socratic Tutoring</span>, starting at{' '}
            <span className="underline decoration-[var(--accent-warm-border)] decoration-4 underline-offset-8 text-[var(--ink-primary)] font-black">₹399/mo</span> — at{' '}
            <span className="text-[var(--accent-warm)] underline decoration-[var(--accent-warm-border)] decoration-4 underline-offset-6">1/4th the Cost</span> of Private Tuitions.
          </h1>

          <p className="text-base sm:text-lg font-medium text-[var(--ink-secondary)] leading-relaxed max-w-3xl mx-auto">
            Interactive digital chalkboard, science diagrams, and coordinate graphs are{' '}
            <span className="text-[var(--accent-warm-hover)] font-bold underline decoration-[var(--accent-warm-border)] decoration-2">
              100% Free Forever
            </span>
            . Unlock live Socratic classes starting at <span className="text-[var(--ink-primary)] font-bold underline decoration-[var(--border-strong)] decoration-2">₹399/mo</span> and face-to-face AI video teachers at <span className="text-[var(--ink-primary)] font-bold underline decoration-[var(--accent-warm-border)] decoration-2">₹899/mo</span>.
          </p>

          {/* Clean Hairline Scholastic Illustration (No text metadata) */}
          <HairlineHeroIllustration />

          {/* Billing Cycle Toggle */}
          <div className="pt-1 flex items-center justify-center gap-3">
            <div className="inline-flex items-center rounded-full border border-[var(--border-subtle)] bg-white p-1.5 shadow-xs">
              <button
                type="button"
                onClick={() => setBillingCycle('monthly')}
                className={`rounded-full px-5 py-2 text-xs sm:text-sm font-bold transition-all cursor-pointer ${
                  billingCycle === 'monthly'
                    ? 'bg-[var(--accent-primary)] text-white shadow-xs'
                    : 'text-[var(--ink-secondary)] hover:text-[var(--ink-primary)]'
                }`}
              >
                Monthly Billing
              </button>
              <button
                type="button"
                onClick={() => setBillingCycle('annual')}
                className={`rounded-full px-5 py-2 text-xs sm:text-sm font-bold transition-all flex items-center gap-2 cursor-pointer ${
                  billingCycle === 'annual'
                    ? 'bg-[var(--accent-primary)] text-white shadow-xs'
                    : 'text-[var(--ink-secondary)] hover:text-[var(--ink-primary)]'
                }`}
              >
                <span>Annual Billing</span>
                <span className="rounded-full bg-[var(--accent-warm-soft)] text-[var(--accent-warm-hover)] text-xs font-black px-2 py-0.5 uppercase tracking-wide">
                  Save 20-25%
                </span>
              </button>
            </div>
          </div>
        </section>

        {/* Pricing Cards Grid - Wider, Roomier Cards */}
        <section className="mt-12 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 sm:gap-7 items-stretch">
          {plans.map((plan) => {
            const price = billingCycle === 'annual' ? plan.annualPrice : plan.monthlyPrice
            return (
              <div
                key={plan.id}
                className={`relative flex flex-col rounded-3xl p-7 sm:p-8 transition-all duration-300 ${
                  plan.popular
                    ? 'border-2 border-[var(--accent-primary)] bg-white shadow-xl ring-4 ring-[var(--accent-primary-border)]'
                    : 'border border-[var(--border-subtle)] bg-white hover:border-[var(--border-strong)] shadow-xs hover:shadow-md'
                }`}
              >
                {/* Popular Badge */}
                {plan.badge && (
                  <div className="absolute -top-3.5 left-1/2 -translate-x-1/2 whitespace-nowrap">
                    <span
                      className={`inline-flex items-center gap-1 rounded-full px-3 py-0.5 text-xs font-black uppercase tracking-wider shadow-xs ${
                        plan.popular
                          ? 'bg-[var(--accent-primary)] text-white'
                          : 'bg-[var(--canvas-soft)] border border-[var(--border-subtle)] text-[var(--ink-secondary)]'
                      }`}
                    >
                      {plan.popular && <Star className="w-3 h-3 fill-current" />}
                      <span>{plan.badge}</span>
                    </span>
                  </div>
                )}

                {/* Card Crest & Header */}
                <div className="space-y-3 pt-1 pb-4 border-b border-[var(--border-subtle)]">
                  <div className="flex items-center justify-between">
                    <h3 className="font-sans text-2xl font-bold text-[var(--ink-primary)] tracking-tight">{plan.name}</h3>
                    <div className="p-2 rounded-2xl bg-[var(--canvas-soft)] border border-[var(--border-subtle)]">
                      {plan.crest}
                    </div>
                  </div>

                  <p className="text-xs sm:text-sm text-[var(--ink-secondary)] leading-relaxed min-h-[38px]">{plan.description}</p>

                  <div className="pt-2 flex items-baseline gap-1.5">
                    <span className="text-4xl sm:text-5xl font-black tracking-tight text-[var(--ink-primary)]">
                      {price === 0 ? '₹0' : `₹${price}`}
                    </span>
                    <span className="text-xs sm:text-sm text-[var(--ink-muted)] font-semibold">{plan.priceSuffix}</span>
                  </div>

                  {billingCycle === 'annual' && plan.annualSavings && (
                    <p className="text-xs font-bold text-[var(--accent-warm)]">{plan.annualSavings}</p>
                  )}
                </div>

                {/* 5 Highlights List */}
                <div className="flex-1 py-5 space-y-3">
                  <div className="text-xs font-black uppercase tracking-wider text-[var(--ink-muted)]">
                    {plan.featuresHeader}
                  </div>

                  <ul className="space-y-3">
                    {plan.features.map((feature, idx) => (
                      <li key={idx} className="flex items-start gap-2.5 text-xs sm:text-sm leading-snug text-[var(--ink-secondary)]">
                        <Check
                          className={`w-4 h-4 mt-0.5 shrink-0 ${
                            feature.freeHighlight
                              ? 'text-[var(--accent-warm)] stroke-[3]'
                              : feature.highlight
                              ? 'text-[var(--accent-primary)] stroke-[2.5]'
                              : 'text-[var(--ink-muted)] stroke-[2]'
                          }`}
                        />
                        <span
                          className={`${
                            feature.freeHighlight
                              ? 'font-bold text-[var(--accent-warm-hover)] bg-[var(--accent-warm-soft)] px-1 py-0.5 rounded'
                              : feature.highlight
                              ? 'font-bold text-[var(--ink-primary)]'
                              : 'font-medium'
                          }`}
                        >
                          {feature.text}
                        </span>
                      </li>
                    ))}
                  </ul>

                  {/* Underlined link to scroll to full comparison */}
                  <div className="pt-3">
                    <a
                      href="#compare"
                      onClick={handleScrollToCompare}
                      className="text-xs sm:text-sm font-bold text-[var(--ink-secondary)] hover:text-[var(--accent-warm)] underline underline-offset-4 decoration-[var(--border-subtle)] hover:decoration-[var(--accent-warm)] transition-colors inline-block"
                    >
                      See all features &amp; full comparison &rarr;
                    </a>
                  </div>
                </div>

                {/* Card CTA */}
                <div className="pt-4 border-t border-[var(--border-subtle)]">
                  <button
                    type="button"
                    disabled={processingPlanId === plan.id}
                    onClick={(e) => handlePlanCheckout(e, plan.id, plan.ctaHref)}
                    className={`w-full inline-flex items-center justify-center gap-2 rounded-full py-3.5 px-4 text-xs sm:text-sm font-semibold transition-all cursor-pointer ${
                      plan.ctaVariant === 'primary'
                        ? 'bg-[var(--accent-primary)] hover:bg-[var(--accent-primary-hover)] text-white shadow-xs'
                        : plan.ctaVariant === 'secondary'
                        ? 'border border-[var(--accent-primary)] bg-white text-[var(--accent-primary)] hover:bg-[var(--accent-primary-soft)]'
                        : 'border border-[var(--border-strong)] bg-white text-[var(--ink-primary)] hover:border-[var(--ink-primary)] hover:bg-[var(--canvas-soft)]'
                    }`}
                  >
                    <span>{processingPlanId === plan.id ? 'Connecting...' : plan.ctaText}</span>
                    <ArrowRight className="w-4 h-4" />
                  </button>
                </div>
              </div>
            )
          })}
        </section>

        {/* Granular Capability Breakdown Table - Clear Column Separation Lines, No Category Rows */}
        <section id="compare" className="mt-28 scroll-mt-24">
          <div className="text-center max-w-3xl mx-auto space-y-3 mb-10">
            <h2 className="font-sans text-3xl sm:text-5xl font-extrabold text-[var(--ink-primary)] tracking-tight">
              Granular Capability Breakdown
            </h2>
            <p className="text-sm sm:text-base font-medium text-[var(--ink-secondary)]">
              Clear, transparent feature comparison. Digital chalkboard derivations and dynamic coordinate graphs remain 100% free across every plan.
            </p>
          </div>

          <div className="overflow-x-auto rounded-3xl border border-[var(--border-subtle)] bg-white shadow-xs">
            <table className="w-full text-left border-collapse min-w-[760px]">
              <thead>
                <tr className="border-b-2 border-[var(--border-strong)] bg-[var(--canvas-soft)]/90 divide-x divide-[var(--border-subtle)]">
                  <th className="py-4 px-6 font-sans text-base sm:text-lg font-bold text-[var(--ink-primary)] w-2/5">
                    Capability
                  </th>
                  <th className="py-4 px-4 text-center font-sans text-base sm:text-lg font-bold text-[var(--ink-primary)] w-[15%]">
                    Free
                  </th>
                  <th className="py-4 px-4 text-center font-sans text-base sm:text-lg font-bold text-[var(--ink-primary)] w-[15%]">
                    Scholar
                  </th>
                  <th className="py-4 px-4 text-center font-sans text-base sm:text-lg font-extrabold text-[var(--accent-warm-hover)] bg-[var(--accent-warm-soft)] w-[15%]">
                    Topper Pro
                  </th>
                  <th className="py-4 px-4 text-center font-sans text-base sm:text-lg font-bold text-[var(--ink-primary)] w-[15%]">
                    Mastery
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[var(--border-subtle)] text-[var(--ink-primary)]">
                {allGranularFeatures.map((feat, fIdx) => (
                  <tr key={fIdx} className="hover:bg-[var(--canvas-soft)]/80 transition-colors divide-x divide-[var(--border-subtle)]">
                    <td className="py-4 px-6 text-sm sm:text-base text-[var(--ink-primary)] font-semibold">
                      {feat.title}
                    </td>
                    <td className="py-4 px-4 text-center">{renderCellContent(feat.free)}</td>
                    <td className="py-4 px-4 text-center">{renderCellContent(feat.scholar)}</td>
                    <td className="py-4 px-4 text-center bg-[var(--accent-warm-soft)]">
                      {renderCellContent(feat.topper)}
                    </td>
                    <td className="py-4 px-4 text-center">{renderCellContent(feat.mastery)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>

        {/* Anaxly vs. YouTube vs. Mass Coaching vs. Home Tutors (Badge Removed, Highlight Word, Vertical Lines) */}
        <section className="mt-28">
          <div className="text-center max-w-4xl mx-auto space-y-3 mb-10">
            <h2 className="font-sans text-3xl sm:text-5xl font-extrabold text-[var(--ink-primary)] tracking-tight">
              <span className="text-[var(--accent-warm)] underline decoration-[var(--accent-warm-border)] decoration-4 underline-offset-6">Anaxly 1-on-1</span> vs. YouTube vs. Mass Coaching vs. Home Tutors
            </h2>
            <p className="text-sm sm:text-base font-medium text-[var(--ink-secondary)]">
              Why passive 50,000-student chat streams fail school students, and how 1-on-1 Socratic chalkboard discipline delivers authentic 95%+ board scores.
            </p>
          </div>

          <div className="overflow-x-auto rounded-3xl border border-[var(--border-subtle)] bg-white shadow-xs">
            <table className="w-full text-left border-collapse min-w-[760px]">
              <thead>
                <tr className="border-b-2 border-[var(--border-strong)] bg-[var(--canvas-soft)]/90 divide-x divide-[var(--border-subtle)]">
                  <th className="py-4 px-6 font-sans text-sm sm:text-base font-bold text-[var(--ink-primary)] w-1/5">
                    Academic Dimension
                  </th>
                  <th className="py-4 px-4 text-center font-sans text-xs sm:text-sm font-bold text-[var(--ink-secondary)] w-1/5">
                    <div className="flex items-center justify-center gap-1.5">
                      <Tv className="w-4 h-4 text-[var(--ink-muted)]" />
                      <span>YouTube Videos</span>
                    </div>
                  </th>
                  <th className="py-4 px-4 text-center font-sans text-xs sm:text-sm font-bold text-[var(--ink-secondary)] w-1/5">
                    <div className="flex items-center justify-center gap-1.5">
                      <Users className="w-4 h-4 text-[var(--ink-muted)]" />
                      <span>Mass Coaching (PW)</span>
                    </div>
                  </th>
                  <th className="py-4 px-4 text-center font-sans text-xs sm:text-sm font-bold text-[var(--ink-secondary)] w-1/5">
                    <div className="flex items-center justify-center gap-1.5">
                      <Clock className="w-4 h-4 text-[var(--ink-muted)]" />
                      <span>Private Home Tutors</span>
                    </div>
                  </th>
                  <th className="py-4 px-4 text-center font-sans text-xs sm:text-sm font-extrabold text-[var(--accent-warm-hover)] bg-[var(--accent-warm-soft)] w-1/5">
                    <div className="flex items-center justify-center gap-1.5">
                      <Star className="w-4 h-4 text-[var(--accent-warm)] fill-current" />
                      <span>Anaxly 1-on-1</span>
                    </div>
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[var(--border-subtle)] text-xs sm:text-sm leading-relaxed text-[var(--ink-secondary)]">
                {alternativesComparison.map((row, idx) => (
                  <tr key={idx} className="hover:bg-[var(--canvas-soft)]/60 transition-colors divide-x divide-[var(--border-subtle)]">
                    <td className="py-4 px-6 font-bold text-[var(--ink-primary)]">{row.dimension}</td>
                    <td className="py-4 px-4 text-center text-[var(--ink-muted)] font-medium">{row.youtube}</td>
                    <td className="py-4 px-4 text-center text-[var(--ink-muted)] font-medium">{row.pw}</td>
                    <td className="py-4 px-4 text-center text-[var(--ink-secondary)] font-medium">{row.tutor}</td>
                    <td className="py-4 px-4 text-center font-bold text-[var(--accent-warm-hover)] bg-[var(--accent-warm-soft)]">
                      {row.anaxly}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>

        {/* Frequently Asked Questions */}
        <section className="mt-28 max-w-3xl mx-auto">
          <div className="text-center space-y-2 mb-10">
            <h2 className="font-sans text-3xl sm:text-4xl font-extrabold text-[var(--ink-primary)] tracking-tight">
              Frequently Asked Questions
            </h2>
            <p className="text-sm font-medium text-[var(--ink-secondary)]">
              Everything you need to know about our visual pedagogy, avatar technology, and pricing plans.
            </p>
          </div>

          <div className="space-y-3">
            {faqs.map((faq, idx) => {
              const isOpen = openFaqIndex === idx
              return (
                <div
                  key={idx}
                  className="rounded-2xl border border-[var(--border-subtle)] bg-white transition-all overflow-hidden shadow-2xs"
                >
                  <button
                    type="button"
                    onClick={() => setOpenFaqIndex(isOpen ? null : idx)}
                    className="w-full text-left px-5 py-4 flex items-center justify-between gap-4 cursor-pointer hover:bg-[var(--canvas-soft)]/60 transition-colors"
                  >
                    <span className="font-bold text-sm sm:text-base text-[var(--ink-primary)]">{faq.q}</span>
                    <HelpCircle
                      className={`w-4 h-4 text-[var(--ink-muted)] transition-transform duration-200 ${
                        isOpen ? 'rotate-180 text-[var(--accent-warm)]' : ''
                      }`}
                    />
                  </button>

                  {isOpen && (
                    <div className="px-5 pb-5 pt-1 border-t border-[var(--border-subtle)] text-xs sm:text-sm text-[var(--ink-secondary)] leading-relaxed">
                      {faq.a}
                    </div>
                  )}
                </div>
              )
            })}
          </div>
        </section>
      
      {/* Test Mode Payment Simulator Modal */}
      {testModalOrder && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-xs p-4 animate-in fade-in duration-200">
          <div className="bg-white rounded-3xl p-6 sm:p-8 max-w-md w-full shadow-2xl border border-[var(--border-subtle)] space-y-6">
            <div className="flex items-center justify-between border-b border-[var(--border-subtle)] pb-4">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-2xl bg-[var(--accent-warm-soft)] border border-[var(--accent-warm-border)] flex items-center justify-center text-[var(--accent-warm)]">
                  <CreditCard className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-lg font-bold text-[var(--ink-primary)]">Razorpay Test Simulator</h3>
                  <p className="text-xs text-[var(--ink-muted)] font-medium">Sandbox Payment Verification</p>
                </div>
              </div>
              <button
                type="button"
                onClick={() => setTestModalOrder(null)}
                className="p-1.5 rounded-xl hover:bg-[var(--canvas-soft)] text-[var(--ink-muted)] hover:text-[var(--ink-primary)] transition-colors cursor-pointer"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="bg-[var(--canvas-soft)] rounded-2xl p-4 border border-[var(--border-subtle)] space-y-2.5 text-xs sm:text-sm">
              <div className="flex justify-between items-center">
                <span className="text-[var(--ink-muted)]">Plan:</span>
                <span className="font-bold text-[var(--ink-primary)] uppercase">{testModalOrder.planId} Pro</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-[var(--ink-muted)]">Billing Cadence:</span>
                <span className="font-semibold text-[var(--ink-secondary)] capitalize">{testModalOrder.billingCycle}</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-[var(--ink-muted)]">Amount Due:</span>
                <span className="font-black text-[var(--ink-primary)] text-base">₹{(testModalOrder.amount / 100).toLocaleString('en-IN')}</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-[var(--ink-muted)]">Razorpay Order ID:</span>
                <span className="font-mono text-xs text-[var(--ink-secondary)] bg-white px-2 py-0.5 rounded border border-[var(--border-subtle)]">
                  {testModalOrder.orderId}
                </span>
              </div>
            </div>

            <div className="space-y-3">
              <button
                type="button"
                disabled={isVerifying}
                onClick={() =>
                  handleVerifyPayment(
                    testModalOrder.orderId,
                    `pay_test_${Date.now()}`,
                    `test_simulated_sig_${testModalOrder.orderId}_${Date.now()}`
                  )
                }
                className="w-full inline-flex items-center justify-center gap-2 rounded-full py-3.5 px-4 text-sm font-semibold text-white bg-[var(--accent-primary)] hover:bg-[var(--accent-primary-hover)] cursor-pointer disabled:opacity-60 shadow-xs"
              >
                <span>{isVerifying ? 'Activating Plan in Database...' : 'Simulate Successful Payment'}</span>
                <ArrowRight className="w-4 h-4" />
              </button>

              <button
                type="button"
                disabled={isVerifying}
                onClick={() => {
                  if (typeof window !== 'undefined' && (window as any).Razorpay) {
                    const options = {
                      key: testModalOrder.keyId,
                      amount: testModalOrder.amount,
                      currency: testModalOrder.currency,
                      name: 'Anaxly',
                      description: `${testModalOrder.planId.toUpperCase()} Subscription`,
                      order_id: testModalOrder.orderId,
                      handler: async function (response: any) {
                        await handleVerifyPayment(
                          response.razorpay_order_id,
                          response.razorpay_payment_id,
                          response.razorpay_signature
                        )
                      },
                      theme: { color: '#1F3852' },
                    }
                    const rzp = new (window as any).Razorpay(options)
                    rzp.open()
                  } else {
                    alert('Razorpay checkout script not available in browser. Use Simulate button above.')
                  }
                }}
                className="w-full inline-flex items-center justify-center gap-2 rounded-2xl py-2.5 px-4 text-xs font-semibold border border-[var(--border-subtle)] hover:bg-[var(--canvas-soft)] text-[var(--ink-secondary)] transition-colors cursor-pointer"
              >
                Retry Launching Official Razorpay Modal
              </button>
            </div>
          </div>
        </div>
      )}
      </main>

      {/* Unified Mainline-Style Anaxly Footer */}
      <LandingFooter />
    </div>
  )
}
