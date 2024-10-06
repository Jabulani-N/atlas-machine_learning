#!/usr/bin/env python3
"""
pandas dataframe manipulation

sorts dataframe
transposes dataframe
    rotates so columns become rows & vice-versa
"""

import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

df = df.sort_values(by="Timestamp", ascending=False).transpose()

print(df.tail(8))
