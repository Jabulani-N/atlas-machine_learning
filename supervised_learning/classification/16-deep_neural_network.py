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

    """

    def __init__(self, nx, layers):
        """nx = no of input features
        nodes = no of nodes in hidden layer
        """

        if isinstance(nx, int) is False:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        if isinstance(layers, int) is False:
            raise TypeError("layers must be an integer")
        if layers < 1:
            raise ValueError("layers must be a positive integer")
