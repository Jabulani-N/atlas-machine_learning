#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K


def dense_block(X, nb_filters, growth_rate, layers):
    """
    builds a denseblock as described in
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

    for layerNum in range(layers):
        out = K.layers.BatchNormalization()(X)
        out = K.layers.Activation('relu')(out)
        out = K.layers.Conv2D(filters=4 * growth_rate,
                            kernel_size=(1, 1), strides=(1, 1),
                            kernel_initializer='he_normal')(out)

        out = K.layers.BatchNormalization()(out)
        out = K.layers.Activation('relu')(out)
        out = K.layers.Conv2D(filters=growth_rate,
                            kernel_size=(3, 3), strides=(1, 1),
                            padding='same', kernel_initializer='he_normal')(X)

        X = K.layers.Concatenate([X, out])

        nb_filters += growth_rate

    return X, nb_filters
