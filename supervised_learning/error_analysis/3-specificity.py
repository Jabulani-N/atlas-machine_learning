#!/usr/bin/env python3
"""module documentation
this module creates a function.

This is essenitally the inverse of task 1: sensitivity
instead of positives, we're working with negatives"""


import numpy as np


def specificity(confusion):
    """does the same idea as task 1
        except this time, we subtract the true
        negatives from the whole thing.

        This could also be done via inverting the
        confusion matrix by changing every cell to
        cell_val = total - cell_val
        we're basically doing that anyway, but in fewer steps."""
    classes = confusion.shape[0]
    specty = np.zeros(classes)

    for class_num in range(classes):
        true_negatives = np.sum(confusion) -\
            np.sum(confusion[class_num, :]) -\
            np.sum(confusion[:, class_num]) +\
                confusion[class_num, class_num]
        actual_negatives = np.sum(confusion) - np.sum(confusion[class_num, :])
        if actual_negatives != 0:
            specty[class_num] =\
                true_negatives / actual_negatives
    return specty
