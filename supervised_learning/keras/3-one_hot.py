#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K


def one_hot(labels, classes=None):
    """
    converts a list of labels (int)
    into a one-hot matrix
    """
    hottie = []
    class_count = len(labels)
    # initialize one-hot matrix with 0s
    for dim0 in range(class_count):
        hottie.append([])
        for dim1 in range(class_count):
            hottie[dim0].append(0)
        hottie[dim0][labels[dim0]] = 1
    return hottie
