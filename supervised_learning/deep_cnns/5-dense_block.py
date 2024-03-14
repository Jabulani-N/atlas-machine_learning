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
    """
    concatenated_outputs = [X]
    for _ in range(layers):
        X = K.layers.BatchNormalization(axis=3)(X)
        X = K.layers.Activation('relu')(X)
        X = K.layers.Conv2D(filters=4 * growth_rate, kernel_size=(1, 1), strides=(1, 1), padding='same', kernel_initializer='he_normal')(X)

        X = K.layers.BatchNormalization(axis=3)(X)
        X = K.layers.Activation('relu')(X)
        X = K.layers.Conv2D(filters=growth_rate, kernel_size=(3, 3), strides=(1, 1), padding='same', kernel_initializer='he_normal')(X)

        concatenated_outputs.append(X)
        X = K.layers.Concatenate(axis=3)(concatenated_outputs)
        nb_filters += growth_rate

    return X, nb_filters
