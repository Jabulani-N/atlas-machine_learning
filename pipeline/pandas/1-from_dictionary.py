#!/usr/bin/env python3
"""converts example dictionary to a pandas dataframe"""

import pandas as pd


# spread out this way as a refresher dict operations
fulldict = {'First': [0.0, 0.5, 1.0, 1.5]}
fulldict['Second'] = ['one', 'two', 'three', 'four']

rowLabels = ['A', 'B', 'C', 'D']

# each dictionary entry is a column
# columns are named after the key; definition is data
df = pd.DataFrame(fulldict, index=rowLabels)
