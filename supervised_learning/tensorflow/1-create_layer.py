#!/usr/bin/env python3
"""module documentation
this module, 1-create_layer, creates a function:
    create_layer
Though classy, it has no class.

"""

import tensorflow.compat.v1 as tf


def create_layer(prev, n, activation):
    """prev is the tensor output of the previous layer
n is the number of nodes in the layer to create
activation is the activation function that the layer should use
"""

    initializer = tf.keras.initializers.VarianceScaling(mode='fan_avg')

    layer = tf.keras.layers.Dense(n, activation=activation,
                                  kernel_initializer=initializer, name='layer')

    return layer(prev)
