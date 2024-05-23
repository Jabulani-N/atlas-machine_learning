#!/usr/bin/env python3
"""task 1"""


import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    if kmax is None:
        kmax = X.shape[0]
    results = []
    d_vars = []

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
