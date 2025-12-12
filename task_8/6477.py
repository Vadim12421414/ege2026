from itertools import *
cnt=0
for val in set(permutations('левиоса')):
    val=''.join(val)
    if val[0] not in 'еиоа':
        if val[3] not in 'лвс':
            cnt+=1
print(cnt)