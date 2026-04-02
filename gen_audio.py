import numpy as np
import struct, base64, io

# Generate a 3.5-second casino ambiance: roulette ball spinning + crowd murmur
sr = 22050
duration = 3.5
t = np.linspace(0, duration, int(sr * duration), endpoint=False)

# 1. Roulette ball spinning: frequency sweep (click-click-click slowing down)
ball_clicks = np.zeros_like(t)
click_times = []
pos = 0.0
speed = 0.02
while pos < duration:
    click_times.append(pos)
    speed *= 1.025
    pos += speed
for ct in click_times:
    idx = int(ct * sr)
    if idx < len(ball_clicks) - 100:
        click_env = np.exp(-np.linspace(0, 10, 100))
        ball_clicks[idx:idx+100] += click_env * 0.3 * (1.0 - ct/duration)

# Add a metallic ring to each click
ball_ring = np.zeros_like(t)
for ct in click_times:
    idx = int(ct * sr)
    length = min(400, len(t) - idx)
    if length > 0:
        ring_t = np.linspace(0, length/sr, length)
        ring = np.sin(2 * np.pi * 2800 * ring_t) * np.exp(-ring_t * 30) * 0.08 * (1.0 - ct/duration)
        ball_ring[idx:idx+length] += ring

# 2. Crowd murmur: filtered noise
np.random.seed(42)
crowd = np.random.randn(len(t)) * 0.06
window = 80
crowd_smooth = np.convolve(crowd, np.ones(window)/window, mode='same')
crowd_env = 0.5 + 0.5 * np.sin(2 * np.pi * 0.7 * t) * np.sin(2 * np.pi * 1.3 * t)
crowd_smooth *= crowd_env

# 3. Ambient casino tone
ambient = np.sin(2 * np.pi * 180 * t) * 0.02 + np.sin(2 * np.pi * 120 * t) * 0.015

# 4. Chip sounds (occasional clinking)
chips = np.zeros_like(t)
chip_times = [0.3, 0.8, 1.2, 1.7, 2.1, 2.6, 3.0]
for ct in chip_times:
    idx = int(ct * sr)
    length = min(600, len(t) - idx)
    if length > 0:
        chip_t = np.linspace(0, length/sr, length)
        chip = (np.sin(2*np.pi*4200*chip_t) + 0.5*np.sin(2*np.pi*6300*chip_t)) * np.exp(-chip_t*15) * 0.04
        chips[idx:idx+length] += chip

# Mix
mix = ball_clicks + ball_ring + crowd_smooth + ambient + chips

# Fade in/out
fade_in = np.linspace(0, 1, int(0.3 * sr))
fade_out = np.linspace(1, 0, int(0.8 * sr))
mix[:len(fade_in)] *= fade_in
mix[-len(fade_out):] *= fade_out

# Normalize
mix = mix / (np.max(np.abs(mix)) + 1e-6) * 0.7

# Convert to 16-bit PCM WAV
samples = (mix * 32767).astype(np.int16)
buf = io.BytesIO()
n_samples = len(samples)
data_size = n_samples * 2
buf.write(b'RIFF')
buf.write(struct.pack('<I', 36 + data_size))
buf.write(b'WAVE')
buf.write(b'fmt ')
buf.write(struct.pack('<IHHIIHH', 16, 1, 1, sr, sr*2, 2, 16))
buf.write(b'data')
buf.write(struct.pack('<I', data_size))
buf.write(samples.tobytes())

wav_data = buf.getvalue()
b64 = base64.b64encode(wav_data).decode('ascii')

with open('casino_audio_b64.txt', 'w') as f:
    f.write(b64)

print(f"WAV size: {len(wav_data)} bytes")
print(f"Base64 size: {len(b64)} chars")
