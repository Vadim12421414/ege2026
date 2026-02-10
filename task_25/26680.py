def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True


def fact_3(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i * i < num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    return d


cnt = 0
for i in range(5000_001, 10 ** 20, 2):
    d = fact_3(i)
    if len(d) == len(set(d)) == 2 and is_prime(abs(d[1] - d[0])):
        print(i, d[1])
        cnt += 1
        if cnt == 5:
            break
