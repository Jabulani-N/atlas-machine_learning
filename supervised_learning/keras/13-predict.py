#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K


def predict(network, data, verbose=False):
    """makes a prediction using a neural network"""
    return network.predict(data, verbose=verbose)
