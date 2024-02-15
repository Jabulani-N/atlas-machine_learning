#!/usr/bin/env python3
"""module documentation
this module creates a function.

"""


import numpy as np


def batch_norm(Z, gamma, beta, epsilon):
    """
    Z = numpy.ndarray of shape (m, n) that should be normalized
    m =  number of data points
    n = number of features in Z
    gamma = numpy.ndarray of shape (1, n)
        containing the scales used for batch normalization
    beta = numpy.ndarray of shape (1, n)
        containing the offsets used for batch normalization
    epsilon = small number used to avoid division by zero

    Return normalized Z matrix
    """
    mean = np.mean(Z, axis=0, keepdims=True)
    variance = np.var(Z, axis=0, keepdims=True)
    Z_norm = (Z - mean) / np.sqrt(variance + epsilon)
    # scale it with gamma and beta (offsets (basically bias))
    Z_norm_scaled = Z_norm * gamma + beta
    return Z_norm_scaled
