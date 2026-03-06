from itertools import combinations as com


def f(x):
    p = 25 <= x <= 64
    q = 40 <= x <= 115
    a = a1 <= x <= a2
    return p <= ((q and (not a)) <= (not p))


line_x = [25, 40, 64, 115]
line_A = [25.1, 40.1, 64.1, 115.1]
ans = []
for a1, a2 in com(line_x, 2):
    if all(f(x) for x in line_A):
        ans.append(a2 - a1)
print(ans)
