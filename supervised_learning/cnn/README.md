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

A [Convolutional Neural Network](https://www.youtube.com/watch?v=YRhxdVk_sIs) (cnn) is an artificial neural network that has "convolotional layers" as hidden layers. These are specialized in pattern recognition. This happens via "filters" that look for particular traits based on the filter's type. filters may look for things like edges, vertical lines, circles, etc. these filters go from as basic as that, to recognizing patterns created by certain patterns of filter triggers.

## Task 0 Convolutional Forward Prop

![Convolutoinal Forward Propagation](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*wqZ0Q4mBaHKjqWx45GPIow.gif)
* [source](https://becominghuman.ai/back-propagation-in-convolutional-neural-networks-intuition-and-code-714ef1c38199)
