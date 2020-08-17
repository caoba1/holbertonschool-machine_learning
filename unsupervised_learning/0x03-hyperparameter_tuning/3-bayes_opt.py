#!/usr/bin/env python3
"""contains the class BayesianOptimization"""

import numpy as np
GP = __import__('2-gp').GaussianProcess


class BayesianOptimization:
    """performs Bayesian optimization on a noiseless 1D Gaussian process"""

    def __init__(self, f, X_init, Y_init, bounds, ac_samples, l=1,
                 sigma_f=1, xsi=0.01, minimize=True):
        """
        constructor
        :param f: black-box function to be optimized
        :param X_init: numpy.ndarray of shape (t, 1)
            representing the inputs already sampled with the black-box function
        :param Y_init: numpy.ndarray of shape (t, 1) representing the outputs
            of the black-box function for each input in X_init
        :param bounds: tuple of (min, max) representing the bounds
            of the space in which to look for the optimal point
        :param ac_samples: number of samples that should be analyzed
            during acquisition
        :param l: length parameter for the kernel
        :param sigma_f: standard deviation given to the output of the
            black-box function
        :param xsi: exploration-exploitation factor for acquisition
        :param minimize: bool determining whether optimization
            should be performed for minimization (True) or maximization (False)
        """
        self.f = 0
        self.gp = GP(X_init, Y_init, l, sigma_f)
        self.X_s
        self.xsi = xsi
        self.minimize = minimize
