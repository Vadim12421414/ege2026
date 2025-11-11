s=[]
for n in range(1, 100_000):
    r=f'{n:b}'
    if n%3==0:
        r=r+r[-3:]
    else:
        r=r+f'{n%3*3:b}'
    r=int(r, 2)

    if r<=170:
        s.append(r)
print(max(s))
