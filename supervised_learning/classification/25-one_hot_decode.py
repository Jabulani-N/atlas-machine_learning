#!/usr/bin/env python3
"""this module contains a function
one hot decode that converts from an aray of categories to
an array of 'is it category 1? is it category 2?...'
"""

import numpy as np


def one_hot_decode(one_hot):
    """recieves an encoded array; turns it into a vector of labels
    answer: the vector of labels"""
    answer = np.zeros(len(one_hot))
    myVal = 0
    for dim1 in one_hot:
        print(str(dim1))
        # for dim2 in dim1:
        #     if dim2 == 0:
        #         myVal += 1
        #     else:
        #         break
        #     answer[dim1] = myVal
        #     myVal = 0
    return answer
