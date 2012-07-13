#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division

__version__ = "0.0.1"

import unittest

import statistic

class TestStatistic(unittest.TestCase):

    def setUp(self):
        self.s = statistic.Statistic()

    def test_calc_rt(self):
        """Calcula un temps de resposta senzill"""
        self.s.add_in(1, 2)
        self.s.add_out(1, 5)
        rt = self.s.calc_rt()
        self.assertEqual(rt, 3)

    def test_calc_rt_two_filtered(self):
        """Calcula un temps de resposta senzill.
        Malgrat és filtrat es comporta igual.
        """
        tasks = [(2, 3), (3, 4), (5, 6), (7, 8)]
        for num, task in enumerate(tasks):
            in_t, out_t = task
            self.s.add_in(num, in_t)
            self.s.add_out(num, out_t)
        rt = self.s.calc_rt()
        self.assertEqual(rt, 1)

    def test_calc_rt_two_nonfiltered(self):
        """Calcula un temps de resposta senzill"""
        tasks = [(2, 3), (3, 4), (5, 6), (7, 8)]
        for num, task in enumerate(tasks):
            in_t, out_t = task
            self.s.add_in(num, in_t)
            self.s.add_out(num, out_t)
        rt = self.s.calc_rt()
        self.assertEqual(rt, 1)


    def test_calc_rt_three_filtered(self):
        """Calcula un temps de resposta senzill.
        Malgrat és filtrat es comporta igual.
        """
        tasks = [(2, 2.5), (3, 4), (5, 5.5), (7, 7.5), (8, 8.5)]
        for num, task in enumerate(tasks):
            in_t, out_t = task
            self.s.add_in(num, in_t)
            self.s.add_out(num, out_t)
        rt = self.s.calc_rt_filtered()
        self.assertEqual(rt, 0.5)

    def test_calc_rt_three_nonfiltered(self):
        """Calcula un temps de resposta senzill"""
        tasks = [(2, 2.5), (3, 4), (5, 5.5), (7, 7.5), (8, 8.5)]
        for num, task in enumerate(tasks):
            in_t, out_t = task
            self.s.add_in(num, in_t)
            self.s.add_out(num, out_t)
        rt = self.s.calc_rt()
        self.assertEqual(rt, 3/5)


if __name__ == '__main__':
    unittest.main()
