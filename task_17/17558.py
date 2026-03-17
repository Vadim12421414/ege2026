with open(r'files/17_17558.txt') as file:
    data=[int(i) for i in file]
chisl_32=len([i for i in data if i%32==0])
ans=[]
for num1, num2 in zip(data, data[1:]):
    cnt=0
    for num in num1, num2:
        if num<0:
            cnt+=1
    if cnt>=1 and num1+num2>chisl_32:
        ans+=[(num1+num2)]
print(len(ans), max(ans))