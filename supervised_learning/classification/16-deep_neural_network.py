#!/usr/bin/env python3
"""module documentation
this module, 16-deep_neural_network.py,
creates a class: DeepNeuralNetwork

"""

import numpy as np


class DeepNeuralNetwork:
    """Object-class summary documentation.

    Attributes:
        L - number of layers
        cache - dictionary holding intermediary values. initialized empty.
        weights - dictionary holding weights and biases.

    """

    def __init__(self, nx, layers):
        """nx = no of input features
        layers = list containing no of nodes in each layer
        """

        if isinstance(nx, int) is False:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        if isinstance(layers, list) is False or layers == []:
            raise TypeError("layers must be a list of positive integers")
        if all(np.greater_equal(layers, 1)) is False:
            raise TypeError("layers must be a list of positive integers")

        self.L = len(layers)
        self.cache = {}
        self.weights = {}

        for layer in range(0, self.L + 1):
            if isinstance(layers[layer], int) is False:
                raise TypeError("layers must be a list of positive integers")
            self.weights['W' + str(layer + 1)] = \
                np.random.randn(layers[layer - 0],
                                layers[layer - 1]) *\
                np.sqrt(2. / layers[layer - 1])

            if layer == 0:
                self.weights['W' + str(layer + 1)] = \
                    np.random.randn(layers[layer], nx) *\
                    np.sqrt(2. / nx)
            self.weights['b' + str(layer + 1)] = \
                np.zeros((layers[layer - 0], 1))
        # weights initialized via he et al.
