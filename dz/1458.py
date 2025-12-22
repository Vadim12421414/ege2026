from itertools import *
matrix='256 13467 2456 237 136 1235 24'.split()
graph='аб бе уж жд дв ва га гб гд гв де'.split()
print(*range(1,8))
for i in permutations('абвгдеж'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
