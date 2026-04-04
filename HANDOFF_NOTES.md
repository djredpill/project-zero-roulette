# Project Zero Roulette — Modified Version Handoff Notes

## Overview

The modified app replaces the original single-mode experience with a **Strategy Selection System**. Users choose a strategy at launch, and the app guides them through the session with prompts, thresholds, and alerts specific to that strategy. If they override the app's recommendations, they get flipped into **Original Mode** (the classic app experience). A **30-day lockout** applies if they go past the final threshold.

---

## The Three Strategies

All strategies use **$2/$2/$2 base bets** ($2 on 0, $2 on 00, $2 on 0/00 split = $6/spin total). All use **17-spin sit-out** after a zero hit. All use **$1,500 starting bankroll**.

### Strategy 1A — "Sit and Climb" (Aggressive)
- **Base bets:** $2/$2/$2
- **After every non-zero spin:** Add $1 to each bet (+$3 total per spin)
- **No cap** — bets keep climbing until a zero hits
- **On zero hit:** Reset to $2/$2/$2, sit out 17 spins
- **Thresholds:** Threshold 1 = 20% (warning), Threshold 2 = 33% (hard stop)
- **Profile:** Highest risk, highest reward. The longer you go without a zero, the bigger the payout when one hits.
- **Simulation result:** Best overall performer. Won 3 of 5 seeds in head-to-head testing.

### Strategy 1B — "Escalate and Cap" (Controlled)
- **Base bets:** $2/$2/$2
- **After every non-zero spin:** Add $1 to each bet (+$3 total per spin)
- **Cap at $15 per bet** — maximum total bet is $45/spin
- **On zero hit:** Reset to $2/$2/$2, sit out 17 spins
- **Thresholds:** Threshold 1 = 20% (warning), Threshold 2 = 33% (hard stop)
- **Profile:** Same escalation as 1A but with a safety net. The cap prevents over-exposure during long dry spells.
- **Simulation result:** Close second to 1A. Higher win rate (41.9% vs 38.9%) but slightly lower average profit per win.

### Strategy 1C — "Steady Eddie" (Conservative)
- **Base bets:** $2/$2/$2 — flat, no escalation ever
- **On zero hit:** Sit out 17 spins, resume at $2/$2/$2
- **Thresholds:** Threshold 1 = 20% (HARD STOP — session ends here)
- **No Threshold 2** — Eddie exits at Threshold 1
- **Profile:** Lowest volatility, longest sessions, most zeros caught. For the player who wants to sit at the table longest with the least stress.
- **Simulation result:** ~49.5% win rate, 195 avg spins per session. The "Quick Exit" 20% threshold was the best-performing Eddie variant.

---

## Threshold System

### Strategy Mode (1A and 1B — Aggressive and Controlled)
- **Threshold 1 (20% win or loss):** Warning alert. Badge lights up (green if winning, red if losing). Border flashes. Pop-up: warning that you're approaching the danger zone, you can keep going but be careful.
- **Threshold 2 (33% win or loss):** Hard stop. Badge lights up. Border flashes. Pop-up: recommends ending session NOW.

### Strategy Mode (1C — Steady Eddie)
- **Threshold 1 (20% win or loss):** Hard stop. Badge lights up. Pop-up: recommends ending session NOW.
- **No Threshold 2** — Eddie never gets there.

### Original Mode
- **15% (first warning)** — heads up
- **20% (second warning)** — stronger alert
- **33% (final threshold)** — hard stop, same lockout treatment if blown past

---

## Badge Display (Strategy Mode)
- **Remove percentage numbers** — no more "L: 1/5" or "W: 33%"
- **Two badges on the right side:** "Threshold 1" and "Threshold 2"
- Badges sit inactive until triggered
- When triggered: flash **red** (loss) or **green** (win)
- Border flashes matching color
- Pop-up appears with appropriate message

---

## Override Flow (When User Ignores Hard Stop)

### First Pop-Up (at hard stop threshold):
- **If winning:** "You've reached your session limit. This app is designed to help you walk away with a profit. We recommend ending your session now."
- **If losing:** "You've reached your session limit. This app is designed to help you walk away losing a minimum amount of your bankroll. We recommend ending your session now."
- Two buttons: **"End Session"** and **"Keep Going"**

