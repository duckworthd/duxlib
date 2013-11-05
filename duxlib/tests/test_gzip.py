from __future__ import absolute_import

import unittest

from duxlib.gzip import *


def test_roundtrip():
  s = "This is an example string to encode"
  assert decode(encode(s)) == s
