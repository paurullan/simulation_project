#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division

__version__ = "0.0.1"

import suite

if __name__ == '__main__':
    s = suite.SimSuite()
    # general una llista de clients de deu en deu fins a tres-cents
    clients = range(10, 310)[::10]
    clients = [10]
    s.client_range = clients
    s.simulation()
    s.chart()
    #print(s)

