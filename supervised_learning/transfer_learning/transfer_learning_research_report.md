# Implimenting Transfer Learning to Train a Keras Model to Label the CIFAR10 Dataset

## Contents
- [Abstract](#abstract)
- [Introduction](#introduction)
- [Materials and Methods](#materials-and-methods)
- [Results](#results)
- [Discussion](#discussion)
- [Literature Cited](#literature-cited)

## Abstract

Following guidance of multiple sources, the EfficientNetB7 Keras model was imported, and  parameters manipulated in order to create a new model to identify the CIFAR10 (cifar10, cif10) Dataset. The top layer was not imported; a new top layer was created instead. Techniques utilized include Dropout and Data Augmentation. Early Stopping is utilized to limit wasted resources.

## Introduction

The success criterion of this project is the creation of a neural network that will classify the CIFAT10 dataset. In theory, this could be done by creating and training a model from scratch, but the *purpose* of this project is learning how much better a choice it is to Transfer Learning from another, already-made neural network model. Doing this, we'll utilize the open-source and freely distributed work of others to give our own work a head start. Heightening our perspective by standing on the shoulders of giants, so to speak.

A lambda layer and output layer should be used to prepare the data to match the trained layers, and to direct the labelling to be relevant for the task at hand.

To train the models specificaly for the domain of the CIFAR10 dataset, it was  trained as normal, but the weights of the layers downloaded were kept frozen, so their training is not wasted.

## Materials and Methods

The project was begun by importing the data from the cifar10 dataset. This data was used as both training data and testing or "validation" data.

The preprocessing operation was written to take place in an indepenant function. As such, it is maximally portable for other applicaitons.

The "Transfer Learning" part of the project came in the form of importing the `EfficientNetB7` Keras application, and with it, the weights associated with the CIFAR10 dataset. The top layer is omitted. The model is directly created from these specifications and frozen. These frozen layers are not retrained at any point.

To replace the omitted top layer, a pooling keras layer is created, recieving the previous, frozen model as input. Following this are a normlaization layer with dropout, a dense ReLu layer, and finally a softmax output layer. All layers are put into creating a single Keras model, compiled with an Adam optimizer, and `model.fit` was used in creating a model to save under the name `cifar10.h5`.



## Results

## Discussion

## Literature Cited
