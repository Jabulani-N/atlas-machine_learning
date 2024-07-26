#!/usr/bin/env python3
"""
This module contains one function
"""

import numpy as np
from gensim.models import Word2Vec
from collections.abc import Mapping


def word2vec_model(sentences, size=100, min_count=5,
                   window=5, negative=5, cbow=True,
                   iterations=5, seed=0, workers=1):
    """
    looks like it's time to learn about gensim
    """
    model = Word2Vec(sentences=sentences, vector_size=size,
                     window=window, min_count=min_count,
                     sg=(not cbow), negative=negative,
                     epochs=iterations, seed=seed, workers=workers)
    return model
