# convolutional Neural Networks

[A Comprehensive Guide to Convolutional Neural Networks — the ELI5 way](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53)

[Understanding Convolutional Layers in Convolutional Neural Networks](https://github.com/Machinelearninguru/Image-Processing-Computer-Vision/blob/master/Convolutional%20Neural%20Network/Convolutional%20Layers/README.md)

[Self-proclaimed best explanation of what a CNN is](https://medium.com/technologymadeeasy/the-best-explanation-of-convolutional-neural-networks-on-the-internet-fbb8b1ad5df8)

When testing code, you may need to use a particular lib file of data. If it is downloaded from online, [this is how you'll get it into a form numpy can use without downloading locally](https://stackoverflow.com/questions/52884563/loading-numpy-array-from-http-response-without-saving-a-file), for use in services such as Google Colab
* for me, this means inserting
  * `response = requests.get('https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-ml/MNIST.npz')`
  * `response.raise_for_status()`
* and altering the `lib` import line to be
  * `lib = np.load(io.BytesIO(response.content))`

A [Convolutional Neural Network](https://www.youtube.com/watch?v=YRhxdVk_sIs) (cnn) is an artificial neural network that has "convolotional layers" as hidden layers. These are specialized in pattern recognition. This happens via "filters" that look for particular traits based on the filter's type. filters may look for things like edges, vertical lines, circles, etc. these filters go from as basic as that, to recognizing patterns created by certain patterns of filter triggers. Not all cnn layers will be convolutional layers.

Convolutional Neural Networks [use the same structure](https://medium.com/technologymadeeasy/the-best-explanation-of-convolutional-neural-networks-on-the-internet-fbb8b1ad5df8) as the neural netweorks we're already familiar with. They have nodes (neurons) with "learnable weights and biases." They recieve an input, run it through the activation function, and generate an output. The cnn claim to fame is they recieve a vector as an input, and generate a vector output.

**Parameter Sharing** "[is sharing of weights by all neurons in a particular feature map](https://medium.com/technologymadeeasy/the-best-explanation-of-convolutional-neural-networks-on-the-internet-fbb8b1ad5df8)."

**Local connectivity** refers to having a given neuronh only look at relevant porition of input data, rather than the entire input, image in the case. This increases efficiency.

## Task 0 Convolutional Forward Prop

![Convolutoinal Forward Propagation](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*wqZ0Q4mBaHKjqWx45GPIow.gif)
* [source](https://becominghuman.ai/back-propagation-in-convolutional-neural-networks-intuition-and-code-714ef1c38199)

<details>
<summary>Task</summary>
Function <code>def conv_forward(A_prev, W, b, activation, padding="same", stride=(1, 1)):</code> performs forward propagation over a convolutional layer of a neural network
    - A_prev is a numpy.ndarray of shape (m, h_prev, w_prev, c_prev) containing the output of the previous layer
        - m is the number of examples
        - h_prev is the height of the previous layer
        - w_prev is the width of the previous layer
        - c_prev is the number of channels in the previous layer
    - W is a numpy.ndarray of shape (kh, kw, c_prev, c_new) containing the kernels for the convolution
        - kh is the filter height
        - kw is the filter width
        - c_prev is the number of channels in the previous layer
        - c_new is the number of channels in the output
    - b is a numpy.ndarray of shape (1, 1, 1, c_new) containing the biases applied to the convolution
    - activation is an activation function applied to the convolution
    - padding is a string that is either same or valid, indicating the type of padding used
    - stride is a tuple of (sh, sw) containing the strides for the convolution
        - sh is the stride for the height
        - sw is the stride for the width
**you may import numpy as np**
Returns: the output of the convolutional layer

</details>


**Convolution** is a type of filtering that takes the dot product of a chunk of an array. This is done over every "chunk," and the outputs create a new "dot product filtered" array. A "convolutional layer" is where these convolutions take place in a cnn. There can be multiple convolutionary filters in a single layer.


## Task 1 Pooling Forward Prop

![Pooling Layer illustration](https://miro.medium.com/v2/resize:fit:828/format:webp/1*gags_WLu961iw6I0ZX6iQA.png)

<details>
<summary>Task</summary>
Function <code>def pool_forward(A_prev, kernel_shape, stride=(1, 1), mode='max'):</code> performs forward propagation over a pooling layer of a neural network.

* A_prev is a numpy.ndarray of shape (m, h_prev, w_prev, c_prev) containing the output of the previous layer
*   m is the number of examples
*   h_prev is the height of the previous layer
*   w_prev is the width of the previous layer
*   c_prev is the number of channels in the previous layer
* kernel_shape is a tuple of (kh, kw) containing the size of the kernel for the pooling
*   kh is the kernel height
*   kw is the kernel width
* stride is a tuple of (sh, sw) containing the strides for the pooling
*   sh is the stride for the height
*   sw is the stride for the width
* mode is a string containing either max or avg, indicating whether to perform maximum or average pooling, respectively
*   you may import numpy as np
* Returns: the output of the pooling layer
</details>

The goal of a **Pooling Layer** is to reduce the size of the input, allowing faster, less burdened computations. A chunk is taken and a pooling operation is applied to it. The result takes the place of the pooled indices. The chunks taken when pooling do not overlap.

![Max Pooling](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jU_Mp73fXzh9_ffvtnbrDQ.png)
* [Max Pooling](https://medium.com/technologymadeeasy/the-best-explanation-of-convolutional-neural-networks-on-the-internet-fbb8b1ad5df8)

## Task 2 Convolutinoal Back Prop
