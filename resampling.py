import librosa
import soundfile as sf

for i in range(1, 10):

    fname = f'./edited_sounds/{i}_1.wav'
    target_fs = 8000

    data, fs = librosa.load(fname, sr=target_fs)
    
    data_pre = librosa.effects.preemphasis(data)

    sf.write(f'./resampled_sounds/{i}_3.wav', data_pre, target_fs)

    print("新しいサンプリング周波数:", target_fs)
