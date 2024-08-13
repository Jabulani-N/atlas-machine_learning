#!/usr/bin/env python3
"""
machine translation module
expands upon task 0
    class
        Dataset
            add method
                encode(self, pt, en)
            edit method
                __init__
"""

import tensorflow_datasets as tfds
import numpy as np


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
        # the below must be None for task0, but here we need it
        self.tokenizer_pt, self.tokenizer_en =\
            self.tokenize_dataset(self.data_train)

    def tokenize_dataset(self, data):
        """
        divides data into tokens
            "tokens" are words, punctuation, etc
        data = tf.data.Dataset
            dataset of tuples of (pt, en)
                pt = tf.Tensor holding Pt sentence
                en = tf.Tensor holding En sentence
        """
        encoder = tfds.deprecated.text.SubwordTextEncoder
        tokenizer_pt = encoder.build_from_corpus(
            (pt.numpy() for pt, en in data), target_vocab_size=2**15
        )
        tokenizer_en = encoder.build_from_corpus(
            (en.numpy() for pt, en in data), target_vocab_size=2**15
        )
        # self.tokenizer_en = tokenizer_en
        # self.tokenizer_pt = tokenizer_pt
        return tokenizer_pt, tokenizer_en

    def encode(self, pt, en):
        """
        encodes a translation INTO tokens
        pt = tf.Tensor holding Pt sentence
        en = tf.Tensor holding En sentence
        """
        # data = (pt, en)
        # tokenizer_pt, tokenizer_en = self.tokenize_dataset(data)
        start_token = [self.tokenizer_pt.vocab_size]
        end_token = [self.tokenizer_pt.vocab_size + 1]
        # start_token = [tokenizer_pt.vocab_size]
        # end_token = [tokenizer_pt.vocab_size + 1]
        pt_tokens = np.array(start_token + self.tokenizer_pt.encode(pt.numpy()) + end_token)
        start_token = [self.tokenizer_en.vocab_size]
        end_token = [self.tokenizer_en.vocab_size + 1]
        # start_token = [tokenizer_en.vocab_size]
        # end_token = [tokenizer_en.vocab_size + 1]
        en_tokens = np.array(start_token + self.tokenizer_en.encode(en.numpy()) + end_token)
        return pt_tokens, en_tokens
