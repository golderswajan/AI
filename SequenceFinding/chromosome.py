import numpy as np
fixed_sequence = [1, 1, 1, 0, 0, 0, 0, 1, 1, 0]


class Chromosome:
    """ Simple Chromosome designed gor GA """

    def __init__(self, genes=list()):
        if not genes:
            genes = list(np.random.randint(2, size=10))
        self.genes = genes

    def get_fitness(self):
        fitness = 0
        for i in range(len(self.genes)):
            if fixed_sequence[i] != self.genes[i]:
                fitness += 1

        return fitness

    def get_genes(self):
        return self.genes

    def mutate(self, index):
        self.genes[index] = np.random.randint(2)

    def __repr__(self):
        return 'Sequence : ' + str(self.genes) + ' Fitness : ' + str(self.get_fitness())

