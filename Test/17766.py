from itertools import *
alph=sorted('сентябрь')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val=''.join(val)
    if val[0]!='0':
        if pos%2==0:
            if val[0]=='р' and 'ь' not in val:
                print(pos)
