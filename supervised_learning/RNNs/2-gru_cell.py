#!/usr/bin/env python3
"""
This module creates the class GRUCell
This class illustrates the function of
a Gated Recurrant  Network
"""

import numpy as np


class GRUCell:
    """simulates a gated ecurrant network"""
    def __init__(self, i, h, o):
        """initiates the class
        i, h, o = dimensionality of
            input data
            hiden state
            outputs
        w = weights
        b = bias

        z = forget gate
        r = update gate
        h = intermediate hidden state
        h = output gate
        y = outputs
        """
        # random NORMAL distribution
        random = np.random.randn
        # I'll assume all gates use hidden state dimensions


