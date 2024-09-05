#!/usr/bin/env python3
"""returns a gym environment attirbute"""

import numpy as np


def epsilon_greedy(Q, state, epsilon):
    """
    Q = numpy.ndarray containing q-table
    state = current state
        int
    epsilon = epsilon used for  calculation
    returns action_index
        int
    """
    # clarity
    qtable = Q
    _, act_count = np.shape(qtable)
    state_row = qtable[state]

    greed = np.random.uniform(0.0, 1.0) < epsilon
    if greed:
        return greed_is_good(act_count)
    else:
        return exploiter_orb(state_row)


def greed_is_good(act_count):
    """
    recieves a state
    returns greed route (randomly take a path)
        aka explore
    """
    return np.random.randint(0, act_count)


def exploiter_orb(state_row):
    """
    recieves a state row
        of a qtable
    returns exploit route
        = index of highest known reward
    """
    return np.argmax(state_row)
