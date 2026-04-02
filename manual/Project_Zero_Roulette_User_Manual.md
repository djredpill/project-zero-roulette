# Project Zero Roulette — User Manual

## Preface

Project Zero Roulette is a specialized statistical analysis and testing application designed to track, analyze, and capitalize on specific patterns in roulette. Developed through iterative testing and refinement, the application combines elements of two distinct betting systems into a unified, data-driven approach. 

The core philosophy of Project Zero Roulette is patience and precision. Rather than betting on every spin, the system tracks the history of the wheel, identifies statistical anomalies (such as prolonged streaks of a single color or parity), and alerts the user when conditions are optimal for a strategic side bet. Simultaneously, it manages a primary betting strategy focused on the zero and double-zero slots, complete with dynamic bankroll management, loss limits, and win goals.

This manual provides a comprehensive guide to every feature of the application, illustrated with screenshots from both iPhone (portrait) and iPad (landscape) to ensure you can navigate the system effectively regardless of your device.

---

## 1. Getting Started

### The Splash Screen
When you first launch the application, you are greeted by the splash screen. This screen includes important notices regarding the statistical nature of the app and responsible gaming resources.

![Splash Screen](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/iphone_01_splash.png)

Tap anywhere on the screen to enter the application.

### Session Setup
Before beginning a session, you must configure your starting parameters. The setup area is located at the top of the screen.

![Setup Screen](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/iphone_02_setup.png)

- **Starting Bankroll:** Enter your total session bankroll (default is $1,500).
- **Unit per zero:** Set your base betting unit for the zero slots (default is $5).
- **Table Type:** Choose between **American** (0 and 00) or **European** (0 only). Switching to European will automatically disable the 00 and split bets.
- **Mode:** Select your tracking mode:
  - **SIM:** For simulation and testing.
  - **LIVE:** For tracking live dealer games.
  - **TABLE:** For tracking automated or physical casino tables.

Once your parameters are set, press the **Start Session** button to lock them in and begin tracking.

---

## 2. Core Gameplay & Tracking

### The Number Pad
The primary interface for tracking spins is the number pad. It is designed for rapid input, allowing you to easily keep up with the pace of the game.

![Number Pad](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/iphone_04_numpad_area.png)

To record a spin, simply tap the corresponding number on the pad. The application features **auto-submit**, meaning the spin is recorded instantly upon tapping the number—no additional confirmation button is required.

If you make a mistake, tap the **Undo** button (yellow) to remove the last recorded spin.

### Session History & Last 36 Numbers
As you record spins, the application maintains a detailed history.

![Session History](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/iphone_05_session_history.png)

- **Last 36 Numbers:** A horizontal strip displays the most recent 36 numbers, color-coded for quick reference.
- **Session History Table:** A comprehensive log of every spin, showing the time, mode, your stake on the zeros, any active side bets, the net profit/loss for that spin, and your running balance.

---

## 3. Streak Alerts & Side Bets

One of the most powerful features of Project Zero Roulette is its automated pattern recognition. The application constantly monitors the spin history for prolonged streaks (e.g., 6+ consecutive black numbers, or 6+ consecutive odd numbers).

### Automated Streak Alerts
When a streak threshold is reached, the application will automatically pause and present a streak alert.

![Streak Alert](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/iphone_05_streak_color.png)

The alert provides:
- A description of the streak (e.g., "The last 6 numbers were all black").
- A strategic suggestion (e.g., "Suggestion: Bet on RED").
- Quick-select buttons to size your side bet based on a percentage of your current bankroll (5%, 10%, 15%), or a custom amount.
- A detailed **Outcome Breakdown** showing exactly how the side bet will impact your balance under various scenarios (winning the side bet, hitting a zero, losing both, etc.).

You have three choices:
1. **Bet + Keep Zeros:** Place the side bet while maintaining your primary bets on the zeros.
2. **Bet + Remove Zeros:** Place the side bet but temporarily suspend your bets on the zeros for this spin.
3. **Ignore:** Decline the side bet and continue tracking.

### Multiple Simultaneous Streaks
If multiple streak conditions are met simultaneously (e.g., 6 numbers that are all black *and* all odd), the application will present the alerts sequentially. After you act on the first alert, the second alert will immediately appear.

### Active Stakes Display
When you accept one or more side bets, they are displayed in the **Active Stake** bar just below the Last 36 Numbers strip.

![Active Stakes](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/iphone_07_active_stakes.png)

