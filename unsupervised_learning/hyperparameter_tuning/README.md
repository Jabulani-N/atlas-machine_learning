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

<details>
    <summary>Test Code</summary>

```

root@alexa-ml2-1:~/hyperparameter_opt# cat 0-main.py
#!/usr/bin/env python3

GP = __import__('0-gp').GaussianProcess
import numpy as np


def f(x):
    """our 'black box' function"""
    return np.sin(5*x) + 2*np.sin(-2*x)

if __name__ == '__main__':
    np.random.seed(0)
    X_init = np.random.uniform(-np.pi, 2*np.pi, (2, 1))
    Y_init = f(X_init)

    gp = GP(X_init, Y_init, l=0.6, sigma_f=2)
    print(gp.X is X_init)
    print(gp.Y is Y_init)
    print(gp.l)
    print(gp.sigma_f)
    print(gp.K.shape, gp.K)
    print(np.allclose(gp.kernel(X_init, X_init), gp.K))
root@alexa-ml2-1:~/hyperparameter_opt# ./0-main.py
True
True
0.6
2
(2, 2) [[4.         0.13150595]
 [0.13150595 4.        ]]
True
root@alexa-ml2-1:~/hyperparameter_opt#

```
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

<details>
    <summary>Test Code</summary>

```
root@alexa-ml2-1:~/hyperparameter_opt# cat 1-main.py
#!/usr/bin/env python3

GP = __import__('1-gp').GaussianProcess
import numpy as np


def f(x):
    """our 'black box' function"""
    return np.sin(5*x) + 2*np.sin(-2*x)

if __name__ == '__main__':
    np.random.seed(0)
    X_init = np.random.uniform(-np.pi, 2*np.pi, (2, 1))
    Y_init = f(X_init)

    gp = GP(X_init, Y_init, l=0.6, sigma_f=2)
    X_s = np.random.uniform(-np.pi, 2*np.pi, (10, 1))
    mu, sig = gp.predict(X_s)
    print(mu.shape, mu)
    print(sig.shape, sig)
root@alexa-ml2-1:~/hyperparameter_opt# ./1-main.py
(10,) [ 0.20148983  0.93469135  0.14512328 -0.99831012  0.21779183 -0.05063668
 -0.00116747  0.03434981 -1.15092063  0.9221554 ]
(10,) [1.90890408 0.01512125 3.91606789 2.42958747 3.81083574 3.99817545
 3.99999903 3.9953012  3.05639472 0.37179608]
root@alexa-ml2-1:~/hyperparameter_opt#

```
</details>

Predicting mean for each point:
* Note: as you study, remember "covariance matrix" is what we calculated in task 0

Predicting standard deviation for each point:

[`numpy.ndarray.flatten`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html) is used to convert a multidimensional array into a 1D array.
[`numpy.diag(arr)`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html) is used to pull the diagonal of `arr` from the center. It can be offset by a second argument (int).

# Task 2

<detials>
    <summary>Instructions</summary>

Based on `1-gp.py`, update the class `GaussianProcess`:

Public instance method `def update(self, X_new, Y_new):` that updates a Gaussian Process:
`X_new` is a `numpy.ndarray` of shape `(1,)` that represents the new sample point
`Y_new` is a `numpy.ndarray` of shape `(1,)` that represents the new sample function value
Updates the public instance attributes `X`, `Y`, and `K`


</detials>

