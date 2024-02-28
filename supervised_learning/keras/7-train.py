#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K


def train_model(network, data, labels,
                batch_size, epochs, validation_data=None,
                early_stopping=False, patience=0,
                learning_rate_decay=False, alpha=0.1,
                decay_rate=1,
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
    learning_rate_decay = boolean for if learning rate decay is used
        learning rate decay only performed if validation_data exists
        performed using inverse time decay
        learning rate  decay is a stepwise fashion after each epoch
        each time the learning rate updates, Keras prints a message
        alpha is the initial learning rate
    decay_rate is the decay rate
    """
    # learning rate decay code goes here
    if validation_data is not None and learning_rate_decay:
        decay_steps = 1
        optimizer = K.optimizers.schedules.InverseTimeDecay(alpha,
                                                            decay_steps,
                                                            decay_rate,
                                                            staircase=True)
    else:
        optimizer = None

    if validation_data is not None and early_stopping and patience < epochs:
        callbacks = K.callbacks.EarlyStopping(patience=patience)

    else:
        callbacks = None
    return network.fit(data, labels, batch_size=batch_size,
                       epochs=epochs, verbose=verbose,
                       shuffle=shuffle, validation_data=validation_data,
                       callbacks=callbacks, optimizer=optimizer)