If you have multiple side bets active, they will stack in this display. In the session history table, side bets are recorded using a compact, color-coded format (e.g., <span style="color:green">R/$71</span> for a winning Red bet, <span style="color:red">E/$50</span> for a losing Even bet).

### Manual Side Bets
You do not have to wait for an automated alert to place a side bet. You can manually configure a side bet at any time.

![Manual Side Bet](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/iphone_11_sidebet_open.png)

1. Tap the **Place Side Bet** button in the Session Controls area.
2. Select the category (Color, Parity, High/Low, Dozen, or Column).
3. Select the specific outcome (e.g., Red, Even, 1st 12).
4. Set your stake amount.
5. Choose whether to keep or remove your zero bets.

---

## 4. Bankroll Management & Alerts

Project Zero Roulette includes robust tools to protect your bankroll and lock in profits.

### Loss Alerts & Crisis Mode
The application tracks your session profit/loss against your starting bankroll. If your balance drops significantly, you will receive automated warnings.

![Loss Alert](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/iphone_15_loss_alert.png)

The **Loss / Win Alerts** panel provides a visual indicator of your current standing. If your balance drops by 40% of your starting bankroll, the application triggers **Crisis Mode**.

![Crisis Modal](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/ipad_land_16_crisis.png)

The Crisis Modal forces you to acknowledge the drawdown and make a conscious decision:
- **Continue Playing:** Acknowledge the risk and proceed.
- **Reset Session:** Clear the current session and start fresh.
- **Quit:** End the session entirely.

### Win Alerts & Raise/Hold
Conversely, when you achieve significant profit milestones, the application will alert you.

![Win State](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/iphone_17_win_state.png)

When you hit a major win threshold, the **Raise/Hold** modal will appear.

![Raise/Hold](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/iphone_18_raise_hold.png)

This feature encourages disciplined profit-taking. You can choose to:
- **Hold:** Keep your betting units the same and protect your profits.
- **Raise:** Increase your base unit size to capitalize on the winning streak.

---

## 5. Sit-Out Mechanics

Sitting out spins is a core component of the Project Zero strategy, allowing you to conserve your bankroll during unfavorable wheel conditions.

### Automated Sit-Out Suggestions
The application tracks the historical average number of spins between zero hits across all your sessions. When a 0 or 00 hits, the application will automatically suggest that you sit out for a number of spins based on this historical average.

![Auto Sit-Out](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/iphone_09_sitout_auto.png)

If you decline the automated suggestion, a secondary prompt allows you to enter a custom number of spins to sit out.

### Manual Sit-Out
You can also initiate a sit-out period manually at any time by pressing the **Sit Out Spins** button in the Session Controls area.

![Manual Sit-Out](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/iphone_13_sitout_manual.png)

### Sitting Out State
While sitting out, the application interface updates to clearly indicate your status.

![Sitting Out](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/iphone_10_sitting_out.png)

The spin input buttons turn gray, and a prominent "Sitting Out" banner displays the number of spins remaining in your sit-out period. You continue to record spins as they occur on the wheel, but no virtual bets are placed, and your balance remains unchanged. You can cancel a sit-out period early by tapping the "Cancel Sit-Out" button.

---

## 6. Session Controls & Reporting

### Mid-Session Adjustments
You can adjust your parameters mid-session without losing your history.

- **Edit Bankroll/Unit:** Tap this button to update your starting bankroll or base unit size.
- **Zero Bet Strip:** Tap any of the zero bet boxes (0, 0/00 split, 00) to manually override the bet amount for that specific slot.

![Zero Bets](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/iphone_26_zero_bets.png)

### Ending a Session
When you are ready to conclude your play, tap **Leave The Casino**.

![Leave Report](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/ipad_land_20_leave_report.png)

This generates a comprehensive **Session Report** detailing:
- Starting and ending balances.
- Session and historical profit/loss.
- Total spins and estimated duration.
- Average spins between zeros (session and historical).
- Sit-out statistics.

You have the option to enter an email address to send this report to yourself, or export the data as a CSV file for further analysis.

### Application Reset
To completely clear all data, including historical averages and saved state, use the **Clear Saved App State** button. This will return the application to its factory default settings.

---

## 7. Customization

Project Zero Roulette includes several visual themes to suit your preference or the lighting conditions of your environment.

You can change the theme using the **Background** dropdown in the setup area. Available options include:
- **White** (Default)
- **Dark**
- **Green**
- **Gold**
- **Turquoise**

![Themes](/home/ubuntu/project-zero-roulette/manual/screenshots_cropped/iphone_theme_dark.png)

*Example: Dark Theme*
