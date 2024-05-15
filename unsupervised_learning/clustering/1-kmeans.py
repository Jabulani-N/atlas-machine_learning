#!/usr/bin/env python3
"""task 1"""


import numpy as np


def kmeans(X, k, iterations=1000):
    """runs iteratsions iterations of k-means clustering"""
    centroid = initialize(X, k)
    if centroid == None or\
        iterations <= 0:
        return None, None


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
        if type(k) is not int or\
           k <= 0:
            return None
        n, d = np.shape(X)
        maxima = np.max(X, 0)
        minima = np.min(X, 0)

        centroids = np.random.uniform(minima, maxima, (k, d))
    except Exception:
        pass
    return centroids
