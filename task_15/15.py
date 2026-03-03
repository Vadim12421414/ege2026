from itertools import combinations as com


def f(x):
    b = 24 <= x <= 90
    c = 47 <= x <= 115
    a = a1 <= x <= a2
    return c <= (((not a) and b) <= (not c))


line_x = [24, 47, 90, 115]
line_A = [24.1, 47.1, 90.1, 115.1]
ans = []
for a1, a2 in com(line_x, 2):
    if all(f(x) for x in line_A):
        ans.append(a2 - a1)
print(min(ans))
