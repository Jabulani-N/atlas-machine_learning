#!/usr/bin/env python3
"""module documentation
this module,0-create_placeholders, creates a function:
    create_placeholders
Though classy, it has no class.

"""

import numpy as np


class RNNCell:
    """reprecents a cell of simple RNN"""
    def __init__(self, i, h, o):
        """
        class initiator
        i, h, o = dimensionality of:
            input, hidden state, output
        """
        random = np.random.rand
        # weights of the cell
        self.Wh = random(h + i, h)
        self.Wy = random(h, o)
        # biases of the cell
        self.bh = np.zeros((1, h))
        self.by = np.zeros((1, o))
