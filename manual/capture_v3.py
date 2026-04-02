"""
Capture screenshots v3 - all modal calls are non-blocking
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

SHOW_GM = """(function(title,msg,showInput,inputVal){
    var m=document.getElementById('genericModal');
    document.getElementById('gmTitle').textContent=title;
    document.getElementById('gmMessage').textContent=msg;
    var inp=document.getElementById('gmInput');
    inp.style.display=showInput?'block':'none';
    if(showInput)inp.value=inputVal||'';
    document.getElementById('gmConfirm').textContent='Yes';
    document.getElementById('gmCancel').textContent='Cancel';
    m.style.display='flex';
})"""

async def run_device(browser, prefix, vw, vh, scale):
    print(f"\n=== {prefix.upper()} ({vw}x{vh}) ===\n")
    ctx = await browser.new_context(viewport={"width": vw, "height": vh}, device_scale_factor=scale)
    page = await ctx.new_page()
    await page.goto(BASE_URL, wait_until="networkidle")
    await page.wait_for_timeout(500)

    # 1. Splash
    await ss(page, f"{prefix}_01_splash", full_page=False)

    # Hide splash without clicking
    await page.evaluate("""
        var s=document.getElementById('splash-overlay');
        if(s){s.style.opacity='0';s.style.pointerEvents='none';s.style.display='none';}
    """)
    await page.wait_for_timeout(300)

    # 2. Setup
    await ss(page, f"{prefix}_02_setup", full_page=False)

    # 3. Start session
    await page.evaluate("doResetSession(true)")
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_03_session_started", full_page=False)

    # 4. Numpad
    if vw < 500:
        await page.evaluate("window.scrollTo(0,200)")
        await page.wait_for_timeout(200)
    await ss(page, f"{prefix}_04_numpad", full_page=False)

    # 5. Enter 6 black numbers for streak
    for n in ["2","4","6","8","10","11"]:
        await page.evaluate(f"handleSpin('{n}')")
        await page.wait_for_timeout(100)
    await page.wait_for_timeout(300)

    # 6. Streak alert
    d = await page.evaluate("document.getElementById('patternDialog').style.display")
    if d == 'flex':
        await ss(page, f"{prefix}_05_streak_color", full_page=False)
        await page.evaluate("document.getElementById('btnKeepZeros').click()")
        await page.wait_for_timeout(500)
        d2 = await page.evaluate("document.getElementById('patternDialog').style.display")
        if d2 == 'flex':
            await ss(page, f"{prefix}_06_streak_parity", full_page=False)
            await page.evaluate("document.getElementById('btnKeepZeros').click()")
            await page.wait_for_timeout(300)

    # 7. Active stakes
    await page.evaluate("window.scrollTo(0,0)")
    await page.wait_for_timeout(200)
    await ss(page, f"{prefix}_07_active_stakes", full_page=False)

    # 8. Settle side bets
    await page.evaluate("handleSpin('14')")
    await page.wait_for_timeout(500)
    await hide_modals(page)
    await page.evaluate("state.sitOut=0;refresh()")
    await page.wait_for_timeout(300)

    # 9. History with side bets
    await page.evaluate("window.scrollTo(0,document.body.scrollHeight)")
    await page.wait_for_timeout(300)
    await ss(page, f"{prefix}_08_history", full_page=False)

    # 10. Zero hit sit-out suggestion
    await page.evaluate("handleSpin('0')")
    await page.wait_for_timeout(500)
    gm = await page.evaluate("document.getElementById('genericModal').style.display")
    if gm == 'flex':
        await ss(page, f"{prefix}_09_sitout_auto", full_page=False)
        await page.evaluate("document.getElementById('gmConfirm').click()")
        await page.wait_for_timeout(500)

    # 11. Sitting out
    await page.evaluate("window.scrollTo(0,0)")
    await page.wait_for_timeout(200)
    await ss(page, f"{prefix}_10_sitting_out", full_page=False)
    await page.evaluate("state.sitOut=0;refresh()")
    await page.wait_for_timeout(200)

    # 12. Manual side bet
    await page.evaluate("openManualSideBet()")
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_11_sidebet_open", full_page=False)
    await page.evaluate("msbSelectType('Color')")
    await page.wait_for_timeout(300)
    await page.evaluate("document.querySelectorAll('.msb-val-btn').forEach(function(b){if(b.textContent==='Red')b.click()})")
    await page.wait_for_timeout(300)
    await ss(page, f"{prefix}_12_sidebet_red", full_page=False)
    await page.evaluate("document.getElementById('manualSideBetModal').style.display='none'")
    await page.wait_for_timeout(200)

    # 13. Sit-out manual dialog (non-blocking)
    await page.evaluate(f"{SHOW_GM}('Sit Out Suggestion','Based on your historical average (24 spins between zeros), suggested sit-out: 24 spins. Use this?',false,'')")
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_13_sitout_manual", full_page=False)
    await hide_modals(page)

    # 14. Zero edit
    await page.evaluate("openZeroEdit()")
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_14_zero_edit", full_page=False)
    await page.evaluate("document.getElementById('zeroEditModal').style.display='none'")
    await page.wait_for_timeout(200)

    # 15. Loss alert (L:1/5)
    await page.evaluate("state.balance=1100;state.lastAlertLevel=null;refresh()")
    await page.wait_for_timeout(300)
    await page.evaluate("window.scrollTo(0,0)")
    await page.wait_for_timeout(200)
    await ss(page, f"{prefix}_15_loss_alert", full_page=False)

    # 16. Crisis modal (40% loss)
    await page.evaluate("state.balance=800;state.lastAlertLevel=null;refresh();checkAlerts()")
    await page.wait_for_timeout(1500)
    cv = await page.evaluate("document.getElementById('crisisModal').style.display")
    if cv == 'flex':
        await ss(page, f"{prefix}_16_crisis", full_page=False)
        await page.evaluate("document.getElementById('crisisModal').style.display='none'")
        await page.wait_for_timeout(200)

    # 17. Win state
    await page.evaluate("state.balance=1900;state.lastAlertLevel=null;refresh();checkAlerts()")
    await page.wait_for_timeout(1000)
    await ss(page, f"{prefix}_17_win_state", full_page=False)
    await page.evaluate("state.balance=1500;state.lastAlertLevel=null;refresh()")
    await page.wait_for_timeout(300)

    # 18. Raise/Hold
    await page.evaluate("showRaiseHold()")
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_18_raise_hold", full_page=False)
    await hide_modals(page)

    # 19. Edit Bankroll (non-blocking)
    await page.evaluate(f"{SHOW_GM}('Edit Bankroll','Enter new Starting Bankroll (or Cancel to skip):',true,'1500')")
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_19_edit_bankroll", full_page=False)
    await hide_modals(page)

    # 20. Leave report
    await page.evaluate("_showLeaveReportInner()")
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_20_leave_report", full_page=False)
    await page.evaluate("document.getElementById('leaveModal').style.display='none'")
    await page.wait_for_timeout(200)

    # 21. Session summary / settings
    await page.evaluate("window.scrollTo(0,document.body.scrollHeight)")
    await page.wait_for_timeout(300)
    await ss(page, f"{prefix}_21_summary_settings", full_page=False)

    # 22-24. Themes
    for theme in ["dark","green","gold"]:
        await page.evaluate(f"state.theme='{theme}';refresh()")
        await page.evaluate("window.scrollTo(0,0)")
        await page.wait_for_timeout(400)
        await ss(page, f"{prefix}_theme_{theme}", full_page=False)

    await page.evaluate("state.theme='white';refresh()")
    await page.wait_for_timeout(300)

    # 25. Reset confirm (non-blocking)
    await page.evaluate(f"{SHOW_GM}('Reset Session','Reset the current session balance?',false,'')")
    await page.wait_for_timeout(500)
    await ss(page, f"{prefix}_25_reset_confirm", full_page=False)
    await hide_modals(page)

    # 26. Zero bets strip
    if vw < 500:
        await page.evaluate("window.scrollTo(0,500)")
    else:
        await page.evaluate("window.scrollTo(0,400)")
    await page.wait_for_timeout(200)
    await ss(page, f"{prefix}_26_zero_bets", full_page=False)

    # 27. Full page
    await page.evaluate("window.scrollTo(0,0)")
    await page.wait_for_timeout(200)
    await ss(page, f"{prefix}_27_full_page", full_page=True)

    await ctx.close()
    print(f"\n{prefix} complete!")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        await run_device(browser, "iphone", 393, 852, 3)
        await run_device(browser, "ipad_land", 1112, 834, 2)
        await run_device(browser, "ipad_port", 834, 1112, 2)
        await browser.close()

    files = sorted(os.listdir(OUT))
    print(f"\nTotal screenshots: {len(files)}")
    for f in files:
        sz = os.path.getsize(os.path.join(OUT, f))
        print(f"  {f} ({sz//1024}KB)")

asyncio.run(main())
