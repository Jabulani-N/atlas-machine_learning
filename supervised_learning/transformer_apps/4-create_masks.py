#!/usr/bin/env python3
"""
placeholder doc
"""

import tensorflow_datasets as tfds
import tensorflow as tf
import numpy as np


def pad_mask(inputs, equal_to_me):
    """
    makes a padding mask of inputs
    shows where inputs is equal to equal_to_me
    """
    return tf.cast(tf.equal(inputs, equal_to_me), tf.float32)



def look_mask(kagamine):
    """
    makes a lookahead mask based on len(gth) kagamine
    """
    shape = (kagamine, kagamine)
    mask = 1 - tf.linalg.band_part(tf.ones(shape), -1, 0)


def create_masks(inputs, target):
    """
    placeholder doc
    begin by inserting details of what inputs and target are
    """

    # Create encoder mask
    # uses 0 as padding token
    encoder_mask = pad_mask(inputs, 0)
    # reshape to (batch_size, 1, 1, seq_len_in) as requested
    # this line inserts the "1"s
    encoder_mask = encoder_mask[:, tf.newaxis, tf.newaxis, :]
    # do the same thing to create target mask
    target_mask = pad_mask(target, 0)[:, tf.newaxis, tf.newaxis, :]
    # do the same thing to create decoder mask
    decoder_mask = pad_mask(target, 0)[:, tf.newaxis, tf.newaxis, :]

    # Create the lookahead mask for the decoder
    seq_len_out = tf.shape(target)[1]
    lookahead_mask = 1 - tf.linalg.band_part(tf.ones((seq_len_out, seq_len_out)), -1, 0)
    # Convert to float for masking  # Shape (seq_len_out, seq_len_out)
    lookahead_mask = tf.cast(lookahead_mask, tf.float32)

    # Combine the lookahead mask and target padding mask
    # Shape (batch_size, 1, seq_len_out, seq_len_out)
    combined_mask = tf.maximum(lookahead_mask, target_mask)

    return encoder_mask, combined_mask, decoder_mask
