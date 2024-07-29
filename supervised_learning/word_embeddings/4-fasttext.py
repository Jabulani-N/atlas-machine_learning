#!/usr/bin/env python3
"""
word2vec → keras embedding layer
"""

import numpy as np
from gensim.models import Word2Vec
from keras.models import Sequential
from keras.layers import Embedding


def fasttext_model(sentences, size=100, min_count=5, negative=5, window=5, cbow=True, iterations=5, seed=0, workers=1):
    """temporary doc"""
    pass
