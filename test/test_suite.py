#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division

__version__ = "0.0.1"

import unittest

import suite

@unittest.skip("Massa temps")
class TestSimSuite(unittest.TestCase):

    def test_one(self):
        s = suite.SimSuite([1])
        s.simulation()
        cadena = str(s)
        self.assertEqual(cadena, '1\t44.95\n')

    def test_two(self):
        s = suite.SimSuite([1, 3])
        s.simulation()
        cadena = str(s)
        self.assertEqual(cadena, '1\t44.95\n3\t45.73\n')

class TestSimSuiteWithoutReplica(unittest.TestCase):

    def test_one(self):
        s = suite.SimSuiteWithoutReplica([1])
        s.simulation()
        cadena = str(s)
        self.assertEqual(cadena, '1\t34.38\n')

    def test_two(self):
        s = suite.SimSuiteWithoutReplica([1, 3])
        s.simulation()
        cadena = str(s)
        self.assertEqual(cadena, '1\t34.38\n3\t42.25\n')



if __name__ == '__main__':
    unittest.main()
