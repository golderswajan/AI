from chromosome import Chromosome, overall_fitness
import ga_accessories as g

population = list()
population.append(Chromosome(13, ''))
population.append(Chromosome(24, ''))
population.append(Chromosome(8, ''))
population.append(Chromosome(19, ''))

print(overall_fitness(population))

generation = 5
chromosome_no = 4
children = list()

for i in range(generation):
    for j in range(chromosome_no - 1):
        children_one, children_two = g.crossover(population[j], population[j+1])
        children.append(children_one)
        children.append(children_two)
    children.sort(key=lambda z: z.fitness, reverse=True)
    for j in range(chromosome_no):
        g.mutation(population[j])
    population.sort(key=lambda z: z.fitness, reverse=True)

    for j in range(2):
        population[chromosome_no - 1 - j] = children[j]

    print(overall_fitness(population))
print(population)