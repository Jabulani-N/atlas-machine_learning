#!/usr/bin/env python3
"""module documentation
this module, 21-deep_neural_network.py,
creates a class: DeepNeuralNetwork

"""

import numpy as np


class DeepNeuralNetwork:
    """Object-class summary documentation.

    Attributes:
        L - number of layers
        cache - dictionary holding intermediary values. initialized empty.
        weights - dictionary holding weights and biases.

    """

    def __init__(self, nx, layers):
        """nx = no of input features = no nodes in input layer(?)
        layers = list containing no of nodes in each layer
        """

        if isinstance(nx, int) is False:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        if isinstance(layers, list) is False or layers == []:
            raise TypeError("layers must be a list of positive integers")
        if all(np.greater_equal(layers, 1)) is False:
            raise TypeError("layers must be a list of positive integers")

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for layer in range(0, self.L):
            if isinstance(layers[layer], int) is False:
                raise TypeError("layers must be a list of positive integers")
            # I reread the review, and only my W1 answer is incorrect
            if layer == 0:
                # print("i'm using the special layer loop")
                self.__weights['W' + str(layer + 1)] = \
                    (np.random.randn(layers[layer], nx) *
                     np.sqrt(2. / nx))
            else:
                self.__weights['W' + str(layer + 1)] = \
                    np.random.randn(layers[layer],
                                    layers[layer - 1]) *\
                    np.sqrt(2. / layers[layer - 1])

            self.__weights['b' + str(layer + 1)] = \
                np.zeros((layers[layer], 1))
        # weights initialized via he et al.

    @property
    def L(self):
        """returns number of layers"""
        return self.__L

    @property
    def cache(self):
        """returns the current cache
        cache is a dictionary to holding
        all intermediary values of the network.
        """

        return self.__cache

    @property
    def weights(self):
        """returns dictionary holding all weights and biases"""
        return self.__weights

    def sigmoid(self, z):
        """returns sigmoid function of z"""
        return (1 / (1 + np.exp(-1 * z)))

    def forward_prop(self, X):
        """performs a single pass of forward propagation"""

        self.__cache['A0'] = X
        for layNum in range(self.__L):
            self.__cache['A' + str(layNum + 1)] =\
                self.sigmoid(
                    np.matmul(self.__weights['W' + str(layNum + 1)],
                              self.__cache['A' + str(layNum)]) +
                    self.__weights['b' + str(layNum + 1)])
        return self.cache['A' + str(self.L)], self.cache

    def cost(self, Y, A):
        """calculates and returns cost of a single forward prop"""
        m = np.shape(A)[1]
        yhati = A
        yi = Y
        return (np.sum(yi * np.log(yhati) +
                (1 - yi) * (np.log(1.0000001 - yhati)))
                / -m)

    def evaluate(self, X, Y):
        """evaluates prediction X vs correct answer Y
        considers anything at least 0.5 as 1; else 0
        """
        self.forward_prop(X)[1]
        Prediction = np.greater_equal(self.cache['A' + str(self.L)],
                                      0.5).astype(int)
        return Prediction, self.cost(Y,
                                     self.cache['A' + str(self.L)])

    def gradient_descent(self, Y, cache, alpha=0.05):
        """updates own weight and bias elements by
        learning rate * gradient of cost
        alpha = α = learning rate
        """
        m = np.shape(Y)[1]
        # dz = cache['A' + str(self.L)] - Y
        # dw = np.dot(cache['A0'], dz.T) / m
        # db = np.sum(dz) / m
        # self.__weights -= alpha * dw.T
        # self.__b -= alpha * db
        dzPrev = Y[self.L]
        for layer in reversed(range(0, self.L)):
            dzCurrent = cache['A' + str(layer)] - dzPrev
            dwCurrent = np.dot(cache['A' + str(layer)], dzCurrent.T) / m
            dbCurrent = np.sum(dzCurrent, axis=1, keepdims=True) / m
            # if this doesn't work, considreremoving axis=1, et al.
            self.weights['W' + layer] -= alpha * dwCurrent.T
            self.weights['b' + layer] -= alpha * dbCurrent
            dzPrev = dzCurrent
