from __future__ import absolute_import

from StringIO import StringIO
import unittest

from duxlib.mirror import *


class SomeService(object):

  def __init__(self, name):
    self.name  = name
    self.count = 0

  def hello(self, other):
    self.count += 1
    return "Hello {}, my name is {}. ({})".format(other, self.name, self.count)


class MirrorTests(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_simple(self):
    sio  = StringIO()
    m    = Mirror(sio, mode='record')
    inst = m(SomeService("name1"), id="name1")

    r1 = inst.hello("other1")
    r2 = inst.hello("other2")

    m.save()
    sio.seek(0)

    m2   = Mirror(sio, mode='replay', strict=True)
    inst_= m2(SomeService("name1"), id="name1")

    r2_ = inst_.hello("other2")   # order doesn't matter when replaying
    r1_ = inst_.hello("other1")

    self.assertEqual(r1, r1_)
    self.assertEqual(r2, r2_)
    self.assertEqual(inst_.count, 0)  # SomeService.hello() wasn't actually called

  def test_multiple_objects(self):
    """Test saving multiple distinct, objects"""

    sio = StringIO()
    m   = Mirror(sio, mode='record')

    # constructor arguments should have no effect on SomeService.hello()
    i1  = m(SomeService(""), id="name1")
    i2  = m(SomeService(""), id="name2")

    r1 = i1.hello("other1")
    r2 = i2.hello("other2")

    m.save()
    sio.seek(0)

    m2  = Mirror(sio, mode='replay', strict=True)
    i1_ = m2(SomeService("name1"), id="name1")
    i2_ = m2(SomeService("name2"), id="name2")

    self.assertEqual(r1, i1_.hello("other1"))
    self.assertEqual(r2, i2_.hello("other2"))
    self.assertEqual(i1_.count, 0)
    self.assertEqual(i2_.count, 0)

    self.assertRaises(KeyError, i1_.hello, "other2")
    self.assertRaises(KeyError, i2_.hello, "other1")

  def test_mutable_collection_arguments(self):
    """Ensure mutable things are converted to their hashable equivalents"""
    sio  = StringIO()
    m    = Mirror(sio, mode='record')
    inst = m(SomeService("name1"), id="name1")

    r1 = inst.hello(["list", {"set"}, {"di": "ct"}, ("tu", "ple")])
    r2 = inst.hello("other2")

    m.save()
    sio.seek(0)

    m2   = Mirror(sio, mode='replay', strict=True)
    inst_= m2(SomeService("name1"), id="name1")

    r2_ = inst_.hello("other2")
    r1_ = inst_.hello(["list", {"set"}, {"di": "ct"}, ("tu", "ple")])

    self.assertEqual(r1, r1_)
    self.assertEqual(r2, r2_)
    self.assertEqual(inst_.count, 0)  # SomeService.hello() wasn't actually called
