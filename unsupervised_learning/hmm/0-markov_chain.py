#!/usr/bin/env python3
"""task 0"""

import numpy as np


def markov_chain(P, s, t=1):
    """
    determines  probability of markov chain being in a state
        after t iterations

        P is a square 2D numpy.ndarray
            shape (n, n)
            representing the transition matrix
            P[i, j] = probability of transitioning from state i to state j
        s is a numpy.ndarray
            shape (1, n)
            represents probability of starting in each state
        """
    if not isinstance(P, np.ndarray) or not isinstance(s, np.ndarray):
        return None  # Return None on failure

    # ascertain squareness
    if P.shape[0] != P.shape[1]:
        return None

    result = np.dot(s, np.linalg.matrix_power(P, t))
    return result
