#!/usr/bin/env python3
"""module documentation
this module, creates a function:
    create_train_op.
    The function creates and returns
        operation that minimizes loss of a tensor set
Though classy, it has no class.

"""


import tensorflow.compat.v1 as tf


def create_train_op(loss, alpha):
    """creates an operation to minimize loss"""
    optimizer = tf.compat.v1.train.GradientDescentOptimizer(alpha)
    lossMinimizer = optimizer.minimize(loss)
    return lossMinimizer
