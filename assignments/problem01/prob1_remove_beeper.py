import numpy as np
import scipy.signal as ss
def beep(X, freq, prom=1, dis=200, h=1):
    mask, _ = ss.find_peaks(X, prominence=prom, distance=dis, height=h)
    beep = freq[mask]
    return beep
## remove the beep tone
def beep_filter(beep, x, q=40, sr=44100, n=5):
    beep = np.abs(beep)
    x_filtered = x.copy()
    for i in beep:
        b, a = ss.iirnotch(i, Q=q, fs=sr)
        for j in range(n):
            x_filtered = ss.filtfilt(b, a, x_filtered)
    return x_filtered