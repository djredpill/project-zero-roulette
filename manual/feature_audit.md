# Project Zero Roulette — Complete Feature Audit

## 1. SPLASH SCREEN
- Full-screen splash with app logo/image
- "Tap anywhere to enter" hint with pulsing animation
- Roulette ball sound effect on tap
- Fades out to reveal main app

## 2. STICKY HEADER
- Always visible at top when scrolling
- Shows: Balance, Mode Badge (SIM/LIVE/TABLE), Session Spins, Spin Counter (X/12)
- Zero bet amounts (0: $5, Spl: $5, 00: $5) — tappable to edit
- Last 36 numbers strip (color-coded)
- Sit-out bar (when active): shows count, ghost hits, Edit/Cancel buttons

## 3. SETUP / CONFIGURATION
- Starting Bankroll input (default $1,500)
- Unit per zero input (default $5)
- Table Type dropdown: American (0 & 00) or European (single 0)
- Background/Theme selector: White, Dark, Blue, Green, Turquoise, Gold, Pink, Grey
- Mode toggle: SIM / LIVE / TABLE (locked once session starts)
- Start Session button
- Session Balance display

## 4. SPIN INPUT
- Text input field (readonly, uses numpad)
- Place Spin button
- Random button (generates random valid number)
- Number Pad: 1-36 color-coded (red/black), 0/00 (green), Undo, Sit Out, Random, SPIN
- Auto-submit: tapping a number on numpad immediately submits the spin

## 5. SESSION CONTROLS
- Reset Session: resets balance, returns to setup screen to change mode/settings
- Export CSV: downloads session report as CSV file
- Reset Historical P/L: resets historical P/L (double confirm for LIVE/TABLE modes)
- Sit Out Spins: manual sit-out with suggested number based on historical avg
- Place Side Bet: opens manual side bet modal
- Undo Last Spin: rolls back the most recent spin
- Edit Bankroll/Unit: change bankroll and unit mid-session
- Leave The Casino: end session with full report
- Clear Saved App State: wipes all localStorage, reloads fresh

## 6. ZERO BETS DISPLAY (Trio Strip)
- Bet on 0: shows amount and payout
- Bet on 0/00 split: shows amount and payout (American only)
- Bet on 00: shows amount and payout (American only)
- Click any box to open Zero Edit Modal
- "Click any Zero box to change individual bets" hint

## 7. ZERO EDIT MODAL
- Individual inputs for Bet on 0, Bet on 00, Bet on Split
- Uniform bet input with Apply button
- Save / Cancel buttons

## 8. LAST 36 NUMBERS
- Color-coded number badges (red/black/green)
- Shows most recent numbers first
- Max 36 numbers displayed

## 9. ACTIVE STAKE BAR
- Appears when side bet(s) are active
- Shows stacked lines for multiple bets: e.g., "R/$71" and "E/$50"
- Each on its own line

## 10. SIT-OUT SYSTEM
- Auto sit-out suggestion after zero/00 hits (uses historical avg gap)
- Dialog: accept suggested, enter custom number, or cancel
- Manual sit-out via Sit Out Spins button (also suggests based on avg)
- Sit-out badge shows remaining spins
- Ghost hit tracking: counts zeros that hit while sitting out
- Edit/Cancel sit-out at any time
- Sticky sit-out bar in header

## 11. SESSION HISTORY TABLE
- Columns: Time, Mode, 0's Stake, Side, Net, Bal.
- Mode shown as colored badge (SIM blue, LIVE amber, TABLE purple)
- Side bets color-coded: green for wins, red for losses
- Compact labels: R/$71, E/$50, D1/$30, C2/$40
- Net colored green (win) or red (loss)
- Scrollable, max 300px height

## 12. SESSION SUMMARY (Right Sidebar)
- Starting Bankroll
- Session P/L (colored)
- Historical P/L (colored)

## 13. LOSS / WIN ALERTS
- 6 threshold badges: L:1/5, L:1/3, L:2/5, W:1/5, W:1/3, W:2/5
- Light up when threshold reached
- Win alerts: green flash border + win chime sound
- Loss alerts: red flash border + loss alert sound
- 40% loss (L:2/5): urgent flash + crisis modal

