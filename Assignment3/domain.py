# -*- coding: utf-8 -*-

from random import *
from utils import *
import numpy as np


class Map:
    def __init__(self, n=20, m=20):
        self.n = n
        self.m = m
        self.surface = np.zeros((self.n, self.m))

    def randomMap(self, fill=0.2):
        for i in range(self.n):
            for j in range(self.m):
                if random() <= fill:
                    self.surface[i][j] = 1

    def __str__(self):
        string = ""
        for i in range(self.n):
            for j in range(self.m):
                string = string + str(int(self.surface[i][j]))
            string = string + "\n"
        return string


# the glass gene can be replaced with int or float, or other types
# depending on your problem's representation
# 0 - UP, 1 - DOWN, 2 - LEFT, 3- RIGHT

class gene:
    def __init__(self):
        pass


directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


class Individual:
    def __init__(self, _rnd, map: Map, start, size=0):
        self._rnd = _rnd
        self.start = start
        self.__size = size
        self.__f = None
        self.__map = map
        self.__map.surface = map.surface.__deepcopy__()
        self.x = [rnd.randint(0, 3) for _ in range(self.__size)]

    # def __initialize(self):
    # start = [randint(0, self.__map.n), randint(0, self.__map.m)]
    # while self.__map.surface[start[0]][start[1]] == 1:
    #     start = [randint(0, self.__map.n), randint(0, self.__map.m)]
    # path = [start]
    # next = start.copy()
    # for i in range(self.__size - 1):
    #     shuffle(directions)
    #     for j in range(4):
    #         next[0] += directions[j][0]
    #         next[1] += directions[j][1]
    #         if self.__map.surface[next[0]][next[1]] == 0:
    #             path.append(next.copy())
    #             break
    #         else:
    #             next[0] -= directions[j][0]
    # #             next[1] -= directions[j][1]
    # print(path)
    # return path

    def fitness(self):
        f = 0
        x, y = self.start
        for dir in self.x:
            move = directions[dir]
            if (self.__map.surface[x][y] != 1):
                self.__map.surface[x][y] = 2
            else:
                stop = 1
                break
            u, g = x, y
            for var in directions:
                x, y = u, g
                while ((0 <= x + var[0] < self.__map.n and
                        0 <= y + var[1] < self.__map.m) and
                       self.__map.surface[x + var[0]][y + var[1]] != 1):
                    x = x + var[0]
                    y = y + var[1]
                    f += 1
            x += move[0]
            y += move[1]
        self.__f = f

    def mutate(self, mutateProbability=0.01):
        if self._rnd.random() < mutateProbability:
            chosen = self._rnd.randint(0, self.__size - 1)
            new = self.x[chosen]
            while self.x[chosen] == new:
                self.x[chosen] = self._rnd.randint(0, 3)

    def crossover(self, otherParent, crossoverProbability=0.8):
        offspring1, offspring2 = Individual(self.__map, self.__size), Individual(self.__map, self.__size)
        if self._rnd.random() < crossoverProbability:
            cut = self._rnd.randint(0, offspring1.__size)
            for i in range(offspring1.__size):
                if i < cut:
                    offspring1.x[i] = self.x[i]
                    offspring2.x[i] = otherParent.x[i]
                else:
                    offspring1.x[i] = otherParent.x[i]
                    offspring2.x[i] = self.x[i]
            offspring1.fitness()
            offspring2.fitness()
            if offspring1.__f > offspring2.__f:
                return offspring1
            return offspring2
            # perform the crossover between the self and the otherParent

        return offspring1, offspring2

    def getFintess(self):
        return self.__f

    def getSize(self):
        return self.__size


class Population():
    def __init__(self, _rnd, start, map: Map, populationSize=0, individualSize=0):
        self.__populationSize = populationSize
        self.__v = [Individual(map, start, individualSize) for x in range(populationSize)]
        self.avgFits = []
        self._rnd = _rnd

    def evaluate(self):
        # evaluates the population
        for x in self.__v:
            x.fitness()

    def selection(self, k=2, tournamentSize = 15):
        result = []
        for _ in range(k):
            s = [x for x in range(self.__populationSize)]
            self._rnd.shuffle(s)
            s = s[:tournamentSize]
            while len(s) > 1:
                if self.__v[s[-1]].getFintess() > self.__v[s[-2]].getFintess():
                    self.__v[s[-2]]=self.__v[s[-1]]
                s.pop()
            result.append(s[0])
        return result


    def avgFit(self):
        s = 0
        for x in self.__v:
            s += x.getFintess()
        return s / self.__v[0].getSize()

    def getBest(self):
        fit = self.__v[0]
        for i in self.__v:
            if i.fitness() > fit.fitness():
                fit = i
        return fit

    def getWorst(self):
        fit = self.__v[0]
        for i in self.__v:
            if i.fitness() < fit.fitness():
                fit = i
        return fit


m = Map()
m.randomMap()
p = Population((0,0),m,100)
p.evaluate()
p.selection()

