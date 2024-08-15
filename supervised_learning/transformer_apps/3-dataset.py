#!/usr/bin/env python3
"""
machine translation module
expands upon task 2
    class
        Dataset
            edit method
                __init__
"""

import tensorflow_datasets as tfds
import tensorflow as tf
import numpy as np


class Dataset:
    def __init__(self, batch_size, max_len):
        """
        creates a datasest of what is to be used in mtl
        updated in a way incompatible with solving task 0
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

        # Filter the training data by length
        self.data_train = self.data_train.filter(
            lambda pt, en: tf.logical_and(
                tf.size(pt) <= max_len,
                tf.size(en) <= max_len))

        # cache dataset to increase performance
        self.data_train = self.data_train.cache()

        # Batch the training data
        self.data_train = self.data_train.padded_batch(
            batch_size)

        # Prefetch training data to increase performance
        self.data_train = self.data_train.prefetch(
            tf.data.experimental.AUTOTUNE)

        # Filter the validation data by length
        self.data_valid = self.data_valid.filter(
            lambda pt, en: tf.logical_and(
                tf.size(pt) <= max_len,
                tf.size(en) <= max_len))
        # Batch the validation data
        self.data_valid = self.data_valid.padded_batch(
            batch_size)

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
        pt_tokens, en_tokens = tf.py_function(self.encode,
                                              [pt, en],
                                              [tf.int64, tf.int64])
        # Set the shape of the tensors
        pt_tokens.set_shape([None])
        en_tokens.set_shape([None])
        return pt_tokens, en_tokens
