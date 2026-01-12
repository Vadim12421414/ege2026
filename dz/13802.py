from itertools import *
graph='eh df af ea fc gc bg ed hb hg db '.split()
matrix='367 568 18 58 247 127 156 234'.split()
print(*range(1, 9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x)+1) in matrix[i.index(y)]for x, y in graph):
        print(*i)
