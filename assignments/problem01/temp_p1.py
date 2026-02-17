import dsp.transforms as tr
import dsp.excel as xl
import dsp.audio as ad
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as ss

data = xl.load_excel(r'/data/prob01_data.xlsx')

X, freq0 = tr.fft_1d(data[:,0])
Y, freq1 = tr.fft_1d(data[:,1])

X_clean, xpsd_clean = tr.denoise_1d(X)
print(X_clean.shape)
print(xpsd_clean.shape)
#remove beeper sound
## identify the beep tone
'''
def beep(psd, freq):
    mask = psd > psd*0.3
    beep = freq[mask]
    return beep
'''
def beep(psd, freq):
    mask, _ = ss.find_peaks(psd, prominence=1, distance=200, height=1)
    beep = freq[mask]
    return beep
## remove the beep tone
def beep_filter(beep, freq, x):
    beep = np.abs(beep)
    x_filtered = x.copy()
    for i in beep:
        b, a = ss.iirnotch(i, Q=40, fs=44100)
        for j in range(5):
            x_filtered = ss.filtfilt(b, a, x_filtered)
    return x_filtered

beep, psd_db = beep(np.abs(X_clean), freq0)

print(beep)
x_filtered = beep_filter(beep, freq0, data[:, 0])


X_restored, f = tr.fft_1d(x_filtered)
xpsd_filtered_db = 10*np.log(np.abs(X_restored) / len(x_filtered) + 1e-12)
plt.plot(freq0, psd_db)
plt.plot(freq0, xpsd_filtered_db)
plt.show()
ad.save_audio(x_filtered.real, '../../test_filtered0.wav')
plt.plot(f, np.abs(X))
plt.plot(f, np.abs(X_restored))
plt.show()


'''
x = tr.ifft_1d(X)
y = tr.ifft_1d(Y)

f=np.stack((x, y), axis=1)
ad.save_audio(x, 'test_audio0.wav')
ad.save_audio(y, 'test_audio1.wav')
ad.save_audio(f, 'test_audio.wav')

f_clean = np.stack((x_clean, y_clean), axis=1)
ad.save_audio(f_clean, 'test_clean.wav')
ad.save_audio(y_clean, 'test_clean1.wav')
ad.save_audio(x_clean, 'test_clean0.wav')
'''
