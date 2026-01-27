from fnmatch import fnmatch

for n in range(12347 - 12347 % 141, 10 ** 8 + 1, 141):
    if fnmatch(str(n), '1234*7'):
        print(n, n // 141)
###############################################################
# 1000000000
# 1234*7
from itertools import *
from string import printable
ans=[]
for l in range(0, 4):
    for z in product(printable[:10], repeat=l):
        num = int('1234' + ''.join(z) + '7')
        if num % 141 == 0 and num < 10 ** 8:
            ans.append([num, num//141])
for i in sorted(ans):
    print(*i)
