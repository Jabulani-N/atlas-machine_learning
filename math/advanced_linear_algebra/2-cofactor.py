#!/usr/bin/env python3
"""module documentation
this module, 2-cofactor.py
calculates the cofactor matrix of matrix matrix
copies task 1's code so all that's needed is assigning the sign to each cell
"""


def cofactor(matrix):
    """calculates cofactor of matrix matrix"""
    underage = minor(matrix)
    length = len(matrix)
    cof = zerosquare(length)
    for rowNum in range(length):
        for colNum in range(length):
            x = colNum + 1
            y = rowNum + 1
            cof[rowNum][colNum] = underage[rowNum][colNum] *\
                                  (-1) ** (x + y)
    return cof


def minor(matrix):
    """calculates the minor of matrix"""
    # preliminary validity checks
    if matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")
    if type(matrix) is not list or\
       matrix == []:
        raise TypeError("matrix must be a list of lists")
    for item in matrix:
        if type(item) is not list:
            raise TypeError("matrix must be a list of lists")
    for item in matrix:
        if type(item) is list:
            if len(item) != len(matrix):
                raise ValueError("matrix must be a non-empty square matrix")
    length = len(matrix)
    if length == 1:
        return [[1]]

    underage = zerosquare(length)
    for rowNum in range(length):
        for colNum in range(length):
            coordinates = (rowNum, colNum)
            submatrix = trim_matrix(coordinates, matrix, length)
            underage[rowNum][colNum] = determinant(submatrix)

    return underage


def trim_matrix(forbidden, matrix, length):
    """
    removes from matrix matrix
        row forbiddenRow
        column forbiddenCol
    returns resultant submatrix
    """
    forbiddenRow, forbiddenCol = forbidden
    sublength = length - 1
    submatrix = zerosquare(sublength)
    passedRow, passedCol = False, False

    # insert a number as long as it is not in a
    #   forbiden row or forbidden column
    for row in range(sublength):
        # new row: new set of columns
        passedCol = False
        for col in range(sublength):
            # once we arrive at forbidden row/col,
            # add one to the position from which we draw from the matrix
            if row == forbiddenRow:
                passedRow = True
            if col == forbiddenCol:
                passedCol = True
            submatrix[row][col] =\
                matrix[row + int(passedRow)][col + int(passedCol)]
    return submatrix


def zerosquare(length):
    """creates a square matrix of zeros"""
    submatrix = []
    for y in range(length):
        submatrix.append([0] * length)
    return submatrix


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
            if len(item) != len(matrix):
                raise ValueError("matrix must be a square matrix")
        elif matrix_shape(matrix)[0] != (1,):
            raise ValueError("matrix must be a square matrix")
    # basic checks are done

    length = len(matrix)
    if length == 1:
        return matrix[0][0]
    elif length == 2:
        return simple_det(matrix)
    else:
        detTotal = 0
        for colNum in range(length):
            submatrix = []
            coeff = matrix[0][colNum]
            withoutRow = matrix[1:]
            det = 0
            for row in withoutRow:
                if row[:colNum] != [] and\
                   row[colNum + 1:] != []:
                    submatrix.append(row[:colNum] + row[colNum + 1:])
                elif row[:colNum] != []:
                    submatrix.append(row[:colNum])
                elif row[colNum + 1:] != []:
                    submatrix.append(row[colNum + 1:])
            detTotal += (-1) ** (colNum) * coeff * determinant(submatrix)
    return detTotal


def simple_det(submatrix):
    """returns determinent of 2x2 matrix"""
    if matrix_shape(submatrix) == (2, 2):
        det = (submatrix[0][0] * submatrix[1][1]) -\
              (submatrix[0][1] * submatrix[1][0])
        return det
    return 0


def matrix_shape(matrix):
    """returns shape of matrix"""
    if type(matrix) is list:
        rows = len(matrix)
    else:
        rows = None
    if type(matrix[0]) is list:
        cols = len(matrix[0])
    else:
        cols = None
    return rows, cols
