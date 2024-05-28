#!/usr/bin/env python3
"""task 1"""

import numpy as np


def regular(P):
    """
    determines
    steady state probabilities of regular markov chain
    """
    if not isinstance(P, np.ndarray):
        return None  # Return None on failure
    if P.shape[0] != P.shape[1]:
        return None

    return steady_state_prop(P.transpose())


def steady_state_prop(P):
    """a step used in steady state"""
    dim = P.shape[0]
    q = (P - np.eye(dim))
    ones = np.ones(dim)
    q = np.c_[q, ones]
    QTQ = np.dot(q, q.T)
    bQT = np.ones(dim)
    return np.linalg.solve(QTQ, bQT)
