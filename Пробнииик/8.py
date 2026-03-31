from itertools import *
from string import *
alph=printable[:7]
cnt=0
for val in product(alph, repeat=7):
    val=''.join(val)
    if val[0]!='0':
        if val[0]!='3' and val[0]!='5' and ('22' and '44' not in val):
            cnt+=1
print(cnt)