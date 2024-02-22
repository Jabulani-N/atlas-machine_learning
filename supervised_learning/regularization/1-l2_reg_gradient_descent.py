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
    # backpropagation
    for layer_num in range(L, 0, -1):
        A_prev = cache["A" + str(layer_num - 1)]
        # we don't have to initialize this because we're starting at the end
        #   and never going to alter position 0, which is input
        dW = (1 / m) * np.dot(dz, A_prev.T) +\
            (lambtha / m) * weights["W" + str(layer_num)]
        # same as how we used to do backprop, but adding L2 regularization
        db = (1 / m) * np.sum(dz, axis=1, keepdims=True)
        dA_prev = np.dot(weights["W" + str(layer_num)].T, dz)
        weights["W" + str(layer_num)] -= alpha * dW
        weights["b" + str(layer_num)] -= alpha * db
        if layer_num > 1:
            dz = dA_prev * (1 - np.power(A_prev, 2))
    return weights
