from fnmatch import fnmatch
from itertools import product
from itertools import *


def not_prime(num):
    for i in range(2, int(num ** .5) + 1):  # потенциальные делители
        if num % i == 0:
            return True
    return False  # Составное или нет

#
# all_n = []
# ans = []
# for n in range(4, 10000):
#     if not_prime(n):
#         all_n += [n]
# for n in all_n:
#     num_mask = int(f'1{n}036')
#     for i in range(num_mask - num_mask % 22768, 10 ** 8, 22768):
#         if fnmatch(str(i), f'1{n}03*6*'):
#             ans += [i, n]
# for i in sorted(ans):
#     print(*i)
# -----------------------------------------------------------------------------]
# 2ой способ
ans=[]
for l1 in range(1, 5):#длинна N
    a = 10 ** l1
    s = 10 ** (l1 - 1)
    for n in range(s, a):
        if not_prime(n):
            for l2 in range(0, 4 - l1 + 1):#длинна *(1)
                for z1 in product('0123456789', repeat=l2):
                    z1 = ''.join(z1)
                    for l3 in range(0, 4 - l2 - l1+ 1):#длинна *(2)
                        for z2 in product('0123456789', repeat=l3):
                            z2 = ''.join(z2)
                            num = int(f'1{n}03{z1}6{z2}')
                            if num % 22768 == 0 and num < 10 ** 8:
                                ans.append([num, n])
for i in sorted(ans):
    print(*i)
