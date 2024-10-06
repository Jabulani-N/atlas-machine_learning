#!/usr/bin/env python3
"""
pandas dataframe manipulation

extracts 10 rows from specified columns
convrets dataframe rows into numpy.ndarray
"""

import pandas as pd
from_file = __import__('2-from_file').from_file


df = from_file(
    'coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv',
    ',')

# my code begins here
relevant_df = df[["High", "Close"]].tail(10)
A = relevant_df.to_numpy()

# provided required code
print(A)
