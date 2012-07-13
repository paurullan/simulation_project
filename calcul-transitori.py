#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division

__version__ = "0.0.1"

import sim

if __name__ == '__main__':

    for number in [100, 150, 200, 250, 300]:
        s = sim.Simulation(number)
        s.simulation()
        name = "evo-%d.png" % number
        s.statistic.plot_rt_evolution(name)
