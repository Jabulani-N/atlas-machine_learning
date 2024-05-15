#!/usr/bin/env python3
"""task 1"""


import numpy as np


def kmeans(X, k, iterations=1000):
    """runs iteratsions iterations of k-means clustering"""
    centroids = initialize(X, k)
    if centroids is None or\
       iterations <= 0:
        return None, None
    # print("sent centroids", centroids)
    # print("sent X", X)
    # note position 0 is first centroid at centroids[0]
    closest = find_closest_centroid(centroids, X)
    # print("decided closest centroids are:", closest)
    return None, None


def find_closest_centroid(centroids, X):
    # Compute Euclidean distance btwn each data point and  centroid
    distances = np.sqrt(np.sum((X[:, np.newaxis] - centroids) ** 2,
                               axis=2))
    # Find the index of the closest centroid for each data point
    closest_centroid_indices = np.argmin(distances, axis=1)
    return closest_centroid_indices


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
