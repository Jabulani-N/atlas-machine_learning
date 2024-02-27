#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K


def optimize_model(network, alpha, beta1, beta2):
    """network is the model to optimize
    alpha is the learning rate
    beta1 is the first Adam optimization parameter
    beta2 is the second Adam optimization parameter

    crossentropy loss
    accuracy metrics
    """
    optimizer = K.optimizers.Adam(learning_rate=alpha,
                            beta_1=beta1,
                            beta_2=beta2)
    network.compile(optimizer=optimizer, loss="crossentropy", metrics="accuracy")
