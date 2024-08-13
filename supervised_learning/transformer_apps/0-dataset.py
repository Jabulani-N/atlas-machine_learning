#!/usr/bin/env python3
"""machine translation module"""

import tensorflow_datasets as tfds
import numpy


class Dataset:
    def __init__(self):
        """
        creates a datasest of what is to be used in mtl
        """
        # gets an already created training dataset
        # training portion
        self.data_train = tfds.load('ted_hrlr_translate/pt_to_en',
                                    split='train',
                                    as_supervised=True)
        # validation portion
        self.data_valid = tfds.load('ted_hrlr_translate/pt_to_en',
                                    split='validation',
                                    as_supervised=True)
        self.tokenizer_pt, self.tokenizer_en =\
            self.tokenize_dataset(self.data_train)

    def tokenize_dataset(self, data):
        """
        divides data into tokens
            words, punctuation, etc
        """
        encoder = tfds.deprecated.text.SubwordTextEncoder
        tokenizer_pt = encoder.build_from_corpus(
            (pt.numpy() for pt, en in data), target_vocab_size=2**15
        )
        tokenizer_en = encoder.build_from_corpus(
            (en.numpy() for pt, en in data), target_vocab_size=2**15
        )
        return tokenizer_pt, tokenizer_en
