from itertools import *
from string import printable
cnt=0
for val in product(printable[:8], repeat=7):
    val=''.join(val)
    if val[0]!='0':
        if not '3' in val:
            if len(set(val))==6:
                if '22' in val or '24' in val or '26' in val or '44' in val or '46' in val or '66' in val:
                    cnt+=1
print(cnt)
