# Project Zero Roulette

## Complete User Manual

**Revision 11** | Copyright 2026 James Jones Jr. All rights reserved.

---

> **Note on Screenshots:** Some screenshots in this manual were captured on an iPhone, while others were taken on the iPad version of the application. All features described in this manual are present and function identically on both devices. The layout may appear slightly different depending on your screen size and orientation, but every button, setting, and feature works the same way regardless of which device you are using.

> **Disclaimer:** This application is intended for statistical analysis and testing purposes only. It does not facilitate real-money gambling. If you or someone you know has a gambling problem, please seek help. Call the National Problem Gambling Helpline at 1-800-GAMBLER.

---

## Preface

*[To be provided by the author — the personal story behind the creation of Project Zero Roulette and what inspired its development.]*

---

## Glossary of Terms

Before diving into the manual, here are some common terms you will encounter throughout this guide. These definitions are written in plain, everyday language so that anyone can follow along regardless of technical background.

| Term | Definition |
|------|-----------|
| **Bankroll** | The total amount of money you start a session with. This is your budget for the session. |
| **Unit** | The base dollar amount placed on each zero bet per spin. For example, if your unit is \$5, you are betting \$5 on zero every spin. |
| **Session** | A single playing period from the time you press "Start Session" until you leave or reset. |
| **Spin** | One round of the roulette wheel. Each time the ball lands on a number, that counts as one spin. |
| **Zero Bet** | A bet placed on the green zero (0) pocket, the double-zero (00) pocket, or the split between them. This is the core strategy of the app. |
| **Side Bet** | An additional bet placed on something other than zero, such as a color (red or black), odd or even, a dozen, or a column. |
| **Popup Box** | A window that appears on top of the screen and requires you to respond (by tapping a button) before you can continue using the app. |
| **Sticky Header** | The bar at the very top of the screen that stays visible even when you scroll down. It always shows your current balance, mode, and other key information. |
| **Sit Out** | A feature that lets you skip a certain number of spins without placing bets. The app tracks what happens during those skipped spins. |
| **Ghost Hit** | When a zero lands while you are sitting out. The app counts these so you can see what you would have won if you had been playing. |
| **Historical Average** | The average number of spins between zero hits across all of your sessions. The app tracks this over time to help you make decisions. |
| **P/L** | Profit or Loss. A positive number means you are ahead; a negative number means you are behind. |
| **SIM Mode** | Simulation mode. You are practicing or testing without real money. |
| **LIVE Mode** | You are tracking bets at an automated (electronic) roulette table in a real casino. |
| **TABLE Mode** | You are tracking bets at a dealer-operated roulette table in a real casino. |
| **Streak** | A run of consecutive spins where the same type of outcome keeps repeating (for example, seven red numbers in a row). |
| **PWA** | Progressive Web App. This means you can install the app to your home screen and use it like a regular app, even without an internet connection. |
| **CSV** | A file format (Comma-Separated Values) that can be opened in spreadsheet programs like Excel or Google Sheets. Used for exporting your session data. |
| **Flashing Border** | The border around the entire screen will briefly flash a color to alert you. It will flash green when alerting to a win threshold, or flash red when alerting to a loss threshold. |

---

## Quick Start Cheat Sheet

If you want to get up and running fast, follow these steps. You can read the detailed sections later.

**Step 1 — Open the App.** Navigate to the app in your browser or tap the icon on your home screen. You will see the splash screen with the roulette table image.

**Step 2 — Enter the App.** Tap once anywhere on the splash screen to enter. (If you need the Gamblers Anonymous Hotline, tap twice instead.)

**Step 3 — Set Your Bankroll.** In the setup area, enter your starting bankroll (the total amount you are willing to play with). The default is \$1,500.

**Step 4 — Choose Your Table Type.** Select "American (0 & 00)" or "European (single 0)" from the Table Type dropdown.

**Step 5 — Choose Your Mode.** Tap SIM for practice, LIVE for an electronic table, or TABLE for a dealer table.

**Step 6 — Press Start Session.** This locks in your settings and begins tracking.

**Step 7 — Enter Spins.** After each spin of the roulette wheel, tap the number that came up on the number pad. The app automatically records it.

**Step 8 — Watch Your Balance.** The sticky header at the top always shows your current balance, and the border will flash green or red when you hit win or loss thresholds.

**Step 9 — Follow the Alerts.** When the app detects a streak or suggests sitting out, read the popup box and choose your action.

**Step 10 — End Your Session.** When you are done, tap "Leave The Casino" to see your full session report. You can export it as a CSV file or email it to yourself.

