""" a + 2b + 3c + 4d = 30 solving """
from chromosome import Chromosome
import numpy as np
import copy


def crossover(first_parent, second_parent):
    crossover_point = np.random.randint(1, 3)
    first_parent = copy.deepcopy(first_parent.get_genes())
    second_parent = copy.deepcopy(second_parent.get_genes())
    first_child = Chromosome(first_parent[:crossover_point]+second_parent[crossover_point:])
    second_child = Chromosome((second_parent[:crossover_point] + first_parent[crossover_point:]))

    return [first_child, second_child]


def mutation(parent):
    position = np.random.randint(4)
    parent_genes = copy.deepcopy(parent.get_genes())
    parent_genes[position] = np.random.randint(31)
    position = np.random.randint(4)
    parent_genes[position] = np.random.randint(31)
    child = Chromosome(parent_genes)
    return child
