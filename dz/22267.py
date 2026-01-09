n_1=[]
r_1=[]
def convert(num, sys):
    res=''
    while num:
        res +=str(num%sys)
        num//=sys
        return res[::-1]
for n in range(1, 100000):
    r=convert(n, 7)
    if r[-1]=='2':
        r=r.replace('3', '*')
        r=r.replace('1', '+')
        r=r.replace('*', '1')
        r=r.replace('+', '3')
        r='21'+r
    else:
        r=r+'36'
        r=r[1:]
        r='1'+r
    r=int(r, 7)
    if r==107:
        n_1.append(n)
print(min(n_1))




