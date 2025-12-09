from itertools import *
alph=sorted('полина')
cnt=0
for val in product(alph, repeat=8):
    val=''.join(val)
    for i in 'оиа':
        val=val.replace(i, '*')
    for x in 'плн':
        val=val.replace(x, '-')
    if val.count('-')>val.count('*'):
        cnt += 1
print(cnt)