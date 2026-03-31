from itertools import *
graph='fa ab ad dc df ef ec cb eg gb'.split()
matrix='457 567 45 136 123 247 126'.split()
print(*range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)