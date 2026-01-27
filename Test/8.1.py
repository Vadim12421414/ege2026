from itertools import *
from string import printable

cnt = 0
alph = printable[10:16]
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val[0] != alph[0]:
        if val[0] != alph[4]:
            if val[-1] != alph[0]:
                if val[-1] != alph[4]:
                    cnt += 1
print(cnt)
