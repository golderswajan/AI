from chromosome import Chromosome
import ga_functions as g
import numpy as np
population_size = 500
population = list()
crossover_rate = 170
mutation_threshold = .3
generation = 300
trial = 25


def main():
    global population, population_size, crossover_rate
    found_flag = False
    for t in range(trial):
        population = list()
        """---- initial population generation -------"""
        for i in range(population_size):
            population.append(Chromosome(9))

        population.sort(key=lambda z: z.fitness, reverse=False)
        children = list()
        for i in range(generation):
            for j in range(crossover_rate):
                first_child, second_child = g.single_point_crossover(population[j], population[j + 1])
                children.append(first_child)
                children.append(second_child)

                first_child, second_child = g.double_point_crossover(population[j + 1], population[j + 2])
                children.append(first_child)
                children.append(second_child)

                first_child, second_child = g.uniform_crossover(population[j], population[j + 2])
                children.append(first_child)
                children.append(second_child)
            children.sort(key=lambda z: z.fitness, reverse=False)

            for j in range(crossover_rate, population_size):
                alpha = np.random.rand()
                if mutation_threshold < alpha:
                    population[j] = g.mutation_swap(population[j])
                else:
                    population[j] = g.mutation_reinitialize(population[j])
            population.sort(key=lambda z: z.fitness, reverse=False)

            for j in range(crossover_rate):
                population[population_size - 1 - j] = children[j]

            population.sort(key=lambda z: z.fitness, reverse=False)

            print('trial->', t, 'generation->', i, 'fitness->', population[0].fitness, 'unique chromosome', len(set(population)))
            if population[0].fitness == 0:
                print(population[0])
                print('Solution Found')
                found_flag = True
                break

        if found_flag:
            break


if __name__ == '__main__':
    main()
