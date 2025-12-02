from itertools import *
#product - функция, которая формирует всевозможные комбинации символов длинны repeat
alph='12'
for val in product(alph, repeat=2):
    val=''.join(val)


 # permutation - функция, которая формирует всевозможные перестановки символов
for val in permutations(alph):
    val = ''.join(val)
    print(val)

#enumirate - нумерует элементы, начиная от старта
res = enumerate(alph, start =1)
print(*res)