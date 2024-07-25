#!/usr/bin/env python3
"""
This module contains one function
"""


def bag_of_words(sentences, vocab=None):
    """
    sumulates bag-of-words embedding

    sentences = list of sentences
    vocab = list of words to use for analysis
        if = None, use all words within sentences
    """
    pass

def word_extractor(sentences):
    """
    returns a list of individual words from a LIST of sentences
    recieve the list of sentences, make a list of
    slays duplicates via "list(set())"
    """
    if isinstance(sentences, list) or\
       isinstance(sentences, tuple) or\
       isinstance(sentences, dict):
        catted = " ".join(sentences)
    else:
        catted = sentences

    words_words_words = catted.split(" ")
    words = list(set(words_words_words))
    return words