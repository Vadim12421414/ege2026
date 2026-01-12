from itertools import *

def f(x):
    m = 32 <= x <= 68
    n = 54 <= x <= 76
    a = a1 <= x <= a2
    return (not(m or n)) == (not a)

linea = [32, 54, 68, 76]
linex = [33, 55, 69]zz

ans = []
for a1, a2 in combinations(linea, 2):
    if all(f(x) for x in linex):
       ans.append(a2-a1)
print(max(ans))