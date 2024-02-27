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
    regularizer = K.regularizers.l2(lambtha)
    layerCount = len(layers)

    # First layer
    if layerCount != 1:
        layer = K.layers.Dense(layers[0],
                               activation=activations[0],
                               kernel_regularizer=regularizer)(X)
        layer = K.layers.Dropout(1 - keep_prob)(layer)
    else:
        layer = K.layers.Dense(layers[0],
                               activation=activations[0],
                               kernel_regularizer=regularizer)(X)

    # Other layers
    for i in range(1, layerCount):
        layer = K.layers.Dense(layers[i],
                               activation=activations[i],
                               kernel_regularizer=regularizer)(layer)
        if i < len(layers) - 1:
            layer = K.layers.Dropout(1 - keep_prob)(layer)

    model = K.Model(inputs=X, outputs=layer)
    return model
