from itertools import *
cnt=0
alph=sorted('котбус')
for val in product(alph,repeat=8):
    val = ''.join(val)
    if 'кот' in val:
        if val[0]!='у' and val[0]!='о':
            cnt += 1
print(cnt)
