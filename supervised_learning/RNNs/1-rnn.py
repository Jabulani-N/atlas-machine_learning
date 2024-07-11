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
    h_prev = np.copy(h_0)
    for time_step in range(np.shape(X)[0]):
        h_next, output_next = rnn_cell.forward(h_prev, X[time_step])
        # make sure H, Y are correct shape for the outputs
        if time_step == 0:
            # each time step contains an output_next
            Y = np.zeros((np.shape(X)[0],
                          np.shape(output_next)[0],
                          np.shape(output_next)[1]))
            # each time step contains an h_{time_step}
            H = np.zeros((np.shape(X)[0] + 1,
                         np.shape(h_0)[0],
                         np.shape(h_0)[1]))
            H[0] = np.copy(h_0)
        # we preserve h_0 data this way
        H[time_step + 1] = h_next
        Y[time_step] = np.copy(output_next)
        h_prev = h_next
    return H, Y
