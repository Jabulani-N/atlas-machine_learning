#!/usr/bin/env python3
"""module documentation
this module creates a function.

"""


import tensorflow.compat.v1 as tf


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """loss is the loss of the network
alpha is the learning rate
beta2 is the RMSProp weight
epsilon is a small number to avoid division by zero
"""
    optimizer = tf.keras.optimizers.RMSprop(alpha, beta2, epsilon)
    rmsprop_operation = optimizer.minimize(loss)
    return rmsprop_operation
