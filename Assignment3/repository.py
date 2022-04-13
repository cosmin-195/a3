# -*- coding: utf-8 -*-

import pickle
from domain import *

class Repository():
    def __init__(self):
        self.__populations = []
        self.cmap = Map()
        self.cmap.randomMap()
        
    def createPopulation(self, args, rnd):
        # args = [populationSize, individualSize] -- you can add more args
        pop = Population(rnd, (0,0),self.cmap, args[0], args[1])
        pop.evaluate()
        self.__populations.append(pop)
        return pop

    def getMap(self):
        return self.cmap

    def saveMap(self, file, map):
        with open(file, 'wb') as f:
            pickle.dump(map, f)
            f.close()

    def setMap(self, map):
        self.map = map

    def genMap(self):
        m = Map()
        m.randomMap()
        return m

    def loadMap(self, file):
        with open(file, 'rb') as f:
            map = pickle.load(f)
            f.close()
            return map


    # TO DO : add the other components for the repository: 
    #    load and save from file, etc
            