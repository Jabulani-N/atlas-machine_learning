# Tensorflow

This directory demonstrates the utilization of [Tensorflow](https://www.tensorflow.org/install/pip).

when assigning attributes to the tensorflow `placeholder` (it's a clas)

* name: `name='myName'` will give a printed result of `myName:0`
* dtype: simply put the dtype. you don't say "data type" or anything.
* size: `size=[None, x]` [will make the first dimension undefined](https://stackoverflow.com/questions/42606722/shape-of-placeholder-in-tensorflow), and able to be changed, rather than set in stone.
  * the "size=" is optional
