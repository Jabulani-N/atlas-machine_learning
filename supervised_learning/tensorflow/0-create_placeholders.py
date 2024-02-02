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
    y = placeholderfor one-hot labels
    """
    x = nx
    y = classes
    return x, y
