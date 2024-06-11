#!/usr/bin/env python3
"""task 5"""

import numpy as np
from scipy.stats import norm
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

    def acquisition(self):
        """calculates the next best sample location
        Uses the Expected Improvement acquisition function
        Returns: X_next, EI
            X_next = numpy.ndarray
                shape (1,)
                    contains a single item
                representing the next best sample point
            EI = numpy.ndarray
                shape (ac_samples,)
                containing the expected improvement of each potential sample

        """
        # runs predict method of the gp object created in task 2
        mean, variance = self.gp.predict(self.X_s)
        mean_sample = self.gp.Y

        orig_variance = variance
        variance = variance.reshape(-1, 1)

        # pick what we optimize for
        if self.minimize:
            first_func = np.min
            second_func = np.max
            argares = np.argmax
        else:
            first_func = np.max
            second_func = np.min
            argares = np.argmin
        mean_sample_opt = first_func(mean_sample)

        with np.errstate(divide='warn'):
            imp = mean_sample_opt - mean - self.xsi
            Z = imp / variance
            Z_for_X_next = imp / orig_variance
            EI = imp * norm.cdf(Z) + variance * norm.pdf(Z)
            # EI[variance == 0.0] = 0.0
            EI_for_X_next = imp * norm.cdf(Z_for_X_next) +\
                orig_variance * norm.pdf(Z_for_X_next)
        X_next = self.X_s[np.where(
            EI_for_X_next == second_func(EI_for_X_next))[0][0]]
        # X_next = self.X_s[argares(EI)]
        # the below is an incomplete attempt to convert to scientific
        # as the checker was expecting it in that format
        # will be abandoned unless necessary
        # MEI = numpy.format_float_scientific(EI[0])
        return X_next, EI[0]

    def optimize(self, iterations=100):
        """optimizes the black-box function

        iterations  = number of iterations
            int
            If next proposed point has already been sampled
                optimization stops early

        return: X_opt, Y_opt
            X_opt = numpy.ndarray
                shape (1,)
                representing optimal point
            Y_opt = numpy.ndarray
                shape (1,)
                representing optimal funciton value
        """
        pass
