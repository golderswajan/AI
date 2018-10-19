import numpy as np
from chromosome import Chromosome
print(np.random.rand())
a = np.zeros(shape=(4,4), dtype=int)
b = np.zeros(shape=(4,4), dtype=int)
s = list()
s.append(Chromosome(4,a))
s.append(Chromosome(4,b))
print(s)
print('swajan')
s=set(s)
print('swajan')
print(s)
# print((a==b).all())

