# Implimenting Transfer Learning to Train a Keras Model to Label the CIFAR10 Dataset


## Contents
- [Abstract](#abstract)
- [Introduction](#introduction)
- [Materials and Methods](#materials-and-methods)
- [Results](#results)
- [Discussion](#discussion)
- [Literature Cited](#literature-cited)

![visual example of off the shelf model as feature extractor](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*qfQ3hmHLwApXZBN-A85r8g.png)

## Abstract

Following guidance of multiple sources, the EfficientNetB7 Keras model was imported, and  parameters manipulated in order to create a new model to identify the CIFAR10 (cifar10, cif10) Dataset. The top layer was not imported; a new top layer was created instead. A Lambda layer was used to convert the cif10 data into a size EfficientNet is used to categorizing. Techniques utilized include Dropout and Data Augmentation. Early Stopping is utilized to limit wasted resources.

## Introduction

The success criterion of this project is the creation of a neural network that will classify the CIFAT10 dataset. In theory, this could be done by creating and training a model from scratch, but the *purpose* of this project is learning how much better a choice it is to Transfer Learning from another, already-made neural network model. Doing this, we'll utilize the open-source and freely distributed work of others to give our own work a head start. Heightening our perspective by standing on the shoulders of giants, so to speak.

A lambda layer and output layer were used to respectively prepare the data to match the trained layers, and to direct the labelling to be relevant for the task at hand.

To train the models specificaly for the domain of the CIFAR10 dataset, it was  trained as normal, but the weights of the layers downloaded were kept frozen, so their training is not wasted.

## Materials and Methods

The project was begun by importing the data from the cifar10 dataset. This data was used as both training data and testing or "validation" data.

The preprocessing operation was written to take place in an indepenant function. As such, it is maximally portable for other applicaitons.

The "Transfer Learning" part of the project came in the form of importing the `EfficientNetB7` Keras application, and with it, the weights associated with the CIFAR10 dataset. The top layer is omitted. The model is directly created from these specifications and frozen. These frozen layers are not retrained at any point.

To replace the omitted top layer, a pooling keras layer is created, recieving the previous, frozen model as input. Following this are a normlaization layer with dropout, a dense ReLu layer, and finally a softmax output layer. All layers are put into creating a single Keras model, compiled with an Adam optimizer, and `model.fit` was used in creating a model to save under the name `cifar10.h5`.

These are the steps taken for the purposes of creating a model. The follwoing was done to improve training efficacy and efficiency:

* multiple learning rates were used, including `0.0005`, `0.0007`, the default `0.001`, and `0.0015`.
* Data augmentation was used to train on rotated, stretched, and flipped versions of traing images.
* Early Stopping was utilized when training, limiting resource waste potentially caused by a large epoch count.
* Dropout was used on trainable layers, including rates of `0.35`, and `0.25`

A Lambda layer was created to resize the input images. As EfficientNet is trained on images of various sizes, up to 600x600 pixels, a Keras Lambda layer is used to scale up the 32x32 cif10 input.
## Results

All training methods peaked at a validation accuracy of approximately `0.32 ±0.01`.

Comparing learning rates: 0.0005 was the most effective tested rate, followed by 0.0007, the default, 0.001 and greater than default values respectively. Early stopping was used with settings to preserve weights producing the best results when testing. 

Comparing results of dropout settings, the lower setting of 0.25 provided better results than 0.35. 0.35 dropout rate never exceeded validation accuracy of 0.3 in any epohch tested.

After introducing a Lambda layer, validation accuracy never fell below `0.85`.

## Discussion

Due to the lack of a lambda layer to convert training images into a more useful size, the efficacy of training was lightly limited, despite the use of data augmentation. It is possible that utilizing a different number of custom trainable layers would have influenced results, though testing is needed. 

Various dropout rates may produce different results if the number of trainable layers is changed.

As all later training sessions ended via early stopping, it is unlikely that increasing epoch count would improve results, unless other parameters were simultaneously changed.

After the addition of a lambda layer, results were immediately improved, and training time was drastically increased per epoch. The massive increase in efficacy is too great to decline, so further improvements would perhaps best be targeted in increasing training speed instead of validation accuracy.

Following
## Literature Cited

[you.com](you.com)'s was referenced for interpretation, syntax corrections, and terminology.

[Introdtion to Transfer Learning](https://www.youtube.com/watch?v=FQM13HkEfBk&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF&index=20:) was heavily referenced for conceptual understanding.

[Nuts and Bolts of AI Applications](#nuts-and-bolts-of-ai-applications-using-deep-learning-by-andrew-ng) was referenced for conceptual understanding.

A [Comprehensive Hands-on Guide to Transfer Learning](https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a) to Transfer Learning was heavily referenced for conceptual understanding and for visual aides.

[stack**overflow**](https://stackoverflow.com/questions/72927229/nameerror-name-scipy-is-not-defined-when-trying-to-create-a-model) was referenced for multiple solutions to simple problems, such as prerequisite installs for running training locally

[Google Colab](https://colab.research.google.com/drive/1FqqntBh4D66uG2p6p8Kj6loOfP71WtoV?usp=sharing) was used as a testing environment and recordkeeper.
