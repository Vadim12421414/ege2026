from itertools import *
matrix='37 367 125 56 34 247 126'.split()
graph='ad de eg gc cf fb ba be'.split()
print(*range(1,8))
for i in permutations('adegcfb'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
