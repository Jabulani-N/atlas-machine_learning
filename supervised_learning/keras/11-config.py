#!/usr/bin/env python3
"""this module creates 2 functions."""


import tensorflow.keras as K


def save_config(network, filename):
    """saves a model’s configuration in JSON format"""
    json_config = network.to_json(filename)
    with open(filename, 'w') as file:
        file.write(json_config)



def load_config(filename):
    """loads a model with a specific configuration"""
    pass
