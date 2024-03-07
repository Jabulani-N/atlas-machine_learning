This document summarizes my understanding of [ImageNet Classification with Deep Convolutional
Neural Networks
](https://papers.nips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)

Said article describes the training of a deep convolutional neural network, utulizing dropout to prevent overfitting, which surpassed performance of the most advanced networks of the time. This network was effective on a significantly largr scale than most, classifying over one million images as opposed to the common tens of thousands.

Convolution made this possible. large-scale training would normally be prohibitively expensive, but 2D convolution reduces the load to practical levels.

The "tens of thousands" of training images were sufficient for "simple recognition tasks," but proved to be not quite ideal when applied to real-world scenarios, represented by large-scale training datasets. Furthermore, actually *getting* a large scale of labelled images was only recently possible, via tools such as LabelMe and ImageNet.

Despite having a worse "best-case" performance, convolutional neural networks (cnns) excel in categorizing trends such as those consistant in images of motion, static entities, and locality, indicating a fit for the task.

