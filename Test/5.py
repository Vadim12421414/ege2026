for n in range(100000):
    r=bin(n)[2:]
    if r.count('1')%2==0:
        r= r+'1'
        r='11'+r[2:]
    else:
        if r.count('0')>r.count('1'):
            r=r+'0'
        else:
            r=r+'1'
    r=int(r, 2)
    if r>271:
        print(n)
        break
