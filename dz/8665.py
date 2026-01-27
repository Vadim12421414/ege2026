from itertools import *
cnt=0
num = '0123456789ab'
for val in product(num, repeat=7):
    val=''.join(val)
    if val[0]!=0 and val.count('b') == 2:
        for i in '02468a':
            val = val.replace(i, '*')
        for i in '13579b':
            val = val.replace(i, '+')
        if  '++' not in val and '**' not in val:
            cnt += 1
print(cnt)

