#!/usr/bin/env python3
"""module documentation
task 1
"""


import numpy as np


def pca(X, ndim):
    """
    performs PCA on a dataset
    X = numpy.ndarray of shape (n, d)
        n = number of data points
        d = number of dimensions in each point
    var = fraction of the variance PCA transformation maintains
    """
    x_mean = np.mean(X, axis=0)
    x_centered = center(X)
    x_standardized = x_centered
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
    eig_vecs_sorted = np.array([x[1] for x in eig_pairs])
    # choose principal components
    # Select top k=ndim eigenvectors
    k = ndim
    # W = Projection matrix
    W = eig_vecs_sorted[:k, :].T
    # multiplying the first two columns by -1
    W[:, 0:2] *= -1
    transformed = np.matmul(x_standardized, W)
    return transformed


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


def center(X):
    """centers X"""
    return (X - np.mean(X, axis=0))


def covariance(x):
    """
    returns covariance matrix of x
    np.cov(x_standardized.T)
    """
    return (x.T @ x)/(x.shape[0]-1)
