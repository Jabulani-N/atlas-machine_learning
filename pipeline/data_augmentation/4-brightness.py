#!/usr/bin/env python3
"""placeholder doc"""


import tensorflow as tf


def change_brightness(image, max_delta):
    """
    changes brightnes of image

    image = image to alter
        tf.Tensor
    max_delta = max birhtness/darkenss change
    """
    return tf.keras.preprocessing.image.random_brightness(
        image, (max_delta, 0))
