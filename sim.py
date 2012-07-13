#!/usr/bin/env python 
#-*- coding: utf-8 -*-

__version__ = "0.0.1"

import heapq
import scipy.stats as stats

import model
import statistic
import chart_generator

class Queue(object):

    def __init__(self):
        self.queue = []

    @property
    def first(self):
        return heapq.heappop(self.queue)

    def add(self, item):
        heapq.heappush(self.queue, item)

    def __len__(self):
        return len(self.queue)

class Simulation(object):

    def __init__(self, n_clients=10, seed=0):
        """Crea una nova simulació on el nombre de clients és la variable."""
        # Quantes passes farem a cada intent de simulació
        self.n_steps = n_clients * 20
        self.task = 0
        self.clock = 0
        self.n_clients = n_clients
        self.user = model.User(seed)
        self.cpu = model.CPU(seed)
        self.disk = model.Disk(seed)
        self.queue = Queue()
        self.statistic = statistic.Statistic(n_clients)
        self.service_pass = {
            self.disk: self.service_disk,
            self.cpu: self.service_cpu,
            self.user: self.service_user,
            }

    def begin(self):
        for task in range(self.n_clients):
            self.add_task(self.user, task)
        self.task = self.n_clients

    def add_task(self, server, task):
        time = server.add(task)
        if time:
            self.enqueu(server, time)

    def enqueu(self, server, time):
            time += self.clock
            self.queue.add((time, server))

    def sim(self):
        self.simulation()
        return self.statistic.calc_rt()

    def simulation(self):
        self.begin()
        while True: 
            for step in range(self.n_steps):
                self.step()
            if self.statistic.is_safe_to_stop:
                break


    def step(self):
        """
        Passa de la simulació.
        Primer es resol la tasca en marxa.
        Es concatenen possibles tasques pel mateix servidor.
        Llavors es resol la continuació d'altres serveis.
        """
        time, server = self.queue.first
        self.clock = time
        task, time = server.process()
        if time:
            self.enqueu(server, time)
        self.service_pass[server](task)

    def service_disk(self, task):
        """Tasca i connexió d'un disc."""
        self.add_task(self.cpu, task)

    def service_user(self, task):
        """Tasca i connexió dels usuaris. Entrada d'esdeveniment"""
        self.task += 1
        new_task = self.task
        self.statistic.add_in(new_task, self.clock)
        self.add_task(self.cpu, new_task)

    def service_cpu(self, task):
        """Tasca i connexió de la CPU. Inclou el càlcul de sortida."""
        choose = self.cpu.choose()
        if choose == 'disk':
            self.add_task(self.disk, task)
        elif choose == 'user':
            self.statistic.add_out(task, self.clock)
            self.add_task(self.user, task)


class SimulationWithReplica(object):

    def __init__(self, n_replica=50, n_clients=10):
        # replica_pass és per si cal executar vàries vegades
        self.replica_pass = 1
        self.error = 0.1
        # per acceplerar el procés
        self.error = 0.1
        self.n_replica = n_replica
        self.n_clients = n_clients
        self.chart = chart_generator.Chart()
        self.values = []

    def _do_simulation(self):
        for replica in range(self.n_replica):
            seed = self.replica_pass * replica
            sim = Simulation(self.n_clients, seed=seed)
            sim.simulation()
            self.values.append(sim.statistic.calc_rt())
        self.replica_pass += 1

    def sim(self):
        while True:
            self._do_simulation()
            if self._error_good_enought():
                break
        return self.calc_rt()

    def calc_rt(self):
        return stats.tmean(self.values)

    def _error_good_enought(self):
        """Determina les configuracions de si cal tornar a replicar. L'enunciat
        determina un 0.10 de marge d'error. """
        # http://docs.scipy.org/doc/scipy/reference/stats.html#module-scipy.stats
        error = stats.tsem(self.values)
        return error < self.error
