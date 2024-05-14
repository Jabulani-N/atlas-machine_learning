# Dimensionality Reduction

# Task 0 - PCA
* PCA stands for "Principle Component Analysis."

## Instrucitons

Write a function def pca(X, var=0.95): that performs PCA on a dataset:

* X is a numpy.ndarray of shape (n, d) where:
    *  n is the number of data points
    *  d is the number of dimensions in each point
* all dimensions have a mean of 0 across all data points
* var is the fraction of the variance that the PCA transformation should maintain
* Returns: the weights matrix, W, that maintains var fraction of X‘s original variance
  * W is a numpy.ndarray of shape (d, nd) where nd is the new dimensionality of the transformed X

[`np.linalg.svd` returns](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html)
* `U`{ (…, M, M), (…, M, K) } array
Unitary array(s). The first a.ndim - 2 dimensions have the same size as those of the input a. The size of the last two dimensions depends on the value of full_matrices. Only returned when compute_uv is True.

* `S`(…, K) array
Vector(s) with the singular values, within each vector sorted in descending order. The first a.ndim - 2 dimensions have the same size as those of the input a.

* `Vh`{ (…, N, N), (…, K, N) } array
Unitary array(s). The first a.ndim - 2 dimensions have the same size as those of the input a. The size of the last two dimensions depends on the value of full_matrices. Only returned when compute_uv is True.

## Resources

[![Singular Value Decomposition](http://img.youtube.com/vi/P5mlg91as1c/0.jpg)](http://www.youtube.com/watch?v=P5mlg91as1c)

[`np.linalg.svd`: Numpy Singular Value Decomposition documentation](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html)


[![How to implement PCA (Principal Component Analysis) from scratch with Python](http://img.youtube.com/vi/Rjr62b_h7S4/0.jpg)](https://www.youtube.com/watch?v=Rjr62b_h7S4)
* explains concept well