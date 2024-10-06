#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# my own code begins here

# rneame colum
df.rename(columns={'Timestamp': 'Datetime'}, inplace=True)

# convert contents of said column from timestamp to datetime
df['Datetime'] = pd.to_datetime(df['Datetime'], utc=False)
# format datetime col to not be hte nanoseconds specific defualt
df['Datetime'] = df['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
# put datetime and close at tail
cols_to_move = ['Datetime', 'Close']
current_cols = df.columns.tolist()

new_order = [
    col for col in current_cols if col not in cols_to_move] + cols_to_move
df = df[new_order]
# turns out we only want to keep those two cols at all
df = df[['Datetime', 'Close']]

# mandatory provided code below
print(df.tail())
