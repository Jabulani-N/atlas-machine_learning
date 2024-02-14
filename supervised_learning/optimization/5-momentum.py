#!/usr/bin/env python3
"""module documentation
this module creates a function.

"""


import numpy as np


def update_variables_momentum(alpha, beta1, var, grad, v):
    """`alpha` = learning rate
`beta1` = momentum weight
`var` = numpy.ndarray containing the variable to be updated
`grad` = numpy.ndarray containing the gradient of var
`v` = previous first moment of var
"""
    moment = np.add(np.multiply(beta1, v),
                    np.multiply((1 - beta1), grad))
    updated_var = np.subtract(var, np.multiply(alpha, v))
    return updated_var, moment
