#!/usr/bin/env python3

import numpy as np
import collections
import math


def uni_bleu(references, sentence):
    """
    this is a machine translation metric

    references = list of reference translations
        each is a list of words in the translation

    sentence = list containing the model proposed sentence
    """
    # prepare list
    precisions = []
    for i in range(1, 2):
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
