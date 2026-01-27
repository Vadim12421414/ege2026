from itertools import combinations as com


def f(x):
    q = 44 <= x <= 50
    p = 43 <= 54
    a = a1 <= x <= a2
    return (a <= p) or q


linea = [43, 44, 49, 53]
linex = [43.1, 45, 50]
ans = []
for a1, a2 in com(linea, 2):
    if all(f(x) for x in linex):
        ans.append(a2 - a1)
print(max(ans))
