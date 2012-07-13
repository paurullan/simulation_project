#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

__version__ = "0.0.1"

import rand


class Server(object):

    def __init__(self, seed=0):
        self.generator = rand.Generator(seed)
        self.name = "server"
        self.working = None
        self.queue = []

    def add(self, task):
        if not self.working:
            self.working = task
            return self.service()
        else:
            self.queue.append(task)
            return None

    def process(self):
        """
        Acabam de processar una petició. Tornam l'element processat i miram si
        tenim més tasques.
        """
        assert (self.working), "No es pot processar si no hi ha tasques"
        task = self.working
        if self.queue:
            self.working = self.queue.pop(0)
            time = self.service()
        else:
            self.working = None
            time = None
        return (task, time)

    @property
    def empty(self):
        """El servidor és buit"""
        return self.working == None

    @property
    def empty_queue(self):
        """La qua del servidor és buida"""
        return len(self.queue) == 0


    def service(self):
        """Determina el temps de processament en ms. Cal reimplementar-lo per
        cada sub-servidor"""
        return 1

    def __len__(self):
        return len(self.queue)


class User(Server):
    """
    Segons el nostre enunciat els ususaris tenen un temps de reflexió de
    Exp(10*1000) en ms.
    """

    def __init__(self, seed=0):
        super(User, self).__init__(seed)
        self.name = "user"
        self.lambd = 10 * 1000  # 10s en ms

    def add(self, task):
        return self.service()

    def process(self):
        return 0, None

    @property
    def empty_queue(self):
        """Truc per simular un servidor sense ques: que sempre estigui buit."""
        return True

    @property
    def empty(self):
        return True

    def service(self):
        """Exp(10*1000) ms"""
        return self.generator.exp(self.lambd)


class CPU(Server):
    """Segons el nostre enunciat la cpu té un temps de resposta C(0.4) ms."""

    def __init__(self, seed=0):
        super(CPU, self).__init__(seed)
        self.name = "cpu"

    def service(self):
        """C(0.4) ms"""
        return self.generator.constant(0.4)

    def choose(self):
        """Escull amb un 0.833 de probabilitats anar al disk (5 transaccions)"""
        prob = self.generator.num
        if prob < 0.833:
            return 'disk'
        else:
            return 'user'


class Disk(Server):
    """
    Segons el nostre enunciat el disc té un temps de resposta que és la
    combinació de les tres distribucions: seek, latència i transfarència de la
    forma (en ms) Exp(3.4) + U(0, 4) + C(2, 5).
    """

    def __init__(self, seed=0):
        super(Disk, self).__init__(seed)
        self.name = "disk"

    def service(self):
        """ Exp(3.4) + U(0, 4) + C(2, 5)"""
        exp = self.generator.exp(3.4)
        u = self.generator.uniform(0, 4)
        c = self.generator.constant(3.5)
        return exp + u + c