That is the basics. Read on for the full, detailed explanation of every feature.

---

## 1. The Splash Screen

When you first open Project Zero Roulette, you are greeted by the splash screen. This is a full-screen display featuring the app's logo and roulette table artwork, along with important legal disclaimers about responsible gaming.

![Splash Screen](/home/ubuntu/project-zero-roulette/manual/images/splash_screen.PNG)

At the bottom of the splash screen, you will see red text inside a dark rounded box that reads:

> **Tap once to enter, tap twice for**
> **Gamblers Anonymous Hotline**

This gives you two options:

**Tapping once** will play a brief roulette ball sound effect and smoothly fade the splash screen away, revealing the main application underneath. There is a very short delay (less than half a second) before the app enters, which is normal — the app is simply making sure you did not intend to tap twice.

**Tapping twice quickly (double-tap)** will not enter the app. Instead, a dark overlay will appear displaying the Gamblers Anonymous Hotline number.

### The Gamblers Anonymous Hotline Overlay

If you double-tap the splash screen, you will see a dark screen with the following information displayed prominently in the center:

![GA Hotline Overlay](/home/ubuntu/project-zero-roulette/manual/images/ga_hotline_overlay.png)

The overlay shows "Gamblers Anonymous Hotline" at the top, followed by the phone number **1-800-522-4700** in large green text. Below the number, it says "Tap the number to call." If you are on a phone, tapping the number will immediately dial it. There is also a "Back" button at the bottom that returns you to the splash screen so you can enter the app if you choose.

This feature exists because Project Zero Roulette takes responsible gaming seriously. The hotline is available 24 hours a day, 7 days a week, and is completely free and confidential.

---

## 2. App Overview and Layout

Once you enter the app, you will see the main interface. On a tablet in landscape orientation, the entire app is visible at once, organized into three main areas.

![Full App Overview — iPad Landscape](/home/ubuntu/project-zero-roulette/manual/images/full_app_overview.PNG)

The layout is divided as follows:

**The Sticky Header** runs across the top of the screen and stays visible at all times, even when you scroll. It shows your current balance, your mode (SIM, LIVE, or TABLE), the number of spins in your session, your spin counter, your zero bet amounts, and the last 36 numbers that have come up.

**The Left Column** contains the spin input area with the number pad, the session controls (buttons for various actions), the zero bet display, and the session history table.

**The Right Sidebar** contains the session summary (bankroll, profit/loss), the loss and win alert badges, and the settings panel.

On a phone, these sections stack vertically since there is less screen space, but all the same features are present. You simply scroll down to access different sections.

![Full App with Title Visible](/home/ubuntu/project-zero-roulette/manual/images/full_app_with_title.PNG)

At the very top of the app (above the sticky header when scrolled to the top), you will see the title "Project Zero Roulette" with a note that reads: "American table by default. Switch to European to disable 00 and split."

---

## 3. Getting Started — Session Setup

Before you can begin tracking spins, you need to configure your session. The setup area is located in the upper portion of the app.

![Session Setup Area](/home/ubuntu/project-zero-roulette/manual/images/session_setup.PNG)

Here is what each setting does:

**Starting Bankroll** — This is the total amount of money you are starting with. The default is \$1,500. Type in whatever amount you brought to the table (or whatever amount you want to practice with in SIM mode). This number is used to calculate your profit/loss percentages and trigger loss alerts.

**Unit per Zero** — This is the base dollar amount you will bet on each zero pocket per spin. The default is \$5. If you set this to \$5 and you are playing an American table, you will be betting \$5 on 0, \$5 on the 0/00 split, and \$5 on 00 — for a total of \$15 per spin in zero bets.

**Table Type** — Choose between:
- **American (0 & 00):** The standard American roulette wheel with both a single zero and a double zero. You will have three zero bets: 0, 0/00 split, and 00.
- **European (single 0):** The European wheel with only a single zero. The 00 and split bets are automatically disabled.

**Background** — Choose your preferred color theme. Options include White, Dark, Blue, Green, Turquoise, Gold, Pink, and Grey. This is purely cosmetic and does not affect gameplay. More detail on themes is provided in Section 12.

**Mode** — This is an important choice that determines how the app treats your data:

| Mode | Badge Color | Purpose |
|------|------------|---------|
| **SIM** | Blue | Simulation / practice mode. Use this when you are not at a real table. |
| **LIVE** | Amber/Yellow | For tracking at an automated (electronic) roulette machine in a casino. |
| **TABLE** | Purple | For tracking at a dealer-operated roulette table in a casino. |

