# Advanced Linear Algebra

This directory contains code that will perform matrix operations.


# Task 0 - Determinant

Create `def determinant(matrix):` that returns the determinant of `matrix`

at it's simplist, a `submat` that is a 2x2 matrix, determinant will be

`det = (submat[0][0] * submat[1][1]) - (submat[0][1] * submat[1][0])`
* it may be easiest to keep this in a separate function `simple_determinant(submat)` where `submat` is always a 2x2 matrix
  * done this way, we can immediately return a correct answer if `matrix` is a 2x2 matrix without needing to do much thinking.
* **requires**
  * identifying size of a matrix

First, I will want to determine the shape of `matrix`.Since no imports are allowed, we cacn use
```
def matrix_shape(matrix):
    """returns shape of matrix"""
    if type(matrix) is list:
        rows = len(matrix)
    else:
        rows = None
    if type(matrix[0]) is list:
            cols = len(matrix[0])
    else: cols = None
    return rows, cols
```

if `matrix` is 2x2, we can directly calculat determinant.

If `matrix` is bigger than 2x2, we'l have to do a whole chain of recursion where we find the determinant by finding each cell's minor individually, by recursively sending the submatrix to the determinant calculator.

You can use this to make a quick 4x4 matrix to experiment with:
```
B = np.zeros((4,4))
count = 0
for col in B:
  for i in range(len(col)):
    col[i] = count
    count += 1
```