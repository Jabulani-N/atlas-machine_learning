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
    Returns:
        boolean of whether the network should be stopped early
        updated count
    """
    if cost >= opt_cost - threshold:
        count += 1
        if count >= patience:
            return True, count
    else:
        count = 0
    return False, count
