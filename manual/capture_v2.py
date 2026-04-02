"""
Capture screenshots - skip splash by hiding it via JS before interaction
"""
import asyncio
from playwright.async_api import async_playwright
import os

BASE_URL = "http://localhost:8080"
OUT = "/home/ubuntu/project-zero-roulette/manual/screenshots"
os.makedirs(OUT, exist_ok=True)

async def ss(page, name, full_page=True):
    path = os.path.join(OUT, f"{name}.png")
    await page.screenshot(path=path, full_page=full_page)
    print(f"  Saved: {name}.png")

async def hide_modals(page):
    await page.evaluate("document.querySelectorAll('.modal-overlay').forEach(m=>m.style.display='none')")
    await page.wait_for_timeout(200)

async def run_device(browser, prefix, vw, vh, scale):
    print(f"\n=== {prefix.upper()} ({vw}x{vh}) ===\n")
    ctx = await browser.new_context(viewport={"width": vw, "height": vh}, device_scale_factor=scale)
    page = await ctx.new_page()

    # Load page and immediately hide splash (avoid audio context hang)
    await page.goto(BASE_URL, wait_until="networkidle")
    await page.wait_for_timeout(500)

    # Screenshot splash first
    await ss(page, f"{prefix}_01_splash", full_page=False)

    # Hide splash without clicking (avoids audio context issue in headless)
    await page.evaluate("""
        const s = document.getElementById('splash-overlay');
        if(s) { s.style.opacity='0'; s.style.pointerEvents='none'; 
        setTimeout(()=>s.style.display='none', 100); }
    """)
    await page.wait_for_timeout(500)

    # 2. Setup screen
    await ss(page, f"{prefix}_02_setup", full_page=False)

    # 3. Start session via JS
    await page.evaluate("doResetSession(true)")
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_03_session_started", full_page=False)

    # 4. Numpad area
    if vw < 500:  # iPhone
        await page.evaluate("window.scrollTo(0, 200)")
        await page.wait_for_timeout(200)
    await ss(page, f"{prefix}_04_numpad", full_page=False)

    # 5. Enter 6 black numbers for streak: 2,4,6,8,10,11
    for n in ["2","4","6","8","10","11"]:
        await page.evaluate(f"handleSpin('{n}')")
        await page.wait_for_timeout(100)
    await page.wait_for_timeout(300)

    # 6. Streak alert (should be visible)
    is_vis = await page.evaluate("document.getElementById('patternDialog').style.display")
    if is_vis == 'flex':
        await ss(page, f"{prefix}_05_streak_alert_color", full_page=False)
        # Accept the bet
        await page.evaluate("document.getElementById('btnKeepZeros').click()")
        await page.wait_for_timeout(500)
        # Check for second alert
        is_vis2 = await page.evaluate("document.getElementById('patternDialog').style.display")
        if is_vis2 == 'flex':
            await ss(page, f"{prefix}_06_streak_alert_parity", full_page=False)
            await page.evaluate("document.getElementById('btnKeepZeros').click()")
            await page.wait_for_timeout(300)

    # 7. Active stakes bar
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(200)
    await ss(page, f"{prefix}_07_active_stakes", full_page=False)

    # 8. Settle side bets with spin 14 (red, even)
    await page.evaluate("handleSpin('14')")
    await page.wait_for_timeout(500)
    await hide_modals(page)
    await page.evaluate("state.sitOut=0;refresh()")
    await page.wait_for_timeout(300)

    # 9. History with color-coded side bets
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    await page.wait_for_timeout(300)
    await ss(page, f"{prefix}_08_history_sidebets", full_page=False)

    # 10. Enter zero for sit-out suggestion
    await page.evaluate("handleSpin('0')")
    await page.wait_for_timeout(500)
    gm_vis = await page.evaluate("document.getElementById('genericModal').style.display")
    if gm_vis == 'flex':
        await ss(page, f"{prefix}_09_sitout_suggestion", full_page=False)
        await page.evaluate("document.getElementById('gmConfirm').click()")
        await page.wait_for_timeout(500)

    # 11. Sitting out state
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(200)
    await ss(page, f"{prefix}_10_sitting_out", full_page=False)

    # Cancel sit-out
    await page.evaluate("state.sitOut=0;refresh()")
    await page.wait_for_timeout(200)

    # 12. Manual side bet modal
    await page.evaluate("openManualSideBet()")
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_11_manual_sidebet_open", full_page=False)

    # Select Color > Red
    await page.evaluate("msbSelectType('Color')")
    await page.wait_for_timeout(300)
    await page.evaluate("""
        document.querySelectorAll('.msb-val-btn').forEach(b=>{if(b.textContent==='Red')b.click()})
    """)
    await page.wait_for_timeout(300)
    await ss(page, f"{prefix}_12_sidebet_configured", full_page=False)
    await page.evaluate("document.getElementById('manualSideBetModal').style.display='none'")
    await page.wait_for_timeout(200)

    # 13. Manual sit-out dialog
    await page.evaluate("""
        appConfirm('Sit Out Suggestion','Based on your historical average (24 spins between zeros), suggested sit-out: 24 spins. Use this?')
    """)
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_13_sitout_manual", full_page=False)
    await hide_modals(page)

    # 14. Zero edit modal
    await page.evaluate("openZeroEdit()")
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_14_zero_edit", full_page=False)
    await page.evaluate("document.getElementById('zeroEditModal').style.display='none'")
    await page.wait_for_timeout(200)

    # 15. Loss alert state (set balance to trigger L:1/5)
    await page.evaluate("state.balance=1100;state.lastAlertLevel=null;refresh()")
    await page.wait_for_timeout(300)
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(200)
    await ss(page, f"{prefix}_15_loss_alert", full_page=False)

    # 16. Crisis modal (40% loss)
    await page.evaluate("state.balance=800;state.lastAlertLevel=null;refresh();checkAlerts()")
    await page.wait_for_timeout(1500)
    crisis_vis = await page.evaluate("document.getElementById('crisisModal').style.display")
    if crisis_vis == 'flex':
        await ss(page, f"{prefix}_16_crisis_modal", full_page=False)
        await page.evaluate("document.getElementById('crisisModal').style.display='none'")
        await page.wait_for_timeout(200)

    # 17. Win alert state
    await page.evaluate("state.balance=1900;state.lastAlertLevel=null;refresh();checkAlerts()")
    await page.wait_for_timeout(1000)
    await ss(page, f"{prefix}_17_win_state", full_page=False)
    await page.evaluate("state.balance=1500;state.lastAlertLevel=null;refresh()")
    await page.wait_for_timeout(300)

    # 18. Raise/Hold modal
    await page.evaluate("showRaiseHold()")
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_18_raise_hold", full_page=False)
    await hide_modals(page)

    # 19. Edit Bankroll prompt
    await page.evaluate("appPrompt('Edit Bankroll','Enter new Starting Bankroll (or Cancel to skip):',String(state.bank))")
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_19_edit_bankroll", full_page=False)
    await hide_modals(page)

    # 20. Leave Casino report
    await page.evaluate("_showLeaveReportInner()")
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_20_leave_report", full_page=False)
    await page.evaluate("document.getElementById('leaveModal').style.display='none'")
    await page.wait_for_timeout(200)

    # 21. Session summary / settings (scroll to bottom)
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    await page.wait_for_timeout(300)
    await ss(page, f"{prefix}_21_summary_settings", full_page=False)

    # 22. Dark theme
    await page.evaluate("state.theme='dark';refresh()")
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_22_dark_theme", full_page=False)

    # 23. Green theme
    await page.evaluate("state.theme='green';refresh()")
    await page.wait_for_timeout(300)
    await ss(page, f"{prefix}_23_green_theme", full_page=False)

    # 24. Gold theme
    await page.evaluate("state.theme='gold';refresh()")
    await page.wait_for_timeout(300)
    await ss(page, f"{prefix}_24_gold_theme", full_page=False)

    # Reset to white
    await page.evaluate("state.theme='white';refresh()")
    await page.wait_for_timeout(300)

    # 25. Reset session confirmation
    await page.evaluate("appConfirm('Reset Session','Reset the current session balance?')")
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_25_reset_confirm", full_page=False)
    await hide_modals(page)

    # 26. Zero bets strip area
    await page.evaluate("window.scrollTo(0, 500)")
    await page.wait_for_timeout(200)
    await ss(page, f"{prefix}_26_zero_bets", full_page=False)

    # 27. Full page overview
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(200)
    await ss(page, f"{prefix}_27_full_page", full_page=True)

    await ctx.close()
    print(f"\n{prefix} screenshots complete!")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # iPhone 14 Pro portrait
        await run_device(browser, "iphone", 393, 852, 3)
        # iPad Pro 10.5 landscape
        await run_device(browser, "ipad_land", 1112, 834, 2)
        # iPad Pro 10.5 portrait (for modals)
        await run_device(browser, "ipad_port", 834, 1112, 2)
        await browser.close()

    files = sorted(os.listdir(OUT))
    print(f"\nTotal screenshots: {len(files)}")
    for f in files:
        sz = os.path.getsize(os.path.join(OUT, f))
        print(f"  {f} ({sz//1024}KB)")

asyncio.run(main())
