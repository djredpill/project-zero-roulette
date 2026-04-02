"""
Capture screenshots of Project Zero Roulette at iPhone and iPad viewport sizes.
Activates every feature and captures the state for the user manual.
"""
import asyncio
from playwright.async_api import async_playwright
import os, time

BASE_URL = "http://localhost:8080"
OUT = "/home/ubuntu/project-zero-roulette/manual/screenshots"
os.makedirs(OUT, exist_ok=True)

# iPhone 14 Pro portrait
IPHONE = {"width": 393, "height": 852, "device_scale_factor": 3}
# iPad Pro 10.5 landscape
IPAD_LAND = {"width": 1112, "height": 834, "device_scale_factor": 2}
# iPad Pro 10.5 portrait (for modals)
IPAD_PORT = {"width": 834, "height": 1112, "device_scale_factor": 2}

async def screenshot(page, name, full_page=True):
    path = os.path.join(OUT, f"{name}.png")
    await page.screenshot(path=path, full_page=full_page)
    print(f"  Saved: {name}.png")

async def dismiss_splash(page):
    """Click the splash screen to dismiss it"""
    await page.click("#splash-overlay")
    await page.wait_for_timeout(2000)  # wait for fade animation

async def clear_state(page):
    """Clear localStorage and reload"""
    await page.evaluate("localStorage.clear()")
    await page.reload()
    await page.wait_for_timeout(1000)

