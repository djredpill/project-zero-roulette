"""
Capture remaining screenshots - fix modal issues by using evaluate to dismiss modals
"""
import asyncio
from playwright.async_api import async_playwright
import os

BASE_URL = "http://localhost:8080"
OUT = "/home/ubuntu/project-zero-roulette/manual/screenshots"

async def screenshot(page, name, full_page=True):
    path = os.path.join(OUT, f"{name}.png")
    await page.screenshot(path=path, full_page=full_page)
    print(f"  Saved: {name}.png")

async def dismiss_all_modals(page):
    """Force dismiss all modals via JS"""
    await page.evaluate("""
        document.querySelectorAll('.modal-overlay').forEach(m => m.style.display='none');
    """)
    await page.wait_for_timeout(200)

async def capture_remaining_iphone(browser):
    print("\n=== REMAINING iPHONE SCREENSHOTS ===\n")
    ctx = await browser.new_context(viewport={"width": 393, "height": 852}, device_scale_factor=3)
    page = await ctx.new_page()
    await page.goto(BASE_URL)
    await page.wait_for_timeout(1500)
    # Dismiss splash
    await page.click("#splash-overlay")
    await page.wait_for_timeout(2000)
    # Start session
    await page.click("#startSession")
    await page.wait_for_timeout(500)
    # Add some spins for history
    for num in ["2", "4", "6", "8", "10", "11", "14", "21", "0"]:
        await page.evaluate(f"handleSpin('{num}')")
        await page.wait_for_timeout(100)
    await dismiss_all_modals(page)
    await page.evaluate("state.sitOut=0;refresh()")
    await page.wait_for_timeout(300)

    # 19. Edit Bankroll - use evaluate to trigger the prompt
    await page.evaluate("""
        document.getElementById('genericModal').style.display='none';
    """)
    await page.wait_for_timeout(200)
    # Trigger edit and screenshot the prompt
    await page.evaluate("""
        appPrompt('Edit Bankroll','Enter new Starting Bankroll (or Cancel to skip):',String(state.bank));
    """)
    await page.wait_for_timeout(500)
    await screenshot(page, "iphone_19_edit_bankroll", full_page=False)
    await dismiss_all_modals(page)
    await page.wait_for_timeout(300)

    # 20. Leave Casino report
    await page.evaluate("_showLeaveReportInner()")
    await page.wait_for_timeout(500)
    await screenshot(page, "iphone_20_leave_report", full_page=False)
    await page.click("#leaveCancel")
    await page.wait_for_timeout(300)

    # 21. Scroll to session summary
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    await page.wait_for_timeout(500)
    await screenshot(page, "iphone_21_session_summary", full_page=False)

    # 22. Settings area (should be visible at bottom)
    await screenshot(page, "iphone_22_settings", full_page=False)

    # 23. Dark theme
    await page.evaluate("state.theme='dark';refresh()")
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(500)
    await screenshot(page, "iphone_23_dark_theme", full_page=False)

    # 24. Green theme
    await page.evaluate("state.theme='green';refresh()")
    await page.wait_for_timeout(300)
    await screenshot(page, "iphone_24_green_theme", full_page=False)

    # 25. Gold theme
    await page.evaluate("state.theme='gold';refresh()")
    await page.wait_for_timeout(300)
    await screenshot(page, "iphone_25_gold_theme", full_page=False)

    # Reset to white
    await page.evaluate("state.theme='white';refresh()")
    await page.wait_for_timeout(300)

    # 26. Active stake bar with multiple bets
    await page.evaluate("""
        state.activeSides = [{type:'Color',value:'red',amt:71,remove:false},{type:'Parity',value:'even',amt:50,remove:false}];
        refresh();
    """)
    await page.evaluate("window.scrollTo(0, 350)")
    await page.wait_for_timeout(300)
    await screenshot(page, "iphone_26_active_stakes", full_page=False)
    await page.evaluate("state.activeSides=[];refresh()")
    await page.wait_for_timeout(300)

    # 27. Full page overview
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(300)
    await screenshot(page, "iphone_27_full_page", full_page=True)

    # 28. Zero bet trio strip
    await page.evaluate("window.scrollTo(0, 500)")
    await page.wait_for_timeout(300)
    await screenshot(page, "iphone_28_zero_bets", full_page=False)

    # 29. Last 36 numbers strip
    await page.evaluate("window.scrollTo(0, 350)")
    await page.wait_for_timeout(300)
    await screenshot(page, "iphone_29_last36", full_page=False)

    # 30. Reset Session confirmation
    await page.evaluate("""
        appConfirm('Reset Session','Reset the current session balance?');
    """)
    await page.wait_for_timeout(500)
    await screenshot(page, "iphone_30_reset_confirm", full_page=False)
    await dismiss_all_modals(page)

    await ctx.close()
    print("\niPhone remaining screenshots complete!")

