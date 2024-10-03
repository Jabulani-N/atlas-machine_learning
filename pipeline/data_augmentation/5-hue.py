#!/usr/bin/env python3
"""placeholder doc"""


import tensorflow as tf


def change_hue(image, delta):
    """
    changes hue of image

    image = image
        3D tf.Tensor
    delta = change amount
        float in rnage [-1, 1]
    """
    return tf.image.adjust_hue(image, delta)
