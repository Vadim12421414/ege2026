from string import printable as alph
def convert2(num, sys):
    res =''
    while num:
        res+=alph[num%sys]
        num//=sys
    return res[::-1]

ans = []
for n in range(1, 100000):
    r = convert2(n, 5)
    if r[-1]=='0':
        r = '33' + r.replace('1', '*').replace('4', '1').replace('*','4')
    else:
        r = '3' + r[1:] + '42'
    r = int(r, 5)
    if r<1922:
        ans.append([r, n])
print(min(ans, key=lambda x: (-x[0], x[1]))[1])