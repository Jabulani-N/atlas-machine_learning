#!/usr/bin/env python3
"""module documentation
this module,1-normalize, creates a function:
    normlaize
Though classy, it has no class.

"""


import numpy as np


def normalize(X, m, s):
    """returns the normalized array of X
    X = input numpy.ndarray shape (d, nx)
        d = number of data points
        nx = number of features
    m = numpy.ndarray shape (nx,)
        contains means of each X feature
    s = numpy.ndarray shape (nx,)
        contains standard devs of each X feature
    """
    return np.divide(np.subtract(X, m), s)
