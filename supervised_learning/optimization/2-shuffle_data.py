#!/usr/bin/env python3
"""module documentation
this module creates a function:
    shuffle_data

"""


import numpy as np


def shuffle_data(X, Y):
    """shuffles numpy.ndarray X, y
    in the same way as each-other
    returns shuffled results
    X is shape (m,nx)
    Y is shape (m,ny)
    """
    permutation = np.random.permutation(np.shape(X)[0])
    # we're literally just making up a random order of indices
    return X[permutation], Y[permutation]
