#!/usr/bin/env python3
"""module documentation
this module, creates a function:
    create_train_op.
    The function creates and returns
        operation that minimizes loss of a tensor set
Though classy, it has no class.

X_train is a numpy.ndarray containing the training input data
Y_train is a numpy.ndarray containing the training labels
X_valid is a numpy.ndarray containing the validation input data
Y_valid is a numpy.ndarray containing the validation labels

layer_sizes: list containing  number of nodes in each layer of network
activations: list containing  activation functions of each layer of the network
alpha is the learning rate
iterations is the number of iterations to train over
save_path designates where to save the model
"""


import tensorflow.compat.v1 as tf
calculate_accuracy = __import__('3-calculate_accuracy').calculate_accuracy
calculate_loss = __import__('4-calculate_loss').calculate_loss
create_placeholders = __import__('0-create_placeholders').create_placeholders
create_train_op = __import__('5-create_train_op').create_train_op
forward_prop = __import__('2-forward_prop').forward_prop


def train(X_train, Y_train, X_valid, Y_valid,
          layer_sizes, activations, alpha,
          iterations, save_path="/tmp/model.ckpt"):
    """builds, trains, and saves a neural network classifier
    Graph has in collection:
        placeholders: x, y
        tensors y_pred, loss, and accuracy
        operation train_op
    """

    # initialize/reset the graph
    tf.compat.v1.reset_default_graph()
    # step 1: fill the graph's collection

    x, y = create_placeholders(X_train.shape[1], Y_train.shape[1])
    prediction = forward_prop(x, layer_sizes, activations)
    loss = calculate_loss(Y_valid, prediction)
    accuracy = calculate_accuracy(Y_valid, prediction)
    train_op = create_train_op(loss, alpha)

    tf.compat.v1.add_to_collection('x', x)
    tf.compat.v1.add_to_collection('y', y)
    tf.compat.v1.add_to_collection('prediction', prediction)
    tf.compat.v1.add_to_collection('loss', loss)
    tf.compat.v1.add_to_collection('accuracy', accuracy)
    tf.compat.v1.add_to_collection('train_op', train_op)
    return save_path
