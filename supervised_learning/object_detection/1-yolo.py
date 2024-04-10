#!/usr/bin/env python3
"""
This module contains the previous a class Yolo
creates the public method process_outputs
There are no import restrictions
"""


import numpy as np
import tensorflow.keras as K


class Yolo:
    """
    model_path = path to where a Darknet Keras model is stored
    classes_path = path to list of class names used for Darknet model
        listed in order of index
    class_t = float representing box score threshold for initial filtering
    nms_t = float representing the IOU threshold for non-max suppression
    anchors is a numpy.ndarray
        shape (outputs, anchor_boxes, 2)
            outputs = number of outputs (predictions) made by the Darknet model
        containins all  anchor boxes:
            anchor_boxes = number of anchor boxes used for each prediction
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
        # Assign the box score threshold for the initial filtering step
        self.class_t = class_t
        # Assign the IOU threshold for non-max suppression
        self.nms_t = nms_t
        # Assign the anchor boxes
        self.anchors = anchors

        # Load the Darknet Keras model
        self.model = K.models.load_model(model_path)
        with open(classes_path, 'r') as classes_file:
            # Read and store the list of class names
            self.class_names = [line.strip()
                                for line in classes_file.readlines()]

    def sigmoid(self, z):
        """returns sigmoid function of z"""
        return (1 / (1 + np.exp(-1 * z)))

    def process_outputs(self, outputs, image_size):
        """
        output shape may not match input shape
        uses sigmoid

        outputs = list of numpy.ndarrays
            containins predictions from Darknet model
                prediction (output) shape
                    shape = (grid_height, grid_width, anchor_boxes, 4 + 1 + classes)
                        grid_height & grid_width => height&width of output grid

        image_size = numpy.ndarray
            contains image’s original size [image_height, image_width]
        """
        boxes = []
        box_confidences = []
        box_class_probs = []
        image_height, image_width = image_size
        input_height, input_width = self.model.input.shape[1:3]


        for output in outputs:
            # Extracting bounding box coordinates
            box_xy = output[..., :2]
            box_wh = np.exp(output[..., 2:4] *
                            (self.anchors / self.model.input.shape[1:3]))
            box_confidence = output[..., 4:5]
            box_class_probs = output[..., 5:]

            # Implementing the logic to calculate bounding box coordinates relative to the original image
            box_xy = 1 / (1 + np.exp(-box_xy))
            # debug
            print("box_wh.shape:", box_wh.shape)
            print("self.anchors.shape: ", self.anchors.shape)
            print("self.model.input.shape", self.model.input.shape)
            # end debug
            # old line below
            # box_wh = np.exp(box_wh) * self.anchors / self.model.input.shape[1:3]

            # Calculating bounding box coordinates
            box_mins = box_xy - (box_wh / 2)
            box_maxes = box_xy + (box_wh / 2)
            box = np.concatenate([box_mins, box_maxes], axis=-1)

            # Appending the calculated values to the respective lists
            boxes.append(box)
            box_confidences.append(box_confidence)
            box_class_probs.append(box_class_probs)

        return boxes, box_confidences, box_class_probs