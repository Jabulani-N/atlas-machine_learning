#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K

def inception_block(A_prev, filters):
    """
    builds an inception block as described in
        https://arxiv.org/pdf/1409.4842.pdf
    A_prev = output from previous layer
    filters = a tuple or list
        containing [F1, F3R, F3,F5R, F5, FPP]:
            F1 = number of filters in 1x1 convolution
            F3R = number of filters in 1x1 convolution before the 3x3 convolution
            F3 = number of filters in 3x3 convolution
            F5R = number of filters in 1x1 convolution before the 5x5 convolution
            F5 = number of filters in 5x5 convolution
            FPP = number of filters in 1x1 convolution after the max pooling
    All convolutions inside inception block should use a rectified linear activation (ReLU)
    Returns: concatenated output of inception block
    """
    F1, F3R, F3, F5R, F5, FPP = filters
    # extract parameters from list filters via direct assignment

    convf1 = K.layers.Conv2D(filters,
    kernel_size,
    strides=(1, 1),
    padding="valid",
    data_format=None,
    dilation_rate=(1, 1),
    groups=1,
    activation=None,
    use_bias=True,
    kernel_initializer="glorot_uniform",
    bias_initializer="zeros",
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None)
