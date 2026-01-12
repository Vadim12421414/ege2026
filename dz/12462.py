from itertools import *
from string import printable
for val in product(printable[16], repeat=6):
    val=''.join(val)
    if val[0]!='0':
        if len(val)==3 or len(val)==5:
            for i in val:
