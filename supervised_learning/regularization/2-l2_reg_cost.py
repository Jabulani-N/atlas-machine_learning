#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.compat.v1 as tf


def l2_reg_cost(cost):
    """placeholder documentation"""
    regularizer = tf.keras.regularizers.L2()
    # print(regularizer)
    crashes_intentionally = tf.keras.regularizers.L2(cost, 0.01)
