from chromosome import Chromosome
import numpy as np


def crossover(parent_one, parent_two):

    bin_one = parent_one.binary
    bin_two = parent_two.binary
    new_bin_one = bin_one[:2] + bin_two[2:]
    new_bin_two = bin_two[:2] + bin_one[2:]

    child_one = Chromosome('', new_bin_one)
    child_two = Chromosome('', new_bin_two)

    return child_one, child_two


def mutation(parent_one):
    random_index = np.random.randint(5)
    parent_one.mutate(random_index)
