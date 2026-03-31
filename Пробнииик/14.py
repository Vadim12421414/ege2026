max_0=0
ans=[]
def convert(num, sys):
    res=''
    while num:
        res+=str(num%sys)
        num//=sys
        return res[::-1]
for x in range(1, 9431):
    numm=convert(39**483+39**235-x, 39)
    print(numm)








