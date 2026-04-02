#!/usr/bin/env python3
"""Replace the synthesized splash sound with the original WAV audio."""

import re

# Read the original base64 audio
with open('/home/ubuntu/project-zero-roulette/casino_audio_b64.txt', 'r') as f:
    audio_b64 = f.read().strip()

# Read the current index.html
with open('/home/ubuntu/project-zero-roulette/index.html', 'r') as f:
    html = f.read()

# The new sound function using the original embedded WAV
new_sound_function = f"""  function playRouletteBallSound(){{
    try{{
      const audio=new Audio('data:audio/wav;base64,{audio_b64}');
      audio.volume=0.4;
      audio.play().catch(()=>{{}});
    }}catch(e){{console.log('Audio not available');}}
  }}"""

# Replace the old synthesized sound function
old_pattern = r'  function playRouletteBallSound\(\)\{.*?\n  \}'
new_html = re.sub(old_pattern, new_sound_function, html, flags=re.DOTALL)

if new_html == html:
    print("ERROR: Pattern not found, no replacement made!")
else:
    with open('/home/ubuntu/project-zero-roulette/index.html', 'w') as f:
        f.write(new_html)
    print("SUCCESS: Original splash sound restored!")
    # Verify
    if 'data:audio/wav;base64,UklGR' in new_html:
        print("VERIFIED: WAV audio data is embedded correctly.")
    else:
        print("WARNING: Could not verify audio embedding.")
