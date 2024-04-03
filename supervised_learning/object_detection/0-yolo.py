#!/usr/bin/env python3
"""
This module creates a class Yolo
There are no import restrictions
"""


import numpy as np
from tensorflow.keras.models import load_model


class Yolo:
    """
    model_path is the path to where a Darknet Keras model is stored
    classes_path is the path to where the list of class names used for the Darknet model, listed in order of index, can be found
    class_t is a float representing the box score threshold for the initial filtering step
    nms_t is a float representing the IOU threshold for non-max suppression
    anchors is a numpy.ndarray
        shape (outputs, anchor_boxes, 2)
            outputs is the number of outputs (predictions) made by the Darknet model
        containins all  anchor boxes:
            anchor_boxes is the number of anchor boxes used for each prediction
        2 => [anchor_box_width, anchor_box_height]
    """
    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        """
        Public instance attributes:
        model: the Darknet Keras model
        class_names: a list of the class names for the model
        class_t: the box score threshold for the initial filtering step
        nms_t: the IOU threshold for non-max suppression
        anchors: the anchor boxes
        """
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
