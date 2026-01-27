from itertools import *
from string import printable

alph = printable[:9]
cnt = 0
for val in product(alph, repeat=7):
    val[0] != '0'
    val = ''.join(val)
    if int(val.count('8')) == 1:
        if int(val[0]) % 2 == 0:
            if int(val[-1]) % 2 != 0:
                cnt += 1
print(cnt)
