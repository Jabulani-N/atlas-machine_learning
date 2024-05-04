#!/usr/bin/env python3
"""module documentation
this module, 0-determinant.py, calculates a matrix's determinant
"""
import numpy as np


def determinant(matrix):
    """content"""
    pass


def simple_det(submatrix):
    """returns determinent of 2x2 matrix"""
    if np.shape(submatrix) == (2, 2):
        det = (submatrix[0][0] * submatrix[1][1]) -\
              (submatrix[0][1] * submatrix[1][0])
        return det
    return 0
