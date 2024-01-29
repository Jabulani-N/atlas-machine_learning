#!/usr/bin/env python3
"""module documentation
this module, 9-neural_network.py, creates a class: NeuralNetwork

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

        self.__W1 = np.random.normal(size=(nodes, nx))
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.normal(size=(1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """returns weights of hidden layer inputs"""
        return self.__W1

    @property
    def W2(self):
        """returns weights of output layer inputs"""
        return self.__W2

    @property
    def W1(self):
        """returns weights of hidden layer inputs"""
        return self.__W1

    @property
    def b1(self):
        """returns biases of each hidden layer node as array of arrays"""
        return self.__b1

    @property
    def b2(self):
        """returns bias of output node"""
        return self.__b2

    @property
    def A1(self):
        """returns prediction (output) of hidden layer"""
        return self.__A1

    @property
    def A2(self):
        """returns prediction output node"""
        return self.__A2