import * as React from 'react'
import { cn } from '@/lib/utils'

type DashCardTone = 'surface' | 'soft' | 'primary'
type DashCardSize = 'sm' | 'md' | 'lg'

const toneClasses: Record<DashCardTone, string> = {
  surface: 'bg-surface border-border-subtle text-ink-primary shadow-soft',
  soft: 'bg-canvas-soft border-border-subtle text-ink-primary',
  primary: 'bg-accent-primary border-accent-primary text-on-primary shadow-card',
}

const sizeClasses: Record<DashCardSize, string> = {
  sm: 'rounded-lg p-4',
  md: 'rounded-xl p-6',
  lg: 'rounded-3xl p-8',
}

interface DashCardProps extends React.HTMLAttributes<HTMLDivElement> {
  tone?: DashCardTone
  size?: DashCardSize
}

/** Dashboard container. `size` sets radius and padding together so nested cards can step down a level. */
export const DashCard = React.forwardRef<HTMLDivElement, DashCardProps>(
  ({ tone = 'surface', size = 'md', className, ...props }, ref) => (
    <div
      ref={ref}
      className={cn('border', toneClasses[tone], sizeClasses[size], className)}
      {...props}
    />
  )
)
DashCard.displayName = 'DashCard'

interface StatTileProps extends React.HTMLAttributes<HTMLDivElement> {
  label: string
  value: React.ReactNode
  unit?: string
  hint?: React.ReactNode
  icon?: React.ReactNode
}

/** Single metric: label, value with optional unit, and a one-line hint. */
export function StatTile({ label, value, unit, hint, icon, className, ...props }: StatTileProps) {
  return (
    <DashCard tone="soft" size="sm" className={cn('flex flex-col gap-2', className)} {...props}>
      <div className="flex items-center justify-between gap-2 text-sm text-ink-muted">
        <span>{label}</span>
        {icon}
      </div>
      <div className="flex items-baseline gap-1.5">
        <span className="text-3xl font-semibold tabular-nums leading-none text-ink-primary">{value}</span>
        {unit && <span className="text-sm text-ink-muted">{unit}</span>}
      </div>
      {hint && <p className="text-xs text-ink-secondary">{hint}</p>}
    </DashCard>
  )
}

interface SectionHeaderProps extends Omit<React.HTMLAttributes<HTMLDivElement>, 'title'> {
  title: React.ReactNode
  description?: React.ReactNode
  /** Right-aligned slot for a button or link. */
  action?: React.ReactNode
  as?: 'h1' | 'h2' | 'h3'
}

/** Title, optional description, and an optional action aligned to the end. */
export function SectionHeader({
  title,
  description,
  action,
  as: Heading = 'h2',
  className,
  ...props
}: SectionHeaderProps) {
  return (
    <div className={cn('flex flex-wrap items-start justify-between gap-3', className)} {...props}>
      <div className="min-w-0 space-y-1">
        <Heading className="font-editorial text-2xl leading-tight text-ink-primary">{title}</Heading>
        {description && <p className="max-w-prose text-sm text-ink-secondary">{description}</p>}
      </div>
      {action && <div className="shrink-0">{action}</div>}
    </div>
  )
}
