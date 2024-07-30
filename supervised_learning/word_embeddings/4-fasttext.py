#!/usr/bin/env python3
"""
word2vec → keras embedding layer
"""

import numpy as np
from gensim.models import FastText
from keras.models import Sequential
from keras.layers import Embedding


def fasttext_model(sentences, size=100, min_count=5,
                   negative=5, window=5, cbow=True,
                   iterations=5, seed=0, workers=1):
    """
    creates and trains a gensim fastText model

    sentences is a list of sentences to be trained on
    size is the dimensionality of the embedding layer
    min_count is the minimum number of occurrences of a word for use in training
    window is the maximum distance between the current and predicted word within a sentence
    negative is the size of negative sampling
    cbow is a boolean to determine the training type; True is for CBOW; False is for Skip-gram
    iterations is the number of iterations to train over
    seed is the seed for the random number generator
    workers is the number of worker threads to train the model

    sg = skip gram
    cbow = continuous bag of words
    sg = opposite of cbow
    """
    model = FastText(sentences, vector_size=size, window=window,
                     min_count=min_count,
                     sg=(not cbow), negative=negative,
                     epochs=iterations, seed=seed, workers=workers)
    return model
