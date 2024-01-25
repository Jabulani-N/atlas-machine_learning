#!/usr/bin/env python3
"""module documentation
this module, 3-neuron.py, creates a class: Neuron

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

        Private instance attributes:
        W: initialized using random normal distribution.
        b: initialized to 0.
        A: initialized to 0.

        """

        if isinstance(nx, int) is False:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__nx = nx
        self.__W = np.random.normal(size=(1, nx))
        # had to reference myself to figure out this line.
        # don't remember original source
        #   treat as source model in future references
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """returns weights"""
        return self.__W

    @property
    def b(self):
        """returns bias"""
        return self.__b

    @property
    def A(self):
        """returns prediction (output; 'answer')"""
        return self.__A

    def forward_prop(self, X):
        """__A = sigmoid function on X"""
        self.__A = self.sigmoid(np.matmul(self.__W, X) + self.__b)
        return self.__A

    def sigmoid(self, z):
        """returns sigmoid function of z"""
        return (1 / (1 + np.exp(-1 * z)))

    def logistic_reg(self, X):
        """returns logistic regression of array X
        This calculation proved obsolete: we needed COST, not LOSS
        """
        return self.sigmoid(np.transpose(self.__W) * X + self.__b)

    def cost(self, Y, A):
        """returns loss function of A; Y is the correct answer
        A = ŷ = yhat. Y is y.

        avoids dividing by 0 via
            1.0000001 - A instead of 1 - A
        """

        m = np.shape(A)[0]
        yhati = A
        yi = Y
        return ((-1 / m) *
                np.sum(yi * np.log(yhati) +
                (1 - yi) * (np.log(1.0000001 - yhati))))
