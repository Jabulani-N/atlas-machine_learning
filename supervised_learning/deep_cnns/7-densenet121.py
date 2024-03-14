#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K
dense_block = __import__('5-dense_block').dense_block
transition_layer = __import__('6-transition_layer').transition_layer


def densenet121(growth_rate=32, compression=1.0):
    """placeholder doc"""
    inputs = K.Input(shape=(224, 224, 3))
    nb_filters = 64

    X = K.layers.Conv2D(filters=nb_filters, kernel_size=(7, 7),
                        strides=(2, 2), padding='same',
                        kernel_initializer='he_normal')(inputs)
    X = K.layers.BatchNormalization(axis=3)(X)
    X = K.layers.Activation('relu')(X)
    X = K.layers.MaxPooling2D(pool_size=(3, 3),
                              strides=(2, 2),
                              padding='same')(X)

    X, nb_filters = dense_block(X, nb_filters, growth_rate, 6)
    X, nb_filters = transition_layer(X, nb_filters, compression)
    X, nb_filters = dense_block(X, nb_filters, growth_rate, 12)
    X, nb_filters = transition_layer(X, nb_filters, compression)
    X, nb_filters = dense_block(X, nb_filters, growth_rate, 24)
    X, nb_filters = transition_layer(X, nb_filters, compression)
    X, nb_filters = dense_block(X, nb_filters, growth_rate, 16)

    X = K.layers.GlobalAveragePooling2D()(X)
    outputs = K.layers.Dense(1000, activation='softmax')(X)

    model = K.Model(inputs=inputs, outputs=outputs, name='densenet121')
    return model
