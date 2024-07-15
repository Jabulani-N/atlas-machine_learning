#!/usr/bin/env python3
"""
This module creates the class LSTMCell
This class illustrates the function of
a Gated Recurrant  Network
"""

import numpy as np


class LSTMCell:
    """simulates an LSTM unit"""
    def __init__(self, i, h, o):
        """initiates the class
        i, h, o = dimensionality of
            input data
            hidden state
            outputs

        f = forget gate
        u = update gate
        c = intermediate cell state
        y = outputs
        """
        # random NORMAL distribution
        random = np.random.randn
        # establish non-output weights
        self.Wf = random(h + i, h)
        self.Wu = random(h + i, h)
        self.Wo = random(h + i, h)
        # output weights
        self.Wy = random(h, o)
        # biases
        self.bf = random(h + i, h)
        self.bu = random(h + i, h)
        self.bo = random(h + i, h)
        self.by = random(h, o)
