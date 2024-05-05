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
            if len(item) != len(matrix):
                raise ValueError("matrix must be a square matrix")
        elif matrix_shape(matrix)[0] != (1,):
            raise ValueError("matrix must be a square matrix")
    # basic checks are done

    length = len(matrix)
    # if matrix is 1x1, determinant is the content
    if length == 1:
        return matrix[0][0]
    # if matrix is 2x2, send to simple det calculator
    elif length == 2:
        return simple_det(matrix)
    # we are done for 1x1 and 2x2
    # now we just need the ones that chain
    else:
        # for loop to shave each row/col
        withoutRow = []
        for rowNum in range(length):
        # get content of the array excluding rowNum
            withoutRow = matrix[:rowNum]
            withoutRow += matrix[rowNum + 1:]
            # withoutRow is a list of lists
            # it is identitcal to matrix except it omits the relevant row
            print("withoutrow:", withoutRow)
            withoutCol = []
            for colNum in range(length):
                submatrix = []
                for row in withoutRow:
                    # get content of the row excluding colNum
                    print("withoutCol before appending:", withoutCol)
                    print("withoutCol will append from row:",row)
                    withoutCol.append(row[:colNum])
                    withoutCol.append(row[colNum + 1:])
                    print("withoutCol after appending:",withoutCol)
                # withoutCol now contains one row of submatrix
                print("withoutCol:",withoutCol)
                submatrix.append(withoutCol)
            # submatrix now contains matrix excluding
            #   row rowNum and col colNum
            print("submatrix:", submatrix)
            return determinant(submatrix)



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
