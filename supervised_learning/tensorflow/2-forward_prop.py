#!/usr/bin/env python3
"""module documentation
this module, 2-forward_prop, creates a function:
    forward_prop
Though classy, it has no class.

"""


import tensorflow.compat.v1 as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """x is the placeholder for the input data
layer_sizes list containing number of nodes in each layer of  network
activations list containing activation functions of each layer of  network
Returns: the prediction of the network in tensor form
"""

    if len(layer_sizes) == len(activations):
        layerCount = len(activations)
        prev = x
        for lyr in range(0, layerCount):
            prev = create_layer(prev, layer_sizes[lyr], activations[lyr])
        return prev
