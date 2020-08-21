#!/usr/bin/env python3
"""contains the class GaussianProcess"""

import numpy as np


class GaussianProcess:
    """represents a noiseless 1D Gaussian process"""

    def __init__(self, X_init, Y_init, l=1, sigma_f=1):
        """
        constructor
        :param X_init: numpy.ndarray of shape (t, 1)
            representing the inputs already sampled with the black-box function
        :param Y_init: numpy.ndarray of shape (t, 1)
            representing the outputs of the black-box function for each input
            in X_init
            t is number of initial samples
        :param l: length parameter for the kernel
        :param sigma_f: standard deviation given to the output of
            the black-box function
        """
        self.X = X_init
        self.Y = Y_init
        self.l = l
        self.sigma_f = sigma_f
        self.K = self.kernel(X_init, X_init)

    def kernel(self, X1, X2):
        """
        calculates the covariance kernel matrix between two matrices:
        :param X1: numpy.ndarray of shape (m, 1)
        :param X2: numpy.ndarray of shape (n, 1)
        :return: covariance kernel matrix as a numpy.ndarray of shape (m, n)
        """
        sqdist = np.sum(X1 ** 2, 1).reshape(-1, 1) \
            + np.sum(X2 ** 2, 1) \
            - 2 * np.dot(X1, X2.T)
        return self.sigma_f ** 2 * np.exp(-0.5 / self.l ** 2 * sqdist)

    def predict(self, X_s):
        """
        * X_s is a numpy.ndarray of shape (s, 1) containing all of
          the points whose mean and standard deviation should be
          calculated
        * s is the number of sample points
        Returns: mu, sigma
        * mu is a numpy.ndarray of shape (s,) containing the mean
          for each point in X_s, respectively
        * sigma is a numpy.ndarray of shape (s,) containing the
          variance for each point in X_s, respectively
        """
        K = self.K
        K_s = self.kernel(self.X, X_s)
        K_ss = self.kernel(X_s, X_s)
        K_inv = np.linalg.inv(K)

        # mean
        mu_s = K_s.T.dot(K_inv).dot(self.Y)
        mu_s = mu_s.reshape(-1)

        # variance from covariance
        cov_s = K_ss - K_s.T.dot(K_inv).dot(K_s)
        var_s = np.diag(cov_s)
        return mu_s, var_s
