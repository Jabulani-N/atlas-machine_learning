#!/usr/bin/env python3
"""placeholder doc"""


import tensorflow as tf


def shear_image(image, intensity):
    """
    randomly shears image

    image = image to shear
        tf.Tensor
    intensity = shear intensity
    """
    return tf.keras.preprocessing.image.random_shear(image, intensity)
