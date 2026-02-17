import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy import fftpack
import pandas as pd
import soundfile as sf

df = pd.read_excel(r'data\prob01_data.xlsx', header=None)
data = df.to_numpy()

if np.max(np.abs(data)) > 1:
    data = data / np.max(np.abs(data))


sf.write('audiofile.wav', data, samplerate=44100)
sf.write('audiofile_0.wav', data[:, 0], samplerate=44100)
sf.write('audiofile_1.wav', data[:, 1], samplerate=44100)

X = np.fft.fft(data[:, 0])
Y = np.fft.fft(data[:, 1])
f = np.fft.fftfreq(len(data[:, 0]), 1/44100)
#f = np.fft.fftshift(f)

F = X * np.conjugate(X) / len(X)

#plt.plot(f[:len(X)//2], np.abs(X)[:len(X)//2])
#plt.plot(f, np.abs(Y))
#plt.plot(f, -20*np.log10(np.abs(X)))
plt.plot(f[:len(data[:,0])//2], F[:len(data[:,0])//2])
plt.show()