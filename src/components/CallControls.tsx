"use client";

import React, { useRef, useEffect } from "react";
import { Mic, MicOff, PhoneOff, Pause, Play } from "lucide-react";
import { Button } from "@/components/ui/button";

interface CallControlsProps {
  isMuted: boolean;
  userVolume?: number;
  userVolumeRef?: React.RefObject<number>;
  onToggleMute: () => void;
  onEndCall: () => void;
  onPause?: () => void;
  isPaused?: boolean;
}

export const CallControls: React.FC<CallControlsProps> = ({
  isMuted,
  userVolume = 0,
  userVolumeRef,
  onToggleMute,
  onEndCall,
  onPause,
  isPaused = false,
}) => {
  const rippleRef = useRef<HTMLSpanElement | null>(null);

  useEffect(() => {
    let animId: number;
    const animate = () => {
      const vol = userVolumeRef?.current ?? userVolume ?? 0;
      if (rippleRef.current) {
        if (!isMuted && vol > 0.04) {
          rippleRef.current.style.display = "block";
          rippleRef.current.style.transform = `scale(${1 + Math.min(vol, 1) * 0.45})`;
          rippleRef.current.style.opacity = `${Math.min(1, vol * 2.5)}`;
        } else {
          rippleRef.current.style.display = "none";
        }
      }
      animId = requestAnimationFrame(animate);
    };
    animId = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(animId);
  }, [isMuted, userVolume, userVolumeRef]);

  return (
    <div className="flex items-center gap-2 sm:gap-3 p-1.5 rounded-full bg-white border border-border">
      {/* Microphone Toggle Button */}
      <button
        onClick={onToggleMute}
        title={isMuted ? "Unmute microphone" : "Mute microphone"}
        className={`relative group flex items-center justify-center w-11 h-11 rounded-full transition-all duration-200 active:scale-95 ${
          isMuted
            ? "bg-destructive/10 text-destructive border border-destructive/20 hover:bg-destructive/20"
            : "bg-canvas text-ink-primary border border-border hover:bg-canvas/80"
        }`}
      >
        {/* Subtle Mic Volume Ripple Ring */}
        <span
          ref={rippleRef}
          className="absolute inset-0 rounded-full border border-botanical pointer-events-none transition-transform duration-75"
          style={{ display: "none" }}
        />

        {isMuted ? <MicOff className="w-5 h-5" strokeWidth={1.5} /> : <Mic className="w-5 h-5" strokeWidth={1.5} />}

        {/* Tooltip */}
        <span className="absolute -top-10 px-2.5 py-1 text-xs text-ink-secondary bg-white border border-border rounded-md opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none whitespace-nowrap shadow-sm">
          {isMuted ? "Unmute" : "Mute"}
        </span>
      </button>

      {/* Pause / Resume Button */}
      {onPause && (
        <button
          onClick={onPause}
          title={isPaused ? "Resume Lesson" : "Pause Lesson"}
          className={`relative group flex items-center justify-center w-11 h-11 rounded-full transition-all duration-200 active:scale-95 ${
            isPaused
              ? "bg-[var(--accent-primary)] text-white hover:bg-[var(--accent-primary-hover)]"
              : "bg-canvas text-ink-primary border border-border hover:bg-canvas/80"
          }`}
        >
          {isPaused ? <Play className="w-5 h-5 fill-current" strokeWidth={1.5} /> : <Pause className="w-5 h-5" strokeWidth={1.5} />}
          <span className="absolute -top-10 px-2.5 py-1 text-xs text-ink-secondary bg-white border border-border rounded-md opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none whitespace-nowrap shadow-sm">
            {isPaused ? "Resume Capsule" : "Pause Capsule"}
          </span>
        </button>
      )}

      {/* Divider */}
      <div className="w-px h-6 bg-border" />

      {/* End Call Button */}
      <Button
        onClick={onEndCall}
        title="End Live Class"
        className="group flex items-center gap-2 px-4 sm:px-5 h-11 rounded-full bg-ink-primary hover:bg-ink-secondary text-white font-medium text-sm transition-all duration-200 active:scale-[0.98] shadow-md"
      >
        <PhoneOff className="w-4 h-4" strokeWidth={1.5} />
        <span>End</span>
      </Button>
    </div>
  );
};
