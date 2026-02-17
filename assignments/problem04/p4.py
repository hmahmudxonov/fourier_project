import dsp.filters as flt
import dsp.transforms as tf
import dsp.image as im
import numpy as np
from config import DATA_DIR, get_assignment_output_dir

def run():

    path1 = DATA_DIR / 'prob04_im01.jpg'
    path2 = DATA_DIR / 'prob04_im02.jpg'
    out_dir = get_assignment_output_dir('problemo04')

    im1 = im.load_image(str(path1), gray=False)
    im2 = im.load_image(str(path2), gray=False)

    h = np.zeros_like(im1, dtype=complex)
    for i in range(3):
        F1 = tf.fft_2d(im1[:, :, i])
        F2 = tf.fft_2d(im2[:, :, i])

        F1_l = flt.gaussian_high_low_pass_filter(F1, pass_type='h', sigma=40)
        F2_h = flt.gaussian_high_low_pass_filter(F2, pass_type='l', sigma=15)

        H = F1_l + F2_h

        h[:, :, i] = tf.ifft_2d(H)

    h = np.real(h)
    h = (h - np.min(h)) / (np.max(h) - np.min(h)) * 255.0
    h = np.clip(h, 0, 255).astype(np.uint8)

#    im.show_image(h)
    save_path1 = out_dir / 'p4_hybrid_rgb.png'
    im.save_image(h, str(save_path1))

    h_gray = im.rgb2gray(h)

#    im.show_image(h_gray)
    save_path2 = out_dir / 'p4_hybrid_gray.png'
    im.save_image(h_gray, str(save_path2))
