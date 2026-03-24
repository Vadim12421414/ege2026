def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'


ans = []
for n in range(1, 1000):
    r = convert(n, 5)
    if sum(map(int, r)) % 5 == 0:
        r = r.replace('0', '*')
        r = r.replace('1', '0')
        r = r.replace('*', '1')
        r = r + '14'
    else:
        r = r + '33'
        r = '44' + r[2:]
    r = int(r, 5)
    if r > 370:
        ans.append([r, n])

print(min(ans, key=lambda x: (x[0], x[1])))
