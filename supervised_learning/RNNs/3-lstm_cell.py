#!/usr/bin/env python3
"""
This module creates the class LSTMCell
This class illustrates the function of
a Gated Recurrant  Network
"""

import numpy as np


class LSTMCell:
    """simulates an Long Short-term Memort unit"""
    def __init__(self, i, h, o):
        """initiates the class
        i, h, o = dimensionality of
            input data
            hidden state
            outputs

        f = forget gate
        u = update gate
        c = intermediate cell state
        o = output gate
        y = outputs
        """
        # random NORMAL distribution
        random = np.random.randn
        # establish non-output weights
        self.Wf = random(h + i, h)
        self.Wu = random(h + i, h)
        self.Wc = random(h + i, h)
        self.Wo = random(h + i, h)
        # output weights
        self.Wy = random(h, o)
        # biases
        self.bf = random(h + i, h)
        self.bu = random(h + i, h)
        self.bc = random(h + i, h)
        self.bo = random(h + i, h)
        self.by = random(h, o)

    def forward(self, h_prev, c_prev, x_t):
        """
        simulates one time step of forward propagation
        h_prev = previous hidden layer
            shape (m, i)
                m = batch size for data
                i = dimentionality of data
        x_t = input data
            shape (m, h)
                m = batch size for data
                h = dimensionality of hidden state
        c_prev = previous cell state
            shape (m, h)
                m = batch size for data
                h = dimensionality of hidden state
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
        return 1 / (1 + np.exp(-x))
