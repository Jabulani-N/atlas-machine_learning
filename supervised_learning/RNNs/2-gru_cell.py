#!/usr/bin/env python3
"""
This module creates the class GRUCell
This class illustrates the function of
a Gated Recurrant  Network
"""

import numpy as np


class GRUCell:
    """simulates a gated ecurrant network"""
    def __init__(self, i, h, o):
        """initiates the class
        i, h, o = dimensionality of
            input data
            hiden state
            outputs
        w = weights
        b = bias

        z = forget gate
        r = update gate
        h = intermediate hidden state
        y = outputs
        """
        # random NORMAL distribution
        random = np.random.randn
        # I'll assume all gates use hidden state dimensions sized like in task0
        self.Wz = random(h + i, h)
        self.Wr = random(h + i, h)
        self.Wh = random(h + i, h)
        # output weights
        self.Wy = random(o, h)
        # biases
        self.bz = np.zeros((1, h))
        self.br = np.zeros((1, h))
        self.bh = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """
        simulates one time step of forward propagation
        """
        pass

    @staticmethod
    def softmax(x, axis=-1):
        """calculates softmax of x"""
        # Subtracting max(x) for numerical stability
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=axis, keepdims=True)

    @staticmethod
    def sigmoid(x):
        """calculates sigmoid of x"""
        # Subtracting max(x) for numerical stability
        e_x = np.exp(x - np.max(x))
        return (1.0 + np.exp(-e_x)) ** -1
