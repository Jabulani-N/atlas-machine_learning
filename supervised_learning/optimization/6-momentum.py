#!/usr/bin/env python3
"""module documentation
this module creates a function.

"""


import tensorflow as tf


def create_momentum_op(loss, alpha, beta1):
    """loss is the loss of the network
alpha is the learning rate
beta1 is the momentum weight
Returns: the momentum optimization operation
"""
    return (tf.keras.optimizers.SGD(learning_rate=alpha, momentum=beta1)).minimize(loss)
