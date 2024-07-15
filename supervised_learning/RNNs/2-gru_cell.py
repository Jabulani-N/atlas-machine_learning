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
        r = update gate = reset gate?
        h = intermediate hidden state = candidate?
        y = outputs
        """
        # random NORMAL distribution
        random = np.random.randn
        # I'll assume all gates use hidden state dimensions sized like in task0
        self.Wz = random(h + i, h)
        self.Wr = random(h + i, h)
        self.Wh = random(h + i, h)
        # output weights
        self.Wy = random(h, o)
        # biases
        self.bz = np.zeros((1, h))
        self.br = np.zeros((1, h))
        self.bh = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
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
        """
        # concatenating because our cell concatenates inputs and hidden layers
        catted_input = np.concatenate((h_prev, x_t), axis=1)
        # create reset, update gates respectively
        r = self.sigmoid(np.dot(catted_input, self.Wr) + self.br)
        z = self.sigmoid(np.dot(catted_input, self.Wz) + self.bz)
        # creating the candidate hidden state
        # prereq because we have concatenated input and hidden states
        catted_x_t_and_reset_times_h_prev = np.concatenate((r * h_prev, x_t),
                                                           axis=1)
        h_candidate = np.tanh(np.dot(catted_x_t_and_reset_times_h_prev,
                                     self.Wh)
                              + self.bh)
        # calculate official current hidden state
        h_next = z * h_candidate + (1 - z) * h_prev
        # calculate output based on hidden state
        # the below is the same as task 0's
        y = np.dot(h_next, self.Wy)  # this is broken part
        y += self.by
        y = self.softmax(y)
        return h_next, y

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
