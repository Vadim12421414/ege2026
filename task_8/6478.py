from itertools import *
cnt=0
for val in product('моль', repeat=5):
    val=''.join(val)
    if 'оь' not in val and 'ьь' not in val and  val[0]!='ь':
        cnt+1
print(cnt)