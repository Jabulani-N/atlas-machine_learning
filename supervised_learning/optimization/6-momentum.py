#!/usr/bin/env python3
"""module documentation
this module creates a function.

"""


import tensorflow.compat.v1 as tf


def create_momentum_op(loss, alpha, beta1):
    """loss is the loss of the network
alpha is the learning rate
beta1 is the momentum weight
Returns: the momentum optimization operation
"""
    optimizer = tf.keras.optimizers.SGD(learning_rate=alpha,
                                        momentum=beta1)
    return optimizer.minimize(loss)