Each mode maintains its own separate historical profit/loss record. This means your practice sessions in SIM mode will never mix with your real casino data in LIVE or TABLE mode. Once you start a session, the mode is locked and cannot be changed until you reset or leave.

**Session Balance** — Displayed to the right of the setup area, this shows your current balance in large text. Before starting, it reflects your starting bankroll.

**Start Session** — Once you have configured everything, tap this button to begin. Your settings will be locked in, and the app will begin tracking your spins.

---

## 4. The Sticky Header

The sticky header is the bar that remains fixed at the top of your screen at all times, no matter how far you scroll down. It provides a constant snapshot of your most important information.

![Sticky Header](/home/ubuntu/project-zero-roulette/manual/images/sticky_header.PNG)

The header displays the following information from left to right:

**Balance** — Your current session balance, shown in bold. This updates in real time after every spin.

**Mode Badge** — A small colored label showing which mode you are in. It will say "SIM" in blue, "LIVE" in amber, or "TABLE" in purple.

**S/Spins** — Short for "Session Spins." This is the total number of spins you have recorded in the current session.

**Spins** — This shows your spin counter in the format "X/Y" (for example, "0/12"). The first number counts up with each spin, and when it reaches the second number, the app will ask if you want to raise your bet. More on this in the Settings section.

**Zero Bet Boxes** — Three small boxes showing your current bet amounts: "0: \$5", "Spl: \$5", and "00: \$5" (on an American table). You can tap any of these boxes to open the zero bet editor and change your amounts. On a European table, only the "0" box appears.

**Last 36 Numbers** — A horizontal ribbon of small colored circles showing the most recent numbers that have come up. Each number is color-coded: green for 0 and 00, red for red numbers, and black for black numbers. This ribbon scrolls horizontally if there are more numbers than can fit on screen.

**Sitting Out Bar** — When you are sitting out spins, a pink bar appears below the other header elements showing "SITTING OUT: X SPINS" along with Edit and Cancel buttons. This bar is only visible when the sit-out feature is active.

---

## 5. Entering Spins — The Number Pad

The number pad is your primary way of recording what happens at the roulette table. After each spin of the wheel, you tap the number that came up.

![Number Pad and Session Controls](/home/ubuntu/project-zero-roulette/manual/images/number_pad_controls.PNG)

**The Spin Input Field** — At the top of the number pad area, there is a text field labeled "Spin Input." You do not need to type into this field directly. Instead, use the number pad below it.

**Place Spin and Random Buttons** — Next to the input field, "Place Spin" submits the currently entered number. "Random" generates a random valid number (useful in SIM mode for quick practice).

**The Number Pad** — A grid of buttons numbered 1 through 36, each color-coded to match the roulette wheel:
- **Red numbers** appear on red buttons
- **Black numbers** appear on dark buttons
- **0 and 00** appear on green buttons

When you tap a number, it is automatically submitted as a spin. You do not need to tap "Place Spin" afterward — the app records it immediately.

**Bottom Row Buttons:**
- **0** — Records a zero hit (green)
- **00** — Records a double-zero hit (green, American tables only)
- **Undo** — Removes the last spin you entered (in case of a mistake)
- **Sit Out** — Opens the sit-out feature
- **Random** — Generates and submits a random number
- **SPIN** — Same as Place Spin, submits whatever is in the input field

After each spin is recorded, the app immediately calculates your profit or loss for that spin, updates your balance, checks for streaks, and updates all displays.

---

## 6. Zero Bets — The Core Strategy

The entire premise of Project Zero Roulette is built around betting on zero. Every spin, you place bets on the zero pockets, and the app tracks whether those bets win or lose.

![Zero Bet Boxes and Session History](/home/ubuntu/project-zero-roulette/manual/images/bottom_section.PNG)

The zero bet display shows three boxes (on an American table):

**Bet on 0** — Your straight-up bet on the single zero. A winning hit pays 35 to 1.

**Bet on 0/00 Split** — Your split bet covering both 0 and 00. A winning hit pays 17 to 1.

**Bet on 00** — Your straight-up bet on the double zero. A winning hit pays 35 to 1.

Each box shows the current bet amount in large text, along with the potential payout below it. You can tap any of these boxes to open the Zero Bet Editor, which allows you to change the amounts individually or set a uniform amount for all three.

When you are playing a European table (single zero only), the 00 and split boxes are hidden, and you only see the single zero bet.

