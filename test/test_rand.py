#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from __future__ import print_function

__version__ = "0.0.1"

import unittest

import rand

class TestGenerator(unittest.TestCase):

    def setUp(self):
        self.gen = rand.Generator()

    def test_first(self):
        num = self.gen.num
        self.assertAlmostEqual(num, 0.4005279)

    def test_constant(self):
        constant = 5
        num = self.gen.constant(constant)
        self.assertEqual(num, constant)

    def test_exp(self):
        lambd = 10*1000
        num = self.gen.exp(lambd)
        self.assertAlmostEqual(num, 5117.058580378)
    
    def test_exp_2(self):
        num_list = [self.gen.exp(1) for i in range(4)]
        results = [0.51170585, 0.95084457, 0.56844949, 0.4829024]
        for num, result in zip(num_list, results):
            self.assertAlmostEqual(num, result)

    def test_uniform(self):
        inf, sup = 0, 10
        result = 4.00527908
        num = self.gen.uniform(inf, sup)
        self.assertAlmostEqual(result, num)

    def test_uniform_2(self):
        inf, sup = 0, 10
        num_list = [self.gen.uniform(inf, sup) for i in range(4)]
        results = [4.00527908, 6.135854695986889, 4.335970293886946, 3.8300998]
        for num, result in zip(num_list, results):
            self.assertAlmostEqual(num, result)


if __name__ == '__main__':
    unittest.main()

