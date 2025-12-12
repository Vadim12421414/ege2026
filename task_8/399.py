from itertools import *
cnt=0
for val in set(permutations('ворота', r=6)):
    val=''.join(val)
    for i in 'оа':
        val=val.replace(i, '*')
    if '**' not in val:
        cnt+=1
cnt=0


