#!/usr/bin/env python3
"""contains the rnn function"""

import numpy as np


def rnn(rnn_cell, X, h_0):
    """
    performs forward propagation for a simple RNN
    :param rnn_cell: an instance of RNNCell
        that will be used for the forward propagation
    :param X: data to be used, given as a numpy.ndarray
        of shape (t, m, i)
        t is the maximum number of time steps
        m is the batch size
        i is the dimensionality of the data
    :param h_0: initial hidden state, given as a numpy.ndarray of shape (m, h)
        h is the dimensionality of the hidden state
    :return: H, Y
        H is a numpy.ndarray containing all of the hidden states
        Y is a numpy.ndarray containing all of the outputs
    """
    t, m, i = X.shape

    H = []
    Y = []

    # initilization
    H.append(h_0)

    # traverse input steps
    for step in range(t):
        h, y = rnn_cell.forward(H[-1], X[step])
        H.append(h)
        Y.append(y)

    H = np.array(H)
    Y = np.array(Y)

    return H, Y
