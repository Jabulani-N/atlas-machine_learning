#!/usr/bin/env python3
"""
This module creates the class BidirectionalCell
this is an update to task 6
"""

import numpy as np


def bi_rnn(bi_cell, X, h_0, h_t):
    """
    recieves a cell and states
    bi_cell = instance of bi-cell class
    X = given data
        shape = (t,m,i)
            t = time steps
            m = batch size
            i = dimensionality of input data
    h_0 = initial forward hidden state
    h_t = initial backward hidden state
    """
    (time_steps, _, _) = np.shape(X)
    hid_forward = np.zeros((time_steps,
                            np.shape(h_0)[0],
                            np.shape(h_0)[1]))
    hid_backward = np.copy(hid_forward)
    h_prev = h_0
    h_next = h_t
    hid_forward[0] = h_0
    hid_backward[-1] = h_t
    for step_num in range(time_steps):
        # run the forward and backward and append hte hidden states
        # we'll also want the final value?
        # can get that by outputting after we've finished stackign states

        # terminology is weird, but I want it to prepare it's own next step
        h_prev = bi_cell.forward(h_prev, X[step_num])
        # hid_forward = np.append(hid_forward, h_next)
        hid_forward[step_num] = h_prev
        # minus makes it count form the end backwards
        h_next = bi_cell.backward(h_next, X[-step_num])
        # hid_backward = np.append(hid_backward, h_next)
        hid_backward[-(step_num + 1)] = h_next
    hid_backward = np.flip(hid_backward, axis=0)
    H = np.concatenate((hid_forward, hid_backward), axis=2)
    # print("backward =  ", hid_backward)
    # print("forward = ", hid_forward)
    # print("H = ", H)
    Y = bi_cell.output(H)
    # Y value is currently incorrect. shpae is correct
    return H, Y
