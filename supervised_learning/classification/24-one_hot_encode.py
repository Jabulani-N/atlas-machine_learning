#!/usr/bin/env python3
"""this module contains a function
one hot encode that converts from an aray of categories to
an array of 'is it category 1? is it category 2?...'
"""

import numpy as np


def one_hot_encode(Y, classes):
    """binarizes an array Y
    Y = array of class numbers (int)
    classes = number of classes within Y
        seems to be the length of Y
    """

    biggestPossibleClassNumber = max(Y)
    parent = np.zeros((classes, len(Y)))

    for numberCheckedFor in range(0, biggestPossibleClassNumber + 1):
        parent[numberCheckedFor] = \
            np.equal(Y, numberCheckedFor)
    return parent
