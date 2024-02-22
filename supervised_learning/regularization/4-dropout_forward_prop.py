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

    Last layer uses softmax activation function
    """
    cache = {"A0": X}  # will hold all outputs and dropout masks
    Activation = X
    for layer in range(1, L):  # excludes last layer
        W = weights["W" + str(layer)]
        b = weights["b" + str(layer)]
        Z = np.dot(W, Activation) + b
        Activation = np.tanh(Z)
        D = np.random.rand(Activation.shape[0], Activation.shape[1])
        D = (D < keep_prob)
        Activation = np.multiply(Activation[0], D)
        Activation = Activation / keep_prob
        cache["Z" + str(layer)] = Z
        cache["A" + str(layer)] = Activation
        cache["D" + str(layer)] = D.astype(int)

    # Last layer softmax
    W = weights["W" + str(L)]
    b = weights["b" + str(L)]
    Z = np.dot(W, Activation) + b
    Activation = np.exp(Z) / np.sum(np.exp(Z), axis=0)
    return cache
