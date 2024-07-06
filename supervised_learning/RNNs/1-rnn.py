#!/usr/bin/env python3
"""
basically runs a single forward prop method
    of the class we defined in task 0
"""

import numpy as np


def rnn(rnn_cell, X, h_0):
    """
    rnn_cell = already created RNN_Cell class object
        see previous task for attribute explanation
    X = input data
        shape: (t, m, i)
    h_0 = initial hidden state
        shape: (m, h)
    """
    H = np.copy(h_0)
    h_prev = np.copy(h_0)
    Y = np.empty(0)
    for time_step in range(np.shape(X)[0] - 1):
        h_next, output_next = rnn_cell.forward(h_prev, X[time_step])
        H = np.append(H, h_next)
        Y = np.append(Y, output_next)
        h_prev = h_next
    return H, np.asarray(Y)
