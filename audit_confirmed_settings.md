# Audit: Confirmed Settings vs Current App Code

## 1. Side bets limited to first 20 spins only
**Status: NOT IMPLEMENTED**
- `runPatternCheck()` has no spin count check — it fires on every spin as long as there's a 6+ streak
- Need to add: `if(state.totalSpins > 20) return;` at the top of `runPatternCheck()`

## 2. Sit-out the full historical average
**Status: IMPLEMENTED (mostly)**
- Auto sit-out suggestion fires after zero hit (line 1422)
- Uses `getHistoricalAvgGap()` which returns the real historical average
- Default fallback is 24 when no data exists
- **Change needed:** Default fallback should be 17 (per confirmed setting #6: pre-loaded avg of 17)

## 3. Walk at 33% loss threshold
**Status: PARTIALLY IMPLEMENTED**
- Loss alerts exist at 20%, 33%, 40% (line 1111)
- 40% triggers crisis modal with options to leave
- But 33% does NOT trigger a walk suggestion — it only flashes the border and plays a sound
- **Change needed:** 33% loss should trigger a walk/leave suggestion (not just an alert)

## 4. Walk at 40% win threshold
**Status: PARTIALLY IMPLEMENTED**
- Win alerts exist at 20%, 33%, 40% (line 1111)
- 40% win flashes border and plays chime
- But there's NO walk/leave suggestion at 40% win
- **Change needed:** 40% win should trigger a "lock in profits and leave" suggestion

## 5. Raise unit when in ANY profit
**Status: NEEDS VERIFICATION**
- Raise/Hold modal fires after N spins (spinCounterMax, default 12)
- It always offers raise regardless of profit/loss
- The confirmed setting says raise when in ANY profit — this may mean the raise should only be offered when balance > bank
- **Current behavior seems correct** — it offers the choice, user decides

## 6. Pre-loaded historical average of 17 spins
**Status: NOT IMPLEMENTED**
- Default fallback in sit-out suggestion is 24 (line 1424)
- `getHistoricalAvgGap()` returns 0 when no data exists
- **Change needed:** Pre-load globalStats.allZeroGaps with a seed value that produces avg of 17, OR change default fallback from 24 to 17