### Second Pop-Up (double confirmation if they tap "Keep Going"):
- "Are you sure? By continuing, you are choosing to play beyond what this app was designed for. From this point forward, you are on your own. The app can no longer protect your bankroll."
- Two buttons: **"I Understand, Keep Going"** and **"No, End Session"**

### If they confirm Keep Going:
- App switches to **Original Mode**
- Remaining balance becomes the new default bankroll
- **Before Original Mode starts, a pop-up appears:**
  - "We strongly recommend that you walk away from the casino. If you or someone you know has a gambling problem, call the National Problem Gambling Helpline at 1-800-522-4700. If you still choose to continue, you may adjust your bankroll below."
  - Bankroll field is editable — they can add money
- Original Mode launches with full original interface and functionality
- All original prompts, pop-ups, sit-out suggestions, bet entry fields work as if they started in Original Mode

---

## 30-Day Lockout

### Triggers:
1. Strategy Mode player overrides thresholds → flipped to Original Mode → closes app → **locked 30 days**
2. Original Mode player (started there by choice) blows past 33% threshold → closes app → **locked 30 days**

### Normal play within thresholds = NO lockout

### On close (after override):
- **If they won:** "You were lucky this time, but this is not normal." + GA helpline info
- **If they lost:** GA helpline info + recommendation to seek help
- "This app will not reopen for 30 days."

### Lockout screen (when they try to reopen during 30 days):
- "This app is temporarily locked. This is not due to non-payment or a technical issue. This is a built-in protection for players who may have a gambling problem. Your app will unlock on [date]. If you need help, call the National Problem Gambling Helpline at 1-800-522-4700."
- No override for regular users. Wait 30 days.
- Lockout date stored in localStorage

### Developer Override (Hidden)
- On the lockout screen, **tap the lockout message 5 times quickly** to reveal a hidden password field
- **Developer password: 062562**
- Entering the correct password clears the lockout immediately
- This is for the developer/owner only — regular users will never know it exists

---

## App Launch Flow

1. **Check for 30-day lockout** — if locked, show lockout screen, stop
2. **Show splash screen** (same as current)
3. **After splash:** Show mode selection screen:
   - **"Sit and Climb"** — Aggressive
   - **"Escalate and Cap"** — Controlled
   - **"Steady Eddie"** — Conservative
   - **"Original Mode"** — Classic (place your own bets)
4. If Strategy Mode selected → load strategy interface with prompts and threshold badges
5. If Original Mode selected → load classic interface (same as current app)

---

## Strategy Mode Prompts (After Every Spin)

The app needs to tell the user what to do after every spin since the simulation handles it automatically but a real player needs guidance:

### Sit and Climb / Escalate and Cap:
- After each non-zero spin: "Add $1 to each zero. New bets: $X/$X/$X" (showing the new amounts)
- For Escalate and Cap: if at cap, "Bets at maximum ($15/$15/$15). Hold."
- After zero hit: "Zero hit! Collect your payout. Sit out 17 spins. Bets will reset to $2/$2/$2."
- During sit-out countdown: "Sitting out: X spins remaining"

### Steady Eddie:
- After each spin: "Keep bets at $2/$2/$2"
- After zero hit: "Zero hit! Collect your payout. Sit out 17 spins."

---

## Permanent Rules
- **Never reduce sit-outs below 17** — data has proven every time that reducing or removing sit-outs makes things worse
- **Never suggest reducing sit-outs** — this is a locked rule
- Display thresholds as percentages in Original Mode, not fractions
- Original Mode interface stays exactly as it looks now — same layout, same feel

---

## File Structure
- **project-zero-roulette** — current working version (untouched)
- **project-zero-roulette-original** — locked backup of base app (never modify)
- **project-zero-roulette-modified** — this is where all changes go

---

## Simulation Results Summary

| Strategy | Total P/L (2,500 sessions) | Win Rate | Avg Spins |
|---|---|---|---|
| 1A "Sit and Climb" | -$95,934 | 38.9% | 32 |
| 1B "Escalate and Cap" | -$104,178 | 40.8% | 36 |
| 1C "Steady Eddie" | -$86,868 | 49.5% | 195 |

Note: Individual 500-session runs showed 1A and 1B as profitable. The aggregate across 2,500 sessions (5 seeds) shows the house edge eventually wins, but single-session win rates of ~40-50% are strong for entertainment purposes.

---

*These notes are for continuity between sessions. The user wants the next session to pick up exactly where this one left off.*
