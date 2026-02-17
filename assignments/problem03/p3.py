import dsp.excel as xl
import numpy as np
import matplotlib.pyplot as plt
from config import DATA_DIR, get_assignment_output_dir

def run():
    path1 = DATA_DIR / 'prob3_im1.xlsx'
    path2 = DATA_DIR / 'prob3_im2.xlsx'
    out_dir = get_assignment_output_dir('problem03')

    data1 = xl.load_excel(str(path1))
    data2 = xl.load_excel(str(path2))

    F1 = np.fft.fft2(data1)
    F2 = np.fft.fft2(data2)

    mag1 = np.abs(F1)
    mag2 = np.abs(F2)
    phase1 = np.angle(F1)
    phase2 = np.angle(F2)

    X1 = mag1 * np.exp(1j * phase2)
    X2 = mag2 * np.exp(1j * phase1)

    x1 = np.fft.ifft2(X1)
    x2 = np.fft.ifft2(X2)

    plt.imshow(x1.real, cmap='jet', origin='lower')
    plt.title('Problem #3: Magnitude_1 + Phase_2')
    plt.clim(-0.5, 0.7)
    plt.colorbar()
    save_path1 = out_dir / 'mag1_ph2.png'
    plt.savefig(str(save_path1))
#    plt.show()

    plt.imshow(data1, cmap='jet', origin='lower')
    plt.title('Problem #3/Image_1')
    plt.colorbar()
    save_path2 = DATA_DIR / 'prob03_im1.png'
    plt.savefig(str(save_path2))
#    plt.show()

    plt.imshow(x2.real, cmap='jet', origin='lower')
    plt.title('Problem #3: Magnitude_2 + Phase_1')
    plt.clim(-0.3, 0.5)
    plt.colorbar()
    save_path3 = out_dir / 'mag2_ph1.png'
    plt.savefig(str(save_path3))
#    plt.show()

    plt.imshow(data2, cmap='jet', origin='lower')
    plt.title('Problem #3/Image_2')
    plt.colorbar()
    save_path4 = DATA_DIR / 'prob03_im2.png'
    plt.savefig(str(save_path4))
#    plt.show()
