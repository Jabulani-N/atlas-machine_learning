#!/usr/bin/env python3
"""
word2vec → keras embedding layer
"""

import numpy as np
from gensim.models import Word2Vec
from keras.models import Sequential
from keras.layers import Embedding


def gensim_to_keras(model):
    """
    converts a gensim word2vec model
        to keras embedding layer

    model = trained gensim word2vec model
    """
    # structure holding the result of training
    keyed_vectors = model.wv
    # vectors themselves, a 2D numpy array
    weights = keyed_vectors.vectors
    # which row in `weights` corresponds to which word?
    index_to_key = keyed_vectors.index_to_key
    train_embeddings = False
    keras_model = Embedding(
        input_dim=weights.shape[0],
        output_dim=weights.shape[1],
        weights=[weights],
        trainable=train_embeddings,
    )
    return keras_model
