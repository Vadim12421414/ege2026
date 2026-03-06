c=0
ans=[]
for n in range(1, 100000):
    r=bin(n)[2:]
    if n%3==0:
        r=r+r[-3:]
    else:
        c=n%3
        c=c*3
        c=bin(c)[2:]
        r=r+c
    r=int(r, 2)
    ans.append([abs(130-r), n])
print(sorted(ans)[:10])