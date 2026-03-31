def convert(num, sys):
    res=''
    while num:
        res+=str(num%sys)
        num//=sys
        return res[::-1]
for i in range(1, 111111):
    r=convert(i, 4)
    print(r)