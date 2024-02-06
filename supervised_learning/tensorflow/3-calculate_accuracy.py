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
    returns accuracy percentage:
        number of correct predcitions / total predictions
    """

    return tf.divide(tf.math.reduce_sum(
            tf.cast(tf.math.equal(y, y_pred),
                    tf.float32)),
                     tf.cast(tf.size(y), tf.float32))
