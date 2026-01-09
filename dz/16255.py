from itertools import *
from string import printable
cnt=0
for val in product(range(9), repeat=7):

    if val[0]!=0:
        if val[0]%2==0:
            if val[-1]%3!=0:
                if val.count(6)>=1:
                    cnt+=1
print(cnt)

