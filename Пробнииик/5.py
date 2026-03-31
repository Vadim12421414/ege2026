def convert(num, sys):
    res=''
    while num !=0:
        res=res+str(num%sys)
        num=num//sys
    return res[::-1]
for n in range(1, 100000):
    r=convert(n, 4)
    if n%4==0:
        r=r+r[:2]
    else:
        c=(n%4)*4
        a=convert(c, 4)
        r=r+str(a)
    r=int(r, 4)
    if r>291:
        print(r)
        break

