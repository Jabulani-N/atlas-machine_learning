#!/usr/bin/env python3
"""module documentation
similar to task 0,
    but predetermined dimensionality
"""


import numpy as np


def pca(X, ndim):
    """
    performs PCA on a dataset
    X = numpy.ndarray of shape (n, d)
        n = number of data points
        d = number of dimensions in each point
        all dimensions have mean of 0
            across all data points
    var = fraction of the variance PCA transformation maintains
    """

    _, _, Vh = np.linalg.svd(X, full_matrices=False)
    W = Vh[:ndim + 1].T
    return W


def mean(x):
    """
    standardization step 3
    np.mean(X, axis = 0)
    """
    return sum(x)/len(x)


def std(x):
    """
    standardization step 2
    np.std(X, axis = 0)
    """
    return (sum((i - mean(x))**2 for i in x)/len(x))**0.5


def Standardize_data(X):
    """standardization all together"""
    return (X - mean(X))/std(X)


def covariance(x):
    """
    returns covariance matrix of x
    np.cov(x_standardized.T)
    """
    return (x.T @ x)/(x.shape[0]-1)
