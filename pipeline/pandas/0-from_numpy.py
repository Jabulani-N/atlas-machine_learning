#!/usr/bin/env python3

import numpy as np
import pandas as pd


def from_numpy(array):
    """
    creates a pandas dataframe from numpy array
        dataframe will be
            labelled in alphabetical order
            capitalized

    array = np.ndarray
    """
    # DataFrame directly from numpy array
    df = pd.DataFrame(array)

    num_columns = df.shape[1]
    # create labels
    # capital letters are ASCII values, starting at 65 = A
    column_labels = [chr(i) for i in range(65, 65 + num_columns)]

    # Assign labels
    df.columns = column_labels

    return df
