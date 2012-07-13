#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division

__version__ = "0.0.1"

import sim
import chart_generator


class SimSuiteBase(object):

    def __init__(self, client_range, sub_class):
        self.client_range = client_range
        self.sub_class = sub_class
        self.values = []

    def simulation(self):
        for clients in self.client_range:
            simulation = self.sub_class(n_clients=clients)
            value = simulation.sim()
            self.values.append(value)
#            print("Finalitzada simulació per %d clients" % (clients, ))

    def chart(self):
        c = chart_generator.Chart()
        c.values = self.values
        c.scale = self.client_range
        c.scatter_rt("sim.png")
        c.scatter_rt_log("sim_log.png")
        c.scatter_rt_y_log("sim_y_log.png")


    def __str__(self):
        s = ""
        for client, value in zip(self.client_range, self.values):
            s += "%d\t%.2f\n" % (client, value, )
        return s


class SimSuite(SimSuiteBase):

    def __init__(self, client_range=[1, 5, 10]):
        super(SimSuite, self).__init__(client_range, sim.SimulationWithReplica)


class SimSuiteWithoutReplica(SimSuiteBase):

    def __init__(self, client_range=[1, 5, 10]):
        super(SimSuiteWithoutReplica, self).__init__(client_range, sim.Simulation)
