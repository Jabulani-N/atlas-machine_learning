#!/usr/bin/env python3
"""module documentation
this module,0-create_placeholders, creates a function:
    create_placeholders
Though classy, it has no class.

"""

import numpy as np


class RNNCell:
    """simulates/reprecents a cell of simple RNN"""
    def __init__(self, i, h, o):
        """
        class initiator
        i, h, o = dimensionality of:
            input, hidden state, output
        """
        # random NORMAL distribution
        random = np.random.randn
        # weights of the cell
        # hidden later and input are concatenated here per client request
        self.Wh = random(h + i, h)
        self.Wy = random(h, o)
        # biases of the cell
        self.bh = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """simulates a forward pass"""
        outputs = []
        # concatenating these because our cell concatenates inputs and hidden layers
        catted_input = np.concatenate(x_t, h_prev)
        # this will only be a single time step
        # so we'll only use the part protected by the source's loop
        h_next = np.tanh(np.dot(self.Wh, catted_input) + np.dot(self.bh))
        y = np.dot(self.Wy, h_next) + self.by
        return h_next, y

    @staticmethod
    def softmax(x, axis=-1):
        """calculates softmax of x"""
        # Subtracting max(x) for numerical stability
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=axis, keepdims=True)
