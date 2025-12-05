from itertools import *

cnt = 0
for val in product('зеркало', repeat=6):
    val = ''.join(val)
    if val.count('к')<=4 and val.count('к')>0 and val.count('з')<=1 and val.count('е') <=1 and val.count('р') <=1 and val.count('а') <=1 and val.count('л') <=1 and val.count('о') <=1:
        cnt += 1
print(cnt)