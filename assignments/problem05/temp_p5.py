import numpy as np
import matplotlib.pyplot as plt
import dsp.image as im
import dsp.excel as xl
import dsp.transforms as tf

data = xl.load_excel(r'D:\Python Projects\fourier_project\data\prob05_data.xlsx')

plt.imshow(data,cmap='jet')
plt.colorbar()
plt.show()

X = tf.fft_2d(data)

plt.imshow(np.abs(X), cmap='jet')
plt.colorbar()
plt.show()