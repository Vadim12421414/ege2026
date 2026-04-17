from itertools import *
alph=sorted('сулак')
ans=[]
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val=''.join(val)
    if pos<=12368 and pos%2==0:
        if val[0]=='л' or val[0]=='с':
            for i in('уа'):
                i.replace('у', '+')
                i.replace('а', '+')
            if '++' not in val and val.count('+')<=2:
                ans.append(val)
print(len(ans))

