# Optimization

This direcetory's parameters are hyper.

# Task 0 Normalization Constants

Though standard deviation and mean are values we calculated in the [math](https://github.com/Jabulani-N/holbertonschool-machine_learning/tree/main/math/probability) course, because numpy is availible this course, we can directly have it calculate [mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html) and [standard deviation](https://numpy.org/doc/stable/reference/generated/numpy.std.html.
* You'll want to specify axis 0, in order to get values for each data point.


# Task 1 Normalize

* [Explanation for why normliaze data](https://www.jeremyjordan.me/batch-normalization/)
* [~~How to normalize data~~](https://www.tensorflow.org/versions/r2.6/api_docs/python/tf/nn/batch_normalization) Tensorflow is not permitted in this assignment task.
  * [As recorded in my previous work](https://github.com/Jabulani-N/holbertonschool-machine_learning/tree/main/math/probability), variance is square of standard deviation.
    * [numpy will make that easy](https://numpy.org/doc/stable/reference/generated/numpy.square.html)

The basic structure we will use for this task is `normalized_X = (X - m) / s`. Numpy will make [subtraction](https://numpy.org/doc/stable/reference/generated/numpy.subtract.html) and [division](https://numpy.org/doc/stable/reference/generated/numpy.divide.html) easy.

## Task 2 Shuffle Data

Don't let the idea of shuffling intimidate you. Think about what shuffling means for a list: pick a random order to read its elements. We just need to come up with a random *order*, and then read off both matrices in that aforementioned "order."

how to get that random order? [Numpy has you covered.](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.permutation.html)
