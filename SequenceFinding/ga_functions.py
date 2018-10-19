from chromosome import Chromosome
import numpy as np


def single_point_crossover(first_parent, second_parent, crossover_point):
    first_parent = first_parent.get_genes()
    second_parent = second_parent.get_genes()
    first_child = Chromosome(first_parent[:crossover_point]+second_parent[crossover_point:])
    second_child = Chromosome((second_parent[:crossover_point] + first_parent[crossover_point:]))

    return [first_child, second_child]


def double_point_crossover(first_parent, second_parent,start_point, end_point):
    first_parent = first_parent.get_genes()
    second_parent = second_parent.get_genes()
    first_child = Chromosome(first_parent[:start_point] + second_parent[start_point:end_point] + first_parent[end_point:])
    second_child = Chromosome(second_parent[:start_point] + first_parent[start_point:end_point] + second_parent[end_point:])

    return [first_child, second_child]


def uniform_crossover(first_parent, second_parent):
    first_child = first_parent.get_genes()
    second_child = second_parent.get_genes()

    for i in range(len(first_child)):
        if np.random.randint(10) % 2 == 0:
            temp = first_child[i]
            first_child[i] = second_child[i]
            second_child[i] = temp

    return [Chromosome(first_child), Chromosome(second_child)]


def mutation(chromosome):
    for i in range(len(chromosome.get_genes())):
        if np.random.randint(10) % 2 != 0:
            chromosome.mutate(i)
    # return chromosome






