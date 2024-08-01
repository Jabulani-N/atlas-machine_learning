#!/usr/bin/env python3
"""
this module
    calculates the N-gram BLEU score of a sentence
"""

import numpy as np
import collections
import math


def cumulative_bleu(references, sentence, n):
    """
    calculates cumulative by averaging
    all ngram scores up to n
    """
    return ngram_bleu(references, sentence, n)
    sky_high_bleu = 0
    for i in range(n, 0, -1):
        sky_high_bleu += ngram_bleu(references, sentence, i)
    bleu_cum = sky_high_bleu / n
    return bleu_cum


def ngram_bleu(references, sentence, n):
    """
    this second attempt was guided by multiple explanations
    this is a machine translation metric

    references = list of reference translations
        each is a list of words in the translation

    sentence = list containing the model proposed sentence

    n = size of n-gram used for evaluation
    """
    sentence_ngrams = calculate_ngrams(sentence, n)
    # dictionary to store  counts for each word
    sentence_counts = collections.Counter(sentence_ngrams)

    max_counts = {}

    for ref_sentence in references:
        current_ref_ngrams = calculate_ngrams(ref_sentence, n)
        current_ref_counts = collections.Counter(current_ref_ngrams)
        # see the most times each word is used in a given translation
        for word in current_ref_counts:
            if word in max_counts:
                max_counts[word] = max(
                    max_counts[word],
                    current_ref_counts[word])
            else:
                max_counts[word] = current_ref_counts[word]

    clipped_counts = {word: min(count, max_counts.get(word, 0)) for word,
                      count in sentence_counts.items()}

    bleu_score = sum(clipped_counts.values())\
        / max(sum(sentence_counts.values()), 1)

    reference_lengths = [len(ref) for ref in references]
    closest_ref_length = min(
      reference_lengths,
      key=lambda x: abs(len(sentence) - x))
    # calculate brevery penalty
    if len(sentence) < closest_ref_length:
        brevity_penalty = math.exp(1 - closest_ref_length / len(sentence))
    else:
        brevity_penalty = 1.0

    bleu_score = brevity_penalty * bleu_score
    return bleu_score


def calculate_ngrams(words, n):
    """
    calculates ngrams from list of words
        makes a
            1gram
            2gram
            3gram
            etc...
    words = list of words
    n = size of n-gram used for evaluation
    """
    wordcount = len(words)
    return [tuple(words[i:i+n]) for i in range(wordcount - n + 1)]
