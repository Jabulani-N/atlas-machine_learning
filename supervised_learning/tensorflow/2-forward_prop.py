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
layer_sizes is a list containing the number of nodes in each layer of the network
activations is a list containing the activation functions for each layer of the network
Returns: the prediction of the network in tensor form
"""
    pass
