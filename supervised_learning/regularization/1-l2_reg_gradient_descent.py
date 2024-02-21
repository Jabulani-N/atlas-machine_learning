#!/usr/bin/env python3
"""this module creates a function."""


import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """
    Y = one-hot numpy.ndarray
        shape (classes, m)
        contains the correct labels for the data
    classes = number of classes
    m = number of data points
    weights = dictionary of the weights and biases of the neural network
    cache = dictionary of the outputs of each layer of the neural network
    alpha = learning rate
    lambtha = L2 regularization parameter
    L = number of layers of the network
    use tanh activations on each layer
        except the last, which uses a softmax activation
    """
    classes, m = np.shape(Y)
    dz = cache["A" + str(L)] - Y
    # dz = cost of last activation slot
    # Remember from the previous weeks that cache[A0] is input
    #   so each layer is naturally enumerated (layer 1 = cache[A1])
