""" a + 2b + 3c + 4d = 30 solving """
from chromosome import Chromosome
from equation_solver_utilities import crossover, mutation

population_size = 20
population = list()
crossover_rate = 7

for i in range(population_size):
    population.append(Chromosome())

population.sort(key=lambda z: z.fitness)

children = list()
for i in range(100):
    for j in range(crossover_rate):
        first_child, second_child = crossover(population[j], population[j + 1])
        children.append(first_child)
        children.append(second_child)
    children.sort(key=lambda z: z.fitness)
    for j in range(crossover_rate, population_size):
        population[j] = mutation(population[j])
    population.sort(key=lambda z: z.fitness)

    for j in range(crossover_rate):
        population[population_size - 1 - j] = children[j]
    population.sort(key=lambda z: z.fitness)
    print('generation->', (i+1), 'best chromosome->', population[0])
    if population[0].fitness == 0:
        print('Solution Found')
        break
