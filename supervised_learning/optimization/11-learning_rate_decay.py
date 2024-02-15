#!/usr/bin/env python3
"""module documentation
this module creates a function.

"""


import numpy as np


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """
    alpha = original learning rate
    decay_rate = weight used to determine the rate at which alpha will decay
    global_step = number of gradient descent passes elapsed
    decay_step = number of gradient descent passes that occur
        before alpha is decayed further
    the learning rate decay should occur in a stepwise fashion
    Returns: the updated value for alpha
    """
    alpha_new = alpha / (1 + decay_rate *
                         (global_step // decay_step))
    return alpha_new
