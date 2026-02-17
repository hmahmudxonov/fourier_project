import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss
import dsp.transforms as tf
import dsp.excel as xl
import dsp.audio as ad
import assignments.problem01.prob1_remove_beeper as p1
import dsp.filters as flt

data = xl.load_excel(r'D:\Python Projects\fourier_project\data\prob02_data.xlsx')

dt = data[1, 0] - data[0, 0]
sr = int(round(1/dt))
print(sr)

X, freq = tf.fft_1d(data[:, 1], sr = sr)

plt.plot(freq, np.abs(X))
plt.show()

beep, mask = flt.beep(np.abs(X), freq, prom=10, h=1e6)
amps = np.abs(X[mask[:3]])

print(amps/len(X)*2)
print(mask)
'''
def dominant_frequency(X, freq):
    idx = np.argmax(np.abs(X))
    f0 = freq[idx]

    print('idx' ,idx)

    X_filt = np.zeros_like(X)
    X_filt[idx] = X[idx]

    idx_sym = (-idx) % len(X)
    X_filt[idx_sym] = X[idx_sym]

    print(f'Dominant frequency: {f0} Hz')
    print(X_filt.shape)
    return X_filt, f0
'''


