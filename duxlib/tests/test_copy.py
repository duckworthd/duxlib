from __future__ import absolute_import

import unittest

from duxlib.copy import *


class Point(CaseClass):
  __slots__ = ['x', 'y']


class Point3D(CaseClass):
  __slots__ = ['x', 'y', 'z']


class TestCaseClass(unittest.TestCase):

  def test_init(self):
    point = Point(1, y=2)
    self.assertEqual(1, point.x)
    self.assertEqual(2, point.y)
    self.assertRaises(KeyError, Point, 1, 2, 3)
    self.assertRaises(KeyError, Point, 1, y=2, z=3)

  def test_unicode(self):
    point = Point(1, 2)
    self.assertEqual("Point(1, 2)", unicode(point))

  def test_eq(self):
    point1 = Point(1,2)
    point2 = Point(1,2)
    point3 = Point(1,3)
    point4 = Point3D(1,2,0)

    # same class
    self.assertEqual(point1, point2)
    self.assertNotEqual(point1, point3)

    # different class
    self.assertNotEqual(point1, point4)
    self.assertNotEqual(point4, point1)

  def def_iter(self):
    point = Point(1,2)
    self.assertEqual([1,2], list(point))

  def test_copy(self):
    point1 = Point(1,2)
    point2 = Point(1,4)
    self.assertEqual(point2, point1.copy(y=4))
    self.assertNotEqual(point1, point1.copy(y=4))

  def test_build(self):
    self.assertEqual(Point(1,2), Point.build({"x": 1, "y": 2, "ignored": 3}))