**How Zero Bets Are Calculated Each Spin:**
- If the spin result is any number 1-36, you lose the total of all your active zero bets.
- If the spin result is 0, you win on your "Bet on 0" (35:1 payout) and your "Bet on 0/00 Split" (17:1 payout), but you lose your "Bet on 00."
- If the spin result is 00, you win on your "Bet on 00" (35:1 payout) and your "Bet on 0/00 Split" (17:1 payout), but you lose your "Bet on 0."

The "Click any Zero box to change individual bets" hint appears below the boxes as a reminder that they are tappable.

### The Zero Bet Editor

When you tap any zero bet box (either in the main display or in the sticky header), a popup box appears that lets you adjust your bets.

The editor provides:
- **Uniform Bet** — Enter a single amount and tap "Apply to All" to set all three bets to the same value.
- **Individual Inputs** — Separate fields for Bet on 0, Bet on 0/00 Split, and Bet on 00, so you can set different amounts for each.
- **Save / Cancel** — Save applies your changes; Cancel closes the editor without changing anything.

---

## 7. Session History

The session history table keeps a complete record of every spin in your current session.

![Session History Showing a Losing Streak](/home/ubuntu/project-zero-roulette/manual/images/session_history_losses.PNG)

The table has the following columns:

| Column | What It Shows |
|--------|--------------|
| **Time** | The time the spin was recorded (e.g., "08:20 AM") |
| **Mode** | A small colored badge showing SIM, LIVE, or TABLE |
| **0's Stake** | The total amount you had wagered on zero bets for that spin |
| **Side** | Any side bet results for that spin, color-coded green for wins and red for losses |
| **Net** | Your net profit or loss for that individual spin, shown in green (win) or red (loss) |
| **Bal.** | Your running balance after that spin |

The table scrolls vertically if you have many spins, and the most recent spin always appears at the top. This gives you a clear picture of how your session has progressed over time.

---

## 8. Session Summary and Alerts

The right sidebar (or below the main area on a phone) contains your session summary and alert system.

### Session Summary

The session summary panel shows three key numbers:

**Starting Bankroll** — The amount you began the session with.

**Session P/L** — Your profit or loss for the current session. This number is green when you are ahead and red when you are behind.

**Historical P/L** — Your cumulative profit or loss across all sessions in the current mode. For example, if you have played three SIM sessions and are down a total of \$105 across all of them, this will show -\$105 in red.

### Loss and Win Alerts

Below the summary, there are six alert badges arranged in two rows:

![Settings and Alert Badges](/home/ubuntu/project-zero-roulette/manual/images/settings_section.PNG)

**Loss Alerts (Red):**
- **L: 1/5** — Lights up when you have lost 20% of your starting bankroll
- **L: 1/3** — Lights up when you have lost 33% of your starting bankroll
- **L: 2/5** — Lights up when you have lost 40% of your starting bankroll (triggers the crisis protection popup)

**Win Alerts (Green):**
- **W: 1/5** — Lights up when you have won 20% above your starting bankroll
- **W: 1/3** — Lights up when you have won 33% above your starting bankroll
- **W: 2/5** — Lights up when you have won 40% above your starting bankroll

When a loss threshold is reached, the border around the entire screen will flash red to get your attention. When a win threshold is reached, the border will flash green and a pleasant chime will play.

The badges start out faded (dimmed) and become fully bright and opaque when their threshold is reached. This gives you a quick visual indicator of where you stand at a glance.

### The 40% Loss Alert — Crisis Protection

When you lose 40% of your starting bankroll, the app takes extra steps to protect you. The border will flash red urgently (faster than normal), and a popup box will appear with a red border at the top.

![40% Loss Alert — Crisis Protection](/home/ubuntu/project-zero-roulette/manual/images/loss_alert_crisis.PNG)

This popup tells you exactly how much you have lost and what your current balance is. It then gives you three choices:

**Continue Playing** — Dismiss the alert and keep going. The app will not stop you, but it wants to make sure you are making a conscious decision.

**Reset Session** — Start over with a fresh session. Your historical record is preserved, but the current session is wiped clean.

**Quit** — This takes you to the "Leave The Casino" report so you can end your session and review your results.

This feature exists because it is easy to lose track of how much you have lost in the heat of the moment. The app forces you to stop, acknowledge the situation, and make a deliberate choice about what to do next.

---

## 9. The Sit-Out System

One of the most important features of Project Zero Roulette is the sit-out system. The idea is simple: after a zero hits, you may want to skip a certain number of spins before betting again, since zeros tend to be spaced apart.

### Automatic Sit-Out Suggestion

Every time a zero (0 or 00) hits, the app will automatically ask if you want to sit out. A popup box appears with the title "Zero Hit — Sit Out?" and gives you three options:

