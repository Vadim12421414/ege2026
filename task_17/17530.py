with open(r'files/17_17530.txt') as file:
    data=[int(i) for i in file]
minn=min(i for i in data if i<=min(data))
ans=[]
for num1, num2 in zip(data, data[1:]):
    cnt=0
    for num in num1, num2:
        if num%55==minn:
            cnt+=1
    if cnt>=1:
        ans+=[(num1+num2)]
print(len(ans), min(ans))


