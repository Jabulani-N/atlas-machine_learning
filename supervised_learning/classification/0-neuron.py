#!/usr/bin/env python3
"""module documentation
this module, 0-neuron.py, creates a class: Neuron
Documentation must precisely match this document to be correct

"""
import numpy as np


class Neuron:
    """Object-class summary documentation.

    Attributes:
        W - weights. Upon instantiation, initialized to
            random normal distribution.
        b - bias of the neuron. Upon instantiation,initialized to 0.
        A -output. Upon instantiation,initialized to 0.

    """

    def __init__(self, nx):
        """__init__ method documentation

        __init__ can optionally instead be documented in the class section
        do not include 'self' as an arg

        nx is the number of input features to the neuron
            If nx is not  integer, raise TypeError: "nx must be an integer"
            If nx < 1, raise ValueError: "nx must be a positive integer"
            IN THAT ORDER

        Public instance attributes:
        W: initialized using random normal distribution.
        b: initialized to 0.
        A: initialized to 0.

        """

        if isinstance(nx, int) is False:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__nx = nx
        self.W = np.random.normal(size=(1, nx))
        # had to reference myself to figure out this line.
        # don't remember original source
        #   treat as source model in future references
        self.b = 0
        self.A = 0