![Three-Option Sit-Out Popup](/home/ubuntu/project-zero-roulette/manual/images/sitout_three_option.png)

**Use Default (17 spins)** — This uses the built-in default of 17 spins, which is based on the mathematical average gap between zeros on an American roulette wheel (38 pockets, so on average a specific zero hits once every 38 spins, but any zero hits more frequently).

**Use Historical Avg (X spins)** — This option uses your personal historical average — the actual average number of spins between zero hits across all your sessions. If the app does not yet have enough data to calculate this (for example, during your very first session), this button will be grayed out and unavailable. As you play more sessions, this number becomes more accurate and more useful.

**Enter Custom** — This lets you type in any number you want. A second popup box will appear asking you to enter the number of spins you would like to sit out.

**Cancel** — Dismisses the popup without sitting out.

### Manual Sit-Out

You can also choose to sit out at any time by tapping the "Sit Out Spins" button in the session controls area, or by tapping the "Sit Out" button on the number pad. This opens the same three-option popup described above.

### The Sitting-Out State

Once you activate a sit-out, the app enters the sitting-out state. A prominent pink bar appears both in the main area and in the sticky header.

![Sitting Out State](/home/ubuntu/project-zero-roulette/manual/images/sitting_out_state.PNG)

The pink bar shows:
- **"SITTING OUT: X SPINS"** — How many spins remain in your sit-out period
- **Edit button** — Tap to change the number of remaining sit-out spins
- **Cancel button** — Tap to end the sit-out immediately and resume betting

While sitting out, you still enter each spin result as it happens. The app does not place any bets during these spins, so your balance does not change. However, the app does track "ghost hits" — if a zero lands while you are sitting out, the app records it and shows you what you would have won. This information appears as an amber-colored note next to the sit-out counter.

When the sit-out period ends (the counter reaches zero), the app automatically resumes normal betting on the next spin.

---

## 10. Streak Detection and Side Bet Alerts

Project Zero Roulette constantly monitors the spin results for streaks — runs of six or more consecutive outcomes of the same type. When a streak is detected, the app alerts you and suggests a side bet.

The app watches for four types of streaks:

| Streak Type | Example |
|-------------|---------|
| **Color** | Six or more reds in a row (or six or more blacks) |
| **Parity** | Six or more odd numbers in a row (or six or more even) |
| **Dozen** | Six or more numbers from the same dozen (1-12, 13-24, or 25-36) |
| **Column** | Six or more numbers from the same column |

When a streak is detected, a popup appears with an amber/yellow border showing:

- The type of streak and how long it has been running
- A suggestion for which side bet to place (for example, if there have been seven reds in a row, it will suggest betting on black)
- Percentage buttons (5%, 10%, 15%, or custom) to calculate how much of your balance to wager
- A dollar amount field for the side bet stake
- An outcome breakdown table showing what happens if you win or lose, with and without your zero bets

You then have three choices:

**Bet + Keep Zeros** — Place the side bet while continuing your normal zero bets.

**Bet + Remove Zeros** — Place the side bet but temporarily remove your zero bets for the next spin (useful if you want to go all-in on the side bet).

**Ignore** — Dismiss the alert and continue without placing a side bet.

If multiple streaks are happening at the same time (for example, a color streak and a parity streak simultaneously), the app will show them one at a time, so you can decide on each one individually.

---

## 11. Placing Side Bets Manually

You do not have to wait for a streak alert to place a side bet. At any time, you can tap the "Place Side Bet" button in the session controls area to open the side bet popup.

![Place a Side Bet Popup](/home/ubuntu/project-zero-roulette/manual/images/side_bet_popup.PNG)

The popup lets you configure your side bet step by step:

**Bet Type** — Choose from Color, Parity, Dozen, or Column by tapping the corresponding button.

**Bet Value** — After selecting a type, the available values appear. For example, if you chose "Color," you will see "Red" and "Black" buttons. If you chose "Dozen," you will see "1st (1-12)," "2nd (13-24)," and "3rd (25-36)." The app automatically highlights the "coldest" option (the one that has appeared least recently) as a suggestion.

**Stake Amount** — Use the percentage buttons (5%, 10%, 15%, or custom) to set your stake as a percentage of your current balance, or type a specific dollar amount directly.

**Outcome Breakdown** — A table at the bottom shows you exactly what will happen in every possible scenario: if the side bet wins, if it loses, and how your zero bets factor in. This helps you understand the full risk before committing.

**Action Buttons:**
- **Bet + Keep Zeros** — Places the side bet while keeping your zero bets active
- **Bet + Remove Zeros** — Places the side bet but sets your zero bets to \$0 for the next spin
- **Cancel** — Closes the popup without placing any bet

