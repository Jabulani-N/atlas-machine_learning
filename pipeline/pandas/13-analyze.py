#!/usr/bin/env python3
"""
pandas dataframe manipulation

calculates descriptive stats
    excludes designated column
"""

import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

stats = df.drop(columns="Timestamp").describe()

print(stats)
