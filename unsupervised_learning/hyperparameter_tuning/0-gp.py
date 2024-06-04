#!/usr/bin/env python3
"""task 0"""

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

    def kernel(self, X1, X2):
        """calculates and returns the covariance kernal matrix
        DO NOT SET IT HERE
            set self.K in the initializer by calling this
        """
        pass
