#!/usr/bin/env python3
"""task 3"""

import numpy as np


def forward(Observation, Emission, Transition, Initial):
    """
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

    # once per observation
    for t in range(1, T):
        for j in range(N):
            F[j, t] = np.sum(F[:, t - 1] *
                             Transition[:, j]) *\
                      Emission[j, Observation[t]]

    P = np.sum(F[:, -1])

    return P, F
