#!/usr/bin/env python3
"""
uses a defined policy
    to play breakout
"""

import keras

# load the policy


def load_policy(poli_address='./policy.h5'):
    """
    returns the requested policy model
    this is set for this project
        written this way for poratability
    """
    return keras.models.load_model(poli_address)