Once a side bet is placed, an "Active Stake" bar appears below the spin input showing what bets are currently active. The side bet is settled on the very next spin — if the outcome matches your bet, you win; if not, you lose. Color and parity bets pay 2 to 1, while dozen and column bets pay 3 to 1.

---

## 12. Background Themes and Customization

Project Zero Roulette offers eight different background themes so you can customize the look of the app to your preference.

![Background Themes](/home/ubuntu/project-zero-roulette/manual/images/background_themes.PNG)

The available themes are:

| Theme | Description |
|-------|-------------|
| **White** | Clean, light background. The default theme. |
| **Dark** | Dark navy background with light text. Easy on the eyes in low light. |
| **Blue** | Deep blue background with soft blue text. |
| **Green** | Forest green background. |
| **Turquoise** | Teal/turquoise background. |
| **Gold** | Warm gold/brown background. |
| **Pink** | Deep magenta/pink background. |
| **Grey** | Neutral dark grey background. |

To change your theme, use the "Background" dropdown in the setup area before or during your session. The theme change takes effect immediately. All text, buttons, cards, and popup boxes automatically adjust their colors to remain readable against the chosen background.

---

## 13. Settings

The settings panel is located in the right sidebar (or at the bottom of the page on a phone) and controls several important behaviors.

![Settings Panel](/home/ubuntu/project-zero-roulette/manual/images/settings_section.PNG)

**Auto Increment Every N Spins** — When this checkbox is enabled, the app will ask you if you want to raise your zero bet amounts after a certain number of spins. This is based on the strategy of gradually increasing your bets over time.

**N Spins** — The number of spins between raise prompts. The default is 12. After every 12 spins, a popup will appear asking "Raise or Hold?" with the option to increase your unit by the increment amount.

**Increment $** — The dollar amount to add to your unit when you choose to raise. The default is \$5. So if your unit is \$5 and you raise, it becomes \$10.

**Spin Counter** — Shows your current position in the spin cycle as "X / Y" (for example, "4/12" means you are 4 spins into a 12-spin cycle). You can manually edit both numbers if needed. The "Reset" button sets the counter back to 0.

**Show 0/00 Split Bet** — When checked, the split bet between 0 and 00 is active and visible. Uncheck this to hide and disable the split bet (it is automatically unchecked on European tables).

**Auto-Place Split Bet When Shown** — When checked, the split bet is automatically placed at the same amount as your unit whenever the split bet is visible. Uncheck this if you want to manually control the split bet amount.

---

## 14. Session Controls

The session controls area provides buttons for various actions you can take during or between sessions.

![Session Controls](/home/ubuntu/project-zero-roulette/manual/images/number_pad_controls.PNG)

Here is what each button does:

**Reset Session** — Ends the current session and returns you to the setup screen where you can change your mode, bankroll, and other settings. Your historical P/L is preserved.

**Export CSV** — Downloads your complete session data as a CSV file that you can open in Excel, Google Sheets, or any spreadsheet program. The file includes a header with your session summary followed by a row for every spin.

**Reset Historical P/L** — Resets your cumulative historical profit/loss back to zero. If you are in LIVE or TABLE mode, the app will ask you to confirm twice (with a countdown timer) because this action cannot be undone and affects your real casino tracking data.

**Sit Out Spins** — Opens the three-option sit-out popup (described in Section 9) so you can manually initiate a sit-out period.

**Place Side Bet** — Opens the manual side bet popup (described in Section 11).

**Undo Last Spin** — Reverses the most recent spin you entered. This is useful if you accidentally tapped the wrong number. It restores your balance, removes the spin from your history, and adjusts all statistics accordingly.

**Edit Bankroll/Unit** — Allows you to change your starting bankroll and unit amount in the middle of a session without resetting. A popup box will appear with fields for the new values.

**Leave The Casino** — Ends your session and displays a comprehensive session report (described in Section 15).

**Clear Saved App State** — This is a nuclear option that erases all saved data from the app, including all session history, historical P/L, and settings for all modes. The app will reload completely fresh, as if you had just installed it. Use this only if you want to start completely over.

---

## 15. Leaving the Casino — The Session Report

When you are ready to end your session, tap "Leave The Casino." The app will first ask you to confirm, and then display a detailed session report.

![Session Report](/home/ubuntu/project-zero-roulette/manual/images/session_report.PNG)

The report includes:

**Mode** — Which mode you were playing in (SIM, LIVE, or TABLE), spelled out in full.

**Starting Bankroll** — The amount you started with.

