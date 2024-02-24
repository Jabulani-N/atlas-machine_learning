#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    nx = number of input features to the network
    layers = list containing number of nodes in each layer
    activations = list containing activation functions used for each layer
    lambtha = L2 regularization parameter
    keep_prob = probability that a node will be kept for dropout
    """
    model = K.models.Sequential()

    for i in range(len(layers)):
        if i == 0:
            model.add(K.layers.Dense(layers[i],
                      input_dim=nx, activation=activations[i],
                      kernel_regularizer=K.regularizers.l2(lambtha)))
        else:
            model.add(K.layers.Dense(layers[i],
                      activation=activations[i],
                      kernel_regularizer=K.regularizers.l2(lambtha)))
        if i < len(layers) - 1:
            model.add(K.layers.Dropout(1 - keep_prob))

    return model
