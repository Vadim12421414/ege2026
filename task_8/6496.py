from itertools import *
cnt=0
for val in product('берск', repeat=6):
    val=''.join(val)
    cnt+=1
print(cnt)