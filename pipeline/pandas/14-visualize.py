#!/usr/bin/env python3
"""
pandas dataframe manipulation

removes designated column
renamtes designated column
converts timestamp vals to date vals

fills designated col values via previous row
fills designated row values via same col
fills deignated col values via default

plot data
    daily interval
    group values such that
        High: max
        Low: min
        Open: mean
        Close: mean
        Volume(BTC): sum
        Volume(Currency): sum
"""

from datetime import date
import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# remove col
df = df.drop(columns="Weighted_Price")
# rename col
df.rename(columns={'Timestamp': 'Date'}, inplace=True)
# convert timestamps in Date to date values
df['Date'] = pd.to_datetime(df['Date'], utc=False)
# index on Date
pass
