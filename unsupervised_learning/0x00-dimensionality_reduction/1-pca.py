#!/usr/bin/env python3
""" contains the pca function"""
import numpy as np


def pca(X, ndim):
    """
    performs PCA on a dataset
    :param X: numpy.ndarray of shape (n, d) where:
        n is the number of data points
        d is the number of dimensions in each point
    :param ndim: new dimensionality of the transformed X
    :return: T, a numpy.ndarray of shape (n, ndim)
        containing the transformed version of X
    """
    X_m = X - np.mean(X, axis=0)
    u, s, vh = np.linalg.svd(X_m)

    W = vh[:, :ndim]
    T = np.matmul(X_m, W)

    return T
