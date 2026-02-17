import soundfile as sf
import numpy as np

def load_audio(path):
    data, sr = sf.read(path)
    if np.max(data) > 1:
        data = data / np.max(data)
    return data, sr

def save_audio(data, path, sr=44100):
    if np.max(data) > 1:
        data = data / np.max(data)
    sf.write(path, data, sr)

def save_audio_raw(data, path, sr=44100):
    sf.write(path, data, sr)


