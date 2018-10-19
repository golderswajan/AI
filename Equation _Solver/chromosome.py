""" a + 2b + 3c + 4d = 30 solving """
import numpy as np


class Chromosome:

    def __init__(self, genes=list()):
        if not genes:
            self.genes = [np.random.randint(31) for i in range(4)]
        else:
            self.genes = genes
        self.fitness = self.get_fitness()

    def get_genes(self):
        return self.genes

    def get_fitness(self):
        return abs(30-(self.genes[0]+self.genes[1]*2+self.genes[2]*3+self.genes[3]*4))

    def __repr__(self):
        return str(self.genes)+'fitness->'+str(self.fitness)+'\n'
