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

layer_sizes is a list containing the number of nodes in each layer of the network
activations is a list containing the activation functions for each layer of the network
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
    """builds, trains, and saves a neural network classifier"""
    return save_path
