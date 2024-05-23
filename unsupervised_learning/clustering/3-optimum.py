#!/usr/bin/env python3
"""task 1"""


import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """calculates optimum number of clusters by variance"""
    if kmax is None:
        kmax = X.shape[0]
    results = []
    d_vars = []
    if type(kmin) is not int or \
       type(kmax) is not int or\
       kmin >= kmax:
        return None, None
    if type(X) is not np.ndarray:
        return None, None

    for k in range(kmin, kmax + 1):
        # Run K-means for the current cluster size
        centroids, clusters = kmeans(X, k, iterations)
        if centroids is None or\
           clusters is None:
            return None, None

        # Calculate the total intra-cluster variance
        total_variance = variance(X, centroids)

        results.append((centroids, clusters))

        base_variance = variance(X, results[0][0])
        d_vars.append(base_variance - total_variance)

    return results, d_vars
