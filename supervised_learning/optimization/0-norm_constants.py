#!/usr/bin/env python3
"""module documentation
this module,0-norm_constants, creates a function:
    normalization_constants
Though classy, it has no class.

"""


import numpy as np


def normalization_constants(X):
    """This function will calculate and return
    mean, standard deviation
    """
    return np.mean(X, axis=0), np.std(X, axis=0)
