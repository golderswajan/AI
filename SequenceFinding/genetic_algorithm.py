from chromosome import Chromosome
import ga_functions as g

population_size = 20
crossover_rate = 11
population = list()
childrens = list()


def main():

    # Population Generation
    for x in range(population_size):
        population.append(Chromosome())

    population.sort(key=lambda z: z.get_fitness())

    print('------------ initial population--------------')
    for x in population:
        print(x)
    print('--------------------------')

    for j in range(100):

        print('iteration : ', j)
        # First Crossover Starts

        for i in range(crossover_rate):
            # Single Point Crossover
            first_child, second_child = g.single_point_crossover(population[i], population[i + 1], 4)
            childrens.append(first_child)
            childrens.append(second_child)

            # Double Point Crossover
            first_child, second_child = g.double_point_crossover(population[i + 1], population[i + 2], 2, 6)
            childrens.append(first_child)
            childrens.append(second_child)

            # Uniform Crossover
            first_child, second_child = g.uniform_crossover(population[i], population[i + 2])
            childrens.append(first_child)
            childrens.append(second_child)

        childrens.sort(key=lambda z: z.get_fitness(), reverse=False)

        # Mutation of right over chromosomes
        for i in range(crossover_rate, population_size):
            g.mutation(population[i])

        population.sort(key=lambda z: z.get_fitness(), reverse=True)

        # Replace Less Fit Parents With Best Fit Childs
        for i in range(crossover_rate):
            population[population_size - 1 - i] = childrens[i]

        population.sort(key=lambda z: z.get_fitness(), reverse=True)

        for x in population:
            if x.get_fitness() == 0:
                print('----------after crossover mutation for first iteration----------------')
                print('--------------------------')
                print(x)
                return


if __name__ == '__main__':
    main()
