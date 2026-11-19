'use client'

import React, { useTransition } from 'react'
import Link from 'next/link'
import * as Menu from '@radix-ui/react-dropdown-menu'
import {
  ChevronDown,
  User,
  Settings,
  Sparkles,
  Volume2,
  GraduationCap,
  Target,
  Bell,
  CreditCard,
  LifeBuoy,
  Keyboard,
  Users,
  LogOut,
  SlidersHorizontal,
  NotebookPen,
  ArrowUpRight,
} from 'lucide-react'
import { signOutAction, switchAccountAction } from '@/app/dashboard/actions'
import { cn } from '@/lib/utils'

interface UserMenuProps {
  userId: string
  name: string
  email?: string
  avatarUrl?: string | null
  track?: string
  planName: string
  planTier: string
  classesRemaining: number
  classesLimit: number
  onOpenQuickPreferences?: () => void
}

const itemClass =
  'group flex w-full cursor-pointer select-none items-center gap-3 rounded-lg px-2.5 py-2 text-sm text-ink-secondary outline-none transition-colors data-[highlighted]:bg-canvas-soft data-[highlighted]:text-ink-primary'

function Item({
  href,
  icon: Icon,
  label,
  hint,
  onSelect,
  external,
}: {
  href?: string
  icon: React.ElementType
  label: string
  hint?: string
  onSelect?: () => void
  external?: boolean
}) {
  const inner = (
    <>
      <Icon className="h-4 w-4 shrink-0 text-ink-muted transition-colors group-data-[highlighted]:text-accent-warm" />
      <span className="flex-1">{label}</span>
      {hint && (
        <kbd className="rounded border border-border-subtle bg-surface px-1.5 font-mono text-xs text-ink-muted">
          {hint}
        </kbd>
      )}
      {external && <ArrowUpRight className="h-3.5 w-3.5 text-ink-muted" />}
    </>
  )
  if (href) {
    return (
      <Menu.Item asChild className={itemClass}>
        <Link href={href} target={external ? '_blank' : undefined}>
          {inner}
        </Link>
      </Menu.Item>
    )
  }
  return (
    <Menu.Item className={itemClass} onSelect={onSelect}>
      {inner}
    </Menu.Item>
  )
}

function Initial({ name, avatarUrl, size }: { name: string; avatarUrl?: string | null; size: string }) {
  return (
    <div
      className={cn(
        'flex shrink-0 items-center justify-center overflow-hidden rounded-full border border-border-subtle bg-gradient-to-br from-accent-warm-soft to-surface',
        size
      )}
    >
      {avatarUrl ? (
        <img className="h-full w-full object-cover" alt="" src={avatarUrl} />
      ) : (
        <span className="font-semibold text-accent-warm">{name.charAt(0).toUpperCase()}</span>
      )}
    </div>
  )
}

