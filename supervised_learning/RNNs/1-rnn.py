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
    # Y = np.empty(0)
    # Y = np.zeros(np.shape(X))
    for time_step in range(np.shape(X)[0] - 1):
        h_next, output_next = rnn_cell.forward(h_prev, X[time_step])
        H = np.append(H, h_next, axis=0)
        # make sure Y is the right shape for the outputs
        if time_step == 0:
            Y = np.zeros((np.shape(X)[0],
                          np.shape(output_next)[0],
                          np.shape(output_next)[1]))
        # print("Y is", Y, "before appednding the output:", output_next)
        # print("output shape", np.shape(output_next))
        # Y = np.append(Y, output_next, axis=0)
        Y[time_step] = np.copy(output_next)
        # print("after appending, Y is", Y)
        h_prev = h_next
    # Y = np.reshape(Y, np.shape(X))
    return H, Y
