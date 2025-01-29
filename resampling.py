import librosa
import soundfile as sf

for i in range(1, 11):

    fname = f'./edited_sounds/{i}_2.wav'
    target_fs = 8000

    data, fs = librosa.load(fname, sr=target_fs)

    sf.write(f'./resampled_sounds/{i}_2.wav', data, target_fs)

    print("新しいサンプリング周波数:", target_fs)
