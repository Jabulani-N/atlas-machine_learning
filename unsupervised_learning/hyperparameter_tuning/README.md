# Hyperparameter Tuning

# Task 0 Initialize Gaussian Process

<details>
    <summary>Instructions</summary>
    Create the class GaussianProcess that represents a noiseless 1D Gaussian process:

Class constructor: `def __init__(self, X_init, Y_init, l=1, sigma_f=1):`

`X_init` is a numpy.ndarray of shape `(t, 1)` representing the inputs already sampled with the black-box function
`Y_init` is a numpy.ndarray of shape `(t, 1)` representing the outputs of the black-box function for each input in `X_init`
`t` is the number of initial samples
`l` is the length parameter for the kernel
`sigma_f` is the standard deviation given to the output of the black-box function
Sets the public instance attributes `X`, `Y`, `l`, and `sigma_f` corresponding to the respective constructor inputs
Sets the public instance attribute `K`, representing the current covariance kernel matrix for the Gaussian process
Public instance method `def kernel(self, X1, X2):` that calculates the covariance kernel matrix between two matrices:

`X1` is a `numpy.ndarray` of shape `(m, 1)`
`X2` is a `numpy.ndarray` of shape `(n, 1)`
the kernel should use the Radial Basis Function (RBF)
`Returns`: the covariance kernel matrix as a `numpy.ndarray` of shape `(m, n)`
</details>

&nbsp;

Most of this task is self-explanatory.

The only thing needing research is "covariance kernal matrix between two matrices" to calculate and assign `self.K`

* "the kernel should use the **Radial Basis Function** (RBF)"

I had to do a relatively brute forced approach to do this one:

* `kernel_matrix[i, j] = self.sigma_f ** 2 * np.exp((-(dist / self.l) ** 2)/2)`
  * `i` is an index on the first 1D input matrix, and `j` is an index on the second.
    * `dist` is distance between the two values in the 1D arrays
      * literally `X1[i] - X2[j]`
  * `sigma_f` and `l` are given via self's init method we made before.
  * do this for every coordinate in `kernal_matrix`

## Task 0 Resources

* Medium article that [explains covariance kernel matrix ca;culation](https://towardsdatascience.com/gaussian-process-models-7ebce1feb83d)
  * can search the phrase "covariance kernel matrix"

* [this person](https://stackoverflow.com/questions/59893922/gaussian-kernel-performance) wrote a particularly efficient manner of calculation, and was looking to go even further beyond the current efficiency.
  * it is based on `k_ij = exp(-||x_i - x_j||^2 / (2 * sigma^2))`.
  * When applied in our initialization method, is supposed to recieve the X_init value twice.
  * This particular application does *not* create correct results in practice here.

&nbsp;


# Task 1

<details>
    <summary>Instructions</summary>
    Based on `0-gp.py`, update the class `GaussianProcess`:

Public instance method `def predict(self, X_s):` that predicts the mean and standard deviation of points in a Gaussian process:
`X_s` is a numpy.ndarray of shape `(s, 1)` containing all of the points whose mean and standard deviation should be calculated
`s` is the number of sample points
`Returns`: `mu`, `sigma`
`mu` is a `numpy.ndarray` of shape `(s,)` containing the mean for each point in `X_s`, respectively
`sigma` is a `numpy.ndarray` of shape `(s,)` containing the variance for each point in `X_s`, respectively
</details>


Predicting mean for each point:
* Note: as you study, remember "covariance matrix" is what we calculated in task 0

Predicting standard deviation for each point:

[`numpy.ndarray.flatten`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html) is used to convert a multidimensional array into a 1D array.
[`numpy.diag(arr)`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html) is used to pull the diagonal of `arr` from the center. It can be offset by a second argument (int).