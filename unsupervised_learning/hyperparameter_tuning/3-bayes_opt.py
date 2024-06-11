#!/usr/bin/env python3
"""task 3"""

import numpy as np
GP = __import__('2-gp').GaussianProcess


class BayesianOptimization:
    """performs Bayesian optimization on noiseless 1D Gaussian process"""
    def __init__(self, f, X_init, Y_init, bounds,
                 ac_samples, l=1, sigma_f=1, xsi=0.01,
                 minimize=True):
        """
        f is the black-box function to be optimized
        X_init = numpy.ndarray
            shape (t, 1)
                t = number of samples
            representing inputs already sampled with black-box function
        Y_init = numpy.ndarray
            shape (t, 1)
                t = t (see above)
            representing outputs of black-box function
                for each input in X_init
        bounds = (min, max)
            tuple
            represents bounds of the space in which to look for optimal point
        ac_samples = number of samples
            logic says this is an int
        l = kernel length parameter
        sigma_f = standard deviation given to output of black box function
        xsi = exploration-exploitation factor for acquisition
        minimize = bool
            minimize = true -> optimize for minimization
            minimize = fale -> optimize for maximization
        """
        min, max = bounds
        self.f, self.minimize, self.xsi = f, minimize, xsi
        self.gp = GP(X_init, Y_init, l, sigma_f)
        self.X_s = np.linspace(min, max, ac_samples, axis=-1)
        # Χ_s above is a 1D array.
        # below we convert to 2D array of arrays
        self.X_s = np.array([np.array([val]) for val in self.X_s])

