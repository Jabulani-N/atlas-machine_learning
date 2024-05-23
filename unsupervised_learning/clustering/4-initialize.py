#!/usr/bin/env python3
"""task 4"""


import numpy as np
kmeans = __import__('1-kmeans').kmeans


def initialize(X, k):
    """initializes variablesf0r Gaussian Mixture Model"""
    centroids = None
    pri = None
    m = None
    S = None

    try:
        if type(k) is not int or k <= 0:
            return None, None, None

        # Initialize cluster centroids using K-means
        centroids, _ = kmeans(X, k)

        if centroids is None:
            return None, None, None

        n, d = X.shape

        # Initialize priors evenly
        pri = np.full(k, 1/k)

        m = centroids.reshape(k, 1, d)

        # Initialize covariance matrices as identity matrices
        S = np.tile(np.identity(d, dtype=float), (k, 1, 1))

    except Exception:
        pass

    return pri, m, S
