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
    # extract filters from list `filters` via direct assignment

    convf1 = K.layers.Conv2D(F1, (1, 1),
                             padding="same",
                             activation="ReLU")(A_prev)
    convf3r = K.layers.Conv2D(F3R, (1, 1),
                             padding="same",
                             activation="ReLU")(A_prev)
    # above is 1x1 layer filter before 3x3 filter
    convf3 = K.layers.Conv2D(F3, (3, 3),
                             padding="same",
                             activation="ReLU")(convf3r)
    convf5r = K.layers.Conv2D(F5R, (1, 1),
                             padding="same",
                             activation="ReLU")(A_prev)
    # above is 1x1 layer filter before 5x5 filter
    convf5 = K.layers.Conv2D(F5, (5, 5),
                             padding="same",
                             activation="ReLU")(convf5r)
    poolpp = K.layers.MaxPooling2D(pool_size=(3, 3), strides=(1,1),
                                   padding="same", data_format=None,
                                   name=None,)(A_prev)
    afterpool = K.layers.Conv2D(FPP, (1, 1),
                             padding="same",
                             activation="ReLU")(poolpp)
    filterConc = K.layers.Concatenate(3)([convf1, convf3, convf5, afterpool])
    return filterConc

