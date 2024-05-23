#!/usr/bin/env python3
"""task 1"""


import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    if kmax is None:
        kmax = 2 * kmin
    results = []
    d_vars = []

    for k in range(kmin, kmax + 1):
        # Run K-means for the current cluster size
        centroids, clusters = kmeans(X, k, iterations)

        # Calculate the total intra-cluster variance
        total_variance = variance(X, centroids)

        results.append((centroids, clusters))

        # Calculate the difference in variance from the smallest cluster size
        if k == kmin:
            base_variance = total_variance
        d_vars.append(total_variance - base_variance)

    return results, d_vars
