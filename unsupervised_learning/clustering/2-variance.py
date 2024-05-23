#!/usr/bin/env python3
"""task 1"""


import numpy as np


def variance(X, C):
    """
    calculates  intra-cluster variance of data set

    X = numpy.ndarray of shape (n, d) containing
        data set
    C = numpy.ndarray of shape (k, d) containing
        centroid means of each cluster
    """
    n, d = np.shape(X)
    k = np.shape(C)[0]
    distances = np.min(np.sum((X[:, np.newaxis] - C) ** 2, axis=2), axis=1)
    # Calculate the total variance
    var = np.sum(distances)
    return var
