#!/usr/bin/env python3
"""Contains the l2_reg_create_layer function"""

import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    """
    creates a tensorflow layer that includes L2 regularization
    :param prev: tensor containing the output of the previous layer
    :param n: number of nodes the new layer should contain
    :param activation: activation function that should be used on the layer
    :param lambtha: L2 regularization parameter
    :return: output of the new layer
    """
    reg = tf.contrib.layers.l2_regularizer(lambtha)
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")

    model = tf.layers.Dense(units=n,
                            activation=activation,
                            kernel_initializer=init,
                            kernel_regularizer=reg)

    return model(prev)
