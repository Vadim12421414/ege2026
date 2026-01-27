from string import printable as alph


def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
        return res[::-1] if res else '0'


ans = 0
for n in range(0, 100000):
    r = convert(n, 4)
    if r % 2 == 0:
        c = int(r[-1]) * 3
        r = '12' + r + str(c)
    else:
        r = '13' + r + '21'
    r = int(r, 4)
    if r < 50:
        ans.append(r)
print(min(ans))
