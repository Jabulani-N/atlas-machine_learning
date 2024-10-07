#!/usr/bin/env python3
"""
pandas dataframe manipulation

performs task 11
    slightly modified for task 12
rearranges MultiIndex levels
    timestamp is the first level
rearanges result into chronological order
    see task 7
"""

import pandas as pd
from_file = __import__('2-from_file').from_file

df1 = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df2 = from_file('bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv', ',')

# index frames
df1.set_index("Timestamp", inplace=True)
df2.set_index("Timestamp", inplace=True)
# filter dataframes to relevant timestamps
timestamp_lo_limit = 1417411980
timestamp_hi_limit = 1417417980
df1 = df1[(df1.index >= timestamp_lo_limit) &
          (df1.index <= timestamp_hi_limit)]

df2 = df2[(df2.index >= timestamp_lo_limit) &
          (df2.index <= timestamp_hi_limit)]

# concatenate dataframes, label keys
df = pd.concat([df2, df1], axis=0, keys=["bitstamp", "coinbase"])
# move timestamp to multiindex level 1
df.swaplevel(0, 1)
# rearrange into chronological order
df = df.sort_values(by="Timestamp", ascending=True)
print(df)
