# Project Zero Roulette Manual — Revision Notes

## Status: Reading paused at page 12-13 of 41. User will continue later.

## PROTOCOL: Do NOT make any changes until the user has finished reading the ENTIRE manual and gives the go-ahead.

---

## Author / Pseudonym
- Creator pseudonym: **James Munchman** (M-U-N-C-H-M-A-N)
- Update copyright and author references when revising

---

## New Screenshots Received (from user, cropped)

| File | Description | Use In Section |
|------|-------------|----------------|
| IMG_3624.PNG | Tight crop of sticky header (Balance, SIM, S/Spins, Spins, zero bets) | Sticky Header section |
| IMG_3626.PNG | Last 36 numbers scrolling ticker in sticky header | Last 36 Numbers explanation |
| IMG_3628.PNG | Full view showing Last 36 in BOTH sticky header AND below number pad, plus SITTING OUT banner in both locations | Last 36 Numbers + Sit Out explanation |
| IMG_3630.PNG | Spin Input panel with full number pad, Place Spin, Random, bottom row | Section 5 - Entering Spins |
| streak_color.png | Color streak popup (6+ reds, suggests Black) | Streak alerts page (top-left of 2x2 grid) |
| streak_parity.png | Parity streak popup (6+ odds, suggests Even) | Streak alerts page (top-right of 2x2 grid) |
| streak_dozen.png | Dozen streak popup (6+ Dozen 1, suggests Dozen 2 coldest) | Streak alerts page (bottom-left of 2x2 grid) |
| streak_column.png | Column streak popup (6+ Column 1, suggests Column 2 coldest) | Streak alerts page (bottom-right of 2x2 grid) |
| ga_hotline_overlay.png | GA hotline overlay with 1-800-522-4700 (user cropped) | Splash screen / GA section |

---

## Manual Structure Changes

1. **Cover Page** — Use the splash screen image as an actual book-style cover (not just white page jumping into text)
2. **Preface** — Placeholder for user's personal story (coming later)
3. **Disclaimer** — Add "Some screenshots are from iPhone, others from the iPad version. All features are present in both versions."
4. **Glossary** — Plain English definitions, no jargon
5. **Quick Start Cheat Sheet** — Step 7 change: "Enter Spins (or choose Random if simulating)"
6. **Full Manual** — Extensive, every feature, every screenshot placed contextually
7. **Index** — Page numbers for every topic/section
8. **Numbered pages** throughout

---

## Content/Wording Changes

### Glossary
- **Zero Bet** definition: Change to "A bet placed on single 0, double 00, or the 0/00 split — or any combination of one, two, or all three of these zero bets."
- **All terms in plain English** — "popup box" not "modal," "flashing green/red border" not "flash state"

### Section 2 - App Overview
- Create **annotated layout diagram** using iPad landscape screenshot with blue numbered borders around: (1) Sticky Header, (2) Left Column, (3) Right Sidebar
- Numbers in the diagram correspond to numbered descriptions in the text

### Section 3 - Sticky Header
- Crop the screenshot tighter — use IMG_3624.PNG (no excess blank space at bottom)
- Use IMG_3626.PNG for the Last 36 numbers scrolling ticker
- Use IMG_3628.PNG to show Last 36 appears in BOTH sticky header AND below number pad, plus sit-out banner in both locations

