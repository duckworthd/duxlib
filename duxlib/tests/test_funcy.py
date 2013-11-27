from __future__ import absolute_import

import unittest

from numpy.testing import assert_allclose
from duxlib.funcy import *


def test_and_then():
  f1 = lambda x: 2 * x
  f2 = lambda x: x + 3
  f3 = lambda x: x / 4.0

  assert and_then([f1, f2, f3])(5) == (((2 * 5) + 3) / 4.0)


def test_combinations():
  arr = {
    "a": [1,2],
    "b": [2,3,4]
  }

  arr2 = [
    {"a": 1, "b": 2},
    {"a": 1, "b": 3},
    {"a": 1, "b": 4},
    {"a": 2, "b": 2},
    {"a": 2, "b": 3},
    {"a": 2, "b": 4},
  ]

  assert combinations(arr) == arr2
