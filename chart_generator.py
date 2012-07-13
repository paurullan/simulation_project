#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import pylab

__version__ = "0.0.1"


class Chart(object):

    def __init__(self):
        self.values = []
        self.names = []
        self.scale = []

        self.ylabel = "Valors Y"
        self.title = u"Títol del gràfic"
        self.color = 'grey'

    def save_response_time(self, filename):
        self.title = u"Temps de resposta de les búsquedes"
        self.ylabel = "Temps (en segons)"
        self.save_bar(filename)

    def save_visited_nodes(self, filename):
        self.title = u"Nombre de nodes visitats en les búsquedes"
        self.ylabel = "Nodes"
        self.save_bar(filename)

    def save_bar(self, filename):
        if len(self.values) != len(self.names):
            raise TypeError
        fig = pylab.figure()
        ax = fig.add_subplot(1, 1, 1)
        ind = range(len(self.values))
        ax.bar(ind, self.values, facecolor=self.color, align='center')
        ax.set_ylabel(self.ylabel)
        ax.set_title(self.title, fontstyle='italic')
        ax.set_xticks(ind)
        ax.set_xticklabels(self.names)
        fig.autofmt_xdate()
        pylab.savefig(filename)
        pylab.close()

    def _scatter_rt_base(self):
        pylab.xlabel("Nombre d'usuaris al sistema (N)")
        pylab.ylabel("Temps de resposta (ms)")
        pylab.scatter(self.scale, self.values)
        pylab.xlim(0)
        pylab.ylim(0)

    def scatter_rt(self, filename):
        self._scatter_rt_base()
        pylab.savefig(filename)
        pylab.close()

    def scatter_rt_log(self, filename):
        self._scatter_rt_base()
        pylab.xlabel("Nombre d'usuaris al sistema (N) [escala log]")
        pylab.xscale("log")
        pylab.savefig(filename)
        pylab.close()

    def scatter_rt_y_log(self, filename):
        self._scatter_rt_base()
        pylab.ylabel("Temps de resposta (ms) [log]")
        pylab.yscale("log")
        pylab.savefig(filename)
        pylab.close()

    def scatter_rt_evolution(self, filename):
        pylab.xlabel("Esdeveniments del sistema (N)")
        pylab.ylabel("Temps de resposta (ms)")
        pylab.scatter(range(len(self.values)), self.values)
        pylab.xlim(0)
        pylab.ylim(0)
        pylab.savefig(filename)
        pylab.close()
