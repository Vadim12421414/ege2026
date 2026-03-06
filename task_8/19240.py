from itertools import *
alph=sorted('январь')
ans=[]
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val=''.join(val)
    if val[0]!='я' and val.count('ь') <2 and 'яя' not in val:
        ans.append(val)
        ans.append(pos)
print(ans)
6443

