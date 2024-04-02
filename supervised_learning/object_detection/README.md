# Object Detection

## [You Only Look Once (YOLO) Explained](https://www.datacamp.com/blog/yolo-object-detection-explained)

YOLO is noteworthily fast, accurate, good at generalizing, and open source. These are some notes I'm making for my own reference, from the linked article. All images used in this segment are from the same linked article.

The algorithm works based on four approaches:
- [Object Detection](#object-detection)
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

#### non-max suppression (NMS)