#!/usr/bin/env python3
"""module documentation
this module creates a function.

"""


import numpy as np


def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    """`alpha` = learning rate
    `beta2` = RMSProp weight
    `epsilon` = small number to avoid division by zero
    `var` = numpy.ndarray containing the variable to be updated
    `grad` = numpy.ndarray containing the gradient of var
    `s` = previous second moment of var
    """
    moment2 = np.multiply(beta2, np.add(s,
                                        np.multiply((1 - beta2),
                                                    np.square(grad))))
    # Update var using the NEW second moment
    updated_var = np.subtract(var,
                              np.multiply(alpha,
                                          (np.divide(grad,
                                                     (np.add(np.sqrt(moment2),
                                                             epsilon))))))
    return updated_var, moment2
