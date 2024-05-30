#!/usr/bin/env python3
"""task 5"""

import numpy as np


def backward(Observation, Emission, Transition, Initial):
    """
    same variables as previous

    Observation = numpy.ndarray
        shape (T,)
            T = number of observations
        contains the index of the observation
    Emission = numpy.ndarray
        shape (N, M)
            N = number of hidden states
            M = number of all possible observations
        containing emission probability of
            specific observation given a hidden state
        Emission[i, j] = probability of observing j given the hidden state i
    Transition = 2D numpy.ndarray
        shape (N, N)
        containing the transition probabilities
        Transition[i, j] = probability of transitioning hidden state i to j
    Initial = numpy.ndarray
        shape (N, 1)
        containing the probability of starting in a particular hidden state
    """
    pass
