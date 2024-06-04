#!/usr/bin/env python3
"""task 1"""

import numpy as np


class GaussianProcess:
    """represents a noiseless 1D Gaussian process"""
    def __init__(self, X_init, Y_init, l=1, sigma_f=1):
        """
        X_init = numpy.ndarray
            shape (t, 1)
            represent inputs already sampled with the black-box function
        Y_init = numpy.ndarray
            shape (t, 1)
            represent outputs of black-box function for each input in X_init
        t = number of initial samples
        l = length parameter for the kernel
        sigma_f = standard deviation
            given to output of the black-box function

    Sets
        public instance attributes
            X
            Y
            l
            sigma_f
    Sets
        public instance attribute
            K
                represent current covariance kernel matrix
                    for the Gaussian process
        """
        # given initialization values
        self.X, self.Y, self.l, self.sigma_f = X_init, Y_init, l, sigma_f
        self.K = self.kernel(X_init, X_init)

    def kernel(self, X1, X2):
        """calculates and returns the covariance kernal matrix
        DO NOT SET IT HERE
            set self.K in the initializer by calling this

        X1 = numpy.ndarray
            shape (m, 1)
        X2 = numpy.ndarray
            shape (n, 1)
        Returns: covariance kernel matrix as a numpy.ndarray of shape (m, n)
        """
        m, n = np.shape(X1)[0], np.shape(X2)[0]
        kernel_matrix = np.zeros((m, n))

        for i in range(m):
            for j in range(n):
                dist = X1[i] - X2[j]
                kernel_matrix[i, j] = self.sigma_f ** 2 * np.exp(
                    (-(dist / self.l) ** 2) / 2)
        return kernel_matrix

    def predict(self, X_s):
        """
        predict mean and standard deviation
        of points in a Gaussian process

        X_s = numpy.ndarray
            contains all points
            shape (s, 1)
                s = number of sample points

        return
            mu, sigma
                mu = numpy.ndarray
                    shape (s,)
                    contains mean for each point in X_s
                sigma = numpy.ndarray
                    shape (s,)
                    contains variance for each point in X_s
        """
        s = np.shape(X_s)[0]
        mu = np.zeros(s)
        sigma = np.zeros(s)
        noise = 0
        for i in range(s):
            mu[i] = self.K ^ (self.K + noise) ^ (-(X_s[i]))
        return mu, sigma
