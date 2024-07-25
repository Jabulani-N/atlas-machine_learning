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

    convert each "sentence" into a one-hot array of whether it has each word
        words in alphabetical order
    """
    if vocab is None:
        words = word_preprocessor(sentences)
    else:
        words = word_preprocessor(vocab)


def word_preprocessor(sentences):
    """
    returns a list of individual words from
        string
        list of sentences
    slays duplicates via "list(set())"
    converts to lowercase
    alphabetizes
    """
    if isinstance(sentences, list) or\
       isinstance(sentences, tuple) or\
       isinstance(sentences, dict):
        catted = " ".join(sentences)
    else:
        catted = sentences

    lower_catted = catted.lower()
    words_words_words = lower_catted.split(" ")
    # words = non-alphebetized, otherwise formatted list
    words = list(set(words_words_words))
    alphabetized_words = sorted(words)
    return alphabetized_words
