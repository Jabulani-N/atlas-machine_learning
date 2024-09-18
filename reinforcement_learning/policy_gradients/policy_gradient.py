#!/usr/bin/env python3
"""computes the policy with a weight of a matrix"""

import numpy as np


def policy(matrix, weight):
    """
    computes the policy with a weight of a matrix
        softmaxes the dot of matrix with weight

    input info pulled from the subsequent task
    matrix = input matrix
    weight = matrix input policy
    """
    return matrix_softmax(weight, matrix)


def softmax(z):
    """
    based on a previous project
    calculate softmax of an array
    """
    # Subtract the maximum value for numerical stability
    exp_z = np.exp(z - np.max(z, axis=-1, keepdims=True))
    return exp_z / exp_z.sum(axis=-1, keepdims=True)


def matrix_softmax(the_list, the_matrix, bias=0):
    """
    helps softmax function
        lets us just directly plug in a matrix and list
    bias exists as a 'just in case'
    """
    return softmax(np.dot(the_matrix, the_list) + bias)
