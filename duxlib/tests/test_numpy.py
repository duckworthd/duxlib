from __future__ import absolute_import

import unittest

from numpy.testing import assert_allclose
from duxlib.numpy import *


def test_inner():
  def _check_inner(arr, lower, upper):
    assert np.all((arr >= lower) & (arr <= upper))

  arr = np.asarray([5,4,3,2,1,0,6,7,8,9])
  examples = [
      (0.01, 4.9 , 5.1) ,
      (0.25, 3.75, 6.25),
      (0.50, 2.5 , 7.5) ,
      (1.00, 0   , 9)   ,
    ]
  for (p, lower, upper) in examples:
    yield (_check_inner, arr[inner(arr, p)], lower, upper)

  arr = [1,2,3,4,5]
  examples = [
      (1.0, 1, 5),
      (0.5, 2, 4),
      (0.25, 2.5, 3.5),
  ]
  for (p, lower, upper) in examples:
    yield (_check_inner, np.asarray(arr)[inner(arr, p)], lower, upper)
