#!/usr/bin/env python3
"""module documentation
this module, 3-calculate_accuracy, creates a function:
    calculate_accuracy
Though classy, it has no class.

"""


import tensorflow.compat.v1 as tf


def calculate_accuracy(y, y_pred):
    """returns tensor of accuracy
    y is a placeholder for the labels of the input data
    y_pred is a tensor containing the network’s predictions
    """

    return tf.divide(y, y_pred)
