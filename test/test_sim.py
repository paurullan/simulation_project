#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division

__version__ = "0.0.1"

import unittest
import filecmp

import sim

def make_filenames(name, filedir="test/test_img"):
    """Per facilitar la creació dels noms interns"""
    d = filedir + "/"
    ext = ".png"
    filename = d + name + ext
    master   = d +name + "_master" + ext
    return filename, master


class TestMakeFilenames(unittest.TestCase):

    def test_make_filenames(self):
        """Codi per provar el mètode make_filenames"""
        f, m = make_filenames("a")
        self.assertEqual(f, "test/test_img/a.png")
        self.assertEqual(m, "test/test_img/a_master.png")


class TestSimulation(unittest.TestCase):

    def setUp(self):
        self.sim = sim.Simulation()

    def test_cpu_one(self):
        """Confirma el comportament de la CPU"""
        self.sim.add_task(self.sim.cpu, 1)
        self.assertEqual(len(self.sim.cpu), 0)
        self.sim.add_task(self.sim.cpu, 2)
        self.sim.add_task(self.sim.cpu, 3)
        self.sim.add_task(self.sim.cpu, 4)
        self.assertEqual(len(self.sim.cpu), 3)
        task, time = self.sim.cpu.process()
        self.assertEqual(task, 1)
        task, time = self.sim.cpu.process()
        self.assertEqual(task, 2)
        task, time = self.sim.cpu.process()
        self.assertEqual(task, 3)
        task, time = self.sim.cpu.process()
        self.assertEqual(task, 4)
        self.assertEqual(time, None)
        self.assertEqual(len(self.sim.cpu), 0)

    def test_simple_init(self):
        self.sim.begin()
        queue_len = len(self.sim.queue.queue)
        self.assertEqual(self.sim.n_clients, queue_len)

    @unittest.skip("Massa temps")
    def test_multiple_init(self):
        initial_clients = 100
        self.sim = sim.Simulation(initial_clients)
        self.sim.begin()
        self.assertEqual(initial_clients, self.sim.n_clients)
        queue_len = len(self.sim.queue.queue)
        self.assertEqual(queue_len, self.sim.n_clients)

    def test_simple_simulation(self):
        self.sim.simulation()
        in_events = len(self.sim.statistic.in_tasks.keys())
        out_events = len(self.sim.statistic.out_tasks.keys())
        rt = self.sim.statistic.calc_rt()
        self.assertEqual(in_events, 115)
        self.assertEqual(out_events, 114)
        self.assertEqual(rt, 42.081392820958506)

    def test_simple_simulation_plot_rt_evolution(self):
        filename, master = make_filenames("test_simple_simulation_plot")
        self.sim.simulation()
        self.sim.statistic.plot_rt_evolution(filename)
        self.assertTrue(filecmp.cmp(filename, master))

    @unittest.skip("Massa temps")
    def test_big_simulation(self):
        """Simulació amb un nombre considerable de clients"""
        initial_clients = 100
        self.sim = sim.Simulation(initial_clients)
        self.sim.simulation()
        rt = self.sim.statistic.calc_rt()
        self.assertEqual(rt, 75.609456257117614)
        
    @unittest.skip("Massa temps")
    def test_big_sim_shortcut(self):
        """Simulació amb un nombre considerable de clients"""
        initial_clients = 100
        self.sim = sim.Simulation(initial_clients)
        self.sim.simulation()
        rt = self.sim.statistic.calc_rt()
        new_sim = sim.Simulation(initial_clients)
        new_rt = new_sim.sim()
        self.assertEqual(rt, new_rt)
        
    @unittest.skip("Massa temps")
    def test_very_big_sim_shortcut(self):
        """Simulació amb un nombre enooooorme de clients"""
        initial_clients = 1000
        self.sim = sim.Simulation(initial_clients)
        self.sim.simulation()
        rt = self.sim.statistic.calc_rt()
        new_sim = sim.Simulation(initial_clients)
        new_rt = new_sim.sim()
        self.assertEqual(rt, new_rt)
        
    def test_small_simulation(self):
        """Simulació amb un sol client"""
        initial_clients = 1
        self.sim = sim.Simulation(initial_clients)
        self.sim.simulation()
        rt = self.sim.statistic.calc_rt()
        self.assertEqual(len(self.sim.statistic), 12)
        self.assertEqual(rt, 34.375171385648777)

    def test_small_two(self):
        """Simulació amb dos clients"""
        initial_clients = 2
        self.sim = sim.Simulation(initial_clients)
        self.sim.simulation()
        rt = self.sim.statistic.calc_rt()
        self.assertEqual(len(self.sim.statistic), 23)
        self.assertEqual(rt, 37.480450372637989)

    def test_small_two_seed_two(self):
        """Simulació amb dos clients"""
        initial_clients = 2
        seed = 1
        self.sim = sim.Simulation(initial_clients, seed)
        self.sim.simulation()
        rt = self.sim.statistic.calc_rt()
        self.assertEqual(len(self.sim.statistic), 25)
        self.assertEqual(rt, 28.93994509522874)


class TestSimulationWithReplica(unittest.TestCase):

    def test_one(self):
        """Comparar que una sola rèplica és igual a una execució"""
        initial_clients = 1
        sim_repli = sim.SimulationWithReplica(n_replica=1, \
                                              n_clients=initial_clients)
        rt_repli = sim_repli.sim()
        # I la comparació
        self.sim = sim.Simulation(initial_clients)
        self.sim.simulation()
        rt = self.sim.statistic.calc_rt()
        self.assertEqual(rt_repli, rt)

    def test_two(self):
        repli = sim.SimulationWithReplica()
        rt = repli.sim()
        self.assertEqual(rt, 47.092064244653564)

if __name__ == '__main__':
    unittest.main()
