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
        if all(np.greater_equal(layers, 1)) is False or\
           all(isinstance(item, int) for item in layers) is False:
            raise ValueError("layers must be a list of positive integers")

        layerCount = len(layers)
        cache = {}
        weights = {}

        for layer in range(1, layerCount + 1):
            weights['W' + str(layer)] = \
                np.random.randn(layers[layer],
                                layers[layer - 1]) * \
                np.sqrt(2. / layers[layer - 1])
            weights['b' + str(layer)] = np.zeros((layers[layer], 1))
        # weights has now been initialized using he et al.
