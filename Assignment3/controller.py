from repository import *

rnd = Random()


class controller():
    def __init__(self, args):
        # args - dictionary of parameters needed in the controller
        self.population = None
        self.args = args
        self.repo = Repository()

    def getMap(self):
        return self.repo.getMap()

    def setMap(self, map):
        self.repo.setMap(map)

    def genMap(self):
        return self.repo.genMap()

    def loadMap(self, file):
        return self.repo.loadMap(file)

    def saveMap(self, file, map):
        return self.repo.saveMap(file, map)

    def setArgs(self, args):
        self.args = args

    def iteration(self):
        # args - list of parameters needed to run one iteration
        # a iteration:
        # selection of the parents
        # create offsprings by crossover of the parents
        # apply some mutations
        # selection of the survivors
        # steady - state --
        for _ in range(self.args['popSize']):
            p1, p2 = self.population.selection(2)
            kid = p1.crossover(p2,self.args['crossOver'])
            kid.mutate(self.args['mutate'])
            kid.fitness()
            worst = self.population.getWorst()
            if worst.getFintess() < kid.getFintess():
                worst = kid


    def run(self):
        # args - list of parameters needed in order to run the algorithm

        # until stop condition
        #    perform an iteration
        #    save the information needed for the statistics

        # return the results and the info for statistics
        for _ in range(self.args['iterations']):
            self.iteration()
        return self.population.getBest().getFintess()

    def solver(self):
        # args - list of parameters needed in order to run the solver
        # 30 it thing
        seeds = []
        avgFits = []
        best = []
        for i in range(self.args['runs']):
            seed = randint(0, 10000)
            rnd.seed(seed)
            self.population = self.repo.createPopulation([self.args['popSize'], self.args['individualSize']], rnd)
            avgFits.append(self.run())
            seeds.append(seed)
            best.append(self.population.getBest())
            print("Iteration "+ str(i) + " #")
        return seeds, avgFits, best
        # create the population,
        # run the algorithm
        # return the results and the statistics

        pass
