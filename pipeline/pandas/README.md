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
