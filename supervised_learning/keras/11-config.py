#!/usr/bin/env python3
"""this module creates 2 functions."""


import tensorflow.keras as K


def save_config(network, filename):
    """saves a model’s configuration in JSON format"""
    network.save_config(filename)


def load_config(filename):
    """loads a model with a specific configuration"""
    pass
