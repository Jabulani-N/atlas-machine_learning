# Object Detection

## Tasks

### Task 0 - Initialize Yolo

Write a class Yolo that uses the Yolo v3 algorithm to perform object detection:

class constructor: def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
`model_path` is the path to where a Darknet Keras model is stored
`classes_path` is the path to where the list of class names used for the Darknet model, listed in order of index, can be found
`class_t` is a float representing the box score threshold for the initial filtering step
`nms_t` is a float representing the IOU threshold for non-max suppression
`anchors` is a numpy.ndarray of shape (outputs, anchor_boxes, 2) containing all of the anchor boxes:
    `outputs` is the number of outputs (predictions) made by the Darknet model
    `anchor_boxes` is the number of anchor boxes used for each prediction
    `2` => `[anchor_box_width, anchor_box_height]`

Public instance attributes:
    `model`: the Darknet Keras model
    `class_names`: a list of the class names for the model
    `class_t`: the box score threshold for the initial filtering step
    `nms_t`: the IOU threshold for non-max suppression
    `anchors`: the anchor boxes


## [You Only Look Once (YOLO) Explained](https://www.datacamp.com/blog/yolo-object-detection-explained)

YOLO is noteworthily fast, accurate, good at generalizing, and open source. These are some notes I'm making for my own reference, from the linked article. All images used in this segment are from the same linked article.

The algorithm works based on four approaches:
- [Object Detection](#object-detection)
  - [Tasks](#tasks)
    - [Task 0 - Initialize Yolo](#task-0---initialize-yolo)
  - [You Only Look Once (YOLO) Explained](#you-only-look-once-yolo-explained)
    - [Residual Blocks](#residual-blocks)
    - [Bounding-box Regression](#bounding-box-regression)
    - [Intersection over Unions (IUO)](#intersection-over-unions-iuo)
      - [non-max suppression (NMS)](#non-max-suppression-nms)

### Residual Blocks

![Residual blocks image](https://images.datacamp.com/image/upload/v1664382699/Application_of_grid_cells_to_the_original_image_7d3c056d06.png)
* example where `N=4`

The object is divided into an NxN grid of equal cells.

### Bounding-box Regression

![Bounding Box image](https://images.datacamp.com/image/upload/v1664382700/Identification_of_significant_and_insignificant_grids_d1e80c8bf4.png)

Bounding boxes are rectangles highlighting each image. These are found via scoring each cell with the chance it has of containing an object.

![bounding box image 2](https://images.datacamp.com/image/upload/v1664382698/Bounding_box_regression_identification_f530973d75.png)

### Intersection over Unions (IUO)

This handles the fact that a single object can exist in multiple cells. The IOU discards cells with low enough chances of containing an object. The chance threshold is set by the user.

#### non-max suppression (NMS)

Of cells that made it through IOU filtering, discards cells that have low comparative chances of contraining an object.
