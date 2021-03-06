#!/usr/bin/env python3
"""Contains the Neuron class"""

import numpy as np


class Neuron:
    """Neuron class
    nx is the number of input features to the neuron
    """

    def __init__(self, nx):
        """constructor"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        """The weights vector for the neuron. Upon instantiation,
        it should be initialized using a random normal distribution."""
        self.__W = np.random.normal(0, 1, (1, nx))

        """The bias for the neuron. Upon instantiation,
        it should be initialized to 0."""
        self.__b = 0

        """The activated output of the neuron (prediction). Upon instantiation,
        it should be initialized to 0."""
        self.__A = 0

    @property
    def W(self):
        """property to retrieve it"""
        return self.__W

    @property
    def b(self):
        """property to retrieve it"""
        return self.__b

    @property
    def A(self):
        """property to retrieve it"""
        return self.__A
