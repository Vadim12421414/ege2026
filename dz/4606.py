from itertools import *
matrix='68 47 45 237 368 15 248 157'.split()
graph='ac cd ce dh he eg gf fb ba af '.split()
print(*range(1,9))
for i in permutations('acdhegfb'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

