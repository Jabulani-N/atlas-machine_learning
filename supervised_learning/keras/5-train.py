#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K


def train_model(network, data, labels,
                batch_size, epochs, validation_data=None,
                verbose=True, shuffle=False):
    """
    network = model to train
    data = numpy.ndarray
        shape (m, nx) containing  input data
    labels = one-hot numpy.ndarray
        shape (m, classes) containing labels of data
    batch_size = size of batch used for mini-batch gradient descent
    epochs = number of passes through data for mini-batch gradient descent
    verbose = boolean that determines if output is printed
    validation_data = validation data
    """
    return network.fit(data, labels, batch_size=batch_size,
                       epochs=epochs, verbose=verbose,
                       shuffle=shuffle, validation_data=validation_data)
