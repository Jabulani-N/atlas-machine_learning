#!/usr/bin/env python3
"""module documentation
this module, 8-neural_network.py, creates a class: NeuralNetwork

"""

import numpy as np


class Neuron:
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
        """initialization documentation"""