from string import printable
from itertools import *
alph = printable[:25]
cnt = 0
for val in product(alph, repeat=4):
    val = ''.join(val)
    if val[0]!= '0':
        val1=val
        for i in alph[0:25:2]:
            val1 = val.replace(i, '+')
        for j in alph[16:25]:
            val = val.replace(j, '*')
        a1 = val.count('*')>2
        b1 = val1.count('+') >= 1
        if b1+a1 ==2:
            cnt+=1
print(cnt)