## 14. CRISIS MODAL (40% Loss)
- Shows loss percentage and current balance
- Options: Continue Playing, Reset Session, Quit (Leave Casino)

## 15. SETTINGS (Right Sidebar)
- Auto increment every N spins checkbox
- N spins input (default 12)
- Increment $ input (default $5)
- Spin counter display with manual edit (X / 12) + Reset button
- Show 0/00 split bet checkbox (American only)
- Auto-place split bet when shown checkbox

## 16. RAISE / HOLD MODAL
- Triggers after N spins completed
- Shows current unit and proposed raise amount
- Raise or Hold buttons

## 17. STREAK DETECTION & SIDE BET ALERTS
- Detects 6+ streaks in: Color, Parity, Dozen, Column
- Multiple simultaneous streaks: sequential alerts for each
- Pattern dialog shows:
  - Streak type and description
  - Suggestion (opposite color/parity, or coldest dozen/column)
  - Suggested side bet percentage buttons: 5%, 10%, 15%, custom %
  - Side bet stake amount
  - Outcome breakdown table (with/without zeros)
- Actions: Bet + Keep Zeros, Bet + Remove Zeros, Ignore

## 18. MANUAL SIDE BET MODAL
- Bet type selection: Color, Parity, Dozen, Column
- Value selection (dynamic based on type)
- Auto-suggests coldest dozen/column
- Percentage buttons: 5%, 10%, 15%, custom %
- Outcome breakdown table
- Bet + Keep Zeros, Bet + Remove Zeros, Cancel

## 19. SIDE BET SETTLEMENT
- All active side bets evaluated on next spin
- Each bet independently checked for win/loss
- Color/Parity: 2x payout; Dozen/Column: 3x payout
- Remove zeros option: zero bets set to $0 for that spin
- History shows color-coded results per bet

## 20. LEAVE THE CASINO / SESSION REPORT
- Confirmation dialog
- Full session report modal:
  - Mode, Starting Bankroll, Ending Balance
  - Session P/L, Historical P/L
  - Total Spins, Est. Duration
  - Session & Historical Avg Spins Between Zeros
  - Sit-Out Statistics (times used, total spins, avg length, ghost hits)
  - Win/loss congratulations message
- Email option: enter email to send report via mailto
- Export CSV option
- Resets session after confirming

## 21. CSV EXPORT
- Full session report header
- Spin-by-spin history with all columns
- Auto-downloads as .csv file

## 22. GLOBAL STATS (Cross-Session)
- allZeroGaps: tracks gaps between zeros across all sessions/modes
- totalSpinsAllTime, totalZerosAllTime
- Used for historical average gap calculation
- Persists in separate localStorage key

## 23. MODE SYSTEM (SIM / LIVE / TABLE)
- SIM: Simulation mode (default) — blue badge
- LIVE: Automated table — amber badge
- TABLE: Dealer table — purple badge
- Each mode has independent Historical P/L
- Mode locked once session starts (unlocks on reset)
- LIVE/TABLE modes require double confirmation for destructive actions

## 24. THEMES (8 options)
- White, Dark, Blue, Green, Turquoise, Gold, Pink, Grey
- Full color scheme changes: background, text, cards, modals, inputs

## 25. PWA SUPPORT
- Installable as home screen app (iOS/Android)
- Service worker for offline capability
- Apple touch icon, manifest.json

## 26. AUDIO
- Splash screen: roulette ball sound (embedded WAV)
- Win chime: synthesized ascending tones
- Loss alert: synthesized descending tones (urgent version for 40% loss)

## 27. STATE PERSISTENCE
- Auto-saves to localStorage after every action
- Separate storage keys per mode (SIM/LIVE/TABLE)
- Global stats stored separately
- Survives app close/reopen
- Clear Saved App State to wipe everything

## 28. UNDO / ROLLBACK
- Undo Last Spin: reverses the most recent spin
- Restores balance, removes from history
- Reverses zero gap tracking
- Reverses global stats
