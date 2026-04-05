from itertools import *
from string import printable as pri
alph=pri[:12]
cnt=0
for val in product(alph, repeat=5):
    kol=0
    val=''.join(val)
    if val[0]!='0':
        if val.count('7')==1:
            for i in val:
                if int(i, 12)>8:
                    kol+=1
            if kol<=3:
                cnt+=1
print(cnt)

