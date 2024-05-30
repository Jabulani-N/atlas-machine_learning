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
    # from instructions
    T = Observation.shape[0]
    N = Transition.shape[0]
    # Initialize the forward path probabilities matrix
    F = np.zeros((N, T))

    # Initialization
    F[:, 0] = Initial.flatten() * Emission[:, Observation[0]]

    F[:, -1] = 1

    # Recursion
    for t in range(T - 2, -1, -1):
        for i in range(N):
            F[i, t] = np.sum(F[:, t + 1] *
                             Transition[i, :] *
                             Emission[:, Observation[t + 1]])

    # Termination
    P = np.sum(Initial.flatten() * Emission[:, Observation[0]] * F[:, 0])
    return P, F
