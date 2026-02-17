import numpy as np
import matplotlib.pyplot as plt
import dsp.filters as flt
import dsp.audio as ad
import dsp.transforms as tf
import dsp.excel as xl
from config import DATA_DIR, get_assignment_output_dir
def run():
    print('Running Problem #1: remove beeper sound from a dog bark')

    path1 = DATA_DIR / 'prob01_data.xlsx'
    out_dir = get_assignment_output_dir('problem01')

    data = xl.load_excel(str(path1))

    # fft
    X, freq0 = tf.fft_1d(data[:, 0])
    Y, freq1 = tf.fft_1d(data[:, 1])

    # denoise
    X_clean, _ = tf.denoise_1d(X)
    Y_clean, _ = tf.denoise_1d(Y)

    # find harmonic frequencies of the beep
    xbeep, _ = flt.beep(np.abs(X_clean), freq0)
    ybeep, _ = flt.beep(np.abs(Y_clean), freq1)
    print(xbeep.shape)
    # remove/filter frequencies, and merge the two signals for stereo file
    x_filtered = flt.beep_filter(xbeep, data[:, 0])
    y_filtered = flt.beep_filter(ybeep, data[:, 1])

    f_filtered = np.stack((x_filtered, y_filtered), axis=1)

    # save as audiofile
    save_path1 = out_dir / 'beep_free_dog_bark.wav'
    ad.save_audio(f_filtered, str(save_path1))

    # fft on filtered audio
    X_filtered, f0 = tf.fft_1d(x_filtered)
    Y_filtered, f1 = tf.fft_1d(y_filtered)

    # plot for comparison of the filtered audio (separately for each channel
    Nx = len(X)//2
    fig1, ax1 = plt.subplots()
    ax1.plot(f0[:Nx], np.abs(X)[:Nx], label='Original')
    ax1.plot(f0[:Nx], np.abs(X_filtered)[:Nx], label='Filtered')
    ax1.set_title(r'Problem #1/Frequency spectrum, channel_1')
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_ylabel('Amplitude')
    ax1.legend()
    ax1.grid()
    save_path2 = out_dir / 'p1_spect_original_vs_filtered_ch1.png'
    fig1.savefig(str(save_path2))
#    plt.show()

    Ny = len(Y)//2
    fig2, ax2 = plt.subplots()
    ax2.plot(f1[:Ny], np.abs(Y)[:Ny], label='Original')
    ax2.plot(f1[:Ny], np.abs(Y_filtered)[:Ny], label='Filtered')
    ax2.set_title(r'Problem #1/Frequency spectrum, channel_2')
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Amplitude')
    ax2.legend()
    ax2.grid()
    save_path3 = out_dir / 'p1_spect_filtered_ch2.png'
    fig2.savefig(str(save_path3))
#    plt.show()
