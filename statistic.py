#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from __future__ import print_function, division

__version__ = "0.0.1"

import scipy.stats as stat

import chart_generator

class Statistic(object):

    def __init__(self, n_clients=10):
        self.in_tasks = {}
        self.out_tasks = {}
        self.n_clients = n_clients
        self.events = 10
        self.threshold = 0.5

    def add_in(self, task, time):
        self.in_tasks[task] = time

    def add_out(self, task, time):
        self.out_tasks[task] = time

    def calc_rt_filtered(self):
        sub_list_keys = self.out_tasks.keys()
        sub_list_keys.sort()
        sub = int(len(sub_list_keys)*self.threshold)
        sub_keys = sub_list_keys[sub:]
        return self._calc_rt_base(sub_keys)

    def calc_rt(self):
        return self.calc_rt_nonfiltered()

    def calc_rt_nonfiltered(self):
        return self._calc_rt_base(self.out_tasks.keys())

    def _calc_rt_base(self, keys):
        values = []
        for key in keys:
            in_time = self.in_tasks[key]
            out_time = self.out_tasks[key]
            values.append(out_time - in_time)
        return stat.tmean(values)

    def calc_rt_evolution(self):
        values = []
        for key in self.out_tasks.iterkeys():
            in_time = self.in_tasks[key]
            out_time = self.out_tasks[key]
            values.append(out_time - in_time)
        return values
    
    def plot_rt_evolution(self, filename):
        chart = chart_generator.Chart()
        chart.values = self.calc_rt_evolution()
        chart.scatter_rt_evolution(filename)

    @property
    def is_safe_to_stop(self):
        return len(self) > (self.n_clients * self.events)

    def __len__(self):
        return len(self.out_tasks)
