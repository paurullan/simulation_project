#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from __future__ import print_function

__version__ = "0.0.1"

import unittest
import os
import filecmp

import chart_generator

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


class TestChart(unittest.TestCase):

    def setUp(self):
        self.chart = chart_generator.Chart()
        self.filedir = "test/test_img"
        if not os.access(self.filedir, os.W_OK):
            os.mkdir(self.filedir)


    def test_first(self):
        self.chart.values = [5]
        self.chart.names = ["Cuixot"]
        filename, master = make_filenames("test_first")
        self.chart.save_bar(filename)
        self.assertTrue(filecmp.cmp(filename, master))

    def test_second(self):
        self.chart.values = [5, 7]
        self.chart.names = ["Cuixot", "Indiot"]
        filename, master = make_filenames("test_second")
        self.chart.save_bar(filename)
        self.assertTrue(filecmp.cmp(filename, master))

    def test_third(self):
        self.chart.names = list("hola_nena")
        self.chart.values = range(1, len(self.chart.names)+1)
        filename, master = make_filenames("test_third")
        self.chart.save_bar(filename)
        self.assertTrue(filecmp.cmp(filename, master))

    def test_four_size(self):
        """En realitat la cota superior ve per si caben enters"""
        self.chart.values = [5, 7.1, 6.4]
        self.chart.names = ["Cuixot", "Indiot", "Pollastre"]
        filename, master = make_filenames("test_four")
        self.chart.save_bar(filename)
        self.assertTrue(filecmp.cmp(filename, master))

    def test_temps_resposta_u(self):
        """
        Exemple de com s'ha de cridar pels temps de resposta de la pràctica.
        """
        self.chart.values = [0.15, 0.004, 0.003, 0.04]
        self.chart.names = [
            "Profunditat",
            u"Veinat més proper",
            "A*",
            "A* relaxat",
            ]
        filename, master = make_filenames("test_temps_resposta_u")
        self.chart.save_response_time(filename)
        self.assertTrue(filecmp.cmp(filename, master))

    def test_nodes_visitats_u(self):
        """
        Exemple de com s'ha de cridar pels nodes visitats en la pràctica.
        """
        self.chart.values = [5, 6, 2, 3]
        self.chart.names = [
            "Profunditat",
            u"Veinat més proper",
            "A*",
            "A* relaxat",
            ]
        filename, master = make_filenames("test_nodes_visitats_u")
        self.chart.save_response_time(filename)
        self.assertTrue(filecmp.cmp(filename, master))

    def test_different_values_exception(self):
        """No podem tenir un gràfic amb manco categories que valors"""
        self.chart.values = [5]
        self.chart.names = ["Cuixot", "Indiot"]
        self.assertRaises(TypeError, self.chart.save_bar, "")


class TestEstatistic(unittest.TestCase):

    def setUp(self):
        filedir = "img"
        if not os.access(filedir, os.W_OK):
            os.mkdir(filedir)
        self.chart = chart_generator.Chart()

    def test_scatter_log(self):
        self.chart.values = [1, 1.5, 2, 3, 4]
        self.chart.scale = [1, 5, 10, 100, 150]
        filename, master = make_filenames("test_scatter_log")
        self.chart.scatter_rt_log(filename)
        self.assertTrue(filecmp.cmp(filename, master))

    def test_scatter_lin(self):
        self.chart. values = [1, 1.5, 2, 3, 4]
        self.chart.scale = [1, 5, 10, 100, 150]
        filename, master = make_filenames("test_scatter_lin")
        self.chart.scatter_rt(filename)
        self.assertTrue(filecmp.cmp(filename, master))


if __name__ == '__main__':
    unittest.main()
