#!/usr/bin/env python3
"""creates pandas dataframe from a file"""

import pandas as pd


def from_file(filename, delimiter):
    """
    loads file filename a as pandas dataframe

    delimiter = column separater
    """
    return pd.read_csv(filename, delimiter=delimiter)
