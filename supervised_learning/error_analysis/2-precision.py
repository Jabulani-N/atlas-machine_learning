#!/usr/bin/env python3
"""module documentation
this module creates a function.

This module is largely copied from the sensitivity function
as the mathematic processes is extremely similar.
"""


import numpy as np


def precision(confusion):
    """
    confusion = confusion numpy.ndarray
        shape (classes, classes)
            classes = number of classes
        row indices = correct labels
        column indices = predicted labels
        As a reminder:
            True Positive = correctly guessed positive
    """
    classes = confusion.shape[0]
    prec = np.zeros(classes)

    for class_num in range(classes):
        true_positives = confusion[class_num, class_num]
        pred_positives = np.sum(confusion[:, class_num])
        if pred_positives != 0:
            prec[class_num] =\
                true_positives / pred_positives
    return prec
