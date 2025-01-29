import numpy as np
from scipy.signal import freqz
from scipy.linalg import solve_toeplitz
import librosa
from write_excel import write_excel
from standardization import concat_and_standardization

def compute_lpc(signal, p):
    """
    LPC係数を計算
    """
    r = np.correlate(signal, signal, mode='full')
    r = r[len(signal)-1:len(signal)+p]
    a = solve_toeplitz((r[:-1], r[:-1]), -r[1:])
    return np.concatenate(([1], a))

def find_formants(signal, fs, p=12, intns_threshold=0.6, min_distance=200):

    a = compute_lpc(signal, p)
    
    poles = np.roots(a)
    intns = np.abs(poles)
    ff = np.angle(poles) * fs / (2 * np.pi)

    formantfreq = ff[(ff > 200) & (ff < 3500) & (intns > intns_threshold)]

    filtered_formants = []
    for f in np.sort(formantfreq):
        if len(filtered_formants) == 0 or abs(f - filtered_formants[-1]) > min_distance:
            filtered_formants.append(f)

    F1 = filtered_formants[0] if len(filtered_formants) > 0 else None
    F2 = filtered_formants[1] if len(filtered_formants) > 1 else None

    return F1, F2

x=1
standarded_data_list = []

for j in range(1, 4):
    spectrum_data = [[], []]
    for i in range(1, 10):
        y, sr = librosa.load(f"resampled_sounds/{i}_{j}.wav", sr=8000)
        y_preemphasized = librosa.effects.preemphasis(y)

        F1, F2 = find_formants(y_preemphasized, sr, p=13, intns_threshold=0.6)
        print(f"[{i}の周波数フォルマント] のF1: {F1} Hz, F2: {F2} Hz")
        spectrum_data[0].append(F1)
        spectrum_data[1].append(F2)

    write_excel(spectrum_data, j)
    data = {'F1': spectrum_data[0], 'F2': spectrum_data[1], 'ラベル': [1, 2, 3, 4, 5, 6, 7, 8, 9], '話者': [j]*9}
    standarded_data_list.append(data)
    concat_and_standardization(standarded_data_list)

