#!/usr/bin/env python3
"""this module creates a function."""


import numpy as np


def early_stopping(cost, opt_cost, threshold, patience, count):
    """
    Early stopping = true when
        cost of the network has not decreased relative to the optimal cost by
            more than the threshold over a specific patience count
    cost is the current validation cost of the neural network
    opt_cost is the lowest recorded validation cost of the neural network
    threshold is the threshold used for early stopping
    patience is the patience count used for early stopping
    count is the count of how long the threshold has not been met
    Returns: a boolean of whether the network should be stopped early, followed by the updated count
    """
    if count <= patience:
        count += 1
        return False, count
    else:
        if opt_cost - threshold < cost:
            count += 1
            return True, count
    return False, count