### Section 5 - Entering Spins (Number Pad)
- Use IMG_3630.PNG for the number pad illustration
- Fix wording: NOT "red numbers appear on red buttons" — instead say "Red numbers on the wheel appear on red buttons. Black numbers on the wheel appear on black buttons." (Don't call them "dark" — call them "black")

### Side Bets
- Add asterisk note: "Individual bets on single numbers, corner bets, street bets, and other combination bets are NOT supported by this app. The only additional bets supported are the parity/group bets (red/black, odd/even, dozens, columns) because the system is based on playing the zeros."
- Casino policy note: "Note: Some casinos may not permit the use of electronic devices at the table. If questioned, this app simply records numbers electronically — the same way some players track results with pen and paper. However, be aware of your casino's policies before using the app at a live table."

### Streak Alerts
- Dedicated page with all 4 streak screenshots in 2x2 grid
- Blue borders around the streak title header in each screenshot
- Layout: Top row = Color (left) + Parity (right) — these have only 2 choices (opposite of streak)
- Bottom row = Dozen (left) + Column (right) — these have 3 choices, app picks the "coldest" (least hit in last 36)
- Explain double streaks: two popups can appear back-to-back (e.g., all odd reds triggers both parity AND color alerts)
- Note: streak popups only appear within the first 20 spins of a session

### Profit/Loss
- Add color indicator explanation: P/L amount displays in **green when in profit** and **red when at a loss**. Two ways to tell: the sign AND the color.

### Ghost Hits
- CODE CHANGE: When a ghost hit happens during sit-out, the number showing what you would have won should **flash/blink** and keep flashing until the next spin is entered (NOT the border — the winnings number itself)
- Manual: Explain that a flashing number during sit-out = ghost hit. Shows what you would have won but does NOT count toward bankroll.

### Sit-Out Suggestion
- Three-option popup already implemented (Use Default 17 / Use Historical Avg / Enter Custom / Cancel)

### Historical P/L
- Explain that Historical P/L is tracked **separately** for each mode (SIM, LIVE, TABLE)
- BUT total spin count is accumulated across ALL modes perpetually — used to calculate the average number of spins between zeros

### First-Spin Win Scenario
- Add explanation: With $5 on each zero bet ($15 total), if a zero hits on the very first spin, net profit = **$255**. Rare but it happens — you could walk away right then.
- This is the philosophy: risk $15 to win $255 (17:1 return). Most systems require risking far more for far less.

### Flashing Borders (general)
- Always describe as: "The border will flash green when alerting to a win threshold, or flash red when alerting to a loss threshold"

### Device Labels on Screenshots
- Every screenshot labeled with device and orientation: *(iPhone, Portrait)*, *(iPhone, Landscape)*, *(iPad, Portrait)*, *(iPad, Landscape)*

---

## APP Code Changes (to implement alongside manual revision)

1. **Ghost hit flashing** — Make the winnings number flash/blink during sit-out ghost hits until next spin
2. **Background theme colors** — Lighten Blue, Green, Turquoise themes (keep White and Dark as-is). Same hues but much lighter, almost pastel but not white.
3. **Splash screen** — Already done (Revision 11): double-tap for GA hotline, 2-line red text with dark pill

---

## Future Items (NOT for this revision)

1. **Simulation tests** — Run with $2,000 and $2,500 starting bankrolls to test if higher bankroll improves win rate
2. **Default bankroll recommendation** — If simulations prove a specific bankroll is optimal, add recommendation to manual
3. **Preface** — User will provide personal story about how/why the app was created
4. **James Munchman pseudonym** — Update all author/copyright references

---

## Screenshots from User's Original Batch (22 total)

| File | Description |
|------|-------------|
| IMG_3564.PNG | iPad landscape - full app overview |
| IMG_3565.PNG | iPad landscape - session in progress |
| IMG_3566.PNG | iPad landscape - settings/controls area |
| IMG_3567.PNG | iPhone portrait - session setup |
| IMG_3569.PNG | Side bet popup (Bet Type options) |
| IMG_3571.PNG | 40% Loss Alert popup |
| IMG_3574.PNG | iPhone portrait - number pad area |
| IMG_3575.PNG | Session history table |
| IMG_3576.PNG | Zero bet cards |
| IMG_3577.PNG | Session summary / right sidebar |
| IMG_3578.PNG | Settings area |
| IMG_3579.PNG | Crisis protection / loss alerts |
| IMG_3580.PNG | Sitting out state |
| IMG_3581.PNG | Session controls |
| IMG_3582.PNG | Background themes |
| IMG_3583.PNG | Session report |
| IMG_3584.PNG | Mid-session edit |
| IMG_3585.PNG | Side bet in action |
| IMG_3586.PNG | Full app with data |
| IMG_3587.PNG | Another full view |
| IMG_3588.PNG | Splash screen (old version) |
| IMG_3590.PNG | iPad landscape full view |

---

## Reading Progress
- **Completed**: Pages 1-12 (Cover through Section 5 - Entering Spins, Number Pad)
- **Remaining**: Pages 13-41
- **Resume point**: Page 13 (after Number Pad section)
