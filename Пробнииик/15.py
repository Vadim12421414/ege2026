from itertools import combinations as com
ans = []


def f(x):
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    a = a1 <= x <= a2
    return p<=((q and (not a)<=(not p)))

line_a = [14, 21, 40, 63]
line_x = [14.1, 21.1, 40.1, 63.1]
for a1, a2 in com(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2 - a1)
print(max(ans))