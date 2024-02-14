# Optimization

This direcetory's parameters are hyper.

# Task 0 Normalization Constants

Though standard deviation and mean are values we calculated in the [math](https://github.com/Jabulani-N/holbertonschool-machine_learning/tree/main/math/probability) course, because numpy is availible this course, we can directly have it calculate [mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html) and [standard deviation](https://numpy.org/doc/stable/reference/generated/numpy.std.html.
* You'll want to specify axis 0, in order to get values for each data point.


# Task 1 Normalize

<details>
  <summary>Testing code</summary>

```

#!/usr/bin/env python3

import numpy as np
normalization_constants =\
    __import__('0-norm_constants').normalization_constants
normalize = __import__('1-normalize').normalize

if __name__ == '__main__':
    np.random.seed(0)
    a = np.random.normal(0, 2, size=(100, 1))
    b = np.random.normal(2, 1, size=(100, 1))
    c = np.random.normal(-3, 10, size=(100, 1))
    X = np.concatenate((a, b, c), axis=1)
    m, s = normalization_constants(X)
    print(X[:10])
    X = normalize(X, m, s)
    print(X[:10])
    m, s = normalization_constants(X)
    print(m)
    print(s)

```
</details>

----

* [Explanation for why normliaze data](https://www.jeremyjordan.me/batch-normalization/)
* [~~How to normalize data~~](https://www.tensorflow.org/versions/r2.6/api_docs/python/tf/nn/batch_normalization) Tensorflow is not permitted in this assignment task.
  * [As recorded in my previous work](https://github.com/Jabulani-N/holbertonschool-machine_learning/tree/main/math/probability), variance is square of standard deviation.
    * [numpy will make that easy](https://numpy.org/doc/stable/reference/generated/numpy.square.html)

The basic structure we will use for this task is `normalized_X = (X - m) / s`. Numpy will make [subtraction](https://numpy.org/doc/stable/reference/generated/numpy.subtract.html) and [division](https://numpy.org/doc/stable/reference/generated/numpy.divide.html) easy.

## Task 2 Shuffle Data

<details>
  <summary>Testing code</summary>

```

#!/usr/bin/env python3

import numpy as np
shuffle_data = __import__('2-shuffle_data').shuffle_data

if __name__ == '__main__':
    X = np.array([[1, 2],
                  [3, 4],
                  [5, 6],
                  [7, 8],
                  [9, 10]])
    Y = np.array([[11, 12],
                 [13, 14],
                 [15, 16],
                 [17, 18],
                 [19, 20]])

    np.random.seed(0)
    X_shuffled, Y_shuffled = shuffle_data(X, Y)

    print(X_shuffled)
    print(Y_shuffled)
```
</details>

----

Don't let the idea of shuffling intimidate you. Think about what shuffling means for a list: pick a random order to read its elements. We just need to come up with a random *order*, and then read off both matrices in that aforementioned "order."

how to get that random order? [Numpy has you covered.](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.permutation.html)

## Task 3

This task is currently imcpomete; in the pursuit of creating a minimum viable product, it will only be revisited should the time limit allow.

<details>
  <summary>Instructions</summary>

```
Write the function def train_mini_batch(X_train, Y_train, X_valid, Y_valid, batch_size=32, epochs=5, load_path="/tmp/model.ckpt", save_path="/tmp/model.ckpt"): that trains a loaded neural network model using mini-batch gradient descent:
* 
* X_train is a numpy.ndarray of shape (m, 784) containing the training data
* m is the number of data points
* 784 is the number of input features
* Y_train is a one-hot numpy.ndarray of shape (m, 10) containing the training labels
* 10 is the number of classes the model should classify
* X_valid is a numpy.ndarray of shape (m, 784) containing the validation data
* Y_valid is a one-hot numpy.ndarray of shape (m, 10) containing the validation labels
* batch_size is the number of data points in a batch
* epochs is the number of times the training should pass through the whole dataset
* load_path is the path from which to load the model
* save_path is the path to where the model should be saved after training
* Returns: the path where the model was saved
* Your training function should allow for a smaller final batch (a.k.a. use the entire training set)
     1) import meta graph and restore session
     2) Get the following tensors and ops from the collection restored
        * x is a placeholder for the input data
        * y is a placeholder for the labels
        * accuracy is an op to calculate the accuracy of the model
        * loss is an op to calculate the cost of the model
        * train_op is an op to perform one pass of gradient descent on the model
  1) loop over epochs:
        * shuffle data
        * loop over the batches:
            * get X_batch and Y_batch from data
            * train your model
    1) Save session
     * You should use `shuffle_data = __import__('2-shuffle_data').shuffle_data`
  * Before the first epoch and after every subsequent epoch, the following should be printed:
        * After {epoch} epochs: where {epoch} is the current epoch
        * \tTraining Cost: {train_cost} where {train_cost} is the cost of the model on the entire training set
        * \tTraining Accuracy: {train_accuracy} where {train_accuracy} is the accuracy of the model on the entire training set
        * \tValidation Cost: {valid_cost} where {valid_cost} is the cost of the model on the entire validation set
        * \tValidation Accuracy: {valid_accuracy} where {valid_accuracy} is the accuracy of the model on the entire validation set
* After every 100 steps gradient descent within an epoch, the following should be printed:
* \tStep {step_number}: where {step_number} is the number of times gradient descent has been run in the current epoch
* \t\tCost: {step_cost} where {step_cost} is the cost of the model on the current mini-batch
* \t\tAccuracy: {step_accuracy} where {step_accuracy} is the accuracy of the model on the current mini-batch
* Advice: the function range can help you to handle this loop inside your dataset by using batch_size as step value
```
</details>

----

<details>
  <summary>Testing code</summary>

```
#!/usr/bin/env python3

import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_eager_execution()
train_mini_batch = __import__('3-mini_batch').train_mini_batch

def one_hot(Y, classes):
    """convert an array to a one-hot matrix"""
    oh = np.zeros((Y.shape[0], classes))
    oh[np.arange(Y.shape[0]), Y] = 1
    return oh

if __name__ == '__main__':
    lib= np.load('../data/MNIST.npz')
    X_train_3D = lib['X_train']
    Y_train = lib['Y_train']
    X_train = X_train_3D.reshape((X_train_3D.shape[0], -1))
    Y_train_oh = one_hot(Y_train, 10)
    X_valid_3D = lib['X_valid']
    Y_valid = lib['Y_valid']
    X_valid = X_valid_3D.reshape((X_valid_3D.shape[0], -1))
    Y_valid_oh = one_hot(Y_valid, 10)

    layer_sizes = [256, 256, 10]
    activations = [tf.nn.tanh, tf.nn.tanh, None]
    alpha = 0.01
    iterations = 5000

    np.random.seed(0)
    save_path = train_mini_batch(X_train, Y_train_oh, X_valid, Y_valid_oh,
                                 epochs=10, load_path='./graph.ckpt',
                                 save_path='./model.ckpt')
    print('Model saved in path: {}'.format(save_path))
```
</details>

----

[How to compile your model](https://www.tensorflow.org/api_docs/python/tf/keras/Model#compile)
you'll be training your model with [`model_name.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model).


## task 4 Moving Average

[This wikipedia article](https://en.wikipedia.org/wiki/Moving_average#Weighted_moving_average) explains the basic idea of a weighted moving average.

[This seems to be a formula for weighted average](https://math.stackexchange.com/questions/4083208/how-is-the-exponential-moving-average-calculated), and below it is a snippet of code that can be translated for our own use.


### Potential Pitfalls:

if you convert the `return`ed list to an numpy.array, it will round before the 14th decimal place, changing results from those expected by the grading algorithm.

## Task 5

## task 6

momentum optimizer in tensorflow: [tf.compat.v1.train.MomentumOptimizer](https://www.tensorflow.org/versions/r2.6/api_docs/python/tf/compat/v1/train/MomentumOptimizer.md)

Either my code or the grading algorithm is currently bugged in this task. This has been reported, and will be moved past.
* there are many commits that are attempts at different formattings. One can check the commits made closeley after "what was I even doing..." to see the different ways I attempted to phrase the file before I realized what the problem was.
  * I write this so I have reference to look at if after the import is fixed, there are errors in performance: I will have previous versions to reference.


## Task 8

Same import problem as task 6

## Task 9

based on [this](https://stackoverflow.com/questions/61103275/what-is-the-difference-between-tensor-and-tensor-in-pytorch), trying by altering variables themselves, rather than creating and editing copies.