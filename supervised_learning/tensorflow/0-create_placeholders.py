#!/usr/bin/env python3
"""module documentation
this module,0-create_placeholders, creates a function:
    create_placeholders
Though classy, it has no class.

"""


import tensorflow.compat.v1 as tf


def create_placeholders(nx, classes):
    """returns two placeholders for the neural network
    nx: the number of feature columns in our data
    classes: the number of classes in our classifier

    x = placeholder for input data
    y = placeholder for one-hot labels

    placeholder: Tensorflow class
    """
    x = tf.placeholder(tf.float32, nx, 'x:0')
    y = tf.placeholder(tf.float32, classes, 'y:0')
    return x, y