**Ending Balance** — The amount you finished with.

**Session P/L** — Your profit or loss for this session, shown in green (profit) or red (loss).

**Historical P/L** — Your cumulative profit or loss across all sessions in this mode.

**Total Spins** — How many spins you recorded during the session.

**Est. Session Duration** — An estimate of how long the session lasted, based on the time between your first and last spin.

**Session Avg Spins Between Zeros** — The average number of spins between zero hits during this particular session.

**Historical Avg Spins Between Zeros** — The average across all your sessions.

**Sit-Out Statistics** — If you used the sit-out feature, this section shows how many times you sat out, the total number of spins you sat out, the average length of each sit-out, and how many ghost hits occurred (zeros that landed while you were sitting out).

At the bottom of the report, you have several options:

**Email Report** — Enter an email address and the app will open your email client with the report pre-filled, ready to send.

**Export CSV** — Download the full session data as a spreadsheet file.

**Confirm & Leave** — Close the report and reset the app for a new session.

**Stay** — Dismiss the report and continue your current session.

---

## 16. Mid-Session Adjustments

You do not have to commit to your initial settings for the entire session. The app provides several ways to make adjustments on the fly.

![Mid-Session Adjustments](/home/ubuntu/project-zero-roulette/manual/images/mid_session_adjustments.PNG)

**Edit Bankroll/Unit** — Tap this button in the session controls to change your starting bankroll or unit amount without resetting your session. This is useful if you decide to add more money to your bankroll or change your betting strategy mid-session.

**Edit Zero Bets** — Tap any zero bet box (in the main display or the sticky header) to open the zero bet editor. You can change individual bet amounts or apply a uniform amount to all three.

**Edit Spin Counter** — In the settings panel, you can manually change the spin counter numbers. This is useful if you lost count or want to adjust the cycle.

**Edit Sit-Out** — While sitting out, tap the "Edit" button to change the number of remaining sit-out spins, or tap "Cancel" to end the sit-out immediately.

---

## 17. The Raise or Hold Prompt

When the auto-increment feature is enabled (which it is by default), the app will prompt you after every N spins (default: 12) to decide whether to increase your bets.

A popup box appears with the title "Raise or Hold?" showing your current unit amount and the proposed new amount. For example, if your unit is \$5 and the increment is \$5, it will offer to raise to \$10.

**Raise** — Increases your unit by the increment amount. All three zero bets are updated accordingly.

**Hold** — Keeps your bets at the current level. The spin counter resets and will prompt you again after another N spins.

This feature is designed to support a progressive betting strategy where you gradually increase your stakes over time.

---

## 18. Modes — SIM, LIVE, and TABLE

The three modes serve different purposes and keep their data completely separate.

**SIM (Simulation)** — This is the default mode, shown with a blue badge. Use SIM mode when you are practicing, testing strategies, or playing without real money. You can freely reset, experiment, and make mistakes without affecting your real casino records.

**LIVE (Automated Table)** — Shown with an amber/yellow badge. Use this mode when you are at a real casino playing on an electronic or automated roulette machine. Because this involves real money, the app adds extra protections: destructive actions like resetting historical P/L require a double confirmation with a countdown timer.

**TABLE (Dealer Table)** — Shown with a purple badge. Use this mode when you are at a real casino playing at a table with a live dealer. It has the same extra protections as LIVE mode.

Each mode maintains its own independent historical P/L, so your simulation practice never contaminates your real casino tracking data. When you switch modes, the app loads the historical data for that mode automatically.

---

## 19. Installing as a Home Screen App (PWA)

Project Zero Roulette is a Progressive Web App, which means you can install it on your phone or tablet and use it just like a regular app — with its own icon, full-screen display, and even some offline capability.

**On iPhone/iPad (Safari):**
1. Open the app in Safari
2. Tap the Share button (the square with an arrow pointing up)
3. Scroll down and tap "Add to Home Screen"
4. Tap "Add" in the upper right corner

**On Android (Chrome):**
1. Open the app in Chrome
2. Tap the three-dot menu in the upper right
3. Tap "Add to Home Screen" or "Install App"
4. Confirm the installation

Once installed, the app will appear on your home screen with the Project Zero Roulette icon. Tapping it opens the app in full-screen mode without the browser address bar, giving you more screen space and a cleaner experience.

---

## 20. Audio Feedback

The app uses sound effects to provide audio feedback for important events:

**Splash Screen Sound** — When you tap to enter the app, a brief roulette ball spinning sound plays. This sets the atmosphere and confirms that your tap was registered.

