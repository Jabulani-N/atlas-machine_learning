#!/usr/bin/env python3
"""module documentation
this module, 13-neural_network.py, creates a class: NeuralNetwork

"""

import numpy as np


class NeuralNetwork:
    """Object-class summary documentation.

    Attributes:
        W1 - weights vector for hidden layer
        b1 - bias of hidden layer.
        A1 - output of hidden layer.
        W2 - weights vector for output neuron
        b2 - bias of output neuron.
        A2 - output of output neuron.

    """

    def __init__(self, nx, nodes):
        """nx = no of input features
        nodes = no of nodes in hidden layer
        """

        if isinstance(nx, int) is False:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        if isinstance(nodes, int) is False:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.__W1 = np.random.normal(size=(nodes, nx))
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.normal(size=(1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """returns weights of hidden layer inputs"""
        return self.__W1

    @property
    def W2(self):
        """returns weights of output layer inputs"""
        return self.__W2

    @property
    def W1(self):
        """returns weights of hidden layer inputs"""
        return self.__W1

    @property
    def b1(self):
        """returns biases of each hidden layer node as array of arrays"""
        return self.__b1

    @property
    def b2(self):
        """returns bias of output node"""
        return self.__b2

    @property
    def A1(self):
        """returns prediction (output) of hidden layer"""
        return self.__A1

    @property
    def A2(self):
        """returns prediction output node"""
        return self.__A2

    def forward_prop(self, X):
        """calculates the forward propagation of the neural network
        A = sigmoid function on  input
        X = input array
        """
        self.__A1 = self.sigmoid(np.matmul(self.__W1, X) + self.__b1)
        self.__A2 = self.sigmoid(np.matmul(self.__W2, self.__A1) + self.__b2)
        return self.__A1, self.__A2

    def sigmoid(self, z):
        """returns sigmoid function of z"""
        return (1 / (1 + np.exp(-1 * z)))

    def cost(self, Y, A):
        """calculates and reutrns cost of a single forward propagation"""
        m = np.shape(A)[1]
        yhati = A
        yi = Y
        return (np.sum(yi * np.log(yhati) +
                (1 - yi) * (np.log(1.0000001 - yhati)))
                / -m)

    def evaluate(self, X, Y):
        """Evaluates one pass of forward propagation.
        X = input data
        Y = correct answer, as used by cost function

        considers anything at least 0.5 as 1; else 0.
        """
        Prediction = np.greater_equal(self.forward_prop(X)[1], 0.5).astype(int)
        return Prediction, self.cost(Y, self.__A2)
        # this is only assigning the __A2 value to Prediction

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """updates self W1,W2,b1,b2 by learning rate * gradient of cost
        alpha = α = learning rate
        """

        m = np.shape(Y)[1]
        dz1 = A1 - Y
        dw1 = np.dot(X, dz1.T) / m
        db1 = np.sum(dz1) / m
        print("the shape of W1 is", np.shape(self.__W1))
        print("the shape of dw1.t is", np.shape(dw1.T))
        self.__W1 -= alpha * dw1.T
        self.__b1 -= alpha * db1

        m = np.shape(Y)[1]
        dz2 = A2 - Y
        dw2 = np.dot(X, dz2.T) / m
        db2 = np.sum(dz2) / m
        self.__W2 -= alpha * dw2.T
        self.__b2 -= alpha * db2
