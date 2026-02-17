import dsp.excel as xl
import dsp.transforms as tf
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss
import dsp.image as im

data1 = xl.load_excel(r'D:/Python Projects\fourier_project\data\prob3_im1.xlsx')
data2 = xl.load_excel(r'D:/Python Projects\fourier_project\data\prob3_im2.xlsx')
'''
print(data1.shape)
print(data2.shape)

print(data1.dtype, data2.dtype)

print(data1.max(), data1.min())
print(data2.max(), data2.min())

data_cpx1 = data1 + 1j*data2
F = data1 * np.exp(1j*data2)

im = np.fft.ifft2(np.fft.ifftshift(data_cpx1))

plt.imshow(im.real)
plt.show()
'''

F1 = np.fft.fft2(data1)
F2 = np.fft.fft2(data2)

mag1 = np.abs(F1)
phase1 = np.angle(F1)
mag2 = np.abs(F2)
phase2 = np.angle(F2)

X1 = mag1 * np.exp(1j*phase2)
X2 = mag2 * np.exp(1j*phase1)

x1 = np.fft.ifft2(X1)
x2 = np.fft.ifft2(X2)
'''
#normalisation1
x1_abs = x1.real/np.max(x1.real)
x2_abs = x2.real/np.max(x2.real)
'''
'''
#normalisation2
x1_abs = x1.real - np.min(x1.real)
x1_abs /= np.max(x1.real)

x2_abs = x2.real - np.min(x2.real)
x2_abs /= np.max(x2.real)
'''
'''
#normalisation3
x1_abs = np.log(np.abs(x1))
x2_abs = np.log(np.abs(x2))
'''

plt.imshow(x1.real, cmap='jet')
plt.title('mag1+ph2')
plt.clim(-0.5, 0.5)
plt.colorbar()
plt.show()

plt.imshow(x2.real, cmap='jet')
plt.title('mag2+ph1')
plt.clim(-0.5, 0.5)
plt.colorbar()
plt.show()
