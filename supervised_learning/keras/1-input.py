#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    nx = number of input features to the network
    layers = list containing the number of nodes in each layer of network
    activations = list containing activation functions
        each index is the respective layer of the network
    lambtha = L2 regularization parameter
    keep_prob = probability that a node will be kept for dropout
    """
    X = K.Input(shape=(nx,))
