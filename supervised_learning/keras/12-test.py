#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K


def test_model(network, data, labels, verbose=True):
    """
    tests a neural network
        loss, accuracy
    """
    results = network.evaluate(data, labels, verbose=verbose)
    return results[0], results[1]
