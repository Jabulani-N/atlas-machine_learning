#!/usr/bin/env python3
"""this module creates 2 functions."""


import tensorflow.keras as K


def save_model(network, filename):
    """saves entire model"""
    network.save(filename)


def load_model(filename):
    """loads a model"""
    return K.saving.load_model(filename)
