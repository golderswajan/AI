import numpy as np


class Chromosome:

    def __init__(self, sudoku_size, sudoku=np.array([])):
        self.sudoku_size = sudoku_size
        if not sudoku.size:
            self.sudoku = np.zeros(shape=(sudoku_size, sudoku_size), dtype=int)
            self.populate_sudoku()
        else:
            self.sudoku = sudoku

        self.fitness_matrix = np.zeros(shape=(2, self.sudoku_size, ), dtype=int)
        self.fitness = self.get_fitness()
        pass

    def get_sudoku(self):
        return self.sudoku

    def populate_sudoku(self):
        for i in range(self.sudoku_size):
            available = list((k+1) for k in range(self.sudoku_size))
            for j in range(self.sudoku_size):
                digit = available[np.random.randint(len(available))]
                self.sudoku[i][j] = digit
                available.remove(digit)
        pass

    def get_fitness(self):
        fitness = 0
        for i in range(self.sudoku_size):
            column = self.sudoku[:, i]
            column_fitness = self.sudoku_size - len(set(column))
            fitness += column_fitness
            self.fitness_matrix[0][i] = column_fitness
        index = 0
        for i in range(0, self.sudoku_size, 3):
            for j in range(0, self.sudoku_size, 3):
                block = self.sudoku[i:i+3, j:j+3]
                block = block.flatten()
                block_fitness = self.sudoku_size - len(set(block))
                fitness += block_fitness
                self.fitness_matrix[1][index] = block_fitness
                index += 1
        return fitness
        pass

    def __eq__(self, other):
        return (self.sudoku == other.sudoku).all()


    def __hash__(self):
        return hash(str(self.sudoku))

    def __repr__(self):
        output = ''
        for i in range(self.sudoku_size):
            for j in range(self.sudoku_size):
                output += str(self.sudoku[i][j])+'  '
                if (j+1) % 3 == 0:
                    output += ' '
            output += '\n'
            if (i+1) % 3 == 0:
                output += '\n'
        output += str(self.fitness_matrix)
        output += '\nFitness -> ' + str(self.fitness)+'\n'
        return output
        pass
