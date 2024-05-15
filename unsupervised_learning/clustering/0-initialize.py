#!/usr/bin/env python3
"""task 0"""


import numpy as np


def initialize(X, k):
    """initializes cluster centroids for K-means
    X is a numpy.ndarray of shape (n, d)
        containing dataset used for K-means clustering
        n = number of data points
        d = number of dimensions for each data point
        k = number of clusters
    """
    centroids = None
    try:
        n, d = np.shape(X)
        maxima = np.max(X, 0)
        minima = np.min(X, 0)

        centroids = np.random.uniform(minima, maxima, (k, d))
    except Exception:
        pass
    return centroids
