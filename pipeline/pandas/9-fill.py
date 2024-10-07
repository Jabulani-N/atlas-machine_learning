#!/usr/bin/env python3
"""
pandas dataframe manipulation

removes a designated col
inferrs designated row,col value by previous row
inferrs designated row,col vlaue by designated col
inferrs designated row,col value by defaul value
"""

import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df_backup = df.copy()

# remove col
col_in_question = "Weighted_Price"
df = df.drop(columns=col_in_question)

# missing Close vales are filled with previous row's version
col_in_question = "Close"
df[col_in_question] = df[col_in_question].ffill()

# missing High, Low, Open set to same row's Close
source_col = "Close"
recip_cols = ["High", "Low", "Open"]
for recip_col in recip_cols:
    df[recip_col] = df[recip_col].fillna(df[source_col].ffill())

# fill missing Volume_(BTC), Volume_(Currency)
default = 0
recip_cols = ["Volume_(BTC)", "Volume_(Currency)"]
df[recip_cols] = df[recip_cols].fillna(default)

print(df.head())
print(df.tail())
