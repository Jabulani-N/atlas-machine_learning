#!/usr/bin/env python3
"""placeholder doc"""


import tensorflow as tf


def rotate_image(image):
    """
    rotates image 90° c.clockwise

    image = image to rotate
        tf.Tensor
    """
    return tf.image.rot90(image)
