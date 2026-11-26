// Material Symbols icon font is only used inside the dashboard/classroom,
// so it's loaded here instead of the root layout (keeps it off the landing page's
// critical path). React 19 hoists this stylesheet into <head>.
export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="" />
      <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0..1,0&icon_names=add,arrow_forward,arrow_right,auto_stories,biotech,calendar_today,check,check_circle,chevron_right,close,eco,edit_document,edit_note,event,functions,history,history_edu,home,insights,menu,menu_book,mic,notifications,play_arrow,play_circle,playlist_add_check,psychology_alt,replay,schedule,school,science,settings,timer,tune,verified&display=block"
        precedence="default"
      />
      {children}
    </>
  )
}
