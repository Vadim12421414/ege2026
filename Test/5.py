w=0
ans=[]
def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for n in range(1, 100000):
    r=convert(n, 3)
    if n%3==0:
        r=r+r[-2:]
    else:
        w=r.count('2')*2+r.count('1')
        w=w*3
        w=convert(w, 3)
        r=r+w
    r=int(r, 3)
    if r>208 and r%2!=0:
        ans.append(r)
print(min(ans))

