with open(r'files/17_9840.txt') as file:
    data=[int(i) for i in file]
max_39=max(i for i in data if abs(i)%100==39 and len(str(abs(i)))==4)
ans=[]
for num1, num2 in zip(data, data[1:]):
    cnt=0
    for num in num1, num2:
        if len(str(abs(num)))==4:
            cnt+=1
    if cnt==1 and (num1+num2)**2<max_39**2:
        ans.append(num1+num2)
print(len(ans), max(ans))