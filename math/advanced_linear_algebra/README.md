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

# Task 1 - Minor

The `minor` of `matrix` is a matrix the same size as `matrix` where each cell is occupied by the determinant of the matrix created when removing the cell's row and column from `matrix`.

we can scan the size of `matrix` to crete a "zeros" matrix and then populate each cell with the relevant determinant. As we are not allowed to import anything, including numpy, we can just write a quick function to make an equivalent array (list of lists.)

We can use the previous task's deterinant calculator to run the determinant part.
* due to no importing, we'll have to copy-paste our own code into this task.

1. scan matrix to ensure it is square and valid as according to task requirements
2. go over each cell in a for loop:
   * if length of matrix side is `length`,
    ```
    for rowNum in range(length):
        for colNum in range(length):
            coordinates = (rowNum, colNum)
            submatrix = remove_lines(coordinates)
            # above function takes 3 arguments: rowNum, colNum and hte matirx to be trimmed.
            # we can create it by copying what we did to filter in task 0
            # this function, once made htis way, will be portable to other tasks
            minorMatrix[rowNum][colNum] = determinant(submatrix)

    return minorMatrix
    ```

## Potential Pitfalls
* The required checks and error messages are slightly different in this task than they were in task-0, so you cannot simply copy and paste them.
*  ~~there is potential for finicky interaction when using `array[row][column]`, so it may be best to append entire rows directly, rather than attempt to assign element by element~~
*  it is VITAL to append CONTENTS of arrays, and not arrays themselves.
   *  If you append an *array* to multiple locatoins, any time you aler any of them, you alter everywhere it was used. You MUST create new arrays to be used as `lists` within the list of `lists`.
# Task 2 - Cofactor

Cofactor is a minor matrix where each cell is multiplied by `(-1) ** (y + x)`.  x and y = `column + 1` and `row + 1` respectively. The plus 1 is because in python, the first row is considered row 0 instead of row 1.
