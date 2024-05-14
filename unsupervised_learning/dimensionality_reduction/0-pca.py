#!/usr/bin/env python3
"""module documentation
placeholder
"""


import numpy as np


def pca(X, var=0.95):
    """
    performs PCA on a dataset
    X = numpy.ndarray of shape (n, d)
        n = number of data points
        d = number of dimensions in each point
        all dimensions have mean of 0
            across all data points
    var = fraction of the variance PCA transformation maintains
    """
    # break dataset into parts
    # I think these are U, sigma, VTranspose respectively
    _, Sing, Vh = np.linalg.svd(X, full_matrices=False)

    # explained variance ratio
    explained_variance_ratio = (Sing ** 2) / np.sum(Sing ** 2)

    # cumulative sum of explained variance
    cum_explained_variance = np.cumsum(explained_variance_ratio)

    # Find number of components needed to maintain given variance
    nd = np.argmax(cum_explained_variance >= var) + 1

    # Return the weights matrix
    W = Vh[:nd + 1].T

    return W
