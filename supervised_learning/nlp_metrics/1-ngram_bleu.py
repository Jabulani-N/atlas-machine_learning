#!/usr/bin/env python3
"""
this module
    calculates the N-gram BLEU score of a sentence
"""

import numpy as np
import collections
import math


def ngram_bleu(references, sentence, n):
    """
    this is a machine translation metric

    references = list of reference translations
        each is a list of words in the translation

    sentence = list containing the model proposed sentence

    n = size of n-gram used for evaluation
    """
    # prepare list
    precisions = []
    for i in range(1, n+1):
        reference_ngrams = collections.Counter()
        candidate_ngrams = collections.Counter()

        for reference in references:
            reference_ngrams.update(
                zip(*[reference[j:] for j in range(i)]))

        candidate_ngrams.update(
            zip(*[sentence[j:] for j in range(i)]))

        common_ngrams = candidate_ngrams & reference_ngrams
        precision = sum(common_ngrams.values()) / max(
            1, sum(candidate_ngrams.values()))

        precisions.append(precision)

    reference_lengths = [len(ref) for ref in references]
    closest_ref_length = min(
      reference_lengths,
      key=lambda x: abs(len(sentence) - x))

    if len(sentence) < closest_ref_length:
        brevity_penalty = math.exp(1 - closest_ref_length / len(sentence))
    else:
        brevity_penalty = 1.0

    bleu_score = brevity_penalty * math.exp(
        sum(math.log(p) for p in precisions)
        / len(precisions))

    return bleu_score
