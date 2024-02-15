#!/usr/bin/env python3
"""module documentation
this module creates a function.

"""


import tensorflow.compat.v1 as tf


def create_batch_norm_layer(prev, n, activation):
    """placeholder documentation"""
    densed = tf.keras.layers.Dense(n,
                                   kernel_initializer=tf.keras.
                                   initializers.
                                   VarianceScaling(mode='fan_avg'),
                                   use_bias=False)
