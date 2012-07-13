#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division

__version__ = "0.0.1"

import unittest

import sim


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.q = sim.Queue()

    def test_simple(self):
        self.q.add(1)
        item = self.q.first
        self.assertEqual(item, 1)

    
    def test_second(self):
        self.q.add(2)
        self.q.add(1)
        self.q.add(3)
        self.q.add(5)
        self.assertEqual(self.q.first, 1)
        self.assertEqual(self.q.first, 2)
        self.assertEqual(self.q.first, 3)
        self.assertEqual(self.q.first, 5)

    def test_third(self):
        self.q.add(2)
        self.q.add(1)
        self.assertEqual(self.q.first, 1)
        self.q.add(3)
        self.assertEqual(self.q.first, 2)
        self.q.add(5)
        self.assertEqual(self.q.first, 3)
        self.assertEqual(self.q.first, 5)

if __name__ == '__main__':
    unittest.main()
