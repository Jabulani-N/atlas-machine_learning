# Deep Convolutional Neural Networks

Learning Objectives
- What is a skip connection?
- What is a bottleneck layer?
- What is the Inception Network?
- What is ResNet? ResNeXt? DenseNet?
- How to replicate a network architecture by reading a journal article

Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8)
- Files will be executed with numpy (version 1.19.2) and tensorflow (version 2.6)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.6.0)
- All your modules should have documentation (python3 -c 'print(import("my_module").doc)')
- All your classes should have documentation (python3 -c 'print(import("my_module").MyClass.doc)')
- All your functions (inside and outside a class) should have documentation (python3 -c 'print(import("my_module").my_function.doc)' and python3 -c 'print(import("my_module").MyClass.my_function.doc)')
- Unless otherwise noted, you are not allowed to import any module except `import tensorflow.keras as K`
- All your files must be executable
- The length of your files will be tested using wc

Assorted Resources:

Identity Block
* https://machinelearningknowledge.ai/keras-implementation-of-resnet-50-architecture-from-scratch/#Implementation_of_Identity_Block

## Task 0 Inception Block

![Inception Block](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/12/4a550a5b5501521f794b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240312%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240312T000948Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1057b914f04521b444a82a5e509bc47a63c28e81a1052f4b8330525a438f9299)
<details>
  <summary>Task</summary>
Write a function def inception_block(A_prev, filters): that builds an inception block as described in Going Deeper with Convolutions (2014):


`A_prev` is the output from the previous layer

`filters` is a tuple or list containing `F1`, `F3R`, `F3`, `F5R`, `F5`, `FPP`, respectively:
* `F1` is the number of filters in the 1x1 convolution
* `F3R` is the number of filters in the 1x1 convolution before the 3x3 convolution
* `F3` is the number of filters in the 3x3 convolution
* `F5R` is the number of filters in the 1x1 convolution before the 5x5 convolution
* `F5` is the number of filters in the 5x5 convolution
* `FPP` is the number of filters in the 1x1 convolution after the max pooling
All convolutions inside the inception block should use a rectified linear activation (ReLU)
Returns: the concatenated output of the inception block

</details>

This task is a tutorial on using [`keras.layers.Conv2D`]([Conv2D](https://keras.io/api/layers/convolution_layers/convolution2d/)), [`keras.layers.MaxPooling2D`](https://keras.io/api/layers/pooling_layers/max_pooling2d/), and [`keras.layers.concatenate`](https://keras.io/api/layers/merging_layers/concatenate/).


### Potential Pitfalls

[`maxpooling2d` is not the same as `maxpool2d`]

## Task 1 Inception Network
<details>
<summary>Tasks</summary>

Write a function `def inception_network():` that builds the inception network as described in [Going Deeper with Convolutions](https://arxiv.org/pdf/1409.4842.pdf) (2014):

- You can assume the input data will have shape `(224, 224, 3)`
- All convolutions inside and outside the inception block should use a rectified linear activation (ReLU)
- You may use `inception_block = __import__('0-inception_block').inception_block`
- Returns: the keras model

</details>

![layerset](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/12/1165affa2943a7a330b1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240312%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240312T052929Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=47df55b957db52a573f98e2fe0a1a34c28a7d76dfae0cbeb11ead98e42649b28)
* layerset to be used


This task is mostly pasting the contents of the above layerset, but will also make use of [`keras.layers.AveragePooling2D](https://keras.io/api/layers/pooling_layers/average_pooling2d/).

### Potential pitfalls

When doing a layer with depth greater than one, such as the second convolutional layer, the filters before the final one are of shape `(1, 1)`.

## task 2 Identity Block

<details>
<summary>Task</summary>

Write a function `def identity_block(A_prev, filters):` that builds an identity block as described in [Deep Residual Learning for Image Recognition (2015)](https://arxiv.org/pdf/1512.03385.pdf):



* `A_prev` is the output from the previous layer
* `filters` is a tuple or list containing `F11`, `F3`, `F12`, respectively:
* `F11` is the number of filters in the first 1x1 convolution
* `F3` is the number of filters in the 3x3 convolution
* `F12` is the number of filters in the second 1x1 convolution
* All convolutions inside the block should be followed by batch normalization along the channels axis and a rectified linear activation (ReLU), respectively.
* All weights should use he normal initialization
* Returns: the activated output of the identity block

</details>

![Ideneity Block](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/12/a884dfda60c795f11df7.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240313%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240313T211912Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=80a36b7260ca2f662d0ea44a7cb0a4408855df6767d6e8213674f0180e6d622a)

## Task 3 Projection Block

The code document for this task is potentially incomplete.
 * though it tests sucessfully localy, results from the checker are imprerfect.

<details>
<summary>Task</summary>

Write a function `def projection_block(A_prev, filters, s=2):` that builds a projection block as described in [Deep Residual Learning for Image Recognition (2015)](https://arxiv.org/pdf/1512.03385.pdf):

- A_prev is the output from the previous layer
- filters is a tuple or list containing F11, F3, F12, respectively:
  - F11 is the number of filters in the first 1x1 convolution
  - F3 is the number of filters in the 3x3 convolution
  - F12 is the number of filters in the second 1x1 convolution as well as the 1x1 convolution in the shortcut connection
- s is the stride of the first convolution in both the main path and the shortcut connection
- All convolutions inside the block should be followed by batch normalization along the channels axis and a rectified linear activation (ReLU), respectively.
- All weights should use he normal initialization
- Returns: the activated output of the projection block

</details>

![Projection Block](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/12/058c583d20b067c344c9.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240313%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240313T211912Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a107e3f5c37033ca4391f1e9ad335d013d064758eede1e6fd6b837f59a94c0a7)

## Task 5 Dense Block

<details>
<summary>Task 5</summary>

Write a function `def dense_block(X, nb_filters, growth_rate, layers):` that builds a dense block as described in [Densely Connected Convolutional Networks](https://arxiv.org/pdf/1608.06993.pdf):

- `X` is the output from the previous layer
- `nb_filters` is an integer representing the number of filters in `X`
- `growth_rate` is the growth rate for the dense block
- `layers` is the number of layers in the dense block
- You should use the bottleneck layers used for DenseNet-B
- All weights should use he normal initialization
- All convolutions should be preceded by Batch Normalization and a rectified linear activation (ReLU), respectively
- Returns: The concatenated output of each layer within the Dense Block and the number of filters within the concatenated outputs, respectively

</details>

![Densely Connected Convolutional Networks](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/1/553bd4eebc1423fc0b72.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240314%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240314T021215Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bc12c59a52ab84cd502fedd815ecaf42df0d702ed9d8b033509e6ef91917e56b)
