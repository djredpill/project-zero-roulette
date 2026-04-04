# Build Notes — Key Code Locations

## Structure
- Lines 1-334: CSS styles
- Lines 336-350: Splash screen HTML
- Lines 352-534: Modal dialogs HTML (pattern, generic, sit-out, raise/hold, crisis, zero edit, leave, manual side bet, live confirm)
- Lines 535-554: Sticky header HTML
- Lines 556-725: Main app HTML (header, left panel, right sidebar)
- Lines 727-895: JS - state, globals, splash init, numpad builder
- Lines 897-1000: JS - modal queue system, generic confirm/prompt, sit-out suggestion
- Lines 1001-1100: JS - side bet, outcome table, audio, pattern analyzer
- Lines 1100-1210: JS - pattern check, flash border, mode switching, live double confirm
- Lines 1213-1270: JS - checkAlerts (current: 20/33/40 thresholds, 6 badges), crisis modal
- Lines 1272-1307: JS - raise/hold, zero edit
- Lines 1308-1418: JS - refresh function
- Lines 1420-1562: JS - saveState, handleSpin
- Lines 1564-1610: JS - rollback, sit-out controls
- Lines 1612-1628: JS - doResetSession
- Lines 1630-1724: JS - leave casino report
- Lines 1725-1826: JS - event handlers
- Lines 1827-2042: JS - more event handlers, manual side bet
- Lines 2043-2095: JS - loadState, init

## Key Changes Needed
1. Add lockout check at startup (before splash)
2. Add strategy selection screen (after splash, before main app)
3. Add state.strategy field ('sit-climb', 'escalate-cap', 'steady-eddie', 'original')
4. Replace 6 badge HTML with 2 threshold badges (strategy mode) / keep 3 badges for original mode (15/20/33)
5. Modify checkAlerts() for strategy-specific thresholds
6. Modify handleSpin() for strategy-specific bet escalation and prompts
7. Add override flow (double confirm → flip to original mode)
8. Add 30-day lockout logic (localStorage)
9. Add developer override (5 taps + password 062562)
10. Strategy mode: auto sit-out 17 (no choice), auto-set bets to $2/$2/$2
11. In strategy mode, hide zero edit, hide unit/bankroll config (lock to $1500/$2)
