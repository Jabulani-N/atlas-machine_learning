#!/usr/bin/env python3
"""module documentation
this module creates a function.

"""


import numpy as np


def create_confusion_matrix(labels, logits):
    """
    labels = one-hot numpy.ndarray
        shape (m, classes) containing correct labels
        m = number of data points
        classes = number of classes
    logits = one-hot numpy.ndarray
    shape (m, classes) containing predicted labels
    Return confusion
        numpy.ndarray shape (classes, classes)
            row indices represent correct labels
            column indices represent predicted labels
    """
    m, classes = np.shape(labels)
    confusion = np.zeros((classes, classes))
    for cls_pos in range(m):
        act_cls_number = np.argmax(labels[cls_pos])
        pred_cls_number = np.argmax(logits[cls_pos])
        confusion[act_cls_number][pred_cls_number] += 1
    return confusion
