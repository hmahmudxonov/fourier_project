import numpy as np
import scipy.signal as ss

#gaussian filter for low and high pass
def gaussian_high_low_pass_filter(F, pass_type:str, sigma):
    rows, cols = F.shape
    crows = rows // 2
    ccols = cols // 2
    Y, X = np.ogrid[:rows, :cols]
    D2 = (Y - crows) ** 2 + (X - ccols) ** 2
    gaussian = np.exp(-D2 / (2 * sigma ** 2))
    F_low = F * gaussian
    F_high = F - F * gaussian
    if pass_type in ['lowpass','low','l']:
        return F_low
    elif pass_type in ['highpass','high','h']:
        return F_high

#extracts indices of sharp peaks, reasonably suited for finding harmonics
def beep(X, freq, prom=1, dis=200, h=1):
    mask, _ = ss.find_peaks(X, prominence=prom, distance=dis, height=h)
    beep = freq[mask]
    return beep, mask

#notch filter for identified frequencies
def beep_filter(beep, x, q=40.0, sr=44100, n=5):
    beep = np.abs(beep)
    x_filtered = x.copy()
    for i in beep:
        b, a = ss.iirnotch(i, Q=q, fs=sr)
        for j in range(n):
            x_filtered = ss.filtfilt(b, a, x_filtered)
    return x_filtered

#remove frequency above a certain threshold (easily modified to remove freqs below it)
def remove_freq_above_threshold(X, freq, f_max):
    idx = np.abs(freq) < f_max
    X_filt = X * idx
    freq_filt = freq * idx
    return X_filt, freq_filt

#amplify frequency band between a & b, both positive
def amplify_freq_band(X, freq, a, b, amp_factor):   #a & b are lower and upper bounds of freq range to be amplified
    idx = (np.abs(freq) > a) & (np.abs(freq) < b)
    X_amped = np.where(idx, amp_factor, 1.0) * X
    return X_amped