from itertools import *
graph='fb fg bc db cg de ea ag cd'.split()
matrix='45  345 256 127 123 37 46'.split()
print(*range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x)+1) in matrix[i.index(y)]for x, y in graph):
        print(*i)
