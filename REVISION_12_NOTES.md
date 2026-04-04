# Project Zero Roulette - Revision 12 Summary

**Date:** April 4, 2026

## Changes Implemented

### 1. Lockout Duration Reduced (30 days to 7 days)
The lockout period triggered when a player pushes past thresholds and ends a session at a loss has been reduced from 30 days to 7 days. The lockout warning modal text has been updated accordingly.

### 2. SIM Mode: No Lockout
When playing in SIM mode, threshold overrides now display an informational warning ("If this had been LIVE or TABLE mode, you would have been locked out for 7 days") instead of triggering the actual lockout flow. Players can continue playing in SIM mode without any lockout consequences. The Leave Casino handler also skips lockout logic in SIM mode.

### 3. Developer Unlock Relocated
The developer unlock trigger on the lockout screen has been moved from 5 taps anywhere on the lockout box to 15 rapid taps specifically in the top-right quadrant of the screen. The tap timeout window is 2 seconds. This makes accidental discovery by end users extremely unlikely.

### 4. Strategy Switch Buttons
A new section has been added below the "Clear Saved App State" button containing five strategy switch buttons (Steady Eddie, Delayed Surge, Slow Grind, Streak Reset, and Switch to Legacy Mode). Each button is color-coded to match its strategy card color from the selection screen.

Behavior includes the following features. Tapping the currently active strategy shows an explanation modal with the strategy description and a note that it is the active strategy. Tapping a different strategy shows the strategy description and asks if the user wants to switch, followed by a second confirmation. Switching to Legacy Mode requires a double confirmation with warning text about removing all strategy protections. The active strategy button shows "(Active)" in its label and appears at reduced opacity.

### 5. Steady Eddie Description Updated
The Steady Eddie description on the strategy selection screen has been changed from "Flat $2/$2/$2 every spin. No escalation. Sit out 17 after a zero hit. Lowest volatility." to "Proven performer but payouts are minimal. Best for keeping bankroll intact."

### 6. LIVE/TABLE Bet Placement Prompt (Foundation)
A `showBetsPlacedPrompt()` function has been added that displays a modal telling the player exactly what bets to place at the table, then waits for confirmation before proceeding. This function is available for integration into the LIVE and TABLE mode spin workflows.

## Technical Details

| Item | Detail |
|------|--------|
| Revision | 12 |
| File modified | index.html |
| Commit hash | d172354 |
| Repository | github.com/djredpill/project-zero-roulette |
| Branch | main |
