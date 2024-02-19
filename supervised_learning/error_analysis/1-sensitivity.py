#!/usr/bin/env python3
"""module documentation
this module creates a function.

"""


import numpy as np


def sensitivity(confusion):
    """
    confusion = confusion numpy.ndarray
        shape (classes, classes)
            classes = number of classes
        row indices = correct labels
        column indices = predicted labels
        As a reminder:
            True Positive = correctly guessed positive
            Actual Positive = answer sheet says positive
    """
    classes = confusion.shape[0]
    Only_Sense_Online = np.zeros(classes)

    for class_num in range(classes):
        true_positives = confusion[class_num, class_num]
        actual_positives = np.sum(confusion[class_num, :])
        if actual_positives != 0:
            Only_Sense_Online[class_num] =\
                true_positives / actual_positives
    return Only_Sense_Online
