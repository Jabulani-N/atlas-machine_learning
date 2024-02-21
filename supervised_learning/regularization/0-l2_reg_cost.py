#!/usr/bin/env python3
"""module documentation
this module creates a function.
"""


import numpy as np
import tensorflow.compat.v1 as tf


def l2_reg_cost(cost, lambtha, weights, L, m):
    """
    cost = cost of network without L2 regularization
    lambtha = regularization parameter
    weights = dictionary of weights & biases (numpy.ndarrays) of neural network
    L = number of layers in neural network
    m = number of data points used
    """
    l2_cost = 0
    for layer in range(1, L + 1):
        l2_cost += np.sum(np.square(weights["W" + str(layer)]))
    l2_regularization = (lambtha / (2 * m)) * l2_cost
    new_cost = cost + l2_regularization
    return new_cost
