#!/usr/bin/env python3
"""module documentation
this module creates a function:
    moving_average

"""


import numpy as np


def moving_average(data, beta):
    """calculates the exponential moving average
    of datalist data.
    beta = weight
        this is represented as 'alpha' or 'α' by some.
    """
    n = len(data)
    avg = 0.0
    mov_avg = []

    for k in range(0, n):
        EMA = beta * avg + (1 - beta) * data[k]
        mov_avg.append(EMA / (1 - beta**(k + 1)))
    # the following line is bias correction
        avg = EMA
    return mov_avg
