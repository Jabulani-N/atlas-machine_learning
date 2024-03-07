#!/usr/bin/env python3
"""placeholder documentation"""


import numpy as np


def pool_backward(dA, A_prev, kernel_shape, stride=(1, 1), mode='max'):
    """
    performs back propagation
        over a pooling layer of a neural network
    """
    m, h_new, w_new, c = dA.shape
    m_prev, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw = kernel_shape
    sh, sw = stride

    dA_prev = np.zeros(A_prev.shape)

    for i in range(m):
        for h in range(h_new):
            for w in range(w_new):
                for c_i in range(c):
                    vert_start = h * sh
                    vert_end = vert_start + kh
                    horiz_start = w * sw
                    horiz_end = horiz_start + kw

                    if mode == 'max':
                        a_prev_slice = A_prev[i, vert_start:vert_end,
                                              horiz_start:horiz_end,
                                              c_i]
                        mask = (a_prev_slice == np.max(a_prev_slice))
                    elif mode == 'avg':
                        mask = np.ones((kh, kw)) / (kh * kw)

                    da = dA[i, h, w, c_i]
                    dA_prev[i,
                            vert_start:vert_end,
                            horiz_start:horiz_end,
                            c_i]\
                        += mask * da

    return dA_prev
