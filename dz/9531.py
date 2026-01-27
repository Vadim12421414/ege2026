from itertools import *
graph='АБ БВ ВГ БД АВ ДЕ ЕЗ ЕЖ ЗЖ ЗА ГД'.split()
matrix='345 35 128 156 124 478 68 367'.split()
print(*range(1, 9))
for i in permutations('АБВГДЖЕЗ'):
    if all(str(i.index(x)+1)in matrix[i.index(y)] for x, y in graph):
        print(*i)
