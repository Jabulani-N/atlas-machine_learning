#!/usr/bin/env python3
"""this module creates a function."""


import numpy as np


def dropout_forward_prop(X, weights, L, keep_prob):
    """
    X = numpy.ndarray of input data
        shape (nx, m)
            nx is the number of input features
            m is the number of data points
    weights = dictionary of the weights and biases of the neural network
    L = number of layers in the network
    keep_prob = probability that a node will be kept
    """
    cache = {}
    Activation = X
    dropout_masks = {}
