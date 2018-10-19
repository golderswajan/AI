import numpy as np
import copy
from chromosome import Chromosome


def single_point_crossover(first, second):
    point = np.random.randint(first.sudoku_size)
    # print(point)
    temp_first = copy.deepcopy(first.get_sudoku())
    temp_second = copy.deepcopy(second.get_sudoku())

    for i in range(point, first.sudoku_size):
        for j in range(first.sudoku_size):
            temp = temp_first[i][j]
            temp_first[i][j] = temp_second[i][j]
            temp_second[i][j] = temp

    return Chromosome(9, temp_first), Chromosome(9, temp_second)


def double_point_crossover(first, second):
    start = np.random.randint(first.sudoku_size)
    end = np.random.randint(first.sudoku_size)
    if start > end:
        start, end = end, start
    temp_first = copy.deepcopy(first.get_sudoku())
    temp_second = copy.deepcopy(second.get_sudoku())
    # print(start, end)
    for i in range(start, end):
        for j in range(first.sudoku_size):
            temp = temp_first[i][j]
            temp_first[i][j] = temp_second[i][j]
            temp_second[i][j] = temp

    return Chromosome(9, temp_first), Chromosome(9, temp_second)


def uniform_crossover(first, second):
    temp_first = copy.deepcopy(first.get_sudoku())
    temp_second = copy.deepcopy(second.get_sudoku())

    for i in range(first.sudoku_size):
        choose = np.random.randint(first.sudoku_size)
        if choose % 2 == 0:
            for j in range(first.sudoku_size):
                temp = temp_first[i][j]
                temp_first[i][j] = temp_second[i][j]
                temp_second[i][j] = temp

    return Chromosome(9, temp_first), Chromosome(9, temp_second)


def mutation_swap(first):
    temp_first = copy.deepcopy(first.get_sudoku())
    rows = np.random.randint(3)

    for i in range(rows):
        row_number = np.random.randint(first.sudoku_size)
        times = np.random.randint(3)
        for j in range(times):
            start = np.random.randint(first.sudoku_size)
            end = np.random.randint(first.sudoku_size)

            # print(row_number, start)
            temp = temp_first[row_number][start]
            # print(temp)

            temp_first[row_number][start] = temp_first[row_number][end]
            temp_first[row_number][end] = temp

    return Chromosome(9, temp_first)


def mutation_reinitialize(first):
    temp_first = copy.deepcopy(first.get_sudoku())
    rows = np.random.randint(3)
    for i in range(rows):
        available = list((k + 1) for k in range(first.sudoku_size))
        for j in range(first.sudoku_size):
            digit = available[np.random.randint(len(available))]
            temp_first[i][j] = digit
            available.remove(digit)
    return Chromosome(9, temp_first)


