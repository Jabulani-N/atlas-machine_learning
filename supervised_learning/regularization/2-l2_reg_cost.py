#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.compat.v1 as tf


def l2_reg_cost(cost):
    """placeholder documentation"""
    L2_regularizer = tf.keras.regularizers.L2()
    all_weights = [v for v in tf.trainable_variables() if "weights" in v.name]
    l2_penalty = tf.contrib.layers.apply_regularization(L2_regularizer,
                                                        all_weights)
    negative_penalty = cost - l2_penalty
    return negative_penalty
