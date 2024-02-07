#!/usr/bin/env python3
"""module documentation
this module, 4-calculate_loss, creates a function:
    calculate_loss
Though classy, it has no class.

"""


import tensorflow.compat.v1 as tf


def calculate_loss(y, y_pred):
    """calculates loss via tensorflow's magical
    inbuilts.

    y is a placeholder for the labels of the input data
    y_pred is a tensor containing the network’s predictions
    Returns: a tensor containing the loss of the prediction
    """
    preMean = tf.nn.softmax_cross_entropy_with_logits(logits=y_pred, labels=y)
    loss = tf.math.reduce_mean(preMean)
    return loss
