# -*- coding: utf-8 -*-

from random import *
from utils import *
import numpy as np
from controller import rnd


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
    def __init__(self, map: Map, size=0):
        self.__size = size
        self.__f = None
        self.__map = map
        self.__x = [rnd.randint(0, 3) for _ in range(self.__size)]

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
        pass
        # compute the fitness for the individual
        # and save it in self.__f

    def mutate(self, mutateProbability=0.01):
        if rnd.random() < mutateProbability:
            chosen = rnd.randint(0, self.__size - 1)
            new = self.__x[chosen]
            while self.__x[chosen] == new:
                self.__x[chosen] = rnd.randint(0, 3)

    def crossover(self, otherParent, crossoverProbability=0.8):
        offspring1, offspring2 = Individual(self.__map, self.__size), Individual(self.__map, self.__size)
        if rnd.random() < crossoverProbability:
            pass
            # perform the crossover between the self and the otherParent 

        return offspring1, offspring2

    def getFintess(self):
        return self.__f

    def getSize(self):
        return self.__size


class Population():
    def __init__(self, populationSize=0, individualSize=0):
        self.__populationSize = populationSize
        self.__v = [Individual(individualSize) for x in range(populationSize)]
        self.avgFits = []

    def evaluate(self):
        # evaluates the population
        for x in self.__v:
            x.fitness()

    def selection(self, k=1):
        # perform a selection of k individuals from the population
        # and returns that selection
        pass

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


m = Map()
m.randomMap()
i = Individual(m, 10)
