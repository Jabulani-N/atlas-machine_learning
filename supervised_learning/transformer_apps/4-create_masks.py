#!/usr/bin/env python3
"""
placeholder doc
"""

import tensorflow_datasets as tfds
import tensorflow as tf
import numpy as np


def create_masks(inputs, target):
    """placeholder doc"""
    # Create the encoder mask
    encoder_mask = tf.cast(tf.equal(inputs, 0), tf.float32)  # Assuming 0 is the padding token
    encoder_mask = encoder_mask[:, tf.newaxis, tf.newaxis, :]  # Shape (batch_size, 1, 1, seq_len_in)

    # Create the lookahead mask for the decoder
    seq_len_out = tf.shape(target)[1]
    lookahead_mask = 1 - tf.linalg.band_part(tf.ones((seq_len_out, seq_len_out)), -1, 0)  # Shape (seq_len_out, seq_len_out)
    lookahead_mask = tf.cast(lookahead_mask, tf.float32)  # Convert to float for masking

    # Create the target padding mask
    target_mask = tf.cast(tf.equal(target, 0), tf.float32)  # Assuming 0 is the padding token
    target_mask = target_mask[:, tf.newaxis, tf.newaxis, :]  # Shape (batch_size, 1, 1, seq_len_out)

    # Combine the lookahead mask and target padding mask
    combined_mask = tf.maximum(lookahead_mask, target_mask)  # Shape (batch_size, 1, seq_len_out, seq_len_out)

    # Create the decoder mask (same as encoder mask but for target)
    decoder_mask = tf.cast(tf.equal(target, 0), tf.float32)  # Assuming 0 is the padding token
    decoder_mask = decoder_mask[:, tf.newaxis, tf.newaxis, :]  # Shape (batch_size, 1, 1, seq_len_out)

    return encoder_mask, combined_mask, decoder_mask
