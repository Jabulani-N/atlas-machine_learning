#!/usr/bin/env python3
"""module documentation
this module, 8-neural_network.py, creates a class: NeuralNetwork

"""

import numpy as np


class NeuralNetwork:
    """Object-class summary documentation.

    Attributes:
        W1 - weights vector for hidden layer
        b1 - bias of hidden layer.
        A1 - output of hidden layer.
        W2 - weights vector for output neuron
        b2 - bias of output neuron.
        A2 - output of output neuron.

    """

    def __init__(self, nx, nodes):
        """nx = no of input features
        nodes = no of nodes in hidden layer
        """

        if isinstance(nx, int) is False:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        if isinstance(nodes, int) is False:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.W1 = np.random.normal(size=(1, nx))
        self.b1 = np.zeros((nodes, 1))
        self.A1 = 0
        self.W2 = np.random.normal(size=(1, nx))
        self.b2 = 0
        self.A2 = 0
