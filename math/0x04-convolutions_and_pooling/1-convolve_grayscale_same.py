#!/usr/bin/env python3
"""contains the convolve_grayscale_valid function"""

import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    performs a same convolution on grayscale images:
    :param images: numpy.ndarray with shape (m, h, w)
        containing multiple grayscale images
        m is the number of images
        h is the height in pixels of the images
        w is the width in pixels of the images
    :param kernel: numpy.ndarray with shape (kh, kw)
        containing the kernel for the convolution
        kh is the height of the kernel
        kw is the width of the kernel
    :return: numpy.ndarray containing the convolved images
    """
    w, h, m = images.shape[2], images.shape[1], images.shape[0]
    kw, kh = kernel.shape[1], kernel.shape[0]

    # Calculate the required padding
    ph = max(int((kh - 1) / 2), int(kh / 2))
    pw = max(int((kw - 1) / 2), int(kw / 2))

    # pad images
    images_padded = np.pad(images,
                           pad_width=((0, 0), (ph, ph), (pw, pw)),
                           mode='constant', constant_values=0)

    # initialize convolution output tensor
    output = np.zeros((m, h, w))

    # Loop over every pixel of the output
    for y in range(h):
        for x in range(w):
            # element-wise multiplication of the kernel and the image
            output[:, y, x] =\
                (kernel * images_padded[:,
                                        y: y + kh,
                                        x: x + kw]).sum(axis=(1, 2))

    return output
