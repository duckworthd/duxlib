from __future__ import absolute_import

from duxlib.pandas import *


def test_to_csv():
  df = pd.DataFrame(
      [
        ["a", 1, 2],
        ["b", 1, 3],
        ["b", 2, 5],
      ],
      columns=["one", "two", "three"]
  )
  csv = to_csv(df, index=False)
  assert csv == 'one,two,three\na,1,2\nb,1,3\nb,2,5\n'
