s=[]
def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for n in range(1, 100000):
    r=convert(n, 7)
    sum_2 = sum(map(int, r))
    if sum_2%2==0:
        r=r+'555'
    else:
        r='33'+r+'6'
    r=int(r, 7)
    if r<12717:
       print(n)
