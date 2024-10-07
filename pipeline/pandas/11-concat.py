#!/usr/bin/env python3
"""
pandas dataframe manipulation

index dataframes
    concatenate dataframes on index column
        only up to a given timestamp
add keys to data labeled bitstamp
add keys to data labeled coinbase
"""

import pandas as pd
from_file = __import__('2-from_file').from_file

df1 = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df2 = from_file('bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv', ',')
# index frames
df1.set_index("Timestamp", inplace=True)
df2.set_index("Timestamp", inplace=True)
# filter dataframes to relevant timestamps
timestamp_limit = 1417411920
df1 = df1[df1.index <= timestamp_limit]
df2 = df2[df2.index <= timestamp_limit]
# concatenate dataframes
df = pd.concat([df1, df2], axis=0)

print(df)
