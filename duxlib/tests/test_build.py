from __future__ import absolute_import

import unittest

from numpy.testing import assert_allclose
from duxlib.build import *


class Parent(Buildable):
  pass


class ChildA(Parent):

  def __init__(self, arg):
    self.arg = arg

  @classmethod
  def build(cls, config):
    return cls(arg=config['arg'])

class ChildB(Parent):
  pass


class TestBuildable(unittest.TestCase):

  def test_build_ok(self):
    self.assertEqual(
      Parent.build({"type": "ChildA", "arg": "val"}).arg,
      "val",
    )

  def test_build_fail_no_type(self):
    self.assertRaises(
      BuildException,
      Parent.build,
      {"arg": "val"},
    )

  def test_build_fail_no_children(self):
    self.assertRaises(
      BuildException,
      ChildB.build,
      {"type": "ChildC"},
    )
