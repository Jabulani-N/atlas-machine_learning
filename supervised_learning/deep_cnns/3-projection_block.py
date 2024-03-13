#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K


def projection_block(A_prev, filters, s=2):
    """
    builds a projection block
        as described in https://arxiv.org/pdf/1512.03385.pdf
    """
    F11, F3, F12 = filters

    X_shortcut = K.layers.Conv2D(filters=F12, kernel_size=(1, 1), strides=(s, s), padding='valid', kernel_initializer='he_normal')(A_prev)
    X_shortcut = K.layers.BatchNormalization(axis=3)(X_shortcut)

    X = K.layers.Conv2D(filters=F11, kernel_size=(1, 1), strides=(s, s), padding='valid', kernel_initializer='he_normal')(A_prev)
    X = K.layers.BatchNormalization(axis=3)(X)
    X = K.layers.Activation('relu')(X)

    X = K.layers.Conv2D(filters=F3, kernel_size=(3, 3), strides=(1, 1), padding='same', kernel_initializer='he_normal')(X)
    X = K.layers.BatchNormalization(axis=3)(X)
    X = K.layers.Activation('relu')(X)

    X = K.layers.Conv2D(filters=F12, kernel_size=(1, 1), strides=(1, 1), padding='valid', kernel_initializer='he_normal')(X)
    X = K.layers.BatchNormalization(axis=3)(X)

    X = K.layers.Add()([X, X_shortcut])
    X = K.layers.Activation('relu')(X)

    return X
