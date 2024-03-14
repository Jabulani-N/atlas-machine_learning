#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K


def transition_layer(X, nb_filters, compression):
    """
    builds a transition layer as described
        https://arxiv.org/pdf/1608.06993.pdf
    X is the output from the previous layer
    nb_filters is an integer representing the number of filters in X
    compression is the compression factor for the transition layer
    Your code should implement compression as used in DenseNet-C
    All weights should use he normal initialization
    All convolutions preceded by
        Batch Normalization
        relu
    Returns:
    output of the transition layer
    number of filters within the output
    """
    X = K.layers.BatchNormalization(axis=3)(X)
    X = K.layers.Activation('relu')(X)
    nb_filters = int(nb_filters * compression)
    X = K.layers.Conv2D(filters=nb_filters,
                        kernel_size=(1, 1),
                        strides=(1, 1),
                        padding='same',
                        kernel_initializer='he_normal')(X)
    X = K.layers.AveragePooling2D(pool_size=(2, 2), strides=(2, 2))(X)
    return X, nb_filters
