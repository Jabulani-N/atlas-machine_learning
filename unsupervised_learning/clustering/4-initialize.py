#!/usr/bin/env python3
"""task 1"""


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

        # Initialize centroid means with the centroids from K-means
        m = centroids

        # Initialize covariance matrices as identity matrices
        S = np.zeros((k, d, d))
        for i in range(k):
            S[i] = np.identity(d)

    except Exception:
        pass

    return pri, m, S
