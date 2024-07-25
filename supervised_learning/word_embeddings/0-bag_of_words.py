#!/usr/bin/env python3
"""
This module contains one function
"""

import numpy as np


def bag_of_words(sentences, vocab=None):
    """
    sumulates bag-of-words embedding

    sentences = list of sentences
    vocab = list of words to use for analysis
        if = None, use all words within sentences

    convert each "sentence" into a one-hot array of whether it has each word
        words in alphabetical order
    """
    num_of_sentences = np.shape(sentences)[0]
    # number_of_sentences = len(sentences)
    if vocab is None:
        words = dupe_slayer(sentences)
        words = sent_preprocess(words)
        words = dupe_slayer(words)
        words = sent_preprocess(words)
    else:
        words = dupe_slayer(vocab)
        words = sent_preprocess(words)
        words = dupe_slayer(words)
        words = sent_preprocess(words)
    num_of_vocab_words = len(words)
    onehot_bag = np.zeros((num_of_sentences, num_of_vocab_words))
    for sentence_num in range(num_of_sentences):
        for word_num in range(num_of_vocab_words):
            onehot_bag[sentence_num][word_num] =\
                sent_preprocess([sentences[sentence_num]]).count(
                    words[word_num])
    return onehot_bag, words


def sent_preprocess(sentences):
    """
    returns a list of individual words from
        string
        list of sentences
    slays duplicates via "list(set())"
    converts to lowercase
    alphabetizes
    removes `'s`
    """
    if isinstance(sentences, list) or\
       isinstance(sentences, tuple) or\
       isinstance(sentences, dict):
        catted = " ".join(sentences)
    else:
        catted = sentences

    lower_catted = catted.lower()
    words = lower_catted.split(" ")
    # words = non-alphebetized, otherwise formatted list
    deconjugated = deconjugate(words)
    alphabetized_words = sorted(deconjugated)
    return alphabetized_words


def dupe_slayer(words_words_words):
    """
    slays duplicates
    items will no longer be in alphabetial order
    """
    return list(set(words_words_words))


def deconjugate(words):
    """
    removes conjugation
    from strings
    in list of strings
    """
    deconjugated = [term.replace("'s", "") for term in words]
    deconjugated = [term.replace("!", "") for term in deconjugated]
    deconjugated = [term.replace(".", "") for term in deconjugated]
    deconjugated = [term.replace("?", "") for term in deconjugated]
    return deconjugated


def close_enough(word1, word2):
    """
    if word1 is a conjugated form of word2
        or vice-versa
        or identical
    returns true
    """
    dec1 = deconjugate(word1)
    dec2 = deconjugate(word2)
    # print("word 1 is", word1)
    # print("word 2 is", word2)
    # print("dec 1 is", dec1)
    # print("dec 2 is", dec2)
    if dec1 == dec2:
        return True
    else:
        return False
