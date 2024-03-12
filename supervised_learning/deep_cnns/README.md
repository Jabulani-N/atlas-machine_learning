# Deep Convolutional Neural Networks

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
