from itertools import permutations
matrix='258 17 56 68 138 347 26 145'.split()
graph='ad ag ac dh hf hb fe eg gc cb'.split()
print(*range(1, 9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)
print(37+15)

