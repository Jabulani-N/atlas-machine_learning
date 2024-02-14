#!/usr/bin/env python3
"""module documentation
this module creates a function.

"""


import numpy as np


def update_variables_Adam(alpha, beta1, beta2,
                          epsilon, var, grad,
                          v, s, t):
    """alpha = learning rate
beta1 = weight used for the first moment
beta2 = weight used for the second moment
epsilon = small number to avoid division by zero
var = numpy.ndarray containing the variable to be updated
grad = numpy.ndarray containing the gradient of var
v = previous first moment of var
s = previous second moment of var
t = time step used for bias correction
"""
    vnew = beta1 * v + (1 - beta1) * grad
    snew = beta2 * s + (1 - beta2) * np.square(grad)

    vcorrect = vnew / (1 - beta1**t)
    scorrect = snew / (1 - beta2**t)
    var = var - alpha * (vcorrect / (np.sqrt(scorrect) + epsilon))
    return var, vcorrect, scorrect
