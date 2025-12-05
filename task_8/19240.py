from itertools import *
alph=sorted('январь')
cnt=[]
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val=''.join(val)
    if val[0]!='я' and val.count('ь') <2 and 'яя' not in val:
        cnt.append(val)
        cnt.append(pos)
print(cnt)
6443

