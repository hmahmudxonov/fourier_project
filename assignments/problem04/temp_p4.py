import cv2
import numpy as np
import matplotlib.pyplot as plt
import dsp.image as im
import dsp.excel as xl
import dsp.transforms as tf

im1 = im.load_image(r'D:\Python Projects\fourier_project\data\prob04_im01.jpg', gray=False)
im2 = im.load_image(r'D:\Python Projects\fourier_project\data\prob04_im02.jpg', gray=False)

print(im1.shape, im2.shape, im1.max())
print(im1.dtype, im2.dtype, im2.max())

#print(im1)
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
'''
F1 = np.zeros_like(im1, dtype=complex)
F2 = np.zeros_like(im2, dtype=complex)
F1_l = np.zeros_like(im1, dtype=complex)
F2_h = np.zeros_like(im2, dtype=complex)
'''
h = np.zeros_like(im1, dtype=complex)
for i in range(3):
    F1 = tf.fft_2d(im1[:,:,i])
    F2 = tf.fft_2d(im2[:,:,i])

    F1_l = gaussian_high_low_pass_filter(F1, pass_type='h', sigma=40)
    F2_h = gaussian_high_low_pass_filter(F2, pass_type='l', sigma=15)

    H = F1_l + F2_h

    h[:,:,i] = tf.ifft_2d(H)

h = np.real(h)
h = (h - np.min(h)) / (np.max(h) - np.min(h)) * 255.0
h = np.clip(h, 0, 255).astype(np.uint8)
print(h.shape, h.dtype, h.real.max())
im.show_image(h)
im.save_image(h, 'hybrid_coloured.png')

h = cv2.cvtColor(h,cv2.COLOR_RGB2GRAY)
im.show_image(h)
im.save_image(h, 'hybrid_grayscale.png')