This task is essentially adding values to the `self.X` and `self.Y` values, and updating the `self.K` based on the result. [`numpy.vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html) should be of use here.
* notice/remember the shape of self.X is [`(t, 1)`](#task-0-initialize-gaussian-process), meaning each entry it it's own row

<details>
    <summary>Test code</summary>

```

root@alexa-ml2-1:~/hyperparameter_opt# cat 2-main.py
#!/usr/bin/env python3

GP = __import__('2-gp').GaussianProcess
import numpy as np


def f(x):
    """our 'black box' function"""
    return np.sin(5*x) + 2*np.sin(-2*x)

if __name__ == '__main__':
    np.random.seed(0)
    X_init = np.random.uniform(-np.pi, 2*np.pi, (2, 1))
    Y_init = f(X_init)

    gp = GP(X_init, Y_init, l=0.6, sigma_f=2)
    X_new = np.random.uniform(-np.pi, 2*np.pi, 1)
    print('X_new:', X_new)
    Y_new = f(X_new)
    print('Y_new:', Y_new)
    gp.update(X_new, Y_new)
    print(gp.X.shape, gp.X)
    print(gp.Y.shape, gp.Y)
    print(gp.K.shape, gp.K)
root@alexa-ml2-1:~/hyperparameter_opt# ./2-main.py
X_new: [2.53931833]
Y_new: [1.99720866]
(3, 1) [[2.03085276]
 [3.59890832]
 [2.53931833]]
(3, 1) [[ 0.92485357]
 [-2.33925576]
 [ 1.99720866]]
(3, 3) [[4.         0.13150595 2.79327536]
 [0.13150595 4.         0.84109203]
 [2.79327536 0.84109203 4.        ]]
root@alexa-ml2-1:~/hyperparameter_opt#

```
</details>

## Potential Pitfall

you will *not* be needing `numpy.append` for this (unless you do a transpose approach to add the value)

# Task 3

<details>
    <summary>Instructions</summary>

Create the class BayesianOptimization that performs Bayesian optimization on a noiseless 1D Gaussian process:

Class constructor `def __init__(self, f, X_init, Y_init, bounds, ac_samples, l=1, sigma_f=1, xsi=0.01, minimize=True):`

* `f` is the black-box function to be optimized

* `X_init` is a `numpy.ndarray` of shape `(t, 1)` representing the inputs already sampled with the black-box function

* `Y_init` is a `numpy.ndarray` of shape `(t, 1)` representing the outputs of the black-box function for each input in `X_init`
t is the number of initial samples

* `bounds` is a tuple of `(min, max)` representing the bounds of the space in which to look for the optimal point

* `ac_samples` is the number of samples that should be analyzed during acquisition

* `l` is the length parameter for the kernel

* `sigma_f` is the standard deviation given to the output of the black-box function

* `xsi` is the exploration-exploitation factor for acquisition

* `minimize` is a `bool` determining whether optimization should be performed for minimization (`True`) or maximization (`False`)

Sets the following public instance attributes:

* `f`: the black-box function

* `gp`: an instance of the class `GaussianProcess`

* `X_s`: a numpy.ndarray of shape `(ac_samples, 1)` containing all acquisition sample points, evenly spaced between `min` and `max`

* `xsi`: the exploration-exploitation factor

* `minimize`: a `bool` for minimization versus maximization

You may use `GP = __import__('2-gp').GaussianProcess`

</details>


<details>
    <summary>Test data</summary>

```

root@alexa-ml2-1:~/hyperparameter_opt# cat 3-main.py 
#!/usr/bin/env python3

GP = __import__('2-gp').GaussianProcess
BO = __import__('3-bayes_opt').BayesianOptimization
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    """our 'black box' function"""
    return np.sin(5*x) + 2*np.sin(-2*x)

if __name__ == '__main__':
    np.random.seed(0)
    X_init = np.random.uniform(-np.pi, 2*np.pi, (2, 1))
    Y_init = f(X_init)

    bo = BO(f, X_init, Y_init, (-np.pi, 2*np.pi), 50, l=2, sigma_f=3, xsi=0.05)
    print(bo.f is f)
    print(type(bo.gp) is GP)
    print(bo.gp.X is X_init)
    print(bo.gp.Y is Y_init)
    print(bo.gp.l)
    print(bo.gp.sigma_f)
    print(bo.X_s.shape, bo.X_s)
    print(bo.xsi)
    print(bo.minimize)
root@alexa-ml2-1:~/hyperparameter_opt# ./3-main.py 
True
True
True
True
2
3
(50, 1) [[-3.14159265]
 [-2.94925025]
 [-2.75690784]
 [-2.56456543]
 [-2.37222302]
 [-2.17988062]
 [-1.98753821]
 [-1.7951958 ]
 [-1.60285339]
 [-1.41051099]
 [-1.21816858]
 [-1.02582617]
 [-0.83348377]
 [-0.64114136]
 [-0.44879895]
 [-0.25645654]
 [-0.06411414]
 [ 0.12822827]
 [ 0.32057068]
 [ 0.51291309]
 [ 0.70525549]
 [ 0.8975979 ]
 [ 1.08994031]
 [ 1.28228272]
 [ 1.47462512]
 [ 1.66696753]
 [ 1.85930994]
 [ 2.05165235]
 [ 2.24399475]
 [ 2.43633716]
 [ 2.62867957]
 [ 2.82102197]
 [ 3.01336438]
 [ 3.20570679]
 [ 3.3980492 ]
 [ 3.5903916 ]
 [ 3.78273401]
 [ 3.97507642]
 [ 4.16741883]
 [ 4.35976123]
 [ 4.55210364]
 [ 4.74444605]
 [ 4.93678846]
 [ 5.12913086]
 [ 5.32147327]
 [ 5.51381568]
 [ 5.70615809]
 [ 5.89850049]
 [ 6.0908429 ]
 [ 6.28318531]]
0.05
True
root@alexa-ml2-1:~/hyperparameter_opt#


```

</details>

`self.X_s` has a length given in an easy-to-read int, so you can direcly utilize [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) to generate it.

# Task 4

[this medium](https://medium.com/@okanyenigun/step-by-step-guide-to-bayesian-optimization-a-python-based-approach-3558985c6818) article has a part that features logic we're likely to use

Looking to basically copy [this](https://krasserm.github.io/2018/03/21/bayesian-optimization/). Where it uses `mu`, I use `mean`for clarity.
* similarly, I use `variance` instead of `sigma`.

# Notes to self

when optimizing, you should probably utulize your previous projet that optimizes a model