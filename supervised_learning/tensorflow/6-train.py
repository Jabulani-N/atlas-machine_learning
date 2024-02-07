#!/usr/bin/env python3
"""module documentation
this module, creates a function:
    create_train_op.
    The function creates and returns
        operation that minimizes loss of a tensor set
Though classy, it has no class.

"""


import tensorflow.compat.v1 as tf


def train(X_train, Y_train, X_valid, Y_valid,
          layer_sizes, activations, alpha,
          iterations, save_path="/tmp/model.ckpt"):
    """builds, trains, and saves a neural network classifier"""
    pass
