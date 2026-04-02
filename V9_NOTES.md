# Version 9 Feature Ideas

## Manual Side Bet Button
- A dedicated button in Session Controls that lets the user manually trigger the side bet workflow at any time (not just on 6+ streak detection)
- User picks bet type (Color, Parity, Dozen, Column) and which value to bet on
- Shows the same % presets (5/10/15/custom) for stake calculation
- Asks keep zeros / remove zeros / adjust zero bets
- Shows the full win/loss outcome table
- Basically the full pattern overlay experience, on demand, anytime

## Simulation Mode vs. Live Betting Mode

**Purpose:** Separate practice/testing data from real casino performance data to protect the integrity of lifetime betting records.

### Mode Selection
- Simulation is the default mode
- Mode is selected at session start via a prompt or toggle in the settings bar
- Mode is locked once a session begins — must end session to switch
- Visual indicator in sticky header: "SIM" badge (blue) or "LIVE" badge (gold/green)

### Separate Data Tracks
- Each mode has its own Historical P/L stored independently in localStorage
- Simulation data can never contaminate Live data and vice versa
- Session History entries are tagged with mode (SIM/LIVE)
- CSV exports include mode label in the output

### Reset Protection by Mode

| Action | Simulation Mode | Live Mode |
|--------|----------------|-----------|
| Reset Historical P/L | Single confirmation (standard custom modal) | Double confirmation with 3-second delay before "Yes, Delete" activates |
| Clear Saved State | Standard confirm | Double confirm with warning about real casino data |

### Visual Differentiation
- Sticky header shows mode badge (SIM vs LIVE) next to balance
- Subtle color accent difference (e.g., blue tint for SIM, gold/green for LIVE)
- Enough to register at a glance without being distracting

### Future Consideration (V10+)
- Lifetime stats dashboard for Live mode: total sessions, total hours, overall win rate, biggest win/loss
- Historical P/L chart over time (Live mode only)
- Ability to peek at the other mode's Historical P/L without switching

### Sticky Sit-Out Bar Enhancement
- Already implemented in 8.3 — ensure it works identically in both modes
