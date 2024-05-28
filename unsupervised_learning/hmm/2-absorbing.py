#!/usr/bin/env python3
"""task 1"""

import numpy as np


def absorbing(P):
    """determines if P is absorbinbg Markov chain
    P is 2D numpy.ndarray
    """
    if not isinstance(P, np.ndarray):
        return None  # Return None on failure
    if P.shape[0] != P.shape[1]:
        return None
    if np.any(np.less_equal(P, 0)):
        return None
    for subarray in P:
        if np.any(np.less_equal(subarray, 0)):
            return None
    if diagonal_check(P, 1) is False:
        return False

def diagonal_check(P, target=1):
    """checks 2D array P
        for any instance of target
            on a diagonal position
    """
    dia = np.diag(P)
    return np.any(np.equal(dia, target))
