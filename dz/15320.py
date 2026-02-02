from itertools import *

alph = sorted('парус')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if 'аа' not in val and val.count('У')<=1:
        print(pos)
        break