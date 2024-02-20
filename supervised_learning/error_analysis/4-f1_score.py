#!/usr/bin/env python3
"""module documentation
this module creates a function.

This is essenitally the inverse of task 1: sensitivity
instead of positives, we're working with negatives"""


import numpy as np


def f1_score(confusion):
    """placeholder documentation"""
    sensitivity = __import__('1-sensitivity').sensitivity
    precision = __import__('2-precision').precision

    product = np.multiply(sensitivity(confusion),
                          precision(confusion))
    sum = np.add(sensitivity(confusion),
                 precision(confusion))
    quotient = np.divide(product, sum)
    f1 = np.multiply(2, quotient)
    return f1
