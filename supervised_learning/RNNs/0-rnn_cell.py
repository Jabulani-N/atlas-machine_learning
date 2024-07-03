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
        """simulates a forward propagation pass"""
        # concatenating because our cell concatenates inputs and hidden layers
        # print("shapes:", np.shape(h_prev), np.shape(x_t))
        catted_input = np.concatenate((h_prev, x_t), axis=1)
        # this will only be a single time step
        # so we'll only use the part protected by the source's loop
        # the basic idea is tanh(dot product of (input, weights)
        h_next = np.tanh(np.dot(catted_input, self.Wh) + self.bh)
        # this is output without an activation function
        y = np.dot(h_next, self.Wy)
        # this is output after softmax activation function
        y = self.softmax(y) + self.by
        return h_next, y

    @staticmethod
    def softmax(x, axis=-1):
        """calculates softmax of x"""
        # Subtracting max(x) for numerical stability
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=axis, keepdims=True)
