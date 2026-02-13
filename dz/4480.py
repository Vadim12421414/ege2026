from math import *
cnt=0
def f(num):
    d=set()
    for i in range(1, int(num**.5)+1):
        if num%i==0:
            d|={i, num//i}
    if sum(d)%2!=0 and prod(d)%2!=0:
        if len(d)>10:
            return len(d)
        return 0
for i in range(800_000+1, 10**20):
    if m:=f(i):
        cnt+=1
        if cnt==6:
            break
