# Clustering

# Notes

## [Understanding K-means Clustering](https://towardsdatascience.com/understanding-k-means-clustering-in-machine-learning-6a6e67336aa1)

## K-means Clustering

[![this 5 min video explains how K-means clustering works](http://img.youtube.com/vi/_aWzGGNrcic/0.jpg)](http://www.youtube.com/watch?v=_aWzGGNrcic)
* this 5 min video explains how K-means clustering works.

# Task 0

## Instructions

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


This task only cares about initializing the centroids. You are not running the entire clustering.

you can think of the contents of X as dimension 0 has the coordinate for a list, and that list is a list of coordinates. if it were 2D, we might have x dimension and y dimension. We're potentially working with *many* dimensions, however, so we just have a whole list reprsented like this.

![example of 3 dimensional lists](./images/clustering%20-%20task%200%20-%20coords.jpg)

This way, we don't "explicitly" say how many dimensions we're working with. We just have a format that flexes itself to work with any count. A 2D list might be worded as "X = 3, Y = 5", or (3, 5) for short. Large dimension numbers take this further. For example, we could say (3, 5, 9, 17, 33, ...)

`np.random.uniform` can take an array-like of floats, so we can put the array of maxima for each dimension as first argument, array of minima for each dimension as asecond argument, and `(k, length of how many dimensions there are)` for size.
* `length of how many dimensions there are` = `np.shape(X)[1]` = `d`


Watch the [5-minute video above](#k-means-clustering) to understand the basic idea.
