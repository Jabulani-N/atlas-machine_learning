#!/usr/bin/env python3
"""module documentation
placeholder
"""


import numpy as np


def likelihood(x, n, P):
    """
    calculates likelihood given various probabilities
    x is the number of occurances
    n is the total number of instances checked
    P is a 1D numpy.ndarray
        containing various hypothetical probabilities of occurance
        you'll look at each one independantly
            do a calculation for each probability within P

    returns liklihood via Bayes Rule
"""
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if type(P) is not np.ndarray or np.ndim(P) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    for value in P:
        if value < 0 or value > 1:
            raise ValueError("All values in P must be in the range [0, 1]")

    k = x
    binCoeff = binomial(n, k)
    likelihoods = []
    for p in P:
        likelihoods.append(binCoeff *
                           (1 - p) ** (n - k))
    return likelihoods


def binomial(n, k):
    """calculates binomial coefficient"""
    return (np.math.factorial(n) /
            (np.math.factorial(k) *
             np.math.factorial(n - k)))
