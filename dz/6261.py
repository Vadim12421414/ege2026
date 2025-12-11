from itertools import *
from string import printable
cnt=0
for val in product(printable[:10], repeat=8):
    val=''.join(val)
    if val.count('3')==1 and val[0]!=val[1] and val[1]!=val[2] and val[2]!=val[3] and val[0]!='0':
        cnt += 1
print(cnt)