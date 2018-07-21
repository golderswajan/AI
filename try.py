import numpy as np

a = [list(0 for i in range(8)) for j in range(8)]
a[4][0] = 8
a[5][1] = 8
a[6][2] = 8
a[3][3] = 8
a[4][4] = 8
a[5][5] = 8
a[6][6] = 8
a[5][7] = 8


def output(a):
    temp = ''
    for i in a:
        temp += str(i)
        temp += '\n'
    return temp

print(output(a))

b =a

b[0][0] = 8

print(output(a))