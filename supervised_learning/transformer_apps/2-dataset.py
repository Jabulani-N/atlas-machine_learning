#!/usr/bin/env python3
"""
machine translation module
expands upon task 1
    class
        Dataset
            add method
                tf_encode(self, pt, en):
            edit method
                __init__
"""

import tensorflow_datasets as tfds
import tensorflow as tf
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
        self.tokenizer_pt, self.tokenizer_en =\
            self.tokenize_dataset(self.data_train)
        # uses tf_encode to turn train/valid data into tensor
        # so tensorflow can more easily work with it
        self.data_train = self.data_train.map(self.tf_encode)
        self.data_valid = self.data_valid.map(self.tf_encode)

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
        return tokenizer_pt, tokenizer_en

    def encode(self, pt, en):
        """
        encodes a translation INTO tokens
        pt = tf.Tensor holding Pt sentence
        en = tf.Tensor holding En sentence
        """
        start_token = [self.tokenizer_pt.vocab_size]
        end_token = [self.tokenizer_pt.vocab_size + 1]
        pt_tokens = np.array(start_token
                             + self.tokenizer_pt.encode(pt.numpy())
                             + end_token)
        start_token = [self.tokenizer_en.vocab_size]
        end_token = [self.tokenizer_en.vocab_size + 1]
        en_tokens = np.array(start_token
                             + self.tokenizer_en.encode(en.numpy())
                             + end_token)
        return pt_tokens, en_tokens

    def tf_encode(self, pt, en):
        """
        TensorFlow wrapper for the encode method.
        essentially turns encode method into a tensor
        """
        # seems to be a way to use the encode method
        pt_tokens, en_tokens = tf.py_function(self.encode, [pt, en], [tf.int64, tf.int64])
        # pt_tensor = tf.convert_to_tensor(pt_tokens, dtype=tf.int64)
        # en_tensor = tf.convert_to_tensor(en_tokens, dtype=tf.int64)
        # Set the shape of the tensors
        pt_tokens.set_shape([None])
        en_tokens.set_shape([None])
        # return pt_tensor, en_tensor
        return pt_tokens, en_tokens
