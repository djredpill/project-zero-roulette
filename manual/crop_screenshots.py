#!/usr/bin/env python3
"""
Auto-crop screenshots to remove excess white/dark/gray backgrounds.
Detects the content bounding box and crops with a small padding.
"""
from PIL import Image
import os

SCREENSHOTS_DIR = "/home/ubuntu/project-zero-roulette/manual/screenshots"
CROPPED_DIR = "/home/ubuntu/project-zero-roulette/manual/screenshots_cropped"
os.makedirs(CROPPED_DIR, exist_ok=True)

PADDING = 10  # pixels of padding around content

def get_content_bbox(img):
    """Find the bounding box of the actual content, ignoring uniform backgrounds."""
    pixels = img.load()
    w, h = img.size
    
    # Sample corners to determine background color
    corners = [
        pixels[0, 0],
        pixels[w-1, 0],
        pixels[0, h-1],
        pixels[w-1, h-1]
    ]
    
    # Use the most common corner color as background
    from collections import Counter
    # Convert to tuples for hashing (handle both RGB and RGBA)
    corner_tuples = []
    for c in corners:
        if isinstance(c, int):
            corner_tuples.append((c, c, c))
        else:
            corner_tuples.append(c[:3])
    
    bg_color = Counter(corner_tuples).most_common(1)[0][0]
    
    # Threshold for "close to background"
    threshold = 30
    
    def is_bg(pixel):
        if isinstance(pixel, int):
            p = (pixel, pixel, pixel)
        else:
            p = pixel[:3]
        return all(abs(p[i] - bg_color[i]) < threshold for i in range(3))
    
    # Find content bounds
    top = 0
    for y in range(h):
        row_has_content = False
        for x in range(0, w, 3):  # sample every 3rd pixel for speed
            if not is_bg(pixels[x, y]):
                row_has_content = True
                break
        if row_has_content:
            top = y
            break
    
    bottom = h - 1
    for y in range(h-1, -1, -1):
        row_has_content = False
        for x in range(0, w, 3):
            if not is_bg(pixels[x, y]):
                row_has_content = True
                break
        if row_has_content:
            bottom = y
            break
    
    left = 0
    for x in range(w):
        col_has_content = False
        for y in range(top, bottom+1, 3):
            if not is_bg(pixels[x, y]):
                col_has_content = True
                break
        if col_has_content:
            left = x
            break
    
    right = w - 1
    for x in range(w-1, -1, -1):
        col_has_content = False
        for y in range(top, bottom+1, 3):
            if not is_bg(pixels[x, y]):
                col_has_content = True
                break
        if col_has_content:
            right = x
            break
    
    return (left, top, right, bottom)

count = 0
for fname in sorted(os.listdir(SCREENSHOTS_DIR)):
    if not fname.endswith('.png'):
        continue
    
    fpath = os.path.join(SCREENSHOTS_DIR, fname)
    img = Image.open(fpath)
    w, h = img.size
    
    try:
        left, top, right, bottom = get_content_bbox(img)
        
        # Add padding
        left = max(0, left - PADDING)
        top = max(0, top - PADDING)
        right = min(w, right + PADDING)
        bottom = min(h, bottom + PADDING)
        
        # Only crop if we're actually removing significant area (>5% on any side)
        width_reduction = (w - (right - left)) / w
        height_reduction = (h - (bottom - top)) / h
        
        if width_reduction > 0.03 or height_reduction > 0.03:
            cropped = img.crop((left, top, right, bottom))
            cropped.save(os.path.join(CROPPED_DIR, fname))
            print(f"CROPPED: {fname} ({w}x{h} -> {right-left}x{bottom-top})")
            count += 1
        else:
            # No significant cropping needed, just copy
            img.save(os.path.join(CROPPED_DIR, fname))
            print(f"KEPT:    {fname} (no significant excess)")
    except Exception as e:
        # On error, just copy the original
        img.save(os.path.join(CROPPED_DIR, fname))
        print(f"ERROR:   {fname} - {e}, kept original")

print(f"\nDone! Cropped {count} images.")
