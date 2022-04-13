# -*- coding: utf-8 -*-


# imports
import numpy

from gui import *
from controller import *
from repository import *
from domain import *


# create a menu
#   1. map options:
#         a. create random map
#         b. load a map
#         c. save a map
#         d visualise map
#   2. EA options:
#         a. parameters setup
#         b. run the solver
#         c. visualise the statistics
#         d. view the drone moving on a path
#              function gui.movingDrone(currentMap, path, speed, markseen)
#              ATTENTION! the function doesn't check if the path passes trough walls

class UI:
    def __init__(self):
        self.defaultArgs = {
            'iterations': 10000,
            'popSize': 100,
            'individualSize': 10,
            'crossOver': 0.8,
            'mutate': 0.01,
            'runs': 2
        }

    def stats(self, P):
        pass

    def run(self):
        cont = controller(self.defaultArgs)
        # pg = initPyGame((400, 400))
        map = Map()
        map.randomMap()
        first = input(
            "1. map options\n\ta. create random map\n\tb. load a map\n\tc. save a map\n\td. see map\n2. EA options")
        while first == "1":
            option = input("a,b,c,d\n")
            if option == "a":
                map = cont.genMap()
            if option == "b":
                file = input("file name:")
                map = cont.loadMap(file)
            if option == "c":
                file = input("file name:")
                cont.saveMap(file, map)
            if option == "d":
                pg = initPyGame((400, 400))
                pg.blit(image(map), (0, 0))
                pygame.display.flip()
                time.sleep(3)
                closePyGame()
            first = input("1 or 2\n")
        cont.setMap(map)

        a = input(
            "Choose the number of iterations. \nInability to decide will lead to me making the choice for you (1000): ")
        if a != "":
            self.defaultArgs['iterations'] = int(a)
        a = input(
            "Choose the population size. \nInability to decide will lead to me making the choice for you (1000): ")
        if a != "":
            self.defaultArgs['popSize'] = int(a)
        a = input(
            "Choose the individual size. \nInability to decide will lead to me making the choice for you (20): ")
        if a != "":
            self.defaultArgs['individualSize'] = int(a)
        a = input(
            "Choose the cross-over rate. \nInability to decide will lead to me making the choice for you (0.8): ")
        if a != "":
            self.defaultArgs['crossOver'] = float(a)
        a = input(
            "Choose the mutation rate. \nInability to decide will lead to me making the choice for you (0.01): ")
        if a != "":
            self.defaultArgs['mutate'] = float(a)

        cont.setArgs(self.defaultArgs) # redundant?
        # pg.blit(image(cont.getMap()), (0, 0))
        # pygame.display.flip()
        # time.sleep(3)
        # closePyGame()
        seeds, fits, bests = cont.solver()
        for i in range(2):
            print(i, " seed:", str(seeds[i]), "fitness:" + str(fits[i]) + "  best=", end=" ")
            for x in bests[i].x:
                if x == 0:
                    print("UP", end=" ")
                if x == 1:
                    print("RIGHT", end=" ")
                if x == 2:
                    print("LEFT", end=" ")
                if x == 3:
                    print("DOWN", end=" ")
            print()

        while True:
            print()
            a = input("0.Visualise statistics\n 1.See drone\n")
            if a == "0":
                avg = numpy.average(fits)
                stddev = numpy.std(fits)
                var = numpy.var(fits)
                print("avg=", avg)
                print("stddev=", stddev)
                print("var=", var)

            if a == "1":
                b = input("Choose run:")
                path = self.getPath(bests[int(b)])
                movingDrone(cont.getMap(), path, 5)

    def getPath(self, individual):
        directions = [(0, -1), (1, 0), (-1, 0), (0, 1)]
        start = (0, 0)
        path = [start]
        for move in individual.x:
            x, y = 0, 0
            x = start[0] + directions[move][0]
            y = start[1] + directions[move][1]
            path.append((x, y))
            start = (x, y)

        print("path=", end=" ")
        for i in path:
            print(i, end=" ")
        print()
        return path


u = UI()
u.run()
