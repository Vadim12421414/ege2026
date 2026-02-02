def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d.add(i)
            d.add(num // i)
    d_1 = []
    for i in sorted(d):
        if i != 9:
            if i % 10 == 9:
                d_1 += [i]
    if d_1:
        return min(d_1)
    return 0


cnt = 0
for n in range(800001, 10 ** 20):
    m = f(n)
    if m:
        print(n, m)
        cnt += 1
        if cnt == 5:
            break