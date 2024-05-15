# Clustering

# Notes

## [Understanding K-means Clustering](https://towardsdatascience.com/understanding-k-means-clustering-in-machine-learning-6a6e67336aa1)

## K-means Clustering

[![this 5 min video explains how K-means clustering works](http://img.youtube.com/vi/_aWzGGNrcic/0.jpg)](http://www.youtube.com/watch?v=_aWzGGNrcic)
* this 5 min video explains how K-means clustering works.

[![this video shows the optimum number of clusters](http://img.youtube.com/vi/xNfOheh-res/0.jpg)](https://www.youtube.com/watch?v=xNfOheh-res)
* This videos shows the optimal/optimum number of clusters
# Task 0

## Instructions

<details>
<summary>Instructions</summary>

Write a function `def initialize(X, k):` that initializes cluster centroids for K-means:


`X` is a numpy.ndarray of shape (n, d) containing the dataset that will be used for K-means clustering
* `n` is the number of data points
* `d` is the number of dimensions for each data point
* `k` is a positive integer containing the number of clusters

The cluster centroids should be initialized with a multivariate uniform distribution along each dimension in `d`:
The minimum values for the distribution should be the minimum values of `X` along each dimension in `d`
The maximum values for the distribution should be the maximum values of `X` along each dimension in `d`
You should use [`numpy.random.uniform`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html) exactly once

You are not allowed to use any loops

Returns: a numpy.ndarray of shape `(k, d)` containing the initialized centroids for each cluster, or `None` on failure

</details>

## Notes

This task only cares about initializing the centroids. You are not running the entire clustering.

you can think of the contents of X as dimension 0 has the coordinate for a list, and that list is a list of coordinates. if it were 2D, we might have x dimension and y dimension. We're potentially working with *many* dimensions, however, so we just have a whole list reprsented like this.

<details>
    <summary> whiteboarding image of how the dimensions work</summary>

![example of 3 dimensional lists](./images/clustering%20-%20task%200%20-%20coords.jpg)

</details>

This way, we don't "explicitly" say how many dimensions we're working with. We just have a format that flexes itself to work with any count. A 2D list might be worded as "X = 3, Y = 5", or (3, 5) for short. Large dimension numbers take this further. For example, we could say (3, 5, 9, 17, 33, ...)

`np.random.uniform` can take an array-like of floats, so we can put the array of maxima for each dimension as first argument, array of minima for each dimension as asecond argument, and `(k, length of how many dimensions there are)` for size.
* `length of how many dimensions there are` = `np.shape(X)[1]` = `d`


Watch the [5-minute video above](#k-means-clustering) to understand the basic idea.

# Task 1

## Instructions
<details>
<summary>Instructions</summary>

Write a function `def kmeans(X, k, iterations=1000):` that performs K-means on a dataset:

* `X` is a `numpy.ndarray` of shape (n, d) containing the dataset
    * `n` is the number of data points
    * `d` is the number of dimensions for each data point
    * `k` is a positive integer containing the number of clusters

`iterations` is a positive integer containing the maximum number of iterations that should be performed

If no change in the cluster centroids occurs between iterations, your function should `return`

Initialize the cluster centroids using a multivariate uniform distribution (based on`0-initialize.py`)

If a cluster contains no data points during the update step, reinitialize its centroid

You should use `numpy.random.uniform` exactly twice

You may use at most 2 loops

Returns: `C`, `clss`, or `None`, `None` on failure

`C` is a numpy.ndarray of shape (k, d) containing the centroid means for each cluster

`clss` is a numpy.ndarray of shape (n,) containing the index of the cluster in C that each data point belongs to

</details>

## Notes

There are two main parts to each iteration.
1. find which centroid (k position) is closest (d values) to the data point and associate it with said centroid number (k position)
2. relocate that centroid (change the d values of the k position, *preferably via making a new array*, to being the average of all the data points)
   * if every single new set of d values is the same as old, immediately return
