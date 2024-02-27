#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K


def one_hot(labels, classes=None):
    """
    converts a list of labels (int)
    into a one-hot matrix
    """
    hottie = K.utils.to_categorical(labels,
                                    num_classes=classes,
                                    dtype='float32')
    return hottie
