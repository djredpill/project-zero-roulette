#!/usr/bin/env python3
"""
Smart crop screenshots for the user manual.
- Splash screens: crop black bars
- Modal/dialog screenshots: crop gray overlay to show just the modal with some context
- Full page views: keep as-is (just trim any pure black/white bars at edges)
"""
from PIL import Image
import os

SCREENSHOTS_DIR = "/home/ubuntu/project-zero-roulette/manual/screenshots"
CROPPED_DIR = "/home/ubuntu/project-zero-roulette/manual/screenshots_cropped"
os.makedirs(CROPPED_DIR, exist_ok=True)

# Screenshots that are modals/dialogs overlaying the app - crop to modal content area
MODAL_SCREENSHOTS = [
    'streak_color', 'streak_parity', 'streak_alert',
    'sitout_auto', 'sitout_manual', 'sitout_suggestion',
    'sidebet_open', 'sidebet_red', 'sidebet_configured',
    'manual_sidebet_open', 'manual_sidebet',
    'zero_edit', 'crisis', 'crisis_modal',
    'raise_hold', 'edit_bankroll',
    'leave_report', 'reset_confirm'
]

# Splash screens - crop black bars
SPLASH_SCREENSHOTS = ['01_splash']

def is_near_color(pixel, target, threshold=30):
    """Check if pixel is near a target color."""
    if isinstance(pixel, int):
        p = (pixel, pixel, pixel)
    else:
        p = pixel[:3]
    return all(abs(p[i] - target[i]) < threshold for i in range(3))

def crop_black_bars(img, padding=10):
    """Crop black bars from splash screens."""
    pixels = img.load()
    w, h = img.size
    
    top = 0
    for y in range(h):
        has_content = False
        for x in range(0, w, 5):
            if not is_near_color(pixels[x, y], (0, 0, 0), 20):
                has_content = True
                break
        if has_content:
            top = y
            break
    
    bottom = h - 1
    for y in range(h-1, -1, -1):
        has_content = False
        for x in range(0, w, 5):
            if not is_near_color(pixels[x, y], (0, 0, 0), 20):
                has_content = True
                break
        if has_content:
            bottom = y
            break
    
    top = max(0, top - padding)
    bottom = min(h, bottom + padding)
    
    if (h - (bottom - top)) / h > 0.05:
        return img.crop((0, top, w, bottom))
    return img

def crop_modal(img, padding=20):
    """Crop to show the modal dialog with a bit of context."""
    pixels = img.load()
    w, h = img.size
    
    # Modals have a gray overlay (around 128,128,128 with some alpha)
    # and the modal itself is white. Find the white modal box.
    # Strategy: find rows/cols that have significant white content (the modal)
    
    # Look for the modal border (often has a colored border or shadow)
    # The modal content is typically white (#fff) surrounded by gray overlay
    
    # Find top of modal: first row with significant white pixels
    modal_top = 0
    for y in range(h):
        white_count = 0
        for x in range(0, w, 3):
            if is_near_color(pixels[x, y], (255, 255, 255), 30):
                white_count += 1
        if white_count > w // 20:  # at least 5% of row is white
            modal_top = y
            break
    
    # Find bottom of modal
    modal_bottom = h - 1
    for y in range(h-1, -1, -1):
        white_count = 0
        for x in range(0, w, 3):
            if is_near_color(pixels[x, y], (255, 255, 255), 30):
                white_count += 1
        if white_count > w // 20:
            modal_bottom = y
            break
    
    # Find left of modal
    modal_left = 0
    for x in range(w):
        white_count = 0
        for y in range(modal_top, modal_bottom + 1, 3):
            if is_near_color(pixels[x, y], (255, 255, 255), 30):
                white_count += 1
        if white_count > (modal_bottom - modal_top) // 20:
            modal_left = x
            break
    
    # Find right of modal
    modal_right = w - 1
    for x in range(w-1, -1, -1):
        white_count = 0
        for y in range(modal_top, modal_bottom + 1, 3):
            if is_near_color(pixels[x, y], (255, 255, 255), 30):
                white_count += 1
        if white_count > (modal_bottom - modal_top) // 20:
            modal_right = x
            break
    
    # Add padding and include the header bar at top for context
    # Include from the very top of the page (header) to just below the modal
    top = 0  # Keep the header
    bottom = min(h, modal_bottom + padding * 2)
    left = max(0, modal_left - padding * 2)
    right = min(w, modal_right + padding * 2)
    
    # Sanity check - modal should be at least 20% of the image
    modal_area = (modal_right - modal_left) * (modal_bottom - modal_top)
    img_area = w * h
    if modal_area < img_area * 0.05:
        # Couldn't find modal reliably, return original
        return img
    
    return img.crop((left, top, right, bottom))

def trim_edges(img, padding=5):
    """Just trim any pure black/white bars at the very edges."""
    pixels = img.load()
    w, h = img.size
    
    # Check bottom for pure white/black bars
    bottom = h - 1
    for y in range(h-1, h//2, -1):
        row_uniform = True
        first_pixel = pixels[0, y][:3] if not isinstance(pixels[0, y], int) else (pixels[0, y],)*3
        if not (is_near_color(first_pixel, (255, 255, 255), 10) or is_near_color(first_pixel, (0, 0, 0), 10)):
            break
        for x in range(0, w, 10):
            p = pixels[x, y][:3] if not isinstance(pixels[x, y], int) else (pixels[x, y],)*3
            if not is_near_color(p, first_pixel, 10):
                row_uniform = False
                break
        if not row_uniform:
            bottom = y
            break
    
    if bottom < h - 10:
        return img.crop((0, 0, w, bottom + padding))
    return img

def get_screenshot_type(fname):
    """Determine what type of screenshot this is."""
    name_lower = fname.lower()
    
    for splash_key in SPLASH_SCREENSHOTS:
        if splash_key in name_lower:
            return 'splash'
    
    for modal_key in MODAL_SCREENSHOTS:
        if modal_key in name_lower:
            return 'modal'
    
    return 'fullpage'

count = 0
for fname in sorted(os.listdir(SCREENSHOTS_DIR)):
    if not fname.endswith('.png'):
        continue
    
    fpath = os.path.join(SCREENSHOTS_DIR, fname)
    img = Image.open(fpath)
    w, h = img.size
    stype = get_screenshot_type(fname)
    
    try:
        if stype == 'splash':
            result = crop_black_bars(img)
            action = "SPLASH-CROP"
        elif stype == 'modal':
            result = crop_modal(img)
            action = "MODAL-CROP"
        else:
            result = trim_edges(img)
            action = "TRIM"
        
        rw, rh = result.size
        if rw != w or rh != h:
            result.save(os.path.join(CROPPED_DIR, fname))
            print(f"{action}: {fname} ({w}x{h} -> {rw}x{rh})")
            count += 1
        else:
            img.save(os.path.join(CROPPED_DIR, fname))
            print(f"KEPT:       {fname}")
    except Exception as e:
        img.save(os.path.join(CROPPED_DIR, fname))
        print(f"ERROR:      {fname} - {e}")

print(f"\nDone! Modified {count} images.")
