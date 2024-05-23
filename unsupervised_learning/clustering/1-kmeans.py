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
    # closest is a 1D list
    centroids_after_iterating = np.copy(centroids)
    old_centroid_pos = np.copy(centroids[0])
    new_centroid_pos = np.copy(old_centroid_pos)
    for iteration in range(iterations):
        closest = find_closest_centroid(centroids, X)
        for i in range(k):
            cluster_points = X[closest == i]
            if len(cluster_points) > 0:
                centroids[i] = np.mean(cluster_points, axis=0)
            else:
                # Reinitialize the centroid if the cluster has no data points
                minima = np.min(X, axis=0)
                maxima = np.max(X, axis=0)
                centroids[i] = np.random.uniform(minima, maxima)
                # add to a count or something
                # if it equals the amount of total centroids
                # then it instantly returns the final answer.
                # we can do above part
                # after we finish what an iteration looks like
    return centroids, closest


def relocate_centroid(X_trimmed, ):
    """
    relocates one centroid
    by returning a single coordinate set
    returns average of positions recieved
    """
    pass


def find_closest_centroid(centroids, X):
    # Compute Euclidean distance btwn each data point and  centroid
    distances = np.sqrt(np.sum((X[:, np.newaxis] - centroids) ** 2,
                               axis=2))
    # Find the index of the closest centroid f0r each data point
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
