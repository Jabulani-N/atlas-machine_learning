#!/usr/bin/env python3
"""this module creates 2 functions."""


import tensorflow.keras as K


def save_model(network, filename):
    """saves entire model"""
    network.save(filename)


def load_model(filename):
    """loads a model"""
    loaded_model = K.saving.load_model(filename, safe_mode=False)
    return loaded_model
