#!/usr/bin/env python3
"""
This module creates a class Yolo
There are no import restrictions
"""


import numpy as np
from tensorflow.keras.models import load_model

class Yolo:
    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        # Load the Darknet Keras model
        self.model = load_model(model_path)
        with open(classes_path, 'r') as file:
            # Read and store the list of class names
            self.class_names = [line.strip() for line in file.readlines()]
        # Assign the box score threshold for the initial filtering step
        self.class_t = class_t
        # Assign the IOU threshold for non-max suppression
        self.nms_t = nms_t
        # Assign the anchor boxes
        self.anchors = anchors
