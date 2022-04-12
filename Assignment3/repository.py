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
        pop = Population(rnd, self.cmap, args[0], args[1])
        self.__populations.append(pop)
        return pop


    def saveMap(self, file):
        with open(file, 'wb') as f:
            pickle.dump(self.cmap, f)
            f.close()

    def loadMap(self, file):
        with open(file, 'rb') as f:
            self.cmap = pickle.load(f)
            f.close()


    # TO DO : add the other components for the repository: 
    #    load and save from file, etc
            