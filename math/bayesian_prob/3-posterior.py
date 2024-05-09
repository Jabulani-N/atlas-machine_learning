#!/usr/bin/env python3
"""module documentation
placeholder
"""


import numpy as np


def posterior(x, n, P, Pr):
    """calculates posterior probability"""
    lik = likelihood(x, n, P)
    prior = Pr
    marge = marginal(x, n, P, Pr)
    post = (lik * prior) / marge
    return post


def marginal(x, n, P, Pr):
    """calculates the marginal probability of obtaining the data"""
    inter = intersection(x, n, P, Pr)
    marge = np.sum(inter)
    return marge


def intersection(x, n, P, Pr):
    """calculates the intersection with `Pr`ior beliefs"""
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")
    if type(P) is not np.ndarray or np.ndim(P) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if type(Pr) is not np.ndarray or\
       np.shape(P) != np.shape(Pr):
        raise TypeError(
            "Pr must be a numpy.ndarray with the same shape as P")
    for p in P:
        if p < 0 or p > 1:
            raise ValueError(
                "All values in P must be in the range [0, 1]")
    for p in Pr:
        if p < 0 or p > 1:
            raise ValueError(
                "All values in Pr must be in the range [0, 1]")
    inter = likelihood(x, n, P) * Pr
    # inter /= np.sum(inter)
    return inter


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
    likelihoods = np.array([])
    for p in P:
        phrase = ((p ** k) * (1 - p) ** (n - k))
        lik = binCoeff * phrase
        likelihoods = np.append(likelihoods, lik)
    return likelihoods


def binomial(n, k):
    """calculates binomial coefficient"""
    return (np.math.factorial(n) /
            (np.math.factorial(k) *
             np.math.factorial(n - k)))
