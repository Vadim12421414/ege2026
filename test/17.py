with open(r'files/') as file:
    data=[int(i) for i in file]
minn=min(i for i in data if len(str(abs(i)))**2)
maxx=max(i for i in data if len(str(abs(i)))==4 and str(i)[-1]=='1')
ans=[]
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    U1=num1>minn
    u2=num2>minn
    u3=num3>minn
