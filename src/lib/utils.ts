import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function isSchemaError(error: any): boolean {
  if (!error || typeof error !== 'object') return false
  
  // Check for Postgres column does not exist (42703)
  // Check for PostgREST schema cache errors (common when migrations run but API cache is stale)
  const errorMessage = (error.message || '').toString().toLowerCase();
  
  return (
    error.code === '42703' || 
    errorMessage.includes('could not find') ||
    errorMessage.includes('schema cache') ||
    (errorMessage.includes('column') && errorMessage.includes('does not exist'))
  )
}

