#!/usr/bin/env python3
"""placeholder documentation"""


import numpy as np


def conv_backward(dZ, A_prev, W, b, padding="same", stride=(1, 1)):
    """
    performs back propagation
        over a convolutional layer of a neural network
    """
    m, h_new, w_new, c_new = dZ.shape
    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw, c_prev, c_new = W.shape
    sh, sw = stride

    dA_prev = np.zeros(A_prev.shape)
    dW = np.zeros(W.shape)
    db = np.zeros(b.shape)

    if padding == "same":
        pad_h = int(((h_prev - 1) * sh + kh - h_prev) / 2) + 1
        pad_w = int(((w_prev - 1) * sw + kw - w_prev) / 2) + 1
        A_prev_padded = np.pad(A_prev, ((0, 0),
                               (pad_h, pad_h),
                               (pad_w, pad_w), (0, 0)),
                               mode='constant', constant_values=(0, 0))
    else:
        A_prev_padded = A_prev
        dA_prev_padded = dA_prev
        pad_h = 0
        pad_w = 0

    dA_prev_padded = np.pad(dA_prev, ((0, 0),
                            (pad_h, pad_h),
                            (pad_w, pad_w), (0, 0)),
                            mode='constant', constant_values=(0, 0))
    for i in range(m):
        for h in range(h_new):
            for w in range(w_new):
                for c in range(c_new):
                    vert_start = h * sh
                    vert_end = vert_start + kh
                    horiz_start = w * sw
                    horiz_end = horiz_start + kw

                    a_slice = A_prev_padded[i, vert_start:vert_end,
                                            horiz_start:horiz_end, :]

                    dA_prev_padded[i, vert_start:vert_end,
                                   horiz_start:horiz_end, :] +=\
                        W[:, :, :, c] *\
                        dZ[i, h, w, c]
                    dW[:, :, :, c] += a_slice * dZ[i, h, w, c]
                    db[:, :, :, c] += dZ[i, h, w, c]

    if padding == "same":
        dA_prev = dA_prev_padded[:, pad_h:-pad_h, pad_w:-pad_w, :]
    else:
        dA_prev = dA_prev_padded

    return dA_prev, dW, db
