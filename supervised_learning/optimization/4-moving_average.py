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
    mov_avg = np.zeros(n)
    mov_avg[0] = data[0]

    for k in range(1, n):
        mov_avg[k] = ((1 - beta) ** (n - k)) *\
                     (beta * data[k]) + data[n - 1]
        # the following line is bias correction
        mov_avg[k] = mov_avg[k] / (1 - beta**(k + 1))
    return mov_avg
