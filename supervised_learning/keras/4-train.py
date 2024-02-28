#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K


def train_model(network, data, labels, batch_size,
                epochs, verbose=True, shuffle=False):
    """
    network = model to train
    data = numpy.ndarray of shape (m, nx) containing the input data
    labels = one-hot numpy.ndarray of shape (m, classes) containing labels of data
    batch_size = size of the batch used for mini-batch gradient descent
    epochs = number of passes through data for mini-batch gradient descent
    verbose = boolean that determines if output should be printed during training
    shuffle
    """
    return network.fit(data, labels, batch_size=batch_size,
                       epochs=epochs, verbose=verbose,
                       shuffle=shuffle)
