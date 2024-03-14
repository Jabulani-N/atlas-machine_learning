#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K


def dense_block(X, nb_filters, growth_rate, layers):
    """
    builds a dense block as described in
        https://arxiv.org/pdf/1608.06993.pdf

    all weights use normal initialization
    all convolutions are precedied by
        Batch Nrmalization
        relu
    X = output from  previous layer
    nb_filters = integer number of filters in X
    growth_rate = growth rate for dense block
    layers = number of layers in dense block

    Returns:
        concatenated output of each layer within Dense Block
        number of filters within concatenated outputs
    """

    out = X
    for _ in range(layers):
        X = K.layers.BatchNormalization(axis=3)(out)
        X = K.layers.Activation('relu')(X)
        X = K.layers.Conv2D(4 * growth_rate, (1, 1), (1, 1),
                            padding='same',
                            kernel_initializer='he_normal')(X)

        X = K.layers.BatchNormalization(axis=3)(X)
        X = K.layers.Activation('relu')(X)
        X = K.layers.Conv2D(growth_rate, (3, 3),
                            padding='same',
                            kernel_initializer='he_normal')(X)

        X = K.layers.Concatenate(axis=3)([out, X])
        nb_filters += growth_rate

    return X, nb_filters
