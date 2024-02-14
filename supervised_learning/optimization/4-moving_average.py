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
    mov_avg = np.zeros(len(data))
    mov_avg[0] = data[0]

    for i in range(1, len(data)):
        mov_avg[i] = (beta * data[i]) +\
                     ((1 - beta) * mov_avg[i - 1])
        # the following line is bias correction
        mov_avg[i] = mov_avg[i] / (1 - beta**(i + 1))
    return mov_avg
