import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib import image as mp_image
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm
from scipy.ndimage import convolve, correlate, filters
from scipy import misc, ndimage


img_src = './data/'


def img_show(image, **argv):
    plt.figure(figsize=(10, 10))
    plt.imshow(image, **argv)  # display the image
    plt.axis('off')
    plt.show()


def img_info(image):
    print(image.shape, image.dtype, type(image))


def get_contrast(img):
    return np.max(img * 255) - np.min(img * 255)


def base_stats(img):
    return "Contrasto: {0:.0f} (valore massimo: {1:.0f}; valore minimo: {2:.0f})".format(get_contrast(img),
                                                                                         np.max(img * 255),
                                                                                         np.min(img * 255))


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


def normalize(img):
    return (img - np.min(img)) / (np.max(img) - np.min(img))
