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
df.set_index("Date", inplace=True)
# fill missing values
# missing values for Close
# missing Close vales are filled with previous row's version
col_in_question = "Close"
df[col_in_question] = df[col_in_question].ffill()
# missing vals for High, Low, Open
# missing High, Low, Open set to same row's Close
source_col = "Close"
recip_cols = ["High", "Low", "Open"]
for recip_col in recip_cols:
    df[recip_col] = df[recip_col].fillna(df[source_col].ffill())
# missing vals for Volume_(BTC), Volume_(Currency)
# fill missing Volume_(BTC), Volume_(Currency)
default = 0
recip_cols = ["Volume_(BTC)", "Volume_(Currency)"]
df[recip_cols] = df[recip_cols].fillna(default)
# plot the data from 2017 and beyond
# isolate 2017 and beyond
df_2017 = df[df.index >= '2017-01-01']
# group same days (D)
df_2017 = df_2017.resample('D').agg({
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum'
})
# plot aggregated data
plt.figure(figsize=(14, 7))
# Plot Close price
plt.subplot(2, 1, 1)
plt.plot(df_2017.index, df_2017['Close'], label='Close Price', color='blue')
plt.title('Daily Close Price from 2017 Onwards')
plt.xlabel('Date')
plt.ylabel('Close Price (USD)')
plt.legend()

# Plot Volume (BTC)
plt.subplot(2, 1, 2)
plt.plot(
    df_2017.index,
    df_2017['Volume_(BTC)'],
    label='Volume (BTC)',
    color='orange')
plt.title('Daily Volume (BTC) from 2017 Onwards')
plt.xlabel('Date')
plt.ylabel('Volume (BTC)')
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()
