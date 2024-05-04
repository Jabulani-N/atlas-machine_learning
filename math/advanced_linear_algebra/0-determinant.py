#!/usr/bin/env python3
"""module documentation
this module, 0-determinant.py, calculates a matrix's determinant
"""
import numpy as np


def determinant(matrix):
    """matrix is list of lists"""
    if type(matrix) is not list or\
    type(matrix[0]) is not list:
        raise TypeError("matrix must be a list of lists")
    if np.shape(matrix)[0] != np.shape(matrix)[1]:
        raise ValueError("matrix must be a square matrix")
    if matrix == [[]]:
        return 1


def simple_det(submatrix):
    """returns determinent of 2x2 matrix"""
    if np.shape(submatrix) == (2, 2):
        det = (submatrix[0][0] * submatrix[1][1]) -\
              (submatrix[0][1] * submatrix[1][0])
        return det
    return 0