**Win Chime** — When you reach a win threshold (W: 1/5, W: 1/3, or W: 2/5), a pleasant ascending chime plays along with the green flashing border.

**Loss Alert Sound** — When you reach a loss threshold (L: 1/5, L: 1/3, or L: 2/5), a descending tone plays along with the red flashing border. The 40% loss alert plays a more urgent, faster version of this sound.

These sounds can be heard through your device's speakers or headphones. If your device is on silent/vibrate mode, you may not hear them.

---

## 21. State Persistence — Your Data Is Saved

Project Zero Roulette automatically saves your data after every action. If you close the app, switch to another app, or even restart your device, your session will be right where you left it when you come back.

The app saves:
- Your current session state (balance, history, settings, active bets)
- Your historical P/L for each mode (SIM, LIVE, TABLE) separately
- Your global statistics (total spins, total zeros, average gaps between zeros)
- Your theme preference

All data is stored locally on your device. Nothing is sent to any server. Your data is completely private.

If you ever want to start completely fresh, use the "Clear Saved App State" button in the session controls. This erases everything and reloads the app as if it were brand new. Be careful — this cannot be undone.

---

## 22. Undo and Rollback

Mistakes happen. Maybe you tapped 14 when the ball actually landed on 41, or you accidentally submitted a spin before the wheel stopped. The undo feature has you covered.

**Undo Last Spin** — Tap this button in the session controls (or the "Undo" button on the number pad) to reverse the most recent spin. The app will:
- Remove the spin from your session history
- Restore your balance to what it was before that spin
- Reverse any zero gap tracking adjustments
- Reverse any global statistics updates
- Remove the number from the "Last 36 Numbers" display

You can only undo the single most recent spin. If you need to undo multiple spins, you would need to undo them one at a time, entering and undoing each one.

---

*[End of Main Manual — Index follows]*

---

## Index

| Topic | Section |
|-------|---------|
| Active Stake Bar | 10, 11 |
| Audio Feedback | 20 |
| Auto Increment | 13, 17 |
| Background Themes | 3, 12 |
| Bankroll, Starting | 3 |
| Bankroll, Editing Mid-Session | 14, 16 |
| Bet on 0 | 6 |
| Bet on 00 | 6 |
| Bet on 0/00 Split | 6 |
| Clear Saved App State | 14, 21 |
| Color Streak | 10 |
| Column Streak | 10 |
| Crisis Protection (40% Loss) | 8 |
| CSV Export | 14, 15 |
| Dark Theme | 12 |
| Double-Tap (GA Hotline) | 1 |
| Dozen Streak | 10 |
| Edit Bankroll/Unit | 14, 16 |
| Edit Sit-Out | 9, 16 |
| Edit Zero Bets | 6, 16 |
| European Table | 3, 6 |
| Export CSV | 14, 15 |
| Flashing Border (Green) | 8 |
| Flashing Border (Red) | 8 |
| Gamblers Anonymous Hotline | 1 |
| Ghost Hits | 9 |
| Glossary | Glossary |
| Historical Average | 9 |
| Historical P/L | 8, 15 |
| Home Screen Installation | 19 |
| Leave The Casino | 14, 15 |
| LIVE Mode | 3, 18 |
| Loss Alerts | 8 |
| Mode Badge | 4 |
| Mode Selection | 3, 18 |
| Number Pad | 5 |
| Outcome Breakdown | 10, 11 |
| Parity Streak | 10 |
| Place Side Bet | 11, 14 |
| Place Spin | 5 |
| Progressive Web App (PWA) | 19 |
| Quick Start | Quick Start |
| Raise or Hold | 13, 17 |
| Random Spin | 5 |
| Reset Historical P/L | 14 |
| Reset Session | 14 |
| Session Controls | 14 |
| Session History | 7 |
| Session Report | 15 |
| Session Setup | 3 |
| Session Summary | 8 |
| Settings | 13 |
| Side Bets (Automatic Alert) | 10 |
| Side Bets (Manual) | 11 |
| SIM Mode | 3, 18 |
| Sit-Out (Automatic Suggestion) | 9 |
| Sit-Out (Manual) | 9, 14 |
| Sitting Out State | 9 |
| Splash Screen | 1 |
| Spin Counter | 4, 13 |
| Spin Input | 5 |
| State Persistence | 21 |
| Sticky Header | 4 |
| Streak Detection | 10 |
| TABLE Mode | 3, 18 |
| Themes | 12 |
| Undo Last Spin | 5, 14, 22 |
| Unit per Zero | 3 |
| Win Alerts | 8 |
| Zero Bet Editor | 6 |
| Zero Bets | 6 |
