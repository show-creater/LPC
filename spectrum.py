from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt
from calc import compute_lpc
from scipy.signal import freqz

for i in range(1,10):
    fname = f'./resampled_sounds/{i}_1.wav'
    fs, data = read(fname)

    if len(data.shape) == 2:
        data = data[:, 0]

    time = np.arange(0, len(data)) / fs
    p = 16
    Fs = 8000

    a = compute_lpc(data, p)

    # LPC係数を計算
    lpc_coeffs = compute_lpc(data, p)

    # 周波数応答を計算
    w, h = freqz(1, lpc_coeffs, worN=512)

    frequencies = w * Fs / (2 * np.pi)

    poles = np.roots(a)

    poles = poles[np.abs(poles) < 1.0]

    ff = np.angle(poles) * fs / (2.0 * np.pi)

    intns = np.abs(poles)

    # 50Hz以上 & ナイキスト周波数以下のフォルマントのみ使用（要確認）
    formantfreq = ff[(ff > 50) & (ff < fs / 2.0) & (intns > 0.85)]

    formants = np.sort(formantfreq)

    print(f"{i}のフォルマント周波数 (Hz):", formants)