# convolutional Neural Networks

[A Comprehensive Guide to Convolutional Neural Networks — the ELI5 way](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53)

[Understanding Convolutional Layers in Convolutional Neural Networks](https://github.com/Machinelearninguru/Image-Processing-Computer-Vision/blob/master/Convolutional%20Neural%20Network/Convolutional%20Layers/README.md)

When testing code, you may need to use a particular lib file of data. If it is downloaded from online, [this is how you'll get it into a form numpy can use without downloading locally](https://stackoverflow.com/questions/52884563/loading-numpy-array-from-http-response-without-saving-a-file), for use in services such as Google Colab
* for me, this means inserting
  * `response = requests.get('https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-ml/MNIST.npz')`
  * `response.raise_for_status()`
* and altering the `lib` import line to be
  * `lib = np.load(io.BytesIO(response.content))`

## Task 0 Convolutional Forward Prop
