import cv2

def load_image(path, gray=True):
    if gray:
        return cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return cv2.imread(path, cv2.IMREAD_COLOR)

def show_image(image, win_name='image'):
    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(win_name, 800, 800)
    cv2.imshow(mat=image, winname=win_name)
    cv2.waitKey(0)

def save_image(image, path):
    cv2.imwrite(path, image)

def rgb2gray(im):
    return cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)