async def capture_iphone(browser):
    print("\n=== CAPTURING iPHONE SCREENSHOTS (Portrait 393x852) ===\n")
    context = await browser.new_context(viewport={"width": IPHONE["width"], "height": IPHONE["height"]}, device_scale_factor=IPHONE["device_scale_factor"])
    page = await context.new_page()
    await page.goto(BASE_URL)
    await page.wait_for_timeout(1500)

    # 1. Splash screen
    await screenshot(page, "iphone_01_splash", full_page=False)

    # Dismiss splash
    await dismiss_splash(page)
    await page.wait_for_timeout(500)

    # 2. Setup screen (before starting session)
    await screenshot(page, "iphone_02_setup", full_page=True)

    # 3. Start session
    await page.click("#startSession")
    await page.wait_for_timeout(500)
    await screenshot(page, "iphone_03_session_started", full_page=False)

    # 4. Number pad area
    await page.evaluate("window.scrollTo(0, 200)")
    await page.wait_for_timeout(300)
    await screenshot(page, "iphone_04_numpad_area", full_page=False)

    # 5. Enter some spins to build history - use numbers that create a color streak
    # Black numbers: 2, 4, 6, 8, 10, 11
    for num in ["2", "4", "6", "8", "10", "11"]:
        await page.evaluate(f"handleSpin('{num}')")
        await page.wait_for_timeout(200)

    # 6. Scroll to see session history
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    await page.wait_for_timeout(300)
    await screenshot(page, "iphone_05_session_history", full_page=False)

    # 7. Scroll back up to see sticky header with data
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(300)
    await screenshot(page, "iphone_06_sticky_header", full_page=False)

    # 8. The 6 black numbers should have triggered a color streak alert
    # Check if pattern dialog is visible
    is_visible = await page.is_visible("#patternDialog")
    if is_visible:
        await screenshot(page, "iphone_07_streak_alert", full_page=False)
        # Click ignore to dismiss
        await page.click("#btnIgnore")
        await page.wait_for_timeout(300)
        # Check for second alert (parity)
        is_visible2 = await page.is_visible("#patternDialog")
        if is_visible2:
            await screenshot(page, "iphone_07b_second_streak_alert", full_page=False)
            await page.click("#btnIgnore")
            await page.wait_for_timeout(300)

    # 9. Enter a zero to trigger sit-out suggestion
    await page.evaluate("handleSpin('0')")
    await page.wait_for_timeout(500)
    is_sitout = await page.is_visible("#genericModal")
    if is_sitout:
        await screenshot(page, "iphone_08_sitout_suggestion", full_page=False)
        # Accept the sit-out
        await page.click("#gmConfirm")
        await page.wait_for_timeout(500)

    # 10. Sit-out badge visible
    await page.evaluate("window.scrollTo(0, 200)")
    await page.wait_for_timeout(300)
    await screenshot(page, "iphone_09_sitting_out", full_page=False)

    # Cancel sit-out for further testing
    await page.evaluate("state.sitOut=0;refresh()")
    await page.wait_for_timeout(300)

    # 11. Open manual side bet modal
    await page.click("#manualSideBetBtn")
    await page.wait_for_timeout(500)
    await screenshot(page, "iphone_10_manual_sidebet", full_page=False)
    # Select Color type
    await page.click('.msb-type-btn[data-type="Color"]')
    await page.wait_for_timeout(300)
    # Select Red
    await page.evaluate("""
        document.querySelectorAll('.msb-val-btn').forEach(b => {
            if(b.textContent === 'Red') b.click();
        });
    """)
    await page.wait_for_timeout(300)
    await screenshot(page, "iphone_11_sidebet_configured", full_page=False)
    # Cancel
    await page.click("#msbCancel")
    await page.wait_for_timeout(300)

    # 12. Open Sit Out manually
    await page.click("#sitOutToggle")
    await page.wait_for_timeout(500)
    await screenshot(page, "iphone_12_sitout_manual", full_page=False)
    # Cancel the dialog
    await page.click("#gmCancel")
    await page.wait_for_timeout(300)

    # 13. Session controls area
    await page.evaluate("window.scrollTo(0, 150)")
    await page.wait_for_timeout(300)
    await screenshot(page, "iphone_13_session_controls", full_page=False)

    # 14. Zero edit modal
    await page.evaluate("openZeroEdit()")
    await page.wait_for_timeout(500)
    await screenshot(page, "iphone_14_zero_edit", full_page=False)
    await page.click("#zeCancel")
    await page.wait_for_timeout(300)

    # 15. Add more spins to trigger win/loss alerts
    # Simulate a big loss by setting balance low
    await page.evaluate("state.balance=900;state.lastAlertLevel=null;refresh();checkAlerts()")
    await page.wait_for_timeout(1000)
    await screenshot(page, "iphone_15_loss_alert", full_page=False)

    # 16. Trigger crisis modal (40% loss)
    await page.evaluate("state.balance=800;state.lastAlertLevel=null;refresh();checkAlerts()")
    await page.wait_for_timeout(1500)
    is_crisis = await page.is_visible("#crisisModal")
    if is_crisis:
        await screenshot(page, "iphone_16_crisis_modal", full_page=False)
        await page.click("#btnCrisisContinue")
        await page.wait_for_timeout(300)

    # Reset balance for more screenshots
    await page.evaluate("state.balance=1800;state.lastAlertLevel=null;refresh();checkAlerts()")
    await page.wait_for_timeout(1000)

    # 17. Win alert state
    await screenshot(page, "iphone_17_win_alert", full_page=False)

    # Reset balance
    await page.evaluate("state.balance=1500;state.lastAlertLevel=null;refresh()")
    await page.wait_for_timeout(300)

    # 18. Raise/Hold modal
    await page.evaluate("showRaiseHold()")
    await page.wait_for_timeout(500)
    await screenshot(page, "iphone_18_raise_hold", full_page=False)
    await page.click("#btnHold")
    await page.wait_for_timeout(300)

    # 19. Edit Bankroll/Unit
    await page.click("#editMidSession")
    await page.wait_for_timeout(500)
    await screenshot(page, "iphone_19_edit_bankroll", full_page=False)
    await page.click("#gmCancel")
    await page.wait_for_timeout(300)

    # 20. Leave Casino report
    await page.evaluate("_showLeaveReportInner()")
    await page.wait_for_timeout(500)
    await screenshot(page, "iphone_20_leave_report", full_page=False)
    await page.click("#leaveCancel")
    await page.wait_for_timeout(300)

    # 21. Session summary sidebar (scroll to right sidebar on mobile)
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    await page.wait_for_timeout(300)
    await screenshot(page, "iphone_21_session_summary", full_page=False)

    # 22. Settings area
    await screenshot(page, "iphone_22_settings", full_page=False)

    # 23. Theme - Dark mode
    await page.evaluate("state.theme='dark';refresh()")
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(500)
    await screenshot(page, "iphone_23_dark_theme", full_page=False)

    # 24. Theme - Green
    await page.evaluate("state.theme='green';refresh()")
    await page.wait_for_timeout(300)
    await screenshot(page, "iphone_24_green_theme", full_page=False)

    # Reset to white
    await page.evaluate("state.theme='white';refresh()")
    await page.wait_for_timeout(300)

    # 25. Full page overview
    await screenshot(page, "iphone_25_full_page", full_page=True)

    # 26. Active stake bar with side bet
    await page.evaluate("""
        state.activeSides = [{type:'Color',value:'red',amt:71,remove:false},{type:'Parity',value:'even',amt:50,remove:false}];
        refresh();
    """)
    await page.evaluate("window.scrollTo(0, 350)")
    await page.wait_for_timeout(300)
    await screenshot(page, "iphone_26_active_stakes", full_page=False)

    # Clear active stakes
    await page.evaluate("state.activeSides=[];refresh()")
    await page.wait_for_timeout(300)

    await context.close()
    print("\niPhone screenshots complete!")

