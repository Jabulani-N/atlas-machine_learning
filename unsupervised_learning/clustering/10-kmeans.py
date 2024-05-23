#!/usr/bin/env python3
"""task 10"""


import sklearn.cluster


def kmeans(X, k):
    """performs K-means on a dataset
        via sklearn"""
    skl_kmeans = sklearn.cluster.KMeans(n_clusters=k)
    skl_kmeans.fit(X)
    C = skl_kmeans.cluster_centers_
    clss = skl_kmeans.labels_
    return C, clss
