from itertools import *
graph='fe ec cg gd db ba af bf ed '.split()
matrix='256 134 267 27 16 135 34'.split()
print(*range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

