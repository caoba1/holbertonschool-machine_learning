#!/usr/bin/env python3
"""Contains the early_stopping function"""


def early_stopping(cost, opt_cost, threshold, patience, count):
    """
    determines if you should stop gradient descent early
    :param cost: current validation cost of the neural network
    :param opt_cost: lowest recorded validation cost of the neural network
    :param threshold: threshold used for early stopping
    :param patience: patience count used for early stopping
    :param count: count of how long the threshold has not been met
    :return: boolean of whether the network should be stopped early,
    followed by the updated count
    """
    if opt_cost - cost > threshold:
        return False, 0
    else:
        count += 1
        if count < patience:
            return False, count
        else:
            return True, count
