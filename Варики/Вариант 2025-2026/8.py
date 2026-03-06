from itertools import *
alph=sorted('строка')
ans=[]
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val=''.join(val)
    if pos%2==0:
        if val[0]!='а' and val[0]!='с' and val[0]!='т':
            if val.count('о')==2:
                ans.append(pos)
print(ans)
