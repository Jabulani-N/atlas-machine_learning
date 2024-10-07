#!/usr/bin/env python3
"""
pandas dataframe manipulation

indexes a dataframe on a given column
    given column = Timestamp
"""

import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
# print("before")
# print(df.tail())

df.set_index("Timestamp", inplace=True)

# print("after")
print(df.tail())
