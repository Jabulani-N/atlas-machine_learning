#!/usr/bin/env python3
"""module documentation
this module creates a function:
    train_mini_batch

"""


import numpy as np
import tensorflow as tf


def train_mini_batch(X_train, Y_train, X_valid, Y_valid, batch_size=32, epochs=5, load_path="/tmp/model.ckpt", save_path="/tmp/model.ckpt"):
    """loads a model,
    trains that model
    saves the trained model"""
    loaded_model = tf.keras.models.load_model(load_path)
    pass
