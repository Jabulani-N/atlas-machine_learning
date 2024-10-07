# Pandas

Pandas is an open-source Python library that affords extraordinarly convenient data manipulation.


## Task 8 - Prune

You can perform general pruning following this example:

```

df = df[df[col_in_question] != prune_this]

```

* this changes `df` to equal the same as it was, but without any rows where items in `col_in_question` have value `prune_this`

but there is a [more efficient way](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.notnull.html) to trim the NaNs.

## Task 9 - Fill

[removing specified rows, cols, labels](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)

## Task 13 - Analyze

[`df.describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) usually wants a list-like of data types if providing an `exclude`, for example, `stats = df.describe(exclude=[pd.Timestamp])`.
* you can alternatively use a string to descibe dtypes
* "To exclude pandas categorical columns, use `category`"

Including only categorical columns from a DataFrame description.

```

df.describe(include=['category'])
       categorical
count            3
unique           3
top              d
freq             1

```