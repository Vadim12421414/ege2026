from itertools import *
from string import printable
cnt=0
for val in product(printable[:12], repeat=7):
    val=''.join(val)
    if val[0]!=0:
        new=''
        for i in val:
            if int(i, 12)%3==3:
                new+='*'
            else:
                new+='/'

print(cnt)