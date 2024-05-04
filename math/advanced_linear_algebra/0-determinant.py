#!/usr/bin/env python3
"""module documentation
this module, 0-determinant.py, calculates a matrix's determinant
"""


def determinant(matrix):
    """matrix is list of lists"""
    if matrix == [[]]:
        return 1
    if type(matrix) is not list:
        raise TypeError("matrix must be a list of lists")
    for item in matrix:
        if type(item) is not list and\
           type(item) is not int:
            raise TypeError("matrix must be a list of lists")
    for item in matrix:
        if type(item) is list:
            if matrix_shape(item) != matrix_shape(matrix)[0]:
                raise ValueError("matrix must be a square matrix")
        elif matrix_shape(matrix)[0] != (1,):
            raise ValueError("matrix must be a square matrix")


def simple_det(submatrix):
    """returns determinent of 2x2 matrix"""
    if matrix_shape(submatrix) == (2, 2):
        det = (submatrix[0][0] * submatrix[1][1]) -\
              (submatrix[0][1] * submatrix[1][0])
        return det
    return 0


def matrix_shape(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    return rows, cols
