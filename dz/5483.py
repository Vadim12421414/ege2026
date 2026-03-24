from itertools import *
def f(w, y, z, x):
    return not(y<=(x==w)) and (z<=x)
for i in product((0, 1), repeat=5):
    table=[
        (1, 1, 1, 0),
        (i[0], i[1], 0, 0),
        (i[2], 0, i[3], i[4])
    ]
    if len(set(table))==len(table):
        for p in permutations('zwyx'):
            if [f(**dict(zip(p, t))) for t in table]==[1, 0, 0]:
                print(*p, sep='')