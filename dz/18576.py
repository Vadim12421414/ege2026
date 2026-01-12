from itertools import *
def f(w, y, z, x):
    return  not(w <= (x == y)) and (z <= x)
for i in product((0, 1), repeat=7):
    table=[
        (i[0], 1, 1, i[1]),
        (0, i[2], i[3], 0),
        (i[4], 0, 1, 0)
    ]
    if len(set(table))==len(table):
        for p in permutations('zwyx'):
            if [f(**dict(zip(p, t))) for t in table]==[1, 1, 1]:
                print(*p, sep='')