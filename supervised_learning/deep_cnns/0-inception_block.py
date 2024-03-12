#!/usr/bin/env python3
"""this module creates a function."""


import tensorflow.keras as K

def inception_block(A_prev, filters):
    """
    builds an inception block as described in
        https://arxiv.org/pdf/1409.4842.pdf
    A_prev is the output from the previous layer
    filters is a tuple or list containing F1, F3R, F3,F5R, F5, FPP, respectively:
    F1 is the number of filters in the 1x1 convolution
    F3R is the number of filters in the 1x1 convolution before the 3x3 convolution
    F3 is the number of filters in the 3x3 convolution
    F5R is the number of filters in the 1x1 convolution before the 5x5 convolution
    F5 is the number of filters in the 5x5 convolution
    FPP is the number of filters in the 1x1 convolution after the max pooling
    All convolutions inside the inception block should use a rectified linear activation (ReLU)
    Returns: the concatenated output of the inception block
    """
    F1, F3R, F3,F5R, F5, FPP = filters
    # extract variables from list filters via direct assignment
