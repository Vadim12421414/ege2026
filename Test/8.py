from itertools import *
ans=[]
alph=sorted('гранит')
for pos, val in enumerate(product(alph, repeat=6)):
    if val[0]!=0:
        if val[0]!='а' and val[0]!='г' and val[0]!='и':
            if val.count('а')==1:
                if pos%2!=0:
                    ans.append(pos)
                    break
print(ans)



