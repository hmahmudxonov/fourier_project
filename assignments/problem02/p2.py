import matplotlib.pyplot as plt
import dsp.filters as flt
import dsp.excel as xl
import dsp.transforms as tf
from config import DATA_DIR, get_assignment_output_dir
import numpy as np
import dsp.audio as ad
def run():
    path = DATA_DIR / 'prob02_data.xlsx'
    output_dir = get_assignment_output_dir('problem02')

    data = xl.load_excel(str(path))

    dt = data[1,0] - data[0,0]
    sr = int(round(1/dt))

    ad.save_audio(data[:,1], str(DATA_DIR/'prob02_data.wav'), sr=sr)

    X, freq = tf.fft_1d(data[:, 1], sr=sr)

    beep, mask = flt.beep(np.abs(X), freq, prom=10, h=1e6)

    x_filt = flt.beep_filter(beep, data[:,1], sr=sr, q=10)
    X_filt, freq_filt = tf.fft_1d(x_filt, sr=sr)


    ad.save_audio_raw(x_filt, str(output_dir / 'x_filt.wav'), sr=sr)


    print(f'Frequencies to be removed: {beep[:4]}')

    plt.figure()
    plt.plot(freq[:len(X)//2], np.abs(X[:len(X)//2]))
    plt.title('Frequency spectrum: original')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    save_path = output_dir / 'freq_spectrum_org.png'
    plt.savefig(save_path)
#    plt.show()
    plt.close()

    plt.figure()
    plt.plot(freq_filt[:len(X)//2], np.abs(X_filt[:len(X)//2]))
    plt.title('Frequency spectrum: filtered')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    save_path = output_dir / 'freq_spectrum_flt.png'
    plt.savefig(save_path)
#    plt.show()
    plt.close()

    print('The hidden message is Hallelujah')
