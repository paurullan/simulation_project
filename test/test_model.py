#!/usr/bin/env python 
#-*- coding: utf-8 -*-

from __future__ import print_function, division

__version__ = "0.0.1"

import unittest

import model


class TestServer(unittest.TestCase):

    def setUp(self):
        self.server = model.Server()

    def test_add_queue(self):
        self.server.add(1)
        self.assertFalse(self.server.empty)
        self.assertTrue(self.server.empty_queue)
        self.server.process()
        self.assertTrue(self.server.empty)
        self.assertTrue(self.server.empty_queue)

    def test_empty_queue(self):
        self.server.add(1)
        self.assertTrue(self.server.empty_queue)
        self.server.add(2)
        self.assertFalse(self.server.empty_queue)
        self.server.process()
        self.assertTrue(self.server.empty_queue)
        self.server.process()
        self.assertTrue(self.server.empty_queue)

    def test_process(self):
        self.server.add(1)
        self.server.add(2)
        self.server.add(3)
        task, time = self.server.process()
        self.assertEqual(task, 1)
        task, time = self.server.process()
        self.assertEqual(task, 2)
        task, time = self.server.process()
        self.assertEqual(task, 3)

    def test_process_time(self):
        self.server.add(1)
        self.server.add(2)
        self.server.add(3)
        task, time = self.server.process()
        self.assertEqual(time, self.server.service())
        task, time = self.server.process()
        self.assertEqual(time, self.server.service())
        task, time = self.server.process()
        self.assertEqual(time, None)

    def test_service_example(self):
        first = 1
        self.server.add(first)
        item, service = self.server.process()
        self.assertEqual(first, item)
        self.assertEqual(service, None)


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = model.User()

    def test_service(self):
        time = self.user.service()
        result = 5117.05858038
        self.assertAlmostEqual(time, result)

    def test_service_2(self):
        num_list = [self.user.service() for i in range(5)]
        results = [
            5117.05858038,
            9508.44572792,
            5684.49491893,
            4829.02431238,
            7054.95497321,
            ]
        for num, result in zip(num_list, results):
            self.assertAlmostEqual(num, result)

class TestCPU(unittest.TestCase):

    def setUp(self):
        self.cpu = model.CPU()

    def test_service(self):
        """El temps de la CPU és constant a 0.4"""
        const = 0.4
        time = self.cpu.service()
        self.assertAlmostEqual(time, const)

    def test_choose(self):
        """Escollim un 0.833 de vegades el disk"""
        steps = 10*1000
        choices = [self.cpu.choose() for i in range(steps)]
        n_disk = filter(lambda x: x == 'disk', choices)
        appereances = len(n_disk)/steps
        self.assertLess(appereances, 0.85)
        self.assertGreater(appereances, 0.8)
        self.assertAlmostEqual(appereances, 0.8318)


class TestDisk(unittest.TestCase):

    def setUp(self):
        self.disk = model.Disk()

    def test_service(self):
        time = self.disk.service()
        self.assertAlmostEqual(time, 7.694141795723532)

    def test_service_seed_one(self):
        self.disk = model.Disk(seed=1)
        time = self.disk.service()
        self.assertAlmostEqual(time, 5.248957469228879)

    def test_four_services(self):
        time = sum([self.disk.service() for i in range(4)])
        self.assertAlmostEqual(time, 30.92443576341943)

    def test_five_services(self):
        time = sum([self.disk.service() for i in range(5)])
        self.assertAlmostEqual(time, 39.459474646190515)

if __name__ == '__main__':
    unittest.main()

