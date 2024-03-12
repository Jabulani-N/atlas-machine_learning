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

## task 1 Inception Network

![layerset](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/12/1165affa2943a7a330b1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240312%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240312T052929Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=47df55b957db52a573f98e2fe0a1a34c28a7d76dfae0cbeb11ead98e42649b28)
* layerset to be used
