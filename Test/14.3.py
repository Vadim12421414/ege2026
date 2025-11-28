def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


max_0 = 0
for x in range(1, 2030):
    num = convert(7 ** 170 + 7 ** 100-x, 7)
    num_0 = num.count('0')
    if max_0 <= num_0:
        max_0 = num_0

        print(x)
