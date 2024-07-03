# Object Detection

Contents
- [Tasks](#tasks)
  - [Task 0](#task-0---initialize-yolo)
- [YOLO Explained](#you-only-look-once-yolo-explained)

## Tasks

### Task 0 - Initialize Yolo

Write a class Yolo that uses the Yolo v3 algorithm to perform object detection:

class constructor: `def __init__(self, model_path, classes_path, class_t, nms_t, anchors)`:

* `model_path` is the path to where a Darknet Keras model is stored
* `classes_path` is the path to where the list of class names used for the Darknet model, listed in order of index, can be found
* `class_t` is a float representing the box score threshold for the initial filtering step
* `nms_t` is a float representing the IOU threshold for non-max suppression
* `anchors` is a numpy.ndarray of shape (outputs, anchor_boxes, 2) containing all of the anchor boxes:
    * `outputs` is the number of outputs (predictions) made by the Darknet model
    * `anchor_boxes` is the number of anchor boxes used for each prediction
    * `2` => `[anchor_box_width, anchor_box_height]`

Public instance attributes:
 * `model`: the Darknet Keras model
 * `class_names`: a list of the class names for the model
 * `class_t`: the box score threshold for the initial filtering step
 * `nms_t`: the IOU threshold for non-max suppression
 * `anchors`: the anchor boxes

Firstly, `class_names`, `class_t`, and `anchors` are provided, so they can be directly assigned.

The `class_names` can be assigned by loading each line separately from `classes_path`.

The model can be loaded by `tesnsorflow.keras.models.load_model(model_path)`

### Task 1 - Process Outputs

Write a class `Yolo` (Based on `0-yolo.py`):

Add public method `def process_outputs(self, outputs, image_size):`
* `outputs` = list of `numpy.ndarray`s containing the predictions from the Darknet model for a single image:
* Each output will have the shape `(grid_height, grid_width, anchor_boxes, 4 + 1 + classes)`
    * `grid_height` & `grid_width` => the height and width of the grid used for the output
    * `anchor_boxes` => the number of anchor boxes used
    * `4` => `(t_x, t_y, t_w, t_h)`
    * `1` => `box_confidence`
    * `classes` => class probabilities for all classes
* `image_size` is a numpy.ndarray containing the image’s original size `[image_height, image_width]`
* Returns a tuple of `(boxes, box_confidences, box_class_probs)`:
  * `boxes`: a list of `numpy.ndarrays` of shape `(grid_height, grid_width, anchor_boxes, 4)` containing the processed boundary boxes for each output, respectively:
    * `4` => `(x1, y1, x2, y2)`
    * `(x1, y1, x2, y2)` should represent the boundary box relative to original image
  * `box_confidences`: a list of numpy.ndarrays of shape (grid_height, grid_width, anchor_boxes, 1) containing the box confidences for each output, respectively
  * `box_class_probs`: a list of numpy.ndarrays of shape (grid_height, grid_width, anchor_boxes, classes) containing the box’s class probabilities for each output, respectively

[This article](https://christianjmills.com/posts/pytorch-train-object-detector-yolox-tutorial/byte-track/) seems to have the struture we'll want to follow

## Task 5 - Preprocess Images

<details>
  <summary>Instructions</summary>
  
Add the public method `def preprocess_images(self, images):`
  * `images`: a `list` of images stored as `numpy.ndarrays`
    * Resize the images with inter-cubic interpolation
    * Rescale all images to have pixel values in the range [0, 1]
  * `Return`s a tuple of `(pimages, image_shapes)`:
    * `pimages`: a `numpy.ndarray` of shape `(ni, input_h, input_w, 3)` containing all preprocessed images
        * `ni`: the number of images that were preprocessed
        * `input_h`: the input height for the Darknet model Note: this can vary by model
        * `input_w`: the input width for the Darknet model Note: this can vary by model
        * `3`: number of color channels
  * `image_shapes`: a numpy.ndarray of shape (ni, 2) containing the original height and width of the images
    * `2` => `(image_height, image_width)`

</details>

[putting text in cv2 (this is cv documentation)](https://docs.opencv.org/4.x/d6/d6e/group__imgproc__draw.html#ga5126f47f883d730f633d74f07456c576)

## [You Only Look Once (YOLO) Explained](https://www.datacamp.com/blog/yolo-object-detection-explained)

YOLO is noteworthily fast, accurate, good at generalizing, and open source. These are some notes I'm making for my own reference, from the linked article. All images used in this segment are from the same linked article.

The algorithm works based on four approaches:
- [Object Detection](#object-detection)
  - [Tasks](#tasks)
    - [Task 0 - Initialize Yolo](#task-0---initialize-yolo)
    - [Task 1 - Process Outputs](#task-1---process-outputs)
  - [Task 5](#task-5)
  - [You Only Look Once (YOLO) Explained](#you-only-look-once-yolo-explained)
    - [Residual Blocks](#residual-blocks)
    - [Bounding-box Regression](#bounding-box-regression)
    - [Intersection over Unions (IUO)](#intersection-over-unions-iuo)
      - [non-max suppression (NMS)](#non-max-suppression-nms)
  - [Dive Really Deep into Yolo V3](#dive-really-deep-into-yolo-v3)
    - [Network Architecture](#network-architecture)
  - [Anchor Box](#anchor-box)

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

## [Dive Really Deep into Yolo V3](https://towardsdatascience.com/dive-really-deep-into-yolo-v3-a-beginners-guide-9e3d2666280e)

These are my notes on the article, made to help better my own understanding. All images used within are located within the linked article unless otherwise noted.

### Network Architecture

![Architecture image](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hULeMGlxnjjvuf7Fx7kuaA.jpeg)

The Feature Extractor used is Darknet. Yolo V3 uses Darknet-53, a 53 layer extractor.

As Darknet is being used for Object Detectoin instead of Classification, Pooling → Softmax "Classification Head" layers are not used. Instead, we have an "Detection Head" (needs to work for multiple scales because Yolo 3 is multi-scaled detector.)

![detection head is to the right in this image](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*SzyNALdsE9pDCpCvtqH7ZQ.jpeg)
* detection head is to the right in this image

The image above shows how we have 3 feature vectors. These are fed into the detector.

But what do the cells in this 52x52x3x(4+1+num_classes) matrix mean? This brings to Anchor Box.

## Anchor Box

"The goal of object detection is to get a bounding box and its class"

    This segment wil continue if relevant and useful to the creation of a project task.
