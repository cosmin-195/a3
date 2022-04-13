# -*- coding: utf-8 -*-


# imports
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
            'iterations': 100,
            'popSize': 100,
            'individualSize': 20,
            'crossOver': 0.8,
            'mutate': 0.01
        }

    def stats(self, P):
        pass

    def run(self):
        # a = input("Choose the number of iterations. \nInability to decide will lead to me making the choice for you (1000): ")
        # if a!="":
        #     self.defaultArgs['iterations'] = int(a)
        # a = input(
        #     "Choose the population size. \nInability to decide will lead to me making the choice for you (1000): ")
        # if a != "":
        #     self.defaultArgs['popSize'] = int(a)
        # a = input(
        #     "Choose the individual size. \nInability to decide will lead to me making the choice for you (20): ")
        # if a != "":
        #     self.defaultArgs['individualSize'] = int(a)
        # a = input(
        #     "Choose the cross-over rate. \nInability to decide will lead to me making the choice for you (0.8): ")
        # if a != "":
        #     self.defaultArgs['iterations'] = float(a)
        # a = input(
        #     "Choose the mutation rate. \nInability to decide will lead to me making the choice for you (0.01): ")
        # if a != "":
        #     self.defaultArgs['iterations'] = float(a)

        cont = controller(self.defaultArgs)
        pg = initPyGame((400, 400))
        pg.blit(image(cont.getMap()), (0, 0))
        pygame.display.flip()
        time.sleep(3)
        closePyGame()
        seeds, fits, bests = cont.solver()
        for i in range(30):
            print(i, " seed:", str(seeds[i]), "fitness:" + str(fits[i]) + "  best=",end=" ")
            for x in bests[i].x:
                if x == 0:
                    print("UP",end=" ")
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
            if a == "1":
                b = input("Choose run:")
                self.stats()


u = UI()
u.run()
