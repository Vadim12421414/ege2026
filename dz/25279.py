from itertools import *


def f(x):
    p = 66 <= x <= 67
    q = 32 <= x <= 125
    t = 30 <= x <= 491
    a = a1 <= x <= a2
    return (not a) <= (p or (not q) or (not t))

linea = [30, 32, 66, 67, 125, 491]
linex = [31, 33, 66.5, 68, 126]

ans = []
for a1, a2 in combinations(linea, 2):
    if all(f(x) for x in linex):
       ans.append(a2-a1)
print(min(ans))
