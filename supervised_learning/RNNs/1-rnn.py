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
    h_0 = initial hidden state
    """
    H = np.copy(h_0)
    h_next, output = rnn_cell.forward(h_0, X)
    H.append(h_next)
    return H, output
