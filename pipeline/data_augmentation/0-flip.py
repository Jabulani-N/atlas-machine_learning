#!/usr/bin/env python3
"""placeholder doc"""

import numpy as np
import tensorflow as tf


def flip_image(image):
    """
    flips an image horizontally
    image = image to flip
        tf.Tnesor object
    return
        flipped image
    """
    return tf.image.flip_left_right(image)
