from itertools import product
from string import printable
cnt=0
for val in product(printable[:8], repeat=5):
    val = ''.join(val)
    if val[0] not in '01357':
        if int(val[0])%2==0:
            if int(val[-1])!=2 and int(val[-1])!=6:
                if val.count('7')<=2:
                    cnt+=1
print(cnt)

