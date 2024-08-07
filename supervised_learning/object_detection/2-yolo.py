#!/usr/bin/env python3
"""
This module adds method filter_boxes
Duplicated from Task 1,
    but in a state NOT all checks pass
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
                    shape = (grid_height, grid_width,
                             anchor_boxes, 4 + 1 + classes)
                        grid_height & grid_width => height&width of output grid

        image_size = numpy.ndarray
            contains image’s original size [image_height, image_width]
        """
        boxes = []
        box_confidences = []
        box_class_probs = []
        image_height, image_width = image_size
        input_height, input_width = self.model.input.shape[1:3]

        for out_idx, output in enumerate(outputs):
            grid_height, grid_width, anchor_boxes = output.shape[:3]
            # store boundary box coords
            raw_bb_c = output[..., :4]

            box_confidence = output[..., 4:5]
            current_box_class_probs = output[..., 5:]
            # confidences and probabilities are straightforward
            # calcs b-box coords relative to original image (like a ratio)
            box_confidences.append(self.sigmoid(box_confidence))
            box_class_probs.append(self.sigmoid(current_box_class_probs))

            # Calculating bounding box coordinates
            for cell_y in range(grid_height):
                for cell_x in range(grid_width):
                    for anc_idx in range(anchor_boxes):
                        anchor_width, anchor_height =\
                            self.anchors[out_idx][anc_idx]
                        tx, ty, tw, th = raw_bb_c[cell_y, cell_x, anc_idx]
                        # sigmoid to get boundry box center (bbc) x,y coords
                        bbc_x = (self.sigmoid(tx) + cell_x)
                        bbc_y = (self.sigmoid(ty) + cell_y)
                        # boundry box width and height
                        bb_w = anchor_width * np.exp(tw)
                        bb_h = anchor_height * np.exp(th)
                        # normalize both pairs
                        bbc_x /= grid_width
                        bbc_y /= grid_height
                        bb_w /= int(self.model.input.shape[1])
                        bb_h /= int(self.model.input.shape[2])
                        # convert to original image scale
                        top_left_x = (bbc_x - (bb_w / 2) * image_width)
                        top_left_y = (bbc_y - (bb_h / 2) * image_height)
                        low_right_x = (bbc_x + (bb_w / 2) * image_width)
                        low_right_y = (bbc_y + (bb_h / 2) * image_height)
                        raw_bb_c[cell_y, cell_x, anc_idx] =\
                            [top_left_x, top_left_y, low_right_x, low_right_y]

            # Appending the calculated values to the respective lists
            boxes.append(raw_bb_c)

        return boxes, box_confidences, box_class_probs

    def filter_boxes(self, boxes, box_confidences, box_class_probs):
        """
        Returns a tuple of (filtered_boxes, box_classes, box_scores)
        boxes: = list of numpy.ndarrays
            shape (grid_height, grid_width, anchor_boxes, 4)
            containing processed boundary boxes for each output
        box_confidences: list of numpy.ndarrays
            shape (grid_height, grid_width, anchor_boxes, 1)
            containing processed box confidences for each output
        box_class_probs: list of numpy.ndarrays
            shape (grid_height, grid_width, anchor_boxes, classes)
            containing processed box class probabilities for each output
        """
        pass