async def capture_ipad(browser):
    print("\n=== iPAD LANDSCAPE SCREENSHOTS ===\n")
    ctx = await browser.new_context(viewport={"width": 1112, "height": 834}, device_scale_factor=2)
    page = await ctx.new_page()
    await page.goto(BASE_URL)
    await page.wait_for_timeout(1500)

    # 1. Splash
    await screenshot(page, "ipad_01_splash", full_page=False)
    await page.click("#splash-overlay")
    await page.wait_for_timeout(2000)

    # 2. Setup screen
    await screenshot(page, "ipad_02_setup", full_page=False)

    # 3. Start session
    await page.click("#startSession")
    await page.wait_for_timeout(500)
    await screenshot(page, "ipad_03_session_started", full_page=False)

    # 4. Enter streak numbers
    for num in ["2", "4", "6", "8", "10", "11"]:
        await page.evaluate(f"handleSpin('{num}')")
        await page.wait_for_timeout(200)

    # Streak alert
    is_vis = await page.is_visible("#patternDialog")
    if is_vis:
        await screenshot(page, "ipad_04_streak_alert", full_page=False)
        await page.click("#btnKeepZeros")
        await page.wait_for_timeout(300)
        is_vis2 = await page.is_visible("#patternDialog")
        if is_vis2:
            await screenshot(page, "ipad_04b_second_streak", full_page=False)
            await page.click("#btnKeepZeros")
            await page.wait_for_timeout(300)

    # 5. Active stakes
    await screenshot(page, "ipad_05_active_stakes", full_page=False)

    # 6. Settle side bets
    await page.evaluate("handleSpin('14')")
    await page.wait_for_timeout(500)
    await dismiss_all_modals(page)
    await page.evaluate("state.sitOut=0;refresh()")
    await page.wait_for_timeout(300)

    # 7. History with side bet results
    await page.evaluate("window.scrollTo(0, 300)")
    await page.wait_for_timeout(300)
    await screenshot(page, "ipad_06_history_with_sides", full_page=False)

    # 8. Enter zero for sit-out
    await page.evaluate("handleSpin('0')")
    await page.wait_for_timeout(500)
    is_sitout = await page.is_visible("#genericModal")
    if is_sitout:
        await screenshot(page, "ipad_07_sitout_suggestion", full_page=False)
        await page.click("#gmConfirm")
        await page.wait_for_timeout(500)

    # 9. Sitting out
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(300)
    await screenshot(page, "ipad_08_sitting_out", full_page=False)
    await page.evaluate("state.sitOut=0;refresh()")
    await page.wait_for_timeout(300)

    # 10. Manual side bet
    await page.click("#manualSideBetBtn")
    await page.wait_for_timeout(500)
    await page.click('.msb-type-btn[data-type="Color"]')
    await page.wait_for_timeout(300)
    await page.evaluate("""
        document.querySelectorAll('.msb-val-btn').forEach(b => {
            if(b.textContent === 'Red') b.click();
        });
    """)
    await page.wait_for_timeout(300)
    await screenshot(page, "ipad_09_manual_sidebet", full_page=False)
    await page.click("#msbCancel")
    await page.wait_for_timeout(300)

    # 11. Zero edit
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
    await page.evaluate("state.balance=1500;state.lastAlertLevel=null;refresh()")
    await page.wait_for_timeout(300)

    # 14. Raise/Hold
    await page.evaluate("showRaiseHold()")
    await page.wait_for_timeout(500)
    await screenshot(page, "ipad_13_raise_hold", full_page=False)
    await page.click("#btnHold")
    await page.wait_for_timeout(300)

    # 15. Leave report
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

    # Reset
    await page.evaluate("state.theme='white';refresh()")
    await page.wait_for_timeout(300)

    # 18. Full page
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(300)
    await screenshot(page, "ipad_17_full_page", full_page=True)

    await ctx.close()

    # iPad portrait for modals
    print("\n=== iPAD PORTRAIT SCREENSHOTS (for modals) ===\n")
    ctx2 = await browser.new_context(viewport={"width": 834, "height": 1112}, device_scale_factor=2)
    page2 = await ctx2.new_page()
    await page2.goto(BASE_URL)
    await page2.wait_for_timeout(1500)
    await page2.click("#splash-overlay")
    await page2.wait_for_timeout(2000)
    await page2.click("#startSession")
    await page2.wait_for_timeout(500)

    # Enter streak
    for num in ["2", "4", "6", "8", "10", "11"]:
        await page2.evaluate(f"handleSpin('{num}')")
        await page2.wait_for_timeout(200)

    is_vis = await page2.is_visible("#patternDialog")
    if is_vis:
        await screenshot(page2, "ipad_port_01_streak_alert", full_page=False)
        await page2.click("#btnIgnore")
        await page2.wait_for_timeout(300)
        is_vis2 = await page2.is_visible("#patternDialog")
        if is_vis2:
            await screenshot(page2, "ipad_port_02_second_streak", full_page=False)
            await page2.click("#btnIgnore")
            await page2.wait_for_timeout(300)

    # Manual side bet configured
    await page2.click("#manualSideBetBtn")
    await page2.wait_for_timeout(500)
    await page2.click('.msb-type-btn[data-type="Dozen"]')
    await page2.wait_for_timeout(500)
    await screenshot(page2, "ipad_port_03_sidebet_dozen", full_page=False)
    await page2.click("#msbCancel")
    await page2.wait_for_timeout(300)

    # Leave report in portrait
    await page2.evaluate("_showLeaveReportInner()")
    await page2.wait_for_timeout(500)
    await screenshot(page2, "ipad_port_04_leave_report", full_page=False)
    await page2.click("#leaveCancel")
    await page2.wait_for_timeout(300)

    # Crisis modal in portrait
    await page2.evaluate("state.balance=800;state.lastAlertLevel=null;refresh();checkAlerts()")
    await page2.wait_for_timeout(1500)
    is_crisis = await page2.is_visible("#crisisModal")
    if is_crisis:
        await screenshot(page2, "ipad_port_05_crisis", full_page=False)
        await page2.click("#btnCrisisContinue")
        await page2.wait_for_timeout(300)

    await page2.evaluate("state.balance=1500;state.lastAlertLevel=null;refresh()")
    await page2.wait_for_timeout(300)

    # Full page portrait
    await screenshot(page2, "ipad_port_06_full_page", full_page=True)

    await ctx2.close()
    print("\niPad screenshots complete!")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        await capture_remaining_iphone(browser)
        await capture_ipad(browser)
        await browser.close()
    files = os.listdir(OUT)
    print(f"\nTotal screenshots: {len(files)}")
    for f in sorted(files):
        print(f"  {f}")

asyncio.run(main())
