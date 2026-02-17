import numpy as np


def fft_1d(x, sr=44100):
    f = np.fft.fftfreq(len(x), 1/sr)
    X = np.fft.fft(x)
    n = len(X)
#    return X[:n//2], f[:n//2]
    return X, f
def ifft_1d(X):
    return np.fft.ifft(X)

def fft_2d(img):
    return np.fft.fftshift(np.fft.fft2(img))

def ifft_2d(F):
    return np.fft.ifft2(np.fft.ifftshift(F))

def denoise_1d(X):
    psd = np.abs(X)**2 / len(X)
    threshold = np.max(psd) * 0.0001
    mask = psd > threshold
    psd_clean = psd * mask
    X_clean = X * mask
    return X_clean, psd_clean