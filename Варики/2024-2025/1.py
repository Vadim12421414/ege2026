from itertools import *
graph='ef ec fg fd dg db ba ca cg'.split()
matrix='457 46 567 12 136 235 13'.split()
print(range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
#8+30