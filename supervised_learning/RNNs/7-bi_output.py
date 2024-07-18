#!/usr/bin/env python3
"""
This module creates the class BidirectionalCell
this is an update to task 6
"""

import numpy as np


class BidirectionalCell:
    """simulates a bidirectional cell of an RNN"""
    def __init__(self, i, h, o):
        """
        initiates the class
        i, h, o = dimensionality of
            input data
            hidden state
            outputs

        hf = hidden state forward
        hb = hidden state backward
        y = outputs
        """
        # random NORMAL distribution
        random = np.random.randn
        # establish non-output weights
        self.Whf = random(h + i, h)
        self.Whb = random(h + i, h)
        # output weights
        # doubled h for forward and backward directions
        self.Wy = random(2 * h, o)
        # biases
        self.bhf = np.zeros((1, h))
        self.bhb = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """
        simulates one time step of forward propagation

        h_prev = previous hidden layer
            shape = (m, h)
                m = batch size of data
                h = dimensionality of hidden state
        x_t = data input
            shape = (m, i)
                m = batch size of data
                i = dimensionality of input
        """
        # this is essentially taken from task 0
        catted_input = np.concatenate((h_prev, x_t), axis=1)
        h_next = np.tanh(np.dot(catted_input, self.Whf) + self.bhf)
        return h_next

    def backward(self, h_next, x_t):
        """
        simulates one time step of backward propagation

        h_next = next hidden layer state
            shape = (m, h)
                m = batch size of data
                h = dimensionality of hidden state
        x_t = data input
            shape = (m, i)
                m = batch size of data
                i = dimensionality of input
        """
        # this is essentially just reversing task 5
        catted_input = np.concatenate((h_next, x_t), axis=1)
        h_prev = np.tanh(np.dot(catted_input, self.Whb) + self.bhb)
        return h_prev

    def output(self, H):
        """
        calculates output y
        H = concatenated h_next and h_prev
            from forward and backward
            shape = (t, m, 2 * h)
                t = time steps done
                m = batch size of data
                h = dimensionality of hidden states
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