async def capture_ipad(browser):
    print("\n=== CAPTURING iPAD SCREENSHOTS (Landscape 1112x834) ===\n")
    context = await browser.new_context(viewport={"width": IPAD_LAND["width"], "height": IPAD_LAND["height"]}, device_scale_factor=IPAD_LAND["device_scale_factor"])
    page = await context.new_page()
    await page.goto(BASE_URL)
    await page.wait_for_timeout(1500)

    # 1. Splash screen
    await screenshot(page, "ipad_01_splash", full_page=False)

    # Dismiss splash
    await dismiss_splash(page)
    await page.wait_for_timeout(500)

    # 2. Setup screen
    await screenshot(page, "ipad_02_setup", full_page=False)

    # 3. Start session
    await page.click("#startSession")
    await page.wait_for_timeout(500)
    await screenshot(page, "ipad_03_session_started", full_page=False)

    # 4. Enter spins to build history (black streak: 2,4,6,8,10,11)
    for num in ["2", "4", "6", "8", "10", "11"]:
        await page.evaluate(f"handleSpin('{num}')")
        await page.wait_for_timeout(200)

    # Check for streak alert
    is_visible = await page.is_visible("#patternDialog")
    if is_visible:
        await screenshot(page, "ipad_04_streak_alert", full_page=False)
        # Accept the bet
        await page.click("#btnKeepZeros")
        await page.wait_for_timeout(300)
        # Check for second alert
        is_visible2 = await page.is_visible("#patternDialog")
        if is_visible2:
            await screenshot(page, "ipad_04b_second_streak", full_page=False)
            await page.click("#btnKeepZeros")
            await page.wait_for_timeout(300)

    # 5. Active stake bar with bets
    await screenshot(page, "ipad_05_active_stakes", full_page=False)

    # 6. Enter a number to settle the side bets
    await page.evaluate("handleSpin('14')")  # 14 is red, even
    await page.wait_for_timeout(500)

    # Check for sit-out suggestion (if 0 was hit)
    # 7. Session history with side bet results
    await page.evaluate("window.scrollTo(0, 300)")
    await page.wait_for_timeout(300)
    await screenshot(page, "ipad_06_history_with_sides", full_page=False)

    # 8. Enter a zero
    await page.evaluate("handleSpin('0')")
    await page.wait_for_timeout(500)
    is_sitout = await page.is_visible("#genericModal")
    if is_sitout:
        await screenshot(page, "ipad_07_sitout_suggestion", full_page=False)
        await page.click("#gmConfirm")
        await page.wait_for_timeout(500)

    # 9. Sitting out state
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(300)
    await screenshot(page, "ipad_08_sitting_out", full_page=False)

    # Cancel sit-out
    await page.evaluate("state.sitOut=0;refresh()")
    await page.wait_for_timeout(300)

    # 10. Manual side bet modal
    await page.click("#manualSideBetBtn")
    await page.wait_for_timeout(500)
    await screenshot(page, "ipad_09_manual_sidebet", full_page=False)
    await page.click("#msbCancel")
    await page.wait_for_timeout(300)

    # 11. Zero edit modal
    await page.evaluate("openZeroEdit()")
    await page.wait_for_timeout(500)
    await screenshot(page, "ipad_10_zero_edit", full_page=False)
    await page.click("#zeCancel")
    await page.wait_for_timeout(300)

    # 12. Crisis modal
    await page.evaluate("state.balance=800;state.lastAlertLevel=null;refresh();checkAlerts()")
    await page.wait_for_timeout(1500)
    is_crisis = await page.is_visible("#crisisModal")
    if is_crisis:
        await screenshot(page, "ipad_11_crisis_modal", full_page=False)
        await page.click("#btnCrisisContinue")
        await page.wait_for_timeout(300)

    # 13. Win state
    await page.evaluate("state.balance=1800;state.lastAlertLevel=null;refresh();checkAlerts()")
    await page.wait_for_timeout(1000)
    await screenshot(page, "ipad_12_win_state", full_page=False)

    # Reset
    await page.evaluate("state.balance=1500;state.lastAlertLevel=null;refresh()")
    await page.wait_for_timeout(300)

    # 14. Raise/Hold modal
    await page.evaluate("showRaiseHold()")
    await page.wait_for_timeout(500)
    await screenshot(page, "ipad_13_raise_hold", full_page=False)
    await page.click("#btnHold")
    await page.wait_for_timeout(300)

    # 15. Leave Casino report
    await page.evaluate("_showLeaveReportInner()")
    await page.wait_for_timeout(500)
    await screenshot(page, "ipad_14_leave_report", full_page=False)
    await page.click("#leaveCancel")
    await page.wait_for_timeout(300)

    # 16. Dark theme
    await page.evaluate("state.theme='dark';refresh()")
    await page.wait_for_timeout(500)
    await screenshot(page, "ipad_15_dark_theme", full_page=False)

    # 17. Turquoise theme
    await page.evaluate("state.theme='turquoise';refresh()")
    await page.wait_for_timeout(300)
    await screenshot(page, "ipad_16_turquoise_theme", full_page=False)

    # Reset to white
    await page.evaluate("state.theme='white';refresh()")
    await page.wait_for_timeout(300)

    # 18. Full page overview
    await screenshot(page, "ipad_17_full_page", full_page=True)

    # Now switch to portrait for modals that might get cut off
    await context.close()

    print("\n=== CAPTURING iPAD PORTRAIT SCREENSHOTS (for modals) ===\n")
    context2 = await browser.new_context(viewport={"width": IPAD_PORT["width"], "height": IPAD_PORT["height"]}, device_scale_factor=IPAD_PORT["device_scale_factor"])
    page2 = await context2.new_page()
    await page2.goto(BASE_URL)
    await page2.wait_for_timeout(1500)
    await dismiss_splash(page2)
    await page2.wait_for_timeout(500)
    await page2.click("#startSession")
    await page2.wait_for_timeout(500)

    # Enter spins for streak
    for num in ["2", "4", "6", "8", "10", "11"]:
        await page2.evaluate(f"handleSpin('{num}')")
        await page2.wait_for_timeout(200)

    # Streak alert in portrait
    is_visible = await page2.is_visible("#patternDialog")
    if is_visible:
        await screenshot(page2, "ipad_port_streak_alert", full_page=False)
        await page2.click("#btnIgnore")
        await page2.wait_for_timeout(300)
        is_visible2 = await page2.is_visible("#patternDialog")
        if is_visible2:
            await page2.click("#btnIgnore")
            await page2.wait_for_timeout(300)

    # Manual side bet in portrait
    await page2.click("#manualSideBetBtn")
    await page2.wait_for_timeout(500)
    # Select Color > Red and configure
    await page2.click('.msb-type-btn[data-type="Color"]')
    await page2.wait_for_timeout(300)
    await page2.evaluate("""
        document.querySelectorAll('.msb-val-btn').forEach(b => {
            if(b.textContent === 'Red') b.click();
        });
    """)
    await page2.wait_for_timeout(300)
    await screenshot(page2, "ipad_port_sidebet_configured", full_page=False)
    await page2.click("#msbCancel")
    await page2.wait_for_timeout(300)

    # Leave report in portrait
    await page2.evaluate("_showLeaveReportInner()")
    await page2.wait_for_timeout(500)
    await screenshot(page2, "ipad_port_leave_report", full_page=False)
    await page2.click("#leaveCancel")
    await page2.wait_for_timeout(300)

    await context2.close()
    print("\niPad screenshots complete!")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        await capture_iphone(browser)
        await capture_ipad(browser)
        await browser.close()
    print(f"\nAll screenshots saved to {OUT}")
    print(f"Total files: {len(os.listdir(OUT))}")

asyncio.run(main())
