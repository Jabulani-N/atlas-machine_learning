#!/usr/bin/env python3
"""placeholder doc"""


import tensorflow as tf


def crop_image(image, size):
    """
    randomly crops an image
    image = image to crop
        tf.Tnesor object
    size = size of crop
        tuple
            each index of the tuple dimension's size
    return
        cropped image
    """
    return tf.image.random_crop(image, size)
