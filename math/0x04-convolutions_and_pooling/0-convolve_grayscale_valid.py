#!/usr/bin/env python3
"""contains the convolve_grayscale_valid function"""

import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    performs a valid convolution on grayscale images
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

    new_h = int(h - kh + 1)
    new_w = int(w - kw + 1)

    # initialize convolution output tensor
    output = np.zeros((m, new_h, new_w))

    # Loop over every pixel of the output
    for x in range(new_w):
        for y in range(new_h):
            # element-wise multiplication of the kernel and the image
            output[:, y, x] = (kernel * images[:,
                                               y: y + kh,
                                               x: x + kw]).sum(axis=(1, 2))

    return output
