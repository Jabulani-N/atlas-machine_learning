#!/usr/bin/env python3
"""task 4"""

import numpy as np


def viterbi(Observation, Emission, Transition, Initial):
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
    T = Observation.shape[0]
    N = Transition.shape[0]
    path = []
    delta = np.zeros((N, T))
    psi = np.zeros((N, T))

    # Initialization
    delta[:, 0] = Initial.flatten() * Emission[:, Observation[0]]

    # once per observation
    for t in range(1, T):
        for j in range(N):
            delta[j, t] = np.max(delta[:, t - 1] * Transition[:, j]) *\
                          Emission[j, Observation[t]]
            psi[j, t] = np.argmax(delta[:, t - 1] * Transition[:, j])

    P = np.max(delta[:, -1])
    path.insert(0, np.argmax(delta[:, -1]))

    # Backtracking
    for t in range(T - 2, -1, -1):
        path.insert(0, int(psi[path[0], t + 1]))

    return path, P
