class Chromosome:
    def __init__(self, decimal, binary):
        self.decimal = None
        self.binary = None
        if not binary:
            self.decimal = decimal
            self.binary = self.dec_to_bin()
        if not decimal:
            self.binary = binary
            self.decimal = self.bin_to_dec()
        self.fitness = self.decimal*self.decimal

    def mutate(self, index):
        self.binary = self.binary[:index] + '1' + self.binary[index+1:]
        self.decimal = self.bin_to_dec()
        self.fitness = self.decimal * self.decimal

    def dec_to_bin(self):
        return "{0:05b}".format(self.decimal)

    def bin_to_dec(self):
        return int(self.binary, 2)

    def __repr__(self):
        return 'decimal->' + str(self.decimal)+'\nbinary->' + str(self.binary)+'\nfitness->' + str(self.fitness) + '\n'


def overall_fitness(population):
    summatio = 0
    for chromosome in population:
        summatio += chromosome.fitness
    return summatio