/** Account dropdown opened from the dashboard header avatar. */
export function UserMenu({
  userId,
  name,
  email,
  avatarUrl,
  track,
  planName,
  planTier,
  classesRemaining,
  classesLimit,
  onOpenQuickPreferences,
}: UserMenuProps) {
  const [pending, startTransition] = useTransition()
  const settings = (tab: string) => `/dashboard/${userId}/settings?tab=${tab}`
  const usedPct = classesLimit > 0 ? Math.min(100, Math.round(((classesLimit - classesRemaining) / classesLimit) * 100)) : 0

  return (
    <Menu.Root modal={false}>
      <Menu.Trigger asChild>
        <button
          type="button"
          className="group flex cursor-pointer items-center gap-2.5 rounded-full border border-transparent p-1 pr-2 text-left transition-all hover:border-border-subtle hover:bg-surface hover:shadow-xs focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-warm data-[state=open]:border-border-subtle data-[state=open]:bg-surface data-[state=open]:shadow-sm"
          aria-label={`Account menu for ${name}`}
        >
          <div className="relative">
            <Initial name={name} avatarUrl={avatarUrl} size="h-9 w-9 text-sm" />
          </div>
          <span className="hidden max-w-[10rem] truncate text-sm font-medium text-ink-primary xl:inline-block">{name}</span>
          <ChevronDown className="hidden h-4 w-4 text-ink-muted transition-transform duration-200 group-data-[state=open]:rotate-180 sm:block" />
        </button>
      </Menu.Trigger>

      <Menu.Portal>
        <Menu.Content
          align="end"
          sideOffset={10}
          collisionPadding={12}
          className="z-50 w-[19rem] origin-[var(--radix-dropdown-menu-content-transform-origin)] rounded-2xl border border-border-subtle bg-surface p-1.5 shadow-xl shadow-black/5 backdrop-blur-xl data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2"
        >
          {/* Identity card */}
          <div className="rounded-xl bg-gradient-to-br from-accent-warm-soft via-surface to-canvas-soft p-3">
            <div className="flex items-center gap-3">
              <Initial name={name} avatarUrl={avatarUrl} size="h-11 w-11 text-base" />
              <div className="min-w-0 flex-1">
                <p className="truncate text-sm font-semibold text-ink-primary">{name}</p>
                {email && <p className="truncate text-xs text-ink-muted">{email}</p>}
                {track && <p className="truncate text-xs text-ink-muted">{track}</p>}
              </div>
            </div>
            <div className="mt-3 space-y-1.5">
              <p className="text-xs text-ink-muted">
                {classesRemaining} of {classesLimit} classes left this month
              </p>
              <div className="h-1.5 overflow-hidden rounded-full bg-border-subtle">
                <div className="h-full rounded-full bg-accent-warm transition-all duration-500" style={{ width: `${usedPct}%` }} />
              </div>
            </div>
            {planTier === 'free' && (
              <Menu.Item asChild>
                <Link
                  href="/pricing"
                  className="mt-3 flex items-center justify-center gap-1.5 rounded-lg bg-accent-warm px-3 py-1.5 text-xs font-semibold text-white outline-none transition-colors hover:bg-accent-warm-hover data-[highlighted]:bg-accent-warm-hover"
                >
                  <Sparkles className="h-3.5 w-3.5" /> Upgrade plan
                </Link>
              </Menu.Item>
            )}
          </div>

          <Menu.Group className="mt-1.5">
            <Item href={`/dashboard/${userId}/profile`} icon={NotebookPen} label="Profile & notes" />
            <Item href={settings('account')} icon={User} label="Account" />
            {onOpenQuickPreferences && (
              <Item icon={SlidersHorizontal} label="Quick preferences" onSelect={onOpenQuickPreferences} />
            )}
          </Menu.Group>

          <Menu.Separator className="my-1.5 h-px bg-border-subtle" />

          <Menu.Sub>
            <Menu.SubTrigger className={cn(itemClass, 'data-[state=open]:bg-canvas-soft')}>
              <Settings className="h-4 w-4 text-ink-muted" />
              <span className="flex-1">Settings</span>
              <ChevronDown className="h-4 w-4 -rotate-90 text-ink-muted" />
            </Menu.SubTrigger>
            <Menu.Portal>
              <Menu.SubContent
                sideOffset={8}
                collisionPadding={12}
                className="z-50 w-56 rounded-2xl border border-border-subtle bg-surface p-1.5 shadow-xl shadow-black/5 backdrop-blur-xl data-[state=open]:animate-in data-[state=open]:fade-in-0 data-[state=open]:zoom-in-95"
              >
                <Item href={settings('account')} icon={User} label="Account" />
                <Item href={settings('avatars')} icon={Sparkles} label="Tutor avatar" />
                <Item href={settings('audio')} icon={Volume2} label="Voice & audio" />
                <Item href={settings('teaching')} icon={GraduationCap} label="Teaching style" />
                <Item href={settings('goals')} icon={Target} label="Study goals" />
                <Item href={settings('notifications')} icon={Bell} label="Notifications" />
                <Item href={settings('appearance')} icon={SlidersHorizontal} label="Appearance" />
              </Menu.SubContent>
            </Menu.Portal>
          </Menu.Sub>
          <Item href={settings('billing')} icon={CreditCard} label="Billing & plan" />
          <Item href={settings('shortcuts')} icon={Keyboard} label="Keyboard shortcuts" />
          <Item href="mailto:shauryaprabhakar097@gmail.com?subject=Anaxly%20support" icon={LifeBuoy} label="Help & feedback" external />

          <Menu.Separator className="my-1.5 h-px bg-border-subtle" />

          <Item
            icon={Users}
            label="Switch account"
            onSelect={() => startTransition(() => switchAccountAction())}
          />
          <Menu.Item
            disabled={pending}
            onSelect={() => startTransition(() => signOutAction())}
            className={cn(itemClass, 'text-red-700 data-[highlighted]:bg-red-50 data-[highlighted]:text-red-800')}
          >
            <LogOut className="h-4 w-4" />
            <span className="flex-1">{pending ? 'Signing out…' : 'Sign out'}</span>
          </Menu.Item>
        </Menu.Content>
      </Menu.Portal>
    </Menu.Root>
  )
}
