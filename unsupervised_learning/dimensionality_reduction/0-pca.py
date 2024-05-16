#!/usr/bin/env python3
"""module documentation
task 0
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
            This means it's already standardized
    var = fraction of the variance PCA transformation maintains
    """

    # x_standardized = Standardize_data(X)
    x_standardized = X
    x_cov = covariance(x_standardized)
    # find eigen composition
    preeig_vals, preeig_vecs = np.linalg.eig(x_cov)
    eig_vals = np.copy(preeig_vals)
    eig_vecs = np.copy(preeig_vecs)

    # make eigenvectors (loadings) largest in absolute value positive
    max_abs_idx = np.argmax(np.abs(eig_vecs), axis=0)
    signs = np.sign(eig_vecs[max_abs_idx, range(eig_vecs.shape[0])])
    eig_vecs = eig_vecs * signs[np.newaxis, :]
    eig_vecs = eig_vecs.T
    # rearrange eigen comp
    # make a list of (eigenvalue, eigenvector) tuples
    eig_pairs = [(np.abs(eig_vals[i]),
                  eig_vecs[i, :])
                 for i in range(len(eig_vals))]
    # sort the from  highest to  lowest
    # based on eigenvalues magnitude
    eig_pairs.sort(key=lambda x: x[0], reverse=True)
    # For further usage
    eig_vals_sorted = np.array([x[0] for x in eig_pairs])
    eig_vecs_sorted = np.array([x[1] for x in eig_pairs])
    # choose principal components
    # Select top k eigenvectors based on the variance
    cumulative_variance = np.cumsum(eig_vals_sorted) /\
        np.sum(eig_vals_sorted)
    # Add 1 to start from 1 component
    k = np.argmax(cumulative_variance >= var + 0) + 2
    # W = Projection matrix
    W = eig_vecs_sorted[:k, :].T
    # multiplying the first two columns by -1
    W[:, 0:2] *= -1
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
    standard deviation
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
