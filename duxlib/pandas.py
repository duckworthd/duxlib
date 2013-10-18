from __future__ import absolute_import

import pandas as pd

def to_records(df):
  """The inverse of `pandas.DataFrame.from_records`

  Parameters
  ----------
  df : DataFrame

  Returns
  -------
  rows : list
      list of dicts, one per row in `df`. Index dropped.
  """
  for _, row in df.iterrows():
    yield dict(row)


def count(key="count"):
  """Count the number of rows in a Dataframe

  >>> df.groupby("country").apply(count("population"))

  Parameters
  ----------
  key : str
      key to name new column
  """
  def count_(group):
    return pd.Series({key: len(group)})
  return count_
