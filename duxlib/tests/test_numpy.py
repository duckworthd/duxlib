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
